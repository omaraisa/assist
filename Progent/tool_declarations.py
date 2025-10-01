# Generated ArcGIS Pro Analysis Tools Function Declarations
# Generated on 2025-09-30T13:21:40.566070
# Total tools: {total_tools}

import arcpy

def clip(in_features, clip_features, out_feature_class=None, cluster_tolerance(optional)=None):
    """Clip

    in_features (Feature Layer; Scene Layer; File; Building Scene Layer): The features that will be clipped.
    clip_features (Feature Layer): The features that will be used to clip the input features.
    out_feature_class (Feature Class; File): The dataset that will be created.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates as well as the distance a coordinate can move in x or y (or both). Set the value higher for data with less coordinate accuracy and lower for data with extremely high accuracy.Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Clip
    result = arcpy.Clip(in_features, clip_features, out_feature_class, cluster_tolerance(optional))
    return result

def table_select(in_table, out_table, where_clause(optional)=None):
    """Table Select

    in_table (Table View; Raster Layer): The table containing records matching the specified expression that will be written to the output table.
    out_table (Table): The output table containing records from the input table that match the specified expression.
    where_clause(optional) (SQL Expression): An SQL expression used to select a subset of records.  For more information on SQL syntax, see SQL reference for elements used in query expressions.
    """
    # Execute Table_Select
    result = arcpy.Table_Select(in_table, out_table, where_clause(optional))
    return result

def split_by_attributes(input_table, target_workspace, split_fields[split_fields,...]=None):
    """Split By Attributes

    input_table (Table View): The input feature class or table containing the data that will be split into the target workspace.
    target_workspace (Workspace; Feature Dataset): The existing workspace where the output feature classes or tables will be written.
    split_fields[split_fields,...] (Field): The fields on which the input will be split into new feature classes or tables.
    """
    # Execute Split_By_Attributes
    result = arcpy.Split_By_Attributes(input_table, target_workspace, split_fields[split_fields,...])
    return result

def select(in_features, out_feature_class, where_clause(optional)=None):
    """Select

    in_features (Feature Layer): The input feature class or layer from which features will be selected.
    out_feature_class (Feature Class): The output feature class that will be created. If no expression is used, the output will contain all the input features.
    where_clause(optional) (SQL Expression): The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.
    """
    # Execute Select
    result = arcpy.Select(in_features, out_feature_class, where_clause(optional))
    return result

def split(in_features, split_features, split_field=None, out_workspace=None, cluster_tolerance(optional)=None):
    """Split

    in_features (Feature Layer): The features to be split.
    split_features (Feature Layer): Polygon features containing a tabular field whose unique values are used to split the input features and provide the output feature classes' names.
    split_field (Field): The character field used to split the input features. This field's values identify the split features used to create each output feature class. The split field's unique values provide the names of the output feature classes.
    out_workspace (Workspace ; Feature Dataset): The existing workspace where the output feature classes are stored.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Set the value higher for data that has less coordinate accuracy and lower for datasets with extremely high accuracy.Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Split
    result = arcpy.Split(in_features, split_features, split_field, out_workspace, cluster_tolerance(optional))
    return result

def select(in_features, out_feature_class, where_clause(optional)=None):
    """Select

    in_features (Feature Layer): The input feature class or layer from which features will be selected.
    out_feature_class (Feature Class): The output feature class that will be created. If no expression is used, the output will contain all the input features.
    where_clause(optional) (SQL Expression): The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.
    """
    # Execute Select
    result = arcpy.Select(in_features, out_feature_class, where_clause(optional))
    return result

def assign_weights_by_pairwise_comparison(input_variables[input_variables,...], out_table, add_comparison_matrix(optional)=None, comparison_matrix(optional)=None):
    """Assign Weights By Pairwise Comparison

    input_variables[input_variables,...] (String): The variable names that will be compared. Any name can be provided.The minimum number of variables is two and the maximum is nine.
    out_table (Table): The name of the output table that will contain calculated weights for the input variables. When the add_comparison_matrix parameter value is ADD_MATRIX, the output table will also include the pairwise comparison matrix.
    add_comparison_matrix(optional) (Boolean): Specifies whether the out_table parameter value will contain the pairwise comparison matrix.ADD_MATRIX—The output table will contain both the pairwise comparison matrix and the calculated weights. This is the default.WEIGHTS_ONLY—The output table will only include the calculated weights.
    comparison_matrix(optional) (Pairwise Weights Table): The pairwise comparison matrix that will be used when calculating the weights.
Define the pairwise comparisons by doing one of the following:Provide a file containing a valid comparison matrix.Specify the variable names and their comparisons.The file can be a geodatabase table, dBASE (.dbf), or comma-delimited files (.csv and .txt).
    """
    # Execute Assign_Weights_By_Pairwise_Comparison
    result = arcpy.Assign_Weights_By_Pairwise_Comparison(input_variables[input_variables,...], out_table, add_comparison_matrix(optional), comparison_matrix(optional))
    return result

def apportion_polygon(in_features, apportion_fields[[field,_{statistic_type}],...], target_features=None, out_features=None, method=None, estimation_features(optional)=None, weight_field(optional)=None, maintain_geometries(optional)=None):
    """Apportion Polygon

    in_features (Feature Layer): The polygon features with numeric attributes that will be                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          summarized into the target polygon geometries.
    apportion_fields[[field,_{statistic_type}],...] (Value Table): The numeric fields from the input polygons that will be summarized by each target polygon and recorded in the output feature class.The optional statistic types are as follows:SUM—The values for the specified field will be added together. Use this statistic for count-based attributes. This is the default.MEAN—The average for the specified field will be calculated. Use this statistic for rate-based attributes, such as population percentages. This option is only valid when the method parameter is set to AREA.MEDIAN—The median of the specified field will be calculated. Use this statistic for rate-based attributes, such as population percentages. This option is only valid when the method parameter is set to AREA.
    target_features (Feature Layer): The polygon 
features and their apportioned fields that will be copied to the output feature class.
    out_features (Feature Class): The output feature class containing the attribute and geometries of the target polygons as well as the specified apportion fields from the input polygons.
    method (String): Specifies the method that will be used to apportion the fields from the input polygons to the target polygons.
AREA—The amount that each input polygon contributes to the summarized values for each target feature will be determined by the area of overlap between the two features. If an input feature overlaps two target features by the same amount,  the apportioned fields will be divided in two and contribute to both target features by half of the total value. This is the default.LENGTH—The attributes from the input features will be divided based on the percentage of how much of a line is within each target feature. Only the line intersecting the input feature is included in the calculation.  The line outside the input feature is excluded.  For example, if one target feature covers 750 meters of a line, and another target feature covers 250 meters of a line, 75% (750 / 1000) of the input feature's attribute values will be aggregated to the first target feature, and 25% (250 / 1000) of the input feature's attribute values will be aggregated to the second target feature.POINTS—The attributes from the input features will be divided based on the number of points inside each target feature overlapping an input feature.  Points outside of the input feature are excluded. Optionally, a weight field can be specified so that the total weight of all points within each target feature will be used to determine how the input features' attribute values are divided. For example, if two target features overlap one input feature, and there are two points inside the first target feature and eight points inside the second target feature, 20% (2 / 10) of the input feature's attribute values will be aggregated to the first target feature, and 80% (8 / 10) of the input feature's attribute values will be aggregated to the second target feature.
    estimation_features(optional) (Feature Layer): The input point or polyline features that will be used to estimate the percent of the input polygon apportion fields to apportion to the target polygon.  This is the amount of the point or line within the intersection divided by the amount within the input feature to create a percentage.
    weight_field(optional) (Field): A numeric field from the target polygon layer that  will be used to adjust which target polygons receive larger apportioned values from the input polygons' fields to apportion. Targets with higher weight are apportioned a higher ratio of the field values.If estimation features are specified, the weight
field will be a numeric field from the estimation features that will
adjust the values apportioned to the target polygons intersecting
the estimation features.
    maintain_geometries(optional) (Boolean): Specifies whether the output feature class will maintain the original geometries of the target polygon layer. MAINTAIN_GEOMETRIES—The output feature class will maintain the original geometries of the target polygon layer. This is the default.INTERSECT_GEOMETRIES—The output feature class will be a geometric intersection of the target polygons and the input polygons. Only areas of the target polygons that overlap an input polygon will be included in the output.
    """
    # Execute Apportion_Polygon
    result = arcpy.Apportion_Polygon(in_features, apportion_fields[[field,_{statistic_type}],...], target_features, out_features, method, estimation_features(optional), weight_field(optional), maintain_geometries(optional))
    return result

def count_overlapping_features(in_features[in_features,...], out_feature_class, min_overlap_count(optional)=None, out_overlap_table(optional)=None):
    """Count Overlapping Features

    in_features[in_features,...] (Feature Layer): The input feature classes or layers. The input features can be point, multipoint, line, or polygon. If multiple inputs are provided, they must all be the same geometry type.
    out_feature_class (Feature Class): The output feature class containing the overlap count.
    min_overlap_count(optional) (Long): Limits the output to only locations that meet or exceed the specified number of overlaps. The default value is 1.
    out_overlap_table(optional) (Table): The output table containing records for each individual overlapping geometry.
    """
    # Execute Count_Overlapping_Features
    result = arcpy.Count_Overlapping_Features(in_features[in_features,...], out_feature_class, min_overlap_count(optional), out_overlap_table(optional))
    return result

