# Generated ArcGIS Pro data-management Progent Functions
# Corrected on 2025-10-01
# Total tools: 400

import arcpy
import os

class DataManagementTools:
    """Generated spatial analysis functions in progent.pyt format"""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def add_3d_formats_to_multipatch(self, params):
        """Add 3D Formats To Multipatch

Converts a multipatch to a 3D object feature layer by linking the feature class with one or more 3D model formats.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            multipatch_materials = params.get("multipatch_materials")
            formats = params.get("formats")

            arcpy.management.Add3DFormatsToMultipatch(in_features, multipatch_materials, formats)

            self._add_to_map(in_features)
            return {"success": True, "output_layer": os.path.basename(in_features), "output_path": in_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_3d_objects(self, params):
        """Export 3D Objects

Exports 3D object features to one or more 3D model file formats.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            target_folder = params.get("target_folder")
            if target_folder is None:
                return {"success": False, "error": "target_folder parameter is required"}
            formats = params.get("formats")
            if formats is None:
                return {"success": False, "error": "formats parameter is required"}
            name_field = params.get("name_field")
            overwrite = params.get("overwrite")
            if overwrite is None:
                return {"success": False, "error": "overwrite parameter is required"}

            arcpy.management.Export3DObjects(in_features, target_folder, formats, name_field, overwrite)

            return {"success": True, "output_folder": target_folder}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_3d_objects(self, params):
        """Import 3D Objects

Imports 3D models from one or more 3D file formats and creates or updates a 3D object feature layer.
        """
        try:
            files_and_folders = params.get("files_and_folders")
            if files_and_folders is None:
                return {"success": False, "error": "files_and_folders parameter is required"}
            updated_features = params.get("updated_features")
            if updated_features is None:
                return {"success": False, "error": "updated_features parameter is required"}
            update = params.get("update")
            translate = params.get("translate")
            elevation = params.get("elevation")
            scale = params.get("scale")
            rotate = params.get("rotate")
            y_is_up = params.get("y_is_up")
            if y_is_up is None:
                return {"success": False, "error": "y_is_up parameter is required"}

            arcpy.management.Import3DObjects(files_and_folders, updated_features, update, translate, elevation, scale, rotate, y_is_up)

            self._add_to_map(updated_features)
            return {"success": True, "output_layer": os.path.basename(updated_features), "output_path": updated_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_3d_formats_from_multipatch(self, params):
        """Remove 3D Formats From Multipatch

Removes the 3D formats referenced by a 3D object feature layer.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            multipatch_materials = params.get("multipatch_materials")
            formats = params.get("formats")

            arcpy.management.Remove3DFormatsFromMultipatch(in_features, multipatch_materials, formats)

            self._add_to_map(in_features)
            return {"success": True, "output_layer": os.path.basename(in_features), "output_path": in_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_archiving(self, params):
        """Disable Archiving

Disables archiving on a geodatabase feature class, table, or feature dataset.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}
            preserve_history = params.get("preserve_history")

            arcpy.management.DisableArchiving(in_dataset, preserve_history)

            return {"success": True, "message": f"Archiving disabled for {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_archiving(self, params):
        """Enable Archiving

Enables archiving on a table, feature class, or feature dataset.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}

            arcpy.management.EnableArchiving(in_dataset)

            return {"success": True, "message": f"Archiving enabled for {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def trim_archive_history(self, params):
        """Trim Archive History

Deletes retired archive records from nonversioned archive-enabled datasets.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            trim_mode = params.get("trim_mode")
            if trim_mode is None:
                return {"success": False, "error": "trim_mode parameter is required"}
            trim_before_date = params.get("trim_before_date")

            arcpy.management.TrimArchiveHistory(in_table, trim_mode, trim_before_date)

            return {"success": True, "message": f"Archive history trimmed for {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_attachments(self, params):
        """Add Attachments

Adds file attachments to the records of a geodatabase feature class or table.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}
            in_join_field = params.get("in_join_field")
            if in_join_field is None:
                return {"success": False, "error": "in_join_field parameter is required"}
            in_match_table = params.get("in_match_table")
            if in_match_table is None:
                return {"success": False, "error": "in_match_table parameter is required"}
            in_match_join_field = params.get("in_match_join_field")
            if in_match_join_field is None:
                return {"success": False, "error": "in_match_join_field parameter is required"}
            in_match_path_field = params.get("in_match_path_field")
            if in_match_path_field is None:
                return {"success": False, "error": "in_match_path_field parameter is required"}
            in_working_folder = params.get("in_working_folder")

            arcpy.management.AddAttachments(in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_path_field, in_working_folder)

            return {"success": True, "message": f"Attachments added to {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_attachments(self, params):
        """Disable Attachments

Disables attachments on a geodatabase feature class or table.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}

            arcpy.management.DisableAttachments(in_dataset)

            return {"success": True, "message": f"Attachments disabled for {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def downgrade_attachments(self, params):
        """Downgrade Attachments

Downgrades the attachments functionality of a feature class or table.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}

            arcpy.management.DowngradeAttachments(in_dataset)

            return {"success": True, "message": f"Attachments downgraded for {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_attachments(self, params):
        """Enable Attachments

Enables attachments on a geodatabase feature class or table.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}

            arcpy.management.EnableAttachments(in_dataset)

            return {"success": True, "message": f"Attachments enabled for {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_attachments(self, params):
        """Export Attachments

Exports file attachments from the records of a geodatabase feature class or table to a specified folder.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}
            out_location = params.get("out_location")
            if out_location is None:
                return {"success": False, "error": "out_location parameter is required"}
            subdirectory_field = params.get("subdirectory_field")
            name_format = params.get("name_format")
            name_fields = params.get("name_fields")

            arcpy.management.ExportAttachments(in_dataset, out_location, subdirectory_field, name_format, name_fields)

            return {"success": True, "output_folder": out_location}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_attachment_match_table(self, params):
        """Generate Attachment Match Table

Creates a match table to be used with the Add Attachments and Remove Attachments tools.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}
            in_folder = params.get("in_folder")
            if in_folder is None:
                return {"success": False, "error": "in_folder parameter is required"}
            out_match_table = params.get("out_match_table")
            if out_match_table is None:
                return {"success": False, "error": "out_match_table parameter is required"}
            in_key_field = params.get("in_key_field")
            if in_key_field is None:
                return {"success": False, "error": "in_key_field parameter is required"}
            in_file_filter = params.get("in_file_filter")
            in_use_relative_paths = params.get("in_use_relative_paths")
            match_pattern = params.get("match_pattern")

            arcpy.management.GenerateAttachmentMatchTable(in_dataset, in_folder, out_match_table, in_key_field, in_file_filter, in_use_relative_paths, match_pattern)

            self._add_to_map(out_match_table)
            return {"success": True, "output_table": os.path.basename(out_match_table), "output_path": out_match_table}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_attachments(self, params):
        """Remove Attachments

Removes attachments from geodatabase feature class or table records.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}
            in_join_field = params.get("in_join_field")
            if in_join_field is None:
                return {"success": False, "error": "in_join_field parameter is required"}
            in_match_table = params.get("in_match_table")
            if in_match_table is None:
                return {"success": False, "error": "in_match_table parameter is required"}
            in_match_join_field = params.get("in_match_join_field")
            if in_match_join_field is None:
                return {"success": False, "error": "in_match_join_field parameter is required"}
            in_match_name_field = params.get("in_match_name_field")

            arcpy.management.RemoveAttachments(in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_name_field)

            return {"success": True, "message": f"Attachments removed from {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def upgrade_attachments(self, params):
        """Upgrade Attachments

Upgrades the attachments functionality on the data.
        """
        try:
            in_dataset = params.get("in_dataset")
            if in_dataset is None:
                return {"success": False, "error": "in_dataset parameter is required"}

            arcpy.management.UpgradeAttachments(in_dataset)

            return {"success": True, "message": f"Attachments upgraded for {in_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_attribute_rule(self, params):
        """Add Attribute Rule

Adds an attribute rule to a dataset.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            name = params.get("name")
            if name is None:
                return {"success": False, "error": "name parameter is required"}
            type = params.get("type")
            if type is None:
                return {"success": False, "error": "type parameter is required"}
            script_expression = params.get("script_expression")
            if script_expression is None:
                return {"success": False, "error": "script_expression parameter is required"}
            is_editable = params.get("is_editable")
            triggering_events = params.get("triggering_events")
            error_number = params.get("error_number")
            error_message = params.get("error_message")
            description = params.get("description")
            subtype = params.get("subtype")
            field = params.get("field")
            exclude_from_client_evaluation = params.get("exclude_from_client_evaluation")
            batch = params.get("batch")
            severity = params.get("severity")
            tags = params.get("tags")
            triggering_fields = params.get("triggering_fields")

            arcpy.management.AddAttributeRule(in_table, name, type, script_expression, is_editable, triggering_events, error_number, error_message, description, subtype, field, exclude_from_client_evaluation, batch, severity, tags, triggering_fields)

            return {"success": True, "message": f"Attribute rule '{name}' added to {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_attribute_rule(self, params):
        """Alter Attribute Rule

Alters the properties of an attribute rule.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            name = params.get("name")
            if name is None:
                return {"success": False, "error": "name parameter is required"}
            description = params.get("description")
            error_number = params.get("error_number")
            error_message = params.get("error_message")
            tags = params.get("tags")
            triggering_events = params.get("triggering_events")
            script_expression = params.get("script_expression")
            exclude_from_client_evaluation = params.get("exclude_from_client_evaluation")
            triggering_fields = params.get("triggering_fields")
            subtype = params.get("subtype")

            arcpy.management.AlterAttributeRule(in_table, name, description, error_number, error_message, tags, triggering_events, script_expression, exclude_from_client_evaluation, triggering_fields, subtype)

            return {"success": True, "message": f"Attribute rule '{name}' altered in {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_attribute_rule(self, params):
        """Delete Attribute Rule

Deletes one or more attribute rules from a dataset.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            names = params.get("names")
            if names is None:
                return {"success": False, "error": "names parameter is required"}
            type = params.get("type")

            arcpy.management.DeleteAttributeRule(in_table, names, type)

            return {"success": True, "message": f"Attribute rule(s) deleted from {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_attribute_rules(self, params):
        """Disable Attribute Rules

Disables one or more attribute rules for a dataset.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            names = params.get("names")
            if names is None:
                return {"success": False, "error": "names parameter is required"}
            type = params.get("type")

            arcpy.management.DisableAttributeRules(in_table, names, type)

            return {"success": True, "message": f"Attribute rule(s) disabled for {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_attribute_rules(self, params):
        """Enable Attribute Rules

Enables one or more attribute rules in a dataset.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            names = params.get("names")
            if names is None:
                return {"success": False, "error": "names parameter is required"}
            type = params.get("type")

            arcpy.management.EnableAttributeRules(in_table, names, type)

            return {"success": True, "message": f"Attribute rule(s) enabled for {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def evaluate_rules(self, params):
        """Evaluate Rules

Evaluates geodatabase rules and functionality.
        """
        try:
            in_workspace = params.get("in_workspace")
            if in_workspace is None:
                return {"success": False, "error": "in_workspace parameter is required"}
            evaluation_types = params.get("evaluation_types")
            if evaluation_types is None:
                return {"success": False, "error": "evaluation_types parameter is required"}
            extent = params.get("extent")
            run_async = params.get("run_async")

            arcpy.management.EvaluateRules(in_workspace, evaluation_types, extent, run_async)

            return {"success": True, "message": f"Rules evaluated for {in_workspace}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_attribute_rules(self, params):
        """Export Attribute Rules

Exports attribute rules from a dataset to a comma-separated values file (.csv).
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            out_csv_file = params.get("out_csv_file")
            if out_csv_file is None:
                return {"success": False, "error": "out_csv_file parameter is required"}

            arcpy.management.ExportAttributeRules(in_table, out_csv_file)

            return {"success": True, "output_file": out_csv_file}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_attribute_rules(self, params):
        """Import Attribute Rules

Imports attribute rules from comma-separated value files (.csv) to a dataset.
        """
        try:
            target_table = params.get("target_table")
            if target_table is None:
                return {"success": False, "error": "target_table parameter is required"}
            csv_file = params.get("csv_file")
            if csv_file is None:
                return {"success": False, "error": "csv_file parameter is required"}

            arcpy.management.ImportAttributeRules(target_table, csv_file)

            return {"success": True, "message": f"Attribute rules imported to {target_table} from {csv_file}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def reorder_attribute_rule(self, params):
        """Reorder Attribute Rule

Reorders the evaluation order of an attribute rule.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            name = params.get("name")
            if name is None:
                return {"success": False, "error": "name parameter is required"}
            evaluation_order = params.get("evaluation_order")
            if evaluation_order is None:
                return {"success": False, "error": "evaluation_order parameter is required"}

            arcpy.management.ReorderAttributeRule(in_table, name, evaluation_order)

            return {"success": True, "message": f"Evaluation order for rule '{name}' in {in_table} has been reordered."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_items_to_catalog_dataset(self, params):
        """Add Items To Catalog Dataset

Adds workspace items and layers to an existing catalog dataset.
        """
        try:
            target_catalog_dataset = params.get("target_catalog_dataset")
            if target_catalog_dataset is None:
                return {"success": False, "error": "target_catalog_dataset parameter is required"}
            input_items = params.get("input_items")
            if input_items is None:
                return {"success": False, "error": "input_items parameter is required"}
            input_item_types = params.get("input_item_types")
            include_subfolders = params.get("include_subfolders")
            footprint_type = params.get("footprint_type")

            arcpy.management.AddItemsToCatalogDataset(target_catalog_dataset, input_items, input_item_types, include_subfolders, footprint_type)

            return {"success": True, "message": f"Items added to {target_catalog_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_portal_items_to_catalog_dataset(self, params):
        """Add Portal Items To Catalog Dataset

Adds ArcGIS Online or ArcGIS Enterprise portal service items to an existing catalog dataset.
        """
        try:
            target_catalog_dataset = params.get("target_catalog_dataset")
            if target_catalog_dataset is None:
                return {"success": False, "error": "target_catalog_dataset parameter is required"}
            input_portal_itemtypes = params.get("input_portal_itemtypes")
            content = params.get("content")
            portal_folders = params.get("portal_folders")
            portal_groups = params.get("portal_groups")
            access_level = params.get("access_level")

            arcpy.management.AddPortalItemsToCatalogDataset(target_catalog_dataset, input_portal_itemtypes, content, portal_folders, portal_groups, access_level)

            return {"success": True, "message": f"Portal items added to {target_catalog_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_catalog_dataset(self, params):
        """Create Catalog Dataset

Creates a catalog dataset to which collections of layers, rasters, datasets, and other items can be added.
        """
        try:
            out_path = params.get("out_path")
            if out_path is None:
                return {"success": False, "error": "out_path parameter is required"}
            out_name = params.get("out_name")
            if out_name is None:
                return {"success": False, "error": "out_name parameter is required"}
            spatial_reference = params.get("spatial_reference")
            template = params.get("template")
            has_z = params.get("has_z")
            out_alias = params.get("out_alias")
            config_keyword = params.get("config_keyword")

            output_catalog = os.path.join(out_path, out_name)
            arcpy.management.CreateCatalogDataset(out_path, out_name, spatial_reference, template, has_z, out_alias, config_keyword)

            self._add_to_map(output_catalog)
            return {"success": True, "output_layer": out_name, "output_path": output_catalog}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_feature_changes(self, params):
        """Detect Feature Changes

Finds where the update line features spatially match the base line features and detects spatial changes, attribute changes, or both, as well as no change.
        """
        try:
            update_features = params.get("update_features")
            if update_features is None:
                return {"success": False, "error": "update_features parameter is required"}
            base_features = params.get("base_features")
            if base_features is None:
                return {"success": False, "error": "base_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None:
                return {"success": False, "error": "search_distance parameter is required"}
            match_fields = params.get("match_fieldssource_field_target_field")
            out_match_table = params.get("out_match_table")
            change_tolerance = params.get("change_tolerance")
            compare_fields = params.get("compare_fieldssource_field_target_field")
            compare_line_direction = params.get("compare_line_direction")

            arcpy.management.DetectFeatureChanges(update_features, base_features, out_feature_class, search_distance, match_fields, out_match_table, change_tolerance, compare_fields, compare_line_direction)

            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": os.path.basename(out_feature_class), "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_compare(self, params):
        """Feature Compare

Compares two feature classes or layers and returns the comparison results.
        """
        try:
            in_base_features = params.get("in_base_features")
            if in_base_features is None:
                return {"success": False, "error": "in_base_features parameter is required"}
            in_test_features = params.get("in_test_features")
            if in_test_features is None:
                return {"success": False, "error": "in_test_features parameter is required"}
            sort_field = params.get("sort_field")
            if sort_field is None:
                return {"success": False, "error": "sort_field parameter is required"}
            compare_type = params.get("compare_type")
            ignore_options = params.get("ignore_options")
            xy_tolerance = params.get("xy_tolerance")
            m_tolerance = params.get("m_tolerance")
            z_tolerance = params.get("z_tolerance")
            attribute_tolerances = params.get("attribute_tolerancesfield_tolerance")
            omit_field = params.get("omit_field")
            continue_compare = params.get("continue_compare")
            out_compare_file = params.get("out_compare_file")

            result = arcpy.management.FeatureCompare(in_base_features, in_test_features, sort_field, compare_type, ignore_options, xy_tolerance, m_tolerance, z_tolerance, attribute_tolerances, omit_field, continue_compare, out_compare_file)

            compare_result = result.getOutput(0)

            return {"success": True, "compare_result": compare_result, "output_file": out_compare_file}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def file_compare(self, params):
        """File Compare

Compares two files and returns the comparison results.
        """
        try:
            in_base_file = params.get("in_base_file")
            if in_base_file is None:
                return {"success": False, "error": "in_base_file parameter is required"}
            in_test_file = params.get("in_test_file")
            if in_test_file is None:
                return {"success": False, "error": "in_test_file parameter is required"}
            file_type = params.get("file_type")
            continue_compare = params.get("continue_compare")
            out_compare_file = params.get("out_compare_file")

            result = arcpy.management.FileCompare(in_base_file, in_test_file, file_type, continue_compare, out_compare_file)

            compare_result = result.getOutput(0)
            return {"success": True, "compare_result": compare_result, "output_file": out_compare_file}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_compare(self, params):
        """Raster Compare

Compares the properties of two raster datasets or two mosaic datasets.
        """
        try:
            in_base_raster = params.get("in_base_raster")
            if in_base_raster is None:
                return {"success": False, "error": "in_base_raster parameter is required"}
            in_test_raster = params.get("in_test_raster")
            if in_test_raster is None:
                return {"success": False, "error": "in_test_raster parameter is required"}
            compare_type = params.get("compare_type")
            ignore_option = params.get("ignore_option")
            continue_compare = params.get("continue_compare")
            out_compare_file = params.get("out_compare_file")
            parameter_tolerances = params.get("parameter_tolerancesparameter_tolerance_type")
            attribute_tolerances = params.get("attribute_tolerancesfield_tolerance")
            omit_field = params.get("omit_field")

            result = arcpy.management.RasterCompare(in_base_raster, in_test_raster, compare_type, ignore_option, continue_compare, out_compare_file, parameter_tolerances, attribute_tolerances, omit_field)

            compare_result = result.getOutput(0)
            return {"success": True, "compare_result": compare_result, "output_file": out_compare_file}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_compare(self, params):
        """Table Compare

Compares two tables or table views and returns the comparison results.
        """
        try:
            in_base_table = params.get("in_base_table")
            if in_base_table is None:
                return {"success": False, "error": "in_base_table parameter is required"}
            in_test_table = params.get("in_test_table")
            if in_test_table is None:
                return {"success": False, "error": "in_test_table parameter is required"}
            sort_field = params.get("sort_field")
            if sort_field is None:
                return {"success": False, "error": "sort_field parameter is required"}
            compare_type = params.get("compare_type")
            ignore_options = params.get("ignore_options")
            attribute_tolerances = params.get("attribute_tolerancesfield_tolerance")
            omit_field = params.get("omit_field")
            continue_compare = params.get("continue_compare")
            out_compare_file = params.get("out_compare_file")

            result = arcpy.management.TableCompare(in_base_table, in_test_table, sort_field, compare_type, ignore_options, attribute_tolerances, omit_field, continue_compare, out_compare_file)

            compare_result = result.getOutput(0)
            return {"success": True, "compare_result": compare_result, "output_file": out_compare_file}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tin_compare(self, params):
        """TIN Compare

Compares two TINs and returns the comparison results.
        """
        try:
            in_base_tin = params.get("in_base_tin")
            if in_base_tin is None:
                return {"success": False, "error": "in_base_tin parameter is required"}
            in_test_tin = params.get("in_test_tin")
            if in_test_tin is None:
                return {"success": False, "error": "in_test_tin parameter is required"}
            compare_type = params.get("compare_type")
            continue_compare = params.get("continue_compare")
            out_compare_file = params.get("out_compare_file")

            result = arcpy.management.TINCompare(in_base_tin, in_test_tin, compare_type, continue_compare, out_compare_file)

            compare_result = result.getOutput(0)
            return {"success": True, "compare_result": compare_result, "output_file": out_compare_file}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_field_multiple(self, params):
        """Add Fields (multiple)

Adds new fields to a table, feature class, or raster.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            template = params.get("template")

            arcpy.management.AddFields(in_table, template)

            return {"success": True, "message": f"Fields added to {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_fields_multiple(self, params):
        """Calculate Fields (multiple)

Calculates the values of two or more fields for a feature class, feature layer, or raster.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            expression_type = params.get("expression_type")
            if expression_type is None:
                return {"success": False, "error": "expression_type parameter is required"}
            fields = params.get("fields")
            if fields is None:
                return {"success": False, "error": "fields parameter is required"}
            code_block = params.get("code_block")
            enforce_domains = params.get("enforce_domains")

            arcpy.management.CalculateFields(in_table, expression_type, fields, code_block, enforce_domains)

            return {"success": True, "message": f"Fields calculated for {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_fields(self, params):
        """Add Fields (multiple)

Adds new fields to a table, feature class, or raster.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            field_description = params.get("field_description")
            if field_description is None:
                return {"success": False, "error": "field_description parameter is required"}

            arcpy.management.AddFields(in_table, field_description)

            return {"success": True, "message": f"Fields added to {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def calculate_fields(self, params):
        """Calculate Fields (multiple)

Calculates the values of two or more fields for a feature class, feature layer, or raster.
        """
        try:
            in_table = params.get("in_table")
            if in_table is None:
                return {"success": False, "error": "in_table parameter is required"}
            expression_type = params.get("expression_type", "PYTHON3")
            fields = params.get("fields")
            if fields is None:
                return {"success": False, "error": "fields parameter is required"}
            code_block = params.get("code_block")
            enforce_domains = params.get("enforce_domains", "NO_ENFORCE_DOMAINS")

            arcpy.management.CalculateFields(in_table, expression_type, fields, code_block, enforce_domains)

            return {"success": True, "message": f"Fields calculated for {in_table}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_fishnet(self, params):
        """Creates a fishnet of rectangular cells."""
        try:
            out_feature_class = params.get("out_feature_class")
            if not out_feature_class:
                return {"success": False, "error": "out_feature_class parameter is required"}

            origin_coord = params.get("origin_coord")
            if not origin_coord:
                return {"success": False, "error": "origin_coord parameter is required"}

            y_axis_coord = params.get("y_axis_coord")
            if not y_axis_coord:
                return {"success": False, "error": "y_axis_coord parameter is required"}

            cell_width = params.get("cell_width", 0)
            cell_height = params.get("cell_height", 0)
            number_rows = params.get("number_rows", 0)
            number_columns = params.get("number_columns", 0)
            corner_coord = params.get("corner_coord")
            labels = params.get("labels", "NO_LABELS")
            template = params.get("template", "#")
            geometry_type = params.get("geometry_type", "POLYGON")

            arcpy.management.CreateFishnet(
                out_feature_class, origin_coord, y_axis_coord,
                cell_width, cell_height, number_rows, number_columns,
                corner_coord, labels, template, geometry_type
            )

            self._add_to_map(out_feature_class)
            return {"success": True, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_random_points(self, params):
        """Creates a specified number of random point features."""
        try:
            out_path = params.get("out_path")
            if not out_path:
                return {"success": False, "error": "out_path parameter is required"}

            out_name = params.get("out_name")
            if not out_name:
                return {"success": False, "error": "out_name parameter is required"}

            constraining_feature_class = params.get("constraining_feature_class")
            constraining_extent = params.get("constraining_extent")
            number_of_points_or_field = params.get("number_of_points_or_field", 0)
            minimum_allowed_distance = params.get("minimum_allowed_distance")
            create_multipoint_output = params.get("create_multipoint_output", "POINT")
            multipoint_size = params.get("multipoint_size", 0)

            out_feature_class = os.path.join(out_path, out_name)
            arcpy.management.CreateRandomPoints(
                out_path, out_name, constraining_feature_class,
                constraining_extent, number_of_points_or_field,
                minimum_allowed_distance, create_multipoint_output, multipoint_size
            )

            self._add_to_map(out_feature_class)
            return {"success": True, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_spatially_balanced_points(self, params):
        """Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design."""
        try:
            in_probability_raster = params.get("in_probability_raster")
            if not in_probability_raster:
                return {"success": False, "error": "in_probability_raster parameter is required"}

            number_output_points = params.get("number_output_points")
            if not number_output_points:
                return {"success": False, "error": "number_output_points parameter is required"}

            out_feature_class = params.get("out_feature_class")
            if not out_feature_class:
                return {"success": False, "error": "out_feature_class parameter is required"}

            arcpy.management.CreateSpatiallyBalancedPoints(
                in_probability_raster, number_output_points, out_feature_class
            )

            self._add_to_map(out_feature_class)
            return {"success": True, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_spatial_sampling_locations(self, params):
        """Creates sample locations within a continuous study area using simple random, stratified, systematic (gridded), or cluster sampling designs."""
        try:
            in_study_area = params.get("in_study_area")
            if not in_study_area:
                return {"success": False, "error": "in_study_area parameter is required"}

            out_features = params.get("out_features")
            if not out_features:
                return {"success": False, "error": "out_features parameter is required"}

            sampling_method = params.get("sampling_method", "SIMPLE_RANDOM")
            strata_id_field = params.get("strata_id_field")
            strata_count_method = params.get("strata_count_method", "EQUAL")
            bin_shape = params.get("bin_shape", "SQUARE")
            bin_size = params.get("bin_size")
            h3_resolution = params.get("h3_resolution")
            num_samples = params.get("num_samples", 1)
            num_samples_per_strata = params.get("num_samples_per_strata")
            population_field = params.get("population_field")
            geometry_type = params.get("geometry_type", "POINT")
            min_distance = params.get("min_distance")
            spatial_relationship = params.get("spatial_relationship", "INTERSECT")

            arcpy.management.CreateSpatialSamplingLocations(
                in_study_area, out_features, sampling_method, strata_id_field,
                strata_count_method, bin_shape, bin_size, h3_resolution,
                num_samples, num_samples_per_strata, population_field,
                geometry_type, min_distance, spatial_relationship
            )

            self._add_to_map(out_features)
            return {"success": True, "output_path": out_features}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_along_lines(self, params):
        """Creates point features along lines or polygons."""
        try:
            input_features = params.get("input_features")
            if not input_features:
                return {"success": False, "error": "input_features parameter is required"}

            output_feature_class = params.get("output_feature_class")
            if not output_feature_class:
                return {"success": False, "error": "output_feature_class parameter is required"}

            point_placement = params.get("point_placement", "DISTANCE")
            distance = params.get("distance")
            percentage = params.get("percentage")
            include_end_points = params.get("include_end_points", False)
            add_chainage_fields = params.get("add_chainage_fields", False)

            arcpy.management.GeneratePointsAlongLines(
                input_features, output_feature_class, point_placement,
                distance, percentage, include_end_points, add_chainage_fields
            )

            self._add_to_map(output_feature_class)
            return {"success": True, "output_path": output_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_rectangles_along_lines(self, params):
        """Creates a series of rectangular polygons that follow a single linear feature or a group of linear features."""
        try:
            in_features = params.get("in_features")
            if not in_features:
                return {"success": False, "error": "in_features parameter is required"}

            out_feature_class = params.get("out_feature_class")
            if not out_feature_class:
                return {"success": False, "error": "out_feature_class parameter is required"}

            length_along_line = params.get("length_along_line")
            if not length_along_line:
                return {"success": False, "error": "length_along_line parameter is required"}

            spatial_sort_method = params.get("spatial_sort_method", "UL_TO_LR")

            arcpy.management.GenerateRectanglesAlongLines(
                in_features, out_feature_class, length_along_line, spatial_sort_method
            )

            self._add_to_map(out_feature_class)
            return {"success": True, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_tessellation(self, params):
        """Generates a tessellated grid of regular polygon features to cover a given extent."""
        try:
            output_feature_class = params.get("output_feature_class")
            if not output_feature_class:
                return {"success": False, "error": "output_feature_class parameter is required"}

            extent = params.get("extent")
            if not extent:
                return {"success": False, "error": "extent parameter is required"}

            shape_type = params.get("shape_type", "SQUARE")
            size = params.get("size")
            spatial_reference = params.get("spatial_reference")
            h3_resolution = params.get("h3_resolution")

            arcpy.management.GenerateTessellation(
                output_feature_class, extent, shape_type, size, spatial_reference, h3_resolution
            )

            self._add_to_map(output_feature_class)
            return {"success": True, "output_path": output_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_transects_along_lines(self, params):
        """Creates perpendicular transect lines at a regular interval along lines."""
        try:
            in_features = params.get("in_features")
            if not in_features:
                return {"success": False, "error": "in_features parameter is required"}

            out_feature_class = params.get("out_feature_class")
            if not out_feature_class:
                return {"success": False, "error": "out_feature_class parameter is required"}

            interval = params.get("interval")
            if not interval:
                return {"success": False, "error": "interval parameter is required"}

            transect_length = params.get("transect_length")
            if not transect_length:
                return {"success": False, "error": "transect_length parameter is required"}

            include_ends = params.get("include_ends", False)

            arcpy.management.GenerateTransectsAlongLines(
                in_features, out_feature_class, interval, transect_length, include_ends
            )

            self._add_to_map(out_feature_class)
            return {"success": True, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def subset_features(self, params):
        """Divides the records of a feature class or table into two subsets: one for training and one for testing."""
        try:
            in_features = params.get("in_features")
            if not in_features:
                return {"success": False, "error": "in_features parameter is required"}

            out_training_feature_class = params.get("out_training_feature_class")
            if not out_training_feature_class:
                return {"success": False, "error": "out_training_feature_class parameter is required"}

            out_test_feature_class = params.get("out_test_feature_class")
            size_of_training_dataset = params.get("size_of_training_dataset", 50)
            subset_size_units = params.get("subset_size_units", "PERCENTAGE_OF_INPUT")

            arcpy.management.SubsetFeatures(
                in_features, out_training_feature_class, out_test_feature_class,
                size_of_training_dataset, subset_size_units
            )

            self._add_to_map(out_training_feature_class)
            if out_test_feature_class:
                self._add_to_map(out_test_feature_class)

            return {"success": True, "training_output": out_training_feature_class, "test_output": out_test_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_subtype(self, params):
        """Adds a new subtype to the subtypes in the input table."""
        try:
            in_table = params.get("in_table")
            if not in_table:
                return {"success": False, "error": "in_table parameter is required"}

            subtype_code = params.get("subtype_code")
            if subtype_code is None:
                return {"success": False, "error": "subtype_code parameter is required"}

            subtype_description = params.get("subtype_description")
            if not subtype_description:
                return {"success": False, "error": "subtype_description parameter is required"}

            arcpy.management.AddSubtype(in_table, subtype_code, subtype_description)

            return {"success": True, "message": f"Subtype '{subtype_description}' added to {in_table}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def remove_subtype(self, params):
        """Removes a subtype from the input table using its code."""
        try:
            in_table = params.get("in_table")
            if not in_table:
                return {"success": False, "error": "in_table parameter is required"}

            subtype_code = params.get("subtype_code")
            if not subtype_code:
                return {"success": False, "error": "subtype_code parameter is required"}

            arcpy.management.RemoveSubtype(in_table, subtype_code)

            return {"success": True, "message": f"Subtype with code '{subtype_code}' removed from {in_table}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def set_default_subtype(self, params):
        """Sets the default value or code for the input table's subtype."""
        try:
            in_table = params.get("in_table")
            if not in_table:
                return {"success": False, "error": "in_table parameter is required"}

            subtype_code = params.get("subtype_code")
            if subtype_code is None:
                return {"success": False, "error": "subtype_code parameter is required"}

            arcpy.management.SetDefaultSubtype(in_table, subtype_code)

            return {"success": True, "message": f"Default subtype for {in_table} set to code '{subtype_code}'."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def set_subtype_field(self, params):
        """Defines the field in the input table or feature class that stores the subtype codes."""
        try:
            in_table = params.get("in_table")
            if not in_table:
                return {"success": False, "error": "in_table parameter is required"}

            field = params.get("field")
            if not field:
                return {"success": False, "error": "field parameter is required"}

            clear_value = params.get("clear_value", False)

            arcpy.management.SetSubtypeField(in_table, field, clear_value)

            return {"success": True, "message": f"Subtype field for {in_table} set to '{field}'."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def analyze(self, params):
        """Updates database statistics of business tables, feature tables, and delta tables, along with the statistics of those tables' indexes."""
        try:
            in_dataset = params.get("in_dataset")
            if not in_dataset:
                return {"success": False, "error": "in_dataset parameter is required"}

            components = params.get("components")
            if not components:
                return {"success": False, "error": "components parameter is required"}

            arcpy.management.Analyze(in_dataset, components)

            return {"success": True, "message": f"Analysis complete for {in_dataset}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def copy_rows(self, params):
        """Copies the rows of a table to a different table."""
        try:
            in_rows = params.get("in_rows")
            if not in_rows:
                return {"success": False, "error": "in_rows parameter is required"}

            out_table = params.get("out_table")
            if not out_table:
                return {"success": False, "error": "out_table parameter is required"}

            config_keyword = params.get("config_keyword")

            arcpy.management.CopyRows(in_rows, out_table, config_keyword)

            return {"success": True, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_table(self, params):
        """Creates a geodatabase table or a dBASE table."""
        try:
            out_path = params.get("out_path")
            if not out_path:
                return {"success": False, "error": "out_path parameter is required"}

            out_name = params.get("out_name")
            if not out_name:
                return {"success": False, "error": "out_name parameter is required"}

            template = params.get("template")
            config_keyword = params.get("config_keyword")
            out_alias = params.get("out_alias")
            oid_type = params.get("oid_type")

            out_table = os.path.join(out_path, out_name)
            arcpy.management.CreateTable(
                out_path, out_name, template, config_keyword, out_alias, oid_type
            )

            return {"success": True, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_unregistered_table(self, params):
        """Creates an empty table in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database."""
        try:
            out_path = params.get("out_path")
            if not out_path:
                return {"success": False, "error": "out_path parameter is required"}

            out_name = params.get("out_name")
            if not out_name:
                return {"success": False, "error": "out_name parameter is required"}

            template = params.get("template")
            config_keyword = params.get("config_keyword")

            out_table = os.path.join(out_path, out_name)
            arcpy.management.CreateUnregisteredTable(
                out_path, out_name, template, config_keyword
            )

            return {"success": True, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_rows(self, params):
        """Deletes all or the selected subset of rows from the input."""
        try:
            in_rows = params.get("in_rows")
            if not in_rows:
                return {"success": False, "error": "in_rows parameter is required"}

            arcpy.management.DeleteRows(in_rows)

            return {"success": True, "message": f"Rows deleted from {in_rows}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_count(self, params):
        """Returns the total number of rows for a table."""
        try:
            in_rows = params.get("in_rows")
            if not in_rows:
                return {"success": False, "error": "in_rows parameter is required"}

            result = arcpy.management.GetCount(in_rows)
            count = int(result.getOutput(0))

            return {"success": True, "count": count}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def pivot_table(self, params):
        """Creates a table from the input table by reducing redundancy in records and flattening one-to-many relationships."""
        try:
            in_table = params.get("in_table")
            if not in_table:
                return {"success": False, "error": "in_table parameter is required"}

            fields = params.get("fields")
            if not fields:
                return {"success": False, "error": "fields parameter is required"}

            pivot_field = params.get("pivot_field")
            if not pivot_field:
                return {"success": False, "error": "pivot_field parameter is required"}

            value_field = params.get("value_field")
            if not value_field:
                return {"success": False, "error": "value_field parameter is required"}

            out_table = params.get("out_table")
            if not out_table:
                return {"success": False, "error": "out_table parameter is required"}

            arcpy.management.PivotTable(
                in_table, fields, pivot_field, value_field, out_table
            )

            self._add_to_map(out_table)
            return {"success": True, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def truncate_table(self, params):
        """Removes all rows from a database table or feature class using truncate procedures in the database."""
        try:
            in_table = params.get("in_table")
            if not in_table:
                return {"success": False, "error": "in_table parameter is required"}

            arcpy.management.TruncateTable(in_table)

            return {"success": True, "message": f"Table {in_table} truncated."}
        except Exception as e:
            return {"success": False, "error": str(e)}