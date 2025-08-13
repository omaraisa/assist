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
using System.Collections.ObjectModel;
using ArcGIS.Desktop.Framework.Threading.Tasks;


namespace Progent
{
    internal class DockpaneViewModel : DockPane, INotifyPropertyChanged
    {
        private string _serverUrl = "ws://localhost:8000/ws";
        private string _connectButtonText = "Connect";
        private bool _isConnected = false;
        private WebSocketService _webSocketService;

        public ObservableCollection<LogEntry> LogEntries { get; set; } = new ObservableCollection<LogEntry>();

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
                    Log(LogEntryType.Info, "Connecting...");
                    _webSocketService = new WebSocketService(ServerUrl);
                    _webSocketService.OnConnected += async () =>
                    {
                        ConnectButtonText = "Disconnect";
                        _isConnected = true;
                        Log(LogEntryType.Info, "Connected to server.");
                        Process.Start(new ProcessStartInfo("http://localhost:8000") { UseShellExecute = true });
                        await _webSocketService.SendMessageAsync(JsonConvert.SerializeObject(new { type = "client_register", client_type = "arcgis_pro" }));
                    };
                    _webSocketService.OnDisconnected += () =>
                    {
                        ConnectButtonText = "Connect";
                        _isConnected = false;
                        Log(LogEntryType.Info, "Disconnected from server.");
                    };
                    _webSocketService.OnError += (error) =>
                    {
                        Log(LogEntryType.Error, error);
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

                    Log(LogEntryType.FunctionCall, $"Executing: {functionName}", parameters);

                    var pythonResultString = await ExecutePythonScriptAsync(functionName, parameters);
                    var pythonResult = JObject.Parse(pythonResultString);

                    if (pythonResult["status"]?.ToString() == "error")
                    {
                        Log(LogEntryType.Error, $"Function '{functionName}' failed.", pythonResult["message"]?.ToString());
                    }
                    else
                    {
                        Log(LogEntryType.FunctionResult, $"Result for: {functionName}", pythonResult["data"]?.ToString(Formatting.Indented));
                    }

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
                Log(LogEntryType.Error, "Error handling message", ex.Message);
            }
        }

        private async Task<string> ExecutePythonScriptAsync(string functionName, string parameters)
        {
            return await QueuedTask.Run(async () =>
            {
                try
                {
                    // 1. Get path to the add-in's directory, which contains the .pyt file
                    var addinPath = Path.GetDirectoryName(new Uri(Assembly.GetExecutingAssembly().Location).AbsolutePath);
                    addinPath = Uri.UnescapeDataString(addinPath);
                    var toolboxPath = Path.Combine(addinPath, "ProgentTools.pyt");

                    // 2. Find the solution root to locate the 'app' directory
                    var solutionPath = Directory.GetParent(addinPath)?.Parent?.Parent?.Parent?.FullName;
                    if (solutionPath == null || !Directory.Exists(Path.Combine(solutionPath, "app")))
                    {
                        solutionPath = Directory.GetParent(addinPath)?.Parent?.FullName;
                        if (solutionPath == null || !Directory.Exists(Path.Combine(solutionPath, "app")))
                        {
                            throw new DirectoryNotFoundException("Could not find the 'app' directory containing spatial functions.");
                        }
                    }
                    var appPath = Path.Combine(solutionPath, "app");

                    // 3. Set up parameters for the geoprocessing tool
                    var args = Geoprocessing.MakeValueArray(functionName, parameters, appPath);
                    var toolName = $"{toolboxPath}\\progent.ExecuteFunctionTool";

                    // 4. Execute the tool
                    var gpResult = await Geoprocessing.ExecuteToolAsync(toolName, args, null, null, GPExecuteToolFlags.None);

                    // 5. Check for errors
                    if (gpResult.IsFailed)
                    {
                        var errorMessages = string.Join(Environment.NewLine, gpResult.Messages.Select(m => m.Text));
                        Log(LogEntryType.Error, "Geoprocessing tool failed.", errorMessages);
                        return JsonConvert.SerializeObject(new { status = "error", message = errorMessages });
                    }

                    // 6. Get the result from the derived output parameter
                    string resultJson = gpResult.Values[3];
                    if (string.IsNullOrWhiteSpace(resultJson))
                    {
                        return JsonConvert.SerializeObject(new { status = "error", message = "Python tool returned no output." });
                    }

                    return resultJson;
                }
                catch (Exception ex)
                {
                    Log(LogEntryType.Error, "C# Exception in ExecutePythonScriptAsync", ex.ToString());
                    return JsonConvert.SerializeObject(new { status = "error", message = ex.Message });
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
                if (_serverUrl != value)
                {
                    _serverUrl = value;
                    OnPropertyChanged();
                }
            }
        }

        public string ConnectButtonText
        {
            get => _connectButtonText;
            set
            {
                if (_connectButtonText != value)
                {
                    _connectButtonText = value;
                    OnPropertyChanged();
                }
            }
        }

        public ICommand ConnectCommand { get; }

        private void Log(LogEntryType type, string message, string details = "")
        {
            System.Windows.Application.Current.Dispatcher.Invoke(() =>
            {
                LogEntries.Add(new LogEntry { Type = type, Message = message, Details = details, Timestamp = DateTime.Now });
            });
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