def union(in_features[[in_features,_{rank}],...], out_feature_class, join_attributes(optional)=None, cluster_tolerance(optional)=None, gaps(optional)=None):
    """Union

    in_features[[in_features,_{rank}],...] (Value Table): The input feature classes or layers. When the distance between features is less than the cluster tolerance, the features with the lower rank will snap to the feature with the higher rank. The highest rank is one. All of the input features must be polygons.
    out_feature_class (Feature Class): The feature class that will contain the results.
    join_attributes(optional) (String): Specifies which attributes from the input features will be transferred to the output feature class.ALL—All the attributes from the input features will be transferred to the output feature class. This is the default. NO_FID—All the attributes except the FID from the input features will be transferred to the output feature class. ONLY_FID—Only the FID field from the input features will be transferred to the output feature class.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    gaps(optional) (Boolean): Specifies whether a feature will be created for areas in the output that are completely enclosed by polygons.Gaps are areas in the output feature class that are completely enclosed by other polygons (created from the intersection of features or from existing holes in the input polygons). These areas are not invalid, but you can identify them for analysis. To identify the gaps in the output, set this parameter to NO_GAPS, and a feature will be created in these areas. To select these features, query the output feature class based on all the input feature's FID values being equal to -1.GAPS—A feature will not be created for an area in the output that is completely enclosed by polygons. This is the default. NO_GAPS—A feature will be created for an area in the output that is completely enclosed by polygons. This feature will have no attribute values and will have a FID value of -1.
    """
    # Execute Union
    result = arcpy.Union(in_features[[in_features,_{rank}],...], out_feature_class, join_attributes(optional), cluster_tolerance(optional), gaps(optional))
    return result

def spatial_join(target_features, join_features, out_feature_class=None, join_operation(optional)=None, join_type(optional)=None, field_mapping(optional)=None, match_option(optional)=None, search_radius(optional)=None, distance_field_name(optional)=None, match_fields[[join_field,_target_field],...](optional)=None):
    """Spatial Join

    target_features (Feature Layer): The attributes from the target features and the attributes from the joined features will be transferred to the output feature class. However, a subset of attributes can be defined by the field map parameter.
    join_features (Feature Layer): The attributes from the join features will be joined to the attributes of the target features. See the explanation of the join_operation parameter for details on how the aggregation of joined attributes are affected by the type of join operation.
    out_feature_class (Feature Class): A new feature class containing the attributes of the target and join features. By default, all attributes of the target features and the attributes of the joined features will be written to the output. However, the set of attributes to be transferred can be defined by the field map parameter.
    join_operation(optional) (String): The operation that will join the target features and join features in the output feature class if multiple join features are found that have the same spatial relationship with a single target feature.
JOIN_ONE_TO_ONE—If multiple join features are found that have the same spatial relationship with a single target feature, the attributes from the multiple join features will be aggregated using a field map merge rule. For example, if a point target feature is found within two separate polygon join features, the attributes from the two polygons will be aggregated before being transferred to the output point feature class. If one polygon has an attribute value of 3 and the other has a value of 7, and a Sum merge rule is specified, the aggregated value in the output feature class will be 10. This is the default.JOIN_ONE_TO_MANY—If multiple join features are found that have the same spatial relationship with a single target feature, the output feature class will contain multiple copies (records) of the target feature. For example, if a single point target feature is found within two separate polygon join features, the output feature class will contain two copies of the target feature: one record with the attributes of one polygon and another record with the attributes of the other polygon.
    join_type(optional) (Boolean): Specifies whether all target features will be maintained in the output feature class (an outer join) or only those that have the specified spatial relationship with the join features (an inner join).KEEP_ALL—All target features will be maintained in the output (outer join). This is the default.KEEP_COMMON— Only those target features that have the specified spatial relationship with the join features will be maintained in the output feature class (inner join). For example, if a point feature class is specified for the target features, and a polygon feature class is specified for the join features with a match_option value of  WITHIN, the output feature class will only contain those target features that are within a polygon join feature. Any target features not within a join feature will be excluded from the output.
    field_mapping(optional) (Field Mappings): The fields that will
be included in the output feature class with their respective properties and
source fields. The output includes all fields from the join and
target features by default. Use the field map to add, delete, rename, and reorder fields, as well as change other field properties.The field map can be used to combine values from two or more input
fields into a single output field.In Python, use the FieldMappings class to define this parameter.
    match_option(optional) (String): Specifies the criteria that will be used to match rows.INTERSECT—The features in the join features will be matched if they intersect a target  feature. This is the default. Specify the distance in the search_radius  parameter.INTERSECT_3D— The features in the join features will be matched if they intersect a target feature in three-dimensional space (x, y, and z). Specify the distance in the search_radius parameter.WITHIN_A_DISTANCE—The features in the join features will be matched if they are within a specified distance of a target feature. Specify the distance in the search_radius parameter.WITHIN_A_DISTANCE_GEODESIC—This is the same as WITHIN_A_DISTANCE except that geodesic distance is used rather than planar distance.  Distance between features will be calculated using a geodesic formula that takes into account the curvature of the spheroid and correctly handles data near and across the dateline and poles. Use this option if the data covers a large geographic extent or the coordinate system of the inputs is unsuitable for distance calculations.WITHIN_A_DISTANCE_3D—The features in the join features will be matched if they are within a specified distance of a target feature in three-dimensional space. Specify the distance in the search_radius parameter.CONTAINS—The features in the join features will be matched if a target feature contains them. The target features must be polygons or polylines. For this option, the target features cannot be points, and the join features can only be polygons when the target features are also polygons.COMPLETELY_CONTAINS—The features in the join features will be matched if a target feature completely contains them. A polygon can completely contain any feature. A point cannot completely contain any feature, not even a point. A polyline can completely contain only polyline and point features.CONTAINS_CLEMENTINI—This spatial relationship produces the same results as COMPLETELY_CONTAINS except that if the join feature is entirely on the boundary of the target feature (no part is properly inside or outside) the feature will not be matched. Clementini defines the boundary polygon as the line separating inside and outside, the boundary of a line is defined as its end points, and the boundary of a point is always empty.WITHIN—The features in the join features will be matched if a target feature is within them. This is the opposite of CONTAINS. For this option, the target features can only be polygons when the join features are also polygons. A point can be a  join feature only if a point is the target. COMPLETELY_WITHIN—The features in the join features will be matched if a target feature is completely within them. This is the opposite of COMPLETELY_CONTAINS. WITHIN_CLEMENTINI—The result will be identical to WITHIN  except if the entirety of the feature in the join features is on the boundary of the target feature, the feature will not be matched. Clementini defines the boundary polygon as the line separating inside and outside, the boundary of a line is defined as its end points, and the boundary of a point is always empty.ARE_IDENTICAL_TO—The features in the join features will be matched if they are identical to a target feature. Both join and target feature must be of the same shape type—point to point, line to line, or polygon to polygon. BOUNDARY_TOUCHES—The features in the join features will be matched if they have a boundary that touches a target feature. When the target and join features are lines or polygons, the boundary of the join feature can only touch the boundary of the target feature and no part of the join feature can cross the boundary of the target feature.SHARE_A_LINE_SEGMENT_WITH—The features in the join features will be matched if they share a line segment with a target feature. The join and target features must be lines or polygons.CROSSED_BY_THE_OUTLINE_OF—The features in the join features will be matched if a target feature is crossed by their outline. The join and target features must be lines or polygons. If polygons are used for the join or target features, the polygon's boundary (line) will be used. Lines that cross at a point will be matched; lines that share a line segment will not be matched.HAVE_THEIR_CENTER_IN—The features in the join features will be matched if a target feature's center falls within them. The center of the feature is calculated as follows: For polygon and multipoint, the geometry's centroid is used, and for line input, the geometry's midpoint is used. Specify the distance in the search_radius parameter.CLOSEST—The feature in the join features that is closest to a target feature will be matched. See the usage tip for more information. Specify the distance in the search_radius parameter.CLOSEST_GEODESIC—This is the same as CLOSEST except that geodesic distance is used rather than planar distance.  Use this option if the data covers a large geographic extent or the coordinate system of the inputs is unsuitable for distance calculations LARGEST_OVERLAP—The feature in the join features will be matched with the target feature with the largest overlap.
    search_radius(optional) (Linear Unit): Join features within this distance of a target feature will be considered for the spatial join. A search radius is only valid when the spatial relationship is specified (the match_option parameter is set to INTERSECT, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_GEODESIC, HAVE_THEIR_CENTER_IN,  CLOSEST, or CLOSEST_GEODESIC). For example, using a search radius of 100 meters with the WITHIN_A_DISTANCE spatial relationship will join feature within 100 meters of a target feature. For the three within-a-distance relationships, if no value is specified for the search_radius, a distance of 0 is used.
    distance_field_name(optional) (String): The name of the field that contains the distance between the target feature and the closest join feature. This field will be added to the output feature class. This parameter is only valid when the spatial relationship is specified (match_option is set to CLOSEST or CLOSEST_GEODESIC. The value of this field is -1 if no feature is matched within a search radius. If no field name is provided, the field will not be added to the output feature class.
    match_fields[[join_field,_target_field],...](optional) (Value Table): Pairs of fields from the join features and target features that will be used for attribute matching. Only the records from the join features that share match field values with the target features will participate in the spatial join.
    """
    # Execute Spatial_Join
    result = arcpy.Spatial_Join(target_features, join_features, out_feature_class, join_operation(optional), join_type(optional), field_mapping(optional), match_option(optional), search_radius(optional), distance_field_name(optional), match_fields[[join_field,_target_field],...](optional))
    return result

def intersect(in_features[[in_features,_{rank}],...], out_feature_class, join_attributes(optional)=None, cluster_tolerance(optional)=None, output_type(optional)=None):
    """Intersect

    in_features[[in_features,_{rank}],...] (Value Table): A list of the input feature classes or layers. When the distance between features is less than the cluster tolerance, the features with the lower rank will snap to the feature with the higher rank. The highest rank is 1. For more information, see Priority ranks and geoprocessing tools.
    out_feature_class (Feature Class): The output feature class.
    join_attributes(optional) (String): Specifies the attributes from the input features that will be transferred to the output feature class.ALL—All the attributes from the input features will be transferred to the output feature class. This is the default. NO_FID—All the attributes except the FID attribute from the input features will be transferred to the output feature class. ONLY_FID—Only the FID attribute from the input features will be transferred to the output feature class.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both).Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    output_type(optional) (String): Specifies the type of intersections that will be returned.INPUT—The intersections returned will be the same geometry type as the input features with the lowest dimension geometry. If all inputs are polygons, the output feature class will contain polygons. If one or more of the inputs are lines and none of the inputs are points, the output will be line. If one or more of the inputs are points, the output feature class will contain points. This is the default. LINE—The intersections  returned will be line. This is only valid if none of the inputs are points. POINT—The intersections  returned will be point. If the inputs are line or polygon, the output will be a multipoint feature class.
    """
    # Execute Intersect
    result = arcpy.Intersect(in_features[[in_features,_{rank}],...], out_feature_class, join_attributes(optional), cluster_tolerance(optional), output_type(optional))
    return result

