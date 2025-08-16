import sys
import json
import io
import contextlib
import traceback

def execute_code(payload_str: str):
    """
    Executes a function from a given Python code string with specified parameters.
    Captures stdout/stderr, sanitizes the result, and prints a final JSON object.
    """
    status = "success"
    data = None
    captured_output = ""

    try:
        payload = json.loads(payload_str)
        code_to_exec = payload.get("code")
        function_name = payload.get("function_name")
        parameters = payload.get("parameters", {})

        if not all([code_to_exec, function_name]):
            raise ValueError("Payload must include 'code' and 'function_name'.")

        # Prepare execution environment
        exec_globals = {}

        # Make arcpy available if it exists
        try:
            import arcpy
            exec_globals['arcpy'] = arcpy
        except ImportError:
            # If arcpy is not available, we can proceed for testing purposes.
            # The executed code should handle the ImportError if it truly needs arcpy.
            pass

        # Capture stdout and stderr
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
            exec(code_to_exec, exec_globals)

            function_to_call = exec_globals.get(function_name)
            if not callable(function_to_call):
                raise NameError(f"Function '{function_name}' not found in the provided code.")

            # The code string is expected to also define the sanitizer
            sanitizer = exec_globals.get('_sanitize_output')
            if not callable(sanitizer):
                 raise NameError(f"Function '_sanitize_output' not found in the provided code.")

            raw_result = function_to_call(**parameters)
            data = sanitizer(raw_result)

        captured_output += stdout_capture.getvalue()
        captured_output += stderr_capture.getvalue()

    except Exception as e:
        status = "error"
        # Use the result from the function if it's an error dict, otherwise format the exception
        if isinstance(data, dict) and 'error' in data:
            pass # Keep the data from the function's own error reporting
        else:
            data = {"error": str(e), "traceback": traceback.format_exc()}

        # Also append any captured output to the error message
        captured_output += stdout_capture.getvalue()
        captured_output += stderr_capture.getvalue()

    finally:
        # Ensure a single JSON object is printed to stdout
        final_result = {
            "status": status,
            "data": data,
            "_captured_output": captured_output.strip()
        }
        print(json.dumps(final_result))


def main():
    # Read the entire input from stdin as a single string
    # This is more robust for complex JSON than using sys.argv
    input_str = sys.stdin.read()
    if not input_str:
        print(json.dumps({"status": "error", "data": {"error": "No input received via stdin."}}))
        return

    execute_code(input_str)

if __name__ == "__main__":
    main()
