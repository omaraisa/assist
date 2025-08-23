from .ai.function_declarations import FunctionDeclaration

# Build AVAILABLE_FUNCTIONS dynamically from the authoritative declarations
# The numeric IDs are assigned deterministically based on the declaration order.

AVAILABLE_FUNCTIONS = {
    1: "select_by_attribute",
    2: "select_by_location",
    3: "get_field_statistics",
    4: "get_layer_summary",
    5: "calculate_area",
    6: "calculate_length",
    7: "get_centroid",
    8: "create_buffer",
    9: "spatial_join",
    10: "clip_layer",
    11: "calculate_distance",
    12: "get_current_project_path",
    13: "get_default_db_path",
    14: "get_field_definitions",
    15: "get_layer_type",
    16: "get_list_of_layer_fields",
    17: "get_data_source_info",
    18: "create_nearest_neighbor_layer",
    19: "get_unique_values_count",
    20: "calculate_empty_values",
    21: "get_map_layers_info",
    22: "get_map_tables_info",
    23: "get_values_frequency",
    24: "get_value_frequency",
    25: "get_coordinate_system",
    26: "get_attribute_table",
    27: "get_field_domain_values",
    28: "calculate_new_field",
    29: "analyze_layer_fields",
    30: "generate_smart_dashboard_layout",
    31: "optimize_dashboard_layout",
    32: "recommend_chart_types",
    33: "plan_dashboard_layout",
    34: "get_current_dashboard_layout",
    35: "get_field_stories_and_samples",
    36: "get_current_dashboard_charts",
    37: "update_dashboard_charts",
    38: "raster_calculator",
    39: "reclassify",
    40: "zonal_statistics_as_table",
    41: "slope",
    42: "aspect",
    43: "hillshade",
    44: "extract_by_mask",
    45: "clip_raster",
    46: "resample",
    47: "get_raster_properties",
    48: "raster_to_point",
    49: "raster_to_polygon",
    50: "raster_to_polyline",
    51: "feature_to_raster",
    52: "polygon_to_raster",
    53: "point_to_raster",
    54: "idw_interpolation",
    55: "kriging_interpolation",
    56: "spline_interpolation",
    57: "natural_neighbor",
    58: "euclidean_distance",
    59: "euclidean_allocation",
    60: "euclidean_direction",
    61: "cost_distance",
    62: "cost_allocation",
    63: "cost_path",
    64: "weighted_overlay",
    65: "weighted_sum",
    66: "extract_by_attribute",
    67: "mosaic_to_new_raster",
    68: "combine_rasters",
    69: "invert_selection"
}

try:
	decls = FunctionDeclaration.functions_declarations
	# Preserve declaration order; assign IDs starting at 1
	for i, name in enumerate(decls.keys(), start=1):
		AVAILABLE_FUNCTIONS[i] = name
except Exception:
	AVAILABLE_FUNCTIONS = {}

def format_available_functions() -> str:
	"""Return a compact single-line listing like '1: name, 2: name'"""
	parts = [f"{k}: {v}" for k, v in sorted(AVAILABLE_FUNCTIONS.items())]
	return ", ".join(parts)

