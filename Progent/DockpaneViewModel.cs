using System;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;
using ArcGIS.Desktop.Framework;
using ArcGIS.Desktop.Framework.Contracts;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using ArcGIS.Desktop.Mapping;
using ArcGIS.Desktop.Core;
using System.Linq;
using System.Collections.Generic;
using ArcGIS.Desktop.Framework.Threading.Tasks;

namespace Progent
{
    internal class DockpaneViewModel : DockPane, INotifyPropertyChanged
    {
        private string _serverUrl = "ws://localhost:8000/ws";
        private string _logText = "";
        private string _connectButtonText = "Connect";
        private bool _isConnected = false;
        private WebSocketService _webSocketService;

        public DockpaneViewModel()
        {
            ConnectCommand = new RelayCommand(async () =>
            {
                if (_isConnected)
                {
                    await _webSocketService.DisconnectAsync();
                }
                else
                {
                    _webSocketService = new WebSocketService(ServerUrl);
                    _webSocketService.OnConnected += async () =>
                    {
                        ConnectButtonText = "Disconnect";
                        _isConnected = true;
                        Log("Connected to server.");
                        Process.Start(new ProcessStartInfo("http://localhost:8000") { UseShellExecute = true });
                        await _webSocketService.SendMessageAsync(JsonConvert.SerializeObject(new { type = "client_register", client_type = "arcgis_pro" }));
                    };
                    _webSocketService.OnDisconnected += () =>
                    {
                        ConnectButtonText = "Connect";
                        _isConnected = false;
                        Log("Disconnected from server.");
                    };
                    _webSocketService.OnError += (error) =>
                    {
                        Log(error);
                        ConnectButtonText = "Connect";
                        _isConnected = false;
                    };
                    _webSocketService.OnMessageReceived += HandleMessageReceived;
                    await _webSocketService.ConnectAsync();
                }
            });
        }

        private async void HandleMessageReceived(string message)
        {
            Log($"Received: {message}");
            try
            {
                var json = JObject.Parse(message);
                var type = json["type"]?.ToString();

                if (type == "execute_function")
                {
                    var functionName = json["function_name"]?.ToString();
                    var parameters = json["parameters"]?.ToString() ?? "{}";
                    var sessionId = json["session_id"]?.ToString();
                    var sourceClient = json["source_client"]?.ToString();

                    var pythonResultString = await ExecutePythonScriptAsync(functionName, parameters);
                    // Log raw python output to help trace errors during execution
                    Log($"Python result raw: {pythonResultString}");
                    var pythonResult = JObject.Parse(pythonResultString);

                    var response = new JObject
                    {
                        ["type"] = "function_response",
                        ["session_id"] = sessionId,
                        ["source_client"] = sourceClient,
                        ["status"] = pythonResult["status"],
                        ["function_name"] = functionName,
                        ["data"] = pythonResult["data"],
                        ["software_context"] = await GetSoftwareContext()
                    };

                    // If python returned an error payload, forward the message/traceback to the server
                    if (pythonResult["message"] != null)
                    {
                        response["message"] = pythonResult["message"];
                    }
                    if (pythonResult["traceback"] != null)
                    {
                        response["traceback"] = pythonResult["traceback"];
                    }

                    await _webSocketService.SendMessageAsync(response.ToString());
                }
                else if (type == "get_software_state")
                {
                    var response = new JObject
                    {
                        ["type"] = "software_state",
                        ["data"] = await GetSoftwareContext()
                    };
                    await _webSocketService.SendMessageAsync(response.ToString());
                }
                else if (type == "heartbeat")
                {
                    await _webSocketService.SendMessageAsync(JsonConvert.SerializeObject(new { type = "heartbeat_ack" }));
                }
            }
            catch (Exception ex)
            {
                Log($"Error handling message: {ex.Message}");
            }
        }

