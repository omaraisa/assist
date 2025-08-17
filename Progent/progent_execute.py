import sys
import json
import os
import traceback

# The 'spatial_functions.py' is now in the same directory as this script.
# No need to modify sys.path.

try:
    from spatial_functions import SpatialFunctions
except ImportError:
    # Backup: search for spatial_functions.py and load it dynamically
    import pathlib
    import importlib.util
    
    script_dir = pathlib.Path(__file__).parent
    
    # Search in common locations
    search_paths = [
        script_dir / "spatial_functions.py",
        script_dir.parent / "spatial_functions.py", 
        script_dir.parent / "Progent" / "spatial_functions.py",
        pathlib.Path.cwd() / "Progent" / "spatial_functions.py",
        pathlib.Path.cwd() / "spatial_functions.py"
    ]
    
    SpatialFunctions = None
    for path in search_paths:
        if path.exists():
            try:
                spec = importlib.util.spec_from_file_location("spatial_functions", str(path))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                SpatialFunctions = getattr(module, 'SpatialFunctions')
                break
            except Exception:
                continue
    
    if SpatialFunctions is None:
        raise ImportError("Could not find or load spatial_functions.py from any search location")

def main():
    try:
        # Support two calling styles:
        # 1) prog.py <function_name> <parameters_json>
        # 2) prog.py <function_name> --paramsfile <path_to_json_file>
        if len(sys.argv) == 3:
            function_name = sys.argv[1]
            parameters_json = sys.argv[2]
            parameters = json.loads(parameters_json)
        elif len(sys.argv) == 4 and sys.argv[2] == "--paramsfile":
            function_name = sys.argv[1]
            params_path = sys.argv[3]
            with open(params_path, "r", encoding="utf-8") as f:
                parameters = json.load(f)
        else:
            print(json.dumps({"status": "error", "message": "Invalid arguments. Use: <function_name> <parameters_json> or <function_name> --paramsfile <path>"}))
            return

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
