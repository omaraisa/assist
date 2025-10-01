# Generated ArcGIS Pro spatial-analyst AI Function Declarations
# Generated on 2025-10-01T14:46:02.622055
# Total tools: 208

functions_declarations = {
    "raster_calculator": {
        "name": "raster_calculator",
        "description": "Build and run a single map algebra expression using Python syntax. Learn more about how Raster Calculator works",
        "parameters": {
                "expression": {
                        "type": "string",
                        "description": "Note:In Python, create and run map algebra expressions using the Spatial Analyst module, which is an extension of the ArcPy Python site package.See Map algebra to learn how to perform an analysis in P..."
                },
                "output_raster": {
                        "type": "string",
                        "description": "Note:See Create output for information about producing output from map algebra expressions in Python."
                }
        },
        "required": [
                "expression",
                "output_raster"
        ]
},
    "con": {
        "name": "con",
        "description": "Performs a conditional if/else evaluation on each of the input cells of an input raster. Learn more about performing conditional evaluation with Con",
        "parameters": {
                "in_conditional_raster": {
                        "type": "string",
                        "description": "The input raster representing the true or false result of the desired condition.It can be of integer or floating point type."
                },
                "in_true_raster_or_constant": {
                        "type": "string",
                        "description": "The input whose values will be used as the output cell values if the condition is true.It can be an integer or a floating-point raster, or a constant value."
                },
                "in_false_raster_or_constant": {
                        "type": "string",
                        "description": "The input whose values will be used as the output cell values if the condition is false.It can be an integer or a floating-point raster, or a constant value.",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "A logical expression that determines which of the input cells are to be true or false.\r\n\r\nThe expression follows the general form of an SQL expression. An example of a where_clause is \"VALUE &gt; 100\"...",
                        "default": None
                }
        },
        "required": [
                "in_conditional_raster",
                "in_true_raster_or_constant"
        ]
},
    "pick": {
        "name": "pick",
        "description": "The value from a position raster is used to determine from which raster in a list of input rasters the output cell value will be obtained.",
        "parameters": {
                "in_position_raster": {
                        "type": "string",
                        "description": "The input raster defining the position of the raster to use for the output value.The input can be an integer or float raster."
                },
                "in_rasters_or_constantsin_raster_or_constant": {
                        "type": "string",
                        "description": "The list of inputs from which the output value will be selected.The inputs can be integer or float rasters. A number can also be used as an input."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.SINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_BAN...",
                        "default": None
                }
        },
        "required": [
                "in_position_raster",
                "in_rasters_or_constantsin_raster_or_constant"
        ]
},
    "set_None": {
        "name": "set_None",
        "description": "Set Null sets identified cell locations to NoData based on a specified criteria. It returns NoData if a conditional evaluation is true, and returns the value specified by another raster if it is false. Learn more about setting cell values to NoData with Set Null",
        "parameters": {
                "in_conditional_raster": {
                        "type": "string",
                        "description": "The input raster representing the true or false result of the desired condition.It can be of integer or floating point type."
                },
                "in_false_raster_or_constant": {
                        "type": "string",
                        "description": "The input whose values will be used as the output cell values if the condition is false.It can be an integer or a floating-point raster, or a constant value."
                },
                "where_clause": {
                        "type": "string",
                        "description": "A logical expression that determines which of the input cells are to be true or false.\r\nThe expression follows the general form of an SQL expression. An example of a where_clause is \"VALUE &gt; 100\".",
                        "default": None
                }
        },
        "required": [
                "in_conditional_raster",
                "in_false_raster_or_constant"
        ]
},
    "calculate_kernel_density_ratio": {
        "name": "calculate_kernel_density_ratio",
        "description": "Calculates a spatial relative risk surface using two input feature datasets. The numerator in the ratio represents cases, such as number of crimes or number of patients, and the denominator represents the control, such as the total population.",
        "parameters": {
                "in_features_numerator": {
                        "type": "string",
                        "description": "The input features (point or line) of the cases for which density will be calculated."
                },
                "in_features_denominator": {
                        "type": "string",
                        "description": "The input features (point or line) of the control for which density will be calculated."
                },
                "population_field_numerator": {
                        "type": "string",
                        "description": "The field denoting population values for each feature. The population field is the count or quantity to be spread across the landscape to create a continuous surface. Use\u202fOID or FID    if no item or s..."
                },
                "population_field_denominator": {
                        "type": "string",
                        "description": "The field denoting population values for each feature. The population field is the count or quantity to be spread across the landscape to create a continuous surface. Use\u202fOID or FID    if no item or s..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "search_radius_numerator": {
                        "type": "string",
                        "description": "The search radius within which density will be calculated. Units are based on the linear unit of the projection of the output spatial reference.For example, if the units are meters\u2014to include all feat...",
                        "default": None
                },
                "search_radius_denominator": {
                        "type": "string",
                        "description": "The search radius within which density will be calculated. Units are based on the linear unit of the projection of the output spatial reference.For example, if the units are meters\u2014to include all feat...",
                        "default": None
                },
                "out_cell_values": {
                        "type": "string",
                        "description": "Specifies what the values in the output raster represent.DENSITIES\u2014The output values represent the calculated density value per unit area for each cell. This is the default.EXPECTED_COUNTS\u2014The output ...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the flat earth (planar) or the shortest path on a spheroid (geodesic) distance will be used.PLANAR\u2014The planar distance between features will be used. This is the default.GEODESIC\u2014The...",
                        "default": None
                },
                "in_barriers_numerator": {
                        "type": "string",
                        "description": "The dataset that defines the barriers. The barriers can be a feature layer of polyline or polygon features.",
                        "default": None
                },
                "in_barriers_denominator": {
                        "type": "string",
                        "description": "The dataset that defines the barriers.The barriers can be a feature layer of polyline or polygon features.",
                        "default": None
                }
        },
        "required": [
                "in_features_numerator",
                "in_features_denominator",
                "population_field_numerator",
                "population_field_denominator"
        ]
},
    "kernel_density": {
        "name": "kernel_density",
        "description": "Calculates a magnitude-per-unit area from point or polyline features using a kernel function to fit a smoothly tapered surface to each point or polyline. A barrier can be used to alter the influence of a feature while calculating kernel density. Learn more about how Kernel Density works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features (point or line) for which to calculate the density."
                },
                "population_field": {
                        "type": "string",
                        "description": "The field denoting population values for each feature. The population field is the count or quantity to be spread across the landscape to create a continuous surface.Values in the population field can..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "The search radius within which density will be calculated. Units are based on the linear unit of the projection of the output spatial reference.For example, if the units are meters\u2014to include all feat...",
                        "default": None
                },
                "area_unit_scale_factor": {
                        "type": "string",
                        "description": "Specifies the area units that will be used for the output density values.A default unit is determined based on the linear unit of the output spatial reference. You can change this to the appropriate u...",
                        "default": None
                },
                "out_cell_values": {
                        "type": "string",
                        "description": "Specifies what the values in the output raster represent.DENSITIES\u2014The output values represent the calculated density value per unit area for each cell. This is the default.EXPECTED_COUNTS\u2014The output ...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the flat earth (planar) or the shortest path on a spheroid (geodesic) method will be used.PLANAR\u2014The planar distance between features will be used. This is the default.GEODESIC\u2014The g...",
                        "default": None
                },
                "in_barriers": {
                        "type": "string",
                        "description": "The dataset that defines the barriers.The barriers can be a feature layer of polyline or polygon features.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "population_field"
        ]
},
    "line_density": {
        "name": "line_density",
        "description": "Calculates a magnitude-per-unit area from polyline features that fall within a radius around each cell. Learn more about how Line Density works",
        "parameters": {
                "in_polyline_features": {
                        "type": "string",
                        "description": "The input line features for which to calculate the density."
                },
                "population_field": {
                        "type": "string",
                        "description": "Numeric field denoting population values (the number of times the line should be counted) for each polyline.Values in the population field can be integer or floating point.The options and default beha..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "The search radius within which density will be calculated. Units are based on the linear unit of the projection of the output spatial reference.For example, if the units are meters\u2014to include all feat...",
                        "default": None
                },
                "area_unit_scale_factor": {
                        "type": "string",
                        "description": "Specifies the area units that will be used for the output density values.A default unit is determined based on the linear unit of the output spatial reference. You can change this to the appropriate u...",
                        "default": None
                }
        },
        "required": [
                "in_polyline_features",
                "population_field"
        ]
},
    "point_density": {
        "name": "point_density",
        "description": "Calculates a magnitude-per-unit area from point features that fall within a neighborhood around each cell. Learn more about how Point Density works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features for which to calculate the density."
                },
                "population_field": {
                        "type": "string",
                        "description": "Field denoting population values for each point. The population field is the count or quantity to be used in the calculation of a continuous surface.Values in the population field can be integer or fl..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "neighborhood": {
                        "type": "string",
                        "description": "Dictates the shape of the area around each cell used to calculate the density value.This is a Neighborhood class.There are four types of neighbourhood class: NbrAnnulus, NbrCircle, NbrRectangle, and N...",
                        "default": None
                },
                "area_unit_scale_factor": {
                        "type": "string",
                        "description": "Specifies the area units that will be used for the output density values.A default unit is determined based on the linear unit of the output spatial reference. You can change this to the appropriate u...",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "population_field"
        ]
},
    "space_time_kernel_density": {
        "name": "space_time_kernel_density",
        "description": "Expands kernel density calculations from analyzing the relative position and magnitude of the input features to include other dimensions such as time and depth (elevation). The resulting output identifies the magnitude-per-unit area using the multiple kernel functions to fit a smoothly tapered surface to each input point. Learn more about how Space Time Kernel Density works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features for which density will be calculated."
                },
                "population_field": {
                        "type": "string",
                        "description": "The field denoting population values for each feature. The population is the count or quantity to be spread across the landscape to create a continuous surface.Values in the population field can be in..."
                },
                "elevation_field": {
                        "type": "string",
                        "description": "The field denoting elevation values for each feature.Values in the elevation field can be integer or floating point.\r\nUse '' to support 3D kernel density with time.\r\nFor 3D features, a pseudo field, S...",
                        "default": None
                },
                "elevation_field_unit": {
                        "type": "string",
                        "description": "Specifies the unit of measure that will be used for the input elevation field value. The default is meters.\r\nUse the appropriate unit to represent the values in the elevation_field parameter value.\r\n\r...",
                        "default": None
                },
                "time_field": {
                        "type": "string",
                        "description": "The field denoting time values for each feature.",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the multidimensional raster output that will be created.The value can be defined by a numeric value or obtained from an existing raster dataset. If no cell size is provided, the envir...",
                        "default": None
                },
                "kernel_search_radius_xy": {
                        "type": "string",
                        "description": "The search radius on the x,y plane within which density will be calculated.\r\nProvide the value and the appropriate units. For example, to include all features within a 1-mile neighborhood when the uni...",
                        "default": None
                },
                "kernel_search_radius_z": {
                        "type": "string",
                        "description": "The vertical search distance in the z-direction within which density will be calculated. This vertical distance will be used to search for features in the upward and downward directions along the z-ax...",
                        "default": None
                },
                "kernel_search_time_window": {
                        "type": "string",
                        "description": "The search range of time within which density will be calculated.\r\nProvide the value and the appropriate units.",
                        "default": None
                },
                "resultant_values": {
                        "type": "string",
                        "description": "Specifies what the values in the output raster will represent.Since the output cell value is related to the specified cell size, the resulting raster cannot be resampled to a different cell size.\r\n\r\nD...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the flat earth (planar) or the shortest path on a spheroid (geodesic) method will be used.PLANAR\u2014The planar distance between features will be used. This is the default.GEODESIC\u2014The g...",
                        "default": None
                },
                "min_elevation": {
                        "type": "string",
                        "description": "The minimum (lowest) elevation that will be used for the multidimensional raster output.",
                        "default": None
                },
                "max_elevation": {
                        "type": "string",
                        "description": "The maximum (highest) elevation that will be used for the multidimensional raster output.",
                        "default": None
                },
                "elevation_interval": {
                        "type": "string",
                        "description": "The elevation interval between slices in the multidimensional raster output.The value must be greater than zero.",
                        "default": None
                },
                "elevation_unit": {
                        "type": "string",
                        "description": "Specifies the unit of elevation interval that will be used for the multidimensional raster output. The default is meter.INCH\u2014Inches will be used.FOOT\u2014Feet will be used. YARD\u2014Yards will be used.MILE_US...",
                        "default": None
                },
                "start_time": {
                        "type": "string",
                        "description": "The start time that will be used for the multidimensional raster output.",
                        "default": None
                },
                "end_time": {
                        "type": "string",
                        "description": "The end time that will be used for the multidimensional raster output.",
                        "default": None
                },
                "time_interval": {
                        "type": "string",
                        "description": "The time interval between slices in the multidimensional raster output.The value must be greater than zero.",
                        "default": None
                },
                "time_interval_unit": {
                        "type": "string",
                        "description": "Specifies the unit of the time interval that will be used for the multidimensional raster output. The default is day.SECOND\u2014The time interval unit will be seconds.MINUTE\u2014The time interval unit will be...",
                        "default": None
                },
                "out_voxel_layer": {
                        "type": "string",
                        "description": "The output voxel layer based on volumetric data stored in the output netCDF raster.\r\n\r\n\r\nThis output type can only be created when the out_raster parameter is set to create a netCDF raster with the .n...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "population_field"
        ]
},
    "distance_accumulation": {
        "name": "distance_accumulation",
        "description": "Calculates accumulated distance for each cell to sources, allowing for straight-line distance, cost distance, and true surface distance, as well as vertical and horizontal cost factors. Learn more about how the distance accumulation tools work",
        "parameters": {
                "in_source_data": {
                        "type": "string",
                        "description": "The input source locations.This is a raster or feature (point, line, or polygon) identifying the cells or locations that will be used to calculate the least accumulated cost distance for each output c..."
                },
                "in_barrier_data": {
                        "type": "string",
                        "description": "The dataset that defines the barriers.The barriers can be defined by an integer or a floating-point raster, or by a point, line, or polygon feature.For a raster barrier, the barrier must have a valid ...",
                        "default": None
                },
                "in_surface_raster": {
                        "type": "string",
                        "description": "A raster defining the elevation values at each cell location.The values are used to calculate the actual surface distance covered when passing between cells.",
                        "default": None
                },
                "in_cost_raster": {
                        "type": "string",
                        "description": "A raster defining the impedance or cost to move planimetrically through each cell.The value at each cell location represents the cost-per-unit distance for moving through the cell. Each cell location ...",
                        "default": None
                },
                "in_vertical_raster": {
                        "type": "string",
                        "description": "A raster defining the z-values for each cell location.The values are used for calculating the slope used to identify the vertical factor incurred when moving from one cell to another.",
                        "default": None
                },
                "vertical_factor": {
                        "type": "string",
                        "description": "The Vertical factor object defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA).There are several factors with modifiers that identify a defined vert...",
                        "default": None
                },
                "in_horizontal_raster": {
                        "type": "string",
                        "description": "A raster defining the horizontal direction at each cell.The values on the raster must be integers ranging from 0 to 360, with 0 degrees being north, or toward the top of the screen, and increasing clo...",
                        "default": None
                },
                "horizontal_factor": {
                        "type": "string",
                        "description": "The Horizontal Factor object defines the relationship between the horizontal cost factor and the horizontal relative moving angle.There are several factors with modifiers that identify a defined horiz...",
                        "default": None
                },
                "out_back_direction_raster": {
                        "type": "string",
                        "description": "The back direction raster contains the calculated direction in degrees. The direction identifies the next cell along the shortest path back to the closest source while avoiding barriers.The range of v...",
                        "default": None
                },
                "out_source_direction_raster": {
                        "type": "string",
                        "description": "The source direction raster identifies the direction of the least accumulated cost source cell as an azimuth in degrees.The range of values is from 0 degrees to 360 degrees, with 0 reserved for the so...",
                        "default": None
                },
                "out_source_location_raster": {
                        "type": "string",
                        "description": "The source location raster is a multiband output. The first band contains a row index, and the second band contains a column index. These indexes identify the location of the source cell that is the l...",
                        "default": None
                },
                "source_initial_accumulation": {
                        "type": "string",
                        "description": "The initial accumulative cost that will be used to begin the cost calculation.Allows for the specification of the fixed cost associated with a source. Instead of starting at a cost of zero, the cost a...",
                        "default": None
                },
                "source_maximum_accumulation": {
                        "type": "string",
                        "description": "The maximum accumulation for the traveler for a source.The cost calculations continue for each source until the specified accumulation is reached.The values must be greater than zero. The default accu...",
                        "default": None
                },
                "source_cost_multiplier": {
                        "type": "string",
                        "description": "The multiplier that will be applied to the cost values.This allows for control of the mode of travel or the magnitude at a source. The greater the multiplier, the greater the cost to move through each...",
                        "default": None
                },
                "source_direction": {
                        "type": "string",
                        "description": "Specifies the direction of the traveler when applying horizontal and vertical factors.FROM_SOURCE\u2014The horizontal factor and vertical factor will be applied beginning at the input source and travel out...",
                        "default": None
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies whether the distance will be calculated using a planar (flat earth) or a geodesic (ellipsoid) method.PLANAR\u2014The distance calculation will be performed on a projected flat plane using a 2D Ca...",
                        "default": None
                }
        },
        "required": [
                "in_source_data"
        ]
},
    "distance_allocation": {
        "name": "distance_allocation",
        "description": "Calculates distance allocation for each cell to the provided sources based on straight-line distance, cost distance, and true surface distance, as well as vertical and horizontal cost factors. Learn more about how the distance accumulation tools work",
        "parameters": {
                "in_source_data": {
                        "type": "string",
                        "description": "The input source locations.This is a raster or feature (point, line, or polygon) identifying the cells or locations that will be used to calculate the least accumulated cost distance for each output c..."
                },
                "in_barrier_data": {
                        "type": "string",
                        "description": "The dataset that defines the barriers.The barriers can be defined by an integer or a floating-point raster, or by a point, line, or polygon feature.For a raster barrier, the barrier must have a valid ...",
                        "default": None
                },
                "in_surface_raster": {
                        "type": "string",
                        "description": "A raster defining the elevation values at each cell location.The values are used to calculate the actual surface distance covered when passing between cells.",
                        "default": None
                },
                "in_cost_raster": {
                        "type": "string",
                        "description": "A raster defining the impedance or cost to move planimetrically through each cell.The value at each cell location represents the cost-per-unit distance for moving through the cell. Each cell location ...",
                        "default": None
                },
                "in_vertical_raster": {
                        "type": "string",
                        "description": "A raster defining the z-values for each cell location.The values are used for calculating the slope used to identify the vertical factor incurred when moving from one cell to another.",
                        "default": None
                },
                "vertical_factor": {
                        "type": "string",
                        "description": "The Vertical factor object defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA).There are several factors with modifiers that identify a defined vert...",
                        "default": None
                },
                "in_horizontal_raster": {
                        "type": "string",
                        "description": "A raster defining the horizontal direction at each cell.The values on the raster must be integers ranging from 0 to 360, with 0 degrees being north, or toward the top of the screen, and increasing clo...",
                        "default": None
                },
                "horizontal_factor": {
                        "type": "string",
                        "description": "The Horizontal Factor object defines the relationship between the horizontal cost factor and the horizontal relative moving angle.There are several factors with modifiers that identify a defined horiz...",
                        "default": None
                },
                "out_distance_accumulation_raster": {
                        "type": "string",
                        "description": "The output distance raster.\r\n\r\n\r\nThe distance accumulation raster contains the accumulative distance for each cell from,\r\nor to, the least-cost source.",
                        "default": None
                },
                "out_back_direction_raster": {
                        "type": "string",
                        "description": "The back direction raster contains the calculated direction in degrees. The direction identifies the next cell along the shortest path back to the closest source while avoiding barriers.The range of v...",
                        "default": None
                },
                "out_source_direction_raster": {
                        "type": "string",
                        "description": "The source direction raster identifies the direction of the least accumulated cost source cell as an azimuth in degrees.\r\nThe range of values is from 0 degrees to 360 degrees, with 0 reserved for the ...",
                        "default": None
                },
                "out_source_location_raster": {
                        "type": "string",
                        "description": "The source location raster is a multiband output. The first band contains a row index, and the second band contains a column index. These indexes identify the location of the source cell that is the l...",
                        "default": None
                },
                "source_field": {
                        "type": "string",
                        "description": "The field used to assign values to the source locations. It must be of integer type.",
                        "default": None
                },
                "source_initial_accumulation": {
                        "type": "string",
                        "description": "The initial accumulative cost that will be used to begin the cost calculation.Allows for the specification of the fixed cost associated with a source. Instead of starting at a cost of zero, the cost a...",
                        "default": None
                },
                "source_maximum_accumulation": {
                        "type": "string",
                        "description": "The maximum accumulation for the traveler for a source.The cost calculations continue for each source until the specified accumulation is reached.The values must be greater than zero. The default accu...",
                        "default": None
                },
                "source_cost_multiplier": {
                        "type": "string",
                        "description": "The multiplier that will be applied to the cost values.This allows for control of the mode of travel or the magnitude at a source. The greater the multiplier, the greater the cost to move through each...",
                        "default": None
                },
                "source_direction": {
                        "type": "string",
                        "description": "Specifies the direction of the traveler when applying horizontal and vertical factors.FROM_SOURCE\u2014The horizontal factor and vertical factor will be applied beginning at the input source and travel out...",
                        "default": None
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies whether the distance will be calculated using a planar (flat earth) or a geodesic (ellipsoid) method.PLANAR\u2014The distance calculation will be performed on a projected flat plane using a 2D Ca...",
                        "default": None
                }
        },
        "required": [
                "in_source_data"
        ]
},
    "least_cost_corridor": {
        "name": "least_cost_corridor",
        "description": "Calculates the sum of two accumulative cost distance rasters with the option to apply a threshold based on percentage or accumulative cost. Learn more about how to connect locations with corridors",
        "parameters": {
                "in_accumulative_cost_distance_raster1": {
                        "type": "string",
                        "description": "The input raster representing the accumulative cost distance from the first source.Use the distance accumulation output from the Distance Accumulation or Distance Allocation tool."
                },
                "in_back_direction_raster1": {
                        "type": "string",
                        "description": "The input back direction raster from the first source. The units are degrees identifying the next cell along the least-cost path back to the first source.Use the back direction output from the Distanc..."
                },
                "in_accumulative_cost_distance_raster2": {
                        "type": "string",
                        "description": "The input raster representing the accumulative cost distance from the second source.Use the distance accumulation output from the Distance Accumulation or Distance Allocation tool."
                },
                "in_back_direction_raster2": {
                        "type": "string",
                        "description": "The input back direction raster from the second source. The units are degrees identifying the next cell along the least-cost path back to the second source.Use the back direction output from the Dista..."
                },
                "threshold_method": {
                        "type": "string",
                        "description": "Specifies how the threshold will be defined.NO_THRESHOLD\u2014No threshold will be applied, and the resulting corridor will cover the full extent of the input rasters. This is the default.PERCENT_OF_LEAST_..."
                },
                "threshold": {
                        "type": "string",
                        "description": "A percent or accumulative cost threshold that determines whether a given cell will be included in the output corridor raster.\r\nWhen the threshold_method parameter is set to PERCENT_OF_LEAST_COST, the ..."
                }
        },
        "required": [
                "in_accumulative_cost_distance_raster1",
                "in_back_direction_raster1",
                "in_accumulative_cost_distance_raster2",
                "in_back_direction_raster2",
                "threshold_method",
                "threshold"
        ]
},
    "optimal_corridor_connections": {
        "name": "optimal_corridor_connections",
        "description": "Calculates the optimal corridor connections between two or more input regions. Learn more about how to connect locations with corridors",
        "parameters": {
                "in_regions": {
                        "type": "string",
                        "description": "The input regions that will be connected by the optimal corridors.Regions can be defined by either a raster or a feature dataset.If the region input is a raster, the regions are defined by groups of c..."
                },
                "out_optimal_polygons": {
                        "type": "string",
                        "description": "The output polygon or line feature class of the optimal corridors that connect each of the input regions. Corridors (or lines) will overlap in locations where corridors travel the same route.Each corr..."
                },
                "in_barriers": {
                        "type": "string",
                        "description": "The dataset that defines the barriers.The barriers can be defined by an integer or a floating-point raster, or by a point, line, or polygon feature.",
                        "default": None
                },
                "in_cost_raster": {
                        "type": "string",
                        "description": "A raster defining the impedance or cost to move planimetrically through each cell.The value at each cell location represents the cost-per-unit distance for moving through the cell. Each cell location ...",
                        "default": None
                },
                "out_optimal_lines": {
                        "type": "string",
                        "description": "The output line feature class identifies the optimal lines to connect each of the input regions. Lines will overlap in locations where paths travel the same route.Each path (or line) is uniquely numbe...",
                        "default": None
                },
                "out_neighbor_polygons": {
                        "type": "string",
                        "description": "The output polygon or line feature class identifying the optimal corridors that connect each region to each of its closest or cost neighbors. Corridors (or lines) will overlap in locations where corri...",
                        "default": None
                },
                "out_neighbor_lines": {
                        "type": "string",
                        "description": "The output line feature class identifying the optimal line from each region to each of its closest or cost neighbors.Each corridor (or polygon) is uniquely numbered and additional fields in the attrib...",
                        "default": None
                },
                "corridor_method": {
                        "type": "string",
                        "description": "Specifies how the corridor will be created.Note:At this release, there is only one method to create corridors: fixed width. Since there is only a single default option, this parameter will be inactive...",
                        "default": None
                },
                "corridor_width": {
                        "type": "string",
                        "description": "A linear distance that defines the width of the resulting corridors. The value must be greater than or equal to zero. The default is zero.",
                        "default": None
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies whether the distance will be calculated using a planar (flat earth) or a geodesic (ellipsoid) method.PLANAR\u2014The distance calculation will be performed on a projected flat plane using a 2D Ca...",
                        "default": None
                }
        },
        "required": [
                "in_regions",
                "out_optimal_polygons"
        ]
},
    "optimal_path_as_line": {
        "name": "optimal_path_as_line",
        "description": "Calculates the optimal path from a source to a destination as a line. Learn more about connecting locations with optimal paths",
        "parameters": {
                "in_destination_data": {
                        "type": "string",
                        "description": "An integer raster or feature (point, line, or polygon) that identifies locations from which the optimal path will be determined to the least costly source.If the input is a raster, it must consist of ..."
                },
                "in_distance_accumulation_raster": {
                        "type": "string",
                        "description": "The distance accumulation raster that will be used to determine the optimal path from the sources to the destinations.The distance accumulation raster is usually created with the Distance Accumulation..."
                },
                "in_back_direction_raster": {
                        "type": "string",
                        "description": "The back direction raster contains calculated directions in degrees. The direction identifies the next cell along the optimal path back to the least accumulative cost source while avoiding barriers.Th..."
                },
                "out_polyline_features": {
                        "type": "string",
                        "description": "The output feature class that is the optimal path or paths."
                },
                "destination_field": {
                        "type": "string",
                        "description": "An integer field that will be used to obtain values for the destination locations.",
                        "default": None
                },
                "path_type": {
                        "type": "string",
                        "description": "Specifies a keyword defining the manner in which the values and zones on the input destination data will be interpreted in the cost path calculations.EACH_ZONE\u2014For each zone on the input destination d...",
                        "default": None
                },
                "create_network_paths": {
                        "type": "string",
                        "description": "Specifies whether complete, and possibly overlapping, paths from the destinations to the sources are calculated or if nonoverlapping network paths are created.DESTINATIONS_TO_SOURCES\u2014Complete paths fr...",
                        "default": None
                }
        },
        "required": [
                "in_destination_data",
                "in_distance_accumulation_raster",
                "in_back_direction_raster",
                "out_polyline_features"
        ]
},
    "optimal_path_as_raster": {
        "name": "optimal_path_as_raster",
        "description": "Calculates the optimal path from a source to a destination as a raster. Learn more about connecting locations with optimal paths",
        "parameters": {
                "in_destination_data": {
                        "type": "string",
                        "description": "An integer raster or feature (point, line, or polygon) that identifies locations from which the optimal path will be determined to the least costly source.If the input is a raster, it must consist of ..."
                },
                "in_distance_accumulation_raster": {
                        "type": "string",
                        "description": "The distance accumulation raster that will be used to determine the optimal path from the sources to the destinations.The distance accumulation raster is usually created with the Distance Accumulation..."
                },
                "in_back_direction_raster": {
                        "type": "string",
                        "description": "The back direction raster contains calculated directions in degrees. The direction identifies the next cell along the optimal path back to the least accumulative cost source while avoiding barriers.Th..."
                },
                "destination_field": {
                        "type": "string",
                        "description": "The field that will be used to obtain values for the destination locations.",
                        "default": None
                },
                "path_type": {
                        "type": "string",
                        "description": "Specifies a keyword defining the manner in which the values and zones on the input destination data will be interpreted in the cost path calculations.EACH_ZONE\u2014For each zone on the input destination d...",
                        "default": None
                }
        },
        "required": [
                "in_destination_data",
                "in_distance_accumulation_raster",
                "in_back_direction_raster"
        ]
},
    "optimal_region_connections": {
        "name": "optimal_region_connections",
        "description": "Calculates the optimal connectivity network between two or more input regions. Learn more about connecting regions with the optimal network",
        "parameters": {
                "in_regions": {
                        "type": "string",
                        "description": "The input regions to be connected by the optimal network.Regions can be defined by either a raster or a feature dataset.If the region input is a raster, the regions are defined by groups of contiguous..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polyline feature class of the optimal network of paths that connect each of the input regions.Each path (or line) is uniquely numbered and additional fields in the attribute table store spe..."
                },
                "in_barrier_data": {
                        "type": "string",
                        "description": "The dataset that defines the barriers.The barriers can be defined by an integer or a floating-point raster, or by a point, line, or polygon feature.",
                        "default": None
                },
                "in_cost_raster": {
                        "type": "string",
                        "description": "A raster defining the impedance or cost to move planimetrically through each cell.The value at each cell location represents the cost-per-unit distance for moving through the cell. Each cell location ...",
                        "default": None
                },
                "out_neighbor_paths": {
                        "type": "string",
                        "description": "The output polyline feature class identifying all paths from each region to each of its closest or cost neighbors.Each path (or line) is uniquely numbered and additional fields in the attribute table ...",
                        "default": None
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies whether the distance will be calculated using a planar (flat earth) or a geodesic (ellipsoid) method.PLANAR\u2014The distance calculation will be performed on a projected flat plane using a 2D Ca...",
                        "default": None
                },
                "connections_within_regions": {
                        "type": "string",
                        "description": "Specifies whether the paths will continue and connect within the input regions.GENERATE_CONNECTIONS\u2014Paths will continue within the input regions to connect all paths that enter a region.NO_CONNECTIONS...",
                        "default": None
                }
        },
        "required": [
                "in_regions",
                "out_feature_class"
        ]
},
    "extract_by_attributes": {
        "name": "extract_by_attributes",
        "description": "Extracts the cells of a raster based on a logical query.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster from which cells will be extracted."
                },
                "where_clause": {
                        "type": "string",
                        "description": "A logical expression that selects a subset of raster cells.The expression follows the general form of an SQL expression. An example of a where_clause is \"VALUE &gt; 100\"."
                }
        },
        "required": [
                "in_raster",
                "where_clause"
        ]
},
    "extract_by_circle": {
        "name": "extract_by_circle",
        "description": "Extracts the cells of a raster based on a circle by specifying the circle's center and radius.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster from which cells will be extracted."
                },
                "center_point": {
                        "type": "string",
                        "description": "The Point class determines the center coordinate (x,y) of the circle defining the area to be extracted.The form of the class is the following: Point (x, y)The coordinates are specified in the same map..."
                },
                "radius": {
                        "type": "string",
                        "description": "The radius of the circle defining the area to be extracted.The radius is specified in map units and is in the same units as the input raster."
                },
                "extraction_area": {
                        "type": "string",
                        "description": "Specifies whether cells inside or outside the input circle will be selected and written to the output raster.INSIDE\u2014Cells inside the input circle will be selected and written to the output raster. All...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "center_point",
                "radius"
        ]
},
    "extract_by_mask": {
        "name": "extract_by_mask",
        "description": "Extracts the cells of a raster that correspond to the areas defined by a mask.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster from which cells will be extracted."
                },
                "in_mask_data": {
                        "type": "string",
                        "description": "The input mask data defining the cell locations to extract.It can be a raster or a feature dataset.When the input mask data is a raster, NoData cells on the mask will be assigned NoData values on the ..."
                },
                "extraction_area": {
                        "type": "string",
                        "description": "Specifies whether cells inside or outside the locations defined by the input mask will be selected and written to the output raster.INSIDE\u2014Cells within the input mask will be selected and written to t...",
                        "default": None
                },
                "analysis_extent": {
                        "type": "string",
                        "description": "The extent that defines the area to be extracted.If not specified, the default extent is the intersection of the in_raster value and the in_mask_data value.The coordinates are specified in the same ma...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_mask_data"
        ]
},
    "extract_by_points": {
        "name": "extract_by_points",
        "description": "Extracts the cells of a raster based on a set of coordinate points. This tool is deprecated and will be removed in a future release. The Extract by Mask tool provides enhanced functionality or performance.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster from which cells will be extracted."
                },
                "pointspoint": {
                        "type": "string",
                        "description": "A Python list of Point class objects denote the locations where values will be extracted from the raster.The point objects are specified in a list of x,y coordinate pairs in the same map units as the ..."
                },
                "extraction_area": {
                        "type": "string",
                        "description": "Identifies whether to extract cells based on the specified point locations (inside) or outside the point locations (outside) .INSIDE\u2014The cell in which the selected point falls will be written to the o...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "pointspoint"
        ]
},
    "extract_by_polygon": {
        "name": "extract_by_polygon",
        "description": "Extracts the cells of a raster based on a polygon by specifying the polygon's vertices. This tool is deprecated and will be removed in a future release. The Extract by Mask tool provides enhanced functionality or performance.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster from which cells will be extracted."
                },
                "polygonpoint": {
                        "type": "string",
                        "description": "A polygon (or polygons) that defines the area of the input raster to be extracted.Each polygon part is a list of vertices defined by Point classes. The points are specified as x,y coordinate pairs in ..."
                },
                "extraction_area": {
                        "type": "string",
                        "description": "Identifies whether to extract cells inside or outside the input polygon.INSIDE\u2014The cells inside the input polygon should be selected and written to the output raster. All cells outside the polygon wil...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "polygonpoint"
        ]
},
    "extract_by_rectangle": {
        "name": "extract_by_rectangle",
        "description": "Extracts the cells of a raster based on a rectangle by specifying the rectangle's extent.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster from which cells will be extracted."
                },
                "rectangleextent": {
                        "type": "string",
                        "description": "A rectangle that defines the area to be extracted.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equal to the visibl..."
                },
                "extraction_area": {
                        "type": "string",
                        "description": "Specifies whether cells inside or outside the input rectangle will be selected and written to the output raster.INSIDE\u2014Cells inside the input rectangle will be selected and written to the output raste...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "rectangleextent"
        ]
},
    "extract_multi_values_to_points": {
        "name": "extract_multi_values_to_points",
        "description": "Extracts cell values at locations specified in a point feature class from one or more rasters and records the values to the attribute table of the point feature class.",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features to which raster values will be added."
                },
                "bilinear_interpolate_values": {
                        "type": "string",
                        "description": "Specifies whether interpolation will be used.NONE\u2014No interpolation will be applied; the value of the cell center will be used. This is the default.BILINEAR\u2014The value of the cell will be calculated fro...",
                        "default": None
                }
        },
        "required": [
                "in_point_features"
        ]
},
    "extract_values_to_points": {
        "name": "extract_values_to_points",
        "description": "Extracts the cell values of a raster based on a set of point features and records the values in the attribute table of an output feature class. The Extract Multi Values to Point tool provides enhanced functionality or performance.",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features defining the locations from which you want to extract the raster cell values."
                },
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset whose values will be extracted.It can be an integer or floating-point type raster."
                },
                "out_point_features": {
                        "type": "string",
                        "description": "The output point feature dataset containing the extracted raster values."
                },
                "interpolate_values": {
                        "type": "string",
                        "description": "Specifies whether interpolation will be used.NONE\u2014No interpolation will be applied; the value of the cell center will be used. This is the default.INTERPOLATE\u2014The value of the cell will be calculated ...",
                        "default": None
                },
                "add_attributes": {
                        "type": "string",
                        "description": "Determines if the raster attributes are written to the output point feature dataset.VALUE_ONLY\u2014Only the value of the input raster is added to the point attributes. This is the default.ALL\u2014All the fiel...",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "in_raster",
                "out_point_features"
        ]
},
    "sample": {
        "name": "sample",
        "description": "Creates a table or a point feature class that shows the values of cells from a raster, or a set of rasters, for defined locations. The locations are defined by raster cells, points, polylines, or polygons. Learn more about how Sample works",
        "parameters": {
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The rasters with values that will be sampled based on the input location data.\r\nThe process_as_multidimensional parameter is only supported when the input is a single, multidimensional raster."
                },
                "in_location_data": {
                        "type": "string",
                        "description": "The data identifying positions where a sample will be taken.The input can be a raster or a feature class."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table or feature class containing the sampled cell values.The output format is determined by the output location and path. By default, the output will be a geodatabase table or a geodatabas..."
                },
                "resampling_type": {
                        "type": "string",
                        "description": "The resampling algorithm that will be used to sample a raster to determine how the values will be obtained from the raster.\r\nNEAREST\u2014Nearest neighbor assignment will be used. This is the default.BILIN...",
                        "default": None
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "A field containing a different value for every location or feature in the input location raster or features.",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be processed.This parameter is only available when the input is a single, multidimensional raster.ALL_SLICES\u2014Samples will be processed for all dimensions (such as ...",
                        "default": None
                },
                "acquisition_definition": {
                        "type": "string",
                        "description": "Specifies the time, depth, or other acquisition data associated with the location features.Only the following combinations are supported:\r\nDimension + Start field or valueDimension + Start field or va...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MINIMUM\u2014The minimum value within the specified range will be calculated.MAXIMUM\u2014The maximum value within the specified range will be calculated.MEDIAN\u2014The...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile to calculate when the Statistics Type parameter is set to Percentile.\r\nThe percentile to calculate when the statistics_type parameter is set to PERCENTILE.This value can range from 0 to...",
                        "default": None
                },
                "buffer_distance": {
                        "type": "string",
                        "description": "The distance around the location data features. The buffer distance is specified in the linear unit of the location feature's spatial reference. If the feature uses a geographic reference, the unit wi...",
                        "default": None
                },
                "layout": {
                        "type": "string",
                        "description": "Specifies whether sampled values will appear in rows or columns in the output table.ROW_WISE\u2014Sampled values will appear in separate rows in the output table. This is the default.COLUMN_WISE\u2014Sampled va...",
                        "default": None
                },
                "generate_feature_class": {
                        "type": "string",
                        "description": "Specifies whether a point feature class with sampled values in its attribute table or a table with sampled values will be generated.TABLE\u2014A table with sampled values will be generated. This is the def...",
                        "default": None
                }
        },
        "required": [
                "in_rastersin_raster",
                "in_location_data",
                "out_table"
        ]
},
    "aggregate": {
        "name": "aggregate",
        "description": "Generates a reduced-resolution version of a raster. Each output cell contains the Sum, Minimum, Maximum, Mean, or Median of the input cells that are encompassed by the extent of that cell. Learn more about how Aggregate works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be aggregated.It can be of integer or floating point type."
                },
                "cell_factor": {
                        "type": "string",
                        "description": "The factor by which the cell size of the input raster will be multiplied. The value must be an integer greater than 1.For example, a cell factor value of 3 results in an output cell size three times l..."
                },
                "aggregation_type": {
                        "type": "string",
                        "description": "The method that will be used for aggregation.The values of the input cells encompassed by the coarser output cells are aggregated by one of the following statistics:SUM\u2014The total of the input cell val...",
                        "default": None
                },
                "extent_handling": {
                        "type": "string",
                        "description": "Specifies whether the boundaries of the input raster will be expanded when its rows or columns are not a multiple of the cell factor.EXPAND\u2014The top or right boundaries of the input raster will be expa...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Denotes whether NoData values are ignored by the aggregation calculation.DATA\u2014Specifies that if NoData values exist for any of the cells that fall within the spatial extent of a larger cell on the out...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "cell_factor"
        ]
},
    "boundary_clean": {
        "name": "boundary_clean",
        "description": "Smooths the boundary between zones in a raster. Learn more about how Boundary Clean works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster for which the boundary between zones will be smoothed.It must be of integer type."
                },
                "sort_type": {
                        "type": "string",
                        "description": "Specifies the type of sorting to use in the smoothing process. The sorting determines the priority by which cells can expand into their neighbors.The sorting can be based on zone value or zone size.NO...",
                        "default": None
                },
                "number_of_runs": {
                        "type": "string",
                        "description": "Specifies the number of times the smoothing process will occur, twice or once.TWO_WAY\u2014The expansion and shrinking operation is performed twice. The first time, the operation is performed according to ...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "expand": {
        "name": "expand",
        "description": "Expands specified zones of a raster by a specified number of cells. Learn more about how Expand works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster for which the identified zones are to be expandedIt must be of integer type."
                },
                "number_cells": {
                        "type": "string",
                        "description": "The number of cells to expand each specified zone by.The value must be an integer greater than 1."
                },
                "zone_valueszone_value": {
                        "type": "string",
                        "description": "The list of zone values to expand.The zone values must be integers. They can be in any order."
                },
                "expand_method": {
                        "type": "string",
                        "description": "The method used to expand the selected zones.MORPHOLOGICAL\u2014Uses a mathematical morphology method to expand the zones. This is the default.DISTANCE\u2014Uses a distance-based method to expand the zones.The ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "number_cells",
                "zone_valueszone_value"
        ]
},
    "majority_filter": {
        "name": "majority_filter",
        "description": "Replaces cells in a raster based on the majority of their contiguous neighboring cells. Learn more about how Majority Filter works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be filtered based on the majority of contiguous neighboring cells.It must be of integer type."
                },
                "number_neighbors": {
                        "type": "string",
                        "description": "Determines the number of neighboring cells to use in the kernel of the filter.FOUR\u2014The kernel of the filter will be the four direct (orthogonal) neighbors to the present cell. This is the default.EIGH...",
                        "default": None
                },
                "majority_definition": {
                        "type": "string",
                        "description": "Specifies the number of contiguous (spatially connected) cells that must be of the same value before a replacement will occur.MAJORITY\u2014A majority of cells must have the same value and be contiguous. T...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "nibble": {
        "name": "nibble",
        "description": "Replaces cells of a raster corresponding to a mask with the value of the nearest neighbor. Learn more about how Nibble works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster with the masked locations that will be replaced by the value of their nearest neighbor.The input raster can be either integer or floating point type."
                },
                "in_mask_raster": {
                        "type": "string",
                        "description": "The raster that identifies the locations in the input raster that will be replaced.\r\nCells with a value of NoData are considered to be within the masked area. In the output raster, these locations wil..."
                },
                "nibble_values": {
                        "type": "string",
                        "description": "Specifies whether NoData cells in the input raster can replace cells in the masked areas if they are the nearest neighbor.\r\n\r\n\r\nALL_VALUES\u2014Both NoData and data values can replace cells in the masked a...",
                        "default": None
                },
                "nibble_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData cells in the input raster that are within the masked area will be preserved or replaced.\r\nPRESERVE_NODATA\u2014 Any NoData cells in the input raster that are within the masked area...",
                        "default": None
                },
                "in_zone_raster": {
                        "type": "string",
                        "description": "The input zone raster. For each zone, input cells that are within the mask will be replaced only by the nearest cell values within that same zone.A zone is all the cells in a raster that have the same...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_mask_raster"
        ]
},
    "region_group": {
        "name": "region_group",
        "description": "For each cell in the output, the identity of the connected region to which that cell belongs is recorded. A unique number is assigned to each region. Learn more about creating individual zones with Region Group",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster for which unique connected regions of cells will be identified.It must be of integer type."
                },
                "number_neighbors": {
                        "type": "string",
                        "description": "Specifies the number of neighboring cells to use when evaluating connectivity between cells that define a region.FOUR\u2014Connectivity is evaluated for the four nearest (orthogonal) neighbors of each inpu...",
                        "default": None
                },
                "zone_connectivity": {
                        "type": "string",
                        "description": "Defines which cell values should be considered when testing for connectivity.WITHIN\u2014Connectivity for a region is evaluated for input cells that are part of the same zone (cell value). The only cells t...",
                        "default": None
                },
                "add_link": {
                        "type": "string",
                        "description": "Specifies whether a link field will be added to the table of the output when the zone_connectivity parameter is set to WITHIN. It is ignored if that parameter is set to CROSS.ADD_LINK\u2014A LINK field wil...",
                        "default": None
                },
                "excluded_value": {
                        "type": "string",
                        "description": "A value that excludes all cells of that zone from the connectivity evaluation. If a cell location contains the value, no spatial connectivity will be evaluated, regardless of how the number of neighbo...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "shrink": {
        "name": "shrink",
        "description": "Shrinks the selected zones by a specified number of cells by replacing them with the value of the cell that is most frequent in its neighborhood. Learn more about how Shrink works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster for which the identified zones are to be shrunk.It must be of integer type."
                },
                "number_cells": {
                        "type": "string",
                        "description": "The number of cells by which to shrink each specified zone.The value must be an integer greater than 0."
                },
                "zone_valueszone_value": {
                        "type": "string",
                        "description": "The list of zone values to shrink.The zone values must be integers. They can be in any order."
                },
                "shrink_method": {
                        "type": "string",
                        "description": "The method to use to shrink the selected zones.MORPHOLOGICAL\u2014Uses a mathematical morphology method to shrink the zones. This is the default.DISTANCE\u2014Uses a distance-based method to shrink the zones.\r\n...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "number_cells",
                "zone_valueszone_value"
        ]
},
    "thin": {
        "name": "thin",
        "description": "Thins rasterized linear features by reducing the number of cells representing the width of the features.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be thinned.It must be of integer type."
                },
                "background_value": {
                        "type": "string",
                        "description": "Specifies the cell value that will identify the background cells. The linear features are formed from the foreground cells.ZERO\u2014The background is composed of cells of 0 or less, or NoData. All cells w...",
                        "default": None
                },
                "filter": {
                        "type": "string",
                        "description": "Specifies whether a filter will be applied as the first phase of thinning.NO_FILTER\u2014No filter will be applied.This is the default.FILTER\u2014The raster will be filtered to smooth the boundaries between fo...",
                        "default": None
                },
                "corners": {
                        "type": "string",
                        "description": "Specifies whether round or sharp turns will be made at turns or junctions.It is also used during the vector conversion process to spline curves or create sharp intersections and corners.ROUND\u2014Attempts...",
                        "default": None
                },
                "maximum_thickness": {
                        "type": "string",
                        "description": "The maximum thickness, in map units, of linear features in the input raster.The default thickness is ten times the cell size.",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "darcy_flow": {
        "name": "darcy_flow",
        "description": "Calculates the groundwater volume balance residual and other outputs for steady flow in an aquifer. Learn more about how Darcy Flow and Darcy Velocity work",
        "parameters": {
                "in_head_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the groundwater head elevation at that location.The head is typically an elevation above some datum, such as mean sea level."
                },
                "in_porosity_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the effective formation porosity at that location."
                },
                "in_thickness_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the saturated thickness at that location.The value for the thickness is interpreted from geological properties of the aquifer."
                },
                "in_transmissivity_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the formation transmissivity at that location.The transmissivity of an aquifer is defined as the hydraulic conductivity K times the saturated aquifer ..."
                },
                "out_direction_raster": {
                        "type": "string",
                        "description": "The output flow direction raster.Each cell value represents the direction of the seepage velocity vector (average linear velocity) at the center of the cell, calculated as the average value of the see...",
                        "default": None
                },
                "out_magnitude_raster": {
                        "type": "string",
                        "description": "An optional output raster where each cell value represents the magnitude of the seepage velocity vector (average linear velocity) at the center of the cell, calculated as the average value of the seep...",
                        "default": None
                }
        },
        "required": [
                "in_head_raster",
                "in_porosity_raster",
                "in_thickness_raster",
                "in_transmissivity_raster"
        ]
},
    "darcy_velocity": {
        "name": "darcy_velocity",
        "description": "Calculates the groundwater seepage velocity vector (direction and magnitude) for steady flow in an aquifer. Learn more about how Darcy Flow and Darcy Velocity work",
        "parameters": {
                "in_head_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the groundwater head elevation at that location.The head is typically an elevation above some datum, such as mean sea level."
                },
                "in_porosity_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the effective formation porosity at that location."
                },
                "in_thickness_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the saturated thickness at that location.The value for the thickness is interpreted from geological properties of the aquifer."
                },
                "in_transmissivity_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the formation transmissivity at that location.The transmissivity of an aquifer is defined as the hydraulic conductivity K times the saturated aquifer ..."
                },
                "out_magnitude_raster": {
                        "type": "string",
                        "description": "The output flow direction raster.Each cell value represents the direction of the seepage velocity vector (average linear velocity) at the center of the cell, calculated as the average value of the see..."
                }
        },
        "required": [
                "in_head_raster",
                "in_porosity_raster",
                "in_thickness_raster",
                "in_transmissivity_raster",
                "out_magnitude_raster"
        ]
},
    "particle_track": {
        "name": "particle_track",
        "description": "Calculates the path of a particle through a velocity field, returning an ASCII file of particle tracking data and, optionally, a feature class of track information. Learn more about how Particle Track works",
        "parameters": {
                "in_direction_raster": {
                        "type": "string",
                        "description": "An input raster where each cell value represents the direction of the seepage velocity vector (average linear velocity) at the center of the cell.Directions are expressed in compass coordinates, in de..."
                },
                "in_magnitude_raster": {
                        "type": "string",
                        "description": "An input raster where each cell value represents the magnitude of the seepage velocity vector (average linear velocity) at the center of the cell.Units are length/time. This can be created by the Darc..."
                },
                "source_point": {
                        "type": "string",
                        "description": "A Python Point class object denotes the location of the source point, in map units, from which to begin the particle tracking.The form of the object is: point(x,y)"
                },
                "out_track_file": {
                        "type": "string",
                        "description": "The output ASCII text file that contains the particle tracking data."
                },
                "step_length": {
                        "type": "string",
                        "description": "The step length to be used for calculating the particle track.The default is one-half the cell size. Units are length.",
                        "default": None
                },
                "tracking_time": {
                        "type": "string",
                        "description": "Maximum elapsed time for particle tracking.The algorithm will follow the track until either this time is met or the particle migrates off the raster or into a depression.The default value is infinity....",
                        "default": None
                },
                "out_track_polyline_features": {
                        "type": "string",
                        "description": "The optional output line feature class containing the particle track.This feature class contains a series of arcs with attributes for position, local velocity direction and magnitude, and cumulative l...",
                        "default": None
                }
        },
        "required": [
                "in_direction_raster",
                "in_magnitude_raster",
                "source_point",
                "out_track_file"
        ]
},
    "porous_puff": {
        "name": "porous_puff",
        "description": "Calculates the time-dependent, two-dimensional concentration distribution in mass per volume of a solute introduced instantaneously and at a discrete point into a vertically mixed aquifer. Learn more about how Porous Puff works",
        "parameters": {
                "in_track_file": {
                        "type": "string",
                        "description": "The input particle track path file.This is an ASCII text file containing information about the position, the local velocity vector, and the cumulative length and time of travel along the path.This fil..."
                },
                "in_porosity_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the effective formation porosity at that location."
                },
                "in_thickness_raster": {
                        "type": "string",
                        "description": "The input raster where each cell value represents the saturated thickness at that location.The value for the thickness is interpreted from geological properties of the aquifer."
                },
                "mass": {
                        "type": "string",
                        "description": "A value for the amount of mass released instantaneously at the source point, in units of mass."
                },
                "dispersion_time": {
                        "type": "string",
                        "description": "A value representing the time horizon for dispersion of the solute, in units of time.The time must be less than or equal to the maximum time in the track file. If the requested time exceeds the availa...",
                        "default": None
                },
                "longitudinal_dispersivity": {
                        "type": "string",
                        "description": "A value representing the dispersivity parallel to the flow direction.For details on how the default value is determined, and how it relates to the scale of the study, see the How Porous Puff works sec...",
                        "default": None
                },
                "dispersivity_ratio": {
                        "type": "string",
                        "description": "A value representing the ratio of longitudinal dispersivity over transverse dispersivity.Transverse dispersivity is perpendicular to the flow direction in the same horizontal plane. The default value ...",
                        "default": None
                },
                "retardation_factor": {
                        "type": "string",
                        "description": "A dimensionless value representing the retardation of the solute in the aquifer.Retardation varies between one and infinity, with one corresponding to no retardation. The default value is one.",
                        "default": None
                },
                "decay_coefficient": {
                        "type": "string",
                        "description": "Decay coefficient for solutes undergoing first-order exponential decay (for example, radionuclides) in units of inverse time.The default is zero, corresponding to no decay.",
                        "default": None
                }
        },
        "required": [
                "in_track_file",
                "in_porosity_raster",
                "in_thickness_raster",
                "mass"
        ]
},
    "basin": {
        "name": "basin",
        "description": "Creates a raster delineating all drainage basins.",
        "parameters": {
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.\r\nA flow direction raster can be created with the Flow Direction tool, using the default D8 flow direction type ."
                }
        },
        "required": [
                "in_flow_direction_raster"
        ]
},
    "derive_continuous_flow": {
        "name": "derive_continuous_flow",
        "description": "Generates a raster of accumulated flow into each cell from an input surface raster with no prior sink or depression filling required. Learn more about how Derive Continuous Flow works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input raster representing a continuous surface."
                },
                "in_depressions_data": {
                        "type": "string",
                        "description": "An optional dataset that defines real depressions.The depressions can be defined either through a raster or a feature layer.If input is a raster, the depression cells must take a valid value, includin...",
                        "default": None
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "An optional input raster dataset that defines the fraction of flow that contributes to flow accumulation at each cell.The weight is only applied to the accumulation of flow.If no accumulation weight r...",
                        "default": None
                },
                "out_flow_direction_raster": {
                        "type": "string",
                        "description": "The output raster that shows the direction of flow at each cell using the D8 or Multiple Flow Direction (MFD) method.The output is of integer type.",
                        "default": None
                },
                "flow_direction_type": {
                        "type": "string",
                        "description": "Specifies the type of flow method that will be used when computing flow directions.D8\u2014Flow direction will be determined by the D8 method. This method assigns flow direction to the steepest downslope n...",
                        "default": None
                },
                "force_flow": {
                        "type": "string",
                        "description": "Specifies whether edge cells will always flow outward or follow normal flow rules.\r\nNORMAL\u2014If the maximum drop on the inside of an edge cell is greater than zero, the flow direction will be determined...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "derive_stream_as_line": {
        "name": "derive_stream_as_line",
        "description": "Generates stream line features from an input surface raster with no prior sink or depression filling required.",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_stream_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the identified streams."
                },
                "in_depressions_data": {
                        "type": "string",
                        "description": "An optional dataset that defines real depressions.The depressions can be defined either through a raster or a feature layer.If input is a raster, the depression cells must take a valid value, includin...",
                        "default": None
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "An optional input raster dataset that defines the fraction of flow that contributes to flow accumulation at each cell.The weight is only applied to the accumulation of flow.If no accumulation weight r...",
                        "default": None
                },
                "accumulation_threshold": {
                        "type": "string",
                        "description": "The threshold for determining whether a given cell is part of a stream in terms of the total area that flows into such cell.",
                        "default": None
                },
                "stream_designation_method": {
                        "type": "string",
                        "description": "Specifies the unique value or order of the streams in the output attribute table.CONSTANT\u2014The output stream segments will all equal 1. This is the default.UNIQUE\u2014Each stream will have a unique ID betw...",
                        "default": None
                },
                "simplify": {
                        "type": "string",
                        "description": "Specifies whether the output stream lines will be smoothed into simpler shapes.NO_SIMPLIFY\u2014The stream feature lines will not be smoothed.SIMPLIFY\u2014The stream feature lines will be simplified using the ...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster",
                "out_stream_features"
        ]
},
    "derive_stream_as_raster": {
        "name": "derive_stream_as_raster",
        "description": "Generates a stream raster from an input surface raster with no prior sink or depression filling required.",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_depressions_data": {
                        "type": "string",
                        "description": "An optional dataset that defines real depressions.The depressions can be defined either through a raster or a feature layer.If input is a raster, the depression cells must take a valid value, includin...",
                        "default": None
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "An optional input raster dataset that defines the fraction of flow that contributes to flow accumulation at each cell.The weight is only applied to the accumulation of flow.If no accumulation weight r...",
                        "default": None
                },
                "accumulation_threshold": {
                        "type": "string",
                        "description": "The threshold for determining whether a given cell is part of a stream in terms of the total area that flows into such cell.",
                        "default": None
                },
                "stream_designation_method": {
                        "type": "string",
                        "description": "Specifies the unique or order of the streams in the output.CONSTANT\u2014The output cell values will all equal 1. This is the default.UNIQUE\u2014Each stream will have a unique ID between intersections in the o...",
                        "default": None
                },
                "force_flow": {
                        "type": "string",
                        "description": "Specifies whether edge cells will always flow outward or follow normal flow rules.\r\nNORMAL\u2014If the maximum drop on the inside of an edge cell is greater than zero, the flow direction will be determined...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "fill": {
        "name": "fill",
        "description": "Fills sinks in a surface raster to remove small imperfections in the data. Learn more about how Fill works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input raster representing a continuous surface."
                },
                "z_limit": {
                        "type": "string",
                        "description": "Maximum elevation difference between a sink and its pour point to be filled.If the difference in z-values between a sink and its pour point is greater than the z_limit, that sink will not be filled.Th...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "flow_accumulation": {
        "name": "flow_accumulation",
        "description": "Creates a raster of accumulated flow into each cell. A weight factor can optionally be applied. Learn more about how Flow Accumulation works",
        "parameters": {
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.The flow direction raster can be created using the Flow Direction tool.\r\nThe flow direction raster can be created using the D8, Multi..."
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "An optional input raster for applying a weight to each cell.If no weight raster is specified, a default weight of 1 will be applied to each cell. For each cell in the output raster, the result will be...",
                        "default": None
                },
                "data_type": {
                        "type": "string",
                        "description": "The output accumulation raster can be integer, floating point, or double type.FLOAT\u2014The output raster will be floating point type. This is the default.INTEGER\u2014The output raster will be integer type.DO...",
                        "default": None
                },
                "flow_direction_type": {
                        "type": "string",
                        "description": "Specifies the input flow direction raster type.D8\u2014The input flow direction raster is of type D8. This is the default.MFD\u2014The input flow direction raster is of type Multi Flow Direction (MFD).DINF\u2014The ...",
                        "default": None
                }
        },
        "required": [
                "in_flow_direction_raster"
        ]
},
    "flow_direction": {
        "name": "flow_direction",
        "description": "Creates a raster of flow direction from each cell to its downslope neighbor, or neighbors, using the D8, Multiple Flow Direction (MFD), or D-Infinity (DINF) method. Learn more about how Flow Direction works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input raster representing a continuous surface."
                },
                "force_flow": {
                        "type": "string",
                        "description": "Specifies whether edge cells will always flow outward or follow normal flow rules.\r\nNORMAL\u2014If the maximum drop on the inside of an edge cell is greater than zero, the flow direction will be determined...",
                        "default": None
                },
                "out_drop_raster": {
                        "type": "string",
                        "description": "An optional output drop raster.The drop raster returns the ratio of the maximum change in elevation from each cell along the direction of flow to the path length between centers of cells, expressed in...",
                        "default": None
                },
                "flow_direction_type": {
                        "type": "string",
                        "description": "Specifies the type of flow method that will be used when computing flow directions.D8\u2014Flow direction will be determined by the D8 method. This method assigns flow direction to the steepest downslope n...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "flow_distance": {
        "name": "flow_distance",
        "description": "Computes, for each cell, the horizontal or vertical component of downslope distance, following the flow paths, to cells on a stream into which they flow. In case of multiple flow paths, minimum, weighted mean, or maximum flow distance can be computed. If an optional flow direction raster is provided, the down slope direction(s) will be limited to those defined by the input flow direction raster.",
        "parameters": {
                "in_stream_raster": {
                        "type": "string",
                        "description": "An input stream raster that represents a linear stream network."
                },
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input raster representing a continuous surface."
                },
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.When a flow direction raster is provided, the down slope direction(s) will be limited to those defined by the input flow directions.T...",
                        "default": None
                },
                "distance_type": {
                        "type": "string",
                        "description": "Determines if the vertical or horizontal component of flow distance is calculated.VERTICAL\u2014The flow distance calculations represent the vertical component of flow distance, following the flow path, fr...",
                        "default": None
                },
                "flow_direction_type": {
                        "type": "string",
                        "description": "Specifies the input flow direction raster type.D8\u2014The input flow direction raster is of type D8. This is the default.MFD\u2014The input flow direction raster is of type Multi Flow Direction (MFD).DINF\u2014The ...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Determines the statistics type used to compute flow distance over multiple flow paths. If there is only a single flow path from each cell to a cell on the stream, all statistics types produce the same...",
                        "default": None
                }
        },
        "required": [
                "in_stream_raster",
                "in_surface_raster"
        ]
},
    "flow_length": {
        "name": "flow_length",
        "description": "Calculates the upstream or downstream distance, or weighted distance, along the flow path for each cell.",
        "parameters": {
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.The flow direction raster can be created using the Flow Direction tool."
                },
                "direction_measurement": {
                        "type": "string",
                        "description": "The direction of measurement along the flow path.DOWNSTREAM\u2014Calculates the downslope distance along the flow path, from each cell to a sink or outlet on the edge of the raster.UPSTREAM\u2014Calculates the ...",
                        "default": None
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "An optional input raster for applying a weight to each cell.If no weight raster is specified, a default weight of 1 will be applied to each cell. For each cell in the output raster, the result will be...",
                        "default": None
                }
        },
        "required": [
                "in_flow_direction_raster"
        ]
},
    "sink": {
        "name": "sink",
        "description": "Creates a raster identifying all sinks or areas of internal drainage. Learn more about how Sink works",
        "parameters": {
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.The flow direction raster can be created using the Flow Direction tool, run using the default flow direction type D8."
                }
        },
        "required": [
                "in_flow_direction_raster"
        ]
},
    "snap_pour_point": {
        "name": "snap_pour_point",
        "description": "Snaps pour points to the cell of highest flow accumulation within a specified distance.",
        "parameters": {
                "in_pour_point_data": {
                        "type": "string",
                        "description": "The input pour point locations that will be snapped.For a raster input, all cells that are not NoData (that is, have a value) will be considered pour points and will be snapped.For a point feature inp..."
                },
                "in_accumulation_raster": {
                        "type": "string",
                        "description": "The input flow accumulation raster.This can be created with the Flow Accumulation tool."
                },
                "snap_distance": {
                        "type": "string",
                        "description": "The maximum distance, in map units, that will be searched for a cell of higher accumulated flow."
                },
                "pour_point_field": {
                        "type": "string",
                        "description": "The field used to assign values to the pour point locations.If the pour point dataset is a raster, use Value.If the pour point dataset is a feature, use a numeric field. If the field contains floating...",
                        "default": None
                }
        },
        "required": [
                "in_pour_point_data",
                "in_accumulation_raster",
                "snap_distance"
        ]
},
    "storage_capacity": {
        "name": "storage_capacity",
        "description": "Creates a table and a chart of elevations and corresponding storage capacities for an input surface raster. The tool calculates the surface area and total volume of the underlying region at a series of elevation increments.",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input raster representing a continuous surface."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that contains for each zone the surface area and total volumes for each increment in elevation."
                },
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset.",
                        "default": None
                },
                "analysis_type": {
                        "type": "string",
                        "description": "Specifies the analysis type.AREA_VOLUME\u2014Both surface areas and total volumes are calculated at each elevation increment. This is the default.AREA\u2014Surface area is calculated at each elevation increment...",
                        "default": None
                },
                "min_elevation": {
                        "type": "string",
                        "description": "The minimum elevation from which storage capacities are assessed.By default, the tool uses the minimum surface raster value in each zone as the minimum elevation for that zone. If a value is provided,...",
                        "default": None
                },
                "max_elevation": {
                        "type": "string",
                        "description": "The maximum elevation from which storage capacities are assessed.By default, the tool uses the maximum surface raster value in each zone as the maximum elevation for that zone. If a value is provided,...",
                        "default": None
                },
                "increment_type": {
                        "type": "string",
                        "description": "Specifies the increment type to use when computing elevation increments between minimum and maximum elevations.NUMBER_OF_INCREMENTS\u2014The number of increments between minimum and maximum elevations is u...",
                        "default": None
                },
                "increment": {
                        "type": "string",
                        "description": "An incremental value that is either the number of increments or the difference in elevation between increments. The value is determined based on the increment type parameter value.",
                        "default": None
                },
                "z_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for vertical z-values.INCH\u2014The linear unit will be inches.FOOT\u2014The linear unit will be feet.YARD\u2014The linear unit will be yards.MILE_US\u2014The linear unit will ...",
                        "default": None
                },
                "out_chart": {
                        "type": "string",
                        "description": "The name of the output chart for display.",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster",
                "out_table",
                "in_zone_data"
        ]
},
    "stream_link": {
        "name": "stream_link",
        "description": "Assigns unique values to sections of a raster linear network between intersections.",
        "parameters": {
                "in_stream_raster": {
                        "type": "string",
                        "description": "An input raster that represents a linear stream network."
                },
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.The flow direction raster can be created using the Flow Direction tool, run using the default flow direction type D8."
                }
        },
        "required": [
                "in_stream_raster",
                "in_flow_direction_raster"
        ]
},
    "stream_order": {
        "name": "stream_order",
        "description": "Assigns a numeric order to segments of a raster representing branches of a linear network. Learn more about how Stream Order works",
        "parameters": {
                "in_stream_raster": {
                        "type": "string",
                        "description": "An input raster that represents a linear stream network.The input stream raster linear network should be represented as values greater than or equal to one on a background of NoData."
                },
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.The flow direction raster can be created using the Flow Direction tool, run using the default flow direction type D8."
                },
                "order_method": {
                        "type": "string",
                        "description": "The method used for assigning stream order.STRAHLER\u2014The method of stream ordering proposed by Strahler in 1952. Stream order only increases when streams of the same order intersect. Therefore, the int...",
                        "default": None
                }
        },
        "required": [
                "in_stream_raster",
                "in_flow_direction_raster"
        ]
},
    "stream_to_feature": {
        "name": "stream_to_feature",
        "description": "Converts a raster representing a linear network to features representing the linear network. Learn more about how Stream to Feature works",
        "parameters": {
                "in_stream_raster": {
                        "type": "string",
                        "description": "An input raster that represents a linear stream network."
                },
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.The flow direction raster can be created using the Flow Direction tool."
                },
                "out_polyline_features": {
                        "type": "string",
                        "description": "Output feature class that will hold the converted streams."
                },
                "simplify": {
                        "type": "string",
                        "description": "Specifies whether weeding is used.SIMPLIFY\u2014 The feature is weeded to reduce the number of vertices. The Douglas-Puecker algorithm for line generalization is used with a tolerance of sqrt(0.5) * cell s...",
                        "default": None
                }
        },
        "required": [
                "in_stream_raster",
                "in_flow_direction_raster",
                "out_polyline_features"
        ]
},
    "watershed": {
        "name": "watershed",
        "description": "Determines the contributing area above a set of cells in a raster. Learn more about how Watershed works",
        "parameters": {
                "in_flow_direction_raster": {
                        "type": "string",
                        "description": "The input raster that shows the direction of flow out of each cell.\r\nThe flow direction raster can be created using the Flow Direction tool, run using the default flow direction type D8."
                },
                "in_pour_point_data": {
                        "type": "string",
                        "description": "The input pour point locations.For a raster, this represents cells above which the contributing area, or catchment, will be determined. All cells that are not NoData will be used as source cells.For a..."
                },
                "pour_point_field": {
                        "type": "string",
                        "description": "The field used to assign values to the pour point locations.If the pour point dataset is a raster, use Value.If the pour point dataset is a feature, use a numeric field. If the field contains floating...",
                        "default": None
                }
        },
        "required": [
                "in_flow_direction_raster",
                "in_pour_point_data"
        ]
},
    "idw": {
        "name": "idw",
        "description": "Interpolates a raster surface from points using an inverse distance weighted (IDW) technique. Learn more about how IDW works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated into a surface raster."
                },
                "z_field": {
                        "type": "string",
                        "description": "The field that holds a height or magnitude value for each point.This can be a numeric field or the Shape field if the input point features contain z-values."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "power": {
                        "type": "string",
                        "description": "The exponent of distance.Controls the significance of surrounding points on the interpolated value. A higher power results in less influence from distant points. It can be any real number greater than...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "The Radius class defines which of the input points will be used to interpolate the value for each cell in the output raster.There are two types of radius classes: RadiusVariable and RadiusFixed. A Var...",
                        "default": None
                },
                "in_barrier_polyline_features": {
                        "type": "string",
                        "description": "Polyline features to be used as a break or limit in searching for the input sample points.",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "z_field"
        ]
},
    "kriging": {
        "name": "kriging",
        "description": "Interpolates a raster surface from points using kriging. The Empirical Bayesian Kriging tool provides enhanced functionality or performance. Learn more about how Kriging works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated into a surface raster."
                },
                "z_field": {
                        "type": "string",
                        "description": "The field that holds a height or magnitude value for each point.This can be a numeric field or the Shape field if the input point features contain z-values."
                },
                "semivariogram_propskriging_model": {
                        "type": "string",
                        "description": "The KrigingModel class defines which kriging model is to be used.There are two types of kriging classes. The KrigingModelOrdinary method has five types of semivariograms available. The KrigingModelUni..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "The Radius class defines which of the input points will be used to interpolate the value for each cell in the output raster.There are two types of radius classes: RadiusVariable and RadiusFixed. A Var...",
                        "default": None
                },
                "out_variance_prediction_raster": {
                        "type": "string",
                        "description": "Optional output raster where each cell contains the predicted variance values for that location.",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "z_field",
                "semivariogram_propskriging_model"
        ]
},
    "natural_neighbor": {
        "name": "natural_neighbor",
        "description": "Interpolates a raster surface from points using a natural neighbor technique. Learn more about how Natural Neighbor works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated into a surface raster."
                },
                "z_field": {
                        "type": "string",
                        "description": "The field that holds a height or magnitude value for each point.This can be a numeric field or the Shape field if the input point features contain z-values."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "z_field"
        ]
},
    "spline": {
        "name": "spline",
        "description": "Interpolates a raster surface from points using a two-dimensional minimum curvature spline technique. The resulting smooth surface passes exactly through the input points. Learn more about how Spline works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated into a surface raster."
                },
                "z_field": {
                        "type": "string",
                        "description": "The field that holds a height or magnitude value for each point.This can be a numeric field or the Shape field if the input point features contain z-values."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "spline_type": {
                        "type": "string",
                        "description": "The type of spline to be used.REGULARIZED\u2014Yields a smooth surface and smooth first derivatives.TENSION\u2014Tunes the stiffness of the interpolant according to the character of the modeled phenomenon.",
                        "default": None
                },
                "weight": {
                        "type": "string",
                        "description": "Parameter influencing the character of the surface interpolation.When the REGULARIZED option is used, it defines the weight of the third derivatives of the surface in the curvature minimization expres...",
                        "default": None
                },
                "number_points": {
                        "type": "string",
                        "description": "The number of points per region used for local approximation.The default is 12.",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "z_field"
        ]
},
    "spline_with_barriers": {
        "name": "spline_with_barriers",
        "description": "Interpolates a raster surface, using barriers, from points using a minimum curvature spline technique. The barriers are entered as either polygon or polyline features. Learn more about how Spline with Barriers works",
        "parameters": {
                "input_point_featuresin_point_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated into a surface raster."
                },
                "z_value_field": {
                        "type": "string",
                        "description": "The field that holds a height or magnitude value for each point.            This can be a numeric field or the Shape field if the input point features contain z-values."
                },
                "input_barrier_features": {
                        "type": "string",
                        "description": "The optional input barrier features to constrain the interpolation.",
                        "default": None
                },
                "output_cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "smoothing_factor": {
                        "type": "string",
                        "description": "The parameter that influences the smoothing of the output surface.            No smoothing is applied when the value is zero and the maximum amount of smoothing is applied when the factor equals 1.   ...",
                        "default": None
                }
        },
        "required": [
                "input_point_featuresin_point_features",
                "z_value_field"
        ]
},
    "topo_to_raster": {
        "name": "topo_to_raster",
        "description": "Interpolates a hydrologically correct raster surface from point, line, and polygon data. Learn more about how Topo to Raster works",
        "parameters": {
                "in_topo_featurestopo_input": {
                        "type": "string",
                        "description": "The Topo class specifies the input features containing the z-values to be interpolated into a surface raster.There are nine types of data accepted inputs to the Topo class: TopoPointElevation, TopoCon..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Extent for the output raster dataset.Interpolation will occur out to the x and y limits, and cells outside that extent will be NoData. For best interpolation results along the edges of the output rast...",
                        "default": None
                },
                "margin": {
                        "type": "string",
                        "description": "Distance in cells to interpolate beyond the specified output extent and boundary.The value must be greater than or equal to 0 (zero). The default value is 20.If the Extent and TopoBoundary feature dat...",
                        "default": None
                },
                "minimum_z_value": {
                        "type": "string",
                        "description": "The minimum z-value to be used in the interpolation.The default is 20 percent below the smallest of all the input values.",
                        "default": None
                },
                "maximum_z_value": {
                        "type": "string",
                        "description": "The maximum z-value to be used in the interpolation.The default is 20 percent above the largest of all input values.",
                        "default": None
                },
                "enforce": {
                        "type": "string",
                        "description": "The type of drainage enforcement to apply.The drainage enforcement option can be set to attempt to remove all sinks or depressions so a hydrologically correct DEM can be created. If sink points have b...",
                        "default": None
                },
                "data_type": {
                        "type": "string",
                        "description": "The dominant elevation data type of the input feature data.CONTOUR\u2014The dominant type of input data will be elevation contours. This is the default.SPOT\u2014The dominant type of input will be point.\r\nSpeci...",
                        "default": None
                },
                "maximum_iterations": {
                        "type": "string",
                        "description": "The maximum number of interpolation iterations.The number of iterations must be greater than zero. A default of 20 is normally adequate for both contour and line data.A value of 30 will clear fewer si...",
                        "default": None
                },
                "roughness_penalty": {
                        "type": "string",
                        "description": "The integrated squared second derivative as a measure of roughness.\r\nThe roughness penalty must be zero or greater. If the primary input data type is CONTOUR, the default is zero. If the primary data ...",
                        "default": None
                },
                "discrete_error_factor": {
                        "type": "string",
                        "description": "The discrete error factor is used to adjust the amount of smoothing when converting the input data to a raster.The value must be greater than zero. The normal range of adjustment is 0.25 to 4, and the...",
                        "default": None
                },
                "vertical_standard_error": {
                        "type": "string",
                        "description": "The amount of random error in the z-values of the input data.The value must be zero or greater. The default is zero.The vertical standard error may be set to a small positive value if the data has sig...",
                        "default": None
                },
                "tolerance_1": {
                        "type": "string",
                        "description": "This tolerance reflects the accuracy and density of the elevation points in relation to surface drainage.For point datasets, set the tolerance to the standard error of the data heights. For contour da...",
                        "default": None
                },
                "tolerance_2": {
                        "type": "string",
                        "description": "This tolerance prevents drainage clearance through unrealistically high barriers.\r\nThe value must be greater than zero. The default is 100 if the data type is CONTOUR and 200 if the data type is SPOT.",
                        "default": None
                },
                "out_stream_features": {
                        "type": "string",
                        "description": "The output line feature class of stream polyline features and ridge line features.The line features are created at the beginning of the interpolation process. It provides the general morphology of the...",
                        "default": None
                },
                "out_sink_features": {
                        "type": "string",
                        "description": "The output point feature class of the remaining sink point features.These are the sinks that were not specified in the sink input feature data and were not cleared during drainage enforcement. Adjusti...",
                        "default": None
                },
                "out_diagnostic_file": {
                        "type": "string",
                        "description": "The output diagnostic file listing all inputs and parameters used and the number of sinks cleared at each resolution and iteration.",
                        "default": None
                },
                "out_parameter_file": {
                        "type": "string",
                        "description": "The output parameter file listing all inputs and parameters used, which can be used with Topo to Raster by File to run the interpolation again.",
                        "default": None
                },
                "profile_penalty": {
                        "type": "string",
                        "description": "The profile curvature roughness penalty is a locally adaptive penalty that can be used to partly replace total curvature.It can yield good results with high-quality contour data but can lead to instab...",
                        "default": None
                },
                "out_residual_feature": {
                        "type": "string",
                        "description": "The output point feature class of all the large elevation residuals as scaled by the local discretisation error.All the scaled residuals larger than 10 should be inspected for possible errors in input...",
                        "default": None
                },
                "out_stream_cliff_error_feature": {
                        "type": "string",
                        "description": "The output point feature class of locations where possible stream and cliff errors occur.The locations where the streams have closed loops, distributaries, and streams over cliffs can be identified fr...",
                        "default": None
                },
                "out_contour_error_feature": {
                        "type": "string",
                        "description": "The output point feature class of possible errors pertaining to the input contour data.Contours with bias in height exceeding five times the standard deviation of the contour values as represented on ...",
                        "default": None
                }
        },
        "required": [
                "in_topo_featurestopo_input"
        ]
},
    "topo_to_raster_by_file": {
        "name": "topo_to_raster_by_file",
        "description": "Interpolates a hydrologically correct raster surface from point, line, and polygon data using parameters specified in a file. Learn more about how Topo to Raster works",
        "parameters": {
                "in_parameter_file": {
                        "type": "string",
                        "description": "The input ASCII text file containing the inputs and parameters to use for the interpolation.The file is typically created from a previous run of Topo to Raster with the optional output parameter file ..."
                },
                "out_stream_features": {
                        "type": "string",
                        "description": "Output feature class of stream polyline features.The polyline features are coded as follows:1. Input stream line not over cliff.2. Input stream line over cliff (waterfall).3. Drainage enforcement clea...",
                        "default": None
                },
                "out_sink_features": {
                        "type": "string",
                        "description": "Output feature class of remaining sink point features.",
                        "default": None
                },
                "out_residual_feature": {
                        "type": "string",
                        "description": "The output point feature class of all the large elevation residuals as scaled by the local discretisation error.All the scaled residuals larger than 10 should be inspected for possible errors in input...",
                        "default": None
                },
                "out_stream_cliff_error_feature": {
                        "type": "string",
                        "description": "The output point feature class of locations where possible stream and cliff errors occur.The locations where the streams have closed loops, distributaries, and streams over cliffs can be identified fr...",
                        "default": None
                },
                "out_contour_error_feature": {
                        "type": "string",
                        "description": "The output point feature class of possible errors pertaining to the input contour data.Contours with bias in height exceeding five times the standard deviation of the contour values as represented on ...",
                        "default": None
                }
        },
        "required": [
                "in_parameter_file"
        ]
},
    "trend": {
        "name": "trend",
        "description": "Interpolates a raster surface from points using a trend technique. Learn more about how Trend works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated into a surface raster."
                },
                "z_field": {
                        "type": "string",
                        "description": "The field that holds a height or magnitude value for each point.This can be a numeric field or the Shape field if the input point features contain z-values.If the regression type is Logistic, the valu..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "order": {
                        "type": "string",
                        "description": "The order of the polynomial.This must be an integer between 1 and 12. A value of 1 will fit a flat plane to the points, and a higher value will fit a more complex surface. The default is 1.",
                        "default": None
                },
                "regression_type": {
                        "type": "string",
                        "description": "The type of regression to be performed.LINEAR\u2014Polynomial regression is performed to fit a least-squares surface to the set of input points. This is applicable for continuous types of data.LOGISTIC\u2014Log...",
                        "default": None
                },
                "out_rms_file": {
                        "type": "string",
                        "description": "File name for the output text file that contains information about the RMS error and the Chi-Square of the interpolation.The extension must be .txt.",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "z_field"
        ]
},
    "cell_statistics": {
        "name": "cell_statistics",
        "description": "Calculates a per-cell statistic from multiple rasters. The available statistics are Majority, Maximum, Mean, Median, Minimum, Minority, Percentile, Range, Standard deviation, Sum, and Variety. Learn more about how Cell Statistics works",
        "parameters": {
                "in_rasters_or_constantsin_raster_or_constant": {
                        "type": "string",
                        "description": "A list of input rasters for which a statistical operation will be calculated for each cell in the analysis window.A number can be used as an input; however, the cell size and extent must first be set ..."
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The mean (average) of the inputs will be calculated. This is the default.MAJORITY\u2014The majority (value that occurs most often) of the inputs will be d...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored by the statistic calculation.DATA\u2014At the processing cell location, if any of the input rasters has NoData, that NoData value will be ignored. The statis...",
                        "default": None
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.\r\nSINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_B...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile value that will be calculated. The default is 90, indicating the 90th percentile.The value can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the specified percentile value is between two input cell values.AUTO_DETECT\u2014If the input rasters are of integer pixel type, the NEAREST met...",
                        "default": None
                }
        },
        "required": [
                "in_rasters_or_constantsin_raster_or_constant"
        ]
},
    "combine": {
        "name": "combine",
        "description": "Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.",
        "parameters": {
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The list of input rasters to be combined."
                }
        },
        "required": [
                "in_rastersin_raster"
        ]
},
    "equal_to_frequency": {
        "name": "equal_to_frequency",
        "description": "Evaluates on a cell-by-cell basis the number of times the values in a set of rasters are equal to another raster.",
        "parameters": {
                "in_value_raster": {
                        "type": "string",
                        "description": "For each cell location in the input value raster, the number of occurrences (frequency) where a raster in the input list has an equal value is counted."
                },
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The list of rasters that will be compared to the value raster."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.SINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_BAN...",
                        "default": None
                }
        },
        "required": [
                "in_value_raster",
                "in_rastersin_raster"
        ]
},
    "greater_than_frequency": {
        "name": "greater_than_frequency",
        "description": "Evaluates on a cell-by-cell basis the number of times a set of rasters is greater than another raster.",
        "parameters": {
                "in_value_raster": {
                        "type": "string",
                        "description": "For each cell location in the input value raster, the number of occurrences (frequency) where a raster in the input list has a greater value is counted."
                },
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The list of rasters that will be compared to the value raster."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.\r\nSINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_B...",
                        "default": None
                }
        },
        "required": [
                "in_value_raster",
                "in_rastersin_raster"
        ]
},
    "highest_position": {
        "name": "highest_position",
        "description": "Determines on a cell-by-cell basis the position of the raster with the maximum value in a set of rasters.",
        "parameters": {
                "in_rasters_or_constantsin_raster_or_constant": {
                        "type": "string",
                        "description": "The list of input rasters for which the position of the input with the highest value will be determined.A number can be used as an input; however, the cell size and extent must first be set in the env..."
                }
        },
        "required": [
                "in_rasters_or_constantsin_raster_or_constant"
        ]
},
    "less_than_frequency": {
        "name": "less_than_frequency",
        "description": "Evaluates on a cell-by-cell basis the number of times a set of rasters is less than another raster.",
        "parameters": {
                "in_value_raster": {
                        "type": "string",
                        "description": "For each cell location in the input value raster, the number of occurrences (frequency) where a raster in the input list has a lesser value is counted."
                },
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The list of rasters that will be compared to the value raster."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.SINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_BAN...",
                        "default": None
                }
        },
        "required": [
                "in_value_raster",
                "in_rastersin_raster"
        ]
},
    "lowest_position": {
        "name": "lowest_position",
        "description": "Determines on a cell-by-cell basis the position of the raster with the minimum value in a set of rasters.",
        "parameters": {
                "in_rasters_or_constantsin_raster_or_constant": {
                        "type": "string",
                        "description": "The list of input rasters for which the position of the input with the lowest value will be determined.A number can be used as an input; however, the cell size and extent must first be set in the envi..."
                }
        },
        "required": [
                "in_rasters_or_constantsin_raster_or_constant"
        ]
},
    "popularity": {
        "name": "popularity",
        "description": "Determines the value in an argument list that is at a certain level of popularity on a cell-by-cell basis. The particular level of popularity (the number of occurrences of each value) is specified by the first argument.",
        "parameters": {
                "in_popularity_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster that defines the popularity position to be returned.A number can be used as an input; however, the cell size and extent must first be set in the environment."
                },
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The list of input rasters used to evaluate the popularity of the values for each cell location."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.SINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_BAN...",
                        "default": None
                }
        },
        "required": [
                "in_popularity_raster_or_constant",
                "in_rastersin_raster"
        ]
},
    "rank": {
        "name": "rank",
        "description": "Ranks on a cell-by-cell basis the values from a set of input rasters and determines which values are returned based on the value of the rank input raster.",
        "parameters": {
                "in_rank_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster that defines the rank position to be returned.A number can be used as an input; however, the cell size and extent must first be set in the environment."
                },
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The list of input rasters from which the cell value of the raster at the specified rank position will be obtained.\r\nFor example, consider a particular location where the cell values in the three input..."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.\r\nSINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_B...",
                        "default": None
                }
        },
        "required": [
                "in_rank_raster_or_constant",
                "in_rastersin_raster"
        ]
},
    "raster_calculator": {
        "name": "raster_calculator",
        "description": "Build and run a single map algebra expression using Python syntax. Learn more about how Raster Calculator works",
        "parameters": {
                "expression": {
                        "type": "string",
                        "description": "Note:In Python, create and run map algebra expressions using the Spatial Analyst module, which is an extension of the ArcPy Python site package.See Map algebra to learn how to perform an analysis in P..."
                },
                "output_raster": {
                        "type": "string",
                        "description": "Note:See Create output for information about producing output from map algebra expressions in Python."
                }
        },
        "required": [
                "expression",
                "output_raster"
        ]
},
    "abs": {
        "name": "abs",
        "description": "Calculates the absolute value of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster for which to calculate the absolute values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "divide": {
        "name": "divide",
        "description": "Divides the values of two rasters on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input whose values will be divided by the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inp..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input whose values the first input are to be divided by.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both in..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "exp": {
        "name": "exp",
        "description": "Calculates the base e exponential of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values for which to find the base e exponential.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "exp10": {
        "name": "exp10",
        "description": "Calculates the base 10 exponential of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values for which to find the base 10 exponential.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "exp2": {
        "name": "exp2",
        "description": "Calculates the base 2 exponential of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values for which to find the base 2 exponential.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "float": {
        "name": "float",
        "description": "Converts each cell value of a raster into a floating-point representation.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster to be converted to floating point.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "int": {
        "name": "int",
        "description": "Converts each cell value of a raster to an integer by truncation.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster to be converted to integer.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "ln": {
        "name": "ln",
        "description": "Calculates the natural logarithm (base e) of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "Input values for which to find the natural logarithm (Ln).To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "log10": {
        "name": "log10",
        "description": "Calculates the base 10 logarithm of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "Input values for which to find the base 10 logarithm.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "log2": {
        "name": "log2",
        "description": "Calculates the base 2 logarithm of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "Input values for which to find the base 2 logarithm.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "minus": {
        "name": "minus",
        "description": "Subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input from which to subtract the values in the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for bot..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input values to subtract from the values in the first input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for bot..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "mod": {
        "name": "mod",
        "description": "Finds the remainder (modulo) of the first raster when divided by the second raster on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The numerator input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size and extent must firs..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The denominator input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size and extent must fi..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "negate": {
        "name": "negate",
        "description": "Changes the sign (multiplies by -1) of the cell values of the input raster on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster to be negated (multiplied by -1).To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "plus": {
        "name": "plus",
        "description": "Adds (sums) the values of two rasters on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input whose values will be added to.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input whose values will be added to the first input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "power": {
        "name": "power",
        "description": "Raises the cell values in a raster to the power of the values found in another raster.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input values to be raised to the power defined by the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input that determines the power the values in the first input will be raised to.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To spec..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "round_down": {
        "name": "round_down",
        "description": "Returns the next lower integer value, just represented as a floating point, for each cell in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to be rounded down.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "round_up": {
        "name": "round_up",
        "description": "Returns the next higher integer value, just represented as a floating point, for each cell in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to be rounded up.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "square": {
        "name": "square",
        "description": "Calculates the square of the cell values in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to find the square of.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "square_root": {
        "name": "square_root",
        "description": "Calculates the square root of the cell values in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to find the square root of.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "times": {
        "name": "times",
        "description": "Multiplies the values of two rasters on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input containing the values to be multiplied.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input containing the values by which the first input will be multiplied.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a nu..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "bitwise_and": {
        "name": "bitwise_and",
        "description": "Performs a Bitwise And operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this bitwise operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this bitwise operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "bitwise_left_shift": {
        "name": "bitwise_left_shift",
        "description": "Performs a Bitwise Left Shift operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input on which to perform the shift.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input defining the number of positions to shift the bits.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both i..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "bitwise_not": {
        "name": "bitwise_not",
        "description": "Performs a Bitwise Not (complement) operation on the binary value of an input raster. Learn more about how Bitwise Math tools work",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster on which to perform the Bitwise Not (complement) operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a nu..."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "bitwise_or": {
        "name": "bitwise_or",
        "description": "Performs a Bitwise Or operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this bitwise operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this bitwise operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "bitwise_right_shift": {
        "name": "bitwise_right_shift",
        "description": "Performs a Bitwise Right Shift operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input on which to perform the shift.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input defining the number of positions to shift the bits.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both i..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "bitwise_xor": {
        "name": "bitwise_xor",
        "description": "Performs a Bitwise eXclusive Or operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this bitwise operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this bitwise operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "boolean_and": {
        "name": "boolean_and",
        "description": "Performs a Boolean And operation on the cell values of two input rasters. If both input values are true (non-zero), the output value is 1. If one or both inputs are false (zero), the output is 0. Learn more about how the Boolean math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this Boolean operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this Boolean operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "boolean_not": {
        "name": "boolean_not",
        "description": "Performs a Boolean Not (complement) operation on the cell values of the input raster. If the input values are true (non-zero), the output value is 0. If the input values are false (zero), the output is 1. Learn more about how the Boolean math tools work",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input to use in this Boolean operation.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "boolean_or": {
        "name": "boolean_or",
        "description": "Performs a Boolean Or operation on the cell values of two input rasters. If one or both input values are true (non-zero), the output value is 1. If both input values are false (zero), the output is 0. Learn more about how the Boolean math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this Boolean operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this Boolean operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "boolean_xor": {
        "name": "boolean_xor",
        "description": "Performs a Boolean eXclusive Or operation on the cell values of two input rasters. If one input value is true (non-zero) and the other false (zero), the output is 1. If both input values are true or both are false, the output is 0. Learn more about how the Boolean math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this Boolean operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this Boolean operation.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "combinatorial_and": {
        "name": "combinatorial_and",
        "description": "Performs a Combinatorial And operation on the cell values of two input rasters. If both input values are true (non-zero), the output is a different value for each unique combination of input values. If one or both inputs are false (zero), the output value is 0. Learn more about how Combinatorial tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this combinatorial operation.It must be of integer type.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specif..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this combinatorial operation.It must be of integer type.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To speci..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "combinatorial_or": {
        "name": "combinatorial_or",
        "description": "Performs a Combinatorial Or operation on the cell values of two input rasters. If either input value is true (non-zero), the output is a different value for each unique combination of input values. If both inputs are false (zero), the output value is 0. Learn more about how Combinatorial tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this combinatorial operation.It must be of integer type.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specif..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this combinatorial operation.It must be of integer type.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To speci..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "combinatorial_xor": {
        "name": "combinatorial_xor",
        "description": "Performs a Combinatorial eXclusive Or operation on the cell values of two input rasters. If one input value is true (non-zero) and the other false (zero), the output is a different value for each unique combination of input values. If both inputs are true or both are false, the output value is 0. Learn more about how Combinatorial tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The first input to use in this combinatorial operation.It must be of integer type.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specif..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The second input to use in this combinatorial operation.It must be of integer type.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To speci..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "equal_to": {
        "name": "equal_to",
        "description": "Performs a Relational equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster equals the second raster and 0 for cells where it does not. Learn more about how the Relational Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input that will be compared to for equality by the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input that will be compared from for equality by the first input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number fo..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "greater_than": {
        "name": "greater_than",
        "description": "Performs a Relational greater-than operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is greater than the second raster and 0 for cells if it is not. Learn more about how the Relational Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input being tested to determine if it is greater than the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a num..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input against which the first input is tested to be greater than.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number fo..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "greater_than_equal": {
        "name": "greater_than_equal",
        "description": "Performs a Relational greater-than-or-equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is greater than or equal to the second raster and 0 if it is not. Learn more about how the Relational Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input being tested to determine if it is greater than or equal to the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To s..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input against which the first input is tested to be greater than or equal to.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "less_than": {
        "name": "less_than",
        "description": "Performs a Relational less-than operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is less than the second raster and 0 if it is not. Learn more about how the Relational Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input being tested to determine if it is less than the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input against which the first input is tested to be less than.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for b..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "less_than_equal": {
        "name": "less_than_equal",
        "description": "Performs a Relational less-than-or-equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is less than or equal to the second raster and 0 where it is not. Learn more about how the Relational Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input being tested to determine if it is less than or equal to the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To spec..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input against which the first input is tested to be less than or equal to.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "not_equal": {
        "name": "not_equal",
        "description": "Performs a Relational not-equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is not equal to the second raster and 0 for cells where it is equal. Learn more about how the Relational Math tools work",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input that will be compared to for inequality by the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number f..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input that will be compared from for inequality by the first input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number ..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "diff": {
        "name": "diff",
        "description": "Determines which values from the first input are logically different from the values of the second input on a cell-by-cell basis. If the values on the two inputs are different, the value on the first input is output. If the values on the two inputs are the same, the output is 0.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input to which the second input will be compared.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, t..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input to which the first input will be compared.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, th..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "inlist": {
        "name": "inlist",
        "description": "Determines which values from the first input are contained in a set of other inputs, on a cell-by-cell basis. For each cell, if the value of the first input raster is found in any of the list of other inputs, that value will be assigned to the output raster. If it is not found, the output cell will be NoData.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input that defines the value that will be looked for in a list of rasters on a cell-by-cell basis.A number can be used as an input for this parameter, provided a raster is specified for the other ..."
                },
                "in_raster_or_constantsin_raster_or_constant": {
                        "type": "string",
                        "description": "A list of input rasters that the first input will be evaluated against. For each location, if the cell value from the first input exists in any of the other rasters, that value will be assigned to the..."
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.\r\nSINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_B...",
                        "default": None
                }
        },
        "required": [
                "in_raster_or_constant",
                "in_raster_or_constantsin_raster_or_constant"
        ]
},
    "is_None": {
        "name": "is_None",
        "description": "Determines which values from the input raster are NoData on a cell-by-cell basis. Returns a value of 1 if the input value is NoData and 0 for cells that are not.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster being tested to identify the cells that are NoData (None).The input can be either integer or floating-point type."
                }
        },
        "required": [
                "in_raster"
        ]
},
    "over": {
        "name": "over",
        "description": "For the cell values in the first input that are not 0, the output value will be that of the first input. Where the cell values are 0, the output will be that of the second input raster.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input for which cell values of 0 will be replaced with the value from the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input whose value will be assigned to the output raster cells where the first input value is 0.A number can be used as an input for this parameter, provided a raster is specified for the other par..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "test": {
        "name": "test",
        "description": "Performs a Boolean evaluation of the input raster using a logical expression. When the expression evaluates to true, the output cell value is 1. If the expression is false, the output cell value is 0.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster on which the Boolean evaluation is performed, based on a logical expression."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The logical expression that will determine which input cells will return a value of true (1) and which will be false (0).The expression follows the general form of an SQL expression. An example of a w..."
                }
        },
        "required": [
                "in_raster",
                "where_clause"
        ]
},
    "acos": {
        "name": "acos",
        "description": "Calculates the inverse cosine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the inverse cosine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "acosh": {
        "name": "acosh",
        "description": "Calculates the inverse hyperbolic cosine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the inverse hyperbolic cosine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "asin": {
        "name": "asin",
        "description": "Calculates the inverse sine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the inverse sine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "asinh": {
        "name": "asinh",
        "description": "Calculates the inverse hyperbolic sine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the inverse hyperbolic sine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "atan": {
        "name": "atan",
        "description": "Calculates the inverse tangent of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the inverse tangent values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "atan2": {
        "name": "atan2",
        "description": "Calculates the inverse tangent (based on x,y) of cells in a raster.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input that specifies the numerator, or y value, to use when calculating the inverse tangent.A number can be used as an input for this parameter, provided a raster is specified for the other parame..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input that specifies the denominator, or x value, to use when calculating the inverse tangent.A number can be used as an input for this parameter, provided a raster is specified for the other para..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "atanh": {
        "name": "atanh",
        "description": "Calculates the inverse hyperbolic tangent of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the inverse hyperbolic tangent values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "cos": {
        "name": "cos",
        "description": "Calculates the cosine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the cosine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "cosh": {
        "name": "cosh",
        "description": "Calculates the hyperbolic cosine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the hyperbolic cosine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "sin": {
        "name": "sin",
        "description": "Calculates the sine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the sine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "sinh": {
        "name": "sinh",
        "description": "Calculates the hyperbolic sine of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the hyperbolic sine values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "tan": {
        "name": "tan",
        "description": "Calculates the tangent of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input for which to calculate the tangent values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "tanh": {
        "name": "tanh",
        "description": "Calculates the hyperbolic tangent of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input to calculate the hyperbolic tangent values for.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "aggregate_multidimensional_raster": {
        "name": "aggregate_multidimensional_raster",
        "description": "Generates a multidimensional raster dataset by combining existing multidimensional raster variables along a dimension.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "dimension": {
                        "type": "string",
                        "description": "The aggregation dimension. This is the dimension along which the variables will be aggregated."
                },
                "aggregation_method": {
                        "type": "string",
                        "description": "Specifies the mathematical method that will be used to combine the aggregated slices in an interval.MEAN\u2014The mean of a pixel's values will be calculated across all slices in the interval. This is the ...",
                        "default": None
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables that will be aggregated along the given dimension. If no variable is specified, all variables with the selected dimension will be aggregated.For example, to aggregate daily t...",
                        "default": None
                },
                "aggregation_def": {
                        "type": "string",
                        "description": "Specifies the dimension interval for which the data will be aggregated.ALL\u2014The data values will be aggregated across all slices. This is the default.INTERVAL_KEYWORD\u2014The variable data will be aggregat...",
                        "default": None
                },
                "interval_keyword": {
                        "type": "string",
                        "description": "Specifies the keyword interval that will be used when aggregating along the dimension. This parameter is required when the aggregation_def parameter is set to INTERVAL_KEYWORD and the aggregation must...",
                        "default": None
                },
                "interval_value": {
                        "type": "string",
                        "description": "The size of the interval that will be used for the aggregation. This parameter is required when the aggregation_def parameter is set to INTERVAL_VALUE.For example, to aggregate 30 years of monthly tem...",
                        "default": None
                },
                "interval_unit": {
                        "type": "string",
                        "description": "The unit that will be used for the interval_value parameter. This parameter is required when the dimension parameter is set to a time field and the aggregation_def parameter is set to INTERVAL_VALUE.I...",
                        "default": None
                },
                "interval_ranges": {
                        "type": "string",
                        "description": "Interval ranges specified in a value table will be used to aggregate groups of values. The value table consists of pairs of minimum and maximum range values, with data type Double or Date.\r\nThis param...",
                        "default": None
                },
                "aggregation_function": {
                        "type": "string",
                        "description": "A custom raster function that will be used to compute the pixel values of the aggregated rasters. The input is a raster function JSON object or an .rft.xml file created from a function chain or a cust...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored in the analysis.DATA\u2014The analysis will include all valid pixels along a given dimension and ignore NoData pixels. This is the default.NODATA\u2014The analysi...",
                        "default": None
                },
                "dimensionless": {
                        "type": "string",
                        "description": "Specifies whether the layer will have dimension values. This parameter is only enabled if a single slice is selected to create a layer.NO_DIMENSIONS\u2014 The layer will not have dimension values.DIMENSION...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of percentile interpolation that will be used when there is an even number of values from the input raster to be calculated.NEAREST\u2014The nearest available value to the desired perc...",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster",
                "dimension"
        ]
},
    "dimensional_moving_statistics": {
        "name": "dimensional_moving_statistics",
        "description": "Calculates statistics over a moving window on multidimensional data along a specified dimension.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster can only be a multidimensional raster in Cloud Raster Format (.crf file)."
                },
                "dimension": {
                        "type": "string",
                        "description": "The name of the dimension along which the window will move.The default value is the first dimension other than x,y found in the input multidimensional raster.",
                        "default": None
                },
                "backward_window": {
                        "type": "string",
                        "description": "The value of how many slices before or above to be included in the defined window. The value must be a positive integer from 1 to 100. The default value is 1.The unit of this parameter is slice.",
                        "default": None
                },
                "forward_window": {
                        "type": "string",
                        "description": "The value of how many slices after or below to be included in the defined window. The value must be a positive integer from 1 to 100. The default value is 1.The unit of this parameter is slice.",
                        "default": None
                },
                "nodata_handling": {
                        "type": "string",
                        "description": "Specifies how NoData values will be handled by the statistic calculation.DATA\u2014NoData values in the value input will be ignored in the results of the defined window that they fall within. This is the d...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The mean (average value) of the cells in the defined window will be calculated. This is the default.CIRCULAR_MEAN\u2014The mean for angles or other cyclic...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile value that will be calculated. The default is 90, for the 90th percentile.The value can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and t...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the percentile value falls between two cell values.This parameter is only supported if the statistics_type parameter is set to MEDIAN or PE...",
                        "default": None
                },
                "circular_wrap_value": {
                        "type": "string",
                        "description": "The value that will be used to convert a linear value to the range of a given circular mean. Its value must be positive. The default value is 360 degrees.\r\nThis parameter is only supported if the stat...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "generate_multidimensional_anomaly": {
        "name": "generate_multidimensional_anomaly",
        "description": "Computes the anomaly for each slice in an existing multidimensional raster to generate a new multidimensional raster. An anomaly is the deviation of an observation from its standard or mean value.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables for which anomalies will be calculated. If no variable is specified, all variables with a time dimension will be analyzed.",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to calculate the anomaly.\r\nDIFFERENCE_FROM_MEAN\u2014The difference between a pixel's value and the mean of that pixel's values across slices defined by the interval ...",
                        "default": None
                },
                "calculation_interval": {
                        "type": "string",
                        "description": "Specifies the temporal interval that will be used to calculate the mean.ALL\u2014The mean is calculated across all slices for each pixel.YEARLY\u2014The yearly mean is calculated for each pixel.RECURRING_MONTHL...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored in the analysis.DATA\u2014The analysis will include all valid pixels along a given dimension and ignore NoData pixels. This is the default.NODATA\u2014The analysi...",
                        "default": None
                },
                "reference_mean_raster": {
                        "type": "string",
                        "description": "The reference raster dataset that contains a previously calculated mean for each pixel. The anomalies will be calculated in comparison to this mean.",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster"
        ]
},
    "band_collection_statistics": {
        "name": "band_collection_statistics",
        "description": "Calculates the statistics for a set of raster bands. Learn more about how Band Collection Statistics works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands.They can be integer or floating point type."
                },
                "out_stat_file": {
                        "type": "string",
                        "description": "The output ASCII file containing the statistics.A .txt extension is required."
                },
                "compute_matrices": {
                        "type": "string",
                        "description": "Specifies whether covariance and correlation matrices are calculated.BRIEF\u2014Only the basic statistical measures (minimum, maximum, mean, and standard deviation) will be calculated for every layer. This...",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band",
                "out_stat_file"
        ]
},
    "class_probability": {
        "name": "class_probability",
        "description": "Creates a multiband raster of probability bands, with one band being created for each class represented in the input signature file. Learn more about how Class Probability works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands.They can be integer or floating point type."
                },
                "in_signature_file": {
                        "type": "string",
                        "description": "Input signature file whose class signatures are used to generate the a priori probability bands.A .gsg extension is required."
                },
                "maximum_output_value": {
                        "type": "string",
                        "description": "Factor for scaling the range of values in the output probability bands.By default, the values range from 0 to 100.",
                        "default": None
                },
                "a_priori_probabilities": {
                        "type": "string",
                        "description": "Specifies how a priori probabilities will be determined.\r\nEQUAL\u2014All classes will have the same a priori probability.SAMPLE\u2014A priori probabilities will be proportional to the number of cells in each cl...",
                        "default": None
                },
                "in_a_priori_file": {
                        "type": "string",
                        "description": "A text file containing a priori probabilities for the input signature classes.An input for the a priori probability file is only required when the File option is used.The extension for the a priori fi...",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band",
                "in_signature_file"
        ]
},
    "create_signatures": {
        "name": "create_signatures",
        "description": "Creates an ASCII signature file of classes defined by input sample data and a set of raster bands. Learn more about how Create Signatures works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands for which to create the signatures.They can be integer or floating point type."
                },
                "in_sample_data": {
                        "type": "string",
                        "description": "The input delineating the set of class samples.The input can be an integer raster or a feature dataset."
                },
                "out_signature_file": {
                        "type": "string",
                        "description": "The output signature file.A .gsg extension must be specified."
                },
                "compute_covariance": {
                        "type": "string",
                        "description": "Specifies whether covariance matrices in addition to the means are calculated.COVARIANCE\u2014Both the covariance matrices and the means for all classes of the in_sample_data will be computed. This is the ...",
                        "default": None
                },
                "sample_field": {
                        "type": "string",
                        "description": "Field of the input raster or feature sample data to assign values to the sampled locations (classes).Only integer or string fields are valid fields. The specified number or string will be used as the ...",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band",
                "in_sample_data",
                "out_signature_file"
        ]
},
    "dendrogram": {
        "name": "dendrogram",
        "description": "Constructs a tree diagram (dendrogram) showing attribute distances between sequentially merged classes in a signature file. Learn more about how Dendrogram works",
        "parameters": {
                "in_signature_file": {
                        "type": "string",
                        "description": "Input signature file whose class signatures are used to produce a dendrogram.A .gsg extension is required."
                },
                "out_dendrogram_file": {
                        "type": "string",
                        "description": "The output dendrogram ASCII file.The extension can be .txt or .asc."
                },
                "distance_calculation": {
                        "type": "string",
                        "description": "Specifies the manner in which the distances between classes in multidimensional attribute space are defined.VARIANCE\u2014 The distances between classes will be computed based on the variances and the Eucl...",
                        "default": None
                },
                "line_width": {
                        "type": "string",
                        "description": "Sets the width of the dendrogram in number of characters on a line.The default is 78.",
                        "default": None
                }
        },
        "required": [
                "in_signature_file",
                "out_dendrogram_file"
        ]
},
    "edit_signatures": {
        "name": "edit_signatures",
        "description": "Edits and updates a signature file by merging, renumbering, and deleting class signatures. Learn more about how Edit Signatures works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands for which to edit the signatures.They can be integer or floating point type."
                },
                "in_signature_file": {
                        "type": "string",
                        "description": "Input signature file whose class signatures are to be edited.A .gsg extension is required."
                },
                "in_signature_remap_file": {
                        "type": "string",
                        "description": "Input ASCII remap table containing the class IDs to be merged, renumbered, or deleted.The extension can be .rmp, .asc or .txt. The default is .rmp."
                },
                "out_signature_file": {
                        "type": "string",
                        "description": "The output signature file.A .gsg extension must be specified."
                },
                "sample_interval": {
                        "type": "string",
                        "description": "The interval to be used for sampling.The default is 10.",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band",
                "in_signature_file",
                "in_signature_remap_file",
                "out_signature_file"
        ]
},
    "iso_cluster": {
        "name": "iso_cluster",
        "description": "Uses an isodata clustering algorithm to determine the characteristics of the natural groupings of cells in multidimensional attribute space and stores the results in an output ASCII signature file. Learn more about how Iso Cluster works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands.They can be integer or floating point type."
                },
                "out_signature_file": {
                        "type": "string",
                        "description": "The output signature file.A .gsg extension must be specified."
                },
                "number_classes": {
                        "type": "string",
                        "description": "Number of classes into which to group the cells."
                },
                "number_iterations": {
                        "type": "string",
                        "description": "Number of iterations of the clustering process to run.The default is 20.",
                        "default": None
                },
                "min_class_size": {
                        "type": "string",
                        "description": "Minimum number of cells in a valid class.The default is 20.",
                        "default": None
                },
                "sample_interval": {
                        "type": "string",
                        "description": "The interval to be used for sampling.The default is 10.",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band",
                "out_signature_file",
                "number_classes"
        ]
},
    "iso_cluster_unsupervised_classification": {
        "name": "iso_cluster_unsupervised_classification",
        "description": "Performs unsupervised classification on a series of input raster bands using the Iso Cluster and Maximum Likelihood Classification tools.",
        "parameters": {
                "input_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands.They can be integer or floating point type."
                },
                "number_of_classes": {
                        "type": "string",
                        "description": "Number of classes into which to group the cells."
                },
                "minimum_class_size": {
                        "type": "string",
                        "description": "Minimum number of cells in a valid class.The default is 20.",
                        "default": None
                },
                "sample_interval": {
                        "type": "string",
                        "description": "The interval to be used for sampling.The default is 10.",
                        "default": None
                },
                "output_signature_fileout_signature_file": {
                        "type": "string",
                        "description": "The output signature file.A .gsg extension must be specified.",
                        "default": None
                }
        },
        "required": [
                "input_raster_bandsin_raster_band",
                "number_of_classes"
        ]
},
    "maximum_likelihood_classification": {
        "name": "maximum_likelihood_classification",
        "description": "Performs a maximum likelihood classification on a set of raster bands and creates a classified raster as output. Learn more about how Maximum Likelihood Classification works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands.While the bands can be integer or floating point type, the signature file only allows integer class values."
                },
                "in_signature_file": {
                        "type": "string",
                        "description": "The input signature file whose class signatures are used by the maximum likelihood classifier.A .gsg extension is required."
                },
                "reject_fraction": {
                        "type": "string",
                        "description": "Select a reject fraction, which determines whether a cell will be classified based on its likelihood of being correctly assigned to one of the classes. Cells whose likelihood of being correctly assign...",
                        "default": None
                },
                "a_priori_probabilities": {
                        "type": "string",
                        "description": "Specifies how a priori probabilities will be determined.EQUAL\u2014All classes will have the same a priori probability.SAMPLE\u2014A priori probabilities will be proportional to the number of cells in each clas...",
                        "default": None
                },
                "in_a_priori_file": {
                        "type": "string",
                        "description": "A text file containing a priori probabilities for the input signature classes.An input for the a priori probability file is only required when the File option is used.The extension for the a priori fi...",
                        "default": None
                },
                "out_confidence_raster": {
                        "type": "string",
                        "description": "The output confidence raster dataset shows the certainty of the classification in 14 levels of confidence, with the lowest values representing the highest reliability. If there are no cells classified...",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band",
                "in_signature_file"
        ]
},
    "principal_components": {
        "name": "principal_components",
        "description": "Performs Principal Component Analysis (PCA) on a set of raster bands and generates a single multiband raster as output. Learn more about how Principal Components works",
        "parameters": {
                "in_raster_bandsin_raster_band": {
                        "type": "string",
                        "description": "The input raster bands.They can be integer or floating point type."
                },
                "number_components": {
                        "type": "string",
                        "description": "Number of principal components.The number must be greater than zero and less than or equal to the total number of input raster bands.The default is the total number of rasters in the input.",
                        "default": None
                },
                "out_data_file": {
                        "type": "string",
                        "description": "Output ASCII data file storing principal component parameters.The output data file records the correlation and covariance matrices, the eigenvalues and eigenvectors, the percent variance each eigenval...",
                        "default": None
                }
        },
        "required": [
                "in_raster_bandsin_raster_band"
        ]
},
    "block_statistics": {
        "name": "block_statistics",
        "description": "Partitions the input into non-overlapping blocks and calculates the statistic of the values within each block. The value is assigned to all of the cells in each block in the output. Learn more about how Block Statistics works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster for which a statistic will be calculated for blocks of cells."
                },
                "neighborhood": {
                        "type": "string",
                        "description": "The cells of the processing block that will be used in the statistic calculation. There are several predefined neighborhood types to choose from, or a custom kernel can be defined.Once the neighborhoo...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.\r\n\r\nMEAN\u2014The mean (average value) of the cells in the neighborhood will be calculated.MAJORITY\u2014The majority (value that occurs most often) of the cells in...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored by the statistic calculation.DATA\u2014If a NoData value exists within a block neighborhood, the NoData value will be ignored. Only cells within the neighbor...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "filter": {
        "name": "filter",
        "description": "Performs either a smoothing (Low pass) or edge-enhancing (High pass) filter on a raster. Learn more about how Filter works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster on which to perform the filter operation."
                },
                "filter_type": {
                        "type": "string",
                        "description": "The type of filter operation to perform.LOW\u2014Traverses a low pass 3-by-3 filter over the raster. This option smooths the entire input raster and reduces the significance of anomalous cells. This is the...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Denotes whether NoData values are ignored by the filter calculation.DATA\u2014If a NoData value exists within the filter, the NoData value will be ignored. Only cells within the filter that have data value...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "focal_flow": {
        "name": "focal_flow",
        "description": "Determines the flow of the values in the input raster within each cell's immediate neighborhood. Learn more about how Focal Flow works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input surface raster for which to calculate the focal flow.The eight immediate neighbors of each cell are evaluated to determine the flow.The input raster can be integer or floating-point."
                },
                "threshold_value": {
                        "type": "string",
                        "description": "Defines a value that constitutes the threshold, which must be equaled or exceeded before flow can occur.The threshold value can be either an integer or floating-point value.If the difference between t...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "focal_statistics": {
        "name": "focal_statistics",
        "description": "Calculates for each input cell location a statistic of the values within a specified neighborhood around it. Learn more about how Focal Statistics works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster for which the focal statistics for each input cell will be calculated."
                },
                "neighborhood": {
                        "type": "string",
                        "description": "The cells surrounding a processing cell that will be used in the statistic calculation. There are several predefined neighborhood types to choose from, or a custom kernel can be defined.Once the neigh...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The mean (average value) of the cells in the neighborhood will be calculated.MAJORITY\u2014The majority (value that occurs most often) of the cells in the...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored by the statistic calculation.DATA\u2014If a NoData value exists within a neighborhood, the NoData value will be ignored. Only cells within the neighborhood t...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile value that will be calculated. The default is 90, for the 90th percentile.The value can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and t...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "line_statistics": {
        "name": "line_statistics",
        "description": "Calculates a statistic on the attributes of lines in a circular neighborhood around each output cell. Learn more about how Line Statistics works",
        "parameters": {
                "in_polyline_features": {
                        "type": "string",
                        "description": "The input lines to use in the neighborhood operation.For each output cell, a statistic will be calculated for all of the portions of the input polyline features that fall within a circular neighborhoo..."
                },
                "field": {
                        "type": "string",
                        "description": "The field for which the specified statistic will be calculated. It can be any numeric field of the input line features.\r\nWhen statistics_type is set to Length, the field parameter can be set to NONE.I..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "The search radius that will be used to calculate the statistic within, in map units.The default radius is five times the output cell size.",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.Statistics are calculated on the value of the specified field for all lines within the neighborhood.MEAN\u2014The average field value in each neighborhood, wei...",
                        "default": None
                }
        },
        "required": [
                "in_polyline_features",
                "field"
        ]
},
    "point_statistics": {
        "name": "point_statistics",
        "description": "Calculates a statistic on the points in a neighborhood around each output cell. Learn more about how Point Statistics works",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input points to use in the neighborhood operation.For each output cell, any input points that fall within the defined neighborhood shape around it are identified. For the selected points, values f..."
                },
                "field": {
                        "type": "string",
                        "description": "The field for which the specified statistic will be calculated. It can be any numeric field of the input point features.It can be the Shape field if the input features contain z-values."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "neighborhood": {
                        "type": "string",
                        "description": "The area around each processing cell within which any input points found will be used in the statistics calculation. There are several predefined neighborhood types to choose from.Once the neighborhoo...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.The calculation is performed on the values of the specified field of the points that fall within the specified neighborhood of each output raster cell.MEA...",
                        "default": None
                }
        },
        "required": [
                "in_point_features",
                "field"
        ]
},
    "fuzzy_membership": {
        "name": "fuzzy_membership",
        "description": "Transforms  the input raster   into a 0 to 1 scale, indicating the strength of a membership in a set, based on a specified fuzzification algorithm. A value of 1 indicates full membership in the fuzzy set, with membership decreasing to 0, indicating it is not a member of the fuzzy set. Learn more about how Fuzzy Membership works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster whose values will be scaled from 0 to 1.It can be an integer or a floating-point raster."
                },
                "fuzzy_function": {
                        "type": "string",
                        "description": "Specifies the algorithm used in fuzzification of the input raster.The fuzzy classes are used to specify the type of membership.The types of membership classes are: \r\n  FuzzyGaussian, FuzzyLarge, Fuzzy...",
                        "default": None
                },
                "hedge": {
                        "type": "string",
                        "description": "Defining a hedge increases or decreases the fuzzy membership values which modify the meaning of a fuzzy set. Hedges are useful to help in controlling the criteria or important attributes.NONE\u2014No hedge...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "fuzzy_overlay": {
        "name": "fuzzy_overlay",
        "description": "Combine fuzzy membership rasters data together, based on selected overlay type. Learn more about how Fuzzy Overlay works",
        "parameters": {
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "A list of input membership rasters to be combined in the overlay."
                },
                "overlay_type": {
                        "type": "string",
                        "description": "Specifies the method used to combine two or more membership data.AND\u2014The minimum of the fuzzy memberships from the input fuzzy rasters.OR\u2014The maximum of the fuzzy memberships from the input rasters.PR...",
                        "default": None
                },
                "gamma": {
                        "type": "string",
                        "description": "The gamma value to be used. This is only available when the Overlay type is set to Gamma.Default value is 0.9.",
                        "default": None
                }
        },
        "required": [
                "in_rastersin_raster"
        ]
},
    "locate_regions": {
        "name": "locate_regions",
        "description": "Identifies the best regions, or groups of contiguous cells, from an input utility (suitability) raster that satisfy a specified evaluation criterion and that meet identified shape, size, number, and interregion distance constraints. This tool uses a parameterized region-growing (PRG) algorithm to grow candidate regions from seed cells by adding neighboring cells to the region that best preserves the specified shape but also maximizes utility for the region. Using a selection algorithm and an evaluation criterion\u2014such as the highest average value\u2014the best region or regions are selected from the candidate regions that meet identified size and spatial constraints. An example of a spatial constraint would be maintaining a certain minimum distance between regions. Learn more about how the Locate Regions tool works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input utility raster from which the regions will be derived.The higher the value in the input raster, the greater the utility.The raster can be of either integer or floating-point type."
                },
                "total_area": {
                        "type": "string",
                        "description": "The total amount of area for all regions.The default is 10 percent of the input cells within the processing extent.",
                        "default": None
                },
                "area_units": {
                        "type": "string",
                        "description": "Defines the area units used for the total_area, minimum_area, and maximum_area parameters.The available options and their corresponding units are the following:SQUARE_MAP_UNITS\u2014For the square of the l...",
                        "default": None
                },
                "number_of_regions": {
                        "type": "string",
                        "description": "Determines how many regions the total_area will be distributed across.The maximum number of regions that can be specified is 30. The default is 1.",
                        "default": None
                },
                "region_shape": {
                        "type": "string",
                        "description": "Defines the shape characteristics for the output regions.The regions start out from seed cell locations and grow outward with preference given to the cells that maintain the desired shape.The availabl...",
                        "default": None
                },
                "region_orientation": {
                        "type": "string",
                        "description": "Defines the orientation of the defined shape. Regions are grown out from the seed locations with preference given to the cells that maintain the desired orientation of the region shapes.The orientatio...",
                        "default": None
                },
                "shape_tradeoff": {
                        "type": "string",
                        "description": "Identifies the weight for the cells when growing the candidate regions in the parameterized region-growing algorithm. The weighting is a tradeoff between a cell's contribution for maintaining the regi...",
                        "default": None
                },
                "evaluation_method": {
                        "type": "string",
                        "description": "The evaluation criteria to be used for determining which of the candidate regions identified in the parameterized region-growing algorithm are most preferred. The preference can be specified based on ...",
                        "default": None
                },
                "minimum_area": {
                        "type": "string",
                        "description": "Define the minimum area allowed for each region.The units specified by area_units will be used.To learn more about how regions are created when the minimum and maximum areas are defined, see How regio...",
                        "default": None
                },
                "maximum_area": {
                        "type": "string",
                        "description": "Define the maximum area allowed for each region.The units specified by area_units will be used.To learn more about how regions are created when the minimum and maximum areas are defined, see How regio...",
                        "default": None
                },
                "minimum_distance": {
                        "type": "string",
                        "description": "Define the minimum distance allowed between regions. No two regions can be within this distance.This parameter influences the parameterized region-growing (PRG) algorithm. If a cell has the potential ...",
                        "default": None
                },
                "maximum_distance": {
                        "type": "string",
                        "description": "Define the maximum distance allowed between regions. No region can be farther apart than this distance from at least one other region.When sequentially selecting regions, if the next best region is fa...",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Defines the distance units that will be used for the minimum_distance and maximum_distance parameters.The available options and their corresponding units are the following:MAP_UNITS\u2014For the linear uni...",
                        "default": None
                },
                "in_existing_regions": {
                        "type": "string",
                        "description": "A dataset identifying where regions already exist.The input can be a raster or feature dataset. If the input is a raster, any location in the raster with a valid value is considered already allocated....",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "Defines which neighboring cells to use in the growth of the regions.The available options are the following:FOUR\u2014Only the four direct (orthogonal) neighbors of the region cells will be considered in t...",
                        "default": None
                },
                "no_islands": {
                        "type": "string",
                        "description": "Defines if islands will be allowed within the potential regions.NO_ISLANDS\u2014The parameterized region-growing algorithm ensures there will be no islands within a region.A flood field algorithm is implem...",
                        "default": None
                },
                "region_seeds": {
                        "type": "string",
                        "description": "Defines the number of seeds from which to grow the potential regions.To learn more about how the seeds influence the region growth algorithm, see How seeds are distributed.The available options are th...",
                        "default": None
                },
                "region_resolution": {
                        "type": "string",
                        "description": "Sets the resolution at which region growth occurs.\r\n\r\n\r\nThe input raster will be resampled to the resolution determined by the number of cells identified by this parameter (see below). For example, fo...",
                        "default": None
                },
                "selection_method": {
                        "type": "string",
                        "description": "Identifies how the regions will be selected.The available options are the following:AUTO\u2014The selection method is based on the Number of regions parameter. If the Number of regions is eight or less, th...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "weighted_overlay": {
        "name": "weighted_overlay",
        "description": "Overlays several rasters using a common measurement scale and weights each according to its importance. Learn more about how Weighted Overlay works",
        "parameters": {
                "in_weighted_overlay_table": {
                        "type": "string",
                        "description": "The Weighted Overlay tool allows the calculation of a multiple-criteria analysis between several rasters.An Overlay class is used to define the table. The WOTable object is used to specify the criteri..."
                }
        },
        "required": [
                "in_weighted_overlay_table"
        ]
},
    "weighted_sum": {
        "name": "weighted_sum",
        "description": "Overlays several rasters, multiplying each by their given weight and summing them together. Learn more about how Weighted Sum works",
        "parameters": {
                "in_rasters": {
                        "type": "string",
                        "description": "TheWeighted Sum tool overlays several rasters, multiplying each by their given weight and summing them together.An Overlay class is used to define the table. The WSTable object is used to specify a Py..."
                }
        },
        "required": [
                "in_rasters"
        ]
},
    "create_constant_raster": {
        "name": "create_constant_raster",
        "description": "Creates a raster of a constant value within the extent and cell size of the analysis window.",
        "parameters": {
                "constant_value": {
                        "type": "string",
                        "description": "The constant value with which to populate all the cells in the output raster."
                },
                "data_type": {
                        "type": "string",
                        "description": "Data type of the output raster dataset.INTEGER\u2014An integer raster will be created.FLOAT\u2014A floating-point raster will be created.\r\nIf the specified data type is floating-point, the values of the cells i...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "The extent for the output raster dataset.The Extent is a Python class.In this tool, it is in the form Extent(XMin, YMin, XMax, YMax)where XMin and YMin define the lower left coordinate of the extent, ...",
                        "default": None
                }
        },
        "required": [
                "constant_value"
        ]
},
    "create_normal_raster": {
        "name": "create_normal_raster",
        "description": "Creates a raster of random values with a normal (Gaussian) distribution within the extent and cell size of the analysis window.",
        "parameters": {
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "The extent for the output raster dataset.The Extent is a Python class.In this tool, it is in the form Extent(XMin, YMin, XMax, YMax)where XMin and YMin define the lower left coordinate of the extent, ...",
                        "default": None
                }
        },
        "required": []
},
    "create_random_raster": {
        "name": "create_random_raster",
        "description": "Creates a raster of random floating-point values between 0.0 and 1.0 within the extent and cell size of the analysis window. The Create Random Raster tool in the Data Management toolbox provides enhanced functionality or performance.",
        "parameters": {
                "seed_value": {
                        "type": "string",
                        "description": "A value to be used to reseed the random number generator.This may be an integer or floating-point number. Rasters are not permitted as input.The random number generator is automatically seeded with th...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "The extent for the output raster dataset.The Extent is a Python class.In this tool, it is in the form Extent(XMin, YMin, XMax, YMax)where XMin and YMin define the lower left coordinate of the extent, ...",
                        "default": None
                }
        },
        "required": []
},
    "lookup": {
        "name": "lookup",
        "description": "Creates a raster by looking up values in another field in the table of the input raster.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster that contains a field from which to create a new raster."
                },
                "lookup_field": {
                        "type": "string",
                        "description": "Field containing the desired values for the new raster.It can be a numeric or string type."
                }
        },
        "required": [
                "in_raster",
                "lookup_field"
        ]
},
    "reclass_by_ascii_file": {
        "name": "reclass_by_ascii_file",
        "description": "Reclassifies (or changes) the values of the input cells of a raster using an ASCII remap file. Learn more about how Reclass by ASCII File works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be reclassified."
                },
                "in_remap_file": {
                        "type": "string",
                        "description": "ASCII remap file defining the single values or ranges to be reclassified and the values they will become.Allowed extensions for the ASCII remap files are .rmp, .txt, and .asc."
                },
                "missing_values": {
                        "type": "string",
                        "description": "Denotes whether missing values in the reclass file retain their value or get mapped to NoData.DATA\u2014Signifies that if any cell location on the input raster contains a value that is not present or recla...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_remap_file"
        ]
},
    "reclass_by_table": {
        "name": "reclass_by_table",
        "description": "Reclassifies (or changes) the values of the input cells of a raster using a remap table.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be reclassified."
                },
                "in_remap_table": {
                        "type": "string",
                        "description": "Table holding fields defining value ranges to be reclassified and the values they will become."
                },
                "from_value_field": {
                        "type": "string",
                        "description": "Field holding the beginning value for each value range to be reclassified.This is a numeric field of the input remap table."
                },
                "to_value_field": {
                        "type": "string",
                        "description": "Field holding the ending value for each value range to be reclassified.This is a numeric field of the input remap table."
                },
                "output_value_field": {
                        "type": "string",
                        "description": "Field holding the integer values to which each range should be changed.This is an integer field of the input remap table."
                },
                "missing_values": {
                        "type": "string",
                        "description": "Denotes whether missing values in the reclass table retain their value or get mapped to NoData.DATA\u2014Signifies that if any cell location on the input raster contains a value not present or reclassed in...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_remap_table",
                "from_value_field",
                "to_value_field",
                "output_value_field"
        ]
},
    "reclassify": {
        "name": "reclassify",
        "description": "Reclassifies (or changes) the values in a raster.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be reclassified."
                },
                "reclass_field": {
                        "type": "string",
                        "description": "Field denoting the values that will be reclassified."
                },
                "remap": {
                        "type": "string",
                        "description": "The Remap object is used to specify how to reclassify values of the input raster.There are two ways to define how the values will be reclassified in the output raster: RemapRange and RemapValue. Eithe..."
                },
                "missing_values": {
                        "type": "string",
                        "description": "Denotes whether missing values in the reclass table retain their value or get mapped to NoData.DATA\u2014Signifies that if any cell location on the input raster contains a value that is not present or recl...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "reclass_field",
                "remap"
        ]
},
    "rescale_by_function": {
        "name": "rescale_by_function",
        "description": "Rescales the input raster values by applying a selected transformation function and transforming the resulting values onto a specified continuous evaluation scale. Learn more about how Rescale by Function works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to rescale."
                },
                "transformation_function": {
                        "type": "string",
                        "description": "Specifies the continuous function to transform the input raster.The transformation function classes are used to specify the type of transformation function.The types of transformation function classes...",
                        "default": None
                },
                "from_scale": {
                        "type": "string",
                        "description": "The starting value of the output evaluation scale.The from_scale value cannot be equal to the to_scale value. The from_scale can be lower or higher than the to_scale (for example, from 1 to 10, or fro...",
                        "default": None
                },
                "to_scale": {
                        "type": "string",
                        "description": "The ending value of the output evaluation scale.The to_scale value cannot be equal to the from_scale value. The to_scale can be lower or higher than the from_scale (for example, from 1 to 10, or from ...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "slice": {
        "name": "slice",
        "description": "Slices or reclassifies the range of values of the input cells into zones (classes). The available data classification methods are equal interval, equal area (quantile), natural breaks, standard deviation (mean-centered), standard deviation (mean as a break), defined interval, and geometric interval.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be reclassified."
                },
                "number_zones": {
                        "type": "string",
                        "description": "The number of zones that the input raster will be reclassified into.This parameter is required when the slice_type parameter value is EQUAL_AREA, EQUAL_INTERVAL, NATURAL_BREAKS, or GEOMETRIC_INTERVAL....",
                        "default": None
                },
                "slice_type": {
                        "type": "string",
                        "description": "Specifies the manner in which the input raster will be reclassified into zones.EQUAL_INTERVAL\u2014The range of input values will be equally divided into the specified number of output zones to determine t...",
                        "default": None
                },
                "base_output_zone": {
                        "type": "string",
                        "description": "The starting value that will be used for zones (classes) on the output raster dataset.Classes will be assigned integer values, increasing by 1 from the starting value.The default starting value is 1.",
                        "default": None
                },
                "nodata_to_value": {
                        "type": "string",
                        "description": "Replace NoData with a value in the output.If this parameter is not set, NoData cells will remain as NoData in the output raster.",
                        "default": None
                },
                "class_interval_size": {
                        "type": "string",
                        "description": "The size of the interval between classes.This parameter is required when the slice_type parameter is set to DEFINED_INTERVAL, STANDARD_DEVIATION_MEAN_CENTERED, or STANDARD_DEVIATION_MEAN_BREAK.If DEFI...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "classify_raster": {
        "name": "classify_raster",
        "description": "Classifies a raster dataset based on an Esri classifier definition file (.ecd) and raster dataset inputs. The .ecd file contains all the information needed to perform a specific type of Esri-supported classification. The inputs to this tool must match the inputs used to generate the required .ecd file. The .ecd file can be generated from any of the classifier training tools, such as Train Random Trees Classifier or Train Support Vector Machine Classifier.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify."
                },
                "in_classifier_definition": {
                        "type": "string",
                        "description": "The input Esri classifier definition file (.ecd) containing the statistics for the chosen attributes for the classifier."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for the classifier. This raster is necessary when calculat...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_classifier_definition"
        ]
},
    "compute_confusion_matrix": {
        "name": "compute_confusion_matrix",
        "description": "Computes a confusion matrix with errors of omission and commission and derives a kappa index of agreement, Intersection over Union (IoU), and overall accuracy between the classified map and the reference data. This tool uses the outputs from the Create Accuracy Assessment Points tool or the Update Accuracy Assessment Points tool.",
        "parameters": {
                "in_accuracy_assessment_points": {
                        "type": "string",
                        "description": "The accuracy assessment point feature class created from the Create Accuracy Assessment Points tool, containing the Classified and GrndTruth fields. These fields are both long integer field types."
                },
                "out_confusion_matrix": {
                        "type": "string",
                        "description": "The output file name of the confusion matrix in table format.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table. If the path is n..."
                }
        },
        "required": [
                "in_accuracy_assessment_points",
                "out_confusion_matrix"
        ]
},
    "compute_segment_attributes": {
        "name": "compute_segment_attributes",
        "description": "Computes a set of attributes associated with the segmented image. The input raster can be a single-band or 3-band, 8-bit segmented image.",
        "parameters": {
                "in_segmented_raster": {
                        "type": "string",
                        "description": "The input segmented raster dataset, where all the pixels belonging to a segment have the same converged RGB color. Usually, it is an 8-bit, 3-band RGB raster, but it can also be a 1-band grayscale ras..."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for the classifier. This raster is necessary when calculat...",
                        "default": None
                },
                "used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.COLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This is...",
                        "default": None
                }
        },
        "required": [
                "in_segmented_raster"
        ]
},
    "create_accuracy_assessment_points": {
        "name": "create_accuracy_assessment_points",
        "description": "Creates randomly sampled points for postclassification accuracy assessment. A common practice is to randomly select hundreds of points and label their classification types by referencing reliable sources, such as field work or human interpretation of high-resolution imagery. The reference points are then compared with the classification results at the same locations.",
        "parameters": {
                "in_class_data": {
                        "type": "string",
                        "description": "The input classification image or other thematic GIS reference data. The input can be a raster or feature class.Typical data is a classification image of a single band of integer data type.If using po..."
                },
                "out_points": {
                        "type": "string",
                        "description": "The output point shapefile or feature class that contains the random points to be used for accuracy assessment."
                },
                "target_field": {
                        "type": "string",
                        "description": "Specifies whether the input data is a classified image or ground truth data.A classified image is the image that was just classified. Ground truth data, or reference data, consists of identified featu...",
                        "default": None
                },
                "num_random_points": {
                        "type": "string",
                        "description": "The total number of random points that will be generated.The actual number may exceed but never fall below this number, depending on sampling strategy and number of classes. The default number of rand...",
                        "default": None
                },
                "sampling": {
                        "type": "string",
                        "description": "Specifies the sampling scheme that will be used.STRATIFIED_RANDOM\u2014Randomly distributed points will be created in each class in which each class has a number of points proportional to its relative area...",
                        "default": None
                },
                "polygon_dimension_field": {
                        "type": "string",
                        "description": "A field that defines the dimension (time) of the features. This parameter is used only if the classification result is a multidimensional raster and you want to generate assessment points from a featu...",
                        "default": None
                },
                "min_point_distance": {
                        "type": "string",
                        "description": "The minimum distance between the reference points. The default is 0.",
                        "default": None
                }
        },
        "required": [
                "in_class_data",
                "out_points"
        ]
},
    "export_training_data_for_deep_learning": {
        "name": "export_training_data_for_deep_learning",
        "description": "Converts labeled vector or raster data to deep learning training datasets using a remote sensing image. The output is a folder of image chips and a folder of metadata files in the specified format.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input source imagery, typically multispectral imagery.Examples of the types of input source imagery include multispectral satellite, drone, aerial, and National Agriculture Imagery Program (NAIP)...."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The folder where the output image chips and metadata will be stored.The folder can also be a folder URL that uses a cloud storage connection file (*.acs)."
                },
                "in_class_data": {
                        "type": "string",
                        "description": "The training sample data in either vector or raster form. Vector inputs should follow the training sample format generated using the Training Samples Manager pane. Raster inputs should follow a classi..."
                },
                "image_chip_format": {
                        "type": "string",
                        "description": "Specifies the raster format that will be used for the image chip outputs.The PNG and JPEG formats support up to three bands.TIFF\u2014TIFF format will be used.PNG\u2014PNG format will be used.JPEG\u2014JPEG format w..."
                },
                "tile_size_x": {
                        "type": "string",
                        "description": "The size of the image chips for the x dimension.",
                        "default": None
                },
                "tile_size_y": {
                        "type": "string",
                        "description": "The size of the image chips for the y dimension.",
                        "default": None
                },
                "stride_x": {
                        "type": "string",
                        "description": "The distance to move in the x direction when creating the next image chips.When stride is equal to tile size, there will be no overlap. When stride is equal to half the tile size, there will be 50 per...",
                        "default": None
                },
                "stride_y": {
                        "type": "string",
                        "description": "The distance to move in the y direction when creating the next image chips.When stride is equal to tile size, there will be no overlap. When stride is equal to half the tile size, there will be 50 per...",
                        "default": None
                },
                "output_nofeature_tiles": {
                        "type": "string",
                        "description": "Specifies whether image chips that do not capture training samples will be exported.ALL_TILES\u2014All image chips, including those that do not capture training samples, will be exported.ONLY_TILES_WITH_FE...",
                        "default": None
                },
                "metadata_format": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the output metadata labels. If the input training sample data is a feature class layer, such as a building layer or a standard classification training sample...",
                        "default": None
                },
                "start_index": {
                        "type": "string",
                        "description": "Legacy:This parameter has been deprecated. Use a value of 0 or # in Python.",
                        "default": None
                },
                "class_value_field": {
                        "type": "string",
                        "description": "The field that contains the class values. If no field is specified, the system searches for a value or classvalue field. The field should be numeric, usually an integer. If the feature does not contai...",
                        "default": None
                },
                "buffer_radius": {
                        "type": "string",
                        "description": "The radius of a buffer around each training sample that will be used to delineate a training sample area. This allows you to create circular polygon training samples from points.\r\nThe linear unit of t...",
                        "default": None
                },
                "in_mask_polygons": {
                        "type": "string",
                        "description": "A polygon feature class that delineates the area where image chips will be created.Only image chips that fall completely within the polygons will be created.",
                        "default": None
                },
                "rotation_angle": {
                        "type": "string",
                        "description": "The rotation angle that will be used to generate image chips.\r\nAn image chip will first be generated with no rotation. It will then be rotated at the specified angle to create additional image chips. ...",
                        "default": None
                },
                "reference_system": {
                        "type": "string",
                        "description": "Specifies the type of reference system that will be used to interpret the input image. The reference system specified must match the reference system used to train the deep learning model.MAP_SPACE\u2014A ...",
                        "default": None
                },
                "processing_mode": {
                        "type": "string",
                        "description": "Specifies how all raster items in a mosaic dataset or an image service will be processed. This parameter is applied when the input raster is a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_I...",
                        "default": None
                },
                "blacken_around_feature": {
                        "type": "string",
                        "description": "Specifies whether the pixels around each object or feature in each image tile will be masked out.This parameter only applies when the metadata_format parameter is set to Labeled_Tiles and an input fea...",
                        "default": None
                },
                "crop_mode": {
                        "type": "string",
                        "description": "Specifies whether the exported tiles will be cropped so that they are all the same size.This parameter only applies when the  metadata_format parameter is set to either Labeled_Tiles or Imagenet, and ...",
                        "default": None
                },
                "in_raster2": {
                        "type": "string",
                        "description": "An additional input  imagery source that will be used for image translation methods.This parameter is valid when the metadata_format parameter is set to Classified_Tiles, Export_Tiles, or CycleGAN.",
                        "default": None
                },
                "in_instance_data": {
                        "type": "string",
                        "description": "The training sample data collected that contains classes for instance segmentation. The input can also be a point feature class without a class value field or an integer raster without class informati...",
                        "default": None
                },
                "instance_class_value_field": {
                        "type": "string",
                        "description": "The field that contains the class values for instance segmentation. If no field is specified, the tool will use a value or class value field if one is present. If the feature does not contain a class ...",
                        "default": None
                },
                "min_polygon_overlap_ratio": {
                        "type": "string",
                        "description": "The minimum overlap percentage for a feature to be included in the training data. If the percentage overlap is less than the value specified, the feature will be excluded from the training chip and wi...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_folder",
                "in_class_data",
                "image_chip_format"
        ]
},
    "generate_training_samples_from_seed_points": {
        "name": "generate_training_samples_from_seed_points",
        "description": "Generates training samples from seed points, such as accuracy assessment points or training sample points. A typical use case is generating training samples from an existing source, such as a thematic raster or a feature class.",
        "parameters": {
                "in_class_data": {
                        "type": "string",
                        "description": "The data source that labels the training samples."
                },
                "in_seed_points": {
                        "type": "string",
                        "description": "A point shapefile or feature class to provide the centers of training sample polygons."
                },
                "out_training_feature_class": {
                        "type": "string",
                        "description": "The output training sample feature class in the format that can be used in training tools, including shapefiles. The output feature class can be either a polygon feature class or a point feature class..."
                },
                "min_sample_area": {
                        "type": "string",
                        "description": "The minimum area needed for each training sample, in square meters. The minimum value must be greater than or equal to 0.",
                        "default": None
                },
                "max_sample_radius": {
                        "type": "string",
                        "description": "The longest distance (in meters) from any point within the training sample to its center seed point. If set to 0, the output training sample will be points instead of polygons. The minimum value must ...",
                        "default": None
                }
        },
        "required": [
                "in_class_data",
                "in_seed_points",
                "out_training_feature_class"
        ]
},
    "inspect_training_samples": {
        "name": "inspect_training_samples",
        "description": "Estimates the accuracy of individual training samples. The cross validation accuracy is computed using the previously generated classification training result in an .ecd file and the training samples. Outputs include a raster dataset containing the misclassified class values and a training sample dataset with the accuracy score for each training sample.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be classified."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "A training sample feature class created in the Training Samples Manager pane."
                },
                "in_classifier_definition": {
                        "type": "string",
                        "description": "The .ecd output classifier file from any of the train classifier tools. The .ecd file is a JSON file that contains attribute information, statistics, or other information needed for the classifier."
                },
                "out_training_feature_class": {
                        "type": "string",
                        "description": "The output individual training samples saved as a feature class. The associated attribute table contains an addition field listing the accuracy score."
                },
                "out_misclassified_raster": {
                        "type": "string",
                        "description": "The output misclassified raster having NoData outside training samples. In training samples, correctly classified pixels are represented as NoData, and misclassified pixels are represented by their cl..."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for the classifier. This raster is necessary when calculat...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "in_classifier_definition",
                "out_training_feature_class",
                "out_misclassified_raster"
        ]
},
    "linear_spectral_unmixing": {
        "name": "linear_spectral_unmixing",
        "description": "Performs subpixel classification and calculates the fractional abundance of different land-cover types for individual pixels.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The \r\ninput raster dataset."
                },
                "in_spectral_profile_file": {
                        "type": "string",
                        "description": "The  spectral information for the different land-cover classes.This can be provided as polygon features, a classifier definition file (.ecd) generated from the Train Maximum Likelihood Classifier tool..."
                },
                "value_option": {
                        "type": "string",
                        "description": "Specifies how the output pixel values will be defined.SUM_TO_ONE\u2014Class values for each pixel will be provided in decimal format with the sum of all classes equal to 1. For example, Class1 = 0.16; Clas...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_spectral_profile_file"
        ]
},
    "remove_raster_segment_tiling_artifacts": {
        "name": "remove_raster_segment_tiling_artifacts",
        "description": "Corrects segments or objects cut by tile boundaries during the segmentation process performed as a raster function. This tool is helpful for some regional processes, such as image segmentation, that have inconsistencies near image tile boundaries. This processing step is included in the Segment Mean Shift tool. It should only be used on a segmented image that was not created from that tool.",
        "parameters": {
                "in_segmented_raster": {
                        "type": "string",
                        "description": "Select the segmented raster with the tiling artifacts that you want to remove."
                },
                "tilesizex": {
                        "type": "string",
                        "description": "Specify the tile width from Segment Mean Shift. If left blank, the default is 512 pixels.",
                        "default": None
                },
                "tilesizey": {
                        "type": "string",
                        "description": "Specify the tile height from Segment Mean Shift. If left blank, the default is 512 pixels.",
                        "default": None
                }
        },
        "required": [
                "in_segmented_raster"
        ]
},
    "segment_mean_shift": {
        "name": "segment_mean_shift",
        "description": "Groups adjacent pixels that have similar spectral characteristics into segments.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to segment. This can be a multispectral or grayscale image."
                },
                "spectral_detail": {
                        "type": "string",
                        "description": "The level of importance given to the spectral differences of features in the imagery.Valid values range from 1.0 to 20.0. A higher value is appropriate when there are features to classify separately t...",
                        "default": None
                },
                "spatial_detail": {
                        "type": "string",
                        "description": "The level of importance given to the proximity between features in the imagery.Valid values range from 1.0 to 20. A higher value is appropriate for a scene in which the features of interest are small ...",
                        "default": None
                },
                "min_segment_size": {
                        "type": "string",
                        "description": "The minimum size of a segment. Merge segments smaller than this size with their best fitting neighbor segment. This is related to the minimum mapping unit for your project.Units are in pixels.",
                        "default": None
                },
                "band_indexes": {
                        "type": "string",
                        "description": "The bands that will be used to segment the imagery, separated by a space. If no band indexes are specified, they are determined by the following criteria:\r\n If the raster has only 3 bands, those 3 ban...",
                        "default": None
                },
                "max_segment_size": {
                        "type": "string",
                        "description": "The maximum size of a segment. Segments that are larger than the specified size will be divided. Use this parameter to prevent artifacts in the output raster resulting from large segments.Units are in...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "train_iso_cluster_classifier": {
        "name": "train_iso_cluster_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Iso Cluster classification definition. This tool performs an unsupervised classification.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify."
                },
                "max_classes": {
                        "type": "string",
                        "description": "Maximum number of desired classes to group pixels or segments. This should be set to be greater than the number of classes in your legend.It is possible that you will get fewer classes than what you s..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output JSON format file that will contain attribute information, statistics, hyperplane vectors, and other information for the classifier. An .ecd file will be created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for classification. This parameter is optional.",
                        "default": None
                },
                "max_iterations": {
                        "type": "string",
                        "description": "The maximum number of iterations the clustering process will run.The recommended range is between 10 and 20 iterations. Increasing this value will linearly increase the processing time.",
                        "default": None
                },
                "min_samples_per_cluster": {
                        "type": "string",
                        "description": "The minimum number of pixels or segments in a valid cluster or class.The default value of 20 is effective in creating statistically significant classes. You can increase this number for more larger cl...",
                        "default": None
                },
                "skip_factor": {
                        "type": "string",
                        "description": "Number of pixels to skip for a pixel image input. If a segmented image is an input, specify the number of segments to skip.",
                        "default": None
                },
                "used_attributes_used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.COLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This is...",
                        "default": None
                },
                "max_merge_per_iter": {
                        "type": "string",
                        "description": "The maximum number of cluster merges per iteration. Increasing the number of merges will reduce the number of classes that are created. A lower value will result in more classes.",
                        "default": None
                },
                "max_merge_distance": {
                        "type": "string",
                        "description": "The maximum distance between cluster centers in feature space. Increasing the distance will allow more clusters to merge, resulting in fewer classes. A lower value will result in more classes. Values ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "max_classes",
                "out_classifier_definition"
        ]
},
    "train_maximum_likelihood_classifier": {
        "name": "train_maximum_likelihood_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Maximum Likelihood Classifier (MLC) classification definition.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "The training sample file or layer that delineates the training sites.These can be either shapefiles or feature classes that contain the training samples. The following field names are required in the ..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output JSON format file that will contain attribute information, statistics, hyperplane vectors, and other information for the classifier. An .ecd file will be created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Incorporates ancillary raster datasets, such as a segmented image or DEM. This parameter is optional.",
                        "default": None
                },
                "used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.COLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This is...",
                        "default": None
                },
                "dimension_value_field": {
                        "type": "string",
                        "description": "Contains dimension values in the input training sample feature class.\r\nThis parameter is required to classify a time series of raster data using the change analysis raster output from the Analyze Chan...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "out_classifier_definition"
        ]
},
    "train_random_trees_classifier": {
        "name": "train_random_trees_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Random Trees classification method. The random trees classifier is an image classification technique that is resistant to overfitting and can work with segmented images and other ancillary raster datasets. For standard image inputs, the tool accepts multiband imagery with any bit depth, and it will perform the Random Trees classification on a pixel basis or segment, based on the input training feature file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify.You can use any Esri-supported raster dataset. One option is a 3-band, 8-bit segmented raster dataset in which all the pixels in the same segment have the same color. Th..."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "The training sample file or layer that delineates the training sites.These can be either shapefiles or feature classes that contain the training samples. The following field names are required in the ..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "A JSON file that contains attribute information, statistics, or other information for the classifier. An .ecd file is created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for classification. This parameter is optional.",
                        "default": None
                },
                "max_num_trees": {
                        "type": "string",
                        "description": "The maximum number of trees in the forest. Increasing the number of trees will lead to higher accuracy rates, although this improvement will level off eventually. The number of trees increases the pro...",
                        "default": None
                },
                "max_tree_depth": {
                        "type": "string",
                        "description": "The maximum depth of each tree in the forest. Depth is another way of saying the number of rules each tree is allowed to create to come to a decision. Trees will not grow any deeper than this setting.",
                        "default": None
                },
                "max_samples_per_class": {
                        "type": "string",
                        "description": "The maximum number of samples that will be used to define each class.The default value of 1000 is recommended when the inputs are nonsegmented rasters. A value that is less than or equal to 0 means th...",
                        "default": None
                },
                "used_attributes_used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.\r\nCOLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This ...",
                        "default": None
                },
                "dimension_value_field": {
                        "type": "string",
                        "description": "Contains dimension values in the input training sample feature class.This parameter is required to classify a time series of raster data using the change analysis raster output from the Analyze Change...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "out_classifier_definition"
        ]
},
    "train_support_vector_machine_classifier": {
        "name": "train_support_vector_machine_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Support Vector Machine (SVM) classification definition.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify.The preferred input is a 3-band, 8-bit segmented raster dataset in which all the pixels in the same segment have the same color. The input can also be a 1-band, 8-bit gr..."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "The training sample file or layer that delineates the training sites.These can be either shapefiles or feature classes that contain the training samples. The following field names are required in the ..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output JSON format file that will contain attribute information, statistics, hyperplane vectors, and other information for the classifier. An .ecd file will be created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for classification. This parameter is optional.",
                        "default": None
                },
                "max_samples_per_class": {
                        "type": "string",
                        "description": "The maximum number of samples that will be used to define each class.The default value of 500 is recommended when the inputs are nonsegmented rasters. A value that is less than or equal to 0 means tha...",
                        "default": None
                },
                "used_attributes_used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.\r\nCOLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This ...",
                        "default": None
                },
                "dimension_value_field": {
                        "type": "string",
                        "description": "Contains dimension values in the input training sample feature class.\r\nThis parameter is required to classify a time series of raster data using the change analysis raster output from the Analyze Chan...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "out_classifier_definition"
        ]
},
    "update_accuracy_assessment_points": {
        "name": "update_accuracy_assessment_points",
        "description": "Updates the Target field in the attribute table to compare reference points to the classified image. Accuracy assessment uses known points to assess the validity of the classification model.",
        "parameters": {
                "in_class_data": {
                        "type": "string",
                        "description": "The input classification image or other thematic GIS reference data. The input can be a raster or feature class.Typical data is a classification image of a single band of integer data type.If using po..."
                },
                "in_points": {
                        "type": "string",
                        "description": "The point feature class with the accuracy assessment points that will be updated.\r\nAll points from this input will be copied to the updated output feature class, and the target_field parameter value w..."
                },
                "out_points": {
                        "type": "string",
                        "description": "The output point shapefile or feature class that contains the random points to be used for accuracy assessment."
                },
                "target_field": {
                        "type": "string",
                        "description": "Specifies whether the input data is a classified image or ground truth data.A classified image is the image that was just classified. Ground truth data, or reference data, consists of identified featu...",
                        "default": None
                },
                "polygon_dimension_field": {
                        "type": "string",
                        "description": "The dimension field for the in_points parameter value. The assessment points will be updated based on the matching dimension values with this field.",
                        "default": None
                },
                "point_dimension_field": {
                        "type": "string",
                        "description": "The dimension field in the in_points parameter value. Input data with identical dimension values will be used to update corresponding points.\r\n\r\n\r\nWhen the in_class_data parameter value is a multidime...",
                        "default": None
                }
        },
        "required": [
                "in_class_data",
                "in_points",
                "out_points"
        ]
},
    "area_solar_radiation": {
        "name": "area_solar_radiation",
        "description": "Derives incoming solar radiation from a raster surface. This tool is deprecated and will be removed in a future release. The Raster Solar Radiation tool provides enhanced functionality or performance.",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input elevation surface raster."
                },
                "latitude": {
                        "type": "string",
                        "description": "The latitude for the site area. The units are decimal degrees with positive values for the northern hemisphere and negative values for the southern hemisphere.For input surface rasters containing a sp...",
                        "default": None
                },
                "sky_size": {
                        "type": "string",
                        "description": "The resolution or sky size for the viewshed, sky map, and sun map rasters. The units are cells.The default is a raster of 200 by 200 cells.",
                        "default": None
                },
                "time_configuration": {
                        "type": "string",
                        "description": "Specifies the time configuration (period) that will be used for calculating solar radiation.The Time class objects will be used to specify the time configuration.The different types of time configurat...",
                        "default": None
                },
                "day_interval": {
                        "type": "string",
                        "description": "The time interval through the year (units: days) that will be used to calculate sky sectors for the sun map.The default value is 14 (biweekly).",
                        "default": None
                },
                "hour_interval": {
                        "type": "string",
                        "description": "The time interval through the day (units: hours) that will be used to calculate sky sectors for the sun map.The default value is 0.5.",
                        "default": None
                },
                "each_interval": {
                        "type": "string",
                        "description": "Specifies whether a single total insolation value will be calculated for all locations or multiple values will be calculated for the specified hour and day interval.\r\n\r\nNOINTERVAL\u2014A single total radia...",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                },
                "slope_aspect_input_type": {
                        "type": "string",
                        "description": "Specifies how slope and aspect information will be derived for analysis.\r\nFROM_DEM\u2014The slope and aspect rasters will be calculated from the input surface raster. This is the default.FLAT_SURFACE\u2014Const...",
                        "default": None
                },
                "calculation_directions": {
                        "type": "string",
                        "description": "The number of azimuth directions that will be used when calculating the viewshed.Valid values must be multiples of 8 (8, 16, 24, 32, and so on). The default value is 32 directions, which is adequate f...",
                        "default": None
                },
                "zenith_divisions": {
                        "type": "string",
                        "description": "The number of zenith divisions that will be used to create sky sectors in the sky map.The default is eight divisions (relative to zenith). Values must be greater than zero and less than half the sky s...",
                        "default": None
                },
                "azimuth_divisions": {
                        "type": "string",
                        "description": "The number of azimuth divisions that will be used to create sky sectors in the sky map.The default is eight divisions (relative to north). Valid values must be multiples of 8. Values must be greater t...",
                        "default": None
                },
                "diffuse_model_type": {
                        "type": "string",
                        "description": "Specifies the type of diffuse radiation model that will be used.UNIFORM_SKY\u2014The uniform diffuse model will be used. The incoming diffuse radiation is the same from all sky directions. This is the defa...",
                        "default": None
                },
                "diffuse_proportion": {
                        "type": "string",
                        "description": "The proportion of global normal radiation flux that is diffuse. Values range from 0 to 1.Set this value according to atmospheric conditions. The default value is 0.3 for generally clear sky conditions...",
                        "default": None
                },
                "transmittivity": {
                        "type": "string",
                        "description": "The fraction of radiation that passes through the atmosphere (averaged overall wavelengths). Values range from 0 (no transmission) to 1 (all transmission).The default is 0.5 for a generally clear sky.",
                        "default": None
                },
                "out_direct_radiation_raster": {
                        "type": "string",
                        "description": "The output raster representing the direct incoming solar radiation for each location.\r\nThe output has units of watt hours per square meter (WH/m2).",
                        "default": None
                },
                "out_diffuse_radiation_raster": {
                        "type": "string",
                        "description": "The output raster representing the diffuse incoming solar radiation for each location.The output has units of watt hours per square meter (WH/m2).",
                        "default": None
                },
                "out_direct_duration_raster": {
                        "type": "string",
                        "description": "The output raster representing the duration of direct incoming solar radiation.\r\nThe output has units of hours.",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "feature_solar_radiation": {
        "name": "feature_solar_radiation",
        "description": "Calculates the incoming solar insolation for input points or polygon features relative to the surface (ground) on Earth or the Moon. The input features can represent locations or engineered surfaces by specifying attributes to define size, height, and orientation for analysis relative to the ground. Solar insolation is calculated as the amount of solar radiation energy received during an amount of time for each feature. Values are represented as totals and averages for the area of the feature and have units, kilowatt hours (kWh) and kilowatt hours per square meter (kWh/m2), respectively. Learn more about how Feature Solar Radiation works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input elevation surface raster."
                },
                "in_features": {
                        "type": "string",
                        "description": "The input features (point or polygon) that represent a location or engineered surface to calculate the amount of solar radiation received."
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each feature.It can be an integer or a string field of the input features."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that will contain the summary of the amount of solar radiation received by the input featuresThe format of the table is determined by the output location and path. By default, the out..."
                },
                "start_date_time": {
                        "type": "string",
                        "description": "The start date and time for the analysis."
                },
                "end_date_time": {
                        "type": "string",
                        "description": "The end date and time for the analysis."
                },
                "time_zone": {
                        "type": "string",
                        "description": "The time zone that will be used for the start and end time. The default is coordinated universal time (UTC).UTC\u2014The time zone will be UTC.Dateline_Standard_Time\u2014The time zone will be Dateline Standard...",
                        "default": None
                },
                "adjust_dst": {
                        "type": "string",
                        "description": "Specifies whether the input time configuration will be adjusted for daylight saving time.This parameter is not applicable for analysis on the Moon.NOT_ADJUSTED_FOR_DST\u2014The input time values will not b...",
                        "default": None
                },
                "use_time_interval": {
                        "type": "string",
                        "description": "Specifies whether a single total insolation value will be calculated for the entire time configuration or multiple radiation values will be calculated for the specified interval.NO_INTERVAL\u2014A single r...",
                        "default": None
                },
                "interval_unit": {
                        "type": "string",
                        "description": "Specifies the time unit that will be used for calculating solar radiation values over the entire time configuration.This parameter is only supported when the use_time_interval parameter is set to INTE...",
                        "default": None
                },
                "interval": {
                        "type": "string",
                        "description": "The value of the duration or time between intervals.The default value is dependent on the interval unit specified. The default value for each of the available units are listed below.\r\nMINUTE\u201460HOUR\u20144D...",
                        "default": None
                },
                "feature_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the raster surface for analysis. It must be a positive integer or floating-point value.You can select a field from the input features dataset, or you can prov...",
                        "default": None
                },
                "feature_area": {
                        "type": "string",
                        "description": "The area associated with the input features. It must be a positive integer or floating-point value.You can select a field from the input features dataset, or you can provide a numerical value.For exam...",
                        "default": None
                },
                "feature_slope": {
                        "type": "string",
                        "description": "The relative slope or incline associated with the input features. It must be a positive integer or floating-point value.You can select a field from the input features dataset, or you can provide a num...",
                        "default": None
                },
                "feature_aspect": {
                        "type": "string",
                        "description": "The relative aspect or direction associated with the input features. It must be a positive integer or floating-point value.You can select a field from the input features dataset, or you can provide a ...",
                        "default": None
                },
                "neighborhood_distance": {
                        "type": "string",
                        "description": "The distance from the target cell center for which the output insolation value will be calculated. It determines the size of the neighborhood.The default value is the input surface raster cell size, r...",
                        "default": None
                },
                "use_adaptive_neighborhood": {
                        "type": "string",
                        "description": "Specifies whether neighborhood distance will vary with landscape changes (adaptive). The maximum distance is determined by the neighborhood distance. The minimum distance is the input raster cell size...",
                        "default": None
                },
                "diffuse_model_type": {
                        "type": "string",
                        "description": "Specifies the type of diffuse radiation model that will be used.UNIFORM_SKY\u2014The uniform diffuse model will be used. The incoming diffuse radiation is the same from all sky directions. This is the defa...",
                        "default": None
                },
                "diffuse_proportion": {
                        "type": "string",
                        "description": "The proportion of global normal radiation flux that is diffuse. Values range from 0 to 1.Set this value according to atmospheric conditions. The default value is 0.3 for generally clear sky conditions...",
                        "default": None
                },
                "transmittivity": {
                        "type": "string",
                        "description": "The fraction of radiation that passes through the atmosphere (averaged overall wavelengths). Values range from 0 (no transmission) to 1 (all transmission).The default is 0.5 for a generally clear sky.",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                },
                "out_join_layer": {
                        "type": "string",
                        "description": "The output layer that will be created by joining the output table to the input feature class. This is an optional output.",
                        "default": None
                },
                "sunmap_grid_level": {
                        "type": "string",
                        "description": "The resolution that will be used to generate the H3 hexagonal grid cells used for internal calculations. A lower grid level value creates fewer, larger sun map areas and decreases tool run time. A hig...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster",
                "in_features",
                "unique_id_field",
                "out_table",
                "start_date_time",
                "end_date_time"
        ]
},
    "points_solar_radiation": {
        "name": "points_solar_radiation",
        "description": "Derives incoming solar radiation for specific locations in a point feature class or location table. This tool is deprecated and will be removed in a future release. The Feature Solar Radiation tool provides enhanced functionality or performance.",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input elevation surface raster."
                },
                "in_points_feature_or_table": {
                        "type": "string",
                        "description": "The input point feature class or table containing the locations where solar radiation will be analyzed."
                },
                "out_global_radiation_features": {
                        "type": "string",
                        "description": "The output feature class representing the global radiation or amount of incoming solar insolation (direct + diffuse) calculated for each location.The output has units of watt hours per square meter (W..."
                },
                "height_offset": {
                        "type": "string",
                        "description": "The height (in meters) above the DEM surface for which calculations will be performed.The height offset will be applied to all input locations.",
                        "default": None
                },
                "latitude": {
                        "type": "string",
                        "description": "The latitude for the site area. The units are decimal degrees with positive values for the northern hemisphere and negative values for the southern hemisphere.For input surface rasters containing a sp...",
                        "default": None
                },
                "sky_size": {
                        "type": "string",
                        "description": "The resolution or sky size for the viewshed, sky map, and sun map rasters. The units are cells.The default is a raster of 200 by 200 cells.",
                        "default": None
                },
                "time_configuration": {
                        "type": "string",
                        "description": "Specifies the time configuration (period) that will be used for calculating solar radiation.The Time class objects will be used to specify the time configuration.The different types of time configurat...",
                        "default": None
                },
                "day_interval": {
                        "type": "string",
                        "description": "The time interval through the year (units: days) that will be used to calculate sky sectors for the sun map.The default value is 14 (biweekly).",
                        "default": None
                },
                "hour_interval": {
                        "type": "string",
                        "description": "The time interval through the day (units: hours) that will be used to calculate sky sectors for the sun map.The default value is 0.5.",
                        "default": None
                },
                "each_interval": {
                        "type": "string",
                        "description": "Specifies whether a single total insolation value will be calculated for all locations or multiple values will be calculated for the specified hour and day interval.NOINTERVAL\u2014A single total radiation...",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                },
                "slope_aspect_input_type": {
                        "type": "string",
                        "description": "Specifies how slope and aspect information will be derived for analysis.FROM_DEM\u2014The slope and aspect rasters will be calculated from the input surface raster. This is the default.FLAT_SURFACE\u2014Constan...",
                        "default": None
                },
                "calculation_directions": {
                        "type": "string",
                        "description": "The number of azimuth directions that will be used when calculating the viewshed.Valid values must be multiples of 8 (8, 16, 24, 32, and so on). The default value is 32 directions, which is adequate f...",
                        "default": None
                },
                "zenith_divisions": {
                        "type": "string",
                        "description": "The number of zenith divisions that will be used to create sky sectors in the sky map.The default is eight divisions (relative to zenith). Values must be greater than zero and less than half the sky s...",
                        "default": None
                },
                "azimuth_divisions": {
                        "type": "string",
                        "description": "The number of azimuth divisions that will be used to create sky sectors in the sky map.The default is eight divisions (relative to north). Valid values must be multiples of 8. Values must be greater t...",
                        "default": None
                },
                "diffuse_model_type": {
                        "type": "string",
                        "description": "Specifies the type of diffuse radiation model that will be used.UNIFORM_SKY\u2014The uniform diffuse model will be used. The incoming diffuse radiation is the same from all sky directions. This is the defa...",
                        "default": None
                },
                "diffuse_proportion": {
                        "type": "string",
                        "description": "The proportion of global normal radiation flux that is diffuse. Values range from 0 to 1.Set this value according to atmospheric conditions. The default value is 0.3 for generally clear sky conditions...",
                        "default": None
                },
                "transmittivity": {
                        "type": "string",
                        "description": "The fraction of radiation that passes through the atmosphere (averaged overall wavelengths). Values range from 0 (no transmission) to 1 (all transmission).The default is 0.5 for a generally clear sky.",
                        "default": None
                },
                "out_direct_radiation_features": {
                        "type": "string",
                        "description": "The output feature class representing the direct incoming solar radiation for each location.The output has units of watt hours per square meter (WH/m2).",
                        "default": None
                },
                "out_diffuse_radiation_features": {
                        "type": "string",
                        "description": "The output feature class representing the incoming solar radiation for each location that is diffuse.The output has units of watt hours per square meter (WH/m2).",
                        "default": None
                },
                "out_direct_duration_features": {
                        "type": "string",
                        "description": "The output feature class representing the duration of direct incoming solar radiation.The output has units of hours.",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster",
                "in_points_feature_or_table",
                "out_global_radiation_features"
        ]
},
    "raster_solar_radiation": {
        "name": "raster_solar_radiation",
        "description": "Calculates the incoming solar insolation for every raster cell of a digital surface model for Earth or the Moon. Solar insolation is calculated as the amount of solar radiation energy received per unit area during an amount of time and is measured in units, kilowatt hours per square meter (kWh/m2). Learn more about how Raster Solar Radiation works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input elevation surface raster."
                },
                "start_date_time": {
                        "type": "string",
                        "description": "The start date and time for the analysis."
                },
                "end_date_time": {
                        "type": "string",
                        "description": "The end date and time for the analysis."
                },
                "in_analysis_mask": {
                        "type": "string",
                        "description": "The input data that defines the locations where the analysis will occur.",
                        "default": None
                },
                "in_slope_raster": {
                        "type": "string",
                        "description": "The input slope raster that will be used when calculating the output solar radiation.If this input is not specified, the tool will calculate slope values internally from the input surface raster. Prov...",
                        "default": None
                },
                "in_aspect_raster": {
                        "type": "string",
                        "description": "The input aspect raster that will be used when calculating the output solar radiation.If this input is not specified, the tool will calculate aspect values internally from the input surface raster. Pr...",
                        "default": None
                },
                "out_direct_radiation_raster": {
                        "type": "string",
                        "description": "The output raster representing the direct incoming solar radiation value for each location.The output has units of kilowatt hours per square meter (kWh/m2).",
                        "default": None
                },
                "out_diffuse_radiation_raster": {
                        "type": "string",
                        "description": "The output raster representing the incoming solar radiation that is diffused by the sky, layers of atmosphere, and other surroundings.The output has units of kilowatt hours per square meter (kWh/m2).",
                        "default": None
                },
                "out_duration_raster": {
                        "type": "string",
                        "description": "The output raster representing the duration of direct incoming solar radiation.The output has units of hours.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "The time zone that will be used for the start and end time. The default is coordinated universal time (UTC).UTC\u2014The time zone will be UTC.Dateline_Standard_Time\u2014The time zone will be Dateline Standard...",
                        "default": None
                },
                "adjust_dst": {
                        "type": "string",
                        "description": "Specifies whether the input time configuration will be adjusted for daylight saving time.This parameter is not applicable for analysis on the Moon.NOT_ADJUSTED_FOR_DST\u2014The input time values will not b...",
                        "default": None
                },
                "use_time_interval": {
                        "type": "string",
                        "description": "Specifies whether a single total insolation value will be calculated for the entire time configuration or multiple radiation values will be calculated for the specified interval.NO_INTERVAL\u2014A single r...",
                        "default": None
                },
                "interval_unit": {
                        "type": "string",
                        "description": "Specifies the time unit that will be used for calculating solar radiation values over the entire time configuration.This parameter is only supported when the use_time_interval parameter is set to INTE...",
                        "default": None
                },
                "interval": {
                        "type": "string",
                        "description": "The value of the duration or time between intervals.The default value is dependent on the interval unit specified. The default value for each of the available units are listed below.\r\nMINUTE\u201460HOUR\u20144D...",
                        "default": None
                },
                "neighborhood_distance": {
                        "type": "string",
                        "description": "The distance from the target cell center for which the output insolation value will be calculated. It determines the size of the neighborhood.The default value is the input surface raster cell size, r...",
                        "default": None
                },
                "use_adaptive_neighborhood": {
                        "type": "string",
                        "description": "Specifies whether neighborhood distance will vary with landscape changes (adaptive). The maximum distance is determined by the neighborhood distance. The minimum distance is the input raster cell size...",
                        "default": None
                },
                "diffuse_model_type": {
                        "type": "string",
                        "description": "Specifies the type of diffuse radiation model that will be used.UNIFORM_SKY\u2014The uniform diffuse model will be used. The incoming diffuse radiation is the same from all sky directions. This is the defa...",
                        "default": None
                },
                "diffuse_proportion": {
                        "type": "string",
                        "description": "The proportion of global normal radiation flux that is diffuse. Values range from 0 to 1.Set this value according to atmospheric conditions. The default value is 0.3 for generally clear sky conditions...",
                        "default": None
                },
                "transmittivity": {
                        "type": "string",
                        "description": "The fraction of radiation that passes through the atmosphere (averaged overall wavelengths). Values range from 0 (no transmission) to 1 (all transmission).The default is 0.5 for a generally clear sky.",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                },
                "sunmap_grid_level": {
                        "type": "string",
                        "description": "The resolution that will be used to generate the H3 hexagonal grid cells used for internal calculations. A lower grid level value creates fewer, larger sun map areas and decreases tool run time. A hig...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster",
                "start_date_time",
                "end_date_time"
        ]
},
    "solar_radiation_graphics": {
        "name": "solar_radiation_graphics",
        "description": "Derives raster representations of a hemispherical viewshed, sun map, and sky map, which are used in the calculation of direct, diffuse, and global solar radiation. This tool is deprecated and will be removed in a future release. The Raster Solar Radiation tool provides enhanced functionality or performance.",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input elevation surface raster."
                },
                "in_points_feature_or_table": {
                        "type": "string",
                        "description": "The input point feature class or table containing the locations where solar radiation will be analyzed.",
                        "default": None
                },
                "sky_size": {
                        "type": "string",
                        "description": "The resolution or sky size for the viewshed, sky map, and sun map rasters. The units are cells.The default is a raster of 200 by 200 cells.",
                        "default": None
                },
                "height_offset": {
                        "type": "string",
                        "description": "The height (in meters) above the DEM surface for which calculations will be performed.The height offset will be applied to all input locations.",
                        "default": None
                },
                "calculation_directions": {
                        "type": "string",
                        "description": "The number of azimuth directions that will be used when calculating the viewshed.Valid values must be multiples of 8 (8, 16, 24, 32, and so on). The default value is 32 directions, which is adequate f...",
                        "default": None
                },
                "latitude": {
                        "type": "string",
                        "description": "The latitude for the site area. The units are decimal degrees with positive values for the northern hemisphere and negative values for the southern hemisphere.For input surface rasters containing a sp...",
                        "default": None
                },
                "time_configuration": {
                        "type": "string",
                        "description": "Specifies the time configuration (period) that will be used for calculating solar radiation.The Time class objects will be used to specify the time configuration.The different types of time configurat...",
                        "default": None
                },
                "day_interval": {
                        "type": "string",
                        "description": "The time interval through the year (units: days) that will be used to calculate sky sectors for the sun map.The default value is 14 (biweekly).",
                        "default": None
                },
                "hour_interval": {
                        "type": "string",
                        "description": "The time interval through the day (units: hours) that will be used to calculate sky sectors for the sun map.The default value is 0.5.",
                        "default": None
                },
                "out_sunmap_raster": {
                        "type": "string",
                        "description": "The output sun map raster.The output is a representation that specifies sun tracks, the apparent position of the sun as it varies through time. The output is at the same resolution as the viewshed and...",
                        "default": None
                },
                "zenith_divisions": {
                        "type": "string",
                        "description": "The number of zenith divisions that will be used to create sky sectors in the sky map.The default is eight divisions (relative to zenith). Values must be greater than zero and less than half the sky s...",
                        "default": None
                },
                "azimuth_divisions": {
                        "type": "string",
                        "description": "The number of azimuth divisions that will be used to create sky sectors in the sky map.The default is eight divisions (relative to north). Valid values must be multiples of 8. Values must be greater t...",
                        "default": None
                },
                "out_skymap_raster": {
                        "type": "string",
                        "description": "The output sky map raster.The output is constructed by dividing the whole sky into a series of sky sectors defined by zenith and azimuth divisions. The output is at the same resolution as the viewshed...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "add_surface_information": {
        "name": "add_surface_information",
        "description": "Attributes input features with height-based statistical information derived from the overlapping portions of a surface.",
        "parameters": {
                "in_feature_class": {
                        "type": "string",
                        "description": "The point, multipoint, polyline, or polygon features that define the locations for determining one or more surface properties."
                },
                "in_surface": {
                        "type": "string",
                        "description": "The LAS dataset, mosaic, raster,  terrain, or TIN surface used for interpolating z-values."
                },
                "out_property": {
                        "type": "string",
                        "description": "Specifies the surface elevation properties that will be added to the attribute table of the input feature class.Z\u2014The surface z-values interpolated for the x,y-location of each single-point feature wi..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the interpolation method that will be used to determine information about the surface.BILINEAR\u2014An interpolation method  exclusive to the raster surface that determines cell values from the f...",
                        "default": None
                },
                "sample_distance": {
                        "type": "string",
                        "description": "The spacing at which z-values will be interpolated. By default, the raster cell size is used when the input surface is a raster, and the natural densification of the triangulated surface is used when ...",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": None
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": None
                },
                "noise_filtering": {
                        "type": "string",
                        "description": "Defines whether portions of the surface that are potentially characterized by anomalous measurements will be excluded from contributing to slope calculations. Other properties are not affected by this...",
                        "default": None
                }
        },
        "required": [
                "in_feature_class",
                "in_surface",
                "out_property"
        ]
},
    "aspect": {
        "name": "aspect",
        "description": "Derives the aspect from each cell of a raster surface. The aspect identifies the compass direction that the downhill slope faces for each location. The Surface Parameters tool provides a newer implementation and enhanced functionality. Learn more about how Aspect works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the calculation will be based on a planar (flat earth) or a geodesic (ellipsoid) method.PLANAR\u2014The calculation will be performed on a projected flat plane using a 2D Cartesian coordi...",
                        "default": None
                },
                "z_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for vertical z-values.It is defined by a vertical coordinate system if it exists. If no vertical coordinate system exists, define the z-unit using the unit ...",
                        "default": None
                },
                "project_geodesic_azimuths": {
                        "type": "string",
                        "description": "Specifies whether geodesic azimuths will be projected to correct the angle distortion caused by the output spatial reference.\r\nGEODESIC_AZIMUTHS\u2014Geodesic azimuths will not be projected. This is the de...",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "contour": {
        "name": "contour",
        "description": "Creates a feature class of contours from a raster surface. Learn more about how Contouring works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_polyline_features": {
                        "type": "string",
                        "description": "The output contour features."
                },
                "contour_interval": {
                        "type": "string",
                        "description": "The interval, or distance, between contour lines.This can be any positive number."
                },
                "base_contour": {
                        "type": "string",
                        "description": "The base contour value.Contours are generated above and below this value as needed to cover the entire value range of the input raster. The default is zero.",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The unit conversion factor used when generating contours. The default value is 1.The contour lines are generated based on the z-values in the input raster, which are often measured in units of meters ...",
                        "default": None
                },
                "contour_type": {
                        "type": "string",
                        "description": "Specifies the type of output. The output can represent the contours as either lines or polygons. There are several options for polygons.\r\n\r\nCONTOUR\u2014A polyline feature class of contours (isolines). Thi...",
                        "default": None
                },
                "max_vertices_per_feature": {
                        "type": "string",
                        "description": "The vertex limit when subdividing a feature. This should only be used when output features contain a very large number of vertices (many millions). This parameter is intended as a way to subdivide ext...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_polyline_features",
                "contour_interval"
        ]
},
    "contour_list": {
        "name": "contour_list",
        "description": "Creates a feature class of selected contour values from a raster surface. Learn more about how Contouring works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_polyline_features": {
                        "type": "string",
                        "description": "The output contour polyline features."
                },
                "contour_valuescontour_value": {
                        "type": "string",
                        "description": "List of z-values for which to create contours."
                }
        },
        "required": [
                "in_raster",
                "out_polyline_features",
                "contour_valuescontour_value"
        ]
},
    "contour_with_barriers": {
        "name": "contour_with_barriers",
        "description": "Creates contours from a raster surface. The inclusion of barrier features allows you to independently generate contours on either side of a barrier.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_contour_feature_class": {
                        "type": "string",
                        "description": "The output contour features."
                },
                "in_barrier_features": {
                        "type": "string",
                        "description": "The input barrier features.The features can be polyline or polygon type.",
                        "default": None
                },
                "in_contour_type": {
                        "type": "string",
                        "description": "The type of contour to create.POLYLINES\u2014 The contour or isoline representation of the input raster.POLYGONS\u2014 Closed polygons representing the contours.\r\nNote:The current version of this tool only supp...",
                        "default": None
                },
                "in_contour_values_file": {
                        "type": "string",
                        "description": "The base contour, contour interval, indexed contour interval, and explicit contour values can also be specified via a text file.",
                        "default": None
                },
                "explicit_only": {
                        "type": "string",
                        "description": "Only explicit contour values are used. Base contour, contour interval, and indexed contour intervals are not specified.NO_EXPLICIT_VALUES_ONLY\u2014 The default, contour interval must be specified.EXPLICIT...",
                        "default": None
                },
                "in_base_contour": {
                        "type": "string",
                        "description": "The base contour value.Contours are generated above and below this value as needed to cover the entire value range of the input raster. The default is zero.",
                        "default": None
                },
                "in_contour_interval": {
                        "type": "string",
                        "description": "The interval, or distance, between contour lines.This can be any positive number.",
                        "default": None
                },
                "in_indexed_contour_interval": {
                        "type": "string",
                        "description": "Contours will also be generated for this interval and will be flagged accordingly in the output feature class.",
                        "default": None
                },
                "in_contour_listin_explicit_contour": {
                        "type": "string",
                        "description": "Explicit values at which to create contours.",
                        "default": None
                },
                "in_z_factor": {
                        "type": "string",
                        "description": "The unit conversion factor used when generating contours. The default value is 1.The contour lines are generated based on the z-values in the input raster, which are often measured in units of meters ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_contour_feature_class"
        ]
},
    "curvature": {
        "name": "curvature",
        "description": "Calculates the curvature of a raster surface and, optionally, includes profile and plan curvature. The Surface Parameters tool provides a newer implementation and enhanced functionality. Learn more about how Curvature works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                },
                "out_profile_curve_raster": {
                        "type": "string",
                        "description": "Output profile curve raster dataset.This is the curvature of the surface in the direction of slope.It will be floating-point type.",
                        "default": None
                },
                "out_plan_curve_raster": {
                        "type": "string",
                        "description": "Output plan curve raster dataset.This is the curvature of the surface perpendicular to the slope direction.It will be floating-point type.",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "cut_fill": {
        "name": "cut_fill",
        "description": "Calculates the volume change between two surfaces. This is typically used for cut and fill operations. Learn more about how Cut Fill works",
        "parameters": {
                "in_before_surface": {
                        "type": "string",
                        "description": "The input representing the surface before the cut or fill operation."
                },
                "in_after_surface": {
                        "type": "string",
                        "description": "The input representing the surface after the cut or fill operation."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                }
        },
        "required": [
                "in_before_surface",
                "in_after_surface"
        ]
},
    "feature_preserving_smoothing": {
        "name": "feature_preserving_smoothing",
        "description": "Smooths a surface raster by removing noise while preserving features. Learn more about how Feature Preserving Smoothing works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance unit that will be used for the Neighborhood Distance parameter. The default is CELLS.\r\nCELLS\u2014The distance unit will be cells.METERS\u2014The distance unit will be meters.CENTIMETERS\u2014...",
                        "default": None
                },
                "neighborhood_distance": {
                        "type": "string",
                        "description": "The distance away from the target cell that defines the size of the processing neighborhood.The value must be a positive number. The default value is 5 cells.",
                        "default": None
                },
                "normal_difference_threshold": {
                        "type": "string",
                        "description": "The maximum normal difference for a neighboring cell to be included in computing a new cell value for the current processing cell. A normal difference is an angle formed by the normal vector of a neig...",
                        "default": None
                },
                "number_iterations": {
                        "type": "string",
                        "description": "The number of times that the smoothing process will be repeated.The value must be a positive integer. The default value is 3.",
                        "default": None
                },
                "maximum_elevation_change": {
                        "type": "string",
                        "description": "The allowed maximum height change of any cell in one iteration.When a new value is calculated for a cell location, it is compared to the original value at that cell location. If the difference is less...",
                        "default": None
                },
                "z_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for vertical z-values.It is defined by a vertical coordinate system if it exists. If no vertical coordinate system exists, define the z-unit using the unit ...",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "geodesic_viewshed": {
        "name": "geodesic_viewshed",
        "description": "Determines the raster surface locations visible to a set of observer features using geodesic methods. Learn more about how the Geodesic Viewshed tool works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster. It can be an integer or a floating-point raster.The input raster is transformed into a 3D geocentric coordinate system during the visibility calculation. NoData cells on the ..."
                },
                "in_observer_features": {
                        "type": "string",
                        "description": "The input feature class that identifies the observer locations. It can be point, multipoint, or polyline features.The input feature class is transformed into a 3D geocentric coordinate system during t..."
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above ground level (AGL) raster.The AGL result is a raster in which each cell value is the minimum height that must be added to a cell that is not visible to make it visible by at least one...",
                        "default": None
                },
                "analysis_type": {
                        "type": "string",
                        "description": "Specifies the type of visibility analysis that will be performed, either determining how visible each cell is to the observers or identifying the observers that are visible for each surface location.F...",
                        "default": None
                },
                "vertical_error": {
                        "type": "string",
                        "description": "The amount of uncertainty (the root mean square [RMS] error) in the surface elevation values. It is a floating-point value representing the expected error of the input elevation values. When this para...",
                        "default": None
                },
                "out_observer_region_relationship_table": {
                        "type": "string",
                        "description": "The output table for identifying the regions that are visible to each observer. This table can be related to the input observer feature class and the output visibility raster for identifying the regio...",
                        "default": None
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": None
                },
                "surface_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the z-value of each cell as it is considered for visibility. It must be a positive integer or floating-point value.You can select a field in the input observe...",
                        "default": None
                },
                "observer_elevation": {
                        "type": "string",
                        "description": "The surface elevations of the observer points or vertices.You can select a field in the input observers dataset, or you can specify a numerical value.When this parameter is not specified, the observer...",
                        "default": None
                },
                "observer_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the observer elevation. It must be a positive integer or floating-point value.You can select a field in the input observers dataset, or you can specify a nume...",
                        "default": None
                },
                "inner_radius": {
                        "type": "string",
                        "description": "The start distance from which visibility will be determined. Cells closer than this distance will not be visible in the output but can still block visibility of the cells between inner radius and oute...",
                        "default": None
                },
                "inner_radius_is_3d": {
                        "type": "string",
                        "description": "Specifies the type of distance that will be used for the inner radius parameter.GROUND\u2014The inner radius will be interpreted as a 2D distance. This is the default.3D\u2014The inner radius will be interprete...",
                        "default": None
                },
                "outer_radius": {
                        "type": "string",
                        "description": "The maximum distance from which visibility will be determined. Cells beyond this distance will be excluded from the analysis.You can select a field in the input observers dataset, or you can specify a...",
                        "default": None
                },
                "outer_radius_is_3d": {
                        "type": "string",
                        "description": "Specifies the type of distance that will be used for the outer radius parameter.GROUND\u2014The outer radius will be interpreted as a 2D distance. This is the default.3D\u2014The outer radius will be interprete...",
                        "default": None
                },
                "horizontal_start_angle": {
                        "type": "string",
                        "description": "The start angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 0.You can select a f...",
                        "default": None
                },
                "horizontal_end_angle": {
                        "type": "string",
                        "description": "The end angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 360.You can select a f...",
                        "default": None
                },
                "vertical_upper_angle": {
                        "type": "string",
                        "description": "The upper vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from above -90 up to and including 90. The value can be integer or floating point. The default...",
                        "default": None
                },
                "vertical_lower_angle": {
                        "type": "string",
                        "description": "The lower vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from -90 up to but not including 90. The value can be integer or floating point. The default v...",
                        "default": None
                },
                "analysis_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to calculate visibility. This parameter allows you to decide on performance level.ALL_SIGHTLINES\u2014A sightline will be run to every cell on the raster to establish...",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_observer_features"
        ]
},
    "geomorphon_landforms": {
        "name": "geomorphon_landforms",
        "description": "Calculates the geomorphon pattern of each cell of an input surface raster and classifies calculated geomorphons into common landform types. Learn more about how Geomorphon Landforms works",
        "parameters": {
                "in_surface_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_geomorphons_raster": {
                        "type": "string",
                        "description": "Each geomorphon pattern will be assigned a unique identifier, which is stored for each cell in the output geomorphons raster.The output is of integer type.",
                        "default": None
                },
                "angle_threshold": {
                        "type": "string",
                        "description": "The angle threshold (in degrees) below which the target cell will be classified as flat.The default value is 1 degree. Specifying a larger value than the default is recommended for low resolution DEMs...",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance unit that will be used for the search_distance and skip_distance parameters.Distance will be measured in the specified unit or number of cells. The default is CELLS.CELLS\u2014The di...",
                        "default": None
                },
                "search_distance": {
                        "type": "string",
                        "description": "The distance away from the target cell that defines the radius of the area that will be used to identify the geomorphon pattern.The default value is 10. Use a search distance value that matches the ty...",
                        "default": None
                },
                "skip_distance": {
                        "type": "string",
                        "description": "The distance away from the target cell where the analysis area starts. Neighboring cells that fall within this distance will be skipped and won't contribute to identification of the geomorphon pattern...",
                        "default": None
                },
                "z_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for vertical z-values.It is defined by a vertical coordinate system if it exists. If no vertical coordinate system exists, define the z-unit using the unit ...",
                        "default": None
                }
        },
        "required": [
                "in_surface_raster"
        ]
},
    "hillshade": {
        "name": "hillshade",
        "description": "Creates a shaded relief from a surface raster by considering the illumination source angle and shadows. Learn more about how Hillshade works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "azimuth": {
                        "type": "string",
                        "description": "Azimuth angle of the light source.The azimuth is expressed in positive degrees from 0 to 360, measured clockwise from north.The default is 315 degrees.",
                        "default": None
                },
                "altitude": {
                        "type": "string",
                        "description": "Altitude angle of the light source above the horizon.The altitude is expressed in positive degrees, with 0 degrees at the horizon and 90 degrees directly overhead.The default is 45 degrees.",
                        "default": None
                },
                "model_shadows": {
                        "type": "string",
                        "description": "Type of shaded relief to be generated.NO_SHADOWS\u2014The output raster only considers local illumination angles; the effects of shadows are not considered.The output values can range from 0 to 255, with 0...",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "interpolate_shape": {
        "name": "interpolate_shape",
        "description": "Creates 3D features by interpolating z-values from a surface. Learn more about how Interpolate Shape works",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The surface that will be used for interpolating z-values."
                },
                "in_feature_class": {
                        "type": "string",
                        "description": "The input features that will be processed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "sample_distance": {
                        "type": "string",
                        "description": "The spacing at which z-values will be interpolated. By default, this is a raster dataset's cell size or a triangulated surface's natural densification.",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the interpolation method that will be used to determine elevation values for the output features. The available options depend on the surface type.\r\nBILINEAR\u2014The value of the query point wil...",
                        "default": None
                },
                "vertices_only": {
                        "type": "string",
                        "description": "Specifies whether the interpolation will only occur along the vertices of an input feature, ignoring the sample distance option.DENSIFY\u2014Interpolation will occur using the sampling distance. This is th...",
                        "default": None
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": None
                },
                "preserve_features": {
                        "type": "string",
                        "description": "Specifies whether features with one or more vertices that fall outside the raster's data area will be retained in the output. This parameter is only available when the input surface is a raster and th...",
                        "default": None
                }
        },
        "required": [
                "in_surface",
                "in_feature_class",
                "out_feature_class"
        ]
},
    "multiscale_surface_deviation": {
        "name": "multiscale_surface_deviation",
        "description": "Calculates the maximum deviation from the mean value across a range of spatial scales. Learn more about how Multiscale Surface Deviation works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_scale_raster": {
                        "type": "string",
                        "description": "The output raster containing the scale at which the maximum deviation was found for each cell. Scales are represented as their neighborhood distance values.It will be floating-point type.",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance unit that will be used for the min_scale, max_scale, and base_increment parameters.Distance will be measured in the number of cells or specified unit. The default is the map uni...",
                        "default": None
                },
                "min_scale": {
                        "type": "string",
                        "description": "The distance that defines the minimum neighborhood scale that elevation difference will be calculated for. This is the distance from the target cell center, creating a square of cells around the targe...",
                        "default": None
                },
                "max_scale": {
                        "type": "string",
                        "description": "The distance that defines the maximum neighborhood scale that elevation difference will be calculated for. This is the distance from the target cell center, creating a square of cells around the targe...",
                        "default": None
                },
                "base_increment": {
                        "type": "string",
                        "description": "The increase in neighborhood distance between scales.\r\nThis parameter value cannot be less than the in_raster cell size or 1 cell.The default value is the cell size of the in_raster parameter value.",
                        "default": None
                },
                "nonlinearity": {
                        "type": "string",
                        "description": "The factor that can introduce nonlinearity into the scale increase at each increment. This causes the increment between scales to increase instead of remaining constant. Generally, values between 1.0 ...",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "multiscale_surface_difference": {
        "name": "multiscale_surface_difference",
        "description": "Calculates the maximum difference from the mean elevation across a range of spatial scales. Learn more about how Multiscale Surface Difference works.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_scale_raster": {
                        "type": "string",
                        "description": "The output raster containing the scale at which the most extreme difference was found for each cell. Scales are represented as their neighborhood distance values.It will be floating-point type.",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance unit that will be used for the min_scale, max_scale, and increment parameters.Distance will be measured in the number of cells or specified unit. The default is the map unit of ...",
                        "default": None
                },
                "min_scale": {
                        "type": "string",
                        "description": "The distance that defines the minimum neighborhood scale that elevation difference will be calculated for. This is the distance from the target cell center, creating a square of cells around the targe...",
                        "default": None
                },
                "max_scale": {
                        "type": "string",
                        "description": "The distance that defines the maximum neighborhood scale that elevation difference will be calculated for. This is the distance from the target cell center, creating a square of cells around the targe...",
                        "default": None
                },
                "increment": {
                        "type": "string",
                        "description": "The increase in neighborhood distance between scales.\r\nThis parameter value cannot be less than the in_raster cell size or 1 cell.The default value is the cell size of the in_raster parameter value.",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "multiscale_surface_percentile": {
        "name": "multiscale_surface_percentile",
        "description": "Calculates the most extreme percentile across a range of spatial scales. Learn more about how Multiscale Surface Percentile works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "out_scale_raster": {
                        "type": "string",
                        "description": "The output raster containing the scale at which the most extreme percentile was found for each cell. Scales are represented as their neighborhood distance values.It will be floating-point type.",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance unit that will be used for the min_scale, max_scale, and base_increment parameters.Distance will be measured in the number of cells or specified unit. The default is the map uni...",
                        "default": None
                },
                "min_scale": {
                        "type": "string",
                        "description": "The distance that defines the minimum neighborhood scale that elevation percentile will be calculated for. This is the distance from the target cell center, creating a square of cells around the targe...",
                        "default": None
                },
                "max_scale": {
                        "type": "string",
                        "description": "The distance that defines the maximum neighborhood scale that elevation percentile will be calculated for. This is the distance from the target cell center, creating a square of cells around the targe...",
                        "default": None
                },
                "base_increment": {
                        "type": "string",
                        "description": "The initial increase in neighborhood distance between scales.This parameter cannot be less than the in_raster cell size or 1 cell.The default value is the cell size of the in_raster parameter value.",
                        "default": None
                },
                "nonlinearity": {
                        "type": "string",
                        "description": "The factor that can introduce nonlinearity into the scale increase at each increment. This causes the increment between scales to increase instead of remaining constant. Generally, values between 1.0 ...",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "observer_points": {
        "name": "observer_points",
        "description": "Identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Observer Points works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_observer_point_features": {
                        "type": "string",
                        "description": "The point feature class that identifies the observer locations.The maximum number of points allowed is 16."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                },
                "curvature_correction": {
                        "type": "string",
                        "description": "Specifies whether correction for the earth's curvature will be applied.FLAT_EARTH\u2014No curvature correction will be applied. This is the default.CURVED_EARTH\u2014Curvature correction will be applied.",
                        "default": None
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": None
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above ground level (AGL) raster.The AGL result is a raster where each cell value is the minimum height that must be added to an otherwise nonvisible cell to make it visible by at least one ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_observer_point_features"
        ]
},
    "slope": {
        "name": "slope",
        "description": "Identifies the slope (gradient or steepness) from each cell of a raster. The Surface Parameters tool provides a newer implementation and enhanced functionality. Learn more about how Slope works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "output_measurement": {
                        "type": "string",
                        "description": "Specifies the measurement units (degrees or percentages) of the output slope raster.DEGREE\u2014The inclination of slope will be calculated in degrees.PERCENT_RISE\u2014The inclination of slope will be calculat...",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the calculation will be based on a planar (flat earth) or a geodesic (ellipsoid) method.PLANAR\u2014The calculation will be performed on a projected flat plane using a 2D Cartesian coordi...",
                        "default": None
                },
                "z_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for vertical z-values.It is defined by a vertical coordinate system if it exists. If no vertical coordinate system exists, define the z-unit using the unit ...",
                        "default": None
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "surface_parameters": {
        "name": "surface_parameters",
        "description": "Determines parameters of a raster surface such as aspect, slope, and curvatures. Learn more about how Surface Parameters works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "parameter_type": {
                        "type": "string",
                        "description": "Specifies the output surface parameter type that will be computed.SLOPE\u2014The rate of change in elevation will be computed. This is the default.ASPECT\u2014The downslope direction of the maximum rate of chan...",
                        "default": None
                },
                "local_surface_type": {
                        "type": "string",
                        "description": "Specifies the type of surface function that will be fitted around the target cell.QUADRATIC\u2014A quadratic surface function will be fitted to the neighborhood cells. This is the default.BIQUADRATIC\u2014A biq...",
                        "default": None
                },
                "neighborhood_distance": {
                        "type": "string",
                        "description": "The output will be calculated over this distance from the target cell center. It determines the neighborhood size.The default value is the input raster cell size, resulting in a 3 by 3 neighborhood.",
                        "default": None
                },
                "use_adaptive_neighborhood": {
                        "type": "string",
                        "description": "Specifies whether neighborhood distance will vary with landscape changes (adaptive). The maximum distance is determined by the neighborhood distance. The minimum distance is the input raster cell size...",
                        "default": None
                },
                "z_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for vertical z-values.It is defined by a vertical coordinate system if it exists. If no vertical coordinate system exists, define the z-unit using the unit ...",
                        "default": None
                },
                "output_slope_measurement": {
                        "type": "string",
                        "description": "The measurement units (degrees or percentages) that will be used for the output slope raster.DEGREE\u2014The inclination of slope will be calculated in degrees.PERCENT_RISE\u2014The inclination of slope will be...",
                        "default": None
                },
                "project_geodesic_azimuths": {
                        "type": "string",
                        "description": "Specifies whether geodesic azimuths will be projected to correct the angle distortion caused by the output spatial reference.\r\nGEODESIC_AZIMUTHS\u2014Geodesic azimuths will not be projected. This is the de...",
                        "default": None
                },
                "use_equatorial_aspect": {
                        "type": "string",
                        "description": "Specifies whether aspect will be measured from a point on the equator or from the north pole.\r\nNORTH_POLE_ASPECT\u2014Aspect will be measured from the north pole. This is the default.EQUATORIAL_ASPECT\u2014Aspe...",
                        "default": None
                },
                "in_analysis_mask": {
                        "type": "string",
                        "description": "The input data defining the locations where the analysis will occur.It can be a raster or feature dataset. If the input is a raster, it can be integer or floating-point type. If the input is feature d...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "viewshed": {
        "name": "viewshed",
        "description": "Determines the raster surface locations visible to a set of observer features. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Viewshed works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_observer_features": {
                        "type": "string",
                        "description": "The feature class that identifies the observer locations.The input can be point or polyline features."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": None
                },
                "curvature_correction": {
                        "type": "string",
                        "description": "Specifies whether correction for the earth's curvature will be applied.FLAT_EARTH\u2014No curvature correction will be applied. This is the default.CURVED_EARTH\u2014Curvature correction will be applied.",
                        "default": None
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": None
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above ground level (AGL) raster.The AGL result is a raster where each cell value is the minimum height that must be added to an otherwise nonvisible cell to make it visible by at least one ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_observer_features"
        ]
},
    "visibility": {
        "name": "visibility",
        "description": "Determines the raster surface locations visible to a set of observer features, or identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_observer_features": {
                        "type": "string",
                        "description": "The feature class that identifies the observer locations.The input can be point or polyline features."
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above-ground-level (AGL) raster.The AGL result is a raster where each cell value is the minimum height that must be added to an otherwise nonvisible cell to make it visible by at least one ...",
                        "default": None
                },
                "analysis_type": {
                        "type": "string",
                        "description": "The visibility analysis type.FREQUENCY\u2014The output records the number of times that each cell location in the input surface raster can be seen by the input observation locations (as points, or as verti...",
                        "default": None
                },
                "nonvisible_cell_value": {
                        "type": "string",
                        "description": "Value assigned to non-visible cells.ZERO\u20140 is assigned to nonvisible cells. This is the default.NODATA\u2014NoData is assigned to nonvisible cells.",
                        "default": None
                },
                "z_factor": {
                        "type": "string",
                        "description": "Number of ground x,y units in one surface z unit.The z-factor adjusts the units of measure for the z units when they are different from the x,y units of the input surface. The z-values of the input su...",
                        "default": None
                },
                "curvature_correction": {
                        "type": "string",
                        "description": "Specifies whether correction for the earth's curvature will be applied.FLAT_EARTH\u2014No curvature correction will be applied. This is the default.CURVED_EARTH\u2014Curvature correction will be applied.",
                        "default": None
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": None
                },
                "surface_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the z-value of each cell as it is considered for visibility. It must be a positive integer or floating-point value.You can select a field in the input observe...",
                        "default": None
                },
                "observer_elevation": {
                        "type": "string",
                        "description": "The surface elevations of the observer points or vertices.You can select a field in the input observers dataset, or you can specify a numerical value.By default, a numerical field SPOT is used if it e...",
                        "default": None
                },
                "observer_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the observer elevation. It must be a positive integer or floating-point value.You can select a field in the input observers dataset, or you can specify a nume...",
                        "default": None
                },
                "inner_radius": {
                        "type": "string",
                        "description": "The start distance from which visibility will be determined. Cells closer than this distance will not be visible in the output but can still block visibility of the cells between inner radius and oute...",
                        "default": None
                },
                "outer_radius": {
                        "type": "string",
                        "description": "The maximum distance from which visibility will be determined. Cells beyond this distance will be excluded from the analysis.It can be a positive or negative integer or floating point value. If it is ...",
                        "default": None
                },
                "horizontal_start_angle": {
                        "type": "string",
                        "description": "The start angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 0.You can select a f...",
                        "default": None
                },
                "horizontal_end_angle": {
                        "type": "string",
                        "description": "The end angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 360.You can select a f...",
                        "default": None
                },
                "vertical_upper_angle": {
                        "type": "string",
                        "description": "The upper vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from above -90 up to and including 90. The value can be integer or floating point. The default...",
                        "default": None
                },
                "vertical_lower_angle": {
                        "type": "string",
                        "description": "The lower vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from -90 up to but not including 90. The value can be integer or floating point. The default v...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_observer_features"
        ]
},
    "tabulate_area": {
        "name": "tabulate_area",
        "description": "Calculates cross-tabulated areas between two datasets and outputs a table.",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset."
                },
                "in_class_data": {
                        "type": "string",
                        "description": "The dataset that defines the classes that will have their area summarized within each zone.The class input can be an integer raster layer or a feature layer."
                },
                "class_field": {
                        "type": "string",
                        "description": "The field that holds the class values.It can be an integer or a string field of the input class data."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that will contain the summary of the area of each class in each zone.The format of the table is determined by the output location and path. By default, the output will be a geodatabas..."
                },
                "processing_cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                },
                "classes_as_rows": {
                        "type": "string",
                        "description": "Specifies how the values from the input class raster will be represented in the output table.CLASSES_AS_FIELDS\u2014Classes will be represented as fields. This is the default.CLASSES_AS_ROWS\u2014Classes will b...",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "in_class_data",
                "class_field",
                "out_table"
        ]
},
    "zonal_characterization": {
        "name": "zonal_characterization",
        "description": "Summarizes the values of multiple rasters within the zones of another dataset and reports the results as a table. Learn more about how zonal statistics tools work",
        "parameters": {
                "in_zone_raster_or_features": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "out_statistics_table": {
                        "type": "string",
                        "description": "The output table that will contain the summary of the values in each zone for all value rasters.The format of the table is determined by the output location and path. By default, the output will be a ..."
                },
                "out_statistics_features": {
                        "type": "string",
                        "description": "The output feature class that will be created by joining the output table to the input zone data.",
                        "default": None
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset.",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values in the value input will be ignored in the results of the zone that they fall within.DATA\u2014Within any particular zone, only cells that have a value in the input value ras...",
                        "default": None
                },
                "percentile_values": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the percentile value falls between two cell values from the input value raster.AUTO_DETECT\u2014If the input value raster is of integer pixel ty...",
                        "default": None
                },
                "circular_calculation": {
                        "type": "string",
                        "description": "Specifies how the input raster will be processed for circular data.ARITHMETIC\u2014Ordinary linear statistics will be calculated. This is the default. CIRCULAR\u2014The statistics for angles or other cyclic qua...",
                        "default": None
                },
                "circular_wrap_value": {
                        "type": "string",
                        "description": "The value that will be used to round a linear value to the range of a given circular statistic. Its value must be a positive integer or a floating-point value. The default value is 360 degrees.This pa...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be calculated if they are multidimensional.\r\nCURRENT_SLICE\u2014Statistics will be calculated from the current slice of the input multidimensional dataset. This is the ...",
                        "default": None
                },
                "add_zone_attributes": {
                        "type": "string",
                        "description": "Specifies whether any of the additional zone attributes from the input zones will be appended to the output feature class.\r\nZONE_FIELD_ONLY\u2014Only the zone ID field from the input zones will be appended...",
                        "default": None
                }
        },
        "required": [
                "in_zone_raster_or_features",
                "out_statistics_table"
        ]
},
    "zonal_fill": {
        "name": "zonal_fill",
        "description": "Fills zones using the minimum cell value from a weight raster along the zone boundary.",
        "parameters": {
                "in_zone_raster": {
                        "type": "string",
                        "description": "The input raster that defines the zones to be filled."
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "The weight, or value, to be assigned to each zone."
                }
        },
        "required": [
                "in_zone_raster",
                "in_weight_raster"
        ]
},
    "zonal_geometry": {
        "name": "zonal_geometry",
        "description": "Calculates the specified geometry measure (area, perimeter, thickness, or the characteristics of an ellipse) for each zone in a dataset. Learn more about how Zonal Geometry works",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It must be an integer field of the zone dataset."
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type that will be calculated.AREA\u2014The area for each zone will be calculated.PERIMETER\u2014The perimeter for each zone will be calculated.THICKNESS\u2014The deepest (or thickest) point wi...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field"
        ]
},
    "zonal_geometry_as_table": {
        "name": "zonal_geometry_as_table",
        "description": "Calculates the geometry measures (area, perimeter, thickness, and the characteristics of an ellipse) for each zone in a dataset and reports the results as a table. Learn more about how Zonal Geometry works",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It must be an integer field of the zone dataset."
                },
                "out_table": {
                        "type": "string",
                        "description": "Output table that will contain the summary of the values in each zone.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table. If the ..."
                },
                "processing_cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster that will be created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn't been explicitly specified ...",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "out_table"
        ]
},
    "zonal_histogram": {
        "name": "zonal_histogram",
        "description": "Creates a table and a histogram graph that show the frequency distribution of cell values on the value input for each unique zone.",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset."
                },
                "in_value_raster": {
                        "type": "string",
                        "description": "The raster that contains the values used to create the histogram."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table file.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table if in a geodatabase workspace, and a dBASE table if in a..."
                },
                "out_graph": {
                        "type": "string",
                        "description": "The name of the output graph for display.",
                        "default": None
                },
                "zones_as_rows": {
                        "type": "string",
                        "description": "Specifies how the values from the input value raster will be represented in the output table.\r\nZONES_AS_FIELDS\u2014Zones will be represented as fields. This is the default.ZONES_AS_ROWS\u2014Zones will be repr...",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "in_value_raster",
                "out_table"
        ]
},
    "zonal_statistics": {
        "name": "zonal_statistics",
        "description": "Summarizes the values of a raster within the zones of another dataset. Learn more about how the zonal statistics tools work",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset."
                },
                "in_value_raster": {
                        "type": "string",
                        "description": "The raster that contains the values for which a statistic will be calculated."
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The average of all cells in the value raster that belong to the same zone as the output cell will be calculated.This is the default.MAJORITY\u2014The valu...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values in the value input will be ignored in the results of the zone that they fall within.DATA\u2014Within any particular zone, only cells that have a value in the input value ras...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be calculated if they are multidimensional.CURRENT_SLICE\u2014Statistics will be calculated from the current slice of the input multidimensional dataset. This is the de...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the percentile value falls between two cell values from the input value raster.AUTO_DETECT\u2014If the input value raster is of integer pixel ty...",
                        "default": None
                },
                "circular_calculation": {
                        "type": "string",
                        "description": "Specifies how the input raster will be processed for circular data.ARITHMETIC\u2014Ordinary linear statistics will be calculated. This is the default. CIRCULAR\u2014The statistics for angles or other cyclic qua...",
                        "default": None
                },
                "circular_wrap_value": {
                        "type": "string",
                        "description": "The value that will be used to round a linear value to the range of a given circular statistic. Its value must be a positive integer or a floating-point value. The default value is 360 degrees.This pa...",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "in_value_raster"
        ]
},
    "zonal_statistics_as_table": {
        "name": "zonal_statistics_as_table",
        "description": "Summarizes the values of a raster within the zones of another dataset and reports the results as a table. Learn more about how the zonal statistics tools work",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset."
                },
                "in_value_raster": {
                        "type": "string",
                        "description": "The raster that contains the values for which a statistic will be calculated."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that will contain the summary of the values in each zone.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table if i..."
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values in the value input will be ignored in the results of the zone that they fall within.DATA\u2014Within any particular zone, only cells that have a value in the input value ras...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.ALL\u2014All of the statistics will be calculated. This is the default.MEAN\u2014The average of all cells in the value raster that belong to the same zone as the ou...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be calculated if they are multidimensional.\r\nCURRENT_SLICE\u2014Statistics will be calculated from the current slice of the input multidimensional dataset. This is the ...",
                        "default": None
                },
                "percentile_values": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the percentile value falls between two cell values from the input value raster.AUTO_DETECT\u2014If the input value raster is of integer pixel ty...",
                        "default": None
                },
                "circular_calculation": {
                        "type": "string",
                        "description": "Specifies how the input raster will be processed for circular data.ARITHMETIC\u2014Ordinary linear statistics will be calculated. This is the default. CIRCULAR\u2014The statistics for angles or other cyclic qua...",
                        "default": None
                },
                "circular_wrap_value": {
                        "type": "string",
                        "description": "The value that will be used to round a linear value to the range of a given circular statistic. Its value must be a positive integer or a floating-point value. The default value is 360 degrees.This pa...",
                        "default": None
                },
                "out_join_layer": {
                        "type": "string",
                        "description": "The output layer that will be created by joining the output table to the input zone data.",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "in_value_raster",
                "out_table"
        ]
}
}
