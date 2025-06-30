"""
A simple utility script to update the log level for specific loggers
to reduce excessive output and improve performance.
"""

import logging
import sys

def reduce_logging():
    """
    Reduce logging level for specific modules to improve performance
    """
    # Set the Gemini handler to log at WARNING level to reduce JSON dumps
    logging.getLogger("app.ai.ai_response_handler").setLevel(logging.WARNING)
    
    # Limit aiohttp logging which can be verbose
    logging.getLogger("aiohttp").setLevel(logging.WARNING)
    
    # For debugging, we can print the current loggers and their levels
    print("Reduced logging for the following loggers:")
    print(" - app.ai.ai_response_handler: WARNING")
    print(" - aiohttp: WARNING")
    print("This should improve response times by reducing verbose logging.")

if __name__ == "__main__":
    reduce_logging()
