# Generated ArcGIS Pro business-analyst Progent Functions
# Generated on 2025-10-01T15:00:45.088604
# Total tools: 46

import arcpy
import os

class BusinessAnalystTools:
    """Generated spatial analysis functions in progent.pyt format"""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def calculate_market_penetration(self, params):
        """Calculate Market Penetration

Calculates the market penetration based on the number of customers within an area compared to a demographic variable such as total population. An optional report can be created detailing the market penetration.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "id_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("CalculateMarketPenetration_Output", aprx.defaultGeodatabase)
            id_field = params.get("id_field")
            if id_field is None:
                return {"success": False, "error": "id_field parameter is required"}
            market_penetration_base_field = params.get("market_penetration_base_field")
            if market_penetration_base_field is None:
                return {"success": False, "error": "market_penetration_base_field parameter is required"}
            in_customer_features = params.get("in_customer_features")
            if in_customer_features is None:
                return {"success": False, "error": "in_customer_features parameter is required"}
            area_description_field = params.get("area_description_field")
            weight_field = params.get("weight_field")
            create_report = params.get("create_report")
            store_id = params.get("store_id")
            link_field = params.get("link_field")
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")

            # Execute Calculate Market Penetration
            arcpy.ba.CalculateMarketPenetration(in_features, out_feature_class, id_field, market_penetration_base_field, in_customer_features, area_description_field, weight_field, create_report, store_id, link_field, report_title, report_folder, report_format)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def color_coded_layer(self, params):
        """Color Coded Layer

