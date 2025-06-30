"""
Performance optimization utilities for the GIS Assistant application.
This module provides functions to improve response time and reduce overhead.
"""

import logging
import json
from typing import Dict, Any, List, Union, Optional

logger = logging.getLogger(__name__)

def truncate_for_logging(obj: Any, max_length: int = 500) -> Any:
    """
    Truncate large objects for logging to avoid performance issues
    
    Args:
        obj: The object to truncate
        max_length: Maximum length for string values
        
    Returns:
        Truncated version of the object
    """
    if isinstance(obj, str) and len(obj) > max_length:
        return obj[:max_length] + "... [truncated]"
    elif isinstance(obj, dict):
        return {k: truncate_for_logging(v) for k, v in list(obj.items())[:10]}
    elif isinstance(obj, list):
        if len(obj) > 10:
            return [truncate_for_logging(o) for o in obj[:10]] + ["... and more"]
        return [truncate_for_logging(o) for o in obj]
    return obj

def log_efficiently(logger, level: str, message: str, obj: Optional[Any] = None, max_length: int = 500):
    """
    Log messages efficiently with object truncation
    
    Args:
        logger: Logger instance
        level: Log level (info, debug, warning, error)
        message: Log message
        obj: Optional object to log (will be truncated)
        max_length: Maximum length for string values
    """
    if obj is not None:
        truncated_obj = truncate_for_logging(obj, max_length)
        if level == "debug":
            logger.debug(f"{message}: {truncated_obj}")
        elif level == "info":
            logger.info(f"{message}: {truncated_obj}")
        elif level == "warning":
            logger.warning(f"{message}: {truncated_obj}")
        elif level == "error":
            logger.error(f"{message}: {truncated_obj}")
    else:
        if level == "debug":
            logger.debug(message)
        elif level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
        elif level == "error":
            logger.error(message)

def optimize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Optimize API payload by removing unnecessary data and reducing size
    
    Args:
        payload: The API payload
        
    Returns:
        Optimized payload
    """
    # Make a copy to avoid modifying the original
    optimized = payload.copy()
    
    # Handle conversation history optimization
    if "messages" in optimized:
        # Limit history depth if excessive
        if len(optimized["messages"]) > 10:
            # Keep system messages plus the last 8 messages
            system_messages = [m for m in optimized["messages"] if m.get("role") == "system"]
            other_messages = [m for m in optimized["messages"] if m.get("role") != "system"][-8:]
            optimized["messages"] = system_messages + other_messages
    
    # For Gemini-specific optimization
    if "contents" in optimized:
        # Limit conversation depth
        if len(optimized["contents"]) > 8:
            optimized["contents"] = optimized["contents"][-8:]
    
    return optimized

def setup_timeouts(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Set up appropriate timeouts for API calls
    
    Args:
        config: API configuration
        
    Returns:
        Config with timeout settings
    """
    config["timeout"] = {
        "request": 30.0,  # 30 second request timeout
        "connect": 10.0,  # 10 second connection timeout
        "sock_read": 60.0  # 60 second socket read timeout
    }
    return config

def performance_metrics_decorator(func):
    """
    Decorator to log performance metrics for functions
    """
    import time
    import functools
    
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logger.info(f"Function {func.__name__} executed in {elapsed_time:.2f} seconds")
        return result
    
    return wrapper