def erase(in_features, erase_features, out_feature_class=None, cluster_tolerance(optional)=None):
    """Erase

    in_features (Feature Layer): The input feature class or layer.
    erase_features (Feature Layer): The features that will be used to erase coincident features in the input.
    out_feature_class (Feature Class): The feature class that will contain only those input features that are not coincident with the erase features.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Erase
    result = arcpy.Erase(in_features, erase_features, out_feature_class, cluster_tolerance(optional))
    return result

def symmetrical_difference(in_features, update_features, out_feature_class=None, join_attributes(optional)=None, cluster_tolerance(optional)=None):
    """Symmetrical Difference

    in_features (Feature Layer): The input feature class or layer.
    update_features (Feature Layer): The update feature class or layer. The geometry type must be the same as that of the input feature class or layer.
    out_feature_class (Feature Class): The feature class to which the results will be written.
    join_attributes(optional) (String): Specifies the attributes that will be transferred to the output feature class.ALL—All the attributes from the input features will be transferred to the output feature class. This is the default. NO_FID—All the attributes except the FID from the input features will be transferred to the output feature class. ONLY_FID—Only the FID field from the input features will be transferred to the output feature class.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both).Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Symmetrical_Difference
    result = arcpy.Symmetrical_Difference(in_features, update_features, out_feature_class, join_attributes(optional), cluster_tolerance(optional))
    return result

def select(in_features, out_feature_class, where_clause(optional)=None):
    """Select

    in_features (Feature Layer): The input feature class or layer from which features will be selected.
    out_feature_class (Feature Class): The output feature class that will be created. If no expression is used, the output will contain all the input features.
    where_clause(optional) (SQL Expression): The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.
    """
    # Execute Select
    result = arcpy.Select(in_features, out_feature_class, where_clause(optional))
    return result

def identity(in_features, identity_features, out_feature_class=None, join_attributes(optional)=None, cluster_tolerance(optional)=None, relationship(optional)=None):
    """Identity

    in_features (Feature Layer): The input feature class or layer.
    identity_features (Feature Layer): The identity feature class or layer. It must be polygon or the same geometry type as the input features.
    out_feature_class (Feature Class): The feature class that will be created and to which the results will be written.
    join_attributes(optional) (String): Specifies how attributes will be transferred to the output feature class.ALL—All the attributes (including FIDs) from the input features, as well as the identity features, will be transferred to the output features.  If no intersection is found, the identity feature values will not be transferred to the output (their values will be set to empty strings or 0) and the identity feature FID will be -1. This is the default. NO_FID—All the attributes except the FID from the input features and identity features will be transferred to the output features.  If no intersection is found, the identity feature values will not be transferred to the output (their values will be set to empty strings or 0). ONLY_FID—All the attributes from the input features and only the FID  from the identity features will be transferred to the output features. If no intersection is found,  the identity features' FID attribute value in the output will be -1.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    relationship(optional) (Boolean): Specifies whether additional spatial relationships between the in_features and identity_features parameter values will be written to the output. This only applies when the geometry type of the in_features parameter value is line and the geometry type of the identity_features parameter value is polygon.NO_RELATIONSHIPS—No additional spatial relationship will be written to the output. KEEP_RELATIONSHIPS—The output line features will contain two additional fields, LEFT_poly and RIGHT_poly.  These  fields contain the feature ID  of the identity_features  parameter value on the left and right side of the line feature.
    """
    # Execute Identity
    result = arcpy.Identity(in_features, identity_features, out_feature_class, join_attributes(optional), cluster_tolerance(optional), relationship(optional))
    return result

def update(in_features, update_features, out_feature_class=None, keep_borders(optional)=None, cluster_tolerance(optional)=None):
    """Update

    in_features (Feature Layer): The input feature class or layer. The geometry type must be polygon.
    update_features (Feature Layer): The features that will be used to update the input features. The geometry type must be polygon.
    out_feature_class (Feature Class): The feature class that will contain the results.
    keep_borders(optional) (Boolean): Specifies whether the boundary of the update polygon features will be kept.BORDERS—The outside border of the update_features parameter value will be kept in the out_feature_class parameter value. This is the default. NO_BORDERS—The outside border of the update_features parameter value will not be kept after it is inserted into the in_features. Item values of the update_features parameter value take precedence over in_features parameter value attributes.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Update
    result = arcpy.Update(in_features, update_features, out_feature_class, keep_borders(optional), cluster_tolerance(optional))
    return result

def clip(in_features, clip_features, out_feature_class=None, cluster_tolerance(optional)=None):
    """Clip

    in_features (Feature Layer; Scene Layer; File; Building Scene Layer): The features that will be clipped.
    clip_features (Feature Layer): The features that will be used to clip the input features.
    out_feature_class (Feature Class; File): The dataset that will be created.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates as well as the distance a coordinate can move in x or y (or both). Set the value higher for data with less coordinate accuracy and lower for data with extremely high accuracy.Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Clip
    result = arcpy.Clip(in_features, clip_features, out_feature_class, cluster_tolerance(optional))
    return result

def pairwise_dissolve(in_features, out_feature_class, dissolve_field[dissolve_field,...](optional)=None, statistics_fields[[field,_{statistic_type}],...](optional)=None, multi_part(optional)=None, concatenation_separator(optional)=None):
    """Pairwise Dissolve

    in_features (Feature Layer): The features to be aggregated.
    out_feature_class (Feature Class): The feature class to be created that will contain the aggregated features.
    dissolve_field[dissolve_field,...](optional) (Field): The field or fields on which features will be aggregated.
    statistics_fields[[field,_{statistic_type}],...](optional) (Value Table): Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are excluded from all calculations.By default, the tool will not calculate any statistics.Numeric attribute fields can be summarized using any statistic. Text attribute fields can be summarized  using minimum, maximum, count, first, last, unique, concatenate, and mode statistics.SUM—The values for the specified field will be added together.MEAN—The average for the specified field will be calculated.MIN—The smallest value of the specified field will be identified.MAX—The largest value of the specified field will be identified.RANGE—The range of values (maximum minus minimum) for the specified field will be calculated.STD—The standard deviation of values for the specified field will be calculated.COUNT—The number of values in the specified field will be identified.FIRST—The specified field value of the first record in the input will be used.LAST—The specified field value of the last record in the input will be used.MEDIAN—The median of the specified field will be calculated.VARIANCE—The variance of the specified field will be calculated.
UNIQUE—The number of unique values of the specified field will be counted.CONCATENATE—The values for the specified field will be concatenated. The values can be separated using the concatenation_separator parameter.MODE—The mode (the most common value) for the specified field will be identified. If more than one value is equally common, the lowest value will be returned.
    multi_part(optional) (Boolean): Specifies whether multipart features will be included in the output.MULTI_PART—Multipart features will be included in the output. This is the default.SINGLE_PART—Multipart features will not be included in the output. Individual features will be created for each part.
    concatenation_separator(optional) (String): A character or characters that will be used to concatenate values when the CONCATENATION option is used for the statistics_fields parameter. By default, the tool will concatenate values without a separator.
    """
    # Execute Pairwise_Dissolve
    result = arcpy.Pairwise_Dissolve(in_features, out_feature_class, dissolve_field[dissolve_field,...](optional), statistics_fields[[field,_{statistic_type}],...](optional), multi_part(optional), concatenation_separator(optional))
    return result

