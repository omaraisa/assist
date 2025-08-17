
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

    def test_happy_path_function_call(self):
        """
        Tests the happy path of a function call from the agent to the WebSocket.
        """
        # 1. Simulate the AI deciding to call the 'create_buffer' function
        tool_input_str = "{'function_name': 'create_buffer', 'layer_name': 'TestLayer', 'distance': 100}"

        # 2. Mock the websocket manager to return a successful result when checked
        session_id = "testsession"
        expected_result_from_pro = {
            "success": True,
            "output_layer": "TestLayer_Buffer_100meters"
        }

        def has_result_side_effect(s_id):
            if s_id == session_id:
                return True
            return False

        def get_result_side_effect(s_id):
            if s_id == session_id:
                return {"data": expected_result_from_pro}
            return None

        self.websocket_manager.has_function_result.side_effect = has_result_side_effect
        self.websocket_manager.get_function_result.side_effect = get_result_side_effect

        # 3. Execute the function
        result = self.agent._execute_spatial_function(tool_input_str, session_id_for_test=session_id)

        # 4. Assertions
        # Assert that the websocket_manager was called to send a message
        self.websocket_manager.send_to_client.assert_called_once()

        # Get the payload that was sent
        call_args = self.websocket_manager.send_to_client.call_args
        sent_payload = call_args[0][1] # second argument of the call

        # Assert the payload has the correct structure
        self.assertEqual(sent_payload['type'], 'execute_function')
        self.assertEqual(sent_payload['function_name'], 'create_buffer')
        self.assertEqual(sent_payload['parameters']['layer_name'], 'TestLayer')
        self.assertIn('session_id', sent_payload)

        # Assert that the final result matches the mocked result from ArcGIS Pro
        self.assertEqual(result, expected_result_from_pro)

    def test_error_case_missing_params(self):
        """
        Tests an error case where a required parameter is missing.
        This test checks the internal logic before the websocket call.
        """
        # The agent tries to call a function but omits a required parameter.
        # In the new architecture, the server doesn't know about required params,
        # so it will send the request, and we expect an error back from the client.
        tool_input_str = "{'function_name': 'create_buffer', 'layer_name': 'TestLayer'}" # Missing 'distance'

        # Mock the websocket manager to return an error from "ArcGIS Pro"
        session_id = "testsession"
        error_result_from_pro = {
            "success": False,
            "error": "Missing required parameter: distance"
        }

        def has_result_side_effect(s_id):
            return True

        def get_result_side_effect(s_id):
            return {"data": error_result_from_pro}

        self.websocket_manager.has_function_result.side_effect = has_result_side_effect
        self.websocket_manager.get_function_result.side_effect = get_result_side_effect

        # Execute the function
        result = self.agent._execute_spatial_function(tool_input_str)

        # Assert that the final result is the error message
        self.assertEqual(result, error_result_from_pro)

if __name__ == '__main__':
    unittest.main()
