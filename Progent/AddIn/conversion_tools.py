# Generated ArcGIS Pro conversion Progent Functions
# Corrected on 2025-10-02
# Total tools: 47 (after removing duplicates)

import arcpy
import os

class ConversionTools:
    """Corrected conversion functions for ArcGIS Pro"""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def excel_to_table(self, params):
        """Excel To Table

Converts Microsoft Excel files into a table.

        params: {"input_excel_file": <File>, "output_table": <Table>, "sheet": <String>, "field_names_row": <Long>, "cell_range": <String>}
        Returns: {"success": True, "output_path": <output_path>} or error
        """
        try:
            input_excel_file = params.get("input_excel_file")
            if input_excel_file is None:
                return {"success": False, "error": "input_excel_file parameter is required"}
            output_table = params.get("output_table")
            if output_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                output_name = f"{os.path.basename(input_excel_file).split('.')[0]}_Excel_To_Table"
                output_table = arcpy.CreateUniqueName(output_name, aprx.defaultGeodatabase)

            sheet = params.get("sheet")
            field_names_row = params.get("field_names_row", 1)
            cell_range = params.get("cell_range")

            arcpy.conversion.ExcelToTable(input_excel_file, output_table, sheet, field_names_row, cell_range)

            self._add_to_map(output_table)
            return {"success": True, "output_path": output_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def table_to_excel(self, params):
        """Table To Excel

Converts a table to a Microsoft Excel file (.xls or .xlsx).

        params: {"input_table": <Table View>, "output_excel_file": <File>, "use_field_alias_column_header": <Boolean>, "use_domain_and_subtype_description": <Boolean>}
        Returns: {"success": True, "output_path": <output_path>} or error
        """
        try:
            input_table = params.get("input_table")
            if input_table is None:
                return {"success": False, "error": "input_table parameter is required"}
            output_excel_file = params.get("output_excel_file")
            if output_excel_file is None:
                return {"success": False, "error": "output_excel_file parameter is required"}

            use_field_alias_column_header = params.get("use_field_alias_column_header", "NAME")
            use_domain_and_subtype_description = params.get("use_domain_and_subtype_description", "CODE")

            arcpy.conversion.TableToExcel(input_table, output_excel_file, use_field_alias_column_header, use_domain_and_subtype_description)

            return {"success": True, "output_path": output_excel_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def pdf_to_tiff(self, params):
        """PDF To TIFF

Exports a .pdf file to Tagged Image File Format (TIFF).

        params: {"in_pdf_file": <File>, "out_tiff_file": <Raster Dataset>, ...}
        Returns: {"success": True, "output_path": <output_path>} or error
        """
        try:
            in_pdf_file = params.get("in_pdf_file")
            if in_pdf_file is None:
                return {"success": False, "error": "in_pdf_file parameter is required"}
            out_tiff_file = params.get("out_tiff_file")
            if out_tiff_file is None:
                return {"success": False, "error": "out_tiff_file parameter is required"}

            pdf_password = params.get("pdf_password")
            pdf_page_number = params.get("pdf_page_number", 1)
            pdf_map = params.get("pdf_map")
            clip_option = params.get("clip_option", "CLIP_TO_MAP")
            resolution = params.get("resolution", 250)
            color_mode = params.get("color_mode", "RGB_TRUE_COLOR")
            tiff_compression = params.get("tiff_compression", "LZW")
            geotiff_tags = params.get("geotiff_tags", "True")

            arcpy.conversion.PDFToTIFF(in_pdf_file, out_tiff_file, pdf_password, pdf_page_number, pdf_map, clip_option, resolution, color_mode, tiff_compression, geotiff_tags)

            self._add_to_map(out_tiff_file)
            return {"success": True, "output_path": out_tiff_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_ascii(self, params):
        """Raster to ASCII

Converts a raster dataset to an ASCII file representing raster data.
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None: return {"success": False, "error": "in_raster parameter is required"}
            out_ascii_file = params.get("out_ascii_file")
            if out_ascii_file is None: return {"success": False, "error": "out_ascii_file parameter is required"}

            arcpy.conversion.RasterToASCII(in_raster, out_ascii_file)

            return {"success": True, "output_path": out_ascii_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_float(self, params):
        """Raster to Float

Converts a raster dataset to a file of binary floating-point values representing raster data.
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None: return {"success": False, "error": "in_raster parameter is required"}
            out_float_file = params.get("out_float_file")
            if out_float_file is None: return {"success": False, "error": "out_float_file parameter is required"}

            arcpy.conversion.RasterToFloat(in_raster, out_float_file)

            return {"success": True, "output_path": out_float_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_point(self, params):
        """Raster to Point

Converts a raster dataset to point features.
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None: return {"success": False, "error": "in_raster parameter is required"}
            out_point_features = params.get("out_point_features")
            if out_point_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_point_features = arcpy.CreateUniqueName("RasterToPoint_Output", aprx.defaultGeodatabase)
            raster_field = params.get("raster_field", "VALUE")

            arcpy.conversion.RasterToPoint(in_raster, out_point_features, raster_field)

            self._add_to_map(out_point_features)
            return {"success": True, "output_path": out_point_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_polygon(self, params):
        """Raster to Polygon

Converts a raster dataset to polygon features.
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None: return {"success": False, "error": "in_raster parameter is required"}
            out_polygon_features = params.get("out_polygon_features")
            if out_polygon_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_polygon_features = arcpy.CreateUniqueName("RasterToPolygon_Output", aprx.defaultGeodatabase)

            simplify = params.get("simplify", "SIMPLIFY")
            raster_field = params.get("raster_field", "VALUE")
            create_multipart_features = params.get("create_multipart_features", "MULTIPLE_OUTER_PART")
            max_vertices_per_feature = params.get("max_vertices_per_feature")

            arcpy.conversion.RasterToPolygon(in_raster, out_polygon_features, simplify, raster_field, create_multipart_features, max_vertices_per_feature)

            self._add_to_map(out_polygon_features)
            return {"success": True, "output_path": out_polygon_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_polyline(self, params):
        """Raster to Polyline

Converts a raster dataset to polyline features.
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None: return {"success": False, "error": "in_raster parameter is required"}
            out_polyline_features = params.get("out_polyline_features")
            if out_polyline_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_polyline_features = arcpy.CreateUniqueName("RasterToPolyline_Output", aprx.defaultGeodatabase)

            background_value = params.get("background_value", "ZERO")
            minimum_dangle_length = params.get("minimum_dangle_length")
            simplify = params.get("simplify", "SIMPLIFY")
            raster_field = params.get("raster_field", "VALUE")

            arcpy.conversion.RasterToPolyline(in_raster, out_polyline_features, background_value, minimum_dangle_length, simplify, raster_field)

            self._add_to_map(out_polyline_features)
            return {"success": True, "output_path": out_polyline_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def wfs_to_feature_class(self, params):
        """WFS To Feature Class

Imports a feature type from a Web Feature Service (WFS) to a feature class in a geodatabase.
        """
        try:
            input_wfs_server = params.get("input_wfs_server")
            if input_wfs_server is None: return {"success": False, "error": "input_wfs_server parameter is required"}
            wfs_feature_type = params.get("wfs_feature_type")
            if wfs_feature_type is None: return {"success": False, "error": "wfs_feature_type parameter is required"}
            out_path = params.get("out_path")
            if out_path is None: return {"success": False, "error": "out_path parameter is required"}
            out_name = params.get("out_name")
            if out_name is None: return {"success": False, "error": "out_name parameter is required"}

            is_complex = params.get("is_complex", "SIMPLE")
            max_features = params.get("max_features")
            expose_metadata = params.get("expose_metadata", "NO_EXPOSE_METADATA")
            swap_xy = params.get("swap_xy", "NO_SWAP_XY")
            page_size = params.get("page_size", 1000)

            result = arcpy.conversion.WFSToFeatureClass(input_wfs_server, wfs_feature_type, out_path, out_name, is_complex, max_features, expose_metadata, swap_xy, page_size)

            output_path = result.getOutput(0)
            self._add_to_map(output_path)
            return {"success": True, "output_path": output_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def gpx_to_features(self, params):
        """GPX To Features

Converts the point data in a .gpx file to features.
        """
        try:
            input_gpx_file = params.get("input_gpx_file")
            if input_gpx_file is None: return {"success": False, "error": "input_gpx_file parameter is required"}
            output_feature_class = params.get("output_feature_class")
            if output_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                output_feature_class = arcpy.CreateUniqueName("GPXToFeatures_Output", aprx.defaultGeodatabase)

            output_type = params.get("output_type", "GPX_POINTS")

            arcpy.conversion.GPXToFeatures(input_gpx_file, output_feature_class, output_type)

            self._add_to_map(output_feature_class)
            return {"success": True, "output_path": output_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def features_to_graphics(self, params):
        """Features To Graphics

Converts a feature layer's symbolized features into graphic elements in a graphics layer.
        """
        try:
            in_layer = params.get("in_layer")
            if in_layer is None: return {"success": False, "error": "in_layer parameter is required"}
            out_layer = params.get("out_layer")
            if out_layer is None: return {"success": False, "error": "out_layer parameter is required"}
            exclude_features = params.get("exclude_features", "EXCLUDE")

            arcpy.conversion.FeaturesToGraphics(in_layer, out_layer, exclude_features)

            return {"success": True, "output_path": out_layer}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def graphics_to_features(self, params):
        """Graphics To Features

Converts a graphics layer into a feature layer with geometries based on the input graphics layer's elements.
        """
        try:
            in_layer = params.get("in_layer")
            if in_layer is None: return {"success": False, "error": "in_layer parameter is required"}
            graphics_type = params.get("graphics_type")
            if graphics_type is None: return {"success": False, "error": "graphics_type parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GraphicsToFeatures_Output", aprx.defaultGeodatabase)

            delete_graphics = params.get("delete_graphics", "DELETE_GRAPHICS")
            reference_scale = params.get("reference_scale")

            arcpy.conversion.GraphicsToFeatures(in_layer, graphics_type, out_feature_class, delete_graphics, reference_scale)

            self._add_to_map(out_feature_class)
            return {"success": True, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def features_to_json(self, params):
        """Features To JSON

Converts features to Esri JSON or GeoJSON format.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_json_file = params.get("out_json_file")
            if out_json_file is None: return {"success": False, "error": "out_json_file parameter is required"}

            format_json = params.get("format_json", "FORMATTED")
            include_z_values = params.get("include_z_values", "INCLUDE_Z_VALUES")
            include_m_values = params.get("include_m_values", "INCLUDE_M_VALUES")
            geojson = params.get("geojson", "NO_GEOJSON")
            output_to_wgs84 = params.get("output_to_wgs84", "NO_WGS84")
            use_field_alias = params.get("use_field_alias", "NO_FIELD_ALIAS")

            arcpy.conversion.FeaturesToJSON(in_features, out_json_file, format_json, include_z_values, include_m_values, geojson, output_to_wgs84, use_field_alias)

            return {"success": True, "output_path": out_json_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def json_to_features(self, params):
        """JSON To Features

Converts feature collections in an Esri JSON or GeoJSON formatted file to a feature class.
        """
        try:
            in_json_file = params.get("in_json_file")
            if in_json_file is None: return {"success": False, "error": "in_json_file parameter is required"}
            out_features = params.get("out_features")
            if out_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_features = arcpy.CreateUniqueName("JSONToFeatures_Output", aprx.defaultGeodatabase)

            geometry_type = params.get("geometry_type")

            arcpy.conversion.JSONToFeatures(in_json_file, out_features, geometry_type)

            self._add_to_map(out_features)
            return {"success": True, "output_path": out_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def kml_to_layer(self, params):
        """KML To Layer

Converts a .kml or .kmz file into datasets in a geodatabase and a layer file.
        """
        try:
            in_kml_file = params.get("in_kml_file")
            if in_kml_file is None: return {"success": False, "error": "in_kml_file parameter is required"}
            output_folder = params.get("output_folder")
            if output_folder is None: return {"success": False, "error": "output_folder parameter is required"}

            output_data = params.get("output_data")
            include_groundoverlay = params.get("include_groundoverlay", "GROUNDOVERLAY")

            result = arcpy.conversion.KMLToLayer(in_kml_file, output_folder, output_data, include_groundoverlay)

            output_path = result.getOutput(0)
            self._add_to_map(output_path)
            return {"success": True, "output_path": output_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def layer_to_kml(self, params):
        """Layer To KML

Converts a feature or raster layer to KML format.
        """
        try:
            layer = params.get("layer")
            if layer is None: return {"success": False, "error": "layer parameter is required"}
            out_kmz_file = params.get("out_kmz_file")
            if out_kmz_file is None: return {"success": False, "error": "out_kmz_file parameter is required"}

            layer_output_scale = params.get("layer_output_scale", 1)
            is_composite = params.get("is_composite", "NO_COMPOSITE")
            boundary_box_extent = params.get("boundary_box_extent")
            image_size = params.get("image_size", 1024)
            dpi_of_client = params.get("dpi_of_client", 96)
            ignore_zvalue = params.get("ignore_zvalue", "ABSOLUTE")

            arcpy.conversion.LayerToKML(layer, out_kmz_file, layer_output_scale, is_composite, boundary_box_extent, image_size, dpi_of_client, ignore_zvalue)

            return {"success": True, "output_path": out_kmz_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def map_to_kml(self, params):
        """Map To KML

Converts a map to KML format.
        """
        try:
            in_map = params.get("in_map")
            if in_map is None: return {"success": False, "error": "in_map parameter is required"}
            out_kmz_file = params.get("out_kmz_file")
            if out_kmz_file is None: return {"success": False, "error": "out_kmz_file parameter is required"}

            map_output_scale = params.get("map_output_scale", 1)
            is_composite = params.get("is_composite", "NO_COMPOSITE")
            is_vector_to_raster = params.get("is_vector_to_raster", "RASTERIZE_LAYERS")
            extent_to_export = params.get("extent_to_export")
            image_size = params.get("image_size", 1024)
            dpi_of_client = params.get("dpi_of_client", 96)
            ignore_zvalue = params.get("ignore_zvalue", "ABSOLUTE")

            arcpy.conversion.MapToKML(in_map, out_kmz_file, map_output_scale, is_composite, is_vector_to_raster, extent_to_export, image_size, dpi_of_client, ignore_zvalue)

            return {"success": True, "output_path": out_kmz_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def las_dataset_to_raster(self, params):
        """LAS Dataset To Raster

Creates a raster using elevation, intensity, or RGB values stored in the lidar points.
        """
        try:
            in_las_dataset = params.get("in_las_dataset")
            if in_las_dataset is None: return {"success": False, "error": "in_las_dataset parameter is required"}
            out_raster = params.get("out_raster")
            if out_raster is None: return {"success": False, "error": "out_raster parameter is required"}

            value_field = params.get("value_field", "ELEVATION")
            interpolation_type = params.get("interpolation_type")
            data_type = params.get("data_type", "FLOAT")
            sampling_type = params.get("sampling_type", "CELLSIZE")
            sampling_value = params.get("sampling_value", 10)
            z_factor = params.get("z_factor", 1)

            arcpy.conversion.LASDatasetToRaster(in_las_dataset, out_raster, value_field, interpolation_type, data_type, sampling_type, sampling_value, z_factor)

            self._add_to_map(out_raster)
            return {"success": True, "output_path": out_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def export_to_cad(self, params):
        """Export To CAD

Exports features to new or existing CAD files.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            output_type = params.get("output_type")
            if output_type is None: return {"success": False, "error": "output_type parameter is required"}
            output_file = params.get("output_file")
            if output_file is None: return {"success": False, "error": "output_file parameter is required"}

            append_to_existing = params.get("append_to_existing", "OVERWRITE_EXISTING_FILES")
            seed_file = params.get("seed_file")

            arcpy.conversion.ExportToCAD(in_features, output_type, output_file, append_to_existing, seed_file)

            return {"success": True, "output_path": output_file}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def table_to_dbase(self, params):
        """Table to dBASE

Converts one or more tables to dBASE tables.
        """
        try:
            input_table = params.get("input_table")
            if input_table is None: return {"success": False, "error": "input_table parameter is required"}
            output_folder = params.get("output_folder")
            if output_folder is None: return {"success": False, "error": "output_folder parameter is required"}

            arcpy.conversion.TableToDBASE(input_table, output_folder)

            return {"success": True, "output_path": output_folder}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def bim_file_to_geodatabase(self, params):
        """BIM File To Geodatabase

Imports the contents of one or more BIM file workspaces into a single geodatabase feature dataset.
        """
        try:
            in_bim_file_workspace = params.get("in_bim_file_workspace")
            if in_bim_file_workspace is None: return {"success": False, "error": "in_bim_file_workspace parameter is required"}
            out_gdb_path = params.get("out_gdb_path")
            if out_gdb_path is None: return {"success": False, "error": "out_gdb_path parameter is required"}
            out_dataset_name = params.get("out_dataset_name")
            if out_dataset_name is None: return {"success": False, "error": "out_dataset_name parameter is required"}

            spatial_reference = params.get("spatial_reference")
            identifier = params.get("identifier")
            include_floorplan = params.get("include_floorplan", "INCLUDE_FLOORPLAN")

            result = arcpy.conversion.BIMFileToGeodatabase(in_bim_file_workspace, out_gdb_path, out_dataset_name, spatial_reference, identifier, include_floorplan)

            output_path = result.getOutput(0)
            self._add_to_map(output_path)
            return {"success": True, "output_path": output_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def cad_to_geodatabase(self, params):
        """CAD To Geodatabase

Reads a CAD dataset and creates feature classes of the drawing.
        """
        try:
            input_cad_datasets = params.get("input_cad_datasets")
            if input_cad_datasets is None: return {"success": False, "error": "input_cad_datasets parameter is required"}
            out_gdb_path = params.get("out_gdb_path")
            if out_gdb_path is None: return {"success": False, "error": "out_gdb_path parameter is required"}
            out_dataset_name = params.get("out_dataset_name")
            if out_dataset_name is None: return {"success": False, "error": "out_dataset_name parameter is required"}

            reference_scale = params.get("reference_scale", 1000)
            spatial_reference = params.get("spatial_reference")

            result = arcpy.conversion.CADToGeodatabase(input_cad_datasets, out_gdb_path, out_dataset_name, reference_scale, spatial_reference)

            output_path = result.getOutput(0)
            self._add_to_map(output_path)
            return {"success": True, "output_path": output_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def export_features(self, params):
        """Export Features

Converts a feature class or feature layer to a new feature class.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_features = params.get("out_features")
            if out_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_features = arcpy.CreateUniqueName("Export_Features_Output", aprx.defaultGeodatabase)

            where_clause = params.get("where_clause")
            use_field_alias_name = params.get("use_field_alias_name", "NOT_USE_ALIAS")
            field_mapping = params.get("field_mapping")
            sort_field = params.get("sort_field")

            arcpy.conversion.ExportFeatures(in_features, out_features, where_clause, use_field_alias_name, field_mapping, sort_field)

            self._add_to_map(out_features)
            return {"success": True, "output_path": out_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def export_table(self, params):
        """Export Table

Exports the rows of a table or table view to a new table.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None: return {"success": False, "error": "in_table parameter is required"}
            out_table = params.get("out_table")
            if out_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("Export_Table_Output", aprx.defaultGeodatabase)

            where_clause = params.get("where_clause")
            use_field_alias_name = params.get("use_field_alias_name", "NOT_USE_ALIAS")
            field_mapping = params.get("field_mapping")
            sort_field = params.get("sort_field")

            arcpy.conversion.ExportTable(in_table, out_table, where_clause, use_field_alias_name, field_mapping, sort_field)

            return {"success": True, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def feature_class_to_geodatabase(self, params):
        """Feature Class To Geodatabase

Converts one or more feature classes or feature layers to geodatabase feature classes.
        """
        try:
            input_features = params.get("input_features")
            if input_features is None: return {"success": False, "error": "input_features parameter is required"}
            output_geodatabase = params.get("output_geodatabase")
            if output_geodatabase is None: return {"success": False, "error": "output_geodatabase parameter is required"}

            arcpy.conversion.FeatureClassToGeodatabase(input_features, output_geodatabase)

            return {"success": True, "output_path": output_geodatabase}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_geodatabase(self, params):
        """Raster To Geodatabase

Loads raster datasets into a geodatabase.
        """
        try:
            input_rasters = params.get("input_rasters")
            if input_rasters is None: return {"success": False, "error": "input_rasters parameter is required"}
            output_geodatabase = params.get("output_geodatabase")
            if output_geodatabase is None: return {"success": False, "error": "output_geodatabase parameter is required"}

            configuration_keyword = params.get("configuration_keyword")

            arcpy.conversion.RasterToGeodatabase(input_rasters, output_geodatabase, configuration_keyword)

            return {"success": True, "output_path": output_geodatabase}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def table_to_geodatabase(self, params):
        """Table To Geodatabase

Converts one or more tables to geodatabase tables in an output geodatabase.
        """
        try:
            input_table = params.get("input_table")
            if input_table is None: return {"success": False, "error": "input_table parameter is required"}
            output_geodatabase = params.get("output_geodatabase")
            if output_geodatabase is None: return {"success": False, "error": "output_geodatabase parameter is required"}

            arcpy.conversion.TableToGeodatabase(input_table, output_geodatabase)

            return {"success": True, "output_path": output_geodatabase}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def feature_to_raster(self, params):
        """Feature to Raster

Converts features to a raster dataset.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            field = params.get("field")
            if field is None: return {"success": False, "error": "field parameter is required"}
            out_raster = params.get("out_raster")
            if out_raster is None: return {"success": False, "error": "out_raster parameter is required"}

            cell_size = params.get("cell_size")

            arcpy.conversion.FeatureToRaster(in_features, field, out_raster, cell_size)

            self._add_to_map(out_raster)
            return {"success": True, "output_path": out_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def point_to_raster(self, params):
        """Point to Raster

Converts point features to a raster dataset.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            value_field = params.get("value_field")
            if value_field is None: return {"success": False, "error": "value_field parameter is required"}
            out_rasterdataset = params.get("out_rasterdataset")
            if out_rasterdataset is None: return {"success": False, "error": "out_rasterdataset parameter is required"}

            cell_assignment = params.get("cell_assignment", "MOST_FREQUENT")
            priority_field = params.get("priority_field", "NONE")
            cellsize = params.get("cellsize")
            build_rat = params.get("build_rat", "BUILD")

            arcpy.conversion.PointToRaster(in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize, build_rat)

            self._add_to_map(out_rasterdataset)
            return {"success": True, "output_path": out_rasterdataset}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def polygon_to_raster(self, params):
        """Polygon to Raster

Converts polygon features to a raster dataset.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            value_field = params.get("value_field")
            if value_field is None: return {"success": False, "error": "value_field parameter is required"}
            out_rasterdataset = params.get("out_rasterdataset")
            if out_rasterdataset is None: return {"success": False, "error": "out_rasterdataset parameter is required"}

            cell_assignment = params.get("cell_assignment", "CELL_CENTER")
            priority_field = params.get("priority_field", "NONE")
            cellsize = params.get("cellsize")
            build_rat = params.get("build_rat", "BUILD")

            arcpy.conversion.PolygonToRaster(in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize, build_rat)

            self._add_to_map(out_rasterdataset)
            return {"success": True, "output_path": out_rasterdataset}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def polyline_to_raster(self, params):
        """Polyline to Raster

Converts polyline features to a raster dataset.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            value_field = params.get("value_field")
            if value_field is None: return {"success": False, "error": "value_field parameter is required"}
            out_rasterdataset = params.get("out_rasterdataset")
            if out_rasterdataset is None: return {"success": False, "error": "out_rasterdataset parameter is required"}

            cell_assignment = params.get("cell_assignment", "MAXIMUM_LENGTH")
            priority_field = params.get("priority_field", "NONE")
            cellsize = params.get("cellsize")
            build_rat = params.get("build_rat", "BUILD")

            arcpy.conversion.PolylineToRaster(in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize, build_rat)

            self._add_to_map(out_rasterdataset)
            return {"success": True, "output_path": out_rasterdataset}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def feature_class_to_shapefile(self, params):
        """Feature Class To Shapefile

Converts one or more feature classes or feature layers to shapefiles.
        """
        try:
            input_features = params.get("input_features")
            if input_features is None: return {"success": False, "error": "input_features parameter is required"}
            output_folder = params.get("output_folder")
            if output_folder is None: return {"success": False, "error": "output_folder parameter is required"}

            arcpy.conversion.FeatureClassToShapefile(input_features, output_folder)

            return {"success": True, "output_path": output_folder}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def raster_to_other_format(self, params):
        """Raster To Other Format

Converts one or more raster datasets to a different format.
        """
        try:
            input_rasters = params.get("input_rasters")
            if input_rasters is None: return {"success": False, "error": "input_rasters parameter is required"}
            output_workspace = params.get("output_workspace")
            if output_workspace is None: return {"success": False, "error": "output_workspace parameter is required"}
            raster_format = params.get("raster_format")
            if raster_format is None: return {"success": False, "error": "raster_format parameter is required"}

            arcpy.conversion.RasterToOtherFormat(input_rasters, output_workspace, raster_format)

            return {"success": True, "output_path": output_workspace}
        except Exception as e:
            return {"success": False, "error": str(e)}