def pairwise_integrate(in_features[in_features,...], cluster_tolerance(optional)):
    """Pairwise Integrate

    in_features[in_features,...] (Value Table): The feature classes that will be integrated. When the distance between features is small in comparison to the tolerance, the vertices or points will be clustered (moved to be coincident).
    cluster_tolerance(optional) (Linear Unit): The distance that determines the range in which feature vertices are made coincident. To minimize undesired movement of vertices, the x,y tolerance should be small. If no value is provided, the x,y tolerance from the first dataset in the list of inputs will be used.Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Pairwise_Integrate
    result = arcpy.Pairwise_Integrate(in_features[in_features,...], cluster_tolerance(optional))
    return result

def pairwise_buffer(in_features, out_feature_class, buffer_distance_or_field=None, dissolve_option(optional)=None, dissolve_field[dissolve_field,...](optional)=None, method(optional)=None, max_deviation(optional)=None):
    """Pairwise Buffer

    in_features (Feature Layer): The input point, line, or polygon features that will be buffered.
    out_feature_class (Feature Class): The feature class containing the output buffers.
    buffer_distance_or_field (Linear Unit; Field): The distance around the input features that will be buffered. Distances can be provided as either a value representing a linear distance or a field from the input features that contains the distance to buffer each feature.See the Usage section for more information about how the tool handles linear units.When specifying a distance, if the linear unit has two words, such as Decimal Degrees, combine the two words into one (for example, 20 DecimalDegrees).
    dissolve_option(optional) (String): Specifies the type of dissolve operation that will be performed to remove buffer overlap.NONE—An individual buffer for each feature will be maintained, regardless of overlap. This is the default. ALL—All buffers will be dissolved together into a single feature, removing any overlap. LIST—Any buffers sharing attribute values in the listed fields (carried over from the input features) will be dissolved.
    dissolve_field[dissolve_field,...](optional) (Field): The list of fields from the input features on which the output buffers will be dissolved. Any buffers sharing attribute values in the listed fields (carried over from the input features) will be dissolved.
    method(optional) (String): Specifies whether the planar or geodesic method will be used to create the buffers.PLANAR—If the input features are in a projected coordinate system, Euclidean buffers will be created. If the input features are in a geographic coordinate system and the buffer distance is in linear units (meters, feet, and so forth, as opposed to angular units such as degrees), geodesic buffers will be created. This is the default. You can use the Output Coordinate System environment setting to specify the coordinate system to use. For example, if the input features are in a projected coordinate system, you can set the environment to a geographic coordinate system to create geodesic buffers. GEODESIC—All buffers will be created using a shape-preserving geodesic buffer method, regardless of the input coordinate system.
    max_deviation(optional) (Linear Unit): The maximum distance the output buffer boundary will deviate from the true buffer boundary. While the true boundary of the buffer is a curve, the output boundary will be densified. Use this parameter to control how the output polygon boundary approximates the true buffer boundary.If this parameter is not set or is set to 0, the tool will identify the maximum deviation. It is recommended that you use the default value. Performance degradation in the tool and in subsequent analyses may result from using a maximum offset deviation that is too small.
    """
    # Execute Pairwise_Buffer
    result = arcpy.Pairwise_Buffer(in_features, out_feature_class, buffer_distance_or_field, dissolve_option(optional), dissolve_field[dissolve_field,...](optional), method(optional), max_deviation(optional))
    return result

def pairwise_clip(in_features, clip_features, out_feature_class=None, cluster_tolerance(optional)=None):
    """Pairwise Clip

    in_features (Feature Layer): The features that will be clipped.
    clip_features (Feature Layer): The features that will be used to clip the input features.
    out_feature_class (Feature Class): The feature class that will be created.
    cluster_tolerance(optional) (Linear Unit): The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    """
    # Execute Pairwise_Clip
    result = arcpy.Pairwise_Clip(in_features, clip_features, out_feature_class, cluster_tolerance(optional))
    return result

def select(in_features, out_feature_class, where_clause(optional)=None):
    """Select

    in_features (Feature Layer): The input feature class or layer from which features will be selected.
    out_feature_class (Feature Class): The output feature class that will be created. If no expression is used, the output will contain all the input features.
    where_clause(optional) (SQL Expression): The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.
    """
    # Execute Select
    result = arcpy.Select(in_features, out_feature_class, where_clause(optional))
    return result

def buffer(in_features, out_feature_class, buffer_distance_or_field=None, line_side(optional)=None, line_end_type(optional)=None, dissolve_option(optional)=None, dissolve_field[dissolve_field,...](optional)=None, method(optional)=None):
    """Buffer

    in_features (Feature Layer): The input point, line, or polygon features that will be buffered.
    out_feature_class (Feature Class): The feature class containing the output buffers.
    buffer_distance_or_field (Linear Unit; Field): The distance around the input features that will be buffered. Distances can be provided as either a value representing a linear distance or a field from the input features that contains the distance to buffer each feature.If linear units are not specified or are entered as Unknown, the linear unit of the input features' spatial reference will be used.When specifying a distance, if the linear unit has two words, such as Decimal Degrees, combine the two words into one (for example, 20 DecimalDegrees).
    line_side(optional) (String): Specifies the sides of the input features that will be buffered. This parameter is only supported for polygon and line features.FULL—For lines, buffers will be generated on both sides of the line. For polygons, buffers will be generated around the polygon and will contain and overlap the area of the input features. This is the default. LEFT—For lines, buffers will be generated on the topological left of the line. This option is not supported for polygon input features.RIGHT—For lines, buffers will be generated on the topological right of the line. This option is not supported for polygon input features.OUTSIDE_ONLY—For polygons, buffers will be generated outside the input polygon only (the area inside the input polygon will be erased from the output buffer). This option is not supported for line input features.
License:This optional parameter is not available with a Desktop Basic or Desktop Standard license.
    line_end_type(optional) (String): Specifies the shape of the buffer at the end of line input features. This parameter is not valid for polygon input features.ROUND—The ends of the buffer will be round, in the shape of a half circle. This is the default. FLAT—The ends of the buffer will be flat or squared and will end at the endpoint of the input line feature. 
License:This optional parameter is not available with a Desktop Basic or Desktop Standard license.
    dissolve_option(optional) (String): Specifies the type of dissolve that will be performed to remove buffer overlap.NONE—An individual buffer for each feature will be maintained, regardless of overlap. This is the default. ALL—All buffers will be dissolved together into a single feature, removing any overlap. LIST—Any buffers sharing attribute values in the listed fields (carried over from the input features) will be dissolved.
    dissolve_field[dissolve_field,...](optional) (Field): The list of fields from the input features on which the output buffers will be dissolved. Any buffers sharing attribute values in the listed fields (carried over from the input features) will be dissolved.
    method(optional) (String): Specifies whether the planar or geodesic method will be used to create the buffers.PLANAR—If the input features are in a projected coordinate system, Euclidean buffers will be created. If the input features are in a geographic coordinate system and the buffer distance is in linear units (meters, feet, and so forth, as opposed to angular units such as degrees), geodesic buffers will be created. This is the default. You can use the Output Coordinate System environment setting to specify the coordinate system to use. For example, if the input features are in a projected coordinate system, you can set the environment to a geographic coordinate system to create geodesic buffers. GEODESIC—All buffers will be created using a shape-preserving geodesic buffer method, regardless of the input coordinate system.
    """
    # Execute Buffer
    result = arcpy.Buffer(in_features, out_feature_class, buffer_distance_or_field, line_side(optional), line_end_type(optional), dissolve_option(optional), dissolve_field[dissolve_field,...](optional), method(optional))
    return result

def graphic_buffer(in_features, out_feature_class, buffer_distance_or_field=None, line_caps(optional)=None, line_joins(optional)=None, miter_limit(optional)=None, max_deviation(optional)=None):
    """Graphic Buffer

    in_features (Feature Layer): The input point, line, or polygon features that will be buffered.
    out_feature_class (Feature Class): The feature class containing the output buffers.
    buffer_distance_or_field (Linear Unit; Field): The distance around the input features that will be buffered. Distances can be provided as either a value representing a linear distance or a field from the input features that contains the distance to buffer each feature.If linear units are not specified or are entered as Unknown, the linear unit of the input features' spatial reference will be used.When specifying a distance, if the linear unit has two words, such as Decimal Degrees, combine the two words into one (for example, 20 DecimalDegrees).
    line_caps(optional) (String): Specifies the type of caps (ends) of the input features that will be buffered. This parameter is only supported for point and polygon features.SQUARE—The output buffer will have a square cap around the end of the input segment. This is the default.BUTT—The output buffer will have a cap perpendicular to the end of the input segment.ROUND—The output buffer will have a cap that is round at the end of the input segment.
    line_joins(optional) (String): Specifies the shape of the buffer at corners where two segments join. This parameter is  only supported for line and polygon features.
MITER—The output buffer feature will be a square or sharp shape around corners. For example, a square input polygon feature will have a square buffer feature. This is the default.BEVEL—The output buffer feature for inner corners will be squared, and the outer corner will be cut perpendicular to the farthest point of the corner.ROUND—The output buffer feature for inner corners will be squared, and the outer corner will be round.
    miter_limit(optional) (Double): Where line segments meet at a sharp angle and the line_joins parameter value has been specified as MITER, this parameter can be used to control how sharp corners in buffer output come to a point. In some cases, the outer angle where two lines join is quite large when using the MITER option. This may cause the point of the corner to extend farther than intended.
    max_deviation(optional) (Linear Unit): The maximum distance the output buffer boundary will deviate from the true buffer boundary. While the true boundary of the buffer is a curve, the output boundary will be densified. Use this parameter to control how the output polygon boundary approximates the true buffer boundary.If this parameter is not set or is set to 0, the tool will identify the maximum deviation. It is recommended that you use the default value. Performance degradation in the tool and in subsequent analyses may result from using a maximum offset deviation that is too small.
    """
    # Execute Graphic_Buffer
    result = arcpy.Graphic_Buffer(in_features, out_feature_class, buffer_distance_or_field, line_caps(optional), line_joins(optional), miter_limit(optional), max_deviation(optional))
    return result

def multiple_ring_buffer(input_features, output_feature_class, distances[distance,...]=None, buffer_unit(optional)=None, dissolve_option(optional)=None, outside_polygons_only(optional)=None, method(optional)=None):
    """Multiple Ring Buffer

    input_features (Feature Layer): The input point, line, or polygon features to be buffered.
    output_feature_class (Feature Class): The output feature class that will contain multiple buffers.
    distances[distance,...] (Double): The list of buffer distances.
    buffer_unit(optional) (String): Specifies the linear unit that will be used with the distance values.Default—The linear unit of the input features' spatial reference will be used. If the Output Coordinate System geoprocessing environment has been set, the linear unit of the environment will be used. The linear unit is ignored if the input features have an unknown or undefined spatial reference. This is the default.Inches—The unit will be inches.Feet—The unit will be feet.Yards—The unit will be yards.Miles—The unit will be miles.NauticalMiles—The unit will be nautical miles.Millimeters—The unit will be millimeters.Centimeters—The unit will be centimeters.Decimeters—The unit will be decimeters.Meters—The unit will be meters.Kilometers—The unit will be kilometers.DecimalDegrees—The unit will be decimal degrees.Points—The unit will be points.
    dissolve_option(optional) (String): Specifies whether buffers will be dissolved to resemble rings around the input features.ALL—Buffers will be dissolved to resemble rings around the input features that do not overlap (think of these as rings or donuts around the input features). The smallest buffer will cover the area of its input feature plus the buffer distance, and subsequent buffers will be rings around the smallest buffer that do not cover the area of the input feature or smaller buffers. All buffers of the same distance will be dissolved into a single feature. This is the default. NONE—Buffers will not be dissolved. All buffer areas will be maintained regardless of overlap. Each buffer will cover its input feature plus the area of any smaller buffers.
    outside_polygons_only(optional) (Boolean): Specifies whether the buffers will cover the input features. This parameter is valid only for polygon input features.FULL—Buffers will overlap or cover the input features. This is the default.OUTSIDE_ONLY—Buffers will be rings around the input features, and will not overlap or cover the input features (the area inside the input polygon will be erased from the buffer).
    method(optional) (String): Specifies the method used to create the buffer.
