import arcpy
import os

class AnalysisTools:
    """A collection of analysis tools generated from ArcGIS Pro documentation."""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def select(self, params):
        """
        Extracts features from an input feature class or input feature layer, 
        typically using a select or SQL expression, and stores them in an output feature class.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Select_Output", aprx.defaultGeodatabase)
            
            where_clause = params.get("where_clause")

            arcpy.analysis.Select(in_features, out_feature_class, where_clause)
            
            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def table_select(self, params):
        """
        Selects table records matching a Structured Query Language (SQL) expression and writes them to an output table.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            out_table = params.get("out_table")
            if out_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("TableSelect_Output", aprx.defaultGeodatabase)

            where_clause = params.get("where_clause")

            arcpy.analysis.TableSelect(in_table, out_table, where_clause)
            
            output_name = os.path.basename(out_table)
            # self._add_to_map(out_table) # Tables are not added to map in the same way
            return {"success": True, "output_table": output_name, "output_path": out_table}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def split_by_attributes(self, params):
        """
        Splits an input dataset by unique attributes.
        """
        try:
            input_table = params.get("input_table")
            if input_table is None:
                return {"success": False, "error": "input_table parameter is required"}
            target_workspace = params.get("target_workspace")
            if target_workspace is None:
                return {"success": False, "error": "target_workspace parameter is required"}
            split_fields = params.get("split_fields")
            if split_fields is None:
                return {"success": False, "error": "split_fields parameter is required"}

            arcpy.analysis.SplitByAttributes(input_table, target_workspace, split_fields)

            return {"success": True, "message": f"Successfully split {input_table} into {target_workspace} by {split_fields}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def clip(self, params):
        """Clip

        Extracts input features that overlay the clip features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            clip_features = params.get("clip_features")
            if clip_features is None: return {"success": False, "error": "clip_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Clip_Output", aprx.defaultGeodatabase)

            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.analysis.Clip(in_features, clip_features, out_feature_class, cluster_tolerance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
        except Exception as e:
            return {"success": False, "error": str(e)}

    def split(self, params):
        """Split

        Splits an input with overlaying features to create a subset of output feature classes.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            split_features = params.get("split_features")
            if split_features is None: return {"success": False, "error": "split_features parameter is required"}
            split_field = params.get("split_field")
            if split_field is None: return {"success": False, "error": "split_field parameter is required"}
            out_workspace = params.get("out_workspace")
            if out_workspace is None: return {"success": False, "error": "out_workspace parameter is required"}
            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.analysis.Split(in_features, split_features, split_field, out_workspace, cluster_tolerance)

        except Exception as e:
            return {"success": False, "error": str(e)}

    def symmetrical_difference(self, params):
        """Symmetrical Difference

        Computes a geometric intersection of the input and update features, returning the input features and update features that do not overlap.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            update_features = params.get("update_features")
            if update_features is None: return {"success": False, "error": "update_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("SymmetricalDifference_Output", aprx.defaultGeodatabase)
            
            join_attributes = params.get("join_attributes", "ALL")
            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.analysis.SymDiff(in_features, update_features, out_feature_class, join_attributes, cluster_tolerance)

        except Exception as e:
            return {"success": False, "error": str(e)}

    def update(self, params):
        """Update

        Computes the geometric intersection of the input features and update features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            update_features = params.get("update_features")
            if update_features is None: return {"success": False, "error": "update_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Update_Output", aprx.defaultGeodatabase)
            
            keep_borders = params.get("keep_borders", "BORDERS")
            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.analysis.Update(in_features, update_features, out_feature_class, keep_borders, cluster_tolerance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
        except Exception as e:
            return {"success": False, "error": str(e)}

    def intersect(self, params):
        """Intersect

        Computes a geometric intersection of the input features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Intersect_Output", aprx.defaultGeodatabase)
            
            join_attributes = params.get("join_attributes", "ALL")
            cluster_tolerance = params.get("cluster_tolerance")
            output_type = params.get("output_type", "INPUT")

            arcpy.analysis.Intersect(in_features, out_feature_class, join_attributes, cluster_tolerance, output_type)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def erase(self, params):
        """Erase

        Creates a feature class by overlaying the input features with the erase features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            erase_features = params.get("erase_features")
            if erase_features is None: return {"success": False, "error": "erase_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Erase_Output", aprx.defaultGeodatabase)
            
            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.analysis.Erase(in_features, erase_features, out_feature_class, cluster_tolerance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def union(self, params):
        """Union

        Computes a geometric union of the input features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Union_Output", aprx.defaultGeodatabase)
            
            join_attributes = params.get("join_attributes", "ALL")
            cluster_tolerance = params.get("cluster_tolerance")
            gaps = params.get("gaps", "GAPS")

            arcpy.analysis.Union(in_features, out_feature_class, join_attributes, cluster_tolerance, gaps)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def identity(self, params):
        """Identity

        Computes a geometric intersection of the input features and identity features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            identity_features = params.get("identity_features")
            if identity_features is None: return {"success": False, "error": "identity_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Identity_Output", aprx.defaultGeodatabase)
            
            join_attributes = params.get("join_attributes", "ALL")
            cluster_tolerance = params.get("cluster_tolerance")
            relationship = params.get("relationship", "NO_RELATIONSHIPS")

            arcpy.analysis.Identity(in_features, identity_features, out_feature_class, join_attributes, cluster_tolerance, relationship)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def frequency(self, params):
        """Frequency

        Reads a table and a set of fields and creates a new table containing unique field values and the number of occurrences of each unique field value.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None: return {"success": False, "error": "in_table parameter is required"}
            out_table = params.get("out_table")
            if out_table is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("Frequency_Output", aprx.defaultGeodatabase)
            
            frequency_fields = params.get("frequency_fields")
            if frequency_fields is None: return {"success": False, "error": "frequency_fields parameter is required"}
            summary_fields = params.get("summary_fields")

            arcpy.analysis.Frequency(in_table, out_table, frequency_fields, summary_fields)

            output_name = os.path.basename(out_table)
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def apportion_polygon(self, params):
        """Apportion Polygon

        Summarizes the attributes of an input polygon layer based on the spatial overlay of a target polygon layer and assigns the summarized attributes to the target polygons.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            apportion_fields = params.get("apportion_fieldsfield_statistic_type")
            if apportion_fields is None: return {"success": False, "error": "apportion_fields parameter is required"}
            target_features = params.get("target_features")
            if target_features is None: return {"success": False, "error": "target_features parameter is required"}
            out_features = params.get("out_features")
            if out_features is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_features = arcpy.CreateUniqueName("ApportionPolygon_Output", aprx.defaultGeodatabase)
            method = params.get("method", "AREA")
            estimation_features = params.get("estimation_features")
            weight_field = params.get("weight_field")
            maintain_geometries = params.get("maintain_geometries", "MAINTAIN_GEOMETRIES")

            arcpy.analysis.ApportionPolygon(in_features, apportion_fields, target_features, out_features, method, estimation_features, weight_field, maintain_geometries)

            output_name = os.path.basename(out_features)
            self._add_to_map(out_features)
            return {"success": True, "output_layer": output_name, "output_path": out_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def count_overlapping_features(self, params):
        """Count Overlapping Features

        Generates planarized overlapping features from the input features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("CountOverlapping_Output", aprx.defaultGeodatabase)
            min_overlap_count = params.get("min_overlap_count", 1)
            out_overlap_table = params.get("out_overlap_table")

            arcpy.analysis.CountOverlappingFeatures(in_features, out_feature_class, min_overlap_count, out_overlap_table)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def pairwise_dissolve(self, params):
        """Pairwise Dissolve

        Aggregates features based on specified attributes using a parallel processing approach.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("PairwiseDissolve_Output", aprx.defaultGeodatabase)
            dissolve_field = params.get("dissolve_field")
            statistics_fields = params.get("statistics_fieldsfield_statistic_type")
            multi_part = params.get("multi_part", "MULTI_PART")
            concatenation_separator = params.get("concatenation_separator", "")

            arcpy.analysis.PairwiseDissolve(in_features, out_feature_class, dissolve_field, statistics_fields, multi_part, concatenation_separator)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def pairwise_integrate(self, params):
        """Pairwise Integrate

        Analyzes the coordinate locations of feature vertices among features in one or more feature classes.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            cluster_tolerance = params.get("cluster_tolerance")
            if cluster_tolerance is None: return {"success": False, "error": "cluster_tolerance parameter is required"}

            arcpy.analysis.PairwiseIntegrate(in_features, cluster_tolerance)

            return {"success": True, "message": f"Successfully ran Pairwise Integrate on {in_features}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def pairwise_buffer(self, params):
        """Pairwise Buffer

        Creates buffer polygons around input features to a specified distance using a parallel processing approach.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("PairwiseBuffer_Output", aprx.defaultGeodatabase)
            buffer_distance_or_field = params.get("buffer_distance_or_field")
            if buffer_distance_or_field is None: return {"success": False, "error": "buffer_distance_or_field parameter is required"}
            dissolve_option = params.get("dissolve_option", "NONE")
            dissolve_field = params.get("dissolve_field")
            method = params.get("method", "PLANAR")
            max_deviation = params.get("max_deviation")

            arcpy.analysis.PairwiseBuffer(in_features, out_feature_class, buffer_distance_or_field, dissolve_option, dissolve_field, method, max_deviation)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def pairwise_clip(self, params):
        """Pairwise Clip

        Extracts input features that overlay the clip features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            clip_features = params.get("clip_features")
            if clip_features is None: return {"success": False, "error": "clip_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("PairwiseClip_Output", aprx.defaultGeodatabase)
            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.analysis.PairwiseClip(in_features, clip_features, out_feature_class, cluster_tolerance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def near(self, params):
        """Near

        Calculates distance and additional proximity information between the input features and the closest feature in another layer or feature class.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            near_features = params.get("near_features")
            if near_features is None: return {"success": False, "error": "near_features parameter is required"}
            search_radius = params.get("search_radius")
            location = params.get("location", "NO_LOCATION")
            angle = params.get("angle", "NO_ANGLE")
            method = params.get("method", "PLANAR")

            arcpy.analysis.Near(in_features, near_features, search_radius, location, angle, method)

            return {"success": True, "message": f"Near analysis complete on {in_features}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_thiessen_polygons(self, params):
        """Create Thiessen Polygons

        Creates Thiessen polygons from point features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("ThiessenPolygons_Output", aprx.defaultGeodatabase)
            fields_to_copy = params.get("fields_to_copy", "ALL")

            arcpy.analysis.CreateThiessenPolygons(in_features, out_feature_class, fields_to_copy)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_origin_destination_links(self, params):
        """Generate Origin-Destination Links

        Generates connecting lines from origin features to destination features.
        """
        try:
            origin_features = params.get("origin_features")
            if origin_features is None: return {"success": False, "error": "origin_features parameter is required"}
            destination_features = params.get("destination_features")
            if destination_features is None: return {"success": False, "error": "destination_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("ODLinks_Output", aprx.defaultGeodatabase)
            origin_group_field = params.get("origin_group_field")
            destination_group_field = params.get("destination_group_field")
            line_type = params.get("line_type", "STRAIGHT_LINE")
            num_nearest = params.get("num_nearest")
            search_distance = params.get("search_distance")

            arcpy.analysis.GenerateOriginDestinationLinks(origin_features, destination_features, out_feature_class, origin_group_field, destination_group_field, line_type, num_nearest, search_distance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def polygon_neighbors(self, params):
        """Polygon Neighbors

        Creates a table with statistics based on polygon contiguity.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_table = params.get("out_table")
            if out_table is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("PolygonNeighbors_Output", aprx.defaultGeodatabase)
            in_fields = params.get("in_fields")
            area_overlap = params.get("area_overlap", "NO_AREA_OVERLAP")
            both_sides = params.get("both_sides", "BOTH_SIDES")
            cluster_tolerance = params.get("cluster_tolerance")
            out_linear_units = params.get("out_linear_units", "DEFAULT")
            out_area_units = params.get("out_area_units", "DEFAULT")

            arcpy.analysis.PolygonNeighbors(in_features, out_table, in_fields, area_overlap, both_sides, cluster_tolerance, out_linear_units, out_area_units)

            output_name = os.path.basename(out_table)
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def multiple_ring_buffer(self, params):
        """Multiple Ring Buffer

        Creates multiple buffers at specified distances around the input features.
        """
        try:
            input_features = params.get("input_features")
            if input_features is None: return {"success": False, "error": "input_features parameter is required"}
            output_feature_class = params.get("output_feature_class")
            if output_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                output_feature_class = arcpy.CreateUniqueName("MultipleRingBuffer_Output", aprx.defaultGeodatabase)
            distances = params.get("distancesdistance")
            if distances is None: return {"success": False, "error": "distances parameter is required"}
            buffer_unit = params.get("buffer_unit")
            dissolve_option = params.get("dissolve_option", "NONE")
            outside_polygons_only = params.get("outside_polygons_only", "FULL")
            method = params.get("method", "GEODESIC")

            arcpy.analysis.MultipleRingBuffer(input_features, output_feature_class, distances, buffer_unit, dissolve_option, outside_polygons_only, method)

            output_name = os.path.basename(output_feature_class)
            self._add_to_map(output_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": output_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def graphic_buffer(self, params):
        """Graphic Buffer

        Creates buffer polygons around input features to a specified distance. 
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GraphicBuffer_Output", aprx.defaultGeodatabase)
            buffer_distance_or_field = params.get("buffer_distance_or_field")
            if buffer_distance_or_field is None: return {"success": False, "error": "buffer_distance_or_field parameter is required"}
            line_caps = params.get("line_caps", "ROUND")
            line_joins = params.get("line_joins", "ROUND")
            miter_limit = params.get("miter_limit")
            max_deviation = params.get("max_deviation")

            arcpy.analysis.GraphicBuffer(in_features, out_feature_class, buffer_distance_or_field, line_caps, line_joins, miter_limit, max_deviation)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_near_table(self, params):
        """Generate Near Table

        Calculates distances and other proximity information between features in one or more feature classes or layers.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            near_features = params.get("near_features")
            if near_features is None: return {"success": False, "error": "near_features parameter is required"}
            out_table = params.get("out_table")
            if out_table is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("GenerateNearTable_Output", aprx.defaultGeodatabase)
            search_radius = params.get("search_radius")
            location = params.get("location", "NO_LOCATION")
            angle = params.get("angle", "NO_ANGLE")
            closest = params.get("closest", "ALL")
            closest_count = params.get("closest_count", 0)
            method = params.get("method", "PLANAR")

            arcpy.analysis.GenerateNearTable(in_features, near_features, out_table, search_radius, location, angle, closest, closest_count, method)

            output_name = os.path.basename(out_table)
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def tabulate_intersection(self, params):
        """Tabulate Intersection

        Computes the intersection between two feature classes and cross tabulates the area, length, or count of the intersecting features.
        """
        try:
            in_zone_features = params.get("in_zone_features")
            if in_zone_features is None: return {"success": False, "error": "in_zone_features parameter is required"}
            zone_fields = params.get("zone_fields")
            if zone_fields is None: return {"success": False, "error": "zone_fields parameter is required"}
            in_class_features = params.get("in_class_features")
            if in_class_features is None: return {"success": False, "error": "in_class_features parameter is required"}
            out_table = params.get("out_table")
            if out_table is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("TabulateIntersection_Output", aprx.defaultGeodatabase)
            class_fields = params.get("class_fields")
            sum_fields = params.get("sum_fields")
            xy_tolerance = params.get("xy_tolerance")
            out_units = params.get("out_units", "UNKNOWN")

            arcpy.analysis.TabulateIntersection(in_zone_features, zone_fields, in_class_features, out_table, class_fields, sum_fields, xy_tolerance, out_units)

            output_name = os.path.basename(out_table)
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def summarize_within(self, params):
        """Summarize Within

        Overlays a polygon layer with another layer to summarize the number of points, length of the lines, or area of the polygons within each polygon.
        """
        try:
            in_polygons = params.get("in_polygons")
            if in_polygons is None: return {"success": False, "error": "in_polygons parameter is required"}
            in_sum_features = params.get("in_sum_features")
            if in_sum_features is None: return {"success": False, "error": "in_sum_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("SummarizeWithin_Output", aprx.defaultGeodatabase)
            keep_all_polygons = params.get("keep_all_polygons", "KEEP_ALL")
            sum_fields = params.get("sum_fieldssummary_field_statistic_type")
            sum_shape = params.get("sum_shape", "ADD_SHAPE_SUM")
            shape_unit = params.get("shape_unit", "METERS")
            group_field = params.get("group_field")
            add_min_maj = params.get("add_min_maj", "NO_MIN_MAJ")
            add_group_percent = params.get("add_group_percent", "NO_GROUP_PERCENT")
            out_group_table = params.get("out_group_table")

            arcpy.analysis.SummarizeWithin(in_polygons, in_sum_features, out_feature_class, keep_all_polygons, sum_fields, sum_shape, shape_unit, group_field, add_min_maj, add_group_percent, out_group_table)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def summary_statistics(self, params):
        """Summary Statistics

        Calculates summary statistics for fields in a table.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None: return {"success": False, "error": "in_table parameter is required"}
            out_table = params.get("out_table")
            if out_table is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("SummaryStatistics_Output", aprx.defaultGeodatabase)
            statistics_fields = params.get("statistics_fieldsfield_statistic_type")
            if statistics_fields is None: return {"success": False, "error": "statistics_fields parameter is required"}
            case_field = params.get("case_field")
            concatenation_separator = params.get("concatenation_separator", "")

            arcpy.analysis.Statistics(in_table, out_table, statistics_fields, case_field, concatenation_separator)

            output_name = os.path.basename(out_table)
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def enrich(self, params):
        """Enrich

        Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Enrich_Output", aprx.defaultGeodatabase)
            variables = params.get("variables")
            if variables is None: return {"success": False, "error": "variables parameter is required"}
            buffer_type = params.get("buffer_type")
            distance = params.get("distance")
            unit = params.get("unit")

            arcpy.analysis.Enrich(in_features, out_feature_class, variables, buffer_type, distance, unit)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def summarize_nearby(self, params):
        """Summarize Nearby

        Finds features that are within a specified distance of features in the input layer and calculates statistics for the nearby features.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            in_sum_features = params.get("in_sum_features")
            if in_sum_features is None: return {"success": False, "error": "in_sum_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("SummarizeNearby_Output", aprx.defaultGeodatabase)
            distance_type = params.get("distance_type")
            if distance_type is None: return {"success": False, "error": "distance_type parameter is required"}
            distances = params.get("distancesdistance")
            if distances is None: return {"success": False, "error": "distances parameter is required"}
            distance_units = params.get("distance_units")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone", "TIME_ZONE_AT_LOCATION")
            keep_all_polygons = params.get("keep_all_polygons", "KEEP_ALL")
            sum_fields = params.get("sum_fieldssummary_field_statistic_type")
            sum_shape = params.get("sum_shape", "ADD_SHAPE_SUM")
            shape_unit = params.get("shape_unit", "METERS")
            group_field = params.get("group_field")
            add_min_maj = params.get("add_min_maj", "NO_MIN_MAJ")
            add_group_percent = params.get("add_group_percent", "NO_GROUP_PERCENT")
            output_grouped_table = params.get("output_grouped_table")

            arcpy.analysis.SummarizeNearby(in_features, in_sum_features, out_feature_class, distance_type, distances, distance_units, time_of_day, time_zone, keep_all_polygons, sum_fields, sum_shape, shape_unit, group_field, add_min_maj, add_group_percent, output_grouped_table)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
