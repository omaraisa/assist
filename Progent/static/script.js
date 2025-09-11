class SmartAssistantClient {
    constructor() {
        this.ws = null;
        this.clientId = null;
        this.currentModel = 'GEMINI_FLASH';
        this.isConnected = false;
        this.conversationHistory = [];
        this.isThinking = false;
        this.isCancelled = false; // Flag to ignore responses after cancellation
        this.isRecognizing = false;
        
        this.initializeElements();
        this.setupEventListeners();
        this.setupVoiceRecognition();
        this.connect();
    }
    
    initializeElements() {
        this.elements = {
            chatMessages: document.getElementById('chat-messages'),
            userInput: document.getElementById('user-input'),
            sendBtn: document.getElementById('send-btn'),
            chatForm: document.getElementById('chat-form'),
            connectionStatus: document.getElementById('connection-status'),
            modelSelect: document.getElementById('ai-model-select'),
            apiKeyBtn: document.getElementById('api-key-btn'),
            apiKeySection: document.getElementById('api-key-section'),
            apiKeyInput: document.getElementById('api-key-input'),
            saveApiKeyBtn: document.getElementById('save-api-key-btn'),
            loadingIndicator: document.getElementById('loading-indicator'),
            // Dashboard elements
            dashboardPanel: document.getElementById('dashboard-panel'),
            dashboardGrid: document.getElementById('dashboard-grid'),
            toggleDashboard: document.getElementById('toggle-dashboard'),
            refreshDashboard: document.getElementById('refresh-dashboard'),
            viewDashboardBtn: document.getElementById('view-dashboard-btn'),
            voiceBtn: document.getElementById('voice-btn')
        };
        
        // Initialize dashboard
        this.dashboard = new DashboardRenderer(this.elements.dashboardGrid);
        
        // Check for existing dashboard data on init
        this.checkInitialDashboardData();
    }
    
    async checkInitialDashboardData() {
        try {
            const response = await fetch('/api/dashboard/latest');
            if (response.ok) {
                const dashboardData = await response.json();
                if (!dashboardData.error) {
                    this.dashboard.render(dashboardData);
                    this.showViewDashboardButton();
                    // Don't auto-show on page load, user should manually show or it will appear when new data comes
                } else {
                    this.dashboard.showPlaceholder();
                }
            }
        } catch (error) {
            console.log('No existing dashboard data found');
            this.dashboard.showPlaceholder();
        }
    }
    
    setupEventListeners() {
        // Form submission
        this.elements.chatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.sendMessage();
        });
        
        // Enter key handling
        this.elements.userInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
            
            // Auto-resize textarea
            this.autoResizeTextarea(e.target);
        });
        
        // Model selection
        this.elements.modelSelect.addEventListener('change', (e) => {
            this.changeModel(e.target.value);
        });
        
        // API key management
        this.elements.apiKeyBtn.addEventListener('click', () => {
            const section = this.elements.apiKeySection;
            section.style.display = section.style.display === 'none' ? 'flex' : 'none';
        });

        this.elements.saveApiKeyBtn.addEventListener('click', () => {
            this.saveApiKeyAndUpdate();
        });
        
        // Dashboard controls
        this.elements.toggleDashboard.addEventListener('click', () => {
            this.toggleDashboard();
        });
        
        this.elements.refreshDashboard.addEventListener('click', () => {
            this.refreshDashboard();
        });
        
        this.elements.viewDashboardBtn.addEventListener('click', () => {
            this.showDashboard();
        });
        
        // Voice recognition
        this.elements.voiceBtn.addEventListener('click', () => {
            this.toggleVoiceRecognition();
        });
    }
    
    autoResizeTextarea(textarea) {
        textarea.style.height = 'auto';
        textarea.style.height = Math.min(textarea.scrollHeight, 120) + 'px';
    }
    
    async connect() {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${protocol}//${window.location.host}/ws`;
        
        try {
            this.ws = new WebSocket(wsUrl);
            
            this.ws.onopen = () => {
                console.log('Connected to server');
                this.isConnected = true;
                this.updateConnectionStatus('Connected', 'success');
                
                // Register as chatbot client
                this.sendWebSocketMessage({
                    type: 'client_register',
                    client_type: 'chatbot'
                });
                
                // Enable input
                this.elements.userInput.disabled = false;
                this.elements.sendBtn.disabled = false;
                this.elements.userInput.placeholder = 'Type your message...';
            };
            
            this.ws.onmessage = (event) => {
                const message = JSON.parse(event.data);
                this.handleMessage(message);
            };
            
            this.ws.onclose = () => {
                console.log('Disconnected from server');
                this.isConnected = false;
                this.updateConnectionStatus('Disconnected', 'error');
                
                // Disable input
                this.elements.userInput.disabled = true;
                this.elements.sendBtn.disabled = true;
                this.elements.userInput.placeholder = 'Reconnecting...';
                
                // Attempt to reconnect after 3 seconds
                setTimeout(() => this.connect(), 3000);
            };
            
            this.ws.onerror = (error) => {
                console.error('WebSocket error:', error);
                this.updateConnectionStatus('Connection Error', 'error');
            };
            
        } catch (error) {
            console.error('Failed to connect:', error);
            this.updateConnectionStatus('Connection Failed', 'error');
            setTimeout(() => this.connect(), 5000);
        }
    }
    
    sendWebSocketMessage(message) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(message));
        } else {
            console.error('WebSocket is not connected');
        }
    }
    
    handleMessage(message) {
        console.log('Received message:', message);
        
        // If we've cancelled and receive an assistant response, ignore it
        if (this.isCancelled && (message.type === 'assistant_message' || message.type === 'function_result')) {
            console.log('Ignoring response after cancellation:', message.type);
            return;
        }
        
        switch (message.type) {
            case 'config':
                this.handleConfigMessage(message.data);
                break;
                
            case 'assistant_message':
                this.addMessage('Progent', message.content, 'bot');
                this.setThinkingState(false);
                break;
                
            case 'function_result':
                // Handle direct function results if needed
                console.log('Function result:', message.data);
                break;
                
            case 'software_state_updated':
                console.log('ArcGIS Pro state updated:', message.data);
                break;
                
            case 'dashboard_update':
                this.handleDashboardUpdate(message.data);
                break;
                
            case 'error':
                this.addMessage('System', `Error: ${message.message}`, 'error');
                this.setThinkingState(false);
                break;
                
            case 'cancelled':
                // Server confirmed cancellation - show message and clear cancel flag
                this.addMessage('System', 'Request cancelled', 'system');
                this.isCancelled = false; // Reset the flag
                console.log('Server confirmed cancellation:', message.message);
                break;
                
            case 'model_changed':
                this.handleModelChanged(message);
                break;
                
            case 'heartbeat_ack':
                // Handle heartbeat acknowledgment
                break;
                
            default:
                console.warn('Unknown message type:', message.type);
        }
    }
    
    handleConfigMessage(config) {
        // Update available models
        if (config.ai_models) {
            this.updateModelOptions(config.ai_models);
        }
        
        // Set current model
        if (config.current_model) {
            this.currentModel = config.current_model;
            this.elements.modelSelect.value = config.current_model;
        }
        
        console.log('Configuration updated:', config);
    }
    
    updateModelOptions(models) {
        const select = this.elements.modelSelect;
        select.innerHTML = '';
        
        // Store models locally for later visibility checks
        this.availableModels = models;

        for (const [key, model] of Object.entries(models)) {
            const option = document.createElement('option');
            option.value = key;
            option.textContent = model.name;
            // Attach api_key_env as data attribute if present
            if (model.api_key_env) {
                option.dataset.apiKeyEnv = model.api_key_env;
            }
            select.appendChild(option);
        }

        // Ensure API key section visibility reflects the current model
        this.toggleApiKeySection();
    }

    // Show or hide the API key section depending on the selected model
    toggleApiKeySection() {
        const select = this.elements.modelSelect;
        const section = this.elements.apiKeySection;
        if (!select || !section || !this.availableModels) return;

        const modelKey = select.value || this.currentModel;
        const model = this.availableModels ? this.availableModels[modelKey] : null;

        // Only hide if model doesn't require API key, don't auto-show
        if (!model || !model.api_key_env) {
            section.style.display = 'none';
        }
        // Don't auto-show - let the user click the key button to show it
    }
    
    sendMessage() {
        // If currently thinking, cancel the request instead of sending
        if (this.isThinking) {
            this.cancelRequest();
            return;
        }

        const message = this.elements.userInput.value.trim();
        if (!message || !this.isConnected) return;
        
        // Clear any previous cancellation flag when starting new request
        this.isCancelled = false;
        
        // Add user message to UI
        this.addMessage('You', message, 'user');
        
        // Clear input
        this.elements.userInput.value = '';
        this.autoResizeTextarea(this.elements.userInput);
        
        // Set thinking state
        this.setThinkingState(true);
        
        // Send to server
        this.sendWebSocketMessage({
            type: 'user_message',
            content: message,
            model: this.currentModel
        });
        
        // Add to conversation history
        this.conversationHistory.push({
            role: 'user',
            content: message,
            timestamp: new Date().toISOString()
        });
    }
    
    addMessage(sender, content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `msg ${type}-msg`;
        
        const timestamp = new Date().toLocaleTimeString([], {
            hour: '2-digit',
            minute: '2-digit'
        });
        
        let messageClass = 'msg-bubble';
        if (type === 'error') {
            messageClass += ' error-message';
        }
        
        messageDiv.innerHTML = `
            <div class="${messageClass}">
                <div class="msg-info">
                    <div class="msg-info-name">${sender}</div>
                    <div class="msg-info-time">${timestamp}</div>
                </div>
                <div class="msg-text">${this.formatMessage(content)}</div>
            </div>
        `;
        
        // Remove welcome message if it exists
        const welcomeMessage = this.elements.chatMessages.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }
        
        this.elements.chatMessages.appendChild(messageDiv);
        this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
        
        // Add to conversation history for assistant messages
        if (type === 'bot') {
            this.conversationHistory.push({
                role: 'assistant',
                content: content,
                timestamp: new Date().toISOString()
            });
        }
    }
    
    formatMessage(content) {
        // Basic formatting - convert line breaks to <br>
        return content
            .replace(/\n/g, '<br>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>');
    }
    
    updateConnectionStatus(status, type) {
        this.elements.connectionStatus.textContent = status;
        this.elements.connectionStatus.className = `status-${type === 'success' ? 'connected' : 'disconnected'}`;
        
        // Update button and input states based on connection
        if (type === 'success') {
            this.elements.userInput.disabled = false;
            // Button is always enabled when connected
            this.elements.sendBtn.disabled = false;
        } else {
            this.elements.userInput.disabled = true;
            // Button is disabled only when disconnected AND not thinking
            this.elements.sendBtn.disabled = !this.isThinking;
        }
    }
    
    changeModel(modelKey) {
        this.currentModel = modelKey;
        console.log(`Model changed to: ${modelKey}`);
        
        // Send model change to server
        this.sendWebSocketMessage({
            type: 'change_model',
            model: modelKey
        });
        
        this.toggleApiKeySection();
    }
    
    async saveApiKeyAndUpdate() {
        const apiKey = this.elements.apiKeyInput.value.trim();
        if (!apiKey) {
            this.showNotification('Please enter an API key.', 'error');
            return;
        }

        try {
            const response = await fetch('/api/update_api_key', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    model_key: this.currentModel,
                    api_key: apiKey,
                }),
            });

            const result = await response.json();

            if (result.success) {
                this.showNotification('API key saved successfully! The model is now ready.', 'success');
                this.elements.apiKeySection.style.display = 'none';
                this.elements.apiKeyInput.value = '';
            } else {
                this.showNotification(`Error: ${result.message}`, 'error');
            }
        } catch (error) {
            console.error('Failed to save API key:', error);
            this.showNotification('An unexpected error occurred while saving the API key.', 'error');
        }
    }

    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
    
    showLoading() {
        this.elements.loadingIndicator.style.display = 'flex';
    }
    
    hideLoading() {
        this.elements.loadingIndicator.style.display = 'none';
    }
    
    setThinkingState(thinking) {
        this.isThinking = thinking;
        if (thinking) {
            this.showLoading();
            // Use a stop/square icon when thinking
            this.elements.sendBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
                    <rect x="6" y="6" width="12" height="12" rx="2"/>
                </svg>
            `;
            this.elements.sendBtn.setAttribute('aria-label', 'Stop');
            this.elements.sendBtn.classList.add('stop-mode');
            this.elements.userInput.disabled = true;
        } else {
            this.hideLoading();
            // Use send/arrow icon when not thinking
            this.elements.sendBtn.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                    <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
                </svg>
            `;
            this.elements.sendBtn.setAttribute('aria-label', 'Send Message');
            this.elements.sendBtn.classList.remove('stop-mode');
            this.elements.userInput.disabled = !this.isConnected;
        }
        // Button is always enabled - user can send when connected or stop when thinking
        this.elements.sendBtn.disabled = false;
    }
    
    cancelRequest() {
        // Set cancellation flag to ignore upcoming responses
        this.isCancelled = true;
        
        // Send cancel request to server
        this.sendWebSocketMessage({
            type: 'cancel_request'
        });
        
        // Immediately restore UI state - don't wait for server response
        this.setThinkingState(false);
    }
    
    // Public methods for debugging
    getConnectionStatus() {
        return {
            connected: this.isConnected,
            currentModel: this.currentModel,
            historyLength: this.conversationHistory.length
        };
    }
    
    clearHistory() {
        this.conversationHistory = [];
        this.elements.chatMessages.innerHTML = `
            <div class="welcome-message">
                <h3>Hi there,</h3>
                <p>I can help you analyze your GIS data, run spatial functions, and provide insights about your ArcGIS Pro project.</p>
                <p>Just type your question or request below, and I'll investigate your data to provide helpful answers.</p>
            </div>
        `;
        console.log('Conversation history cleared');
    }
    
    handleModelChanged(message) {
        console.log('Model changed:', message);
        
        // Update the current model
        this.currentModel = message.model;
        
        // Update the dropdown selection
        this.elements.modelSelect.value = message.model;
        
        // Show confirmation message
        this.addMessage('System', `AI model changed to: ${message.model_name}`, 'info');
        
        // Update API key section visibility
        this.toggleApiKeySection();
    }
    
    // Dashboard methods
    toggleDashboard() {
        const panel = this.elements.dashboardPanel;
        const button = this.elements.toggleDashboard;
        const appLayout = document.querySelector('.app-layout');
        
        if (panel.classList.contains('active')) {
            panel.classList.remove('active');
            appLayout.classList.remove('dashboard-active');
            button.textContent = 'Show';
            // Show view dashboard button when dashboard is hidden
            if (this.dashboard && this.dashboard.currentData) {
                this.showViewDashboardButton();
            }
        } else {
            panel.classList.add('active');
            appLayout.classList.add('dashboard-active');
            button.textContent = 'Hide';
            this.hideViewDashboardButton();
        }
    }
    
    async refreshDashboard() {
        try {
            const response = await fetch('/api/dashboard/latest');
            if (response.ok) {
                const dashboardData = await response.json();
                if (dashboardData.error) {
                    console.log('No dashboard data available');
                    this.dashboard.showPlaceholder();
                    this.hideViewDashboardButton();
                } else {
                    this.dashboard.render(dashboardData);
                    this.showDashboard(); // Show dashboard when manually refreshed and data is available
                }
            }
        } catch (error) {
            console.error('Failed to refresh dashboard:', error);
            this.dashboard.showPlaceholder();
            this.hideViewDashboardButton();
        }
    }
    
    updateDashboard(dashboardData) {
        if (dashboardData && this.dashboard) {
            this.dashboard.render(dashboardData);
        }
    }
    
    handleDashboardUpdate(dashboardData) {
        console.log('Dashboard update received:', dashboardData);
        if (dashboardData && this.dashboard) {
            // Store current dashboard visibility state
            const wasVisible = this.elements.dashboardPanel.classList.contains('active');
            
            this.dashboard.render(dashboardData);
            
            if (wasVisible) {
                // If dashboard was already visible, just refresh it
                this.showDashboard();
            } else {
                // If dashboard was hidden, show the view button
                this.showViewDashboardButton();
                this.showDashboard();
            }
            
            this.elements.viewDashboardBtn.style.display = 'inline-block';
        }
    }
    
    showDashboard() {
        const panel = this.elements.dashboardPanel;
        const button = this.elements.toggleDashboard;
        const appLayout = document.querySelector('.app-layout');
        
        if (!panel.classList.contains('active')) {
            panel.classList.add('active');
            appLayout.classList.add('dashboard-active');
            button.textContent = 'Hide';
            this.hideViewDashboardButton();
        }
    }
    
    hideDashboard() {
        const panel = this.elements.dashboardPanel;
        const button = this.elements.toggleDashboard;
        const appLayout = document.querySelector('.app-layout');
        
        panel.classList.remove('active');
        appLayout.classList.remove('dashboard-active');
        button.textContent = 'Show';
        
        // Show the view dashboard button if there's data available
        if (this.dashboard && this.dashboard.currentData) {
            this.showViewDashboardButton();
        }
    }
    
    showViewDashboardButton() {
        this.elements.viewDashboardBtn.style.display = 'inline-block';
    }
    
    hideViewDashboardButton() {
        this.elements.viewDashboardBtn.style.display = 'none';
    }

    setupVoiceRecognition() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRecognition) {
            this.recognition = new SpeechRecognition();
            this.recognition.continuous = false;
            this.recognition.lang = 'en-US';
            this.recognition.interimResults = false;
            this.recognition.maxAlternatives = 1;

            this.recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                this.elements.userInput.value = transcript;
                this.autoResizeTextarea(this.elements.userInput);
                    if (transcript && transcript.trim()) {
                        this.sendMessage();
                    }
            };

            this.recognition.onerror = (event) => {
                console.error('Speech recognition error:', event.error);
                this.setVoiceRecognitionState(false);
            };

            this.recognition.onend = () => {
                this.setVoiceRecognitionState(false);
            };
        } else {
            console.warn('Speech Recognition not supported');
            if (this.elements.voiceBtn) {
                this.elements.voiceBtn.style.display = 'none';
            }
        }
    }

    toggleVoiceRecognition() {
        if (this.recognition && !this.isRecognizing) {
            try {
                this.recognition.start();
                this.setVoiceRecognitionState(true);
            } catch(e) {
                console.error("Error starting recognition:", e);
            }

        } else if (this.recognition && this.isRecognizing) {
            this.recognition.stop();
        }
    }

    setVoiceRecognitionState(isRecognizing) {
        this.isRecognizing = isRecognizing;
        if (isRecognizing) {
            this.elements.voiceBtn.classList.add('recording');
            this.elements.userInput.placeholder = 'Listening...';
        } else {
            this.elements.voiceBtn.classList.remove('recording');
            this.elements.userInput.placeholder = 'Type your message...';
        }
    }
}

