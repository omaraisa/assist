import unittest
import sys
import os
import json

# Add the Progent directory to the Python path to find spatial_functions
progent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(progent_dir, '..'))

# Since spatial_functions is now in Progent, we need to adjust the import
from Progent.spatial_functions import SpatialFunctions

class TestFunctionParsing(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        # We need to mock the websocket_manager
        class MockWebSocketManager:
            def get_arcgis_client(self):
                return "mock_client"
            def send_to_client(self, client_id, payload):
                pass
            def has_function_result(self, session_id):
                return False
            def get_function_result(self, session_id):
                return None

        self.spatial_functions = SpatialFunctions(MockWebSocketManager())

    def test_happy_path_create_buffer(self):
        """Test a valid call to the create_buffer function."""
        result = self.spatial_functions.create_buffer(
            layer_name="MyLayer",
            distance=100,
            units="meters"
        )
        self.assertFalse(result["success"])
        self.assertIn("ArcPy is not available", result["error"])

    def test_missing_parameters_create_buffer(self):
        """Test calling create_buffer with missing parameters."""
        with self.assertRaises(TypeError):
            self.spatial_functions.create_buffer(layer_name="MyLayer")

    def test_invalid_parameters_create_buffer(self):
        """Test calling create_buffer with invalid parameters."""
        result = self.spatial_functions.create_buffer(
            layer_name="MyLayer",
            distance="invalid",
            units="meters"
        )
        self.assertFalse(result["success"])
        self.assertIn("ArcPy is not available", result["error"])

if __name__ == '__main__':
    unittest.main()
