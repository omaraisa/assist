import sys
import json
import traceback
import importlib

# It's crucial that arcpy is available in the environment where this script is run.
# The ArcGIS Pro Python environment should be used.
try:
    import arcpy
except ImportError:
    # This block allows the script to fail gracefully if arcpy is not found.
    # The JSON output will report the error to the calling process.
    print(json.dumps({
        "status": "error",
        "message": "Failed to import arcpy. This script must be run in an ArcGIS Pro Python environment.",
        "traceback": traceback.format_exc()
    }))
    sys.exit(1)

def execute_arcpy_tool(tool_name: str, parameters: dict) -> dict:
    """
    Dynamically finds and executes an arcpy tool with the given parameters.
    It searches for the tool in the top-level arcpy module and then in common toolboxes.

    Args:
        tool_name (str): The name of the arcpy tool to execute (e.g., 'Buffer_analysis').
        parameters (dict): A dictionary of parameters for the tool.

    Returns:
        dict: A dictionary containing the result of the execution.
    """
    try:
        tool_function = None

        # 1. First, try to find the tool in the top-level arcpy module
        if hasattr(arcpy, tool_name):
            tool_function = getattr(arcpy, tool_name)

        # 2. If not found, search in common toolboxes
        else:
            # List of common toolbox modules to search within arcpy
            # Note: arcpy.<toolbox_alias> may not be loaded by default, so we import them.
            toolboxes_to_check = [
                "analysis", "management", "conversion", "data_management",
                "cartography", "spatial_analyst", "network_analyst", "geoanalytics"
            ]
            for toolbox_alias in toolboxes_to_check:
                try:
                    # Dynamically import the toolbox module
                    toolbox_module = importlib.import_module(f"arcpy.{toolbox_alias}")
                    if hasattr(toolbox_module, tool_name):
                        tool_function = getattr(toolbox_module, tool_name)
                        break # Found it, so exit the loop
                except ImportError:
                    # This toolbox may not be available/licensed, just skip it
                    continue

        if tool_function is None:
            raise AttributeError(f"Tool '{tool_name}' not found in arcpy or common toolboxes.")

        # Execute the tool using keyword arguments.
        # The parameters dictionary keys must match the arcpy tool's parameter names.
        result = tool_function(**parameters)

        # The result object from arcpy can be complex.
        # Often, we just want the output path, which can be retrieved by converting it to a string.
        output = str(result)

        # Some tools might return multiple outputs. getOutput() can be used.
        # For simplicity, we'll stick with the string representation for now.
        if hasattr(result, 'getOutput'):
            # This is a more robust way to get the primary output
            output = result.getOutput(0)

        return {
            "status": "success",
            "data": {
                "message": f"Tool '{tool_name}' executed successfully.",
                "output_path": output
            }
        }

    except arcpy.ExecuteError:
        # This catches errors from the execution of the tool itself (e.g., invalid parameters)
        return {
            "status": "error",
            "message": f"ArcPy ExecuteError executing '{tool_name}': {arcpy.GetMessages(2)}",
            "traceback": traceback.format_exc()
        }
    except Exception as e:
        # This catches other errors, like AttributeError if the tool doesn't exist
        # or TypeError if parameters are wrong.
        return {
            "status": "error",
            "message": f"An unexpected error occurred with tool '{tool_name}': {str(e)}",
            "traceback": traceback.format_exc()
        }

def main():
    """
    Main function to parse arguments and run the tool execution.
    The script expects a single argument: the path to a JSON file containing
    the tool name and parameters.
    """
    try:
        if len(sys.argv) != 2:
            print(json.dumps({
                "status": "error",
                "message": "Invalid arguments. Expected a single argument: path to a JSON parameters file."
            }))
            return

        params_path = sys.argv[1]
        with open(params_path, "r", encoding="utf-8") as f:
            request_data = json.load(f)

        tool_name = request_data.get("tool_name")
        parameters = request_data.get("parameters")

        if not tool_name or not isinstance(parameters, dict):
            print(json.dumps({
                "status": "error",
                "message": "Invalid JSON structure. 'tool_name' (string) and 'parameters' (dict) are required."
            }))
            return

        # Execute the tool and get the result
        result = execute_arcpy_tool(tool_name, parameters)

        # Print the final result as a single JSON string to stdout
        print(json.dumps(result, indent=4))

    except Exception as e:
        # Catch-all for any other errors during script execution (e.g., file not found)
        print(json.dumps({
            "status": "error",
            "message": f"A critical error occurred in the execution script: {str(e)}",
            "traceback": traceback.format_exc()
        }))

if __name__ == "__main__":
    main()
