# Offline LLM Setup for ArcGIS Pro Smart Assistant

This guide helps you set up local LLMs using Ollama for the ArcGIS Pro Smart Assistant.

## Prerequisites

1. **Install Ollama**: Download and install Ollama from https://ollama.ai
2. **Start Ollama**: Run `ollama serve` to start the Ollama server on `localhost:11434`

## Quick Setup

1. Run the setup script to install required packages:
    ```batch
    setup_offline_llm.bat
    ```

2. Download recommended models:
    ```bash
    ollama pull llama3.2:8b
    ollama pull codellama:13b
    ollama pull mistral:7b
    ```

## Features

### RAG (Retrieval-Augmented Generation)
- The assistant now uses RAG for initial instructions and general ArcGIS questions
- Knowledge base includes ArcGIS Pro basics, spatial analysis concepts, and assistant capabilities
- RAG is used only for general help questions, not for specific data analysis tasks

### Local LLM Models
- **Llama 3.2 8B**: General purpose model, good for most tasks
- **CodeLlama 13B**: Specialized for code and technical tasks
- **Mistral 7B**: Fast and efficient for general conversations

## How It Works

1. **RAG Context**: When you ask general questions about ArcGIS or need help, the assistant uses the knowledge base to provide context
2. **Current State**: Your current ArcGIS Pro state (layers, maps, etc.) is always included in the context
3. **Function Calling**: Local models can still call spatial analysis functions to work with your data

## Usage

1. Start the assistant normally
2. Select an Ollama model from the dropdown (models with "Local" in the name)
3. Ask questions or request analysis - the assistant will use both RAG knowledge and your current ArcGIS state

## Troubleshooting

- **"Ollama service not available"**: Make sure Ollama is running with `ollama serve`
- **Model not found**: Ensure you've downloaded the model with `ollama pull <model_name>`
- **RAG not working**: Check that the `rag_db` directory was created and contains data

## Configuration

Edit `app/config.py` to:
- Change Ollama base URL (default: `http://localhost:11434`)
- Enable/disable RAG (`ENABLE_RAG = True/False`)
- Adjust RAG chunk size and overlap

## Performance Tips

- **Llama 3.2 8B**: Fastest, good for most tasks
- **CodeLlama 13B**: Better for technical analysis but slower
- **Mistral 7B**: Good balance of speed and capability

The local models work entirely offline and don't require API keys!
