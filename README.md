# 🤖 ArcGIS Pro Smart Assistant

A powerful AI-powered assistant for ArcGIS Pro that provides intelligent GIS data analysis through natural language conversation.

## ✨ Features

- 🧠 **Multi-AI Support**: OpenAI GPT-4, Google Gemini, Anthropic Claude
- 💬 **Natural Language Interface**: Chat with your GIS data in Arabic or English
- 🔧 **Comprehensive GIS Toolkit**: A wide range of spatial analysis capabilities executed on the client.
- 🌐 **Decoupled Architecture**: A FastAPI server for AI orchestration and a separate ArcGIS Pro client for all `arcpy` execution, communicating via WebSockets.
- 📊 **Investigation Mode**: AI chains multiple analyses for comprehensive insights.

## 🚀 Quick Start

**See [`QUICK_START.md`](QUICK_START.md) for the fastest way to get started!**

## 📁 Project Structure

The project is divided into two main components: the server-side application (`app/`) and the ArcGIS Pro client (`Progent/`).

- **`app/`**: The core FastAPI web server.
  - `main.py`: The main entry point for the FastAPI server.
  - `langchain_agent.py`: The AI agent responsible for understanding user queries and orchestrating function calls.
  - `websocket_manager.py`: Manages the WebSocket communication between the server and the ArcGIS Pro client.
  - `ai/function_declarations.py`: Contains the function signatures that the AI uses to understand the available tools. This acts as a "manual" for the AI, but contains no executable code.

- **`Progent/`**: The ArcGIS Pro Add-in (the client).
  - `progent.pyt`: A Python Toolbox that contains all the GIS-specific functions using `arcpy`. This is where all the actual GIS work happens.
  - `WebSocketService.cs`: The C# service that runs within ArcGIS Pro, handling the WebSocket connection and executing functions in `progent.pyt` based on messages from the server.

- **`static/` & `templates/`**: The web UI for the chat interface.

##  architectural-principle

The server application (`app/`) is designed to be completely decoupled from the ArcGIS Pro client (`Progent/`). The server's role is to manage the AI, handle user interactions, and pass messages to the client. It has no knowledge of how the GIS functions are implemented and contains no `arcpy` code. All GIS-specific logic and execution are handled exclusively by the client running within ArcGIS Pro.

## 🔧 Available AI Models

- **Gemini Flash** ⚡ (Recommended - Fast & Free)
- **Gemini Pro** 🧠 (Advanced reasoning)
- **GPT-4 Turbo** 💎 (OpenAI premium)
- **GPT-4o** 🚀 (Latest OpenAI)
- **Claude Sonnet** 🎭 (Anthropic)

## 🗺️ GIS Analysis Functions

The assistant provides 27 built-in spatial analysis functions:

- **Data Exploration**: Layer summaries, field statistics, unique values
- **Spatial Selection**: Select by attribute, location, proximity
- **Geometric Analysis**: Calculate area, length, centroids, buffers
- **Spatial Operations**: Clipping, spatial joins, nearest neighbor
- **Data Export**: Excel export, frequency tables, validation

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Server won't start | Run `setup_environment.bat` |
| API errors | Check API keys in `.env` file |
| ArcGIS connection fails | Verify paths in `connect_arcgis.bat` |
| Function errors | Check ArcGIS Pro connection |

## 📋 System Requirements

- Windows 10/11
- Python 3.8+
- 2GB free disk space
- Internet connection (for AI APIs)
- ArcGIS Pro (optional, for GIS functions)

## 🔐 Security Notes

- API keys are stored locally in `.env` file
- No data is sent to external servers except AI API calls
- WebSocket connections are local (localhost only)

## 📜 License

This project is intended for educational and research purposes. Please ensure compliance with AI provider terms of service.

---

**Status: Production Ready** ✅  
**Last Updated: June 16, 2025**
