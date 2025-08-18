import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Progent Toolbox"
        self.alias = "progent"
        self.tools = [TestCurrentProject]

class TestCurrentProject(object):
    def __init__(self):
        self.label = "RunPythonCode"
        self.description = "Test access to ArcGIS Pro's CURRENT project."

    def getParameterInfo(self):
        return []

    def execute(self, parameters, messages):
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        lyr = aprx.listMaps()[0].listLayers()[0]
        out_fc = f"{aprx.defaultGeodatabase}\\test_copy"
        arcpy.management.CopyFeatures(lyr, out_fc)
        messages.addMessage(f"Copied {lyr.name} to {out_fc}")
