import sys
import json
import os
import traceback

# Add the 'app' directory to the Python path
# This is a relative path from the location of this script
progent_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.abspath(os.path.join(progent_dir, '..', 'app'))
if app_dir not in sys.path:
    sys.path.append(app_dir)

from spatial_functions import SpatialFunctions

def main():
    try:
        input_data = sys.stdin.read()
        data = json.loads(input_data)
        function_name = data.get("function_name")
        parameters = data.get("parameters", {})

        if not function_name:
            raise ValueError("function_name not provided in input JSON.")

        spatial_functions = SpatialFunctions(None)

        if not hasattr(spatial_functions, function_name):
            raise Exception(f"Function '{function_name}' not found in SpatialFunctions")

        func = getattr(spatial_functions, function_name)
        result = func(**parameters)

        print(json.dumps({"status": "success", "data": result}))

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e), "traceback": traceback.format_exc()}))

if __name__ == "__main__":
    main()
