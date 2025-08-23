using System;
using System.Net.WebSockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Progent
{
    internal class WebSocketService
    {
        private ClientWebSocket _client;
        private readonly Uri _uri;
        private CancellationTokenSource _cancellationTokenSource;
        private int _maxRetries = 5;
        private int _retryDelay = 1000;

        public event Action<string> OnMessageReceived;
        public event Action OnConnected;
        public event Action OnDisconnected;
        public event Action<string> OnError;

        public WebSocketService(string url)
        {
            _uri = new Uri(url);
        }

        public async Task ConnectAsync()
        {
            if (_client?.State == WebSocketState.Open)
            {
                return;
            }
            _cancellationTokenSource = new CancellationTokenSource();
            await ConnectWithRetriesAsync();
        }

        private async Task ConnectWithRetriesAsync()
        {
            int attempt = 0;
            while (attempt < _maxRetries && !_cancellationTokenSource.IsCancellationRequested)
            {
                try
                {
                    _client = new ClientWebSocket();
                    await _client.ConnectAsync(_uri, _cancellationTokenSource.Token);
                    OnConnected?.Invoke();
                    _ = Task.Run(ReceiveLoop);
                    return;
                }
                catch (Exception ex)
                {
                    OnError?.Invoke($"Connection attempt {attempt + 1} failed: {ex.Message}");
                    attempt++;
                    await Task.Delay(_retryDelay * attempt);
                }
            }
            OnError?.Invoke("Failed to connect after multiple attempts.");
            OnDisconnected?.Invoke();
        }


        public async Task DisconnectAsync()
        {
            _cancellationTokenSource?.Cancel();
            if (_client?.State == WebSocketState.Open)
            {
                await _client.CloseAsync(WebSocketCloseStatus.NormalClosure, "Closing", CancellationToken.None);
            }
            OnDisconnected?.Invoke();
        }

        public async Task SendMessageAsync(string message)
        {
            if (_client?.State != WebSocketState.Open)
            {
                throw new InvalidOperationException("WebSocket is not connected.");
            }

            var buffer = new ArraySegment<byte>(Encoding.UTF8.GetBytes(message));
            await _client.SendAsync(buffer, WebSocketMessageType.Text, true, _cancellationTokenSource.Token);
        }

        private async Task ReceiveLoop()
        {
            var buffer = new byte[1024 * 1024]; // 1MB buffer
            try
            {
                while (_client.State == WebSocketState.Open && !_cancellationTokenSource.IsCancellationRequested)
                {
                    var result = await _client.ReceiveAsync(new ArraySegment<byte>(buffer), _cancellationTokenSource.Token);
                    if (result.MessageType == WebSocketMessageType.Text)
                    {
                        var message = Encoding.UTF8.GetString(buffer, 0, result.Count);
                        OnMessageReceived?.Invoke(message);
                    }
                    else if (result.MessageType == WebSocketMessageType.Close)
                    {
                        break;
                    }
                }
            }
            catch (WebSocketException ex)
            {
                OnError?.Invoke($"WebSocket error: {ex.Message}. Attempting to reconnect...");
                _ = ConnectWithRetriesAsync();
            }
            catch (Exception ex)
            {
                OnError?.Invoke($"Error in receive loop: {ex.Message}");
            }
            finally
            {
                if (!_cancellationTokenSource.IsCancellationRequested)
                {
                    OnDisconnected?.Invoke();
                }
            }
        }
    }
}