PLANAR—Buffers will be created using a Euclidean buffer method. This is the default when the input has a projected coordinate system.GEODESIC—Buffers will be created using a shape-preserving geodesic buffer method. This is the default when the input has  a geographic coordinate system.
    """
    # Execute Multiple_Ring_Buffer
    result = arcpy.Multiple_Ring_Buffer(input_features, output_feature_class, distances[distance,...], buffer_unit(optional), dissolve_option(optional), outside_polygons_only(optional), method(optional))
    return result

def near(in_features, near_features[near_features,...], search_radius(optional)=None, location(optional)=None, angle(optional)=None, method(optional)=None, field_names[[property,_fieldname],...](optional)=None, distance_unit(optional)=None, match_fields[[input_field,_near_field],...](optional)=None):
    """Near

    in_features (Feature Layer): The input features, which can be point, polyline, polygon, or multipoint type.
    near_features[near_features,...] (Feature Layer): One or more feature layers or feature classes containing near feature candidates. The near features can be point, polyline, polygon, or multipoint. If multiple layers or feature classes are specified, the NEAR_FC field will be added to the input table and will store the paths of the source feature class containing the nearest feature found. The same feature class or layer can be used as both input features and near features.
    search_radius(optional) (Linear Unit): The radius that will be used to search for near features. If no value is specified, all near features will be considered. If a distance but no unit or unknown is specified, the units of the coordinate system of the input features will be used. If the GEODESIC option is used for the method parameter, use a linear unit such as kilometers or miles.
    location(optional) (Boolean): Specifies whether x- and y-coordinates of the closest location of the near feature will be written to the NEAR_X and NEAR_Y fields.NO_LOCATION— Location information will not be written. This is the default.LOCATION— Location information will be written.
    angle(optional) (Boolean): Specifies whether the near angle will be calculated and written to the NEAR_ANGLE field in the output table. A near angle measures direction of the line connecting an input feature to its nearest feature at their closest locations. When the PLANAR method is used for the method parameter, the angle will be within the range of -180° to 180°, with 0° to the east, 90° to the north, 180° (or -180°) to the west, and -90° to the south. When the GEODESIC method is used, the angle will be within the range of -180° to 180°, with 0° to the north, 90° to the east, 180° (or -180°) to the south, and -90° to the west.NO_ANGLE—The near angle will not be calculated or written. This is the default.ANGLE—The near angle will be calculated and written to the NEAR_ANGLE field.
    method(optional) (String): Specifies whether a shortest path on a spheroid (geodesic) or a flat earth (planar) distance method will be used. It is recommended that you use the GEODESIC method for data stored in a coordinate system that is not appropriate for distance measurements (for example, Web Mercator or any geographic coordinate system) and for a dataset that spans a large geographic area.PLANAR—Planar distance will be used between features. This is the default.  GEODESIC—Geodesic distance will be used between features.  This method takes into account the curvature of the spheroid and correctly deals with data near the international date line and the poles.
    field_names[[property,_fieldname],...](optional) (Value Table): The names of the attribute fields that will be added during processing.If this parameter is not used or any fields that will be added are excluded from this parameter, the default field names will be used.By default, the NEAR_FID and NEAR_DIST fields will be added, the NEAR_X and NEAR_Y fields will be added when the location parameter is set to LOCATION, the NEAR_ANGLE field will be added when the angle parameter is set to ANGLE, and the NEAR_FC field will be added when multiple inputs are used.
    distance_unit(optional) (String): Specifies the unit of measurement for the NEAR_DIST field. When no unit of measurement is specified, the values in the NEAR_DIST field will be in the linear unit of the input feature's coordinate system. If the input is in a geographic coordinate system and the geodesic method is used, the units of the NEAR_DIST field will be meters. Kilometers—The unit will be kilometers.Meters—The unit will be meters.NauticalMilesInt—The unit will be international nautical miles.MilesInt—The unit will be  statute miles.YardsInt—The unit will be international yards.FeetInt—The unit will be  international feet.NauticalMiles—The unit will be U.S. survey nautical miles.Miles—The unit will be U.S. survey miles.Yards—The unit will be U.S. survey yards.Feet—The unit will be  U.S. survey feet.
    match_fields[[input_field,_near_field],...](optional) (Value Table): The pairs of fields from the input features and near features that will be used for attribute matching. Only the near features that share match field values with the input features will be used in the near calculation.
    """
    # Execute Near
    result = arcpy.Near(in_features, near_features[near_features,...], search_radius(optional), location(optional), angle(optional), method(optional), field_names[[property,_fieldname],...](optional), distance_unit(optional), match_fields[[input_field,_near_field],...](optional))
    return result

def polygon_neighbors(in_features, out_table, in_fields[in_fields,...](optional)=None, area_overlap(optional)=None, both_sides(optional)=None, cluster_tolerance(optional)=None, out_linear_units(optional)=None, out_area_units(optional)=None):
    """Polygon Neighbors

    in_features (Feature Layer): The input polygon features.
    out_table (Table): The output table.
    in_fields[in_fields,...](optional) (Field): The input attribute field or fields that will be used to identify unique polygons or polygon groups and represent them in the output.
    area_overlap(optional) (Boolean): Specifies whether overlapping relationships will  be analyzed and included in the output.  
NO_AREA_OVERLAP—Overlapping relationships will not be analyzed or included in the output. This is the default.AREA_OVERLAP—Overlapping relationships will be analyzed and included in the output.
    both_sides(optional) (Boolean): Specifies whether both sides of neighbor relationships will be included in the output.BOTH_SIDES— For a pair of neighboring polygons, both neighboring information of one polygon being the source and the other being the neighbor and vice versa will be included. This is the default.NO_BOTH_SIDES— For a pair of neighboring polygons, only neighboring information of one polygon being the source and the other being the neighbor will be included. The reciprocal relationship will not be included.
    cluster_tolerance(optional) (Linear Unit): The minimum distance between coordinates before they will be considered equal. By default, this is the x,y tolerance of the input  features.Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    out_linear_units(optional) (String): Specifies the units that will be used to report the total  length of the coincident edge between neighboring polygons. The default is the input feature units.UNKNOWN—The length unit will be unknown.KILOMETERS—The length unit will be kilometers.METERS—The length unit will be meters.DECIMETERS—The length unit will be decimeters.CENTIMETERS—The length unit will be centimeters.MILLIMETERS—The length unit will be millimeters.MILES_INTERNATIONAL—The length unit will be statute miles.NAUTICAL_MILES_INTERNATIONAL—The length unit will be international nautical miles.YARDS_INTERNATIONAL—The length unit will be international yards.FEET_INTERNATIONAL—The length unit will be international feet.INCHES_INTERNATIONAL—The length unit will be international inches.MILES—The length unit will be US survey miles.NAUTICAL_MILES—The length unit will be US survey nautical miles.YARDS—The length unit will be US survey yards.FEET—The length unit will be US survey feet.INCHES—The length unit will be US survey inches.DECIMAL_DEGREES—The length unit will be decimal degrees.POINTS—The length unit will be points.
    out_area_units(optional) (String): Specifies the units that will be used to report the area overlap of neighboring polygons.  The default is the input feature units. 
This parameter is only enabled when the area_overlap parameter is set to AREA_OVERLAP.UNKNOWN—The area unit will be square unknown.SQUARE_KILOMETERS—The area unit will be square kilometers.SQUARE_METERS—The area unit will be square meters.SQUARE_DECIMETERS—The area unit will be square decimeters.SQUARE_CENTIMETERS—The area unit will be square centimeters.SQUARE_MILLIMETERS—The area unit will be square millimeters.SQUARE_MILES—The area unit will be square statute miles.SQUARE_NAUTICAL_MILES—The area unit will be square international nautical miles.SQUARE_YARDS—The area unit will be square international yards.SQUARE_FEET—The area unit will be square international feet.SQUARE_INCHES—The area unit will be square international inches.SQUARE_MILES_US—The area unit will be square US survey miles.SQUARE_NAUTICAL_MILES_US—The area unit will be square US survey nautical miles.SQUARE_YARDS_US—The area unit will be square US survey yards.SQUARE_FEET_US—The area unit will be square US survey feet.SQUARE_INCHES_US—The area unit will be square US survey inches.ACRES_US—The area unit will be US survey acres.HECTARES—The area unit will be hectares.ACRES—The area unit will be international acres.ARES—The area unit will be ares.
    """
    # Execute Polygon_Neighbors
    result = arcpy.Polygon_Neighbors(in_features, out_table, in_fields[in_fields,...](optional), area_overlap(optional), both_sides(optional), cluster_tolerance(optional), out_linear_units(optional), out_area_units(optional))
    return result

def generate_near_table(in_features, near_features[near_features,...], out_table=None, search_radius(optional)=None, location(optional)=None, angle(optional)=None, closest(optional)=None, closest_count(optional)=None, method(optional)=None, distance_unit(optional)=None, match_fields[[input_field,_near_field],...](optional)=None):
    """Generate Near Table

    in_features (Feature Layer): The input features, which can be point, polyline, polygon, or multipoint type.
    near_features[near_features,...] (Feature Layer): One or more feature layers or feature classes containing near feature candidates. The near features can be point, polyline, polygon, or multipoint. If multiple layers or feature classes are specified, the NEAR_FC field will be added to the input table and will store the paths of the source feature class containing the nearest feature found. The same feature class or layer can be used as both input features and near features.
    out_table (Table): The output table containing the result of the analysis.
    search_radius(optional) (Linear Unit): The radius that will be used to search for near features. If no value is specified, all near features will be considered. If a distance but no unit or unknown is specified, the units of the coordinate system of the input features will be used. If the GEODESIC option is used for the method parameter, use a linear unit such as kilometers or miles.
    location(optional) (Boolean): Specifies whether x- and y-coordinates of the input feature's location and closest location of the near feature will be written to the FROM_X, FROM_Y, NEAR_X, and NEAR_Y fields.NO_LOCATION— Locations will not be written to the output table. This is the default.LOCATION— Locations will be written to the output table.
    angle(optional) (Boolean): Specifies whether the near angle will be calculated and written to the  NEAR_ANGLE field in the output table. A near angle measures direction of the line connecting an input feature to its nearest feature at their closest locations.  When the PLANAR method is used for  the method parameter, the angle will be within the range of -180° to 180°,  with 0° to the east, 90° to the north, 180° (or -180°) to the west, and -90° to the south.  When  the GEODESIC method is used for  the method parameter, the angle will be within the range of -180° to 180°, with 0° to the north, 90° to the east, 180° (or -180°) to the south, and -90° to the west.
