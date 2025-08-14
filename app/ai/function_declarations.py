"""
Function Declarations for AI Models
"""

class FunctionDeclaration:
    """Generate function declarations for different AI models"""
    
    # Note: All chart-related functions (e.g., chart recommendations, dashboard layout planning) do not accept more than two fields per chart.
    functions_declarations = {
        "select_by_attribute": {
            "name": "select_by_attribute",
            "description": "Execute attribute-based selection on a GIS layer using SQL-like WHERE clause conditions.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to perform selection on"
                },
                "where_clause": {
                    "type": "string",
                    "description": "SQL WHERE clause for attribute selection (e.g., 'POPULATION > 1000000')"
                },
                "selection_type": {
                    "type": "string",
                    "description": "Type of selection to perform",
                    "enum": ["NEW_SELECTION", "ADD_TO_SELECTION", "REMOVE_FROM_SELECTION", "SUBSET_SELECTION"],
                    "default": "NEW_SELECTION"
                }
            },
            "required": ["layer_name", "where_clause"]
        },
        # ... rest of the function declarations ...
        "recommend_chart_types": {
            "name": "recommend_chart_types",
            "description": (
                "Enhanced AI-Powered Chart Type Recommendation System (Step 3). "
                "Analyzes both single-field characteristics and multi-field relationships to recommend diverse chart types that avoid the 'too many histograms' problem. "
                "Features: field relationship detection for scatter plots/grouped charts, token-efficient AI prompts, chart diversity optimization, and integration with existing retry mechanisms. "
                "Note: No chart accepts more than two fields."
            ),
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to analyze for enhanced chart recommendations"
                },
                "target_field": {
                    "type": "string",
                    "description": "Optional specific field to focus chart recommendations on"
                }
            },
            "required": ["layer_name"]
        },
        "plan_dashboard_layout": {
            "name": "plan_dashboard_layout",
            "description": (
                "AI-Powered Dashboard Layout Planning System. Uses AI to create optimal dashboard layouts that maximize space utilization and visual effectiveness. "
                "Works with chart recommendations to create intelligent 12x6 grid layouts with proper positioning and sizing. "
                "Note: No chart accepts more than two fields."
            ),
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to plan dashboard layout for"
                },
                "chart_recommendations": {
                    "type": "array",
                    "description": (
                        "Optional array of chart recommendation objects. If not provided, will use existing recommendations or generate new ones. "
                        "Note: Each chart recommendation must not contain more than two fields."
                    ),
                    "items": {
                        "type": "object"
                    }
                }
            },
            "required": ["layer_name"]
        },

        "raster_calculator": {
            "name": "raster_calculator",
            "description": "Performs a raster calculation using map algebra expressions. Example: NDVI = (NIR - Red) / (NIR + Red)",
            "parameters": {
                "expression": {"type": "string", "description": "Map algebra expression string"},
                "output_raster": {"type": "string", "description": "Path to save the output raster"}
            },
            "required": ["expression", "output_raster"]
        },
        "reclassify": {
            "name": "reclassify",
            "description": "Reclassifies raster values into new categories. reclass_map example: {1: 10, 2: 20, 3: 30}",
            "parameters": {
                "input_raster": {"type": "string", "description": "Input raster layer name"},
                "reclass_map": {"type": "object", "description": "Dictionary mapping old values to new values"},
                "output_raster": {"type": "string", "description": "Path to save the output raster"}
            },
            "required": ["input_raster", "reclass_map", "output_raster"]
        },
        "zonal_statistics_as_table": {
            "name": "zonal_statistics_as_table",
            "description": "Calculates statistics on raster values within the zones of another dataset.",
            "parameters": {
                "input_raster": {"type": "string", "description": "Input raster layer name"},
                "zone_layer": {"type": "string", "description": "Layer defining the zones"},
                "zone_field": {"type": "string", "description": "Field in zone layer to group statistics by"},
                "output_table": {"type": "string", "description": "Path to save the output table"},
                "statistics_type": {"type": "string", "description": "Statistic to calculate", "enum": ["MEAN", "MAJORITY", "MAXIMUM", "MEDIAN", "MINIMUM", "MINORITY", "RANGE", "STD", "SUM", "VARIETY"], "default": "MEAN"}
            },
            "required": ["input_raster", "zone_layer", "zone_field", "output_table"]
        },
        "raster_to_polygon": {
            "name": "raster_to_polygon",
            "description": "Converts raster cells into polygons.",
            "parameters": {
                "input_raster": {"type": "string", "description": "Input raster layer name"},
                "output_polygon": {"type": "string", "description": "Path to save the output polygon feature class"},
                "simplify": {"type": "boolean", "description": "Simplify polygon edges", "default": True}
            },
            "required": ["input_raster", "output_polygon"]
        },
        "slope": {
            "name": "slope",
            "description": "Calculates slope in degrees or percent rise from a DEM raster.",
            "parameters": {
                "input_dem": {"type": "string", "description": "Input DEM raster layer name"},
                "output_raster": {"type": "string", "description": "Path to save the output slope raster"},
                "measurement": {"type": "string", "description": "Units for slope calculation", "enum": ["DEGREE", "PERCENT_RISE"], "default": "DEGREE"}
            },
            "required": ["input_dem", "output_raster"]
        },
        "aspect": {
            "name": "aspect",
            "description": "Calculates the compass direction of slope faces.",
            "parameters": {
                "input_dem": {"type": "string", "description": "Input DEM raster layer name"},
                "output_raster": {"type": "string", "description": "Path to save the output aspect raster"}
            },
            "required": ["input_dem", "output_raster"]
        },
        "hillshade": {
            "name": "hillshade",
            "description": "Generates a shaded relief raster from a surface raster.",
            "parameters": {
                "input_dem": {"type": "string", "description": "Input DEM raster layer name"},
                "output_raster": {"type": "string", "description": "Path to save the output hillshade raster"},
                "azimuth": {"type": "number", "description": "Azimuth angle of the light source", "default": 315},
                "altitude": {"type": "number", "description": "Altitude angle of the light source", "default": 45}
            },
            "required": ["input_dem", "output_raster"]
        },
        "extract_by_mask": {
            "name": "extract_by_mask",
            "description": "Extracts raster cells within the mask layer boundary.",
            "parameters": {
                "input_raster": {"type": "string", "description": "Input raster layer name"},
                "mask_layer": {"type": "string", "description": "Layer to use as a mask"},
                "output_raster": {"type": "string", "description": "Path to save the output raster"}
            },
            "required": ["input_raster", "mask_layer", "output_raster"]
        },
        "clip_raster": {
            "name": "clip_raster",
            "description": "Clips a raster to a specified rectangular extent. extent format: (xmin, ymin, xmax, ymax)",
            "parameters": {
                "input_raster": {"type": "string", "description": "Input raster layer name"},
                "extent": {"type": "array", "items": {"type": "number"}, "description": "Clipping extent as a tuple (xmin, ymin, xmax, ymax)"},
                "output_raster": {"type": "string", "description": "Path to save the output raster"}
            },
            "required": ["input_raster", "extent", "output_raster"]
        },
        "resample": {
            "name": "resample",
            "description": "Changes raster cell size using specified resampling method.",
            "parameters": {
                "input_raster": {"type": "string", "description": "Input raster layer name"},
                "output_raster": {"type": "string", "description": "Path to save the output raster"},
                "cell_size": {"type": "number", "description": "New cell size for the output raster"},
                "resampling_type": {"type": "string", "description": "Resampling method", "enum": ["NEAREST", "BILINEAR", "CUBIC"], "default": "NEAREST"}
            },
            "required": ["input_raster", "output_raster", "cell_size"]
        },
        "invert_selection": {
            "name": "invert_selection",
            "description": "Inverts the current selection for a given layer. All selected features become unselected, and all unselected features become selected.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to invert the selection for"}
            },
            "required": ["layer_name"]
        },
        "dissolve_layer": {
            "name": "dissolve_layer",
            "description": "Dissolves features in a layer based on a specified attribute field.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to dissolve"},
                "dissolve_field": {"type": "string", "description": "The field to dissolve features on"},
                "output_name": {"type": "string", "description": "The name of the output dissolved layer"}
            },
            "required": ["layer_name", "dissolve_field", "output_name"]
        },
        "add_field": {
            "name": "add_field",
            "description": "Adds a new field to a layer's attribute table.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to add the field to"},
                "field_name": {"type": "string", "description": "The name of the new field"},
                "field_type": {"type": "string", "description": "The data type of the new field", "enum": ["TEXT", "FLOAT", "DOUBLE", "SHORT", "LONG", "DATE"], "default": "TEXT"}
            },
            "required": ["layer_name", "field_name"]
        },
        "delete_field": {
            "name": "delete_field",
            "description": "Deletes a field from a layer's attribute table.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to delete the field from"},
                "field_name": {"type": "string", "description": "The name of the field to delete"}
            },
            "required": ["layer_name", "field_name"]
        },
        "get_layer_count": {
            "name": "get_layer_count",
            "description": "Gets the total number of features in a layer.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to get the count from"}
            },
            "required": ["layer_name"]
        },
        "export_to_excel": {
            "name": "export_to_excel",
            "description": "Exports the attribute table of a layer to an Excel file.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to export"},
                "output_excel": {"type": "string", "description": "The path to the output Excel file"}
            },
            "required": ["layer_name", "output_excel"]
        },
        "create_feature_class": {
            "name": "create_feature_class",
            "description": "Creates a new, empty feature class in a specified geodatabase.",
            "parameters": {
                "out_path": {"type": "string", "description": "The path to the geodatabase where the feature class will be created"},
                "out_name": {"type": "string", "description": "The name of the new feature class"},
                "geometry_type": {"type": "string", "description": "The geometry type of the new feature class", "enum": ["POINT", "MULTIPOINT", "POLYLINE", "POLYGON"], "default": "POINT"}
            },
            "required": ["out_path", "out_name"]
        },
        "get_selection_count": {
            "name": "get_selection_count",
            "description": "Gets the number of selected features in a layer.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to get the selection count from"}
            },
            "required": ["layer_name"]
        },
        "clear_selection": {
            "name": "clear_selection",
            "description": "Clears the current selection for a specified layer.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to clear the selection for"}
            },
            "required": ["layer_name"]
        },
        "zoom_to_layer": {
            "name": "zoom_to_layer",
            "description": "Zooms the map view to the full extent of a specified layer.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to zoom to"}
            },
            "required": ["layer_name"]
        },
        "get_map_extent": {
            "name": "get_map_extent",
            "description": "Gets the current extent of the active map.",
            "parameters": {},
            "required": []
        },
        "set_map_extent": {
            "name": "set_map_extent",
            "description": "Sets the extent of the active map to the specified coordinates.",
            "parameters": {
                "xmin": {"type": "number", "description": "The minimum x-coordinate of the extent"},
                "ymin": {"type": "number", "description": "The minimum y-coordinate of the extent"},
                "xmax": {"type": "number", "description": "The maximum x-coordinate of the extent"},
                "ymax": {"type": "number", "description": "The maximum y-coordinate of the extent"}
            },
            "required": ["xmin", "ymin", "xmax", "ymax"]
        },
        "add_layer_to_map": {
            "name": "add_layer_to_map",
            "description": "Adds a layer to the current map from a specified path.",
            "parameters": {
                "layer_path": {"type": "string", "description": "The path to the layer file to add"}
            },
            "required": ["layer_path"]
        },
        "remove_layer_from_map": {
            "name": "remove_layer_from_map",
            "description": "Removes a layer from the current map.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to remove"}
            },
            "required": ["layer_name"]
        },
        "get_layout_list": {
            "name": "get_layout_list",
            "description": "Gets a list of all layouts in the current ArcGIS Pro project.",
            "parameters": {},
            "required": []
        },
        "export_layout_to_pdf": {
            "name": "export_layout_to_pdf",
            "description": "Exports a specified layout to a PDF file.",
            "parameters": {
                "layout_name": {"type": "string", "description": "The name of the layout to export"},
                "output_pdf": {"type": "string", "description": "The path to the output PDF file"}
            },
            "required": ["layout_name", "output_pdf"]
        },
        "list_workspaces": {
            "name": "list_workspaces",
            "description": "Lists all workspaces in the current ArcGIS Pro project.",
            "parameters": {},
            "required": []
        },
        "list_feature_classes": {
            "name": "list_feature_classes",
            "description": "Lists all feature classes in a specified workspace or geodatabase.",
            "parameters": {
                "workspace": {"type": "string", "description": "The path to the workspace or geodatabase"}
            },
            "required": ["workspace"]
        },
        "get_raster_properties": {
            "name": "get_raster_properties",
            "description": "Gets key properties of a raster layer, such as band count and pixel type.",
            "parameters": {
                "raster_name": {"type": "string", "description": "The name of the raster layer"}
            },
            "required": ["raster_name"]
        },
        "get_vector_properties": {
            "name": "get_vector_properties",
            "description": "Gets key properties of a vector layer, such as shape type and feature type.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the vector layer"}
            },
            "required": ["layer_name"]
        }
    }
