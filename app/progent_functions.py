import json
import os
import uuid
import random
from datetime import datetime
from typing import Dict, List, Any
from .ai.function_declarations import FunctionDeclaration
from .dashboard_api import (
    mission_generate_dashboard,
    mission_get_layout,
    mission_get_charts,
    mission_get_field_info,
    mission_update_charts,
    mission_add_charts
)

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
    26: "clear_selection",
    27: "get_field_domain_values",
    28: "calculate_new_field",
    37: "raster_calculator",
    38: "reclassify",
    39: "zonal_statistics_as_table",
    40: "slope",
    41: "aspect",
    42: "hillshade",
    43: "extract_by_mask",
    44: "clip_raster",
    45: "resample",
    46: "get_raster_properties",
    47: "raster_to_point",
    48: "raster_to_polygon",
    49: "raster_to_polyline",
    50: "feature_to_raster",
    51: "polygon_to_raster",
    52: "point_to_raster",
    53: "idw_interpolation",
    54: "kriging_interpolation",
    55: "spline_interpolation",
    56: "natural_neighbor",
    57: "euclidean_distance",
    58: "euclidean_allocation",
    59: "euclidean_direction",
    60: "cost_distance",
    61: "cost_allocation",
    62: "cost_path",
    63: "weighted_overlay",
    64: "weighted_sum",
    65: "extract_by_attribute",
    66: "mosaic_to_new_raster",
    67: "combine_rasters",
    68: "invert_selection",
    # New dashboard functions
    70: "mission_generate_dashboard",
    71: "mission_get_layout",
    72: "mission_get_charts",
    73: "mission_get_field_info",
    74: "mission_update_charts",
    75: "mission_add_charts",
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

