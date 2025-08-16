"""
Fallback Functions Module
"""

class FallbackFunctions:
    """A collection of fallback functions for the server."""

    def __init__(self, websocket_manager=None):
        self.websocket_manager = websocket_manager

    def echo(self, message: str) -> str:
        """
        A simple echo function that returns the message it received.
        """
        return f"The server received your message: {message}"
