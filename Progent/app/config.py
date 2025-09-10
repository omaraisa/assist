from pydantic_settings import BaseSettings
from typing import Dict, Any
import os

class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 6060
    DEBUG: bool = True
    
    # AI Models Configuration
    AI_MODELS: Dict[str, Dict[str, Any]] = {
        "GEMINI_FLASH": {
            "name": "Gemini 1.5 Flash",
            "model": "gemini-1.5-flash-latest",
            "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
            "max_tokens": 8192,
            "temperature": 0.7,
            "api_key_env": "GEMINI_API_KEY"
        },
        "GEMINI_PRO": {
            "name": "Gemini 1.5 Pro", 
            "model": "gemini-1.5-pro-latest",
            "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent",
            "max_tokens": 32768,
            "temperature": 0.7,
            "api_key_env": "GEMINI_API_KEY"
        },
        "GEMINI_FLASH_EXP": {
            "name": "Gemini 2.0 Flash Experimental",
            "model": "gemini-2.0-flash-exp",
            "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent",
            "max_tokens": 8192,
            "temperature": 0.7,
            "api_key_env": "GEMINI_API_KEY"
        },        # Temporarily disabled due to context length limitations with function calling
        # "GPT4": {
        #     "name": "GPT-4",
        #     "model": "gpt-4",
        #     "endpoint": "https://api.openai.com/v1/chat/completions",
        #     "max_tokens": 8192,
        #     "temperature": 0.7,
        #     "api_key_env": "OPENAI_API_KEY"
        # },
        # "GPT4_TURBO": {
        #     "name": "GPT-4 Turbo",
        #     "model": "gpt-4-turbo",
        #     "endpoint": "https://api.openai.com/v1/chat/completions",
        #     "max_tokens": 4096,
        #     "temperature": 0.7,
        #     "api_key_env": "OPENAI_API_KEY"
        # },
        # "GPT4O": {
        #     "name": "GPT-4o",
        #     "model": "gpt-4o",
        #     "endpoint": "https://api.openai.com/v1/chat/completions",
        #     "max_tokens": 4096,
        #     "temperature": 0.7,
        #     "api_key_env": "OPENAI_API_KEY"
        # },
        # "CLAUDE": {
        #     "name": "Claude 3.5 Sonnet",
        #     "model": "claude-3-5-sonnet-20241022",
        #     "endpoint": "https://api.anthropic.com/v1/messages",
        #     "max_tokens": 8192,
        #     "temperature": 0.7,
        #     "api_key_env": "ANTHROPIC_API_KEY"        },
        # Ollama Models (Local LLMs)
        "OLLAMA_GEMMA": {
                "name": "llama3 8B (Local)",
                "model": "llama3:8b",
                "provider": "ollama",
                "endpoint": "http://localhost:11434",
                "max_tokens": 8192,
                "temperature": 0.7,
                "local": True
            },
            # "OLLAMA_LLAMA31": {
            #     "name": "Llama 3.2 3B (Local)",
            #     "model": "llama3.2:3b",
            #     "provider": "ollama",
            #     "endpoint": "http://localhost:11434",
            #     "max_tokens": 32768,
            #     "temperature": 0.7,
            #     "local": True
            # },
            # "OLLAMA_CODELLAMA": {
            #     "name": "CodeLlama 13B (Local)",
            #     "model": "codellama:13b",
            #     "provider": "ollama", 
            #     "endpoint": "http://localhost:11434",
            #     "max_tokens": 32768,
            #     "temperature": 0.7,
            #     "local": True
            # },
            # "OLLAMA_MISTRAL": {
            #     "name": "Mistral 7B (Local)",
            #     "model": "mistral:7b",
            #     "provider": "ollama",
            #     "endpoint": "http://localhost:11434", 
            #     "max_tokens": 32768,
            #     "temperature": 0.7,
            #     "local": True
            # }
    }
    
    # Default AI Model
    DEFAULT_AI_MODEL: str = "GEMINI_FLASH"
    
    # API Keys (loaded from environment variables)
    # NOTE: To use different models, set their API keys in .env file:
    # - For Gemini models: Set GEMINI_API_KEY
    # - For OpenAI models: Set OPENAI_API_KEY 
    # - For Claude: Set ANTHROPIC_API_KEY
    # - For Ollama: No API key needed (local)
    GEMINI_API_KEY: str = "AIzaSyCd-sdQInmKN3spQqNjN4e1O2pQRsBV05Q"
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    
    # Ollama Configuration
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    ENABLE_RAG: bool = True
    RAG_CHUNK_SIZE: int = 1000
    RAG_CHUNK_OVERLAP: int = 200
    
    # WebSocket Configuration
    WS_HEARTBEAT_INTERVAL: int = 30
    WS_MAX_CONNECTIONS: int = 100
    
    # Chat Configuration
    MAX_HISTORY_LENGTH: int = 10
    ENABLE_INVESTIGATION_MODE: bool = True
    AUTO_SAVE_HISTORY: bool = True
    
    # State Configuration - Reduce payload by including only essential info
    STATE_INCLUDE_FIELDS: Dict[str, list] = {
        "layers": ["name", "isVisible", "definitionQuery"],
        "tables": ["name"],
        "project": ["path", "name"],
        "map": ["name", "spatialReference"]
    }
    
    EXCLUDE_DETAILED_FIELDS: bool = True
    MAX_FEATURE_SUMMARY: int = 100
    
    # Message Types for WebSocket identification
    MESSAGE_TYPES: Dict[str, Dict[str, str]] = {
        "CONNECTION": {
            "REGISTER": "client_register",
            "HEARTBEAT": "heartbeat",
            "HEARTBEAT_ACK": "heartbeat_ack"
        },
        "DATA": {
            "SOFTWARE_STATE": "software_state",
            "FUNCTIONS_LIST": "functions_list",
            "ERROR": "error",
            "SUCCESS": "success"
        },
        "COMMAND": {
            "FUNCTION_CALL": "function_request",
            "EXECUTE_FUNCTION": "execute_function", 
            "GET_STATE": "get_software_state",
            "INVESTIGATE": "investigate_command"
        },
        "RESPONSE": {
            "USER_MESSAGE": "user_message",
            "PROGENT_MESSAGE": "progent_message",
            "SYSTEM_MESSAGE": "system_message",
            "FUNCTION_RESULT": "function_result"
        }
    }
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()

