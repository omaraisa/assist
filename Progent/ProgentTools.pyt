import arcpy
import sys
import os
import json
import traceback

class Toolbox:
    def __init__(self):
        self.label = "Progent Tools"
        self.alias = "progent"
        self.tools = [ExecuteFunctionTool]

class ExecuteFunctionTool:
    def __init__(self):
        self.label = "Execute Progent Function"
        self.description = "Executes a function from the spatial_functions module."
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Parameter 1: Function Name
        param_function_name = arcpy.Parameter(
            displayName="Function Name",
            name="function_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # Parameter 2: Parameters JSON
        param_parameters_json = arcpy.Parameter(
            displayName="Parameters JSON",
            name="parameters_json",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # Parameter 3: App Directory Path
        param_app_path = arcpy.Parameter(
            displayName="App Directory Path",
            name="app_path",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # Parameter 4: Output JSON
        param_output_json = arcpy.Parameter(
            displayName="Output JSON",
            name="output_json",
            datatype="GPString",
            parameterType="Derived",
            direction="Output")

        return [param_function_name, param_parameters_json, param_app_path, param_output_json]

    def execute(self, parameters, messages):
        function_name = parameters[0].valueAsText
        parameters_json = parameters[1].valueAsText
        app_path = parameters[2].valueAsText

        output_data = {}

        try:
            # Add the app directory to the path
            if app_path not in sys.path:
                sys.path.append(app_path)

            from spatial_functions import SpatialFunctions

            # Load parameters
            params = json.loads(parameters_json)

            # Execute function
            spatial_funcs = SpatialFunctions(arcpy.mp.ArcGISProject("CURRENT"))
            func = getattr(spatial_funcs, function_name)
            result = func(**params)

            output_data = {"status": "success", "data": result}

        except Exception as e:
            tb = traceback.format_exc()
            output_data = {"status": "error", "message": str(e), "traceback": tb}

        # Set the output parameter value
        output_json_str = json.dumps(output_data)
        arcpy.SetParameterAsText(3, output_json_str)
        messages.addMessage(f"Result: {output_json_str}")
        return
