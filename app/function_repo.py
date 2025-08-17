"""
This module provides a repository for simple, non-arcpy functions that can be
executed directly on the server. This allows for rapid development and testing
of new functions without requiring a full deployment to the ArcGIS Pro add-in.
"""

import logging

logger = logging.getLogger(__name__)

def hello_world(name: str = "World") -> dict:
    """
    A simple example function that returns a greeting.
    """
    logger.info(f"Executing hello_world with name: {name}")
    return {"success": True, "message": f"Hello, {name}!"}

# A dictionary to hold the available functions in this repository.
# This allows for dynamic dispatch of functions.
FUNCTION_REPO = {
    "hello_world": hello_world,
}
