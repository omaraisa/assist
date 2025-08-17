
import unittest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch

from app.langchain_agent import LangChainAgent
from app.websocket_manager import WebSocketManager

class TestMigration(unittest.TestCase):

    def setUp(self):
        # Patch get_model_config to avoid API key errors during testing
        self.patcher = patch('app.config.get_model_config')
        self.mock_get_model_config = self.patcher.start()
        self.mock_get_model_config.return_value = {
            "model": "gemini-1.5-flash-001",
            "api_key": "dummy_key",
            "temperature": 0.0,
            "max_tokens": 1024
        }

        # Mock the WebSocketManager
        self.websocket_manager = MagicMock(spec=WebSocketManager)
        self.websocket_manager.get_arcgis_client.return_value = "arcgis_pro_client_id"
        self.websocket_manager.send_to_client = AsyncMock()

        # Mock the LangChainAgent
        self.agent = LangChainAgent(model_key="GEMINI_FLASH", websocket_manager=self.websocket_manager)
        # Mock the agent_executor to avoid real AI calls
        self.agent.agent_executor = MagicMock()
        self.agent.agent_executor.ainvoke = AsyncMock()

    def tearDown(self):
        self.patcher.stop()

    def test_happy_path_tool_call(self):
        """
        Tests the happy path of a tool call from the agent to the WebSocket.
        """
        # 1. Simulate the AI deciding to call the 'Buffer_analysis' tool
        tool_input_str = "{'tool_name': 'Buffer_analysis', 'parameters': {'in_features': 'TestLayer', 'out_feature_class': 'TestBuffer', 'buffer_distance_or_field': '100 Meters'}}"

        # 2. Mock the websocket manager to return a successful result when checked
        session_id = "testsession"
        expected_result_from_pro = {
            "status": "success",
            "data": {
                "message": "Tool 'Buffer_analysis' executed successfully.",
                "output_path": "C:\\path\\to\\TestBuffer.shp"
            }
        }

        def has_result_side_effect(s_id):
            if s_id == session_id:
                return True
            return False

        def get_result_side_effect(s_id):
            if s_id == session_id:
                return expected_result_from_pro
            return None

        self.websocket_manager.has_function_result.side_effect = has_result_side_effect
        self.websocket_manager.get_function_result.side_effect = get_result_side_effect

        # 3. Execute the tool
        result = self.agent._execute_arcpy_tool(tool_input_str, session_id_for_test=session_id)

        # 4. Assertions
        # Assert that the websocket_manager was called to send a message
        self.websocket_manager.send_to_client.assert_called_once()

        # Get the payload that was sent
        call_args = self.websocket_manager.send_to_client.call_args
        sent_payload = call_args[0][1] # second argument of the call

        # Assert the payload has the correct structure
        self.assertEqual(sent_payload['type'], 'execute_tool')
        self.assertEqual(sent_payload['tool_name'], 'Buffer_analysis')
        self.assertEqual(sent_payload['parameters']['in_features'], 'TestLayer')
        self.assertIn('session_id', sent_payload)

        # Assert that the final result matches the mocked result from ArcGIS Pro
        self.assertEqual(result, expected_result_from_pro)

    def test_error_case_missing_params(self):
        """
        Tests an error case where a required parameter is missing.
        The server should send the request, and we expect an error back from the client.
        """
        tool_input_str = "{'tool_name': 'Buffer_analysis', 'parameters': {'in_features': 'TestLayer'}}" # Missing other params

        # Mock the websocket manager to return an error from "ArcGIS Pro"
        session_id = "testsession_error"
        error_result_from_pro = {
            "status": "error",
            "message": "ArcPy ExecuteError: Missing required parameter 'out_feature_class'"
        }

        def has_result_side_effect(s_id):
            return True

        def get_result_side_effect(s_id):
            return error_result_from_pro

        self.websocket_manager.has_function_result.side_effect = has_result_side_effect
        self.websocket_manager.get_function_result.side_effect = get_result_side_effect

        # Execute the tool
        result = self.agent._execute_arcpy_tool(tool_input_str, session_id_for_test=session_id)

        # Assert that the final result is the error message
        self.assertEqual(result, error_result_from_pro)

if __name__ == '__main__':
    unittest.main()
