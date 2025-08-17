import arcpy

class Toolbox:
    def __init__(self):
        self.label = "Progent Tools"
        self.alias = "progent"
        self.tools = [RunPythonCode]

class RunPythonCode:
    def __init__(self):
        self.label = "Run Python Code"
        self.description = "Executes a block of Python code provided by the Progent AI assistant."
        self.canRunInBackground = False

    def getParameterInfo(self):
        param = arcpy.Parameter(
            displayName="Python Code",
            name="python_code",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        return [param]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        import json
        import traceback
        from progent_helpers import select_by_attribute, create_buffer, clip_layer, get_layer_summary, get_field_statistics, select_by_location

        code_to_execute = parameters[0].valueAsText

        # Prepare a dictionary to hold the globals and locals for exec
        exec_globals = {
            'arcpy': arcpy,
            'result': None,  # The executed code should set this variable
            'select_by_attribute': select_by_attribute,
            'create_buffer': create_buffer,
            'clip_layer': clip_layer,
            'get_layer_summary': get_layer_summary,
            'get_field_statistics': get_field_statistics,
            'select_by_location': select_by_location,
        }

        try:
            exec(code_to_execute, exec_globals)

            # The executed code is expected to set a variable named 'result'
            output = exec_globals.get('result')

            response = {
                "status": "success",
                "data": output
            }
            messages.addMessage(json.dumps(response))

        except Exception as e:
            error_message = str(e)
            traceback_info = traceback.format_exc()
            response = {
                "status": "error",
                "message": error_message,
                "traceback": traceback_info
            }
            # Add error message for debugging in Pro
            messages.addErrorMessage(f"Error executing script: {error_message}")
            messages.addErrorMessage(f"Traceback: {traceback_info}")
            # Also return as a JSON message for the application
            messages.addMessage(json.dumps(response))

        return