NO_ANGLE—The near angle will not be calculated and the NEAR_ANGLE field will not be added to the output table. This is the default.ANGLE—The near angle will be calculated and the NEAR_ANGLE field will be added  to the output table.
    closest(optional) (Boolean): Specifies whether only the closest near feature will be written to the output table.CLOSEST—Only the closest near feature will be written to the output table. This is the default.ALL—Multiple near features will be written to the output table (a limit can be specified in the closest_count parameter).
    closest_count(optional) (Long): Limits the number of near features reported for each input feature. This parameter is ignored if the closest parameter  is set to CLOSEST.
    method(optional) (String): Specifies whether a shortest path on a spheroid (geodesic) or a flat earth (planar) distance method will be used. It is recommended that you use the GEODESIC method for data stored in a coordinate system that is not appropriate for distance measurements (for example, Web Mercator or any geographic coordinate system) and for a dataset that spans a large geographic area.PLANAR—Planar distance will be used between features. This is the default.  GEODESIC—Geodesic distance will be used between features.  This method takes into account the curvature of the spheroid and correctly deals with data near the international date line and the poles.
    distance_unit(optional) (String): Specifies the unit of measurement for the NEAR_DIST field. When no unit of measurement is specified, the values in the NEAR_DIST field will be in the linear unit of the input feature's coordinate system. If the input is in a geographic coordinate system and the geodesic method is used, the units of the NEAR_DIST field will be meters. Kilometers—The unit will be kilometers.Meters—The unit will be meters.NauticalMilesInt—The unit will be international nautical miles.MilesInt—The unit will be  statute miles.YardsInt—The unit will be international yards.FeetInt—The unit will be  international feet.NauticalMiles—The unit will be U.S. survey nautical miles.Miles—The unit will be U.S. survey miles.Yards—The unit will be U.S. survey yards.Feet—The unit will be  U.S. survey feet.
    match_fields[[input_field,_near_field],...](optional) (Value Table): The pairs of fields from the input features and near features that will be used for attribute matching. Only the near features that share match field values with the input features will be used in the near calculation.
    """
    # Execute Generate_Near_Table
    result = arcpy.Generate_Near_Table(in_features, near_features[near_features,...], out_table, search_radius(optional), location(optional), angle(optional), closest(optional), closest_count(optional), method(optional), distance_unit(optional), match_fields[[input_field,_near_field],...](optional))
    return result

def create_thiessen_polygons(in_features, out_feature_class, fields_to_copy(optional)=None):
    """Create Thiessen Polygons

    in_features (Feature Layer): The point input features from which Thiessen polygons will be generated.
    out_feature_class (Feature Class): The output feature class containing the Thiessen polygons that are generated from the point input features.
    fields_to_copy(optional) (String): Specifies which fields from the input features will be transferred to the output feature class.ONLY_FID—Only the FID field from the input features will be transferred to the output feature class. This is the default. ALL—All fields from the input features will be transferred to the output feature class.
    """
    # Execute Create_Thiessen_Polygons
    result = arcpy.Create_Thiessen_Polygons(in_features, out_feature_class, fields_to_copy(optional))
    return result

def select(in_features, out_feature_class, where_clause(optional)=None):
    """Select

    in_features (Feature Layer): The input feature class or layer from which features will be selected.
    out_feature_class (Feature Class): The output feature class that will be created. If no expression is used, the output will contain all the input features.
    where_clause(optional) (SQL Expression): The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.
    """
    # Execute Select
    result = arcpy.Select(in_features, out_feature_class, where_clause(optional))
    return result

def generate_origin_destination_links(origin_features, destination_features, out_feature_class=None, origin_group_field(optional)=None, destination_group_field(optional)=None, line_type(optional)=None, num_nearest(optional)=None, search_distance(optional)=None, distance_unit=None, aggregate_links(optional)=None, sum_fields[sum_fields,...](optional)=None):
    """Generate Origin-Destination Links

    origin_features (Feature Layer): The input features from which links will be generated.
    destination_features (Feature Layer): The destination features to which links will be generated.
    out_feature_class (Feature Class): The output polyline feature class that will contain the output links.
    origin_group_field(optional) (Field): The attribute field from the input origin features that will be used for grouping. Features that have the same group field value between origins and destinations will be connected with a link.
    destination_group_field(optional) (Field): The attribute field from the input destination features that will be used for grouping. Features that have the same group field value between origins and destinations will be connected with a link.
    line_type(optional) (String): Specifies whether a shortest path on a spheroid (geodesic) or a  Cartesian projected earth (planar) will be used when generating the output links. Geodesic lines will have a slight curve when their length exceeds approximately 50 kilometers, as the curvature of the Earth makes the shortest distance between two points appear curved when viewed on a 2D map.It is recommended that you use the GEODESIC line type with data stored in a coordinate system that is not appropriate for distance measurements (for example, Web Mercator and any geographic coordinate system) or any dataset that spans a large geographic area.PLANAR—Planar distance will be used between features. This is the default.  GEODESIC—Geodesic distances will be used between features.  This line type takes into account the curvature of the spheroid and correctly deals with data near the dateline and poles.
    num_nearest(optional) (Double): The maximum number of links that will be generated per origin feature to the nearest destination features. If no number is specified, the tool will generate links between all origin and destination features.For example, using a value of 1 will generate links between each origin feature and its closest destination feature.
    search_distance(optional) (Double): The maximum distance between an origin and destination feature that will produce a link feature  in the output. The unit of the search distance is specified in the distance unit parameter. If no search distance  is specified, the tool will generate links between all origin and destination features regardless of their distance apart.
    distance_unit (String): Specifies the units used to measure the length of the links. Distances for each link will appear in the LINK_DIST field. If a distance unit  is not specified, the distance unit of the origin features' coordinate system will be used.KILOMETERS—The distance between origin and destination will be calculated in kilometers.METERS—The distance between origin and destination will be calculated in meters.MILES—The distance between origin and destination will be calculated in miles.NAUTICALMILES—The distance between origin and destination will be calculated in nautical miles.YARDS—The distance between origin and destination will be calculated in yards.FEET—The distance between origin and destination will be calculated in feet.
    aggregate_links(optional) (Boolean): Specifies whether overlapping links will be aggregated.AGGREGATE_OVERLAPPING—Overlapping links will be aggregated if the starting point coordinates are the same.NO_AGGREGATE—Overlapping links will not be aggregated. This is the default.
    sum_fields[sum_fields,...](optional) (Value Table): Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are excluded from all calculations.By default, the tool will not calculate any statistics.Numeric attribute fields can be summarized using any statistic. Text attribute fields can be summarized using minimum, maximum, count, first, last, unique, and concatenate statistics.SUM—The values for the specified field will be added together.MEAN—The average for the specified field will be calculated.MIN—The smallest value for all records of the specified field will be found.MAX—The largest value for all records of the specified field will be found.RANGE—The range of values (maximum minus minimum) for the specified field will be calculated.STD—The standard deviation of values in the specified field will be calculated.COUNT—The number of values included in the statistical calculations will be found. Each value will be counted except null values. To determine the number of null values in a field, create a count on the field in question, create a count on a different field that does not contain null values (for example, the OID if present), and subtract the two values.FIRST—The specified field value of the first record in the input will be used.LAST—The specified field value of thee last record in the input will be used.MEDIAN—The median for all records of the specified field will be calculated.VARIANCE—The variance for all records of the specified field will be calculated.
UNIQUE—The number of unique values of the specified field will be counted.
    """
    # Execute Generate_Origin-Destination_Links
    result = arcpy.Generate_Origin-Destination_Links(origin_features, destination_features, out_feature_class, origin_group_field(optional), destination_group_field(optional), line_type(optional), num_nearest(optional), search_distance(optional), distance_unit, aggregate_links(optional), sum_fields[sum_fields,...](optional))
    return result

def summarize_within(in_polygons, in_sum_features, out_feature_class=None, keep_all_polygons(optional)=None, sum_fields[[summary_field,_statistic_type],...](optional)=None, sum_shape(optional)=None, shape_unit(optional)=None, group_field(optional)=None, add_min_maj(optional)=None, add_group_percent(optional)=None, out_group_table(optional)=None):
    """Summarize Within

    in_polygons (Feature Layer): The polygons that will be used to summarize the features, or portions of features, in the input summary layer.
    in_sum_features (Feature Layer): The point, line, or polygon features that will be summarized for each polygon in the input polygons.
    out_feature_class (Feature Class): The output polygon feature class containing the same geometries and attributes as the input polygons. The feature class will include additional attributes for the number of points, length of lines, and area of polygons inside each input polygon and statistics about those features.
    keep_all_polygons(optional) (Boolean): Specifies whether all input polygons or only those intersecting or containing at least one  input summary feature will be copied to the output feature class.KEEP_ALL—All input polygons will be copied to the output feature class. This is the default.ONLY_INTERSECTING—Only input polygons that intersect or contain at least one input summary feature will be copied to the output feature class.
    sum_fields[[summary_field,_statistic_type],...](optional) (Value Table): A list of attribute  field names from the input summary features, as well as statistical summary types that will be calculated for those attribute fields for all points in each polygon. Summary fields must be numeric. Text and other attribute field types are not supported.
