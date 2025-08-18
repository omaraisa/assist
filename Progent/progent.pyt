import arcpy

class RunPythonCode(object):
    def __init__(self):
        self.label = "RunPythonCode"
        self.description = "Test access to ArcGIS Pro's CURRENT project."
        # Ensure the tool runs in-process so arcpy.mp.ArcGISProject('CURRENT') is valid
        self.canRunInBackground = False

    def getParameterInfo(self):
        return []

    def execute(self, parameters, messages):
        # This tool must run in the ArcGIS Pro process so 'CURRENT' works
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        lyr = aprx.listMaps()[0].listLayers()[0]
        out_fc = f"{aprx.defaultGeodatabase}\\test_copy"
        arcpy.management.CopyFeatures(lyr, out_fc)
        messages.addMessage(f"Copied {lyr.name} to {out_fc}")


class Toolbox(object):
    def __init__(self):
        self.label = "Progent Toolbox"
        self.alias = "progent"
        self.tools = [RunPythonCode]