# Helper function to get API key for a specific model
def get_api_key(model_key: str) -> str:
    """Get API key for a specific AI model"""
    if model_key not in settings.AI_MODELS:
        raise ValueError(f"Unknown AI model: {model_key}")
    
    model_config = settings.AI_MODELS[model_key]
    
    # Check if this is a local model (no API key needed)
    if model_config.get("local", False) or model_config.get("provider") == "ollama":
        return ""  # No API key needed for local models
    
    # For cloud models, get the API key
    if "api_key_env" not in model_config:
        raise ValueError(f"Model {model_key} missing api_key_env configuration")
        
    env_var = model_config["api_key_env"]
    # Check environment variable first (for dynamic updates), then fall back to settings
    api_key = os.environ.get(env_var) or getattr(settings, env_var, "")
    
    if not api_key:
        model_name = model_config["name"]
        # Allow server to start without API key, but log a warning.
        # The key will be requested from the user via the UI when needed.
        print(f"Warning: API key not found for {model_name}. Please set {env_var} or add it through the UI.")
        return ""

    return api_key

# Helper function to get model config
def get_model_config(model_key: str) -> Dict[str, Any]:
    """Get configuration for a specific AI model"""
    if model_key not in settings.AI_MODELS:
        raise ValueError(f"Unknown AI model: {model_key}")
    
    config = settings.AI_MODELS[model_key].copy()
    config["api_key"] = get_api_key(model_key)
    
    return config
