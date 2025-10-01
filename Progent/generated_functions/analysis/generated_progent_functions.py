# Generated ArcGIS Pro Analysis Tools Progent Functions
# Generated on 2025-10-01T11:38:01.346956
# Total tools: {len(progent_functions)}

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

    def select(self, params):
        """Select

Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select
            arcpy.Select(in_features, out_feature_class, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_select(self, params):
        """Table Select

Selects table records matching a Structured Query Language (SQL) expression and writes them to an output table.

        params: {"in_table": <Table View; Raster Layer>, "out_table": <Table>, "where_clause": <SQL Expression>}
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

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Table_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table Select
            arcpy.TableSelect(in_table, out_table, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def split_by_attributes(self, params):
        """Split By Attributes

Splits an input dataset by unique attributes.

        params: {"input_table": <Table View>, "target_workspace": <Workspace; Feature Dataset>, "split_fields": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{input_table.replace(' ', '_')}_Split_By_Attributes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Split By Attributes
            arcpy.SplitByAttributes(input_table, target_workspace, split_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def clip(self, params):
        """Clip

Extracts input features that overlay the clip features. Use this tool to cut out a piece of one dataset using one or more of the features in another dataset as a cookie cutter. This is particularly useful for creating a new dataset—also referred to as a study area or area of interest (AOI)—that contains a geographic subset of the features in another, larger dataset. Clip operations can also be performed using the Pairwise Clip tool.

        params: {"in_features": <Feature Layer; Scene Layer; File; Building Scene Layer>, "clip_features": <Feature Layer>, "out_feature_class": <Feature Class; File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    clip_features = params.get("clip_features")
    if clip_features is None:
        return {"success": False, "error": "clip_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Clip"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Clip
            arcpy.Clip(in_features, clip_features, out_feature_class, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def split(self, params):
        """Split

Splits an input with overlaying features to  create a subset of output feature classes.

        params: {"in_features": <Feature Layer>, "split_features": <Feature Layer>, "split_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    split_features = params.get("split_features")
    if split_features is None:
        return {"success": False, "error": "split_features parameter is required"}
    split_field = params.get("split_field")
    if split_field is None:
        return {"success": False, "error": "split_field parameter is required"}
    out_workspace = params.get("out_workspace")
    if out_workspace is None:
        return {"success": False, "error": "out_workspace parameter is required"}
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Split"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Split
            arcpy.Split(in_features, split_features, split_field, out_workspace, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select(self, params):
        """Select

Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select
            arcpy.Select(in_features, out_feature_class, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def assign_weights_by_pairwise_comparison(self, params):
        """Assign Weights By Pairwise Comparison

Calculates the relative weights for a set of input variables by comparing them in pairs. Learn more about how Assign Weights By Pairwise Comparison works

        params: {"input_variables": <String>, "out_table": <Table>, "add_comparison_matrix": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    input_variables = params.get("input_variables")
    if input_variables is None:
        return {"success": False, "error": "input_variables parameter is required"}
    out_table = params.get("out_table")
    if out_table is None:
        return {"success": False, "error": "out_table parameter is required"}
    add_comparison_matrix = params.get("add_comparison_matrix")
    comparison_matrix = params.get("comparison_matrix")

            # Generate output name and path
            output_name = f"{input_variables.replace(' ', '_')}_Assign_Weights_By_Pairwise_Comparison"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Assign Weights By Pairwise Comparison
            arcpy.AssignWeightsByPairwiseComparison(input_variables, out_table, add_comparison_matrix, comparison_matrix)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select(self, params):
        """Select

Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select
            arcpy.Select(in_features, out_feature_class, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def symmetrical_difference(self, params):
        """Symmetrical Difference

Computes a geometric intersection of the input and update features, returning the input features and update features that do not overlap. Features or portions of features in the input and update features that do not overlap will be written to the output feature class.

        params: {"in_features": <Feature Layer>, "update_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    update_features = params.get("update_features")
    if update_features is None:
        return {"success": False, "error": "update_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    join_attributes = params.get("join_attributes")
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Symmetrical_Difference"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Symmetrical Difference
            arcpy.SymmetricalDifference(in_features, update_features, out_feature_class, join_attributes, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def erase(self, params):
        """Erase

Creates a feature class by overlaying the input features with the erase features. Only those portions of the input features falling outside the erase features  are copied to the output feature class. An alternate tool is available for erase operations. See the Pairwise Erase tool documentation for details.

        params: {"in_features": <Feature Layer>, "erase_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    erase_features = params.get("erase_features")
    if erase_features is None:
        return {"success": False, "error": "erase_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Erase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Erase
            arcpy.Erase(in_features, erase_features, out_feature_class, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update(self, params):
        """Update

Computes the geometric intersection of the input features and update features. The attributes and geometry of the input features are updated by the update features in the output feature class.

        params: {"in_features": <Feature Layer>, "update_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    update_features = params.get("update_features")
    if update_features is None:
        return {"success": False, "error": "update_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    keep_borders = params.get("keep_borders")
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Update"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update
            arcpy.Update(in_features, update_features, out_feature_class, keep_borders, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def intersect(self, params):
        """Intersect

Computes a geometric intersection of the input features. Features or portions of features that overlap in all layers or feature classes will be written to the output feature class. An alternate tool is available for intersect operations. See the Pairwise Intersect tool documentation for details. The Pairwise Intersect tool is similar to this tool  in that geometric intersections are computed, but it is different in that intersections are computed on pairs of features rather than all combinations of features. Learn more about how Intersect works

        params: {"in_featuresin_features_rank": <Value Table>, "out_feature_class": <Feature Class>, "join_attributes": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_featuresin_features_rank = params.get("in_featuresin_features_rank")
    if in_featuresin_features_rank is None:
        return {"success": False, "error": "in_featuresin_features_rank parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    join_attributes = params.get("join_attributes")
    cluster_tolerance = params.get("cluster_tolerance")
    output_type = params.get("output_type")

            # Generate output name and path
            output_name = f"{in_featuresin_features_rank.replace(' ', '_')}_Intersect"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Intersect
            arcpy.Intersect(in_featuresin_features_rank, out_feature_class, join_attributes, cluster_tolerance, output_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apportion_polygon(self, params):
        """Apportion Polygon

Summarizes the attributes of an input polygon layer based on the spatial overlay of a target polygon layer and assigns the summarized attributes to the target polygons. The target polygons have summed numeric attributes derived from the input polygons that each target overlaps. This process is typically known as apportioning or apportionment. This tool can be used to estimate the population of one

feature based on the percentage of that feature that overlays another feature

with a known population. The Enrich Layer tool uses detailed aggregation and apportionment settings to summarize data.  The Apportion Polygon tool is similar to the Enrich Layer tool. However, Apportion Polygon uses specified apportionment, while Enrich Layer uses U.S. Census Block points or global settlement points for apportionment. For more information, see Data apportionment.

        params: {"in_features": <Feature Layer>, "apportion_fieldsfield_statistic_type": <Value Table>, "target_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    apportion_fieldsfield_statistic_type = params.get("apportion_fieldsfield_statistic_type")
    if apportion_fieldsfield_statistic_type is None:
        return {"success": False, "error": "apportion_fieldsfield_statistic_type parameter is required"}
    target_features = params.get("target_features")
    if target_features is None:
        return {"success": False, "error": "target_features parameter is required"}
    out_features = params.get("out_features")
    if out_features is None:
        return {"success": False, "error": "out_features parameter is required"}
    method = params.get("method")
    if method is None:
        return {"success": False, "error": "method parameter is required"}
    estimation_features = params.get("estimation_features")
    weight_field = params.get("weight_field")
    maintain_geometries = params.get("maintain_geometries")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Apportion_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apportion Polygon
            arcpy.ApportionPolygon(in_features, apportion_fieldsfield_statistic_type, target_features, out_features, method, estimation_features, weight_field, maintain_geometries)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def count_overlapping_features(self, params):
        """Count Overlapping Features

Generates planarized overlapping features from the input features. The count of overlapping features is written to the output features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "min_overlap_count": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    min_overlap_count = params.get("min_overlap_count")
    out_overlap_table = params.get("out_overlap_table")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Count_Overlapping_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Count Overlapping Features
            arcpy.CountOverlappingFeatures(in_features, out_feature_class, min_overlap_count, out_overlap_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def identity(self, params):
        """Identity

Computes a geometric intersection of the input features and identity features. The input features or portions thereof that overlap identity features will get the attributes of those identity features.

        params: {"in_features": <Feature Layer>, "identity_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    identity_features = params.get("identity_features")
    if identity_features is None:
        return {"success": False, "error": "identity_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    join_attributes = params.get("join_attributes")
    cluster_tolerance = params.get("cluster_tolerance")
    relationship = params.get("relationship")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Identity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Identity
            arcpy.Identity(in_features, identity_features, out_feature_class, join_attributes, cluster_tolerance, relationship)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatial_join(self, params):
        """Spatial Join

Joins attributes from one feature to another based on the spatial relationship. The target features and the joined attributes from the join features are written to the output feature class. Learn more about Spatial Join relationships by feature type

        params: {"target_features": <Feature Layer>, "join_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    target_features = params.get("target_features")
    if target_features is None:
        return {"success": False, "error": "target_features parameter is required"}
    join_features = params.get("join_features")
    if join_features is None:
        return {"success": False, "error": "join_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    join_operation = params.get("join_operation")
    join_type = params.get("join_type")
    field_mapping = params.get("field_mapping")
    match_option = params.get("match_option")
    search_radius = params.get("search_radius")
    distance_field_name = params.get("distance_field_name")
    match_fieldsjoin_field_target_field = params.get("match_fieldsjoin_field_target_field")

            # Generate output name and path
            output_name = f"{target_features.replace(' ', '_')}_Spatial_Join"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatial Join
            arcpy.SpatialJoin(target_features, join_features, out_feature_class, join_operation, join_type, field_mapping, match_option, search_radius, distance_field_name, match_fieldsjoin_field_target_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def union(self, params):
        """Union

Computes a geometric union of the input features. All features and their attributes will be written to the output feature class. Learn more about how Union works

        params: {"in_featuresin_features_rank": <Value Table>, "out_feature_class": <Feature Class>, "join_attributes": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_featuresin_features_rank = params.get("in_featuresin_features_rank")
    if in_featuresin_features_rank is None:
        return {"success": False, "error": "in_featuresin_features_rank parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    join_attributes = params.get("join_attributes")
    cluster_tolerance = params.get("cluster_tolerance")
    gaps = params.get("gaps")

            # Generate output name and path
            output_name = f"{in_featuresin_features_rank.replace(' ', '_')}_Union"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Union
            arcpy.Union(in_featuresin_features_rank, out_feature_class, join_attributes, cluster_tolerance, gaps)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select(self, params):
        """Select

Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select
            arcpy.Select(in_features, out_feature_class, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pairwise_dissolve(self, params):
        """Pairwise Dissolve

Aggregates features based on specified attributes using a parallel processing approach. An alternate tool is available for dissolve operations. See the Dissolve tool documentation for details.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "dissolve_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    dissolve_field = params.get("dissolve_field")
    statistics_fieldsfield_statistic_type = params.get("statistics_fieldsfield_statistic_type")
    multi_part = params.get("multi_part")
    concatenation_separator = params.get("concatenation_separator")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Pairwise_Dissolve"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pairwise Dissolve
            arcpy.PairwiseDissolve(in_features, out_feature_class, dissolve_field, statistics_fieldsfield_statistic_type, multi_part, concatenation_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pairwise_integrate(self, params):
        """Pairwise Integrate

Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect. Pairwise Integrate performs

the following processing tasks: Vertices within the x,y tolerance of one another will be assigned the same coordinate location.When a vertex of one feature is within the x,y tolerance of an edge of any other feature, a new vertex will be inserted on the edge.When line segments intersect, a vertex will be inserted at the point of intersection for each feature involved in the intersection. An alternate tool is available for vector data integration. See the Integrate tool documentation for details.

        params: {"in_features": <Value Table>, "cluster_tolerance": <Linear Unit>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Pairwise_Integrate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pairwise Integrate
            arcpy.PairwiseIntegrate(in_features, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def clip(self, params):
        """Clip

Extracts input features that overlay the clip features. Use this tool to cut out a piece of one dataset using one or more of the features in another dataset as a cookie cutter. This is particularly useful for creating a new dataset—also referred to as a study area or area of interest (AOI)—that contains a geographic subset of the features in another, larger dataset. Clip operations can also be performed using the Pairwise Clip tool.

        params: {"in_features": <Feature Layer; Scene Layer; File; Building Scene Layer>, "clip_features": <Feature Layer>, "out_feature_class": <Feature Class; File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    clip_features = params.get("clip_features")
    if clip_features is None:
        return {"success": False, "error": "clip_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Clip"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Clip
            arcpy.Clip(in_features, clip_features, out_feature_class, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pairwise_buffer(self, params):
        """Pairwise Buffer

Creates buffer polygons around input features to a specified distance using a parallel processing approach. Alternate tools are available for buffer operations. See the Buffer and Graphic Buffer tool documentation for details.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "buffer_distance_or_field": <Linear Unit; Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    buffer_distance_or_field = params.get("buffer_distance_or_field")
    if buffer_distance_or_field is None:
        return {"success": False, "error": "buffer_distance_or_field parameter is required"}
    dissolve_option = params.get("dissolve_option")
    dissolve_field = params.get("dissolve_field")
    method = params.get("method")
    max_deviation = params.get("max_deviation")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Pairwise_Buffer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pairwise Buffer
            arcpy.PairwiseBuffer(in_features, out_feature_class, buffer_distance_or_field, dissolve_option, dissolve_field, method, max_deviation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pairwise_clip(self, params):
        """Pairwise Clip

Extracts input features that overlay the clip features. Use this tool to cut out a piece of one feature class using one or more of the features in another feature class. This is particularly useful for creating a new feature class—also referred to as a study area or area of interest (AOI)—that contains a geographic subset of the features in another, larger feature class. Clip operations can also be performed with  the Clip tool.

        params: {"in_features": <Feature Layer>, "clip_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    clip_features = params.get("clip_features")
    if clip_features is None:
        return {"success": False, "error": "clip_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Pairwise_Clip"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pairwise Clip
            arcpy.PairwiseClip(in_features, clip_features, out_feature_class, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select(self, params):
        """Select

Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select
            arcpy.Select(in_features, out_feature_class, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def buffer(self, params):
        """Buffer

Creates buffer polygons around input features to a specified distance. Alternate tools are available for buffer operations. See the Pairwise Buffer and Graphic Buffer  tool documentation for details. Learn more about how Buffer works

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "buffer_distance_or_field": <Linear Unit; Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    buffer_distance_or_field = params.get("buffer_distance_or_field")
    if buffer_distance_or_field is None:
        return {"success": False, "error": "buffer_distance_or_field parameter is required"}
    line_side = params.get("line_side")
    line_end_type = params.get("line_end_type")
    dissolve_option = params.get("dissolve_option")
    dissolve_field = params.get("dissolve_field")
    method = params.get("method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Buffer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Buffer
            arcpy.Buffer(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def near(self, params):
        """Near

Calculates distance and additional proximity information between the input features and the closest feature in another layer or feature class. Learn more about how proximity is calculated by geoprocessing tools

        params: {"in_features": <Feature Layer>, "near_features": <Feature Layer>, "search_radius": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    near_features = params.get("near_features")
    if near_features is None:
        return {"success": False, "error": "near_features parameter is required"}
    search_radius = params.get("search_radius")
    location = params.get("location")
    angle = params.get("angle")
    method = params.get("method")
    field_namesproperty_fieldname = params.get("field_namesproperty_fieldname")
    distance_unit = params.get("distance_unit")
    match_fieldsinput_field_near_field = params.get("match_fieldsinput_field_near_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Near"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Near
            arcpy.Near(in_features, near_features, search_radius, location, angle, method, field_namesproperty_fieldname, distance_unit, match_fieldsinput_field_near_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_thiessen_polygons(self, params):
        """Create Thiessen Polygons

Creates Thiessen polygons from point features. Each Thiessen polygon contains only a single point input feature. Any location within a Thiessen polygon is closer to its associated point than to any other point input feature.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "fields_to_copy": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    fields_to_copy = params.get("fields_to_copy")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Create_Thiessen_Polygons"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Thiessen Polygons
            arcpy.CreateThiessenPolygons(in_features, out_feature_class, fields_to_copy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_origin_destination_links(self, params):
        """Generate Origin-Destination Links

Generates connecting lines from origin features to destination features. This is often referred to as a spider diagram.

        params: {"origin_features": <Feature Layer>, "destination_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    origin_features = params.get("origin_features")
    if origin_features is None:
        return {"success": False, "error": "origin_features parameter is required"}
    destination_features = params.get("destination_features")
    if destination_features is None:
        return {"success": False, "error": "destination_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    origin_group_field = params.get("origin_group_field")
    destination_group_field = params.get("destination_group_field")
    line_type = params.get("line_type")
    num_nearest = params.get("num_nearest")
    search_distance = params.get("search_distance")
    distance_unit = params.get("distance_unit")
    if distance_unit is None:
        return {"success": False, "error": "distance_unit parameter is required"}
    aggregate_links = params.get("aggregate_links")
    sum_fields = params.get("sum_fields")

            # Generate output name and path
            output_name = f"{origin_features.replace(' ', '_')}_Generate_Origin-Destination_Links"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Origin-Destination Links
            arcpy.GenerateOriginDestinationLinks(origin_features, destination_features, out_feature_class, origin_group_field, destination_group_field, line_type, num_nearest, search_distance, distance_unit, aggregate_links, sum_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def polygon_neighbors(self, params):
        """Polygon Neighbors

Creates a table with statistics based on polygon contiguity (overlaps, coincident edges, or nodes). Learn more about how Polygon Neighbors works

        params: {"in_features": <Feature Layer>, "out_table": <Table>, "in_fields": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_table = params.get("out_table")
    if out_table is None:
        return {"success": False, "error": "out_table parameter is required"}
    in_fields = params.get("in_fields")
    area_overlap = params.get("area_overlap")
    both_sides = params.get("both_sides")
    cluster_tolerance = params.get("cluster_tolerance")
    out_linear_units = params.get("out_linear_units")
    out_area_units = params.get("out_area_units")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Polygon_Neighbors"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Polygon Neighbors
            arcpy.PolygonNeighbors(in_features, out_table, in_fields, area_overlap, both_sides, cluster_tolerance, out_linear_units, out_area_units)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multiple_ring_buffer(self, params):
        """Multiple Ring Buffer

Creates multiple buffers at specified distances around the input features. These buffers can be merged and dissolved using the buffer distance values to create nonoverlapping buffers.

        params: {"input_features": <Feature Layer>, "output_feature_class": <Feature Class>, "distancesdistance": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    input_features = params.get("input_features")
    if input_features is None:
        return {"success": False, "error": "input_features parameter is required"}
    output_feature_class = params.get("output_feature_class")
    if output_feature_class is None:
        return {"success": False, "error": "output_feature_class parameter is required"}
    distancesdistance = params.get("distancesdistance")
    if distancesdistance is None:
        return {"success": False, "error": "distancesdistance parameter is required"}
    buffer_unit = params.get("buffer_unit")
    dissolve_option = params.get("dissolve_option")
    outside_polygons_only = params.get("outside_polygons_only")
    method = params.get("method")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Multiple_Ring_Buffer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multiple Ring Buffer
            arcpy.MultipleRingBuffer(input_features, output_feature_class, distancesdistance, buffer_unit, dissolve_option, outside_polygons_only, method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def graphic_buffer(self, params):
        """Graphic Buffer

Creates buffer polygons around input features to a specified distance. A number of cartographic shapes are available for buffer ends (caps) and corners (joins) when the buffer is generated around the feature. Learn more about how Graphic Buffer works Alternate tools are available for buffer operations. See the Pairwise Buffer and Buffer  tool documentation for details.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "buffer_distance_or_field": <Linear Unit; Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    buffer_distance_or_field = params.get("buffer_distance_or_field")
    if buffer_distance_or_field is None:
        return {"success": False, "error": "buffer_distance_or_field parameter is required"}
    line_caps = params.get("line_caps")
    line_joins = params.get("line_joins")
    miter_limit = params.get("miter_limit")
    max_deviation = params.get("max_deviation")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Graphic_Buffer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Graphic Buffer
            arcpy.GraphicBuffer(in_features, out_feature_class, buffer_distance_or_field, line_caps, line_joins, miter_limit, max_deviation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_near_table(self, params):
        """Generate Near Table

Calculates distances and other proximity information between features in one or more feature classes or layers. Unlike the Near tool, which modifies the input, Generate Near Table writes results to a new stand-alone table and supports finding more than one near feature. Learn more about how proximity is calculated by geoprocessing tools

        params: {"in_features": <Feature Layer>, "near_features": <Feature Layer>, "out_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    near_features = params.get("near_features")
    if near_features is None:
        return {"success": False, "error": "near_features parameter is required"}
    out_table = params.get("out_table")
    if out_table is None:
        return {"success": False, "error": "out_table parameter is required"}
    search_radius = params.get("search_radius")
    location = params.get("location")
    angle = params.get("angle")
    closest = params.get("closest")
    closest_count = params.get("closest_count")
    method = params.get("method")
    distance_unit = params.get("distance_unit")
    match_fieldsinput_field_near_field = params.get("match_fieldsinput_field_near_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generate_Near_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Near Table
            arcpy.GenerateNearTable(in_features, near_features, out_table, search_radius, location, angle, closest, closest_count, method, distance_unit, match_fieldsinput_field_near_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select(self, params):
        """Select

Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Select"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select
            arcpy.Select(in_features, out_feature_class, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tabulate_intersection(self, params):
        """Tabulate Intersection

Computes the intersection between two feature classes and cross tabulates the area, length, or count of the intersecting features.

        params: {"in_zone_features": <Feature Layer>, "zone_fields": <Field>, "in_class_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_zone_features = params.get("in_zone_features")
    if in_zone_features is None:
        return {"success": False, "error": "in_zone_features parameter is required"}
    zone_fields = params.get("zone_fields")
    if zone_fields is None:
        return {"success": False, "error": "zone_fields parameter is required"}
    in_class_features = params.get("in_class_features")
    if in_class_features is None:
        return {"success": False, "error": "in_class_features parameter is required"}
    out_table = params.get("out_table")
    if out_table is None:
        return {"success": False, "error": "out_table parameter is required"}
    class_fields = params.get("class_fields")
    sum_fields = params.get("sum_fields")
    xy_tolerance = params.get("xy_tolerance")
    out_units = params.get("out_units")

            # Generate output name and path
            output_name = f"{in_zone_features.replace(' ', '_')}_Tabulate_Intersection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Tabulate Intersection
            arcpy.TabulateIntersection(in_zone_features, zone_fields, in_class_features, out_table, class_fields, sum_fields, xy_tolerance, out_units)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def summarize_within(self, params):
        """Summarize Within

Overlays a polygon layer with another layer to summarize the number of points, length of the lines, or area of the polygons within each polygon, and calculate attribute field statistics about the features within the polygons. The following are example scenarios using Summarize Within:From a layer of watershed boundaries and a layer of land-use boundaries by land-use type, calculate total acreage of land-use type for each watershed.From a layer of parcels in a county and a layer of city boundaries, summarize the average value of vacant parcels within each city boundary.From a layer of counties and a layer of roads, summarize the total mileage of roads by road type in each county.

        params: {"in_polygons": <Feature Layer>, "in_sum_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_polygons = params.get("in_polygons")
    if in_polygons is None:
        return {"success": False, "error": "in_polygons parameter is required"}
    in_sum_features = params.get("in_sum_features")
    if in_sum_features is None:
        return {"success": False, "error": "in_sum_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    keep_all_polygons = params.get("keep_all_polygons")
    sum_fieldssummary_field_statistic_type = params.get("sum_fieldssummary_field_statistic_type")
    sum_shape = params.get("sum_shape")
    shape_unit = params.get("shape_unit")
    group_field = params.get("group_field")
    add_min_maj = params.get("add_min_maj")
    add_group_percent = params.get("add_group_percent")
    out_group_table = params.get("out_group_table")

            # Generate output name and path
            output_name = f"{in_polygons.replace(' ', '_')}_Summarize_Within"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Summarize Within
            arcpy.SummarizeWithin(in_polygons, in_sum_features, out_feature_class, keep_all_polygons, sum_fieldssummary_field_statistic_type, sum_shape, shape_unit, group_field, add_min_maj, add_group_percent, out_group_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def summary_statistics(self, params):
        """Summary Statistics

Calculates summary statistics for fields in a table.

        params: {"in_table": <Table View; Raster Layer>, "out_table": <Table>, "statistics_fieldsfield_statistic_type": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_table = params.get("in_table")
    if in_table is None:
        return {"success": False, "error": "in_table parameter is required"}
    out_table = params.get("out_table")
    if out_table is None:
        return {"success": False, "error": "out_table parameter is required"}
    statistics_fieldsfield_statistic_type = params.get("statistics_fieldsfield_statistic_type")
    if statistics_fieldsfield_statistic_type is None:
        return {"success": False, "error": "statistics_fieldsfield_statistic_type parameter is required"}
    case_field = params.get("case_field")
    concatenation_separator = params.get("concatenation_separator")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Summary_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Summary Statistics
            arcpy.SummaryStatistics(in_table, out_table, statistics_fieldsfield_statistic_type, case_field, concatenation_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enrich(self, params):
        """Enrich

Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations.  The output is a duplicate of your input with additional attribute fields.  This tool requires an ArcGIS Online organizational account or a locally installed Business Analyst dataset. The demographic and landscape information available with this tool can come from ArcGIS Online or locally installed Business Analyst data. The Enrich tool will consume credits if ArcGIS Online is set as the Business Analyst data source. The Enrich tool uses detailed aggregation and apportionment settings to summarize data. For more information, see Data apportionment.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "variables": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    variables = params.get("variables")
    if variables is None:
        return {"success": False, "error": "variables parameter is required"}
    buffer_type = params.get("buffer_type")
    distance = params.get("distance")
    unit = params.get("unit")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Enrich"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enrich
            arcpy.Enrich(in_features, out_feature_class, variables, buffer_type, distance, unit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def summarize_nearby(self, params):
        """Summarize Nearby

Finds features that are within a specified distance of features in the input layer and calculates statistics for the nearby features. Distance can be measured as a straight-line distance, a drive-time distance (for example, within 10 minutes), or a drive distance (for example, within 5 kilometers). For drive-time and drive-distance measurements, you  must be signed in to an  ArcGIS Online organizational account with Network Analysis privileges. Both measurement options consume credits. The following are example scenarios using Summarize Nearby:Calculate the total population within a 5minute drive time of a proposed new store location.Calculate the number of freeway access ramps within a 1-mile drive distance of a proposed new store location to use as a measure of store accessibility.

        params: {"in_features": <Feature Layer>, "in_sum_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    in_sum_features = params.get("in_sum_features")
    if in_sum_features is None:
        return {"success": False, "error": "in_sum_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    distance_type = params.get("distance_type")
    if distance_type is None:
        return {"success": False, "error": "distance_type parameter is required"}
    distancesdistance = params.get("distancesdistance")
    if distancesdistance is None:
        return {"success": False, "error": "distancesdistance parameter is required"}
    distance_units = params.get("distance_units")
    time_of_day = params.get("time_of_day")
    time_zone = params.get("time_zone")
    keep_all_polygons = params.get("keep_all_polygons")
    sum_fieldssummary_field_statistic_type = params.get("sum_fieldssummary_field_statistic_type")
    sum_shape = params.get("sum_shape")
    shape_unit = params.get("shape_unit")
    group_field = params.get("group_field")
    add_min_maj = params.get("add_min_maj")
    add_group_percent = params.get("add_group_percent")
    output_grouped_table = params.get("output_grouped_table")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Summarize_Nearby"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Summarize Nearby
            arcpy.SummarizeNearby(in_features, in_sum_features, out_feature_class, distance_type, distancesdistance, distance_units, time_of_day, time_zone, keep_all_polygons, sum_fieldssummary_field_statistic_type, sum_shape, shape_unit, group_field, add_min_maj, add_group_percent, output_grouped_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def frequency(self, params):
        """Frequency

Reads a table and a set of fields and creates a new table containing unique field values and the number of occurrences of each unique field value.

        params: {"in_table": <Table View; Raster Layer>, "out_table": <Table>, "frequency_fields": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_table = params.get("in_table")
    if in_table is None:
        return {"success": False, "error": "in_table parameter is required"}
    out_table = params.get("out_table")
    if out_table is None:
        return {"success": False, "error": "out_table parameter is required"}
    frequency_fields = params.get("frequency_fields")
    if frequency_fields is None:
        return {"success": False, "error": "frequency_fields parameter is required"}
    summary_fields = params.get("summary_fields")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Frequency
            arcpy.Frequency(in_table, out_table, frequency_fields, summary_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
