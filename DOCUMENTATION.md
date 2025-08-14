# ArcGIS Pro Smart Assistant - Documentation

## 1. Overview

The ArcGIS Pro Smart Assistant is an AI-powered spatial analysis assistant that integrates with ArcGIS Pro to provide natural language interaction with GIS functions. It consists of a FastAPI web server that communicates with ArcGIS Pro through a WebSocket connection, allowing users to execute spatial functions via an AI chat interface.

This document provides a detailed overview of the project's architecture, components, and instructions for installation and usage.

## 2. Architecture & Components

The system follows a client-server architecture with WebSocket communication.

*   **FastAPI Web Server (`app/main.py`):** Hosts the web interface, manages WebSocket connections, and routes messages. It never executes spatial functions directly.
*   **ArcGIS Pro Add-in (`Progent/` directory):** The client that runs inside ArcGIS Pro. It establishes the WebSocket connection to the FastAPI server, executes GIS functions, and automatically opens the chatbot interface in a browser upon successful connection.
*   **WebSocket Manager (`app/websocket_manager.py`):** The central hub for routing messages between the web client and the ArcGIS Pro Add-in.
*   **AI Service (`app/ai_service.py`):** Manages interactions with multiple AI models, including Gemini, GPT, Claude, and local Ollama models.
*   **LangChain Agent (`app/langchain_agent.py`):** Uses the ReAct pattern for reasoning and tool usage, orchestrating the AI's interaction with the GIS functions. This is the primary execution path for all "safe mode" interactions.

### 2.1. Key Components

*   **Spatial Functions Module (`app/spatial_functions.py`):** This module contains over 33 GIS analysis functions (e.g., `create_buffer`, `spatial_join`, `select_by_attribute`). These functions use the `arcpy` library and can only be executed within the ArcGIS Pro environment.
*   **Function Declarations (`app/ai/function_declarations.py`):** A structured metadata file that acts as a "function manual" for the AI agent. It provides the AI with details on function signatures and parameters, allowing for dynamic function discovery and usage.

### 2.2. WebSocket Communication Flow

The communication path is as follows:

1.  **Web Client -> FastAPI Server -> WebSocket Manager -> ArcGIS Pro Add-in**
2.  **ArcGIS Pro Add-in -> Spatial Functions -> Function Results -> WebSocket Manager -> FastAPI Server -> Web Client**

## 3. Installation and Setup

### 3.1. Prerequisites

*   ArcGIS Pro 3.x
*   Python 3.9 or higher
*   .NET 6.0 SDK (for building the ArcGIS Pro Add-in)

### 3.2. Server Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/omaraisa/assist.git
    cd assist
    ```
2.  **Create a Python virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your API keys:**
    *   The application searches for API keys in the following order: environment variables, `.env` file, `config.py`.
    *   Create a `.env` file in the root directory of the project.
    *   Add your API keys to the `.env` file, for example:
        ```
        GEMINI_API_KEY="your_gemini_api_key"
        OPENAI_API_KEY="your_openai_api_key"
        ANTHROPIC_API_KEY="your_anthropic_api_key"
        ```
5.  **Start the server:**
    ```bash
    python run.py
    ```
    The server will be running at `http://localhost:8000`.

### 3.3. ArcGIS Pro Add-in Setup

1.  **Open the solution:** Open the `Progent.sln` file in the `Progent/` directory with Visual Studio 2022.
2.  **Build the solution:** Build the solution in "Release" mode. This will create the add-in file (`.esriAddinX`) in the `Progent/bin/Release/` directory.
3.  **Install the add-in:** Double-click the `.esriAddinX` file to install it in ArcGIS Pro.

## 4. Usage

1.  **Start the server:** Make sure the FastAPI server is running.
2.  **Open ArcGIS Pro:** Open a project in ArcGIS Pro.
3.  **Open the Smart Assistant dockpane:** Go to the "Add-In" tab and click the "Show Dockpane" button.
4.  **Connect to the server:** The dockpane will open. Enter the server URL (default is `ws://localhost:8000/ws`) and click "Connect".
5.  **Chat with the assistant:** Once connected, the chatbot interface will open in your default web browser. You can now start interacting with the AI assistant.

### 4.1. Dashboard Features

*   **Smart Dashboard:** The assistant can generate a smart dashboard with charts and graphs based on your data.
*   **Partial Updates:** You can refresh individual charts on the dashboard without reloading the entire panel.
*   **Automatic Opening:** The dashboard will open automatically whenever it's updated.

### 4.2. Expert Mode

*   **Warning:** Expert mode allows the AI to execute raw Python code directly in your ArcGIS Pro environment. This is a powerful feature, but it should be used with caution.
*   **Enable Expert Mode:** You can enable expert mode from the chat interface. You will be asked to confirm that you understand the risks.

## 5. Logging

The application uses colored logging in the command window for better readability. The logging configuration is defined in the `log_config.yaml` file.

The `watchfiles` library, which is used for auto-reloading the server, can be a bit noisy. To reduce the log spam, the log level for `watchfiles` has been set to `WARNING` in the `log_config.yaml` file.
