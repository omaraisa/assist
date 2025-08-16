import pytest
import json
import sys
import os
from unittest.mock import MagicMock, patch

# Add the project root to the Python path to allow imports from app and Progent
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

from app.function_repo import CREATE_BUFFER_CODE
# The progent_execute script is designed to be run as a main script,
# so we import its function directly for testing.
from Progent.progent_execute import execute_code

@pytest.fixture
def mock_arcpy_env():
    """Pytest fixture to provide a mocked arcpy module and related objects."""
    mock_arcpy = MagicMock()
    mock_aprx = MagicMock()
    mock_map = MagicMock()
    mock_layer = MagicMock()
    mock_layer.name = "TestLayer"

    mock_aprx.activeMap = mock_map
    mock_map.listLayers.return_value = [mock_layer]
    mock_aprx.defaultGeodatabase = "C:/fakepath/default.gdb"

    mock_arcpy.mp.ArcGISProject.return_value = mock_aprx
    mock_arcpy.CreateUniqueName.side_effect = lambda path: f"{path}_1"

    # Return all the components needed for detailed assertions
    return {
        "arcpy": mock_arcpy,
        "aprx": mock_aprx,
        "map": mock_map,
        "layer": mock_layer
    }

def run_test(capsys, payload):
    """Helper function to run the execute_code function and parse its output."""
    payload_str = json.dumps(payload)
    execute_code(payload_str)
    captured = capsys.readouterr()
    return json.loads(captured.out)

def test_create_buffer_happy_path(capsys, mock_arcpy_env):
    """
    Tests the successful execution of the create_buffer code string.
    """
    mock_arcpy = mock_arcpy_env["arcpy"]
    mock_layer = mock_arcpy_env["layer"]

    with patch.dict(sys.modules, {'arcpy': mock_arcpy}):
        payload = {
            "code": CREATE_BUFFER_CODE,
            "function_name": "create_buffer",
            "parameters": {
                "layer_name": "TestLayer",
                "distance": 100,
                "units": "meters"
            }
        }

        result = run_test(capsys, payload)

        # Assertions
        assert result['status'] == 'success'
        assert result['data']['success'] is True
        assert result['data']['layer_name'] == "TestLayer"
        assert result['data']['output_layer'].startswith("TestLayer_Buffer_100meters")
        assert "output_path" not in result['data'] # Check sanitization
        assert result['_captured_output'] == ""

        # Check if arcpy.analysis.Buffer was called correctly
        mock_arcpy.analysis.Buffer.assert_called_once()
        call_args = mock_arcpy.analysis.Buffer.call_args[1]
        assert call_args['in_features'] == mock_layer
        assert call_args['buffer_distance_or_field'] == "100 METERS"

def test_create_buffer_layer_not_found(capsys, mock_arcpy_env):
    """
    Tests the case where the specified layer does not exist.
    """
    mock_arcpy = mock_arcpy_env["arcpy"]
    # Configure mock to find no layers
    mock_arcpy.mp.ArcGISProject.return_value.activeMap.listLayers.return_value = []

    with patch.dict(sys.modules, {'arcpy': mock_arcpy}):
        payload = {
            "code": CREATE_BUFFER_CODE,
            "function_name": "create_buffer",
            "parameters": {
                "layer_name": "NonExistentLayer",
                "distance": 50,
                "units": "feet"
            }
        }

        result = run_test(capsys, payload)

        # Assertions
        assert result['status'] == 'success' # The script itself runs successfully
        assert result['data']['success'] is False
        assert "Layer 'NonExistentLayer' not found" in result['data']['error']
        assert result['_captured_output'] == ""

def test_create_buffer_invalid_units(capsys, mock_arcpy_env):
    """
    Tests the case where invalid units are provided.
    """
    mock_arcpy = mock_arcpy_env["arcpy"]
    with patch.dict(sys.modules, {'arcpy': mock_arcpy}):
        payload = {
            "code": CREATE_BUFFER_CODE,
            "function_name": "create_buffer",
            "parameters": {
                "layer_name": "TestLayer",
                "distance": 10,
                "units": "parsecs" # Invalid unit
            }
        }

        result = run_test(capsys, payload)

        # Assertions
        assert result['status'] == 'success'
        assert result['data']['success'] is False
        assert "Invalid units: 'parsecs'" in result['data']['error']
        assert result['_captured_output'] == ""

        # Ensure the buffer tool was not called
        mock_arcpy.analysis.Buffer.assert_not_called()
