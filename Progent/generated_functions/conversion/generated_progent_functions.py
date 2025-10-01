# Generated ArcGIS Pro conversion Progent Functions
# Generated on 2025-10-01T14:01:07.517023
# Total tools: 50

import arcpy
import os

class GeneratedSpatialFunctions:
    """Generated spatial analysis functions in progent.pyt format"""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def excel_to_table(self, params):
        """Excel To Table

Converts Microsoft Excel files into a table.

        params: {"input_excel_file": <File>, "output_table": <Table>, "field_names_row": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_excel_file = params.get("input_excel_file")
        if input_excel_file is None:
            return {"success": False, "error": "input_excel_file parameter is required"}
        output_table = params.get("output_table")
        if output_table is None:
            return {"success": False, "error": "output_table parameter is required"}
        field_names_row = params.get("field_names_row")
        cell_range = params.get("cell_range")

            # Generate output name and path
            output_name = f"{input_excel_file.replace(' ', '_')}_Excel_To_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Excel To Table
            arcpy.ExcelToTable(input_excel_file, output_table, field_names_row, cell_range)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_excel(self, params):
        """Table To Excel

Converts  a table to a Microsoft Excel file (.xls or .xlsx).

        params: {"input_table": <Table View>, "output_excel_file": <File>, "use_field_alias_column_header": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        output_excel_file = params.get("output_excel_file")
        if output_excel_file is None:
            return {"success": False, "error": "output_excel_file parameter is required"}
        use_field_alias_column_header = params.get("use_field_alias_column_header")
        use_domain_and_subtype_description = params.get("use_domain_and_subtype_description")

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Table_To_Excel"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To Excel
            arcpy.TableToExcel(input_table, output_excel_file, use_field_alias_column_header, use_domain_and_subtype_description)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pdf_to_tiff(self, params):
        """PDF To TIFF

Exports a .pdf file to Tagged Image File Format (TIFF).

        params: {"in_pdf_file": <File>, "out_tiff_file": <Raster Dataset>, "pdf_password": <Encrypted String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_pdf_file = params.get("in_pdf_file")
        if in_pdf_file is None:
            return {"success": False, "error": "in_pdf_file parameter is required"}
        out_tiff_file = params.get("out_tiff_file")
        if out_tiff_file is None:
            return {"success": False, "error": "out_tiff_file parameter is required"}
        pdf_password = params.get("pdf_password")
        pdf_page_number = params.get("pdf_page_number")
        pdf_map = params.get("pdf_map")
        clip_option = params.get("clip_option")
        resolution = params.get("resolution")
        color_mode = params.get("color_mode")
        tiff_compression = params.get("tiff_compression")
        geotiff_tags = params.get("geotiff_tags")

            # Generate output name and path
            output_name = f"{in_pdf_file.replace(' ', '_')}_PDF_To_TIFF"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute PDF To TIFF
            arcpy.PDFToTIFF(in_pdf_file, out_tiff_file, pdf_password, pdf_page_number, pdf_map, clip_option, resolution, color_mode, tiff_compression, geotiff_tags)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_ascii(self, params):
        """Raster to ASCII

Converts a raster dataset to an ASCII file representing raster data.

        params: {"in_raster": <Raster Layer>, "out_ascii_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_ascii_file = params.get("out_ascii_file")
        if out_ascii_file is None:
            return {"success": False, "error": "out_ascii_file parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Raster_to_ASCII"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster to ASCII
            arcpy.RastertoASCII(in_raster, out_ascii_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_float(self, params):
        """Raster to Float

Converts a raster dataset to a file of binary floating-point values representing raster data.

        params: {"in_raster": <Raster Layer>, "out_float_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_float_file = params.get("out_float_file")
        if out_float_file is None:
            return {"success": False, "error": "out_float_file parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Raster_to_Float"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster to Float
            arcpy.RastertoFloat(in_raster, out_float_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_point(self, params):
        """Raster to Point

Converts a raster dataset to point features.

        params: {"in_raster": <Raster Layer>, "out_point_features": <Feature Class>, "raster_field": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_point_features = params.get("out_point_features")
        if out_point_features is None:
            return {"success": False, "error": "out_point_features parameter is required"}
        raster_field = params.get("raster_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Raster_to_Point"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster to Point
            arcpy.RastertoPoint(in_raster, out_point_features, raster_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_polygon(self, params):
        """Raster to Polygon

Converts a raster dataset to polygon features.

        params: {"in_raster": <Raster Layer>, "out_polygon_features": <Feature Class>, "simplify": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_polygon_features = params.get("out_polygon_features")
        if out_polygon_features is None:
            return {"success": False, "error": "out_polygon_features parameter is required"}
        simplify = params.get("simplify")
        raster_field = params.get("raster_field")
        create_multipart_features = params.get("create_multipart_features")
        max_vertices_per_feature = params.get("max_vertices_per_feature")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Raster_to_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster to Polygon
            arcpy.RastertoPolygon(in_raster, out_polygon_features, simplify, raster_field, create_multipart_features, max_vertices_per_feature)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_polyline(self, params):
        """Raster to Polyline

Converts a raster dataset to polyline features.

        params: {"in_raster": <Raster Layer>, "out_polyline_features": <Feature Class>, "background_value": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_polyline_features = params.get("out_polyline_features")
        if out_polyline_features is None:
            return {"success": False, "error": "out_polyline_features parameter is required"}
        background_value = params.get("background_value")
        minimum_dangle_length = params.get("minimum_dangle_length")
        simplify = params.get("simplify")
        raster_field = params.get("raster_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Raster_to_Polyline"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster to Polyline
            arcpy.RastertoPolyline(in_raster, out_polyline_features, background_value, minimum_dangle_length, simplify, raster_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def wfs_to_feature_class(self, params):
        """WFS To Feature Class

Imports a feature type from a Web Feature Service (WFS) to a feature class in a geodatabase.

        params: {"input_wfs_server": <String>, "wfs_feature_type": <String>, "out_path": <Workspace; Feature Dataset; Folder>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_wfs_server = params.get("input_wfs_server")
        if input_wfs_server is None:
            return {"success": False, "error": "input_wfs_server parameter is required"}
        wfs_feature_type = params.get("wfs_feature_type")
        if wfs_feature_type is None:
            return {"success": False, "error": "wfs_feature_type parameter is required"}
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        is_complex = params.get("is_complex")
        max_features = params.get("max_features")
        expose_metadata = params.get("expose_metadata")
        swap_xy = params.get("swap_xy")
        page_size = params.get("page_size")

            # Generate output name and path
            output_name = f"{input_wfs_server.replace(' ', '_')}_WFS_To_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute WFS To Feature Class
            arcpy.WFSToFeatureClass(input_wfs_server, wfs_feature_type, out_path, out_name, is_complex, max_features, expose_metadata, swap_xy, page_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def features_to_gpx(self, params):
        """Features To GPX

Converts point, multipoint, or polyline features to a GPX format file (.gpx).

        params: {"in_features": <Feature Layer>, "out_gpx_file": <File>, "name_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_gpx_file = params.get("out_gpx_file")
        if out_gpx_file is None:
            return {"success": False, "error": "out_gpx_file parameter is required"}
        name_field = params.get("name_field")
        description_field = params.get("description_field")
        z_field = params.get("z_field")
        date_field = params.get("date_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Features_To_GPX"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Features To GPX
            arcpy.FeaturesToGPX(in_features, out_gpx_file, name_field, description_field, z_field, date_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def gpx_to_features(self, params):
        """GPX To Features

Converts the point data in a .gpx file to features.

        params: {"input_gpx_file": <File>, "output_feature_class": <Feature Class>, "output_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_gpx_file = params.get("input_gpx_file")
        if input_gpx_file is None:
            return {"success": False, "error": "input_gpx_file parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        output_type = params.get("output_type")

            # Generate output name and path
            output_name = f"{input_gpx_file.replace(' ', '_')}_GPX_To_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GPX To Features
            arcpy.GPXToFeatures(input_gpx_file, output_feature_class, output_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def features_to_graphics(self, params):
        """Features To Graphics

Converts a feature layer's symbolized features into graphic elements in a graphics layer.

        params: {"in_layer": <Feature Layer>, "out_layer": <Graphics Layer>, "exclude_features": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        exclude_features = params.get("exclude_features")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Features_To_Graphics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Features To Graphics
            arcpy.FeaturesToGraphics(in_layer, out_layer, exclude_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def graphics_to_features(self, params):
        """Graphics To Features

Converts a graphics layer into a feature layer with geometries based on the input graphics layer's elements.

        params: {"in_layer": <Graphics Layer>, "graphics_type": <String>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        graphics_type = params.get("graphics_type")
        if graphics_type is None:
            return {"success": False, "error": "graphics_type parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        delete_graphics = params.get("delete_graphics")
        reference_scale = params.get("reference_scale")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Graphics_To_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Graphics To Features
            arcpy.GraphicsToFeatures(in_layer, graphics_type, out_feature_class, delete_graphics, reference_scale)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def features_to_json(self, params):
        """Features To JSON

Converts features to Esri JSON or GeoJSON format. The fields, geometry, and spatial reference of features will be converted to their corresponding JSON representation and written to a file with a .json or .geojson extension.

        params: {"in_features": <Feature Layer>, "out_json_file": <File>, "format_json": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_json_file = params.get("out_json_file")
        if out_json_file is None:
            return {"success": False, "error": "out_json_file parameter is required"}
        format_json = params.get("format_json")
        include_z_values = params.get("include_z_values")
        include_m_values = params.get("include_m_values")
        geojson = params.get("geojson")
        outputtowgs84 = params.get("outputtowgs84")
        use_field_alias = params.get("use_field_alias")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Features_To_JSON"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Features To JSON
            arcpy.FeaturesToJSON(in_features, out_json_file, format_json, include_z_values, include_m_values, geojson, outputtowgs84, use_field_alias)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def json_to_features(self, params):
        """JSON To Features

Converts feature collections in an Esri JSON formatted file (.json) or a GeoJSON formatted file (.geojson) to a feature class.

        params: {"in_json_file": <File>, "out_features": <Feature Class>, "geometry_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_json_file = params.get("in_json_file")
        if in_json_file is None:
            return {"success": False, "error": "in_json_file parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        geometry_type = params.get("geometry_type")

            # Generate output name and path
            output_name = f"{in_json_file.replace(' ', '_')}_JSON_To_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute JSON To Features
            arcpy.JSONToFeatures(in_json_file, out_features, geometry_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def kml_to_layer(self, params):
        """KML To Layer

Converts a .kml or .kmz file into datasets in a geodatabase  and a layer file.  The layer file  maintains the symbology of the input .kml or .kmz file. Learn more about KML support in ArcGIS

        params: {"in_kml_file": <File; KML Layer>, "output_folder": <Folder>, "output_data": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_kml_file = params.get("in_kml_file")
        if in_kml_file is None:
            return {"success": False, "error": "in_kml_file parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        output_data = params.get("output_data")
        include_groundoverlay = params.get("include_groundoverlay")
        out_suffix = params.get("out_suffix")

            # Generate output name and path
            output_name = f"{in_kml_file.replace(' ', '_')}_KML_To_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute KML To Layer
            arcpy.KMLToLayer(in_kml_file, output_folder, output_data, include_groundoverlay, out_suffix)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def layer_to_kml(self, params):
        """Layer To KML

Converts a feature or raster layer  to KML format (.kmz or .kml file). The output KML will contain a translation of Esri feature geometries, raster cells, layer symbology, and other properties. Learn more about KML support in ArcGIS

        params: {"layer": <Feature Layer; Raster Layer; Mosaic Layer; Group Layer; Layer File>, "out_kmz_file": <File; Workspace; KML Layer>, "layer_output_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        layer = params.get("layer")
        if layer is None:
            return {"success": False, "error": "layer parameter is required"}
        out_kmz_file = params.get("out_kmz_file")
        if out_kmz_file is None:
            return {"success": False, "error": "out_kmz_file parameter is required"}
        layer_output_scale = params.get("layer_output_scale")
        is_composite = params.get("is_composite")
        boundary_box_extent = params.get("boundary_box_extent")
        image_size = params.get("image_size")
        dpi_of_client = params.get("dpi_of_client")
        ignore_zvalue = params.get("ignore_zvalue")

            # Generate output name and path
            output_name = f"{layer.replace(' ', '_')}_Layer_To_KML"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Layer To KML
            arcpy.LayerToKML(layer, out_kmz_file, layer_output_scale, is_composite, boundary_box_extent, image_size, dpi_of_client, ignore_zvalue)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def map_to_kml(self, params):
        """Map To KML

Converts a map containing feature or raster layers  to KML format (.kmz  file). The output KML will contain a translation of Esri feature geometries, raster cells, layer symbology, and other properties. Learn more about KML support in ArcGIS

        params: {"in_map": <Map>, "out_kmz_file": <File>, "map_output_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        out_kmz_file = params.get("out_kmz_file")
        if out_kmz_file is None:
            return {"success": False, "error": "out_kmz_file parameter is required"}
        map_output_scale = params.get("map_output_scale")
        is_composite = params.get("is_composite")
        is_vector_to_raster = params.get("is_vector_to_raster")
        extent_to_export = params.get("extent_to_export")
        image_size = params.get("image_size")
        dpi_of_client = params.get("dpi_of_client")
        ignore_zvalue = params.get("ignore_zvalue")
        layout = params.get("layout")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Map_To_KML"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Map To KML
            arcpy.MapToKML(in_map, out_kmz_file, map_output_scale, is_composite, is_vector_to_raster, extent_to_export, image_size, dpi_of_client, ignore_zvalue, layout)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_las(self, params):
        """Convert LAS

Converts .las, .zlas, and .laz files between different LAS compression methods, file versions, and point record formats.

        params: {"in_las": <Layer File; LAS Dataset Layer; Folder; File>, "target_folder": <Folder>, "file_version": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las = params.get("in_las")
        if in_las is None:
            return {"success": False, "error": "in_las parameter is required"}
        target_folder = params.get("target_folder")
        if target_folder is None:
            return {"success": False, "error": "target_folder parameter is required"}
        file_version = params.get("file_version")
        point_format = params.get("point_format")
        compression = params.get("compression")
        las_options = params.get("las_options")
        out_las_dataset = params.get("out_las_dataset")
        define_coordinate_system = params.get("define_coordinate_system")
        in_coordinate_system = params.get("in_coordinate_system")

            # Generate output name and path
            output_name = f"{in_las.replace(' ', '_')}_Convert_LAS"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert LAS
            arcpy.ConvertLAS(in_las, target_folder, file_version, point_format, compression, las_options, out_las_dataset, define_coordinate_system, in_coordinate_system)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def las_dataset_to_raster(self, params):
        """LAS Dataset To Raster

Creates a raster using elevation, intensity, or RGB values stored in the lidar points referenced by the LAS dataset.

        params: {"in_las_dataset": <LAS Dataset Layer>, "out_raster": <Raster Dataset>, "value_field": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        value_field = params.get("value_field")
        interpolation_type_binning_cell_assignment_type_void_fill_method_or_triangulation_interpolation_method_point_thinning_type_point_selection_method_resolution = params.get("interpolation_type_binning_cell_assignment_type_void_fill_method_or_triangulation_interpolation_method_point_thinning_type_point_selection_method_resolution")
        data_type = params.get("data_type")
        sampling_type = params.get("sampling_type")
        sampling_value = params.get("sampling_value")
        z_factor = params.get("z_factor")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_LAS_Dataset_To_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute LAS Dataset To Raster
            arcpy.LASDatasetToRaster(in_las_dataset, out_raster, value_field, interpolation_type_binning_cell_assignment_type_void_fill_method_or_triangulation_interpolation_method_point_thinning_type_point_selection_method_resolution, data_type, sampling_type, sampling_value, z_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mesh_to_las(self, params):
        """Mesh To LAS

Converts an integrated mesh into a LAS format point cloud.

        params: {"in_mesh": <Scene Layer; File>, "target_folder": <Folder>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mesh = params.get("in_mesh")
        if in_mesh is None:
            return {"success": False, "error": "in_mesh parameter is required"}
        target_folder = params.get("target_folder")
        if target_folder is None:
            return {"success": False, "error": "target_folder parameter is required"}
        method = params.get("method")
        maximum_triangle_area = params.get("maximum_triangle_area")
        extent = params.get("extent")
        boundary = params.get("boundary")
        rearrange_points = params.get("rearrange_points")
        compute_stats = params.get("compute_stats")
        out_las_dataset = params.get("out_las_dataset")
        compression = params.get("compression")

            # Generate output name and path
            output_name = f"{in_mesh.replace(' ', '_')}_Mesh_To_LAS"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mesh To LAS
            arcpy.MeshToLAS(in_mesh, target_folder, method, maximum_triangle_area, extent, boundary, rearrange_points, compute_stats, out_las_dataset, compression)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def point_cloud_to_raster(self, params):
        """Point Cloud To Raster

Creates a raster surface from height values in a point cloud scene layer package (*.slpk file) or Indexed 3D Scene (I3S) service.

        params: {"in_point_cloud": <Scene Layer; File>, "cell_size": <Linear Unit>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_cloud = params.get("in_point_cloud")
        if in_point_cloud is None:
            return {"success": False, "error": "in_point_cloud parameter is required"}
        cell_size = params.get("cell_size")
        if cell_size is None:
            return {"success": False, "error": "cell_size parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        cell_assignment = params.get("cell_assignment")
        void_fill = params.get("void_fill")
        z_factor = params.get("z_factor")

            # Generate output name and path
            output_name = f"{in_point_cloud.replace(' ', '_')}_Point_Cloud_To_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Point Cloud To Raster
            arcpy.PointCloudToRaster(in_point_cloud, cell_size, out_raster, cell_assignment, void_fill, z_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sas_to_table(self, params):
        """SAS To Table

Converts a SAS dataset to a table.

        params: {"in_sas_dataset": <String>, "out_table": <Table>, "use_cas_connection": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_sas_dataset = params.get("in_sas_dataset")
        if in_sas_dataset is None:
            return {"success": False, "error": "in_sas_dataset parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        use_cas_connection = params.get("use_cas_connection")
        hostname = params.get("hostname")
        port = params.get("port")
        username = params.get("username")
        password = params.get("password")
        custom_cfg_file = params.get("custom_cfg_file")
        authinfo_file = params.get("authinfo_file")

            # Generate output name and path
            output_name = f"{in_sas_dataset.replace(' ', '_')}_SAS_To_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute SAS To Table
            arcpy.SASToTable(in_sas_dataset, out_table, use_cas_connection, hostname, port, username, password, custom_cfg_file, authinfo_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_sas(self, params):
        """Table To SAS

Converts a table to a SAS dataset.

        params: {"in_table": <Table View>, "out_sas_dataset": <String>, "replace_sas_dataset": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_sas_dataset = params.get("out_sas_dataset")
        if out_sas_dataset is None:
            return {"success": False, "error": "out_sas_dataset parameter is required"}
        replace_sas_dataset = params.get("replace_sas_dataset")
        use_domain_and_subtype_description = params.get("use_domain_and_subtype_description")
        use_cas_connection = params.get("use_cas_connection")
        hostname = params.get("hostname")
        port = params.get("port")
        username = params.get("username")
        password = params.get("password")
        custom_cfg_file = params.get("custom_cfg_file")
        authinfo_file = params.get("authinfo_file")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Table_To_SAS"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To SAS
            arcpy.TableToSAS(in_table, out_sas_dataset, replace_sas_dataset, use_domain_and_subtype_description, use_cas_connection, hostname, port, username, password, custom_cfg_file, authinfo_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_cad_fields(self, params):
        """Add CAD Fields

Adds several reserved CAD fields in one step. Fields created by this tool are used by the Export To CAD tool to generate CAD entities with specific properties.   After executing this tool, you must calculate or type the appropriate field values.

        params: {"input_table": <Table View>, "entities": <Boolean>, "layerprops": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        entities = params.get("entities")
        if entities is None:
            return {"success": False, "error": "entities parameter is required"}
        layerprops = params.get("layerprops")
        textprops = params.get("textprops")
        docprops = params.get("docprops")
        xdataprops = params.get("xdataprops")

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Add_CAD_Fields"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add CAD Fields
            arcpy.AddCADFields(input_table, entities, layerprops, textprops, docprops, xdataprops)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_to_cad(self, params):
        """Export To CAD

Exports features to  new or existing CAD files based on one or more input feature layers or feature classes. The geometry, feature attributes, and coordinates system of ArcGIS feature layers will be included when outputting to AutoCAD .dwg or .dxf files. This GIS data  can be used with the ArcGIS for AutoCAD plug-in to AutoCAD.  If you do not have the plug-in, you can access the output geometry as CAD entities.

        params: {"in_features": <Feature Layer>, "output_type": <String>, "append_to_existing": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_type = params.get("output_type")
        if output_type is None:
            return {"success": False, "error": "output_type parameter is required"}
        append_to_existing = params.get("append_to_existing")
        seed_file = params.get("seed_file")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Export_To_CAD"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export To CAD
            arcpy.ExportToCAD(in_features, output_type, append_to_existing, seed_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_to_cad(self, params):
        """Export to CAD

Exports features to  new or existing CAD files based on one or more input feature layers or feature classes. The geometry, feature attributes, and coordinates system of ArcGIS feature layers will be included when outputting to AutoCAD .dwg or .dxf files. This GIS data  can be used with the ArcGIS for AutoCAD plug-in to AutoCAD.  If you do not have the plug-in, you can access the output geometry as CAD entities.

        params: {"in_features": <Feature Layer>, "output_type": <String>, "append_to_existing": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_type = params.get("output_type")
        if output_type is None:
            return {"success": False, "error": "output_type parameter is required"}
        append_to_existing = params.get("append_to_existing")
        seed_file = params.get("seed_file")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Export_to_CAD"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export to CAD
            arcpy.ExporttoCAD(in_features, output_type, append_to_existing, seed_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multipatch_to_collada(self, params):
        """Multipatch To Collada

Converts one or more multipatch features into a collection of COLLADA files (.dae) and referenced texture image files in an output folder.

        params: {"in_features": <Feature Layer>, "output_folder": <Folder>, "prepend_source": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        prepend_source = params.get("prepend_source")
        field_name = params.get("field_name")
        collada_version = params.get("collada_version")
        if collada_version is None:
            return {"success": False, "error": "collada_version parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Multipatch_To_Collada"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multipatch To Collada
            arcpy.MultipatchToCollada(in_features, output_folder, prepend_source, field_name, collada_version)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_dbase(self, params):
        """Table to dBASE

Converts one or more tables to dBASE tables.

        params: {"input_table": <Table View>, "output_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Table_to_dBASE"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table to dBASE
            arcpy.TabletodBASE(input_table, output_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_dbase(self, params):
        """Table To dBASE

Converts one or more tables to dBASE tables.

        params: {"input_table": <Table View>, "output_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Table_To_dBASE"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To dBASE
            arcpy.TableTodBASE(input_table, output_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_dbase(self, params):
        """Table to dBASE

Converts one or more tables to dBASE tables.

        params: {"input_table": <Table View>, "output_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Table_to_dBASE"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table to dBASE
            arcpy.TabletodBASE(input_table, output_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bim_file_to_geodatabase(self, params):
        """BIM File To Geodatabase

Imports the contents of one or more BIM file workspaces into a single geodatabase feature dataset.

        params: {"in_bim_file_workspace": <BIM File Workspace>, "out_gdb_path": <Workspace>, "out_dataset_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_bim_file_workspace = params.get("in_bim_file_workspace")
        if in_bim_file_workspace is None:
            return {"success": False, "error": "in_bim_file_workspace parameter is required"}
        out_gdb_path = params.get("out_gdb_path")
        if out_gdb_path is None:
            return {"success": False, "error": "out_gdb_path parameter is required"}
        out_dataset_name = params.get("out_dataset_name")
        if out_dataset_name is None:
            return {"success": False, "error": "out_dataset_name parameter is required"}
        spatial_reference = params.get("spatial_reference")
        identifier = params.get("identifier")
        include_floorplan = params.get("include_floorplan")

            # Generate output name and path
            output_name = f"{in_bim_file_workspace.replace(' ', '_')}_BIM_File_To_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute BIM File To Geodatabase
            arcpy.BIMFileToGeodatabase(in_bim_file_workspace, out_gdb_path, out_dataset_name, spatial_reference, identifier, include_floorplan)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cad_to_geodatabase(self, params):
        """CAD To Geodatabase

Reads a CAD dataset and creates feature classes of the drawing. The feature classes are written to a geodatabase feature dataset.

        params: {"input_cad_datasetscad_drawing_dataset": <CAD Drawing Dataset>, "out_gdb_path": <Workspace>, "out_dataset_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_cad_datasetscad_drawing_dataset = params.get("input_cad_datasetscad_drawing_dataset")
        if input_cad_datasetscad_drawing_dataset is None:
            return {"success": False, "error": "input_cad_datasetscad_drawing_dataset parameter is required"}
        out_gdb_path = params.get("out_gdb_path")
        if out_gdb_path is None:
            return {"success": False, "error": "out_gdb_path parameter is required"}
        out_dataset_name = params.get("out_dataset_name")
        if out_dataset_name is None:
            return {"success": False, "error": "out_dataset_name parameter is required"}
        reference_scale = params.get("reference_scale")
        if reference_scale is None:
            return {"success": False, "error": "reference_scale parameter is required"}
        spatial_reference = params.get("spatial_reference")

            # Generate output name and path
            output_name = f"{input_cad_datasetscad_drawing_dataset.replace(' ', '_')}_CAD_To_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute CAD To Geodatabase
            arcpy.CADToGeodatabase(input_cad_datasetscad_drawing_dataset, out_gdb_path, out_dataset_name, reference_scale, spatial_reference)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_features(self, params):
        """Export Features

Converts a feature class or feature layer to a new feature class.

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        where_clause = params.get("where_clause")
        use_field_alias_name = params.get("use_field_alias_name")
        field_mapping = params.get("field_mapping")
        sort_field = params.get("sort_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Export_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Features
            arcpy.ExportFeatures(in_features, out_features, where_clause, use_field_alias_name, field_mapping, sort_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_table(self, params):
        """Export Table

Exports the rows of a table or table view to a new table.

        params: {"in_table": <Table View; Raster Layer>, "out_table": <Table>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        where_clause = params.get("where_clause")
        use_field_alias_name = params.get("use_field_alias_name")
        if use_field_alias_name is None:
            return {"success": False, "error": "use_field_alias_name parameter is required"}
        field_mapping = params.get("field_mapping")
        sort_field = params.get("sort_field")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Export_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Table
            arcpy.ExportTable(in_table, out_table, where_clause, use_field_alias_name, field_mapping, sort_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_bim_file_floorplan(self, params):
        """Extract BIM File Floorplan

Extracts 2.5D floor plan data from a BIM file workspace into a geodatabase dataset.

        params: {"in_bim_file_workspace": <BIM File Workspace>, "output_workspace": <Workspace>, "out_feature_dataset_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_bim_file_workspace = params.get("in_bim_file_workspace")
        if in_bim_file_workspace is None:
            return {"success": False, "error": "in_bim_file_workspace parameter is required"}
        output_workspace = params.get("output_workspace")
        if output_workspace is None:
            return {"success": False, "error": "output_workspace parameter is required"}
        out_feature_dataset_name = params.get("out_feature_dataset_name")
        if out_feature_dataset_name is None:
            return {"success": False, "error": "out_feature_dataset_name parameter is required"}
        out_polyline_featureclass_name = params.get("out_polyline_featureclass_name")
        if out_polyline_featureclass_name is None:
            return {"success": False, "error": "out_polyline_featureclass_name parameter is required"}
        out_polygon_featureclass_name = params.get("out_polygon_featureclass_name")
        if out_polygon_featureclass_name is None:
            return {"success": False, "error": "out_polygon_featureclass_name parameter is required"}
        out_poi_featureclass_name = params.get("out_poi_featureclass_name")
        if out_poi_featureclass_name is None:
            return {"success": False, "error": "out_poi_featureclass_name parameter is required"}
        out_footprint_featureclass_name = params.get("out_footprint_featureclass_name")
        if out_footprint_featureclass_name is None:
            return {"success": False, "error": "out_footprint_featureclass_name parameter is required"}
        additional_polyline_categories = params.get("additional_polyline_categories")
        if additional_polyline_categories is None:
            return {"success": False, "error": "additional_polyline_categories parameter is required"}
        additional_polygon_categories = params.get("additional_polygon_categories")
        if additional_polygon_categories is None:
            return {"success": False, "error": "additional_polygon_categories parameter is required"}
        included_levels = params.get("included_levels")
        if included_levels is None:
            return {"success": False, "error": "included_levels parameter is required"}

            # Generate output name and path
            output_name = f"{in_bim_file_workspace.replace(' ', '_')}_Extract_BIM_File_Floorplan"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract BIM File Floorplan
            arcpy.ExtractBIMFileFloorplan(in_bim_file_workspace, output_workspace, out_feature_dataset_name, out_polyline_featureclass_name, out_polygon_featureclass_name, out_poi_featureclass_name, out_footprint_featureclass_name, additional_polyline_categories, additional_polygon_categories, included_levels)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_locations_from_document(self, params):
        """Extract Locations From Document

Analyzes documents containing unstructured or semistructured text, such as email messages, travel forms, and so on, and extracts locations to a point feature class. The tool analyzes and processes the input documents as follows:Recognizes spatial coordinates specified in the content of the documents and  creates points representing these locations. The following coordinate formats are recognized: decimal degrees, degrees decimal minutes, degrees minutes seconds, Universal Transverse Mercator, and Military Grid Reference System.Recognizes place names specified in the content of the documents that are defined in a custom location file and creates points representing these locations. A custom location file associates a place name with a spatial coordinate representing that location. Recognizes text that is of interest, extracts this information from a document, and records it in fields in the output feature class's attribute table. This tool supports all Microsoft Office documents (Word, PowerPoint, and Excel); Adobe PDF documents; marked-up text such as XML and HTML documents; and any files containing plain text such as text files (.txt).

        params: {"in_file": <File>, "out_feature_class": <Feature Class>, "in_template": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_file = params.get("in_file")
        if in_file is None:
            return {"success": False, "error": "in_file parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        in_template = params.get("in_template")
        coord_dd_latlon = params.get("coord_dd_latlon")
        coord_dd_xydeg = params.get("coord_dd_xydeg")
        coord_dd_xyplain = params.get("coord_dd_xyplain")
        coord_dm_latlon = params.get("coord_dm_latlon")
        coord_dm_xymin = params.get("coord_dm_xymin")
        coord_dms_latlon = params.get("coord_dms_latlon")
        coord_dms_xysec = params.get("coord_dms_xysec")
        coord_dms_xysep = params.get("coord_dms_xysep")
        coord_utm = params.get("coord_utm")
        coord_ups_north = params.get("coord_ups_north")
        coord_ups_south = params.get("coord_ups_south")
        coord_mgrs = params.get("coord_mgrs")
        coord_mgrs_northpolar = params.get("coord_mgrs_northpolar")
        coord_mgrs_southpolar = params.get("coord_mgrs_southpolar")
        comma_decimal = params.get("comma_decimal")
        coord_use_lonlat = params.get("coord_use_lonlat")
        in_coor_system = params.get("in_coor_system")
        in_custom_locations = params.get("in_custom_locations")
        fuzzy_match = params.get("fuzzy_match")
        max_features_extracted = params.get("max_features_extracted")
        ignore_first_features = params.get("ignore_first_features")
        date_monthname = params.get("date_monthname")
        date_m_d_y = params.get("date_m_d_y")
        date_yyyymmdd = params.get("date_yyyymmdd")
        date_yymmdd = params.get("date_yymmdd")
        date_yyjjj = params.get("date_yyjjj")
        max_dates_extracted = params.get("max_dates_extracted")
        ignore_first_dates = params.get("ignore_first_dates")
        date_range_begin = params.get("date_range_begin")
        date_range_end = params.get("date_range_end")
        in_custom_attributes = params.get("in_custom_attributes")
        file_link = params.get("file_link")
        file_mod_datetime = params.get("file_mod_datetime")
        pre_text_length = params.get("pre_text_length")
        post_text_length = params.get("post_text_length")
        std_coord_fmt = params.get("std_coord_fmt")
        req_word_breaks = params.get("req_word_breaks")

            # Generate output name and path
            output_name = f"{in_file.replace(' ', '_')}_Extract_Locations_From_Document"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Locations From Document
            arcpy.ExtractLocationsFromDocument(in_file, out_feature_class, in_template, coord_dd_latlon, coord_dd_xydeg, coord_dd_xyplain, coord_dm_latlon, coord_dm_xymin, coord_dms_latlon, coord_dms_xysec, coord_dms_xysep, coord_utm, coord_ups_north, coord_ups_south, coord_mgrs, coord_mgrs_northpolar, coord_mgrs_southpolar, comma_decimal, coord_use_lonlat, in_coor_system, in_custom_locations, fuzzy_match, max_features_extracted, ignore_first_features, date_monthname, date_m_d_y, date_yyyymmdd, date_yymmdd, date_yyjjj, max_dates_extracted, ignore_first_dates, date_range_begin, date_range_end, in_custom_attributes, file_link, file_mod_datetime, pre_text_length, post_text_length, std_coord_fmt, req_word_breaks)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_locations_from_text(self, params):
        """Extract Locations From Text

Analyzes input text or a text file and extracts locations to a point feature class. If the input text is a file path, the identified file will be opened and its content will be analyzed. If the input text is unstructured information such as an email message, or semistructured text such as a travel forms, the input text itself will be analyzed. The tool extracts locations found in the text or in the content of the file and adds the resulting points to a feature class. The tool analyzes and processes the text as follows:Recognizes spatial coordinates specified in the content of the text and  creates points representing these locations. The following coordinate formats are recognized: decimal degrees, degrees decimal minutes, degrees minutes seconds, Universal Transverse Mercator, and Military Grid Reference System.Recognizes place names specified in the text that are defined in a custom location file and creates points representing these locations. A custom location file associates a place name with a spatial coordinate representing that location. Recognizes text that is of interest, extracts this information from the text provided, and records it in fields in the output feature class's attribute table.

        params: {"in_text": <String>, "out_feature_class": <Feature Class>, "in_template": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_text = params.get("in_text")
        if in_text is None:
            return {"success": False, "error": "in_text parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        in_template = params.get("in_template")
        coord_dd_latlon = params.get("coord_dd_latlon")
        coord_dd_xydeg = params.get("coord_dd_xydeg")
        coord_dd_xyplain = params.get("coord_dd_xyplain")
        coord_dm_latlon = params.get("coord_dm_latlon")
        coord_dm_xymin = params.get("coord_dm_xymin")
        coord_dms_latlon = params.get("coord_dms_latlon")
        coord_dms_xysec = params.get("coord_dms_xysec")
        coord_dms_xysep = params.get("coord_dms_xysep")
        coord_utm = params.get("coord_utm")
        coord_ups_north = params.get("coord_ups_north")
        coord_ups_south = params.get("coord_ups_south")
        coord_mgrs = params.get("coord_mgrs")
        coord_mgrs_northpolar = params.get("coord_mgrs_northpolar")
        coord_mgrs_southpolar = params.get("coord_mgrs_southpolar")
        comma_decimal = params.get("comma_decimal")
        coord_use_lonlat = params.get("coord_use_lonlat")
        in_coor_system = params.get("in_coor_system")
        in_custom_locations = params.get("in_custom_locations")
        fuzzy_match = params.get("fuzzy_match")
        max_features_extracted = params.get("max_features_extracted")
        ignore_first_features = params.get("ignore_first_features")
        date_monthname = params.get("date_monthname")
        date_m_d_y = params.get("date_m_d_y")
        date_yyyymmdd = params.get("date_yyyymmdd")
        date_yymmdd = params.get("date_yymmdd")
        date_yyjjj = params.get("date_yyjjj")
        max_dates_extracted = params.get("max_dates_extracted")
        ignore_first_dates = params.get("ignore_first_dates")
        date_range_begin = params.get("date_range_begin")
        date_range_end = params.get("date_range_end")
        in_custom_attributes = params.get("in_custom_attributes")
        file_link = params.get("file_link")
        file_mod_datetime = params.get("file_mod_datetime")
        pre_text_length = params.get("pre_text_length")
        post_text_length = params.get("post_text_length")
        std_coord_fmt = params.get("std_coord_fmt")
        req_word_breaks = params.get("req_word_breaks")

            # Generate output name and path
            output_name = f"{in_text.replace(' ', '_')}_Extract_Locations_From_Text"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Locations From Text
            arcpy.ExtractLocationsFromText(in_text, out_feature_class, in_template, coord_dd_latlon, coord_dd_xydeg, coord_dd_xyplain, coord_dm_latlon, coord_dm_xymin, coord_dms_latlon, coord_dms_xysec, coord_dms_xysep, coord_utm, coord_ups_north, coord_ups_south, coord_mgrs, coord_mgrs_northpolar, coord_mgrs_southpolar, comma_decimal, coord_use_lonlat, in_coor_system, in_custom_locations, fuzzy_match, max_features_extracted, ignore_first_features, date_monthname, date_m_d_y, date_yyyymmdd, date_yymmdd, date_yyjjj, max_dates_extracted, ignore_first_dates, date_range_begin, date_range_end, in_custom_attributes, file_link, file_mod_datetime, pre_text_length, post_text_length, std_coord_fmt, req_word_breaks)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_class_to_geodatabase(self, params):
        """Feature Class To Geodatabase

Converts one or more feature classes or feature layers to geodatabase feature classes.

        params: {"input_features": <Feature Layer>, "output_geodatabase": <Feature Dataset; Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_geodatabase = params.get("output_geodatabase")
        if output_geodatabase is None:
            return {"success": False, "error": "output_geodatabase parameter is required"}

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Feature_Class_To_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Class To Geodatabase
            arcpy.FeatureClassToGeodatabase(input_features, output_geodatabase)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mobile_geodatabase_to_file_geodatabase(self, params):
        """Mobile Geodatabase To File Geodatabase

Copies the contents of a mobile geodatabase to a new file geodatabase.

        params: {"in_mobile_gdb": <File>, "out_file_gdb": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mobile_gdb = params.get("in_mobile_gdb")
        if in_mobile_gdb is None:
            return {"success": False, "error": "in_mobile_gdb parameter is required"}
        out_file_gdb = params.get("out_file_gdb")
        if out_file_gdb is None:
            return {"success": False, "error": "out_file_gdb parameter is required"}

            # Generate output name and path
            output_name = f"{in_mobile_gdb.replace(' ', '_')}_Mobile_Geodatabase_To_File_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mobile Geodatabase To File Geodatabase
            arcpy.MobileGeodatabaseToFileGeodatabase(in_mobile_gdb, out_file_gdb)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_geodatabase(self, params):
        """Raster To Geodatabase

Loads raster datasets into a geodatabase.

        params: {"input_rasters": <Raster Dataset; Raster Layer>, "output_geodatabase": <Workspace>, "configuration_keyword": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_rasters = params.get("input_rasters")
        if input_rasters is None:
            return {"success": False, "error": "input_rasters parameter is required"}
        output_geodatabase = params.get("output_geodatabase")
        if output_geodatabase is None:
            return {"success": False, "error": "output_geodatabase parameter is required"}
        configuration_keyword = params.get("configuration_keyword")

            # Generate output name and path
            output_name = f"{input_rasters.replace(' ', '_')}_Raster_To_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster To Geodatabase
            arcpy.RasterToGeodatabase(input_rasters, output_geodatabase, configuration_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_geodatabase(self, params):
        """Table To Geodatabase

Converts one or more tables to geodatabase tables in an output geodatabase.

        params: {"input_table": <Table View>, "output_geodatabase": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        output_geodatabase = params.get("output_geodatabase")
        if output_geodatabase is None:
            return {"success": False, "error": "output_geodatabase parameter is required"}

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Table_To_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To Geodatabase
            arcpy.TableToGeodatabase(input_table, output_geodatabase)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_raster_to_geopackage(self, params):
        """Add Raster To GeoPackage

Loads raster datasets into an OGC GeoPackage raster pyramid.

        params: {"in_dataset": <Raster Layer; Mosaic Layer>, "target_geopackage": <Workspace>, "raster_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        target_geopackage = params.get("target_geopackage")
        if target_geopackage is None:
            return {"success": False, "error": "target_geopackage parameter is required"}
        raster_name = params.get("raster_name")
        if raster_name is None:
            return {"success": False, "error": "raster_name parameter is required"}
        tiling_scheme = params.get("tiling_scheme")
        tiling_scheme_file = params.get("tiling_scheme_file")
        area_of_interest = params.get("area_of_interest")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Add_Raster_To_GeoPackage"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Raster To GeoPackage
            arcpy.AddRasterToGeoPackage(in_dataset, target_geopackage, raster_name, tiling_scheme, tiling_scheme_file, area_of_interest)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_to_raster(self, params):
        """Feature to Raster

Converts features to a raster dataset.

        params: {"in_features": <Feature Layer>, "field": <Field>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        field = params.get("field")
        if field is None:
            return {"success": False, "error": "field parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        cell_size = params.get("cell_size")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature to Raster
            arcpy.FeaturetoRaster(in_features, field, out_raster, cell_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multipatch_to_raster(self, params):
        """Multipatch to Raster

Converts multipatch features to a raster dataset.

        params: {"in_multipatch_features": <Feature Layer>, "out_raster": <Raster Dataset>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multipatch_features = params.get("in_multipatch_features")
        if in_multipatch_features is None:
            return {"success": False, "error": "in_multipatch_features parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        cell_size = params.get("cell_size")
        cell_assignment_method = params.get("cell_assignment_method")

            # Generate output name and path
            output_name = f"{in_multipatch_features.replace(' ', '_')}_Multipatch_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multipatch to Raster
            arcpy.MultipatchtoRaster(in_multipatch_features, out_raster, cell_size, cell_assignment_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def point_to_raster(self, params):
        """Point to Raster

Converts point features to a raster dataset. Learn how the Point to Raster tool works

        params: {"in_features": <Feature Layer>, "value_field": <Field>, "out_rasterdataset": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_rasterdataset = params.get("out_rasterdataset")
        if out_rasterdataset is None:
            return {"success": False, "error": "out_rasterdataset parameter is required"}
        cell_assignment = params.get("cell_assignment")
        priority_field = params.get("priority_field")
        cellsize = params.get("cellsize")
        build_rat = params.get("build_rat")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Point_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Point to Raster
            arcpy.PointtoRaster(in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize, build_rat)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def polygon_to_raster(self, params):
        """Polygon to Raster

Converts polygon features to a raster dataset. Learn how the Polygon to Raster tool works

        params: {"in_features": <Feature Layer>, "value_field": <Field>, "out_rasterdataset": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_rasterdataset = params.get("out_rasterdataset")
        if out_rasterdataset is None:
            return {"success": False, "error": "out_rasterdataset parameter is required"}
        cell_assignment = params.get("cell_assignment")
        priority_field = params.get("priority_field")
        cellsize = params.get("cellsize")
        build_rat = params.get("build_rat")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Polygon_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Polygon to Raster
            arcpy.PolygontoRaster(in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize, build_rat)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def polyline_to_raster(self, params):
        """Polyline to Raster

Converts polyline features to a raster dataset. Learn more about how the Polyline to Raster tool works

        params: {"in_features": <Feature Layer>, "value_field": <Field>, "out_rasterdataset": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_rasterdataset = params.get("out_rasterdataset")
        if out_rasterdataset is None:
            return {"success": False, "error": "out_rasterdataset parameter is required"}
        cell_assignment = params.get("cell_assignment")
        priority_field = params.get("priority_field")
        cellsize = params.get("cellsize")
        build_rat = params.get("build_rat")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Polyline_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Polyline to Raster
            arcpy.PolylinetoRaster(in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize, build_rat)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_other_format(self, params):
        """Raster To Other Format

Converts one or more raster datasets to a different format.

        params: {"input_rasters": <Raster Dataset; Raster Layer>, "output_workspace": <Workspace>, "raster_format": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_rasters = params.get("input_rasters")
        if input_rasters is None:
            return {"success": False, "error": "input_rasters parameter is required"}
        output_workspace = params.get("output_workspace")
        if output_workspace is None:
            return {"success": False, "error": "output_workspace parameter is required"}
        raster_format = params.get("raster_format")

            # Generate output name and path
            output_name = f"{input_rasters.replace(' ', '_')}_Raster_To_Other_Format"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster To Other Format
            arcpy.RasterToOtherFormat(input_rasters, output_workspace, raster_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_class_to_shapefile(self, params):
        """Feature Class To Shapefile

Converts the features from one or more feature classes or feature layers to shapefiles and adds them to a folder of shapefiles.

        params: {"input_features": <Feature Layer>, "output_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Feature_Class_To_Shapefile"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Class To Shapefile
            arcpy.FeatureClassToShapefile(input_features, output_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