The following are the statistic types:Sum—The total value of all the points in each polygon will be calculated.Mean—The average or mean value of all the points in each polygon will be calculated.Min—The smallest value of all the points in each polygon will be identified.Max—The largest value of all the points in each polygon will be identified.Stddev—The standard deviation of all the points in each polygon will be calculated.
    sum_shape(optional) (Boolean): Specifies whether attributes for the number of points, length of lines, and area of polygon features summarized in each input polygon will be added to the output feature class.ADD_SHAPE_SUM—Shape summary attributes will be added to the output feature class. This is the default.NO_SHAPE_SUM—Shape summary attributes will not be added to the output feature class.
    shape_unit(optional) (String): Specifies the unit that will be used when calculating shape summary
attributes. If the input summary features are points, no shape unit is necessary, since only the count of points in each input polygon is added.If the input summary features are lines, specify  a linear unit.  If the input summary features are polygons, specify an areal unit.METERS—The unit will be meters.KILOMETERS—The unit will be kilometers.FEET—The unit will be feet.YARDS—The unit will be yards.MILES—The unit will be miles.ACRES—The unit will be acres.HECTARES—The unit will be hectares.SQUAREMETERS—The unit will be square meters.SQUAREKILOMETERS—The unit will be square kilometers.SQUAREFEET—The unit will be square feet.SQUAREYARDS—The unit will be square yards.SQUAREMILES—The unit will be square miles.
    group_field(optional) (Field): An attribute field from the input summary features that will be used for grouping. Features that have the same group field value will be combined and summarized with other features with the same group field value.When a group field is provided, the  out_grouped_table parameter value is required.
    add_min_maj(optional) (Boolean): Specifies whether minority and majority fields will be added to the output. This parameter allows you to determine which group field value is the minority (least dominant) and the majority (most dominant) within each input polygon.This parameter is enabled if you provided a group_field parameter value.NO_MIN_MAJ—Minority and majority fields will not be added to the output. This is the default.ADD_MIN_MAJ—Minority and majority fields will be added to the output.
    add_group_percent(optional) (Boolean): Specifies whether a percentage attribute field will be added to the output. This parameter allows you to determine the percentage of each attribute value in each group.This parameter is enabled if you provided a group_field parameter value.NO_PERCENT—A percentage attribute field will not be added to the output. This is the default.ADD_PERCENT—A percentage attribute field will be added to the output.
    out_group_table(optional) (Table): An output table that includes summary fields for each group of summary features for each input polygon. The table will have the following attribute fields:Join_ID—An ID corresponding to an ID field added to the output feature classThe group fieldA shape summary fieldOne field for each summary fieldA percentage fieldThis parameter is required when the group_field parameter value is provided.
    """
    # Execute Summarize_Within
    result = arcpy.Summarize_Within(in_polygons, in_sum_features, out_feature_class, keep_all_polygons(optional), sum_fields[[summary_field,_statistic_type],...](optional), sum_shape(optional), shape_unit(optional), group_field(optional), add_min_maj(optional), add_group_percent(optional), out_group_table(optional))
    return result

def summary_statistics(in_table, out_table, statistics_fields[[field,_{statistic_type}],...]=None, case_field[case_field,...](optional)=None, concatenation_separator(optional)=None):
    """Summary Statistics

    in_table (Table View; Raster Layer): The input table containing the fields that will be used to calculate statistics.
    out_table (Table): The output table that will store the calculated statistics.
    statistics_fields[[field,_{statistic_type}],...] (Value Table): Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are excluded from all calculations.Numeric attribute fields can be summarized using any statistic. Text attribute fields can be summarized  using minimum, maximum, count, first, last, unique, concatenate, and mode statistics. Date, Date only, and Timestamp offset attribute fields can be summarized only with the mean, minimum, maximum, count, first, last, unique, and concatenate statistics.The DBMS statistic types are only supported for input geodatabase data sources, including enterprise geodatabases, feature services, cloud data warehouses, and SQLite geodatabases  SUM—The values for the specified field will be added together.MEAN—The average for the specified field will be calculated.MIN—The smallest value of the specified field will be identified.MAX—The largest value of the specified field will be identified.RANGE—The range of values (maximum minus minimum) for the specified field will be calculated.STD—The standard deviation of values for the specified field will be calculated.COUNT—The number of values in the specified field will be identified.FIRST—The specified field value of the first record in the input will be used.LAST—The specified field value of the last record in the input will be used.MEDIAN—The median of the specified field will be calculated.VARIANCE—The variance of the specified field will be calculated.
UNIQUE—The number of unique values of the specified field will be counted.CONCATENATE—The values for the specified field will be concatenated. The values can be separated using the concatenation_separator parameter.MODE—The mode (the most common value) for the specified field will be identified. If more than one value is equally common, the lowest value will be returned.DBMS_SUM—The values for the specified field will be added together.DBMS_MEAN—The average for the specified field will be calculated.DBMS_MIN—The smallest value of the specified field will be identified.DBMS_MAX—The largest value of the specified field will be identified.
DBMS_STD—The standard deviation of values for the specified field will be calculated.DBMS_COUNT—The number of values in the specified field will be identified.
DBMS_MEDIAN—The median of the specified field will be calculated.DBMS_VARIANCE—The variance of the specified field will be calculated.
    case_field[case_field,...](optional) (Field): The field or fields in the input that will be used to calculate statistics separately for each unique attribute value (or combination of attribute values when multiple fields are specified).
    concatenation_separator(optional) (String): A character or characters that will be used to concatenate values when the CONCATENATION option is used for the statistics_fields parameter. By default, the tool will concatenate values without a separator.
    """
    # Execute Summary_Statistics
    result = arcpy.Summary_Statistics(in_table, out_table, statistics_fields[[field,_{statistic_type}],...], case_field[case_field,...](optional), concatenation_separator(optional))
    return result

def tabulate_intersection(in_zone_features, zone_fields[zone_fields,...], in_class_features=None, out_table=None, class_fields[class_fields,...](optional)=None, sum_fields[sum_fields,...](optional)=None, xy_tolerance(optional)=None, out_units(optional)=None):
    """Tabulate Intersection

    in_zone_features (Feature Layer): The features used to identify zones.
    zone_fields[zone_fields,...] (Field): The attribute field or fields that will be used to define zones.
    in_class_features (Feature Layer): The features used to identify classes.
    out_table (Table): The table that will contain the cross tabulation of intersections between zones and classes.
    class_fields[class_fields,...](optional) (Field): The attribute field or fields used to define classes.
    sum_fields[sum_fields,...](optional) (Field): The fields that will be summed from the in_class_features parameter.
    xy_tolerance(optional) (Linear Unit): The distance that determines the range in which features or their vertices are considered equal. By default, this is the x,y tolerance of the in_zone_features parameter value.
Caution:  Changing this parameter's value may cause failure or unexpected results.  It is recommended that you do not modify this parameter. It has been removed from view on the tool dialog box.  By default, the input feature class's spatial reference x,y tolerance property is used.
    out_units(optional) (String): Specifies the units that will be used to calculate area or length measurements. Setting output units when the 
input class features are points is not supported.UNKNOWN—The units will be unknown.KILOMETERS—The units will be kilometers.METERS—The units will be meters.DECIMETERS—The units will be decimeters.CENTIMETERS—The units will be centimeters.MILLIMETERS—The units will be millimeters.MILES_INTERNATIONAL—The units will be statute miles.NAUTICAL_MILES_INTERNATIONAL—The units will be international nautical miles.YARDS_INTERNATIONAL—The units will be international yards.FEET_INTERNATIONAL—The units will be international feet.INCHES_INTERNATIONAL—The units will be international inches.MILES—The units will be US survey miles.NAUTICAL_MILES—The units will be US survey nautical miles.YARDS—The units will be US survey yards.FEET—The units will be US survey feet.INCHES—The units will be US survey inches.DECIMAL_DEGREES—The units will be decimal degrees.POINTS—The units will be points.ARES—The units will be ares.SQUARE_KILOMETERS—The units will be square kilometers.SQUARE_METERS—The units will be square meters.SQUARE_DECIMETERS—The units will be square decimeters.SQUARE_CENTIMETERS—The units will be square centimeters.SQUARE_MILLIMETERS—The units will be square millimeters.SQUARE_MILES—The units will be square statute miles.SQUARE_NAUTICAL_MILES—The area unit will be square international nautical miles.SQUARE_YARDS—The units will be square international yards.SQUARE_FEET—The units will be square international feet.SQUARE_INCHES—The units will be square international inches.SQUARE_MILES_US—The units will be square US survey miles.SQUARE_NAUTICAL_MILES_US—The area unit will be square US survey nautical miles.SQUARE_YARDS_US—The units will be square US survey yards.SQUARE_FEET_US—The units will be square US survey feet.SQUARE_INCHES_US—The units will be square US survey inches.ACRES_US—The units will be US survey acres.HECTARES—The units will be hectares.ACRES—The units will be international acres.
    """
    # Execute Tabulate_Intersection
    result = arcpy.Tabulate_Intersection(in_zone_features, zone_fields[zone_fields,...], in_class_features, out_table, class_fields[class_fields,...](optional), sum_fields[sum_fields,...](optional), xy_tolerance(optional), out_units(optional))
    return result

def summarize_nearby(in_features, in_sum_features, out_feature_class=None, distance_type=None, distances[distance,...]=None, distance_units(optional)=None, time_of_day(optional)=None, time_zone(optional)=None, keep_all_polygons(optional)=None, sum_fields[[summary_field,_statistic_type],...](optional)=None, sum_shape(optional)=None, shape_unit(optional)=None, group_field(optional)=None, add_min_maj(optional)=None, add_group_percent(optional)=None, output_grouped_table(optional)=None):
    """Summarize Nearby

    in_features (Feature Layer): The point, line, or polygon features that will be buffered. Those buffers will be used to summarize the input summary features.
    in_sum_features (Feature Layer): The point, line, or polygon features that will be summarized.
    out_feature_class (Feature Class): The output polygon feature class containing the buffered input features, attributes of the input features, and new attributes about the number points, length of lines, and area of polygons inside each buffer and statistics about those features.
    distance_type (String): Specifies the distance measurement type that will be used to generate buffer areas. Both driving distance and driving time will use the road network and honor restrictions such as one-way streets. Driving time honors the current posted speed limits. To use the drive-time and drive-distance measurement options, you must be signed in to an ArcGIS Online organizational account with Network Analysis privileges. Each time the tool runs successfully, credits are debited from your subscription based on the service used and the results returned from the service. The Credits page provides details about credits.All distance types except straight-line distance use ArcGIS Online routing and network services.DRIVING_DISTANCE—The distance will be covered in a car or other similar small automobiles, such as pickup trucks. Travel follows all rules that are specific to cars.DRIVING_TIME—The distance will be covered within a specified time in a car or other similar small automobiles, such as pickup trucks. Dynamic travel speeds based on traffic are used where it is available when you specify a time of day. Travel follows all rules that are specific to cars.STRAIGHT_LINE—A Euclidean or straight-line distance will be used.TRUCKING_DISTANCE—The distance will be covered along designated truck routes. Travel follows all rules for cars as well as rules specific to trucking.TRUCKING_TIME—The distance will be covered within a specified time when traveling along designated truck routes.  Dynamic travel speeds based on traffic are used where it is available when you specify a time of day. Travel follows all rules for cars as well as rules specific to trucking.WALKING_DISTANCE—The distance will be covered along paths and roads that allow pedestrian traffic.WALKING_TIME—The distance will be covered within a specified time when walking along paths and roads that allow pedestrian traffic.
    distances[distance,...] (Double): Distance values that will define a search distance (for straight-line, driving, trucking, or walking distance) or travel time (for driving, trucking, or walking time). Features that are within (or equal to) the distances you provide will be summarized.Multiple values can be specified. One area around each input feature will be generated for each distance.
    distance_units(optional) (String): Specifies the unit that will be used for the distance values.
