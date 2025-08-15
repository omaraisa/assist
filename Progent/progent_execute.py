import sys
import json
import traceback

def main():
    try:
        input_data = sys.stdin.read()
        data = json.loads(input_data)

        code = data.get("code")
        function_name = data.get("function_name")
        parameters = data.get("parameters", {})

        if not code or not function_name:
            raise ValueError("'code' and 'function_name' must be provided.")

        exec_locals = {}
        exec(code, globals(), exec_locals)

        func = exec_locals.get(function_name)

        if not func:
            raise NameError(f"Function '{function_name}' not found after executing code.")

        result = func(**parameters)

        print(json.dumps({"status": "success", "data": result}))

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e), "traceback": traceback.format_exc()}))

if __name__ == "__main__":
    main()
