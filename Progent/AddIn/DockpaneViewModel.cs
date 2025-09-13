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
using ArcGIS.Desktop.Framework.Threading.Tasks;

namespace Progent
{
    internal class DockpaneViewModel : DockPane, INotifyPropertyChanged
    {
        private string _serverUrl = "ws://localhost:6060/ws";
        private string _logText = "";
        private string _connectButtonText = "Connect";
        private bool _isConnected = false;
        private bool _isBusy = false;
        public bool IsConnected
        {
            get => _isConnected;
            set
            {
                _isConnected = value;
                OnPropertyChanged();
            }
        }
        public bool IsBusy
        {
            get => _isBusy;
            set
            {
                _isBusy = value;
                OnPropertyChanged();
            }
        }
        private WebSocketService _webSocketService;

        public DockpaneViewModel()
        {
            // Set logo based on theme - simple and reliable
            SetThemeAwareLogo();
            ConnectCommand = new RelayCommand(async () =>
            {
                IsBusy = true;
                try
                {
                    if (IsConnected)
                    {
                        await _webSocketService.DisconnectAsync();
                        IsBusy = false;
                    }
                    else
                    {
                        _webSocketService = new WebSocketService(ServerUrl);
                        _webSocketService.OnConnected += async () =>
                        {
                            ConnectButtonText = "Disconnect";
                            IsConnected = true;
                            Log("Connected to server.");
                            Process.Start(new ProcessStartInfo("http://localhost:6060") { UseShellExecute = true });
                            await _webSocketService.SendMessageAsync(JsonConvert.SerializeObject(new { type = "client_register", client_type = "arcgis_pro" }));
                            IsBusy = false;
                        };
                        _webSocketService.OnDisconnected += () =>
                        {
                            ConnectButtonText = "Connect";
                            IsConnected = false;
                            Log("Disconnected from server.");
                            IsBusy = false;
                        };
                        _webSocketService.OnError += (error) =>
                        {
                            Log(error);
                            ConnectButtonText = "Connect";
                            IsConnected = false;
                            IsBusy = false;
                        };
                        _webSocketService.OnMessageReceived += HandleMessageReceived;
                        await _webSocketService.ConnectAsync();
                    }
                }
                catch (Exception ex)
                {
                    Log($"Error in connect command: {ex.Message}");
                    IsBusy = false;
                }
            }, () => !IsBusy);
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

                        var pythonResultString = await ExecutePytToolAsync(functionName, parameters);
                        // If the tool returned a JSON message, prefer parsing that; otherwise parse the wrapper
                        JObject pythonResult;
                        try
                        {
                            pythonResult = JObject.Parse(pythonResultString);
                            // If data is a JSON string, try to parse it into an object
                            var dataToken = pythonResult["data"];
                            if (dataToken != null && dataToken.Type == JTokenType.String)
                            {
                                var dataText = dataToken.ToString().Trim();
                                if (dataText.StartsWith("{") || dataText.StartsWith("["))
                                {
                                    try { pythonResult["data"] = JObject.Parse(dataText); }
                                    catch { /* leave as string or array */ }
                                }
                            }
                        }
                        catch
                        {
                            // fallback: embed raw string
                            pythonResult = new JObject { ["status"] = "error", ["data"] = pythonResultString };
                        }

                    var data = pythonResult["data"];
                        bool isDashboardUpdate = (data is JObject dataObj) && dataObj.Value<bool>("is_dashboard_update");

                        if (isDashboardUpdate)
                        {
                            var dashboardUpdate = new JObject
                            {
                                ["type"] = "dashboard_update",
                                ["session_id"] = sessionId,
                                ["source_client"] = sourceClient,
                                ["data"] = data
                            };
                            await _webSocketService.SendMessageAsync(dashboardUpdate.ToString());

                            var ackResponse = new JObject
                            {
                                ["type"] = "function_response",
                                ["session_id"] = sessionId,
                                ["source_client"] = sourceClient,
                                ["status"] = "success",
                                ["function_name"] = functionName,
                                ["data"] = new JObject { ["message"] = "Dashboard layout generated and updated." }
                            };
                            await _webSocketService.SendMessageAsync(ackResponse.ToString());
                        }
                        else
                        {
                            var response = new JObject
                            {
                                ["type"] = "function_response",
                                ["session_id"] = sessionId,
                                ["source_client"] = sourceClient,
                                ["status"] = pythonResult["status"],
                                ["function_name"] = functionName ?? "RunPythonCode",
                                ["data"] = data,
                                ["software_context"] = await GetSoftwareContext()
                            };
                            await _webSocketService.SendMessageAsync(response.ToString());
                        }
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

    private async Task<string> ExecutePytToolAsync(string functionName, string parametersJson)
        {
            try
            {
                var addinAssemblyPath = Path.GetDirectoryName(new Uri(Assembly.GetExecutingAssembly().Location).AbsolutePath);
                // Resolve the expected .pyt toolbox path next to the add-in assembly
                var toolboxPath = Path.Combine(Uri.UnescapeDataString(addinAssemblyPath), "progent.pyt");

                // Build the fully-qualified tool reference for ExecuteToolAsync (pyt tool referenced by full path)
                var toolReference = Path.Combine(toolboxPath, "RunPythonCode");

                // Diagnostic logging: resolved paths and toolbox presence
                Log($"Resolved add-in assembly path: {addinAssemblyPath}");
                Log($"Resolved toolbox path: {toolboxPath}");
                Log($"Tool reference used for ExecuteToolAsync: {toolReference}");
                Log($"Toolbox file exists: {File.Exists(toolboxPath)}; toolbox directory exists: {Directory.Exists(toolboxPath)}");

                // Defensive: ensure toolbox exists and log helpful message if not
                if (!File.Exists(toolboxPath) && !Directory.Exists(toolboxPath))
                {
                    var missingMsg = $"Toolbox not found at '{toolboxPath}'. Make sure 'progent.pyt' is deployed with the add-in.";
                    Log(missingMsg);
                    return JsonConvert.SerializeObject(new { status = "error", data = missingMsg });
                }

                // Pass the function name and parameters JSON to the script tool as arguments
                var parameters = Geoprocessing.MakeValueArray(functionName, parametersJson);
                var result = await Geoprocessing.ExecuteToolAsync(toolReference, parameters, null, new CancelableProgressorSource().Progressor, GPExecuteToolFlags.Default);

                // Log detailed GP result information for troubleshooting
                try
                {
                    var msgs = result.Messages.Select(m => $"[{m.Type}] {m.Text}");
                    var msgsList = string.Join("\n", msgs);
                    Log($"Geoprocessing result - IsFailed: {result.IsFailed}; Messages count: {result.Messages.Count()}");
                    if (!string.IsNullOrEmpty(msgsList))
                        Log($"Geoprocessing messages:\n{msgsList}");
                    else
                        Log("Geoprocessing returned no messages.");
                }
                catch (Exception exMsg)
                {
                    Log($"Error while logging GP messages: {exMsg}");
                }

                // If the script tool emitted a JSON message, prefer returning that JSON directly
                foreach (var m in result.Messages)
                {
                    var text = m.Text?.Trim();
                    if (!string.IsNullOrEmpty(text) && (text.StartsWith("{") || text.StartsWith("[")))
                    {
                        // assume this is the JSON payload from the script tool
                        return text;
                    }
                }

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
                foreach(var layer in activeMap.GetLayersAsFlattenedList())
                {
                    var layerInfo = new JObject
                    {
                        ["visible"] = layer.IsVisible,
                        ["layer_type"] = layer.GetType().Name
                    };

                    // Handle different layer types
                    if (layer is ArcGIS.Desktop.Mapping.FeatureLayer featureLayer)
                    {
                        layerInfo["definition_query"] = featureLayer.DefinitionQuery;
                        var fields = new JObject();
                        try
                        {
                            foreach(var field in featureLayer.GetFeatureClass().GetDefinition().GetFields())
                            {
                                fields[field.Name] = field.FieldType.ToString();
                            }
                        }
                        catch (Exception ex)
                        {
                            // Some feature layers might not have accessible fields
                            fields["error"] = $"Unable to access fields: {ex.Message}";
                        }
                        layerInfo["fields"] = fields;
                        layerInfo["geometry_type"] = featureLayer.ShapeType.ToString();
                    }
                    else if (layer is ArcGIS.Desktop.Mapping.RasterLayer rasterLayer)
                    {
                        layerInfo["data_type"] = "Raster";
                        // Raster layers don't have traditional fields, but we can include basic info
                        layerInfo["fields"] = new JObject(); // Empty for rasters
                    }
                    else
                    {
                        // Other layer types (group layers, etc.)
                        layerInfo["data_type"] = "Other";
                        layerInfo["fields"] = new JObject();
                    }

                    layersInfo[layer.Name] = layerInfo;
                }
                context["layers_info"] = layersInfo;

                // Include standalone tables in the layers_info as well for consistency
                foreach(var table in activeMap.GetStandaloneTablesAsFlattenedList())
                {
                    var tableInfo = new JObject
                    {
                        ["visible"] = true, // Tables are typically always "visible" in the table of contents
                        ["layer_type"] = "StandaloneTable",
                        ["data_type"] = "Table",
                        ["fields"] = new JObject()
                    };

                    // Try to get table fields
                    try
                    {
                        var tableFields = new JObject();
                        // For standalone tables, we need to use a different approach
                        var tableDef = table.GetTable().GetDefinition();
                        foreach(var field in tableDef.GetFields())
                        {
                            tableFields[field.Name] = field.FieldType.ToString();
                        }
                        tableInfo["fields"] = tableFields;
                    }
                    catch (Exception ex)
                    {
                        tableInfo["fields"] = new JObject { ["error"] = $"Unable to access fields: {ex.Message}" };
                    }

                    layersInfo[table.Name] = tableInfo;
                }

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

        private void SetThemeAwareLogo()
        {
            try
            {
                var app = System.Windows.Application.Current;
                if (app?.Resources == null) return;

                // Check if we're in dark theme by looking at background brush
                bool isDarkTheme = false;
                if (app.Resources.Contains("Esri_BackgroundBrush"))
                {
                    var brush = app.Resources["Esri_BackgroundBrush"] as System.Windows.Media.SolidColorBrush;
                    if (brush != null)
                    {
                        var color = brush.Color;
                        var brightness = (color.R * 0.299 + color.G * 0.587 + color.B * 0.114);
                        isDarkTheme = brightness < 128;
                    }
                }

                // Use bright logo for dark theme, regular logo for light theme
                var logoPath = isDarkTheme ? "/Progent;component/Images/logo-bright.png" : "/Progent;component/Images/logo.png";
                var uri = new Uri($"pack://application:,,,{logoPath}", UriKind.Absolute);
                var bitmap = new System.Windows.Media.Imaging.BitmapImage(uri);
                
                app.Resources["ProgentLogo"] = bitmap;
            }
            catch
            {
                // If anything fails, silently continue - logo just won't show
            }
        }

        public event PropertyChangedEventHandler PropertyChanged;

        protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
