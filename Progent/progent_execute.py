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
        if len(sys.argv) != 3:
            print(json.dumps({"status": "error", "message": "Invalid number of arguments. Expected function_name and parameters_json."}))
            return

        function_name = sys.argv[1]
        parameters_json = sys.argv[2]
        parameters = json.loads(parameters_json)

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
