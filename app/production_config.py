"""
Production configuration for ArcGIS Pro Smart Assistant
"""

from .config import Settings as BaseSettings
from typing import Dict, Any
import os

class ProductionSettings(BaseSettings):
    """Production-specific settings"""
    
    # Production server settings
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Security settings
    CORS_ORIGINS: list = ["http://localhost:3000", "https://yourdomain.com"]
    ALLOWED_HOSTS: list = ["localhost", "yourdomain.com"]
    
    # Production API limits
    WS_MAX_CONNECTIONS: int = 1000
    REQUEST_TIMEOUT: int = 300
    MAX_CONCURRENT_REQUESTS: int = 100
    
    # Logging configuration
    LOG_LEVEL: str = "INFO"
    LOG_FILE_PATH: str = "/app/logs/production.log"
    ENABLE_ACCESS_LOGS: bool = True
    
    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60  # seconds
    
    # Production AI settings
    AI_REQUEST_TIMEOUT: int = 60
    AI_MAX_RETRIES: int = 3
    AI_RETRY_DELAY: int = 2
    
    # Database settings (for future session storage)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./progent.db")
    
    # Monitoring
    ENABLE_METRICS: bool = True
    METRICS_ENDPOINT: str = "/metrics"
    
    class Config:
        env_file = ".env.production"
        case_sensitive = True

# Create production settings instance
production_settings = ProductionSettings()