// Dashboard Renderer Class
class DashboardRenderer {
    constructor(gridElement) {
        this.gridElement = gridElement;
        this.charts = new Map();
        this.currentData = null;
    }
    
    render(dashboardData) {
        if (!dashboardData || !dashboardData.charts) {
            this.showPlaceholder();
            return;
        }
        
        this.currentData = dashboardData;
        this.clearGrid();
        
        // Create chart containers based on layout
        dashboardData.charts.forEach((chart, index) => {
            this.createChartContainer(chart, index);
        });
    }
    
    clearGrid() {
        this.gridElement.innerHTML = '';
        this.charts.clear();
    }
    
    showPlaceholder() {
        this.gridElement.innerHTML = `
            <div class="dashboard-placeholder">
                <h3>No Dashboard Available</h3>
                <p>Ask the AI to analyze a layer to generate dashboard insights</p>
            </div>
        `;
    }
    
    createChartContainer(chartConfig, index) {
        const container = document.createElement('div');
        container.className = 'chart-container';
        container.id = `chart-${index}`;
        
        // Apply grid positioning
        const layout = chartConfig.layout || { size: 'medium' };
        const size = layout.size || 'medium';
        container.classList.add(`chart-${size}`);
        
        // Debug logging
        console.log(`Creating chart ${index}:`, {
            title: chartConfig.title,
            size: size,
            template: layout.template,
            hasExplicitPosition: !!(layout.column && layout.row),
            layout: layout
        });
        
        // Only use explicit positioning if we have specific positioning data
        // Otherwise let CSS grid auto-placement handle positioning with size classes
        const useExplicitPositioning = layout.column && layout.row && 
                                     layout.template && layout.template !== 'auto';
        
        if (useExplicitPositioning) {
            const width = layout.width || this.getSizeWidth(size);
            const height = layout.height || this.getSizeHeight(size);
            container.style.gridColumn = `${layout.column} / span ${width}`;
            container.style.gridRow = `${layout.row} / span ${height}`;
            console.log(`Applied explicit positioning to chart ${index}:`, {
                gridColumn: container.style.gridColumn,
                gridRow: container.style.gridRow
            });
        } else {
            console.log(`Using CSS auto-placement for chart ${index} with size class: chart-${size}`);
        }
        // Otherwise let CSS handle it with the size class
        
        container.innerHTML = `
            <div class="chart-header">
                <h3 class="chart-title">${chartConfig.title || 'Chart'}</h3>
                <span class="chart-type">${chartConfig.type.toUpperCase()}</span>
            </div>
            <div class="chart-canvas-wrapper">
                <canvas class="chart-canvas" id="canvas-${index}"></canvas>
            </div>
            <div class="chart-info">
                ${chartConfig.description || ''}
            </div>
        `;
        
        this.gridElement.appendChild(container);
        
        // Create the chart
        setTimeout(() => {
            this.createChart(chartConfig, `canvas-${index}`);
        }, 100);
    }
    
