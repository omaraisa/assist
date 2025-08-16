CREATE_BUFFER_CODE = """
import arcpy
import os
import json
import math

def _sanitize_output(result_dict):
    \"\"\"
    Sanitizes the output dictionary to remove sensitive information like absolute paths.
    Only allows specific keys in the final output.
    \"\"\"
    if not isinstance(result_dict, dict):
        return result_dict

    allowed_keys = {
        "function_executed",
        "layer_name",
        "success",
        "output_layer",
        "buffer_distance",
        "buffer_units",
        "error"
    }

    # Return a new dictionary with only the allowed keys
    return {key: value for key, value in result_dict.items() if key in allowed_keys}

def create_buffer(layer_name: str, distance: float, units: str = "meters"):
    \"\"\"
    Creates a buffer around features in a specified layer. This function is self-contained
    and designed to be executed in an ArcGIS Pro environment where arcpy is available.
    It does not use logging and returns a JSON-friendly dictionary.
    \"\"\"
    try:
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        map_obj = aprx.activeMap

        target_layer = None
        for layer in map_obj.listLayers():
            if layer.name == layer_name:
                target_layer = layer
                break

        if not target_layer:
            return {"success": False, "error": f"Layer '{layer_name}' not found in the map"}

        # Sanitize layer name for use in output path
        sanitized_layer_name = "".join(c for c in layer_name if c.isalnum() or c in (' ', '_')).rstrip()

        output_name = f"{sanitized_layer_name.replace(' ', '_')}_Buffer_{int(distance)}{units}"
        output_fc = os.path.join(aprx.defaultGeodatabase, output_name)

        # Ensure the output name is unique to avoid overwriting
        output_fc = arcpy.CreateUniqueName(output_fc)
        final_output_name = os.path.basename(output_fc)

        unit_mapping = {
            "meters": "METERS",
            "kilometers": "KILOMETERS",
            "feet": "FEET",
            "miles": "MILES"
        }
        arcpy_units = unit_mapping.get(units.lower())

        if not arcpy_units:
            return {"success": False, "error": f"Invalid units: '{units}'. Valid units are: {list(unit_mapping.keys())}"}

        arcpy.analysis.Buffer(
            in_features=target_layer,
            out_feature_class=output_fc,
            buffer_distance_or_field=f"{distance} {arcpy_units}",
            line_side="FULL",
            line_end_type="ROUND",
            dissolve_option="NONE"
        )

        # Add the new layer to the map
        map_obj.addDataFromPath(output_fc)

        result = {
            "function_executed": "create_buffer",
            "layer_name": layer_name,
            "success": True,
            "output_layer": final_output_name,
            "output_path": output_fc, # This will be sanitized out
            "buffer_distance": distance,
            "buffer_units": units
        }

        return result

    except Exception as e:
        return {"success": False, "error": str(e)}
"""