        private Task<string> ExecutePythonScriptAsync(string functionName, string parameters)
        {
            return Task.Run(() =>
            {
                var pathProExe = Path.GetDirectoryName(new Uri(Assembly.GetEntryAssembly().Location).AbsolutePath);
                pathProExe = Uri.UnescapeDataString(pathProExe);
                pathProExe = Path.Combine(pathProExe, @"Python\envs\arcgispro-py3");

                var pathPython = Path.GetDirectoryName(new Uri(Assembly.GetExecutingAssembly().Location).AbsolutePath);
                pathPython = Uri.UnescapeDataString(pathPython);

                var scriptPath = Path.Combine(pathPython, "progent_execute.py");

                // Ensure spatial_functions.py is available in the same directory as progent_execute.py
                var spatialFunctionsSource = Path.Combine(pathPython, "spatial_functions.py");
                var spatialFunctionsTarget = Path.Combine(Path.GetDirectoryName(scriptPath), "spatial_functions.py");
                
                if (File.Exists(spatialFunctionsSource) && !File.Exists(spatialFunctionsTarget))
                {
                    try
                    {
                        File.Copy(spatialFunctionsSource, spatialFunctionsTarget, overwrite: true);
                        Log($"Copied spatial_functions.py to: {spatialFunctionsTarget}");
                    }
                    catch (Exception ex)
                    {
                        Log($"Warning: Could not copy spatial_functions.py: {ex.Message}");
                    }
                }

                // Write parameters to temp file to avoid quoting/escaping issues
                var tempParamsPath = Path.Combine(Path.GetTempPath(), $"progent_params_{Guid.NewGuid().ToString()}.json");
                File.WriteAllText(tempParamsPath, parameters);

                var pythonExePath = Path.Combine(pathProExe, "python.exe");

                var procStartInfo = new ProcessStartInfo
                {
                    FileName = pythonExePath,
                    Arguments = $"\"{scriptPath}\" --paramsfile \"{tempParamsPath}\"",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                var proc = new Process { StartInfo = procStartInfo };
                try
                {
                    proc.Start();

                    string result = proc.StandardOutput.ReadToEnd();
                    string error = proc.StandardError.ReadToEnd();
                    proc.WaitForExit();

                    if (!string.IsNullOrEmpty(error))
                    {
                        // Return well-formed JSON so the caller can parse and forward message/traceback
                        return JsonConvert.SerializeObject(new { status = "error", message = error });
                    }

                    return result;
                }
                finally
                {
                    // Cleanup temp params file
                    try { if (File.Exists(tempParamsPath)) File.Delete(tempParamsPath); } catch { }
                }
            });
        }

        private Task<JObject> GetSoftwareContext()
        {
            return QueuedTask.Run(() =>
            {
                var context = new JObject();
                var project = Project.Current;
                var activeMap = MapView.Active?.Map;

                if (project == null || activeMap == null)
                {
                    context["error"] = "No active map found";
                    return context;
                }

                context["project_path"] = project.Path;
                context["default_gdb"] = project.DefaultGeodatabasePath;
                context["map_name"] = activeMap.Name;

                var layersInfo = new JObject();
                foreach(var layer in activeMap.GetLayersAsFlattenedList().OfType<FeatureLayer>())
                {
                    var layerInfo = new JObject
                    {
                        ["definition_query"] = layer.DefinitionQuery,
                        ["visible"] = layer.IsVisible
                    };
                    var fields = new JObject();
                    foreach(var field in layer.GetFeatureClass().GetDefinition().GetFields())
                    {
                        fields[field.Name] = field.FieldType.ToString();
                    }
                    layerInfo["fields"] = fields;
                    layersInfo[layer.Name] = layerInfo;
                }
                context["layers_info"] = layersInfo;

                var tablesInfo = new JObject();
                foreach(var table in activeMap.GetStandaloneTablesAsFlattenedList())
                {
                    tablesInfo[table.Name] = new JObject { ["name"] = table.Name };
                }
                context["tables_info"] = tablesInfo;

                return context;
            });
        }


        public string ServerUrl
        {
            get => _serverUrl;
            set
            {
                _serverUrl = value;
                OnPropertyChanged();
            }
        }

        public string LogText
        {
            get => _logText;
            set
            {
                _logText = value;
                OnPropertyChanged();
            }
        }

        public string ConnectButtonText
        {
            get => _connectButtonText;
            set
            {
                _connectButtonText = value;
                OnPropertyChanged();
            }
        }

        public ICommand ConnectCommand { get; }

        private void Log(string message)
        {
            LogText += $"{DateTime.Now:T} - {message}{Environment.NewLine}";
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
