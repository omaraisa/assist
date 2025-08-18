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
using ArcGIS.Desktop.Core.Geoprocessing;

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

                    var pythonResultString = await ExecutePytToolAsync();
                    var pythonResult = JObject.Parse(pythonResultString);

                    var response = new JObject
                    {
                        ["type"] = "function_response",
                        ["session_id"] = sessionId,
                        ["source_client"] = sourceClient,
                        ["status"] = pythonResult["status"],
                        ["function_name"] = "RunPythonCode (test)",
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
                Log($"Error handling message: {ex.Message}");
            }
        }

        private async Task<string> ExecutePytToolAsync()
        {
            try
            {
                var addinAssemblyPath = Path.GetDirectoryName(new Uri(Assembly.GetExecutingAssembly().Location).AbsolutePath);
                var toolboxPath = Path.Combine(Uri.UnescapeDataString(addinAssemblyPath), "progent.pyt");

                Geoprocessing.ImportToolbox(toolboxPath);

                var parameters = Geoprocessing.MakeValueArray();
                var result = await Geoprocessing.ExecuteToolAsync("progent.RunPythonCode", parameters, null, new CancelableProgressorSource().Progressor, GPExecuteToolFlags.Default);

                if (result.IsFailed)
                {
                    var messages = string.Join("\n", result.Messages.Select(m => m.Text));
                    return JsonConvert.SerializeObject(new { status = "error", data = messages });
                }
                else
                {
                    var messages = string.Join("\n", result.Messages.Select(m => m.Text));
                    return JsonConvert.SerializeObject(new { status = "success", data = messages });
                }
            }
            catch (Exception ex)
            {
                return JsonConvert.SerializeObject(new { status = "error", data = ex.ToString() });
            }
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
