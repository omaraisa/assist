# Generated ArcGIS Pro conversion AI Function Declarations
# Generated on 2025-10-01T14:01:07.518023
# Total tools: 50

functions_declarations = {
    "excel_to_table": {
        "name": "excel_to_table",
        "description": "Converts Microsoft Excel files into a table.",
        "parameters": {
                "input_excel_file": {
                        "type": "string",
                        "description": "The Excel file that will be converted."
                },
                "output_table": {
                        "type": "string",
                        "description": "The output table."
                },
                "field_names_row": {
                        "type": "string",
                        "description": "The row in the Excel sheet that contains values that will be used as field names.  The default value is 1.  The row specified will be skipped when converting records to the output table.If the Sheet\tp...",
                        "default": null
                },
                "cell_range": {
                        "type": "string",
                        "description": "The  cell range. This parameter is disabled when a named ranged is selected. If no cell range is specified, the tool will use the start and end cells of the specified sheet.A cell is the intersection ...",
                        "default": null
                }
        },
        "required": [
                "input_excel_file",
                "output_table"
        ]
},
    "table_to_excel": {
        "name": "table_to_excel",
        "description": "Converts  a table to a Microsoft Excel file (.xls or .xlsx).",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "The table or tables to be converted to an Excel file."
                },
                "output_excel_file": {
                        "type": "string",
                        "description": "The output Excel file. Specify the format of the Excel file using the .xls or .xlsx file extension."
                },
                "use_field_alias_column_header": {
                        "type": "string",
                        "description": "Specifies whether input field names or field aliases will be used as the output column names.NAME\u2014Column headers will be set using the input field names. This is the default.ALIAS\u2014Column headers will ...",
                        "default": null
                },
                "use_domain_and_subtype_description": {
                        "type": "string",
                        "description": "Specifies whether values from subtype fields or fields with a coded value domain will be transferred to the output.CODE\u2014All field values will be used as they are stored in the table. This is the defau...",
                        "default": null
                }
        },
        "required": [
                "input_table",
                "output_excel_file"
        ]
},
    "pdf_to_tiff": {
        "name": "pdf_to_tiff",
        "description": "Exports a .pdf file to Tagged Image File Format (TIFF).",
        "parameters": {
                "in_pdf_file": {
                        "type": "string",
                        "description": "The input .pdf file to be exported to TIFF."
                },
                "out_tiff_file": {
                        "type": "string",
                        "description": "The output  .tif file."
                },
                "pdf_password": {
                        "type": "string",
                        "description": "This parameter is unavailable at ArcGIS 3.5. It will be supported in a future release.",
                        "default": null
                },
                "pdf_page_number": {
                        "type": "string",
                        "description": "The page number of the PDF document to export to TIFF.",
                        "default": null
                },
                "pdf_map": {
                        "type": "string",
                        "description": "The map that will be exported.In a .pdf file, a map is a defined container of graphics on the PDF page that has a spatial reference. A PDF map is equivalent to an ArcGIS Pro map in that it is the cont...",
                        "default": null
                },
                "clip_option": {
                        "type": "string",
                        "description": "Specifies whether the entire page or only the map will be exported.CLIP_TO_MAP\u2014Only  the map specified in the pdf_map parameter will be exported to TIFF.NO_CLIP\u2014The entire page will be exported to TIF...",
                        "default": null
                },
                "resolution": {
                        "type": "string",
                        "description": "The resolution of the output .tif file in dots per inch (DPI).  The default is 250.",
                        "default": null
                },
                "color_mode": {
                        "type": "string",
                        "description": "Specifies the number of bits that will be used to describe color.Note:Additional options will be supported in a future release.RGB_TRUE_COLOR\u201432-bit RGBA color will be used. If the tiff_compression pa...",
                        "default": null
                },
                "tiff_compression": {
                        "type": "string",
                        "description": "Specifies the compression scheme for the output .tif file.LZW\u2014Lempel-Ziv-Welch, a lossless data compression, will be used. This is the default.DEFLATE\u2014A lossless data compression will be used.JPEG\u2014JPE...",
                        "default": null
                },
                "geotiff_tags": {
                        "type": "string",
                        "description": "Specifies whether GeoTIFF tags will be added to the output. This parameter is only supported if the in_pdf_file parameter value has a spatial reference.GEOTIFF_TAGS\u2014GeoTIFF tags will be added to the o...",
                        "default": null
                }
        },
        "required": [
                "in_pdf_file",
                "out_tiff_file"
        ]
},
    "raster_to_ascii": {
        "name": "raster_to_ascii",
        "description": "Converts a raster dataset to an ASCII file representing raster data.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset.The raster can be integer or floating-point type."
                },
                "out_ascii_file": {
                        "type": "string",
                        "description": "The output ASCII raster file."
                }
        },
        "required": [
                "in_raster",
                "out_ascii_file"
        ]
},
    "raster_to_float": {
        "name": "raster_to_float",
        "description": "Converts a raster dataset to a file of binary floating-point values representing raster data.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset.The raster can be integer or floating-point type."
                },
                "out_float_file": {
                        "type": "string",
                        "description": "The output floating-point raster file.The file name must have a .flt extension."
                }
        },
        "required": [
                "in_raster",
                "out_float_file"
        ]
},
    "raster_to_point": {
        "name": "raster_to_point",
        "description": "Converts a raster dataset to point features.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset.The raster can be integer or floating-point type."
                },
                "out_point_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the converted points."
                },
                "raster_field": {
                        "type": "string",
                        "description": "The field to assign values from the cells in the input raster to the points in the output dataset.It can be an integer, floating point, or string field.",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "out_point_features"
        ]
},
    "raster_to_polygon": {
        "name": "raster_to_polygon",
        "description": "Converts a raster dataset to polygon features.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset.The raster must be integer type."
                },
                "out_polygon_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the converted polygons."
                },
                "simplify": {
                        "type": "string",
                        "description": "Determines if the output polygons will be smoothed into simpler shapes or conform to the input raster's cell edges.SIMPLIFY\u2014The polygons will be smoothed into simpler shapes. The smoothing is done in ...",
                        "default": null
                },
                "raster_field": {
                        "type": "string",
                        "description": "The field used to assign values from the cells in the input raster to the polygons in the output dataset.It can be an integer or a string field.",
                        "default": null
                },
                "create_multipart_features": {
                        "type": "string",
                        "description": "Specifies whether the output polygons will consist of single-part or multipart features.\r\nMULTIPLE_OUTER_PART\u2014Specifies that multipart features will be created based on polygons that have the same val...",
                        "default": null
                },
                "max_vertices_per_feature": {
                        "type": "string",
                        "description": "The vertex limit used to subdivide a polygon into smaller polygons. This parameter produces similar output as created by the Dice tool.If left empty, the output polygons will not be split. The default...",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "out_polygon_features"
        ]
},
    "raster_to_polyline": {
        "name": "raster_to_polyline",
        "description": "Converts a raster dataset to polyline features.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset.The raster must be integer type."
                },
                "out_polyline_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the converted polylines."
                },
                "background_value": {
                        "type": "string",
                        "description": "Specifies the value that will identify the background cells. The raster dataset is viewed as a set of foreground cells and background cells. The linear features are formed from the foreground cells.ZE...",
                        "default": null
                },
                "minimum_dangle_length": {
                        "type": "string",
                        "description": "Minimum length of dangling polylines that will be retained. The default is zero.",
                        "default": null
                },
                "simplify": {
                        "type": "string",
                        "description": "Simplifies a line by removing small fluctuations or extraneous bends from it while preserving its essential shape.SIMPLIFY\u2014The polylines will be simplified into simpler shapes such that each contains ...",
                        "default": null
                },
                "raster_field": {
                        "type": "string",
                        "description": "The field used to assign values from the cells in the input raster to the polyline features in the output dataset.It can be an integer or a string field.",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "out_polyline_features"
        ]
},
    "wfs_to_feature_class": {
        "name": "wfs_to_feature_class",
        "description": "Imports a feature type from a Web Feature Service (WFS) to a feature class in a geodatabase.",
        "parameters": {
                "input_wfs_server": {
                        "type": "string",
                        "description": "The URL of the source WFS service (for example,  http://sampleserver6.arcgisonline.com/arcgis/services/SampleWorldCities/MapServer/WFSServer?). If the input is a complex WFS service (is_complex is set..."
                },
                "wfs_feature_type": {
                        "type": "string",
                        "description": "The name of the WFS layer that will be extracted from the input WFS service."
                },
                "out_path": {
                        "type": "string",
                        "description": "The location of the output feature class or geodatabase.If the input is a simple WFS service, the output location can be a geodatabase or a feature dataset in a geodatabase. If the output location is ..."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the output feature class or geodatabase.If the input is a simple WFS service, the name will be used to create a feature class in the output location. If the feature class name already exis..."
                },
                "is_complex": {
                        "type": "string",
                        "description": "Specifies whether the input_WFS_server parameter value is a complex WFS service.COMPLEX\u2014The WFS service is a complex WFS service.NOT_COMPLEX\u2014The WFS service is not a complex WFS service. This is the d...",
                        "default": null
                },
                "max_features": {
                        "type": "string",
                        "description": "The maximum number of features that can be returned. The default is 1000.",
                        "default": null
                },
                "expose_metadata": {
                        "type": "string",
                        "description": "Specifies whether metadata tables will be created from the service. This is only applicable to complex WFS services.EXPOSE_METADATA\u2014Metadata tables will be created in the output geodatabase.DO_NOT_EXP...",
                        "default": null
                },
                "swap_xy": {
                        "type": "string",
                        "description": "Specifies whether the x,y axis order of the output feature class will be swapped. Some WFS services may have the order of the x,y coordinates swapped on the server side, causing the feature class to d...",
                        "default": null
                },
                "page_size": {
                        "type": "string",
                        "description": "The page size that will be used when downloading features from the WFS service. The default is 100. Some servers limit the number of features that can be requested at a time or server performance may ...",
                        "default": null
                }
        },
        "required": [
                "input_wfs_server",
                "wfs_feature_type",
                "out_path",
                "out_name"
        ]
},
    "features_to_gpx": {
        "name": "features_to_gpx",
        "description": "Converts point, multipoint, or polyline features to a GPX format file (.gpx).",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point, multipoint, or line features."
                },
                "out_gpx_file": {
                        "type": "string",
                        "description": "The .gpx file that will be created with the  geometry and attributes of the input features."
                },
                "name_field": {
                        "type": "string",
                        "description": "A field from the input features with values used to populate the GPX name tag.",
                        "default": null
                },
                "description_field": {
                        "type": "string",
                        "description": "A field from the input features with\r\nvalues used to populate the GPX desc tag.",
                        "default": null
                },
                "z_field": {
                        "type": "string",
                        "description": "A numeric field from the input features with  values used to populate the GPX elevation tag. If an elevation field is not specified, the z-values from the input features' geometries will be used to po...",
                        "default": null
                },
                "date_field": {
                        "type": "string",
                        "description": "A date/time field from the input features with values used to populate the GPX time tag.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_gpx_file"
        ]
},
    "gpx_to_features": {
        "name": "gpx_to_features",
        "description": "Converts the point data in a .gpx file to features.",
        "parameters": {
                "input_gpx_file": {
                        "type": "string",
                        "description": "The input .gpx file to be converted."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output point feature class."
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies the geometry type of the output feature class.POINTS\u2014An output point feature class will be created. All GPX points will be included in the output. This is the default.TRACKS_AS_LINES\u2014An outp...",
                        "default": null
                }
        },
        "required": [
                "input_gpx_file",
                "output_feature_class"
        ]
},
    "features_to_graphics": {
        "name": "features_to_graphics",
        "description": "Converts a feature layer's symbolized features into graphic elements in a graphics layer.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The layer to convert to graphics."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The graphics layer containing the converted graphic elements."
                },
                "exclude_features": {
                        "type": "string",
                        "description": "Specifies whether the converted\r\nfeatures will be excluded using a query.EXCLUDE_FEATURES\u2014The features will be excluded. This is the default.KEEP_FEATURES\u2014The features will not be excluded; they will ...",
                        "default": null
                }
        },
        "required": [
                "in_layer",
                "out_layer"
        ]
},
    "graphics_to_features": {
        "name": "graphics_to_features",
        "description": "Converts a graphics layer into a feature layer with geometries based on the input graphics layer's elements.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The graphics layer containing the source graphic elements that will be converted to features."
                },
                "graphics_type": {
                        "type": "string",
                        "description": "Specifies the type of graphic element that will be converted.POINT\u2014Point graphic elements will be converted.POLYLINE\u2014Polyline graphic elements will be converted.POLYGON\u2014Polygon graphic elements will b..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature layer that will contain the converted graphic elements."
                },
                "delete_graphics": {
                        "type": "string",
                        "description": "Specifies whether the converted graphic elements from the in_layer parameter will be deleted after conversion.DELETE_GRAPHICS\u2014The converted graphic elements will be deleted. This is the default.KEEP_G...",
                        "default": null
                },
                "reference_scale": {
                        "type": "string",
                        "description": "The reference scale that will be used to convert text elements to annotation features. This parameter is required when the graphics_type parameter is set to ANNOTATION.",
                        "default": null
                }
        },
        "required": [
                "in_layer",
                "graphics_type",
                "out_feature_class"
        ]
},
    "features_to_json": {
        "name": "features_to_json",
        "description": "Converts features to Esri JSON or GeoJSON format. The fields, geometry, and spatial reference of features will be converted to their corresponding JSON representation and written to a file with a .json or .geojson extension.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features that will be converted to JSON format."
                },
                "out_json_file": {
                        "type": "string",
                        "description": "The output .json or .geojson file."
                },
                "format_json": {
                        "type": "string",
                        "description": "Specifies whether the JSON will be formatted to improve readability similar to the ArcGIS REST API specification's PJSON (Pretty JSON) format.NOT_FORMATTED\u2014 The features will not be formatted. This is...",
                        "default": null
                },
                "include_z_values": {
                        "type": "string",
                        "description": "Specifies whether the z-values of the features will be included in the JSON.NO_Z_VALUES\u2014 The z-values will not be included in geometries, and the hasZ property of the JSON will not be included. This i...",
                        "default": null
                },
                "include_m_values": {
                        "type": "string",
                        "description": "Specifies whether the m-values of the features will be included in the JSON.NO_M_VALUES\u2014 The m-values will not be included in geometries, and the hasM property of the JSON will not be included. This i...",
                        "default": null
                },
                "geojson": {
                        "type": "string",
                        "description": "Specifies whether the output will be created in GeoJSON format, conforming to the GeoJSON specification or Esri JSON format,.GEOJSON\u2014 The output will be created in GeoJSON format (.geojson file). NO_G...",
                        "default": null
                },
                "outputtowgs84": {
                        "type": "string",
                        "description": "Specifies whether the input features will be projected to the WGS84 geographic coordinate system with a default geographic transformation. This parameter only applies when the output is GeoJSON.WGS84\u2014...",
                        "default": null
                },
                "use_field_alias": {
                        "type": "string",
                        "description": "Specifies whether the output file will use field aliases for feature attributes.USE_FIELD_NAME\u2014Output feature attributes will not use field aliases; they will use field names. This is the default.USE_...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_json_file"
        ]
},
    "json_to_features": {
        "name": "json_to_features",
        "description": "Converts feature collections in an Esri JSON formatted file (.json) or a GeoJSON formatted file (.geojson) to a feature class.",
        "parameters": {
                "in_json_file": {
                        "type": "string",
                        "description": "The input .json or .geojson file that will be converted to a feature class. The input file extension determines the format used by the tool for proper conversion. For Esri JSON formatted file, use the..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the features from the input .json or .geojson file."
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type that will be used to convert from GeoJSON to features. This parameter is only used when the input is a .geojson file.\r\nIf the .geojson file does not contain any of the spec...",
                        "default": null
                }
        },
        "required": [
                "in_json_file",
                "out_features"
        ]
},
    "kml_to_layer": {
        "name": "kml_to_layer",
        "description": "Converts a .kml or .kmz file into datasets in a geodatabase  and a layer file.  The layer file  maintains the symbology of the input .kml or .kmz file. Learn more about KML support in ArcGIS",
        "parameters": {
                "in_kml_file": {
                        "type": "string",
                        "description": "The .kml or .kmz file that will be converted to geodatabase datasets."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The destination folder where the output geodatabase and layer file (.lyrx) will be created."
                },
                "output_data": {
                        "type": "string",
                        "description": "The name that will be used for both the output geodatabase and layer file (.lyrx). The default is the name of the input file.\r\nYou can specify the name of an existing geodatabase in the target folder,...",
                        "default": null
                },
                "include_groundoverlay": {
                        "type": "string",
                        "description": "Specifies whether ground overlays from the KML will be included in the output.\r\nUse caution if the KMZ points to a service that serves imagery. The tool will attempt to convert the raster imagery at a...",
                        "default": null
                },
                "out_suffix": {
                        "type": "string",
                        "description": "The suffix that will be added to the names of all output feature datasets, feature classes, mosaic datasets, and layer files. If no suffix is specified, the name of the feature dataset in the output g...",
                        "default": null
                }
        },
        "required": [
                "in_kml_file",
                "output_folder"
        ]
},
    "layer_to_kml": {
        "name": "layer_to_kml",
        "description": "Converts a feature or raster layer  to KML format (.kmz or .kml file). The output KML will contain a translation of Esri feature geometries, raster cells, layer symbology, and other properties. Learn more about KML support in ArcGIS",
        "parameters": {
                "layer": {
                        "type": "string",
                        "description": "The  feature or raster layer  or group layer that will be converted to KML format."
                },
                "out_kmz_file": {
                        "type": "string",
                        "description": "The output .kml or .kmz file. The output file can use the .kmz extension  to produce an archive or zipped file, or the .kml  extension to produce a basic KML format file. An output .kmz file is the de..."
                },
                "layer_output_scale": {
                        "type": "string",
                        "description": "The scale of the output file. For raster layers, a value of 0 can be used to create one untiled output image. If a value greater than or equal to 1 is used, it will determine the output resolution of ...",
                        "default": null
                },
                "is_composite": {
                        "type": "string",
                        "description": "Specifies whether the output will be a single composite image.  This parameter only applies if you specify the output KML as a .kmz file, as output .kml files do not support ground overlay images or r...",
                        "default": null
                },
                "boundary_box_extent": {
                        "type": "string",
                        "description": "The geographic extent of the layer to be converted. Only features or raster cells in this extent will be included in the output KML. The extent can be specified using the following options:MAXOF\u2014The m...",
                        "default": null
                },
                "image_size": {
                        "type": "string",
                        "description": "The size of the tiles for raster layers if the layer_output_scale parameter value is greater than or equal to 1. This parameter has no effect on layers that are not raster layers.",
                        "default": null
                },
                "dpi_of_client": {
                        "type": "string",
                        "description": "The device resolution for KML output when the is_composite parameter is set to COMPOSITE. Use this parameter with the image_size parameter to control output image resolution.This parameter does not re...",
                        "default": null
                },
                "ignore_zvalue": {
                        "type": "string",
                        "description": "Specifies whether the z-values of the input features will be ignored and all features will be located, or clamped, at the ground elevation.ABSOLUTE\u2014The z-values of the features will be maintained in t...",
                        "default": null
                }
        },
        "required": [
                "layer",
                "out_kmz_file"
        ]
},
    "map_to_kml": {
        "name": "map_to_kml",
        "description": "Converts a map containing feature or raster layers  to KML format (.kmz  file). The output KML will contain a translation of Esri feature geometries, raster cells, layer symbology, and other properties. Learn more about KML support in ArcGIS",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The map, scene, or basemap that will be converted to KML."
                },
                "out_kmz_file": {
                        "type": "string",
                        "description": "The output KML file, which is compressed and has a .kmz extension."
                },
                "map_output_scale": {
                        "type": "string",
                        "description": "The scale at which each layer in the map will be exported. This\r\nparameter is important with any scale dependency, such as layer\r\nvisibility or scale-dependent rendering. If the layer is not\r\nvisible ...",
                        "default": null
                },
                "is_composite": {
                        "type": "string",
                        "description": "Specifies whether the output KML will contain a single composite image or separate layers.COMPOSITE\u2014The output KML will contain a single image that\r\ncomposites all the features in the map into a singl...",
                        "default": null
                },
                "is_vector_to_raster": {
                        "type": "string",
                        "description": "Specifies whether each feature layer in the map will be converted to a separate raster image\r\nor preserved as features. This parameter is not used if the is_composite parameter is set to COMPOSITE.VEC...",
                        "default": null
                },
                "extent_to_export": {
                        "type": "string",
                        "description": "The geographic extent of the layer to be converted. Only features or raster cells in this extent will be included in the output KML. The extent can be specified using the following options:\r\nMAXOF\u2014The...",
                        "default": null
                },
                "image_size": {
                        "type": "string",
                        "description": "The size of the tiles for raster layers if\r\nthe map_output_scale parameter value is greater than\r\nor equal to 1. This parameter has no effect on layers that are not raster layers.",
                        "default": null
                },
                "dpi_of_client": {
                        "type": "string",
                        "description": "The device resolution for any rasters in the output KML\r\ndocument. Typical screen resolution is 96 dpi. If the data in\r\nthe map supports a high resolution and the KML requires it,\r\nconsider increasing...",
                        "default": null
                },
                "ignore_zvalue": {
                        "type": "string",
                        "description": "Specifies whether the z-values of the input features will be ignored and all features will be located, or clamped, at the ground elevation.ABSOLUTE\u2014The z-values of the features will be maintained in t...",
                        "default": null
                },
                "layout": {
                        "type": "string",
                        "description": "The name of the layout that contains legend elements that will be included in the KML output as screen overlays.",
                        "default": null
                }
        },
        "required": [
                "in_map",
                "out_kmz_file"
        ]
},
    "convert_las": {
        "name": "convert_las",
        "description": "Converts .las, .zlas, and .laz files between different LAS compression methods, file versions, and point record formats.",
        "parameters": {
                "in_las": {
                        "type": "string",
                        "description": "The .las, .zlas, or .laz files that will be converted. Multiple files can be processed by specifying the folder containing the files or a LAS dataset."
                },
                "target_folder": {
                        "type": "string",
                        "description": "The existing folder where the output files will be written."
                },
                "file_version": {
                        "type": "string",
                        "description": "Specifies the file version that will be used for the output files.SAME_AS_INPUT\u2014The output file version will be the same as the input. This is the default.1.0\u2014The base version for the LAS format that ...",
                        "default": null
                },
                "point_format": {
                        "type": "string",
                        "description": "Specifies the point record format that will be used for the output files. The available options will vary based on the output LAS format file version.\r\n0\u2014The base type for storing discrete LAS points ...",
                        "default": null
                },
                "compression": {
                        "type": "string",
                        "description": "Specifies whether the output files will be stored in  a compressed or uncompressed format.NO_COMPRESSION\u2014Output files will be in the uncompressed LAS format (*.las). This format supports edits to clas...",
                        "default": null
                },
                "las_options": {
                        "type": "string",
                        "description": "Specifies the modifications that will be made to the output files that will reduce their size and improve their performance in display and analysis.\r\nREARRANGE_POINTS\u2014Points will be rearranged to impr...",
                        "default": null
                },
                "out_las_dataset": {
                        "type": "string",
                        "description": "The output LAS dataset referencing the newly created .las files.",
                        "default": null
                },
                "define_coordinate_system": {
                        "type": "string",
                        "description": "Specifies how the coordinate system of each input file will be defined.NO_FILES\u2014The coordinate system of each input file will be defined by the information in its header. Any file that lacks spatial r...",
                        "default": null
                },
                "in_coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system that will be used to define the spatial reference of some or all input files based on the define_coordinate_system parameter value.",
                        "default": null
                }
        },
        "required": [
                "in_las",
                "target_folder"
        ]
},
    "las_dataset_to_raster": {
        "name": "las_dataset_to_raster",
        "description": "Creates a raster using elevation, intensity, or RGB values stored in the lidar points referenced by the LAS dataset.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be processed."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The location and name of the output raster. When storing a raster dataset in a geodatabase or in a folder such as an Esri Grid, do not add a file extension to the name of the raster dataset. A file ex..."
                },
                "value_field": {
                        "type": "string",
                        "description": "Specifies the information from the lidar data that will be used to generate the raster output.\r\nELEVATION\u2014Elevation from the lidar files will be used to create the raster. This is the default.INTENSIT...",
                        "default": null
                },
                "interpolation_type_binning_cell_assignment_type_void_fill_method_or_triangulation_interpolation_method_point_thinning_type_point_selection_method_resolution": {
                        "type": "string",
                        "description": "The interpolation type that will be used to determine the cell value of the output raster. Either binning or triangulation based interpolation can be specified. Each type presents unique options for a...",
                        "default": null
                },
                "data_type": {
                        "type": "string",
                        "description": "Specifies the type of numeric values that will be stored in the output raster.\t\t\t\t\tFLOAT\u2014The output raster will use 32-bit floating point, which supports values ranging from -3.402823466e+38 to 3.4028...",
                        "default": null
                },
                "sampling_type": {
                        "type": "string",
                        "description": "Specifies how the Sampling Value parameter will be interpreted to define the output raster's cell size.\t\t\t\t\tOBSERVATIONS\u2014The Sampling Value will define the number of columns or rows in the output rast...",
                        "default": null
                },
                "sampling_value": {
                        "type": "string",
                        "description": "The value used in conjunction with the Sampling Type parameter to define the output raster's cell size.",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": null
                }
        },
        "required": [
                "in_las_dataset",
                "out_raster"
        ]
},
    "mesh_to_las": {
        "name": "mesh_to_las",
        "description": "Converts an integrated mesh into a LAS format point cloud.",
        "parameters": {
                "in_mesh": {
                        "type": "string",
                        "description": "The integrated mesh scene layer package or I3S service that will be exported to the LAS format point cloud."
                },
                "target_folder": {
                        "type": "string",
                        "description": "The folder where the output LAS format files that will be created from the integrated mesh will be stored."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to create the point cloud from the integrated mesh.\r\nSAMPLE_POINTS_FROM_FACES\u2014Points will be sampled from the integrated mesh triangle faces. Triangles may poten...",
                        "default": null
                },
                "maximum_triangle_area": {
                        "type": "string",
                        "description": "Controls the density of points created from the integrated mesh by defining the maximum area of each triangle that contributes points. Any mesh triangle that is larger than this value will be subdivid...",
                        "default": null
                },
                "extent": {
                        "type": "string",
                        "description": "The extent of the integrated mesh that will be exported to the point cloud. If the processing extent is specified with an extraction boundary polygon, both the intersection of the extent and the bound...",
                        "default": null
                },
                "boundary": {
                        "type": "string",
                        "description": "The polygon features defining the area that will be clipped.",
                        "default": null
                },
                "rearrange_points": {
                        "type": "string",
                        "description": "Specifies whether points  in the .las  or .zlas files will be rearranged to optimize the performance of reading and updating the classification of the point cloud.\r\nMAINTAIN_POINTS\u2014The order of points...",
                        "default": null
                },
                "compute_stats": {
                        "type": "string",
                        "description": "Specifies whether statistics will be computed for the .las files referenced by the LAS dataset. Computing statistics provides a spatial index for each .las file, which improves analysis and display pe...",
                        "default": null
                },
                "out_las_dataset": {
                        "type": "string",
                        "description": "The output LAS dataset that will reference the LAS format files created by the conversion process.",
                        "default": null
                },
                "compression": {
                        "type": "string",
                        "description": "Specifies whether the output .las file will be in  a compressed format or the standard LAS format.NO_COMPRESSION\u2014The output will be in the standard LAS format (*.las file). This is the default.ZLAS\u2014Ou...",
                        "default": null
                }
        },
        "required": [
                "in_mesh",
                "target_folder"
        ]
},
    "point_cloud_to_raster": {
        "name": "point_cloud_to_raster",
        "description": "Creates a raster surface from height values in a point cloud scene layer package (*.slpk file) or Indexed 3D Scene (I3S) service.",
        "parameters": {
                "in_point_cloud": {
                        "type": "string",
                        "description": "The point cloud scene layer package (*.slpk file) or I3S point cloud scene layer service that will be used to generate an elevation raster. An I3S point cloud scene layer service must have the export ..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The length and width of each cell in the output raster."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The location and name of the output raster. When storing a raster dataset in a geodatabase or in a folder such as an Esri Grid, do not add a file extension to the name of the raster dataset. A file ex..."
                },
                "cell_assignment": {
                        "type": "string",
                        "description": "Specifies the method that will be used for assigning values to cells containing points.AVERAGE\u2014The cell value will be defined by the average of the z-values for all points in the cell. This is the def...",
                        "default": null
                },
                "void_fill": {
                        "type": "string",
                        "description": "Specifies the method that will be used for interpolating the values of cells within the interpolation zone that do not contain points.NONE\u2014No value will be assigned to raster cells that do not contain...",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves the z-values unchanged.",
                        "default": null
                }
        },
        "required": [
                "in_point_cloud",
                "cell_size",
                "out_raster"
        ]
},
    "sas_to_table": {
        "name": "sas_to_table",
        "description": "Converts a SAS dataset to a table.",
        "parameters": {
                "in_sas_dataset": {
                        "type": "string",
                        "description": "The input SAS dataset.\r\nProvide the dataset in the form libref.tablename in which libref is the name of a SAS library and tablename is the name of the SAS dataset."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table."
                },
                "use_cas_connection": {
                        "type": "string",
                        "description": "Specifies whether the input SAS dataset will be downloaded from CAS or accessed from a local SAS library.USE_CAS\u2014The input SAS dataset will be downloaded from CAS.LOCAL_SAS\u2014The input SAS dataset will ...",
                        "default": null
                },
                "hostname": {
                        "type": "string",
                        "description": "The URL of the CAS host.",
                        "default": null
                },
                "port": {
                        "type": "string",
                        "description": "The port of the CAS connection.",
                        "default": null
                },
                "username": {
                        "type": "string",
                        "description": "The username for the CAS connection.",
                        "default": null
                },
                "password": {
                        "type": "string",
                        "description": "The password for the CAS connection.  This password is hidden and not accessible after running the tool.",
                        "default": null
                },
                "custom_cfg_file": {
                        "type": "string",
                        "description": "The file specifying custom configurations for the SAS session. The file is only required for customized local or remote SAS deployments.",
                        "default": null
                },
                "authinfo_file": {
                        "type": "string",
                        "description": "The file containing authentication information when connecting to CAS.\r\nThe file must contain the username and encoded password for the connection.  If a file is provided, the username and password pa...",
                        "default": null
                }
        },
        "required": [
                "in_sas_dataset",
                "out_table"
        ]
},
    "table_to_sas": {
        "name": "table_to_sas",
        "description": "Converts a table to a SAS dataset.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table."
                },
                "out_sas_dataset": {
                        "type": "string",
                        "description": "The output SAS dataset.\r\nProvide the dataset in the form libref.table in which libref is the name of a SAS library and table is the name of the SAS table."
                },
                "replace_sas_dataset": {
                        "type": "string",
                        "description": "Specifies whether an existing SAS dataset will be overwritten in the output.OVERWRITE\u2014The output SAS dataset can overwrite an existing dataset.NO_OVERWRITE\u2014The output SAS dataset cannot overwrite an e...",
                        "default": null
                },
                "use_domain_and_subtype_description": {
                        "type": "string",
                        "description": "Specifies whether domain and subtype descriptions will be included in the output SAS dataset.USE_DOMAIN\u2014Domain and subtype descriptions will be included in the output SAS dataset.NO_DOMAIN\u2014Domain and ...",
                        "default": null
                },
                "use_cas_connection": {
                        "type": "string",
                        "description": "Specifies whether the output SAS dataset will be uploaded to \r\nCAS or saved in a local SAS library.USE_CAS\u2014The output SAS dataset will be uploaded to CAS.LOCAL_SAS\u2014The output SAS dataset will be saved...",
                        "default": null
                },
                "hostname": {
                        "type": "string",
                        "description": "The URL of the CAS host.",
                        "default": null
                },
                "port": {
                        "type": "string",
                        "description": "The port of the CAS connection.",
                        "default": null
                },
                "username": {
                        "type": "string",
                        "description": "The username for the CAS connection.",
                        "default": null
                },
                "password": {
                        "type": "string",
                        "description": "The password for the CAS connection.  This password is hidden and not accessible after running the tool.",
                        "default": null
                },
                "custom_cfg_file": {
                        "type": "string",
                        "description": "The file specifying custom configurations for the SAS session. The file is only required for customized local or remote SAS deployments.",
                        "default": null
                },
                "authinfo_file": {
                        "type": "string",
                        "description": "The file containing authentication information when connecting to CAS.\r\nThe file must contain the username and encoded password for the connection.  If a file is provided, the username and password pa...",
                        "default": null
                }
        },
        "required": [
                "in_table",
                "out_sas_dataset"
        ]
},
    "add_cad_fields": {
        "name": "add_cad_fields",
        "description": "Adds several reserved CAD fields in one step. Fields created by this tool are used by the Export To CAD tool to generate CAD entities with specific properties.   After executing this tool, you must calculate or type the appropriate field values.",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "Input table, feature class, or shapefile that will have the CAD-specific fields added to it"
                },
                "entities": {
                        "type": "string",
                        "description": "Adds the list of CAD-specific Entity property fields to the input tableADD_ENTITY_PROPERTIES\u2014Adds the list of CAD-specific Entity property fields to the input tableNO_ENTITY_PROPERTIES\u2014Does not add th..."
                },
                "layerprops": {
                        "type": "string",
                        "description": "Adds the list of CAD-specific Layer property fields to the input tableADD_LAYER_PROPERTIES\u2014Adds the list of CAD-specific Layer property fields to the input tableNO_LAYER_PROPERTIES\u2014Does not add the li...",
                        "default": null
                },
                "textprops": {
                        "type": "string",
                        "description": "Adds the list of CAD-specific Text property fields to the input tableADD_TEXT_PROPERTIES\u2014Adds the list of CAD-specific Text property fields to the input tableNO_TEXT_PROPERTIES\u2014Does not add the list o...",
                        "default": null
                },
                "docprops": {
                        "type": "string",
                        "description": "Adds the list of CAD-specific Document property fields to the input tableADD_DOCUMENT_PROPERTIES\u2014Adds the list of CAD-specific Document property fields to the input tableNO_DOCUMENT_PROPERTIES\u2014Does no...",
                        "default": null
                },
                "xdataprops": {
                        "type": "string",
                        "description": "Adds the list of CAD-specific XData property fields to the input tableADD_XDATA_PROPERTIES\u2014Adds the list of CAD-specific XData property fields to the input tableNO_XDATA_PROPERTIES\u2014Does not add the li...",
                        "default": null
                }
        },
        "required": [
                "input_table",
                "entities"
        ]
},
    "export_to_cad": {
        "name": "export_to_cad",
        "description": "Exports features to  new or existing CAD files based on one or more input feature layers or feature classes. The geometry, feature attributes, and coordinates system of ArcGIS feature layers will be included when outputting to AutoCAD .dwg or .dxf files. This GIS data  can be used with the ArcGIS for AutoCAD plug-in to AutoCAD.  If you do not have the plug-in, you can access the output geometry as CAD entities.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "A collection of feature classes and feature layers whose spatial reference and geometry  will be exported to one or more CAD files. Both the feature geometry and the feature attributes  will be added ..."
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies the CAD platform and file version that will be used for new  output CAD files. Multiple versions of CAD software may share one file format version for multiple releases.  The options reflect..."
                },
                "append_to_existing": {
                        "type": "string",
                        "description": "Specifies whether the output will be appended to an existing CAD file. This allows you to add information to a CAD file on disk.Append_To_Existing_Files\u2014Entities will be appended to an output CAD file...",
                        "default": null
                },
                "seed_file": {
                        "type": "string",
                        "description": "An existing CAD drawing whose contents and document and layer properties will be used as a seed file when output CAD files are created. The CAD platform and format version of the seed file overrides t...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "output_type"
        ]
},
    "export_to_cad": {
        "name": "export_to_cad",
        "description": "Exports features to  new or existing CAD files based on one or more input feature layers or feature classes. The geometry, feature attributes, and coordinates system of ArcGIS feature layers will be included when outputting to AutoCAD .dwg or .dxf files. This GIS data  can be used with the ArcGIS for AutoCAD plug-in to AutoCAD.  If you do not have the plug-in, you can access the output geometry as CAD entities.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "A collection of feature classes and feature layers whose spatial reference and geometry  will be exported to one or more CAD files. Both the feature geometry and the feature attributes  will be added ..."
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies the CAD platform and file version that will be used for new  output CAD files. Multiple versions of CAD software may share one file format version for multiple releases.  The options reflect..."
                },
                "append_to_existing": {
                        "type": "string",
                        "description": "Specifies whether the output will be appended to an existing CAD file. This allows you to add information to a CAD file on disk.Append_To_Existing_Files\u2014Entities will be appended to an output CAD file...",
                        "default": null
                },
                "seed_file": {
                        "type": "string",
                        "description": "An existing CAD drawing whose contents and document and layer properties will be used as a seed file when output CAD files are created. The CAD platform and format version of the seed file overrides t...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "output_type"
        ]
},
    "multipatch_to_collada": {
        "name": "multipatch_to_collada",
        "description": "Converts one or more multipatch features into a collection of COLLADA files (.dae) and referenced texture image files in an output folder.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The multipatch features to be exported."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The destination folder where the output COLLADA files and texture image files will be placed."
                },
                "prepend_source": {
                        "type": "string",
                        "description": "Specifies whether the names of the output COLLADA files will be prepended with the name of the source feature layer.\r\nPREPEND_SOURCE_NAME\u2014The file names will be prepended with the name of the source f...",
                        "default": null
                },
                "field_name": {
                        "type": "string",
                        "description": "The feature attribute that will be used as the output COLLADA file name for each exported feature. If no field is specified, the feature's Object ID will be used.",
                        "default": null
                },
                "collada_version": {
                        "type": "string",
                        "description": "Specifies the COLLADA version to which the files will be exported.\r\n1.5\u2014Files will be exported to COLLADA version 1.5. Version 1.5 supports the inclusion of georeferencing information and enhanced ren..."
                }
        },
        "required": [
                "in_features",
                "output_folder",
                "collada_version"
        ]
},
    "table_to_dbase": {
        "name": "table_to_dbase",
        "description": "Converts one or more tables to dBASE tables.",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "The list of tables to be converted to dBASE tables."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The destination folder where the output dBASE tables will be placed."
                }
        },
        "required": [
                "input_table",
                "output_folder"
        ]
},
    "table_to_dbase": {
        "name": "table_to_dbase",
        "description": "Converts one or more tables to dBASE tables.",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "The list of tables to be converted to dBASE tables."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The destination folder where the output dBASE tables will be placed."
                }
        },
        "required": [
                "input_table",
                "output_folder"
        ]
},
    "table_to_dbase": {
        "name": "table_to_dbase",
        "description": "Converts one or more tables to dBASE tables.",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "The list of tables to be converted to dBASE tables."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The destination folder where the output dBASE tables will be placed."
                }
        },
        "required": [
                "input_table",
                "output_folder"
        ]
},
    "bim_file_to_geodatabase": {
        "name": "bim_file_to_geodatabase",
        "description": "Imports the contents of one or more BIM file workspaces into a single geodatabase feature dataset.",
        "parameters": {
                "in_bim_file_workspace": {
                        "type": "string",
                        "description": "The BIM file or files that will be converted to geodatabase feature classes."
                },
                "out_gdb_path": {
                        "type": "string",
                        "description": "The geodatabase where the output feature dataset will be created. This  must be an existing geodatabase."
                },
                "out_dataset_name": {
                        "type": "string",
                        "description": "The building dataset name."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature dataset.To control other aspects of the spatial reference, such as the x,y-, z-, and m-domains, resolutions, and tolerances, set the appropriate geoprocessi...",
                        "default": null
                },
                "identifier": {
                        "type": "string",
                        "description": "A unique building identifier that will be added to all output feature classes. The identifier allows you to add unique names to each building to be used at a later time.",
                        "default": null
                },
                "include_floorplan": {
                        "type": "string",
                        "description": "Specifies whether the output dataset will include the floorplan feature classes.INCLUDE_FLOORPLAN\u2014The output dataset will include the floorplan feature classes. This is the default.EXCLUDE_FLOORPLAN\u2014T...",
                        "default": null
                }
        },
        "required": [
                "in_bim_file_workspace",
                "out_gdb_path",
                "out_dataset_name"
        ]
},
    "cad_to_geodatabase": {
        "name": "cad_to_geodatabase",
        "description": "Reads a CAD dataset and creates feature classes of the drawing. The feature classes are written to a geodatabase feature dataset.",
        "parameters": {
                "input_cad_datasetscad_drawing_dataset": {
                        "type": "string",
                        "description": "The collection of CAD files that will be converted to geodatabase features."
                },
                "out_gdb_path": {
                        "type": "string",
                        "description": "The geodatabase where the output feature dataset will be created. This  geodatabase must already exist."
                },
                "out_dataset_name": {
                        "type": "string",
                        "description": "The name of the feature dataset that will be created."
                },
                "reference_scale": {
                        "type": "string",
                        "description": "This parameter is not needed for this tool, as CAD annotation is treated as points in ArcGIS Pro."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature dataset. To control other aspects of the spatial reference, such as the x-, y-, z-, and m-domains, resolutions, and tolerances, set the appropriate geoproce...",
                        "default": null
                }
        },
        "required": [
                "input_cad_datasetscad_drawing_dataset",
                "out_gdb_path",
                "out_dataset_name",
                "reference_scale"
        ]
},
    "export_features": {
        "name": "export_features",
        "description": "Converts a feature class or feature layer to a new feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that will be exported to a new feature class."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class containing the exported features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of features.  For more information on SQL syntax  see the help topic SQL reference for query expressions used in ArcGIS.",
                        "default": null
                },
                "use_field_alias_name": {
                        "type": "string",
                        "description": "Specifies whether the input's field names or field aliases will be used as the output field name.NOT_USE_ALIAS\u2014The input's field names will be used as the output field names. This is the default.USE_A...",
                        "default": null
                },
                "field_mapping": {
                        "type": "string",
                        "description": "The fields that will be transferred to the output dataset with their respective properties and source fields. The output includes all fields from the input dataset by default.Use the field map to add,...",
                        "default": null
                },
                "sort_field": {
                        "type": "string",
                        "description": "The field or fields whose values will be used to reorder the input records and the direction the records will be sorted.ASCENDING\u2014Records will be sorted from low value to high value.DESCENDING\u2014Records...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_features"
        ]
},
    "export_table": {
        "name": "export_table",
        "description": "Exports the rows of a table or table view to a new table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table containing the rows to be exported to a new table."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table containing the exported rows. If the output location is a folder, include an extension such as .csv, .txt, or .dbf to export the table to the respective format. If the output location..."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of records.  For more information on SQL syntax see the help topic SQL reference for query expressions used in ArcGIS.",
                        "default": null
                },
                "use_field_alias_name": {
                        "type": "string",
                        "description": "Specifies whether the input's field names or field aliases will be used as the output field name.NOT_USE_ALIAS\u2014The input's field names will be used as the output field names. This is the default.USE_A..."
                },
                "field_mapping": {
                        "type": "string",
                        "description": "The fields that will be transferred to the output dataset with their respective properties and source fields. The output includes all fields from the input dataset by default.Use the field map to add,...",
                        "default": null
                },
                "sort_field": {
                        "type": "string",
                        "description": "The field or fields whose values will be used to reorder the input records and the direction the records will be sorted.ASCENDING\u2014Records will be sorted from low value to high value.DESCENDING\u2014Records...",
                        "default": null
                }
        },
        "required": [
                "in_table",
                "out_table",
                "use_field_alias_name"
        ]
},
    "extract_bim_file_floorplan": {
        "name": "extract_bim_file_floorplan",
        "description": "Extracts 2.5D floor plan data from a BIM file workspace into a geodatabase dataset.",
        "parameters": {
                "in_bim_file_workspace": {
                        "type": "string",
                        "description": "The BIM file workspace that contains the building information to be extracted."
                },
                "output_workspace": {
                        "type": "string",
                        "description": "The geodatabase where the output feature dataset will be created. This  must be an existing geodatabase."
                },
                "out_feature_dataset_name": {
                        "type": "string",
                        "description": "The name of the dataset where the output feature classes will be created. If the feature dataset does not exist, it will be created with the spatial reference of the input BIM file workspace."
                },
                "out_polyline_featureclass_name": {
                        "type": "string",
                        "description": "The name of the output polyline feature class. Polyline features will be extracted into this feature class."
                },
                "out_polygon_featureclass_name": {
                        "type": "string",
                        "description": "The name of the output polygon feature class. Polygon features will be extracted into this feature class."
                },
                "out_poi_featureclass_name": {
                        "type": "string",
                        "description": "The name of the output points of interest feature class. Points of interest features will be extracted into this feature class."
                },
                "out_footprint_featureclass_name": {
                        "type": "string",
                        "description": "The name of the output footprint feature class. Footprint polygons from the BIM file workspace will be created in this feature class. The feature class will include the following categories:Merge Slab..."
                },
                "additional_polyline_categories": {
                        "type": "string",
                        "description": "The additional polyline features that will be included in the floor plan polyline feature class.  Features from the following categories can be included:\r\n FurnitureFurniture systemWindows(All)"
                },
                "additional_polygon_categories": {
                        "type": "string",
                        "description": "Specifies the additional polygon features that will be included in the floor plan polygon feature class.  Features from the following categories can be included from Revit data:\r\n AreasRoomsRoofs\r\n\r\nF..."
                },
                "included_levels": {
                        "type": "string",
                        "description": "The building level or levels of features that will be included in the output feature classes. If no building levels are provided, features from all levels will be included by default."
                }
        },
        "required": [
                "in_bim_file_workspace",
                "output_workspace",
                "out_feature_dataset_name",
                "out_polyline_featureclass_name",
                "out_polygon_featureclass_name",
                "out_poi_featureclass_name",
                "out_footprint_featureclass_name",
                "additional_polyline_categories",
                "additional_polygon_categories",
                "included_levels"
        ]
},
    "extract_locations_from_document": {
        "name": "extract_locations_from_document",
        "description": "Analyzes documents containing unstructured or semistructured text, such as email messages, travel forms, and so on, and extracts locations to a point feature class. The tool analyzes and processes the input documents as follows:Recognizes spatial coordinates specified in the content of the documents and  creates points representing these locations. The following coordinate formats are recognized: decimal degrees, degrees decimal minutes, degrees minutes seconds, Universal Transverse Mercator, and Military Grid Reference System.Recognizes place names specified in the content of the documents that are defined in a custom location file and creates points representing these locations. A custom location file associates a place name with a spatial coordinate representing that location. Recognizes text that is of interest, extracts this information from a document, and records it in fields in the output feature class's attribute table. This tool supports all Microsoft Office documents (Word, PowerPoint, and Excel); Adobe PDF documents; marked-up text such as XML and HTML documents; and any files containing plain text such as text files (.txt).",
        "parameters": {
                "in_file": {
                        "type": "string",
                        "description": "The input file that will be scanned for locations\r\n(coordinates or custom locations), dates, and custom attributes; or a folder in which all files in the folder will be scanned for locations."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing point features that represent the locations that were found."
                },
                "in_template": {
                        "type": "string",
                        "description": "The template file (*.lxttmpl) that determines the setting to use for each tool parameter. When a template file is provided, all values specified for other parameters will be ignored except those that ...",
                        "default": null
                },
                "coord_dd_latlon": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as decimal degrees formatted as latitude and longitude (infrequent false positives). Examples are: 33.8N 77.035W and W77N38.88909.FIND_DD_LATLON\u2014The ...",
                        "default": null
                },
                "coord_dd_xydeg": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as decimal degrees formatted as X Y with degree symbols (infrequent false positives). Examples are: 38.8\u00b0 -77.035\u00b0 and -077d+38.88909d.FIND_DD_XYDEG\u2014...",
                        "default": null
                },
                "coord_dd_xyplain": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as decimal degrees formatted as X Y with no symbols (frequent false positives). Examples are: 38.8 -77.035 and -077.0, +38.88909.FIND_DD_XYPLAIN\u2014The ...",
                        "default": null
                },
                "coord_dm_latlon": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees decimal minutes formatted as latitude and longitude (infrequent false positives). Examples are: 3853.3N 7702.100W and W7702N3853.3458.FIND...",
                        "default": null
                },
                "coord_dm_xymin": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees decimal minutes formatted as X Y with minutes symbols (infrequent false positives). Examples are: 3853' -7702.1' and -07702m+3853.3458m.FI...",
                        "default": null
                },
                "coord_dms_latlon": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees minutes seconds formatted as latitude and longitude (infrequent false positives). Examples are: 385320.7N 770206.000W and W770206N385320.7...",
                        "default": null
                },
                "coord_dms_xysec": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees minutes seconds formatted as X Y with seconds symbols (infrequent false positives). Examples are: 385320\" -770206.0\" and -0770206.0s+38532...",
                        "default": null
                },
                "coord_dms_xysep": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees minutes seconds formatted as X Y with separators (moderate false positives). Examples are: 8:53:20 -77:2:6.0 and -077/02/06/+38/53/20.76.F...",
                        "default": null
                },
                "coord_utm": {
                        "type": "string",
                        "description": "Specifies whether to search for Universal Transverse Mercator (UTM) coordinates (infrequent false positives). Examples are: 18S 323503 4306438 and 18 north 323503.25 4306438.39.FIND_UTM_MAINWORLD\u2014The ...",
                        "default": null
                },
                "coord_ups_north": {
                        "type": "string",
                        "description": "Specifies whether to search for Universal Polar Stereographic (UPS) coordinates in the north polar area (infrequent false positives). Examples are: Y 2722399 2000000 and north 2722399 2000000.FIND_UTM...",
                        "default": null
                },
                "coord_ups_south": {
                        "type": "string",
                        "description": "Specifies whether to search for Universal Polar Stereographic (UPS) coordinates in the south polar area (infrequent false positives). Examples are: A 2000000 3168892 and south 2000000 3168892.FIND_UTM...",
                        "default": null
                },
                "coord_mgrs": {
                        "type": "string",
                        "description": "Specifies whether to search for Military Grid Reference System (MGRS) coordinates (infrequent false positives). Examples are: 18S UJ 13503 06438 and 18SUJ0306.\r\nFIND_MGRS_MAINWORLD\u2014The tool will searc...",
                        "default": null
                },
                "coord_mgrs_northpolar": {
                        "type": "string",
                        "description": "Specifies whether to search for Military Grid Reference System (MGRS) coordinates in the north polar area (infrequent false positives). Examples are: Y TG 56814 69009 and YTG5669.FIND_MGRS_NORTHPOLAR\u2014...",
                        "default": null
                },
                "coord_mgrs_southpolar": {
                        "type": "string",
                        "description": "Specifies whether to search for Military Grid Reference System (MGRS) coordinates in the south polar area (moderate false positives). Examples are: A TN 56814 30991 and ATN5630.FIND_MGRS_SOUTHPOLAR\u2014Th...",
                        "default": null
                },
                "comma_decimal": {
                        "type": "string",
                        "description": "Specifies whether a comma (,) will be recognized as a decimal separator. By default, content is scanned for\r\nspatial coordinates defined by numbers that use a period (.) or a middle dot (\u00b7) as the dec...",
                        "default": null
                },
                "coord_use_lonlat": {
                        "type": "string",
                        "description": "When numbers resemble x,y coordinates, both numbers are less than 90, and there are no symbols or notations to indicate which number represents the latitude or longitude, results can be ambiguous. Int...",
                        "default": null
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The coordinate system that will be used to interpret the spatial coordinates defined in the input. GCS-WGS-84 is the default.",
                        "default": null
                },
                "in_custom_locations": {
                        "type": "string",
                        "description": "The custom location file (.lxtgaz) that will be used when scanning the input content. A point is created to represent each occurrence of each place name in the custom location file up to the limits es...",
                        "default": null
                },
                "fuzzy_match": {
                        "type": "string",
                        "description": "Specifies whether fuzzy matching will be used for searching the custom location file.USE_FUZZY\u2014Fuzzy matching will be used when searching the custom location file.DONT_USE_FUZZY\u2014Exact matching will be...",
                        "default": null
                },
                "max_features_extracted": {
                        "type": "string",
                        "description": "The maximum number of features that can be extracted. The tool will stop scanning the input content for locations when the maximum number is reached. When running as a geoprocessing service, the servi...",
                        "default": null
                },
                "ignore_first_features": {
                        "type": "string",
                        "description": "The number of features detected and ignored before extracting all other features. This parameter can be used to focus the search on a specific portion of the data.",
                        "default": null
                },
                "date_monthname": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which the month name appears (infrequent false positives). 12 May 2003 and January 15, 1997 are examples.FIND_DATE_MONTHNAME\u2014The tool will search for dates in ...",
                        "default": null
                },
                "date_m_d_y": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the M/D/Y or D/M/Y format (moderate false positives). 5/12/03 and 1-15-1997 are examples.FIND_DATE_M_D_Y\u2014The tool will search for dates in...",
                        "default": null
                },
                "date_yyyymmdd": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the YYYYMMDD format (moderate false positives). 20030512 and 19970115 are examples.FIND_DATE_YYYYMMDD\u2014The tool will search for dates in wh...",
                        "default": null
                },
                "date_yymmdd": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the YYMMDD format (frequent false positives). 030512 and 970115 are examples.FIND_DATE_YYMMDD\u2014The tool will search for dates in which numb...",
                        "default": null
                },
                "date_yyjjj": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the YYJJJ or YYYYJJJ format (frequent false positives). 03132 and 97015 are examples.FIND_DATE_YYJJJ\u2014The tool will search for dates in whi...",
                        "default": null
                },
                "max_dates_extracted": {
                        "type": "string",
                        "description": "The maximum number of dates that will be extracted.",
                        "default": null
                },
                "ignore_first_dates": {
                        "type": "string",
                        "description": "The number of dates that will be detected and ignored before extracting all other dates.",
                        "default": null
                },
                "date_range_begin": {
                        "type": "string",
                        "description": "The earliest acceptable date to extract. Detected dates matching this value or later will be extracted.",
                        "default": null
                },
                "date_range_end": {
                        "type": "string",
                        "description": "The latest acceptable date to extract. Detected dates matching this value or earlier will be extracted.",
                        "default": null
                },
                "in_custom_attributes": {
                        "type": "string",
                        "description": "The custom attribute file (.lxtca) that will be used to scan the input content. Fields will be created in the output feature class's attribute table for all custom attributes defined in the file. When...",
                        "default": null
                },
                "file_link": {
                        "type": "string",
                        "description": "The file path that will be used as the file name in the output data when the Input File parameter (in_file in Python) is transferred to the server. If this parameter is not specified, the path of the ...",
                        "default": null
                },
                "file_mod_datetime": {
                        "type": "string",
                        "description": "The UTC date and time that the file was modified will be used as the modified attribute in the output data when the Input File parameter (in_file in Python) is transferred to the server. If this param...",
                        "default": null
                },
                "pre_text_length": {
                        "type": "string",
                        "description": "Content is extracted from the input document to provide context for the location that was found. This parameter defines the maximum number of characters that will be extracted preceding the text that ...",
                        "default": null
                },
                "post_text_length": {
                        "type": "string",
                        "description": "Content is extracted from the input document to provide context for the location that was found. This parameter defines the maximum number of characters that will be extracted following the text that ...",
                        "default": null
                },
                "std_coord_fmt": {
                        "type": "string",
                        "description": "Specifies the coordinate format that will be used to store the coordinate location. A standard representation of the spatial coordinate that defines the point feature is recorded in a field in the att...",
                        "default": null
                },
                "req_word_breaks": {
                        "type": "string",
                        "description": "Specifies whether to search for text using word breaks. A word break occurs when words (text) are bounded by whitespace or punctuation characters as in European languages. This setting can produce fre...",
                        "default": null
                }
        },
        "required": [
                "in_file",
                "out_feature_class"
        ]
},
    "extract_locations_from_text": {
        "name": "extract_locations_from_text",
        "description": "Analyzes input text or a text file and extracts locations to a point feature class. If the input text is a file path, the identified file will be opened and its content will be analyzed. If the input text is unstructured information such as an email message, or semistructured text such as a travel forms, the input text itself will be analyzed. The tool extracts locations found in the text or in the content of the file and adds the resulting points to a feature class. The tool analyzes and processes the text as follows:Recognizes spatial coordinates specified in the content of the text and  creates points representing these locations. The following coordinate formats are recognized: decimal degrees, degrees decimal minutes, degrees minutes seconds, Universal Transverse Mercator, and Military Grid Reference System.Recognizes place names specified in the text that are defined in a custom location file and creates points representing these locations. A custom location file associates a place name with a spatial coordinate representing that location. Recognizes text that is of interest, extracts this information from the text provided, and records it in fields in the output feature class's attribute table.",
        "parameters": {
                "in_text": {
                        "type": "string",
                        "description": "The text that will be scanned for locations (coordinates or custom locations), dates, and custom attributes; or text defining a file path, whose contents will be scanned for locations. For geoprocessi..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing point features that represent the locations that were found."
                },
                "in_template": {
                        "type": "string",
                        "description": "The template file (*.lxttmpl) that determines the setting to use for each tool parameter. When a template file is provided, all values specified for other parameters will be ignored except those that ...",
                        "default": null
                },
                "coord_dd_latlon": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as decimal degrees formatted as latitude and longitude (infrequent false positives). Examples are: 33.8N 77.035W and W77N38.88909.FIND_DD_LATLON\u2014The ...",
                        "default": null
                },
                "coord_dd_xydeg": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as decimal degrees formatted as X Y with degree symbols (infrequent false positives). Examples are: 38.8\u00b0 -77.035\u00b0 and -077d+38.88909d.FIND_DD_XYDEG\u2014...",
                        "default": null
                },
                "coord_dd_xyplain": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as decimal degrees formatted as X Y with no symbols (frequent false positives). Examples are: 38.8 -77.035 and -077.0, +38.88909.FIND_DD_XYPLAIN\u2014The ...",
                        "default": null
                },
                "coord_dm_latlon": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees decimal minutes formatted as latitude and longitude (infrequent false positives). Examples are: 3853.3N 7702.100W and W7702N3853.3458.FIND...",
                        "default": null
                },
                "coord_dm_xymin": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees decimal minutes formatted as X Y with minutes symbols (infrequent false positives). Examples are: 3853' -7702.1' and -07702m+3853.3458m.FI...",
                        "default": null
                },
                "coord_dms_latlon": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees minutes seconds formatted as latitude and longitude (infrequent false positives). Examples are: 385320.7N 770206.000W and W770206N385320.7...",
                        "default": null
                },
                "coord_dms_xysec": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees minutes seconds formatted as X Y with seconds symbols (infrequent false positives). Examples are: 385320\" -770206.0\" and -0770206.0s+38532...",
                        "default": null
                },
                "coord_dms_xysep": {
                        "type": "string",
                        "description": "Specifies whether to search for coordinates stored as degrees minutes seconds formatted as X Y with separators (moderate false positives). Examples are: 8:53:20 -77:2:6.0 and -077/02/06/+38/53/20.76.F...",
                        "default": null
                },
                "coord_utm": {
                        "type": "string",
                        "description": "Specifies whether to search for Universal Transverse Mercator (UTM) coordinates (infrequent false positives). Examples are: 18S 323503 4306438 and 18 north 323503.25 4306438.39.FIND_UTM_MAINWORLD\u2014The ...",
                        "default": null
                },
                "coord_ups_north": {
                        "type": "string",
                        "description": "Specifies whether to search for Universal Polar Stereographic (UPS) coordinates in the north polar area (infrequent false positives). Examples are: Y 2722399 2000000 and north 2722399 2000000.FIND_UTM...",
                        "default": null
                },
                "coord_ups_south": {
                        "type": "string",
                        "description": "Specifies whether to search for Universal Polar Stereographic (UPS) coordinates in the south polar area (infrequent false positives). Examples are: A 2000000 3168892 and south 2000000 3168892.FIND_UTM...",
                        "default": null
                },
                "coord_mgrs": {
                        "type": "string",
                        "description": "Specifies whether to search for Military Grid Reference System (MGRS) coordinates (infrequent false positives). Examples are: 18S UJ 13503 06438 and 18SUJ0306.\r\nFIND_MGRS_MAINWORLD\u2014The tool will searc...",
                        "default": null
                },
                "coord_mgrs_northpolar": {
                        "type": "string",
                        "description": "Specifies whether to search for Military Grid Reference System (MGRS) coordinates in the north polar area (infrequent false positives). Examples are: Y TG 56814 69009 and YTG5669.FIND_MGRS_NORTHPOLAR\u2014...",
                        "default": null
                },
                "coord_mgrs_southpolar": {
                        "type": "string",
                        "description": "Specifies whether to search for Military Grid Reference System (MGRS) coordinates in the south polar area (moderate false positives). Examples are: A TN 56814 30991 and ATN5630.FIND_MGRS_SOUTHPOLAR\u2014Th...",
                        "default": null
                },
                "comma_decimal": {
                        "type": "string",
                        "description": "Specifies whether a comma (,) will be recognized as a decimal separator. By default, content is scanned for\r\nspatial coordinates defined by numbers that use a period (.) or a middle dot (\u00b7) as the dec...",
                        "default": null
                },
                "coord_use_lonlat": {
                        "type": "string",
                        "description": "When numbers resemble x,y coordinates, both numbers are less than 90, and there are no symbols or notations to indicate which number represents the latitude or longitude, results can be ambiguous. Int...",
                        "default": null
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The coordinate system that will be used to interpret the spatial coordinates defined in the input. GCS-WGS-84 is the default.",
                        "default": null
                },
                "in_custom_locations": {
                        "type": "string",
                        "description": "The custom location file (.lxtgaz) that will be used when scanning the input content. A point is created to represent each occurrence of each place name in the custom location file up to the limits es...",
                        "default": null
                },
                "fuzzy_match": {
                        "type": "string",
                        "description": "Specifies whether fuzzy matching will be used for searching the custom location file.USE_FUZZY\u2014Fuzzy matching will be used when searching the custom location file.DONT_USE_FUZZY\u2014Exact matching will be...",
                        "default": null
                },
                "max_features_extracted": {
                        "type": "string",
                        "description": "The maximum number of features that can be extracted. The tool will stop scanning the input content for locations when the maximum number is reached. When running as a geoprocessing service, the servi...",
                        "default": null
                },
                "ignore_first_features": {
                        "type": "string",
                        "description": "The number of features detected and ignored before extracting all other features. This parameter can be used to focus the search on a specific portion of the data.",
                        "default": null
                },
                "date_monthname": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which the month name appears (infrequent false positives). 12 May 2003 and January 15, 1997 are examples.FIND_DATE_MONTHNAME\u2014The tool will search for dates in ...",
                        "default": null
                },
                "date_m_d_y": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the M/D/Y or D/M/Y format (moderate false positives). 5/12/03 and 1-15-1997 are examples.FIND_DATE_M_D_Y\u2014The tool will search for dates in...",
                        "default": null
                },
                "date_yyyymmdd": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the YYYYMMDD format (moderate false positives). 20030512 and 19970115 are examples.FIND_DATE_YYYYMMDD\u2014The tool will search for dates in wh...",
                        "default": null
                },
                "date_yymmdd": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the YYMMDD format (frequent false positives). 030512 and 970115 are examples.FIND_DATE_YYMMDD\u2014The tool will search for dates in which numb...",
                        "default": null
                },
                "date_yyjjj": {
                        "type": "string",
                        "description": "Specifies whether to search for dates in which numbers are in the YYJJJ or YYYYJJJ format (frequent false positives). 03132 and 97015 are examples.FIND_DATE_YYJJJ\u2014The tool will search for dates in whi...",
                        "default": null
                },
                "max_dates_extracted": {
                        "type": "string",
                        "description": "The maximum number of dates that will be extracted.",
                        "default": null
                },
                "ignore_first_dates": {
                        "type": "string",
                        "description": "The number of dates that will be detected and ignored before extracting all other dates.",
                        "default": null
                },
                "date_range_begin": {
                        "type": "string",
                        "description": "The earliest acceptable date to extract. Detected dates matching this value or later will be extracted.",
                        "default": null
                },
                "date_range_end": {
                        "type": "string",
                        "description": "The latest acceptable date to extract. Detected dates matching this value or earlier will be extracted.",
                        "default": null
                },
                "in_custom_attributes": {
                        "type": "string",
                        "description": "The custom attribute file (.lxtca) that will be used to scan the input content. Fields will be created in the output feature class's attribute table for all custom attributes defined in the file. When...",
                        "default": null
                },
                "file_link": {
                        "type": "string",
                        "description": "The file path that will be used as the file name in the output data when the Input File parameter (in_file in Python) is transferred to the server. If this parameter is not specified, the path of the ...",
                        "default": null
                },
                "file_mod_datetime": {
                        "type": "string",
                        "description": "The UTC date and time that the file was modified will be used as the modified attribute in the output data when the Input File parameter (in_file in Python) is transferred to the server. If this param...",
                        "default": null
                },
                "pre_text_length": {
                        "type": "string",
                        "description": "Content is extracted from the input document to provide context for the location that was found. This parameter defines the maximum number of characters that will be extracted preceding the text that ...",
                        "default": null
                },
                "post_text_length": {
                        "type": "string",
                        "description": "Content is extracted from the input document to provide context for the location that was found. This parameter defines the maximum number of characters that will be extracted following the text that ...",
                        "default": null
                },
                "std_coord_fmt": {
                        "type": "string",
                        "description": "Specifies the coordinate format that will be used to store the coordinate location. A standard representation of the spatial coordinate that defines the point feature is recorded in a field in the att...",
                        "default": null
                },
                "req_word_breaks": {
                        "type": "string",
                        "description": "Specifies whether to search for text using word breaks. A word break occurs when words (text) are bounded by whitespace or punctuation characters as in European languages. This setting can produce fre...",
                        "default": null
                }
        },
        "required": [
                "in_text",
                "out_feature_class"
        ]
},
    "feature_class_to_geodatabase": {
        "name": "feature_class_to_geodatabase",
        "description": "Converts one or more feature classes or feature layers to geodatabase feature classes.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "One or more feature classes or feature layers that will be imported into a geodatabase."
                },
                "output_geodatabase": {
                        "type": "string",
                        "description": "The output or destination geodatabase."
                }
        },
        "required": [
                "input_features",
                "output_geodatabase"
        ]
},
    "mobile_geodatabase_to_file_geodatabase": {
        "name": "mobile_geodatabase_to_file_geodatabase",
        "description": "Copies the contents of a mobile geodatabase to a new file geodatabase.",
        "parameters": {
                "in_mobile_gdb": {
                        "type": "string",
                        "description": "The mobile geodatabase with the contents that will be copied to a new file geodatabase."
                },
                "out_file_gdb": {
                        "type": "string",
                        "description": "The name and location of the output file geodatabase, for example, c:\\temp\\outputGeodatabases\\copiedFGDB.gdb."
                }
        },
        "required": [
                "in_mobile_gdb",
                "out_file_gdb"
        ]
},
    "raster_to_geodatabase": {
        "name": "raster_to_geodatabase",
        "description": "Loads raster datasets into a geodatabase.",
        "parameters": {
                "input_rasters": {
                        "type": "string",
                        "description": "The input raster datasets."
                },
                "output_geodatabase": {
                        "type": "string",
                        "description": "The output or destination geodatabase."
                },
                "configuration_keyword": {
                        "type": "string",
                        "description": "The storage parameters (configuration) for a geodatabase. Configuration keywords are set up by your database administrator.",
                        "default": null
                }
        },
        "required": [
                "input_rasters",
                "output_geodatabase"
        ]
},
    "table_to_geodatabase": {
        "name": "table_to_geodatabase",
        "description": "Converts one or more tables to geodatabase tables in an output geodatabase.",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "The list of tables that will be converted to geodatabase tables. Input tables can be INFO, dBASE, OLE DB, geodatabase tables, or table views."
                },
                "output_geodatabase": {
                        "type": "string",
                        "description": "The destination geodatabase where the tables will be placed."
                }
        },
        "required": [
                "input_table",
                "output_geodatabase"
        ]
},
    "add_raster_to_geopackage": {
        "name": "add_raster_to_geopackage",
        "description": "Loads raster datasets into an OGC GeoPackage raster pyramid.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The raster dataset to load into the OGC GeoPackage raster pyramid."
                },
                "target_geopackage": {
                        "type": "string",
                        "description": "The GeoPackage into which the raster dataset will be loaded."
                },
                "raster_name": {
                        "type": "string",
                        "description": "The name of the output GeoPackage raster pyramid."
                },
                "tiling_scheme": {
                        "type": "string",
                        "description": "Specifies the tiling scheme.TILED\u2014The spatial reference of the input raster will be maintained and tiles will be generated consistent with the GeoPackage standard. This is the default.ARCGISONLINE_SCH...",
                        "default": null
                },
                "tiling_scheme_file": {
                        "type": "string",
                        "description": "A custom tiling scheme file that is required when tiling_scheme is set to FROM_FILE.",
                        "default": null
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "An area of interest used to limit the area of the raster to be loaded, rather than the entire dataset.",
                        "default": null
                }
        },
        "required": [
                "in_dataset",
                "target_geopackage",
                "raster_name"
        ]
},
    "feature_to_raster": {
        "name": "feature_to_raster",
        "description": "Converts features to a raster dataset.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature dataset to be converted to a raster dataset."
                },
                "field": {
                        "type": "string",
                        "description": "The field used to assign values to the output raster.It can be any field of the input feature dataset's attribute table.If the Shape field of a point or multipoint dataset contains z- or m-values, eit..."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset to be created.If the output raster will not be saved to a geodatabase, specify .tif for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE file format, or no ..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster being created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn\u2019t been explicitly specified as the ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "field",
                "out_raster"
        ]
},
    "multipatch_to_raster": {
        "name": "multipatch_to_raster",
        "description": "Converts multipatch features to a raster dataset.",
        "parameters": {
                "in_multipatch_features": {
                        "type": "string",
                        "description": "The input multipatch features to be converted to a raster."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset to be created.It will be of floating point type.If the output raster will not be saved to a geodatabase, specify .tif for TIFF file format, .CRF for CRF file format, .img for..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster being created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn\u2019t been explicitly specified as the ...",
                        "default": null
                },
                "cell_assignment_method": {
                        "type": "string",
                        "description": "Specifies whether the maximum or minimum z-value will be used for a cell when more than one z-value is detected at the cell center location when a vertical line is extended from the cell center locati...",
                        "default": null
                }
        },
        "required": [
                "in_multipatch_features",
                "out_raster"
        ]
},
    "point_to_raster": {
        "name": "point_to_raster",
        "description": "Converts point features to a raster dataset. Learn how the Point to Raster tool works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point or multipoint input feature dataset to be converted to a raster."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field used to assign values to the output raster.It can be any field of the input feature dataset's attribute table.If the Shape field of a point or multipoint dataset contains z- or m-values, eit..."
                },
                "out_rasterdataset": {
                        "type": "string",
                        "description": "The output raster dataset to be created.If the output raster will not be saved to a geodatabase, specify .tif for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE file format, or no ..."
                },
                "cell_assignment": {
                        "type": "string",
                        "description": "The method to determine how the cell will be assigned a value when more than one feature falls within a cell.MOST_FREQUENT\u2014If there is more than one feature within the cell, the one with the most comm...",
                        "default": null
                },
                "priority_field": {
                        "type": "string",
                        "description": "This field is used when a feature should take preference over another feature with the same attribute.Priority field is only used with the Most frequent cell assignment type option.",
                        "default": null
                },
                "cellsize": {
                        "type": "string",
                        "description": "The cell size of the output raster being created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn\u2019t been explicitly specified as the ...",
                        "default": null
                },
                "build_rat": {
                        "type": "string",
                        "description": "Specifies whether the output raster will have a raster attribute table.This parameter only applies to integer rasters.BUILD\u2014The output raster will have a raster attribute table. This is the default.DO...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "value_field",
                "out_rasterdataset"
        ]
},
    "polygon_to_raster": {
        "name": "polygon_to_raster",
        "description": "Converts polygon features to a raster dataset. Learn how the Polygon to Raster tool works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polygon input feature dataset to be converted to a raster."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field used to assign values to the output raster.It can be any field of the input feature dataset's attribute table."
                },
                "out_rasterdataset": {
                        "type": "string",
                        "description": "The output raster dataset to be created.If the output raster will not be saved to a geodatabase, specify .tif for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE file format, or no ..."
                },
                "cell_assignment": {
                        "type": "string",
                        "description": "The method to determine how the cell will be assigned a value when more than one feature falls within a cell.CELL_CENTER\u2014The polygon that overlaps the center of the cell yields the attribute to assign...",
                        "default": null
                },
                "priority_field": {
                        "type": "string",
                        "description": "This field is used to determine which feature should take preference over another feature that falls over a cell. When it is used, the feature with the largest positive priority is always selected for...",
                        "default": null
                },
                "cellsize": {
                        "type": "string",
                        "description": "The cell size of the output raster being created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn\u2019t been explicitly specified as the ...",
                        "default": null
                },
                "build_rat": {
                        "type": "string",
                        "description": "Specifies whether the output raster will have a raster attribute table.This parameter only applies to integer rasters.BUILD\u2014The output raster will have a raster attribute table. This is the default.DO...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "value_field",
                "out_rasterdataset"
        ]
},
    "polyline_to_raster": {
        "name": "polyline_to_raster",
        "description": "Converts polyline features to a raster dataset. Learn more about how the Polyline to Raster tool works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polyline input feature dataset to be converted to a raster."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field used to assign values to the output raster.It can be any field of the input feature dataset's attribute table."
                },
                "out_rasterdataset": {
                        "type": "string",
                        "description": "The output raster dataset to be created.If the output raster will not be saved to a geodatabase, specify .tif for TIFF file format, .CRF for CRF file format, .img for ERDAS IMAGINE file format, or no ..."
                },
                "cell_assignment": {
                        "type": "string",
                        "description": "The method to determine how the cell will be assigned a value when more than one feature falls within a cell.MAXIMUM_LENGTH\u2014The feature with the longest length that covers the cell will determine the ...",
                        "default": null
                },
                "priority_field": {
                        "type": "string",
                        "description": "This field is used to determine which feature should take preference over another feature that falls over a cell. When it is used, the feature with the largest positive priority is always selected for...",
                        "default": null
                },
                "cellsize": {
                        "type": "string",
                        "description": "The cell size of the output raster being created.This parameter can be defined by a numeric value or obtained from an existing raster dataset. If the cell size hasn\u2019t been explicitly specified as the ...",
                        "default": null
                },
                "build_rat": {
                        "type": "string",
                        "description": "Specifies whether the output raster will have a raster attribute table.This parameter only applies to integer rasters.BUILD\u2014The output raster will have a raster attribute table. This is the default.DO...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "value_field",
                "out_rasterdataset"
        ]
},
    "raster_to_other_format": {
        "name": "raster_to_other_format",
        "description": "Converts one or more raster datasets to a different format.",
        "parameters": {
                "input_rasters": {
                        "type": "string",
                        "description": "The raster datasets  to convert."
                },
                "output_workspace": {
                        "type": "string",
                        "description": "The folder where the raster dataset will be written."
                },
                "raster_format": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the output raster dataset.BIL\u2014The output will be Esri BIL format.BIP\u2014The output will be Esri BIP format.BMP\u2014The output will be Microsoft BMP format.BSQ\u2014The o...",
                        "default": null
                }
        },
        "required": [
                "input_rasters",
                "output_workspace"
        ]
},
    "feature_class_to_shapefile": {
        "name": "feature_class_to_shapefile",
        "description": "Converts the features from one or more feature classes or feature layers to shapefiles and adds them to a folder of shapefiles.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The list of input feature classes or feature layers that will be converted and added to the output folder."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The folder where the shapefiles will be written."
                }
        },
        "required": [
                "input_features",
                "output_folder"
        ]
}
}