    getSizeWidth(size) {
        const widthMap = {
            'small': 3,
            'medium': 4,
            'large': 6,
            'wide': 8,
            'tall': 4,
            'full': 12
        };
        return widthMap[size] || 4;
    }
    
    getSizeHeight(size) {
        const heightMap = {
            'small': 2,
            'medium': 3,
            'large': 4,
            'wide': 3,
            'tall': 5,
            'full': 4
        };
        return heightMap[size] || 3;
    }
    
    createChart(config, canvasId) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        
        // Prepare chart data and options based on type
        const chartData = this.prepareChartData(config);
        const chartOptions = this.getChartOptions(config);
        
        try {
            const chart = new Chart(ctx, {
                type: this.mapChartType(config.type),
                data: chartData,
                options: chartOptions
            });
            
            this.charts.set(canvasId, chart);
        } catch (error) {
            console.error('Failed to create chart:', error);
            this.showChartError(canvas.parentElement, error.message);
        }
    }
    
    mapChartType(type) {
        const typeMap = {
            'pie': 'pie',
            'donut': 'doughnut',
            'bar': 'bar',
            'column': 'bar',
            'histogram': 'bar',
            'line': 'line',
            'scatter': 'scatter',
            'area': 'line',
            'box_plot': 'bar'
        };
        return typeMap[type] || 'bar';
    }
    
    prepareChartData(config) {
        const data = config.data || {};
        
        // Handle different chart types
        switch (config.type) {
            case 'pie':
            case 'donut':
                return {
                    labels: data.labels || [],
                    datasets: [{
                        data: data.values || [],
                        backgroundColor: this.generateColors(data.labels?.length || 0),
                        borderWidth: 1
                    }]
                };
                
            case 'bar':
            case 'column':
            case 'histogram':
                // Check if this is a multi-series chart with datasets
                if (data.datasets && Array.isArray(data.datasets) && data.datasets.length > 1) {
                    // Multi-series bar chart
                    const colors = this.generateColors(data.datasets.length);
                    return {
                        labels: data.labels || [],
                        datasets: data.datasets.map((dataset, index) => ({
                            label: dataset.label || dataset.name || `Series ${index + 1}`,
                            data: dataset.data || [],
                            backgroundColor: colors[index],
                            borderColor: colors[index].replace('0.8', '1'),
                            borderWidth: 1
                        }))
                    };
                } else {
                    // Single-series bar chart (backward compatibility)
                    return {
                        labels: data.labels || [],
                        datasets: [{
                            label: config.y_field || 'Count',
                            data: data.values || [],
                            backgroundColor: 'rgba(54, 162, 235, 0.6)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }]
                    };
                }
                
            case 'line':
            case 'area':
                return {
                    labels: data.labels || [],
                    datasets: [{
                        label: config.y_field || 'Value',
                        data: data.values || [],
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: config.type === 'area' ? 'rgba(75, 192, 192, 0.2)' : 'transparent',
                        fill: config.type === 'area',
                        tension: 0.1
                    }]
                };
                
            case 'scatter':
                return {
                    datasets: [{
                        label: `${config.x_field} vs ${config.y_field}`,
                        data: data.points || [],
                        backgroundColor: 'rgba(255, 99, 132, 0.6)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                };
                
            default:
                return { labels: [], datasets: [] };
        }
    }
    
    getChartOptions(config) {
        const baseOptions = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: config.type !== 'histogram',
                    position: 'bottom'
                },
                title: {
                    display: false
                }
            }
        };
        
        // Add scale options for non-pie charts
        if (!['pie', 'donut'].includes(config.type)) {
            baseOptions.scales = {
                x: {
                    title: {
                        display: true,
                        text: config.x_field || ''
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: config.y_field || 'Count'
                    },
                    beginAtZero: true
                }
            };
        }
        
        return baseOptions;
    }
    
    generateColors(count) {
        const colors = [
            'rgba(255, 99, 132, 0.8)',
            'rgba(54, 162, 235, 0.8)',
            'rgba(255, 205, 86, 0.8)',
            'rgba(75, 192, 192, 0.8)',
            'rgba(153, 102, 255, 0.8)',
            'rgba(255, 159, 64, 0.8)',
            'rgba(199, 199, 199, 0.8)',
            'rgba(83, 102, 255, 0.8)'
        ];
        
        const result = [];
        for (let i = 0; i < count; i++) {
            result.push(colors[i % colors.length]);
        }
        return result;
    }
    
    showChartError(container, message) {
        const wrapper = container.querySelector('.chart-canvas-wrapper');
        wrapper.innerHTML = `
            <div class="dashboard-error">
                <strong>Chart Error:</strong> ${message}
            </div>
        `;
    }
}

// Initialize the client when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.smartAssistant = new SmartAssistantClient();
    
    // Expose some methods for debugging
    window.sa = {
        status: () => window.smartAssistant.getConnectionStatus(),
        clear: () => window.smartAssistant.clearHistory(),
        reconnect: () => window.smartAssistant.connect()
    };
    
    console.log('Smart Assistant initialized. Use window.sa for debugging methods.');
});

// Add some CSS for error messages and system messages
const style = document.createElement('style');
style.textContent = `
    .error-message {
        background-color: rgba(220, 53, 69, 0.1) !important;
        border: 1px solid rgba(220, 53, 69, 0.3);
        color: #dc3545 !important;
    }
    
    /* System messages */
    .msg.system-msg {
        justify-content: center;
        align-self: center;
        max-width: 60%;
    }

    .msg.system-msg .msg-bubble {
        background-color: rgba(255, 193, 7, 0.1);
        border: 1px solid rgba(255, 193, 7, 0.3);
        color: var(--text-color);
        text-align: center;
        font-size: 0.9rem;
        padding: 0.8rem 1rem;
        min-width: auto;
        border-radius: 20px;
    }
`;
document.head.appendChild(style);