Creates multilevel, scale-dependent choropleth layers from a variable describing a business, demographic, consumer, or landscape characteristic.

        params: {"classification_variable": <String>, "out_layer_name": <String>, "classification_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            classification_variable = params.get("classification_variable")
            if classification_variable is None:
                return {"success": False, "error": "classification_variable parameter is required"}
            out_layer_name = params.get("out_layer_name")
            if out_layer_name is None:
                return {"success": False, "error": "out_layer_name parameter is required"}
            classification_method = params.get("classification_method")
            if classification_method is None:
                return {"success": False, "error": "classification_method parameter is required"}
            number_of_classes = params.get("number_of_classes")
            if number_of_classes is None:
                return {"success": False, "error": "number_of_classes parameter is required"}
            area_of_interest = params.get("area_of_interest")
            out_dataset_path = params.get("out_dataset_path")
            out_dataset_name = params.get("out_dataset_name")
            boundary_mode = params.get("boundary_mode")
            secondary_variable = params.get("secondary_variable")
            grid_size = params.get("grid_size")
            renderer_type = params.get("renderer_type")

            # Execute Color Coded Layer
            arcpy.ba.ColorCodedLayer(classification_variable, out_layer_name, classification_method, number_of_classes, area_of_interest, out_dataset_path, out_dataset_name, boundary_mode, secondary_variable, grid_size, renderer_type)

            # ColorCodedLayer creates a layer file, not a feature class.
            # The output is the layer name, which is not a path to be added to the map directly.
            # We will assume the tool adds it to the map automatically.
            return {"success": True, "output_layer": out_layer_name}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enrich_layer(self, params):
        """Enrich Layer

Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations. The output is a duplicate of the input with additional attribute fields. This tool requires an ArcGIS Online organizational account or a locally stored or installed dataset. This tool uses detailed aggregation and apportionment settings to summarize data.  The Apportion Polygon tool is similar to this tool. However, Apportion Polygon uses user-specified apportionment. Enrich Layer uses U.S. Census Block points or global settlement points for apportionment. For more information, see Data apportionment.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "variables": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("EnrichLayer_Output", aprx.defaultGeodatabase)
            variables = params.get("variables")
            if variables is None:
                return {"success": False, "error": "variables parameter is required"}
            buffer_type = params.get("buffer_type")
            distance = params.get("distance")
            unit = params.get("unit")

            # Execute Enrich Layer
            arcpy.ba.EnrichLayer(in_features, out_feature_class, variables, buffer_type, distance, unit)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def find_nearby_locations(self, params):
        """Find Nearby Locations

Identifies locations closest to the input features based on a selected distance type. The number of points in the output is defined by limiting the count or percentage of location points to return or by limiting the distance from the input points.

        params: {"in_features": <Feature Layer>, "id_field": <Field>, "in_location_points": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            id_field = params.get("id_field")
            if id_field is None:
                return {"success": False, "error": "id_field parameter is required"}
            in_location_points = params.get("in_location_points")
            if in_location_points is None:
                return {"success": False, "error": "in_location_points parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("FindNearbyLocations_Output", aprx.defaultGeodatabase)
            distance_type = params.get("distance_type")
            units = params.get("units")
            distance_limit = params.get("distance_limit")
            number_limit = params.get("number_limit")
            if number_limit is None:
                return {"success": False, "error": "number_limit parameter is required"}
            percent_limit = params.get("percent_limit")
            if percent_limit is None:
                return {"success": False, "error": "percent_limit parameter is required"}
            create_report = params.get("create_report")
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")
            report_fields = params.get("report_fields")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")
            location_name = params.get("location_name")

            # Execute Find Nearby Locations
            arcpy.ba.FindNearbyLocations(in_features, id_field, in_location_points, out_feature_class, distance_type, units, distance_limit, number_limit, percent_limit, create_report, report_title, report_folder, report_format, report_fields, travel_direction, time_of_day, time_zone, search_tolerance, location_name)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_desire_lines(self, params):
        """Generate Desire Lines

Generates a series of lines from each customer to an associated store location. These lines are often called spider diagrams. The tool can also generate an optional Wind Rose report from the output. Note:This tool is similar to the Generate Origin-Destination Links tool in the Analysis toolbox Proximity toolset.

        params: {"in_stores_layer": <Feature Layer>, "in_customers_layer": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_stores_layer = params.get("in_stores_layer")
            if in_stores_layer is None:
                return {"success": False, "error": "in_stores_layer parameter is required"}
            in_customers_layer = params.get("in_customers_layer")
            if in_customers_layer is None:
                return {"success": False, "error": "in_customers_layer parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GenerateDesireLines_Output", aprx.defaultGeodatabase)
            store_id_field = params.get("store_id_field")
            if store_id_field is None:
                return {"success": False, "error": "store_id_field parameter is required"}
            link_field = params.get("link_field")
            if link_field is None:
                return {"success": False, "error": "link_field parameter is required"}
            distance_type = params.get("distance_type")
            units = params.get("units")
            cutoff = params.get("cutoff")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            create_report = params.get("create_report")
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")

            # Execute Generate Desire Lines
            arcpy.ba.GenerateDesireLines(in_stores_layer, in_customers_layer, out_feature_class, store_id_field, link_field, distance_type, units, cutoff, travel_direction, time_of_day, time_zone, create_report, report_title, report_folder, report_format)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_grids_and_hexagons(self, params):
        """Generate Grids and Hexagons

Creates features with vector-based square grid cells, hexagons, or H3 hexagons for a given area.

        params: {"area_of_interest": <Feature Layer>, "out_feature_class": <Feature Class>, "cell_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            area_of_interest = params.get("area_of_interest")
            if area_of_interest is None:
                return {"success": False, "error": "area_of_interest parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GenerateGridsAndHexagons_Output", aprx.defaultGeodatabase)
            cell_type = params.get("cell_type")
            enrich_type = params.get("enrich_type")
            cell_size = params.get("cell_size")
            h3_resolution = params.get("h3_resolution")
            variables = params.get("variables")
            distance_type = params.get("distance_type")
            distance = params.get("distance")
            units = params.get("units")
            out_enriched_buffers = params.get("out_enriched_buffers")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")
            polygon_detail = params.get("polygon_detail")
            out_centroids = params.get("out_centroids")

            # Execute Generate Grids and Hexagons
            arcpy.ba.GenerateGridsAndHexagons(area_of_interest, out_feature_class, cell_type, enrich_type, cell_size, h3_resolution, variables, distance_type, distance, units, out_enriched_buffers, travel_direction, time_of_day, time_zone, search_tolerance, polygon_detail, out_centroids)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_points_from_business_listings(self, params):
        """Generate Points from Business Listings

Generates a point feature layer from a business point location search.

        params: {"out_feature_class": <Feature Class>, "in_search_features": <Feature Layer>, "search_terms": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromBusinessListings_Output", aprx.defaultGeodatabase)
            in_search_features = params.get("in_search_features")
            search_terms = params.get("search_terms")
            exact_match = params.get("exact_match")
            match_name_only = params.get("match_name_only")
            filters = params.get("filters")
            max_count = params.get("max_count")
            business_dataset = params.get("business_dataset")
            find_related_poi = params.get("find_related_poi")
            if find_related_poi is None:
                return {"success": False, "error": "find_related_poi parameter is required"}
            style = params.get("style")

            # Execute Generate Points from Business Listings
            arcpy.ba.GeneratePointsFromBusinessListings(out_feature_class, in_search_features, search_terms, exact_match, match_name_only, filters, max_count, business_dataset, find_related_poi, style)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def huff_model(self, params):
        """Huff Model

Creates a probability surface to predict the sales potential of an area based on distance and an attractiveness factor.

        params: {"in_facility_features": <Feature Layer>, "facility_id_field": <Field>, "in_candidate_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_facility_features = params.get("in_facility_features")
            if in_facility_features is None:
                return {"success": False, "error": "in_facility_features parameter is required"}
            facility_id_field = params.get("facility_id_field")
            if facility_id_field is None:
                return {"success": False, "error": "facility_id_field parameter is required"}
            in_candidate_features = params.get("in_candidate_features")
            if in_candidate_features is None:
                return {"success": False, "error": "in_candidate_features parameter is required"}
            candidate_id_field = params.get("candidate_id_field")
            if candidate_id_field is None:
                return {"success": False, "error": "candidate_id_field parameter is required"}
            in_sales_potential_features = params.get("in_sales_potential_features")
            if in_sales_potential_features is None:
                return {"success": False, "error": "in_sales_potential_features parameter is required"}
            sales_potential_id_field = params.get("sales_potential_id_field")
            if sales_potential_id_field is None:
                return {"success": False, "error": "sales_potential_id_field parameter is required"}
            sales_potential_field = params.get("sales_potential_field")
            if sales_potential_field is None:
                return {"success": False, "error": "sales_potential_field parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("HuffModel_Output", aprx.defaultGeodatabase)
            attractiveness_variables = params.get("attractiveness_variables")
            if attractiveness_variables is None:
                return {"success": False, "error": "attractiveness_variables parameter is required"}
            distance_exponent = params.get("distance_exponent")
            if distance_exponent is None:
                return {"success": False, "error": "distance_exponent parameter is required"}
            distance_type = params.get("distance_type")
            distance_units = params.get("distance_units")
            out_distance_matrix = params.get("out_distance_matrix")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")

            # Execute Huff Model
            arcpy.ba.HuffModel(in_facility_features, facility_id_field, in_candidate_features, candidate_id_field, in_sales_potential_features, sales_potential_id_field, sales_potential_field, out_feature_class, attractiveness_variables, distance_exponent, distance_type, distance_units, out_distance_matrix, travel_direction, time_of_day, time_zone)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def huff_model_calibration(self, params):
        """Huff Model Calibration

Calculates exponent values for use in the Huff Model tool.

        params: {"in_facility_features": <Feature Layer>, "facility_id_field": <Field>, "in_customer_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_facility_features = params.get("in_facility_features")
            if in_facility_features is None:
                return {"success": False, "error": "in_facility_features parameter is required"}
            facility_id_field = params.get("facility_id_field")
            if facility_id_field is None:
                return {"success": False, "error": "facility_id_field parameter is required"}
            in_customer_features = params.get("in_customer_features")
            if in_customer_features is None:
                return {"success": False, "error": "in_customer_features parameter is required"}
            link_field = params.get("link_field")
            if link_field is None:
                return {"success": False, "error": "link_field parameter is required"}
            in_sales_potential_features = params.get("in_sales_potential_features")
            if in_sales_potential_features is None:
                return {"success": False, "error": "in_sales_potential_features parameter is required"}
            sales_potential_id_field = params.get("sales_potential_id_field")
            if sales_potential_id_field is None:
                return {"success": False, "error": "sales_potential_id_field parameter is required"}
            out_calibration = params.get("out_calibration")
            if out_calibration is None:
                return {"success": False, "error": "out_calibration parameter is required"}
            attractiveness_variables = params.get("attractiveness_variables")
            if attractiveness_variables is None:
                return {"success": False, "error": "attractiveness_variables parameter is required"}
            customer_weight_field = params.get("customer_weight_field")
            distance_type = params.get("distance_type")
            distance_units = params.get("distance_units")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")

            # Execute Huff Model Calibration
            arcpy.ba.HuffModelCalibration(in_facility_features, facility_id_field, in_customer_features, link_field, in_sales_potential_features, sales_potential_id_field, out_calibration, attractiveness_variables, customer_weight_field, distance_type, distance_units, travel_direction, time_of_day, time_zone)

            output_name = os.path.basename(out_calibration)
            # self._add_to_map(out_calibration) # Output is a table
            return {"success": True, "output_layer": output_name, "output_path": out_calibration}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_business_analyst_report_template(self, params):
        """Import Business Analyst Report Template

Imports an online report so that it can run locally using a locally installed ArcGIS Business Analyst dataset. This tool is the underlying engine that runs the Import Template interactive workflow from the Catalog pane. This tool is ideal for performing more advanced automated tasks, such as importing templates through Python scripting or programmatically modifying data paths. The Import Template workflow will run the tool in the background and add its information to the Geoprocessing history.

        params: {"online_report_template_id": <String>, "output_folder": <Folder>, "dataset_id": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            online_report_template_id = params.get("online_report_template_id")
            if online_report_template_id is None:
                return {"success": False, "error": "online_report_template_id parameter is required"}
            output_folder = params.get("output_folder")
            dataset_id = params.get("dataset_id")
            config = params.get("config")

            # Execute Import Business Analyst Report Template
            arcpy.ba.ImportBusinessAnalystReportTemplate(online_report_template_id, output_folder, dataset_id, config)

            return {"success": True}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def summary_reports(self, params):
        """Summary Reports

Creates infographic and summary reports for a boundary layer using standard or custom templates.

        params: {"in_features": <Feature Layer>, "report_templates": <String>, "reports_folder": <Folder>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            report_templates = params.get("report_templates")
            if report_templates is None:
                return {"success": False, "error": "report_templates parameter is required"}
            reports_folder = params.get("reports_folder")
            if reports_folder is None:
                return {"success": False, "error": "reports_folder parameter is required"}
            summarization_options = params.get("summarization_options")
            single_report = params.get("single_report")
            formats = params.get("formats")
            store_id_field = params.get("store_id_field")
            store_name_field = params.get("store_name_field")
            store_address_field = params.get("store_address_field")
            store_latitude_field = params.get("store_latitude_field")
            store_longitude_field = params.get("store_longitude_field")
            ring_id_field = params.get("ring_id_field")
            area_description_field = params.get("area_description_field")
            title = params.get("title")
            subtitle = params.get("subtitle")
            report_per_feature = params.get("report_per_feature")
            add_infographic_header = params.get("add_infographic_header")
            add_infographic_footer = params.get("add_infographic_footer")
            add_infographic_data_source = params.get("add_infographic_data_source")
            report_style = params.get("report_style")

            # Execute Summary Reports
            arcpy.ba.SummaryReports(in_features, report_templates, reports_folder, summarization_options, single_report, formats, store_id_field, store_name_field, store_address_field, store_latitude_field, store_longitude_field, ring_id_field, area_description_field, title, subtitle, report_per_feature, add_infographic_header, add_infographic_footer, add_infographic_data_source, report_style)

            return {"success": True, "reports_folder": reports_folder}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_sdcx_index(self, params):
        """Generate SDCX Index

Creates an index for a Statistical Data Collection (SDCX). The index will improve performance when using the custom data in analysis tools such as Enrich Layer.

        params: {"sdcx_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            sdcx_file = params.get("sdcx_file")
            if sdcx_file is None:
                return {"success": False, "error": "sdcx_file parameter is required"}

            # Execute Generate SDCX Index
            arcpy.ba.GenerateSDCXIndex(sdcx_file)

            return {"success": True}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_field_based_suitability_criteria(self, params):
        """Add Field Based Suitability Criteria

Adds criteria based on the numerical fields existing in the input layer.

        params: {"in_analysis_layer": <Feature Layer; Group Layer>, "fields": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}
            fields = params.get("fields")
            if fields is None:
                return {"success": False, "error": "fields parameter is required"}

            # Execute Add Field Based Suitability Criteria
            arcpy.ba.AddFieldBasedSuitabilityCriteria(in_analysis_layer, fields)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_point_layer_based_suitability_criteria(self, params):
        """Add Point Layer Based Suitability Criteria

Adds criteria based on spatial relationships between the input layer and a specified point layer.

        params: {"in_analysis_layer": <Feature Layer; Group Layer>, "site_layer_id_field": <String>, "in_point_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}
            site_layer_id_field = params.get("site_layer_id_field")
            if site_layer_id_field is None:
                return {"success": False, "error": "site_layer_id_field parameter is required"}
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            criteria_type = params.get("criteria_type")
            if criteria_type is None:
                return {"success": False, "error": "criteria_type parameter is required"}
            distance_type = params.get("distance_type")
            units = params.get("units")
            in_site_centers_features = params.get("in_site_centers_features")
            site_centers_id_field = params.get("site_centers_id_field")
            weight_field = params.get("weight_field")
            if weight_field is None:
                return {"success": False, "error": "weight_field parameter is required"}
            statistics_type = params.get("statistics_type")
            cutoff_distance = params.get("cutoff_distance")

            # Execute Add Point Layer Based Suitability Criteria
            arcpy.ba.AddPointLayerBasedSuitabilityCriteria(in_analysis_layer, site_layer_id_field, in_point_features, criteria_type, distance_type, units, in_site_centers_features, site_centers_id_field, weight_field, statistics_type, cutoff_distance)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_variable_based_suitability_criteria(self, params):
        """Add Variable Based Suitability Criteria

Adds criteria based on the values calculated for the input layer using the Enrich Layer tool.

        params: {"in_analysis_layer": <Feature Layer; Group Layer>, "variables": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}
            variables = params.get("variables")
            if variables is None:
                return {"success": False, "error": "variables parameter is required"}

            # Execute Add Variable Based Suitability Criteria
            arcpy.ba.AddVariableBasedSuitabilityCriteria(in_analysis_layer, variables)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_suitability_score(self, params):
        """Calculate Suitability Score

Calculates or recalculates a suitability score.

        params: {"in_analysis_layer": <Feature Layer; Group Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}

            # Execute Calculate Suitability Score
            arcpy.ba.CalculateSuitabilityScore(in_analysis_layer)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_suitability_analysis_layer(self, params):
        """Make Suitability Analysis Layer

Creates a Suitability Analysis group layer for an input site's polygonal layer.

        params: {"in_features": <Feature Layer>, "layer_name": <String>, "out_dataset_path": <Workspace>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}
            out_dataset_path = params.get("out_dataset_path")
            out_dataset_name = params.get("out_dataset_name")

            # Execute Make Suitability Analysis Layer
            result = arcpy.ba.MakeSuitabilityAnalysisLayer(in_features, layer_name, out_dataset_path, out_dataset_name)

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer)
            return {"success": True, "output_layer": layer_name}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_suitability_criteria(self, params):
        """Remove Suitability Criteria

Removes criteria from a suitability analysis layer.

        params: {"in_analysis_layer": <Feature Layer; Group Layer>, "drop_criteria": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}
            drop_criteria = params.get("drop_criteria")
            if drop_criteria is None:
                return {"success": False, "error": "drop_criteria parameter is required"}

            # Execute Remove Suitability Criteria
            arcpy.ba.RemoveSuitabilityCriteria(in_analysis_layer, drop_criteria)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_criteria_properties(self, params):
        """Set Criteria Properties

Defines parameters for criteria.

        params: {"in_analysis_layer": <Feature Layer; Group Layer>, "criteria_propertiescriterion_title_weight_influence_ideal_value_minimum_value_maximum_value_enabled": <Value Table>, "criteria_score_preset": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}
            criteria_properties = params.get("criteria_properties")
            if criteria_properties is None:
                return {"success": False, "error": "criteria_properties parameter is required"}
            criteria_score_preset = params.get("criteria_score_preset")
            preprocessing = params.get("preprocessing")
            criteria_score_method = params.get("criteria_score_method")
            final_score_method = params.get("final_score_method")

            # Execute Set Criteria Properties
            arcpy.ba.SetCriteriaProperties(in_analysis_layer, criteria_properties, criteria_score_preset, preprocessing, criteria_score_method, final_score_method)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_target_site(self, params):
        """Set Target Site

Adds a target site to a Suitability Analysis group layer. A target site is typically a trade area around a high-performing location, such as a store or clinic. Criteria values in the target site are used to score candidate sites that are closest in value to the target site.

        params: {"in_analysis_layer": <Group Layer; Feature Dataset>, "target_site_layer": <Feature Layer>, "target_site_feature_id": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_analysis_layer = params.get("in_analysis_layer")
            if in_analysis_layer is None:
                return {"success": False, "error": "in_analysis_layer parameter is required"}
            target_site_layer = params.get("target_site_layer")
            target_site_feature_id = params.get("target_site_feature_id")

            # Execute Set Target Site
            arcpy.ba.SetTargetSite(in_analysis_layer, target_site_layer, target_site_feature_id)

            return {"success": True, "output_layer": in_analysis_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze_market_area_gap(self, params):
        """Analyze Market Area Gap

Generates a layer that displays the gap between total customers and expected customers. Learn more about Analyze Market Area Gap outputs

        params: {"customer_layer": <Feature Layer>, "target_profile": <File>, "base_profile": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            customer_layer = params.get("customer_layer")
            if customer_layer is None:
                return {"success": False, "error": "customer_layer parameter is required"}
            target_profile = params.get("target_profile")
            if target_profile is None:
                return {"success": False, "error": "target_profile parameter is required"}
            base_profile = params.get("base_profile")
            if base_profile is None:
                return {"success": False, "error": "base_profile parameter is required"}
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("AnalyzeMarketAreaGap_Output", aprx.defaultGeodatabase)
            target_group = params.get("target_group")
            if target_group is None:
                return {"success": False, "error": "target_group parameter is required"}
            core_target = params.get("core_target")
            if core_target is None:
                return {"success": False, "error": "core_target parameter is required"}
            developmental_target = params.get("developmental_target")
            if developmental_target is None:
                return {"success": False, "error": "developmental_target parameter is required"}
            boundary_layer = params.get("boundary_layer")
            create_report = params.get("create_report")
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")

            # Execute Analyze Market Area Gap
            arcpy.ba.AnalyzeMarketAreaGap(customer_layer, target_profile, base_profile, geography_level, out_feature_class, target_group, core_target, developmental_target, boundary_layer, create_report, report_title, report_folder, report_format)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze_market_potential(self, params):
        """Analyze Market Potential

Generates a layer that displays expected customers by a selected geography level. Learn more about Analyze Market Potential outputs

        params: {"target_profile": <File>, "base_profile": <File>, "geography_level": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            target_profile = params.get("target_profile")
            if target_profile is None:
                return {"success": False, "error": "target_profile parameter is required"}
            base_profile = params.get("base_profile")
            if base_profile is None:
                return {"success": False, "error": "base_profile parameter is required"}
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("AnalyzeMarketPotential_Output", aprx.defaultGeodatabase)
            boundary_layer = params.get("boundary_layer")
            create_report = params.get("create_report")
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")

            # Execute Analyze Market Potential
            arcpy.ba.AnalyzeMarketPotential(target_profile, base_profile, geography_level, out_feature_class, boundary_layer, create_report, report_title, report_folder, report_format)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_target_group(self, params):
        """Create Target Group

Creates a new target group. A target group is a container for targets that you create, name, and populate with segments from a locally installed Business Analyst dataset.

        params: {"target_group": <File>, "input_type": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            target_group = params.get("target_group")
            if target_group is None:
                return {"success": False, "error": "target_group parameter is required"}
            input_type = params.get("input_type")
            if input_type is None:
                return {"success": False, "error": "input_type parameter is required"}

            # Execute Create Target Group
            arcpy.ba.CreateTargetGroup(target_group, input_type)

            return {"success": True, "output_file": target_group}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_segmentation_profile(self, params):
        """Export Segmentation Profile

Exports a segmentation profile to a table.

        params: {"in_profile": <File>, "out_table_name": <Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_profile = params.get("in_profile")
            if in_profile is None:
                return {"success": False, "error": "in_profile parameter is required"}
            out_table_name = params.get("out_table_name")
            if out_table_name is None:
                return {"success": False, "error": "out_table_name parameter is required"}

            # Execute Export Segmentation Profile
            arcpy.ba.ExportSegmentationProfile(in_profile, out_table_name)

            output_name = os.path.basename(out_table_name)
            return {"success": True, "output_table": output_name, "output_path": out_table_name}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_customer_segmentation_profile(self, params):
        """Generate Customer Segmentation Profile

Creates a segmentation profile with an existing customer layer.

        params: {"in_customers_layer": <Feature Layer>, "in_segmentation_base": <String>, "out_profile": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_customers_layer = params.get("in_customers_layer")
            if in_customers_layer is None:
                return {"success": False, "error": "in_customers_layer parameter is required"}
            in_segmentation_base = params.get("in_segmentation_base")
            if in_segmentation_base is None:
                return {"success": False, "error": "in_segmentation_base parameter is required"}
            out_profile = params.get("out_profile")
            if out_profile is None:
                return {"success": False, "error": "out_profile parameter is required"}
            in_volume_field = params.get("in_volume_field")

            # Execute Generate Customer Segmentation Profile
            arcpy.ba.GenerateCustomerSegmentationProfile(in_customers_layer, in_segmentation_base, out_profile, in_volume_field)

            return {"success": True, "output_file": out_profile}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_market_area_segmentation_profile(self, params):
        """Generate Market Area Segmentation Profile

Creates a segmentation profile by summarizing segments from standard geography boundaries within the input area.

        params: {"in_features": <Feature Layer>, "segmentation_base": <String>, "out_profile": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            segmentation_base = params.get("segmentation_base")
            if segmentation_base is None:
                return {"success": False, "error": "segmentation_base parameter is required"}
            out_profile = params.get("out_profile")
            if out_profile is None:
                return {"success": False, "error": "out_profile parameter is required"}

            # Execute Generate Market Area Segmentation Profile
            arcpy.ba.GenerateMarketAreaSegmentationProfile(in_features, segmentation_base, out_profile)

            return {"success": True, "output_file": out_profile}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_segmentation_profile_report(self, params):
        """Generate Segmentation Profile Report

Creates a report that displays segments of your customers and compares them to the study area (base profile).

        params: {"target_profile": <File>, "base_profile": <File>, "report_title": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            target_profile = params.get("target_profile")
            if target_profile is None:
                return {"success": False, "error": "target_profile parameter is required"}
            base_profile = params.get("base_profile")
            if base_profile is None:
                return {"success": False, "error": "base_profile parameter is required"}
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")

            # Execute Generate Segmentation Profile Report
            arcpy.ba.GenerateSegmentationProfileReport(target_profile, base_profile, report_title, report_folder, report_format)

            return {"success": True, "reports_folder": report_folder}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_survey_report_for_profile(self, params):
        """Generate Survey Report For Profile

Displays characteristics from the consumer survey data for your target profile to determine customer lifestyle habits and preferences.

        params: {"target_profile": <File>, "base_profile": <File>, "survey_category": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            target_profile = params.get("target_profile")
            if target_profile is None:
                return {"success": False, "error": "target_profile parameter is required"}
            base_profile = params.get("base_profile")
            if base_profile is None:
                return {"success": False, "error": "base_profile parameter is required"}
            survey_category = params.get("survey_category")
            if survey_category is None:
                return {"success": False, "error": "survey_category parameter is required"}
            report_folder = params.get("report_folder")
            if report_folder is None:
                return {"success": False, "error": "report_folder parameter is required"}
            sort_column = params.get("sort_column")
            sort_order = params.get("sort_order")
            report_title = params.get("report_title")
            report_format = params.get("report_format")

            # Execute Generate Survey Report For Profile
            arcpy.ba.GenerateSurveyReportForProfile(target_profile, base_profile, survey_category, report_folder, sort_column, sort_order, report_title, report_format)

            return {"success": True, "reports_folder": report_folder}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_survey_report_for_targets(self, params):
        """Generate Survey Report For Targets

Displays the top characteristics, in each of the selected survey categories, of your Core and Developmental target groups, as well as your overall customer profile.

        params: {"target_profile": <File>, "target_group": <File>, "core_target": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            target_profile = params.get("target_profile")
            if target_profile is None:
                return {"success": False, "error": "target_profile parameter is required"}
            target_group = params.get("target_group")
            if target_group is None:
                return {"success": False, "error": "target_group parameter is required"}
            core_target = params.get("core_target")
            if core_target is None:
                return {"success": False, "error": "core_target parameter is required"}
            developmental_target = params.get("developmental_target")
            if developmental_target is None:
                return {"success": False, "error": "developmental_target parameter is required"}
            report_folder = params.get("report_folder")
            if report_folder is None:
                return {"success": False, "error": "report_folder parameter is required"}
            report_type = params.get("report_type")
            survey_categories = params.get("survey_categories")
            report_title = params.get("report_title")
            report_format = params.get("report_format")

            # Execute Generate Survey Report For Targets
            arcpy.ba.GenerateSurveyReportForTargets(target_profile, target_group, core_target, developmental_target, report_folder, report_type, survey_categories, report_title, report_format)

            return {"success": True, "reports_folder": report_folder}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_target_group_layer(self, params):
        """Generate Target Group Layer

Generates a layer that identifies geographies that contain selected segments and categorized groups based on targets.

        params: {"geography_level": <String>, "segmentation_base": <String>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            segmentation_base = params.get("segmentation_base")
            if segmentation_base is None:
                return {"success": False, "error": "segmentation_base parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            target_group = params.get("target_group")
            if target_group is None:
                return {"success": False, "error": "target_group parameter is required"}
            boundary_layer = params.get("boundary_layer")

            # Execute Generate Target Group Layer
            arcpy.ba.GenerateTargetGroupLayer(geography_level, segmentation_base, out_feature_class, target_group, boundary_layer)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_target_layer(self, params):
        """Generate Target Layer

Creates a layer that identifies geographies that contain selected segments and geographies that do not contain selected segments.

        params: {"geography_level": <String>, "segmentation_base": <String>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            segmentation_base = params.get("segmentation_base")
            if segmentation_base is None:
                return {"success": False, "error": "segmentation_base parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            input_type = params.get("input_type")
            if input_type is None:
                return {"success": False, "error": "input_type parameter is required"}
            target_group = params.get("target_group")
            target = params.get("target")
            segments = params.get("segments")
            boundary_layer = params.get("boundary_layer")

            # Execute Generate Target Layer
            arcpy.ba.GenerateTargetLayer(geography_level, segmentation_base, out_feature_class, input_type, target_group, target, segments, boundary_layer)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_target_penetration_layer(self, params):
        """Generate Target Penetration Layer

Generates a layer based on the percent of penetration of selected segments, providing a detailed view of the concentrations of the target segments.

        params: {"geography_level": <String>, "segmentation_base": <String>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            segmentation_base = params.get("segmentation_base")
            if segmentation_base is None:
                return {"success": False, "error": "segmentation_base parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            input_type = params.get("input_type")
            if input_type is None:
                return {"success": False, "error": "input_type parameter is required"}
            target_group = params.get("target_group")
            target = params.get("target")
            segments = params.get("segments")
            boundary_layer = params.get("boundary_layer")

            # Execute Generate Target Penetration Layer
            arcpy.ba.GenerateTargetPenetrationLayer(geography_level, segmentation_base, out_feature_class, input_type, target_group, target, segments, boundary_layer)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_segmentation_profile(self, params):
        """Import Segmentation Profile

Generates a segmentation profile from a table.

        params: {"in_table": <Table View>, "segmentation_base": <String>, "out_profile": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            segmentation_base = params.get("segmentation_base")
            if segmentation_base is None:
                return {"success": False, "error": "segmentation_base parameter is required"}
            out_profile = params.get("out_profile")
            if out_profile is None:
                return {"success": False, "error": "out_profile parameter is required"}
            segment_id_field = params.get("segment_id_field")
            if segment_id_field is None:
                return {"success": False, "error": "segment_id_field parameter is required"}
            count_field = params.get("count_field")
            if count_field is None:
                return {"success": False, "error": "count_field parameter is required"}
            total_volume_field = params.get("total_volume_field")

            # Execute Import Segmentation Profile
            arcpy.ba.ImportSegmentationProfile(in_table, segmentation_base, out_profile, segment_id_field, count_field, total_volume_field)

            return {"success": True, "output_file": out_profile}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_survey_profiles(self, params):
        """Import Survey Profiles

Imports segmentation profiles consisting of survey variable data.

        params: {"profiles": <String>, "out_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            profiles = params.get("profiles")
            if profiles is None:
                return {"success": False, "error": "profiles parameter is required"}
            out_folder = params.get("out_folder")
            if out_folder is None:
                return {"success": False, "error": "out_folder parameter is required"}

            # Execute Import Survey Profiles
            arcpy.ba.ImportSurveyProfiles(profiles, out_folder)

            return {"success": True, "output_folder": out_folder}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def assign_customers_by_distance(self, params):
        """Assign Customers By Distance

Assigns customers to the closest store based on a selected distance type.

        params: {"in_features": <Feature Layer>, "in_store_features": <Feature Layer>, "store_id_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            in_store_features = params.get("in_store_features")
            if in_store_features is None:
                return {"success": False, "error": "in_store_features parameter is required"}
            store_id_field = params.get("store_id_field")
            if store_id_field is None:
                return {"success": False, "error": "store_id_field parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            link_field = params.get("link_field")
            distance_type = params.get("distance_type")
            distance_units = params.get("distance_units")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")

            # Execute Assign Customers By Distance
            arcpy.ba.AssignCustomersByDistance(in_features, in_store_features, store_id_field, out_feature_class, link_field, distance_type, distance_units, travel_direction, time_of_day, time_zone, search_tolerance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_approximate_drive_times(self, params):
        """Generate Approximate Drive Times

Creates trade areas that approximate the size, shape, and area of existing polygons using available routes from the selected distance type.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "distance_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            distance_type = params.get("distance_type")
            if distance_type is None:
                return {"success": False, "error": "distance_type parameter is required"}
            units = params.get("units")
            in_stores_layer = params.get("in_stores_layer")
            store_id_field = params.get("store_id_field")
            link_field = params.get("link_field")
            iterations_limit = params.get("iterations_limit")
            minimum_step = params.get("minimum_step")
            target_percent_diff = params.get("target_percent_diff")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")
            polygon_detail = params.get("polygon_detail")

            # Execute Generate Approximate Drive Times
            arcpy.ba.GenerateApproximateDriveTimes(in_features, out_feature_class, distance_type, units, in_stores_layer, store_id_field, link_field, iterations_limit, minimum_step, target_percent_diff, travel_direction, time_of_day, time_zone, search_tolerance, polygon_detail)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_customer_derived_trade_areas(self, params):
        """Generate Customer Derived Trade Areas

Creates trade areas around stores based on the number of customers or volume attribute of each customer.

        params: {"in_stores_layer": <Feature Layer>, "store_id_field": <Field>, "in_customers_layer": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_stores_layer = params.get("in_stores_layer")
            if in_stores_layer is None:
                return {"success": False, "error": "in_stores_layer parameter is required"}
            store_id_field = params.get("store_id_field")
            if store_id_field is None:
                return {"success": False, "error": "store_id_field parameter is required"}
            in_customers_layer = params.get("in_customers_layer")
            if in_customers_layer is None:
                return {"success": False, "error": "in_customers_layer parameter is required"}
            link_field = params.get("link_field")
            if link_field is None:
                return {"success": False, "error": "link_field parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            method = params.get("method")
            if method is None:
                return {"success": False, "error": "method parameter is required"}
            rings = params.get("rings")
            if rings is None:
                return {"success": False, "error": "rings parameter is required"}
            customer_aggregation_type = params.get("customer_aggregation_type")
            if customer_aggregation_type is None:
                return {"success": False, "error": "customer_aggregation_type parameter is required"}
            customer_weight_field = params.get("customer_weight_field")
            exclude_outlying_customers = params.get("exclude_outlying_customers")
            cutoff_distance = params.get("cutoff_distance")
            dissolve_option = params.get("dissolve_option")
            use_customer_centroids = params.get("use_customer_centroids")
            distance_type = params.get("distance_type")
            units = params.get("units")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")
            polygon_detail = params.get("polygon_detail")
            iterations_limit = params.get("iterations_limit")
            minimum_step = params.get("minimum_step")
            target_percent_diff = params.get("target_percent_diff")

            # Execute Generate Customer Derived Trade Areas
            arcpy.ba.GenerateCustomerDerivedTradeAreas(in_stores_layer, store_id_field, in_customers_layer, link_field, out_feature_class, method, rings, customer_aggregation_type, customer_weight_field, exclude_outlying_customers, cutoff_distance, dissolve_option, use_customer_centroids, distance_type, units, travel_direction, time_of_day, time_zone, search_tolerance, polygon_detail, iterations_limit, minimum_step, target_percent_diff)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_drive_time_trade_area(self, params):
        """Generate Drive Time Trade Area

Creates a feature class of trade areas around point features based on travel time and distance.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "distance_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            distance_type = params.get("distance_type")
            if distance_type is None:
                return {"success": False, "error": "distance_type parameter is required"}
            distances = params.get("distances")
            if distances is None:
                return {"success": False, "error": "distances parameter is required"}
            units = params.get("units")
            id_field = params.get("id_field")
            dissolve_option = params.get("dissolve_option")
            remove_overlap = params.get("remove_overlap")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")
            polygon_detail = params.get("polygon_detail")
            input_method = params.get("input_method")
            expression = params.get("expression")

            # Execute Generate Drive Time Trade Area
            arcpy.ba.GenerateDriveTimeTradeArea(in_features, out_feature_class, distance_type, distances, units, id_field, dissolve_option, remove_overlap, travel_direction, time_of_day, time_zone, search_tolerance, polygon_detail, input_method, expression)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_geographies_from_overlay(self, params):
        """Generate Geographies From Overlay

Generates trade areas from the features of an input standard geography level that has a specified spatial relationship with the input.

        params: {"geography_level": <String>, "in_features": <Feature Layer>, "id_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            id_field = params.get("id_field")
            if id_field is None:
                return {"success": False, "error": "id_field parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            overlap_type = params.get("overlap_type")
            ratios = params.get("ratios")

            # Execute Generate Geographies From Overlay
            arcpy.ba.GenerateGeographiesFromOverlay(geography_level, in_features, id_field, out_feature_class, overlap_type, ratios)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_standard_geography_trade_areas(self, params):
        """Generate Standard Geography Trade Areas

Creates trade areas based on predefined named statistical areas. This tool does not consume credits.

        params: {"geography_level": <String>, "out_feature_class": <Feature Class>, "input_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            geography_level = params.get("geography_level")
            if geography_level is None:
                return {"success": False, "error": "geography_level parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            input_type = params.get("input_type")
            in_ids_table = params.get("in_ids_table")
            geography_key_field = params.get("geography_key_field")
            ids_list = params.get("ids_list")
            summarize_duplicates = params.get("summarize_duplicates")
            group_field = params.get("group_field")
            dissolve_output = params.get("dissolve_output")

            # Execute Generate Standard Geography Trade Areas
            arcpy.ba.GenerateStandardGeographyTradeAreas(geography_level, out_feature_class, input_type, in_ids_table, geography_key_field, ids_list, summarize_duplicates, group_field, dissolve_output)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_threshold_drive_times(self, params):
        """Generate Threshold Drive Times

Creates a feature class of network distance trade areas that expand around point features until criteria is reached.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "threshold_variable": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            threshold_variable = params.get("threshold_variable")
            if threshold_variable is None:
                return {"success": False, "error": "threshold_variable parameter is required"}
            threshold_values = params.get("threshold_values")
            if threshold_values is None:
                return {"success": False, "error": "threshold_values parameter is required"}
            distance_type = params.get("distance_type")
            if distance_type is None:
                return {"success": False, "error": "distance_type parameter is required"}
            units = params.get("units")
            id_field = params.get("id_field")
            travel_direction = params.get("travel_direction")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            search_tolerance = params.get("search_tolerance")
            polygon_detail = params.get("polygon_detail")
            iterations_limit = params.get("iterations_limit")
            minimum_step = params.get("minimum_step")
            target_percent_diff = params.get("target_percent_diff")
            input_method = params.get("input_method")
            expression = params.get("expression")

            # Execute Generate Threshold Drive Times
            arcpy.ba.GenerateThresholdDriveTimes(in_features, out_feature_class, threshold_variable, threshold_values, distance_type, units, id_field, travel_direction, time_of_day, time_zone, search_tolerance, polygon_detail, iterations_limit, minimum_step, target_percent_diff, input_method, expression)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_threshold_rings(self, params):
        """Generate Threshold Rings

Creates a feature class of ring trade areas that expand around point features until the threshold value is reached.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "threshold_variable": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            threshold_variable = params.get("threshold_variable")
            if threshold_variable is None:
                return {"success": False, "error": "threshold_variable parameter is required"}
            threshold_values = params.get("threshold_values")
            if threshold_values is None:
                return {"success": False, "error": "threshold_values parameter is required"}
            units = params.get("units")
            id_field = params.get("id_field")
            input_method = params.get("input_method")
            expression = params.get("expression")
            minimum_step = params.get("minimum_step")
            target_percent_diff = params.get("target_percent_diff")

            # Execute Generate Threshold Rings
            arcpy.ba.GenerateThresholdRings(in_features, out_feature_class, threshold_variable, threshold_values, units, id_field, input_method, expression, minimum_step, target_percent_diff)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_trade_area_rings(self, params):
        """Generate Trade Area Rings

Creates rings around point locations.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "radii": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            radii = params.get("radii")
            units = params.get("units")
            id_field = params.get("id_field")
            remove_overlap = params.get("remove_overlap")
            dissolve_option = params.get("dissolve_option")
            input_method = params.get("input_method")
            expression = params.get("expression")

            # Execute Generate Trade Area Rings
            arcpy.ba.GenerateTradeAreaRings(in_features, out_feature_class, radii, units, id_field, remove_overlap, dissolve_option, input_method, expression)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def measure_cannibalization(self, params):
        """Measure Cannibalization

Calculates the amount of overlap between two or more polygons. Overlap refers to the extent of the polygons beyond intersection. An optional report can be created detailing overlapped statistics.

        params: {"in_features": <Feature Layer>, "area_id_field": <Field>, "area_description_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            area_id_field = params.get("area_id_field")
            if area_id_field is None:
                return {"success": False, "error": "area_id_field parameter is required"}
            area_description_field = params.get("area_description_field")
            if area_description_field is None:
                return {"success": False, "error": "area_description_field parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            store_id_field = params.get("store_id_field")
            create_report = params.get("create_report")
            report_title = params.get("report_title")
            report_folder = params.get("report_folder")
            report_format = params.get("report_format")
            variables = params.get("variables")

            # Execute Measure Cannibalization
            arcpy.ba.MeasureCannibalization(in_features, area_id_field, area_description_field, out_feature_class, store_id_field, create_report, report_title, report_folder, report_format, variables)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_overlap(self, params):
        """Remove Overlap

Removes overlap between two or more areas to form adjacent boundaries.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            method = params.get("method")
            define_trade_area = params.get("define_trade_area")
            ring_id_field = params.get("ring_id_field")
            weight_field = params.get("weight_field")
            store_id = params.get("store_id")
            in_stores_layer = params.get("in_stores_layer")
            link_field = params.get("link_field")

            # Execute Remove Overlap
            arcpy.ba.RemoveOverlap(in_features, out_feature_class, method, define_trade_area, ring_id_field, weight_field, store_id, in_stores_layer, link_field)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_overlap_multiple(self, params):
        """Remove Overlap (multiple)

Removes overlap between polygons contained in multiple input layers.

        params: {"in_features": <Value Table>, "out_feature_class": <Feature Class>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            method = params.get("method")
            join_attributes = params.get("join_attributes")

            # Execute Remove Overlap (multiple)
            arcpy.ba.RemoveOverlap(in_features, out_feature_class, method, join_attributes)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}