MILES—The units will be miles.KILOMETERS—The units will be kilometers.FEET—The units will be feet.YARDS—The units will be yards.METERS—The units will be meters.HOURS—The units will be hours.MINUTES—The units will be minutes.SECONDS—The units will be seconds.
    time_of_day(optional) (Date): The date or time when traffic conditions will be considered during travel time. Traffic conditions, especially in urbanized areas, can significantly impact the area covered within a specified travel time. If no date or time is specified, the distance covered during a specified travel time will not be impacted by traffic. Traffic conditions may be live or typical (historical) based on the date and time specified for this parameter. Esri saves live traffic data for 12 hours and references
predictive data extending 12 hours into the future. If the time and date you specify is within the 24-hour time window, live traffic is used. If it is outside the time window, typical or historic traffic is used.
    time_zone(optional) (String): Specifies the time zone that will be used for the specified time of day. Time zones can be specified in local time or coordinated universal time (UTC).

GEOLOCAL—The time of day refers to the local  time zone or zones in which the input features are located. This option can cause the analysis to have rolling start times across time zones. This is the default.For example, setting a geolocal time of day to 9:00 a.m. causes the drive times for points in the eastern time zone to start at 9:00 a.m. eastern time, and 9:00 a.m. central time for points in the central time zone. (The start times are offset by an hour in real or UTC time.)UTC—The time of day refers to coordinated universal time (UTC). The start times for all points are simultaneous, regardless of time zones.For example, setting a UTC time of day to 9:00 a.m. causes the drive times for points in the eastern time zone to start at 4:00 a.m. eastern time, and 3:00 a.m. central time for points in the central time zone. (The start times are simultaneous.)
    keep_all_polygons(optional) (Boolean): Specifies whether all buffers of the input features or only those intersecting or containing at least one input summary feature will be copied to the output feature class.KEEP_ALL—All buffers will be copied to the output feature class. This is the default.ONLY_INTERSECTING—Only buffers that intersect or contain at least one input summary feature will be copied to the output feature class.
    sum_fields[[summary_field,_statistic_type],...](optional) (Value Table): A list of attribute  field names from the input summary features and statistical summary types that will be calculated for those attribute fields for all points within each input feature buffer. Summary fields must be numeric. Text and other attribute field types are not supported.
The following statistic types are supported:Sum—The total value of all the points in each buffer will be calculated.Mean—The average of all the points in each buffer will be calculated.Min—The smallest value of all the points in each buffer will be identified.Max—The largest value of all the points in each buffer will be identified.Stddev—The standard deviation of all the points in each buffer will be calculated.
    sum_shape(optional) (Boolean): Specifies whether attributes for the number of points, length of lines, and area of polygon features summarized in each input feature buffer (shape summary attributes) will be added to the output feature class. ADD_SHAPE_SUM—Shape summary attributes will be added to the output feature class. This is the default.NO_SHAPE_SUM—Shape summary attributes will not be added to the output feature class.
    shape_unit(optional) (String): Specifies the unit that will be used when calculating shape summary
attributes. If the input summary features are points, no shape unit is necessary, since only the count of points within each input feature buffer is added.If the input summary features are lines, specify  a linear unit.  If the input summary features are polygons, specify an areal unit.METERS—The units will be meters.KILOMETERS—The units will be kilometers.FEET—The units will be feet.YARDS—The units will be yards.MILES—The units will be miles.ACRES—The units will be acres.HECTARES—The units will be hectares.SQUAREMETERS—The units will be square meters.SQUAREKILOMETERS—The units will be square kilometers.SQUAREFEET—The units will be square feet.SQUAREYARDS—The units will be square yards.SQUAREMILES—The units will be square miles.
    group_field(optional) (Field): The attribute field from the input summary features that will be used for grouping. Features that have the same group field value will be combined and summarized with other features with the same group field value.When a group field is specified, an additional output grouped table will be created and its location must be specified in the out_grouped_table parameter.
    add_min_maj(optional) (Boolean): Specifies whether minority (least dominant) and majority (most dominant) group field values within each input feature buffer will be added to the output. This parameter is enabled if you specified a group_field parameter value.
NO_MIN_MAJ—Minority and majority fields will not be added to the output. This is the default.ADD_MIN_MAJ—Minority and majority fields will be added to the output.
    add_group_percent(optional) (Boolean): Specifies whether a percentage of each attribute value in each group will be added to the output. This parameter allows you to determine the percentage of each attribute value in each group. This parameter is enabled if you specified a group_field parameter value.
NO_PERCENT—A percentage attribute field will not be added to the output. This is the default.ADD_PERCENT—A percentage attribute field will be added to the output.
    output_grouped_table(optional) (Table): An output table that includes summary fields for each group of summary features for each input feature buffer. If a group field is specified, the output grouped table is required.The table will have the following attribute fields:Join_ID—An ID corresponding to an ID field added to the output feature classThe group fieldA shape summary field such as count of points or length of linesOne field for each summary fieldPercentage field
    """
    # Execute Summarize_Nearby
    result = arcpy.Summarize_Nearby(in_features, in_sum_features, out_feature_class, distance_type, distances[distance,...], distance_units(optional), time_of_day(optional), time_zone(optional), keep_all_polygons(optional), sum_fields[[summary_field,_statistic_type],...](optional), sum_shape(optional), shape_unit(optional), group_field(optional), add_min_maj(optional), add_group_percent(optional), output_grouped_table(optional))
    return result

def frequency(in_table, out_table, frequency_fields[frequency_fields,...]=None, summary_fields[summary_fields,...](optional)=None):
    """Frequency

    in_table (Table View; Raster Layer): The table containing the field(s) that will be used to calculate frequency statistics.
    out_table (Table): The output table that will store the frequency statistics.
    frequency_fields[frequency_fields,...] (Field): The field(s) used to calculate frequency statistics. Each unique combination of field values will be included as a new row in the output table.
    summary_fields[summary_fields,...](optional) (Field): The attribute field(s) to sum and add to the output table. Values will be summed for each unique combination of frequency fields. Null values are excluded from this calculation.
    """
    # Execute Frequency
    result = arcpy.Frequency(in_table, out_table, frequency_fields[frequency_fields,...], summary_fields[summary_fields,...](optional))
    return result

def enrich(in_features, out_feature_class, variables[variables,...]=None, buffer_type(optional)=None, distance(optional)=None, unit(optional)=None):
    """Enrich

    in_features (Feature Layer): The features to be enriched.
    out_feature_class (Feature Class): A new layer containing both the input attributes and user-selected attributes. User-selected attributes are summarized from underlying demographic boundaries. Only the area inside the input boundary is considered.
    variables[variables,...] (String): The variables to be summarized and added to the output feature class.
    buffer_type(optional) (String): Input point features must have an associated boundary polygon to enrich. When connected to ArcGIS Online, travel mode options are dynamically populated. Input line features can only use Straight Line distance. The default value is Straight Line.
    distance(optional) (Double): Determines the distance or size of an area to enrich (for example, a 1-mile buffer or 5-minute walk time). Units correspond to the buffer type. The default value is 1.
    unit(optional) (String): The units associated with the distance or time parameter.Miles—MilesYards—YardsFeet—FeetKilometers—KilometersMeters—MetersHours—HoursMinutes—MinutesSeconds—Seconds
    """
    # Execute Enrich
    result = arcpy.Enrich(in_features, out_feature_class, variables[variables,...], buffer_type(optional), distance(optional), unit(optional))
    return result

def select(in_features, out_feature_class, where_clause(optional)=None):
    """Select

    in_features (Feature Layer): The input feature class or layer from which features will be selected.
    out_feature_class (Feature Class): The output feature class that will be created. If no expression is used, the output will contain all the input features.
    where_clause(optional) (SQL Expression): The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.
    """
    # Execute Select
    result = arcpy.Select(in_features, out_feature_class, where_clause(optional))
    return result