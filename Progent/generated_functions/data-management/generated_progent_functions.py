# Generated ArcGIS Pro data-management Progent Functions
# Generated on 2025-10-01T14:27:18.440280
# Total tools: 400

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

    def add_3d_formats_to_multipatch(self, params):
        """Add 3D Formats To Multipatch

Converts a multipatch to a 3D object feature layer by linking the feature class with one or more 3D model formats.

        params: {"in_features": <Table View>, "multipatch_materials": <Boolean>, "formats": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        multipatch_materials = params.get("multipatch_materials")
        formats = params.get("formats")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Add_3D_Formats_To_Multipatch"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add 3D Formats To Multipatch
            arcpy.Add3DFormatsToMultipatch(in_features, multipatch_materials, formats)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_3d_objects(self, params):
        """Export 3D Objects

Exports 3D object features to one or more 3D model file formats.

        params: {"in_features": <Feature Layer>, "target_folder": <Folder>, "formats": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Export_3D_Objects"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export 3D Objects
            arcpy.Export3DObjects(in_features, target_folder, formats, name_field, overwrite)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_3d_objects(self, params):
        """Import 3D Objects

Imports 3D models from one or more 3D file formats and creates or updates a 3D object feature layer.

        params: {"files_and_folders": <File; Folder>, "updated_features": <Feature Layer>, "update": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{files_and_folders.replace(' ', '_')}_Import_3D_Objects"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import 3D Objects
            arcpy.Import3DObjects(files_and_folders, updated_features, update, translate, elevation, scale, rotate, y_is_up)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_3d_formats_from_multipatch(self, params):
        """Remove 3D Formats From Multipatch

Removes the 3D formats  referenced by a 3D object feature layer.

        params: {"in_features": <Feature Layer>, "multipatch_materials": <Boolean>, "formats": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        multipatch_materials = params.get("multipatch_materials")
        formats = params.get("formats")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Remove_3D_Formats_From_Multipatch"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove 3D Formats From Multipatch
            arcpy.Remove3DFormatsFromMultipatch(in_features, multipatch_materials, formats)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_archiving(self, params):
        """Disable Archiving

Disables archiving on a geodatabase feature class, table, or feature dataset. Learn more about the process of disabling archiving

        params: {"in_dataset": <Table; Feature Class; Feature Dataset>, "preserve_history": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        preserve_history = params.get("preserve_history")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Disable_Archiving"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disable Archiving
            arcpy.DisableArchiving(in_dataset, preserve_history)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_archiving(self, params):
        """Enable Archiving

Enables archiving on a table, feature class, or feature dataset. Learn more about the process of enabling  archiving

        params: {"in_dataset": <Table; Feature Class; Feature Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Enable_Archiving"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Archiving
            arcpy.EnableArchiving(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def trim_archive_history(self, params):
        """Trim Archive History

Deletes retired archive records from nonversioned archive-enabled datasets. Over time, the archive history of a table can increase exponentially as the edit history is maintained. This can affect storage and backup management decisions and may affect performance if the data becomes too large for the system in place. Some organizations may use nonversioned archiving because it is required for certain functionality and have no need for historical records, or they may want to remove older data that is no longer relevant. This tool allows you to delete all retired rows or the retired rows older than a specified date. Learn more about trimming the archive history

        params: {"in_table": <Table View>, "trim_mode": <String>, "trim_before_date": <Date>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        trim_mode = params.get("trim_mode")
        if trim_mode is None:
            return {"success": False, "error": "trim_mode parameter is required"}
        trim_before_date = params.get("trim_before_date")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Trim_Archive_History"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Trim Archive History
            arcpy.TrimArchiveHistory(in_table, trim_mode, trim_before_date)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_attachments(self, params):
        """Add Attachments

Adds file attachments to the records of a geodatabase feature class or table. The attachments are stored in the geodatabase in a separate attachment table that maintains linkage to the target dataset. Attachments are added to the target dataset using a match table that indicates for each input record (or an attribute group of records) the path to a file to add as an attachment to that record. Learn more about working with the  tools in the Attachments toolset

        params: {"in_dataset": <Table View>, "in_join_field": <Field>, "in_match_table": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Add_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Attachments
            arcpy.AddAttachments(in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_path_field, in_working_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_attachments(self, params):
        """Disable Attachments

Disables attachments on a geodatabase feature class or table. The tool deletes the attachment relationship class and attachment table.

        params: {"in_dataset": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Disable_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disable Attachments
            arcpy.DisableAttachments(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def downgrade_attachments(self, params):
        """Downgrade Attachments

Downgrades the attachments functionality of a feature class or table.

        params: {"in_dataset": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Downgrade_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Downgrade Attachments
            arcpy.DowngradeAttachments(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_attachments(self, params):
        """Enable Attachments

Enables attachments on a geodatabase feature class or table. The tool creates the necessary attachment relationship class and attachment table that will store attachment files internally. Learn more about working with the Attachments geoprocessing tools

        params: {"in_dataset": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Enable_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Attachments
            arcpy.EnableAttachments(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_attachments(self, params):
        """Export Attachments

Exports file attachments from the records of a geodatabase feature class or table to a specified folder. Attachments can also be exported to  subdirectories  based on an attribute value from a specified attribute column. Exported attachments can be renamed using one or more field attribute values. Learn more about working with the Attachments geoprocessing tools

        params: {"in_dataset": <Table View>, "out_location": <Folder>, "subdirectory_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Export_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Attachments
            arcpy.ExportAttachments(in_dataset, out_location, subdirectory_field, name_format, name_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_attachment_match_table(self, params):
        """Generate Attachment Match Table

Creates a match table to be used with the Add Attachments and Remove Attachments tools. Learn more about working with the Attachments geoprocessing tools

        params: {"in_dataset": <Table View>, "in_folder": <Folder>, "out_match_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Generate_Attachment_Match_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Attachment Match Table
            arcpy.GenerateAttachmentMatchTable(in_dataset, in_folder, out_match_table, in_key_field, in_file_filter, in_use_relative_paths, match_pattern)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_attachments(self, params):
        """Remove Attachments

Removes attachments from geodatabase feature class or table records. Since attachments are not actually stored in the input dataset, no changes will be made to that feature class or table. Changes will be made to the related geodatabase table that stores the attachments and maintains linkage with the input dataset. A match table is used to identify the input records (or attribute groups of records) that will have attachments removed. Learn more about working with the tools in the Attachments toolset

        params: {"in_dataset": <Table View>, "in_join_field": <Field>, "in_match_table": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Remove_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Attachments
            arcpy.RemoveAttachments(in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_name_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def upgrade_attachments(self, params):
        """Upgrade Attachments

Upgrades the attachments functionality on the data. When attachments are enabled on a feature class, an attachment table and relationship class are created to store the attachment data when an attachment is added to a feature. The attachment
table that is created includes fields that are used to store information about the attachment.

        params: {"in_dataset": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Upgrade_Attachments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Upgrade Attachments
            arcpy.UpgradeAttachments(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_attribute_rule(self, params):
        """Add Attribute Rule

Adds an attribute rule to a dataset. Attribute rules are user-defined rules that can be added to a dataset to enhance the editing experience and help enforce data integrity. These rules can be used to populate attribute values or constrain permissible feature configurations and are enforced during feature editing. If a rule is violated when editing a feature, an error message will be returned. Learn more about attribute rules Learn about the ArcGIS Arcade scripting language

        params: {"in_table": <Table View>, "name": <String>, "type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Add_Attribute_Rule"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Attribute Rule
            arcpy.AddAttributeRule(in_table, name, type, script_expression, is_editable, triggering_events, error_number, error_message, description, subtype, field, exclude_from_client_evaluation, batch, severity, tags, triggering_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_attribute_rule(self, params):
        """Alter Attribute Rule

Alters the properties of an attribute rule.

        params: {"in_table": <Table View>, "name": <String>, "description": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Alter_Attribute_Rule"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Alter Attribute Rule
            arcpy.AlterAttributeRule(in_table, name, description, error_number, error_message, tags, triggering_events, script_expression, exclude_from_client_evaluation, triggering_fields, subtype)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_attribute_rule(self, params):
        """Delete Attribute Rule

Deletes one or more attribute rules from a dataset. Learn more about attribute rules

        params: {"in_table": <Table View>, "names": <String>, "type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        names = params.get("names")
        if names is None:
            return {"success": False, "error": "names parameter is required"}
        type = params.get("type")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Delete_Attribute_Rule"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Attribute Rule
            arcpy.DeleteAttributeRule(in_table, names, type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_attribute_rules(self, params):
        """Disable Attribute Rules

Disables one or more attribute rules for a dataset.

        params: {"in_table": <Table View>, "names": <String>, "type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        names = params.get("names")
        if names is None:
            return {"success": False, "error": "names parameter is required"}
        type = params.get("type")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Disable_Attribute_Rules"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disable Attribute Rules
            arcpy.DisableAttributeRules(in_table, names, type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_attribute_rules(self, params):
        """Enable Attribute Rules

Enables one or more attribute rules in a dataset

        params: {"in_table": <Table View>, "names": <String>, "type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        names = params.get("names")
        if names is None:
            return {"success": False, "error": "names parameter is required"}
        type = params.get("type")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Enable_Attribute_Rules"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Attribute Rules
            arcpy.EnableAttributeRules(in_table, names, type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def evaluate_rules(self, params):
        """Evaluate Rules

Evaluates geodatabase rules and functionality. Learn more about evaluating attribute rules

        params: {"in_workspace": <Workspace>, "evaluation_types": <String>, "extent": <Extent>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Evaluate_Rules"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Evaluate Rules
            arcpy.EvaluateRules(in_workspace, evaluation_types, extent, run_async)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_attribute_rules(self, params):
        """Export Attribute Rules

Exports attribute rules from a dataset to a comma-separated values file (.csv).

        params: {"in_table": <Table View>, "out_csv_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_csv_file = params.get("out_csv_file")
        if out_csv_file is None:
            return {"success": False, "error": "out_csv_file parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Export_Attribute_Rules"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Attribute Rules
            arcpy.ExportAttributeRules(in_table, out_csv_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_attribute_rules(self, params):
        """Import Attribute Rules

Imports attribute rules from  comma-separated value files (.csv) to a dataset.

        params: {"target_table": <Table View>, "csv_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        target_table = params.get("target_table")
        if target_table is None:
            return {"success": False, "error": "target_table parameter is required"}
        csv_file = params.get("csv_file")
        if csv_file is None:
            return {"success": False, "error": "csv_file parameter is required"}

            # Generate output name and path
            output_name = f"{target_table.replace(' ', '_')}_Import_Attribute_Rules"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import Attribute Rules
            arcpy.ImportAttributeRules(target_table, csv_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def reorder_attribute_rule(self, params):
        """Reorder Attribute Rule

Reorders the evaluation order of an attribute rule. The evaluation order controls the sequence in which rules are evaluated. The evaluation order is important when there are dependencies on calculated fields, since the result may be impacted if the rules are in a different order. Learn more about attribute rule evaluation order

        params: {"in_table": <Table View>, "name": <String>, "evaluation_order": <Long>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Reorder_Attribute_Rule"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Reorder Attribute Rule
            arcpy.ReorderAttributeRule(in_table, name, evaluation_order)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_items_to_catalog_dataset(self, params):
        """Add Items To Catalog Dataset

Adds workspace items and layers—such as geodatabase datasets, raster layers, feature layers, mosaic layers, and other items—to an existing catalog dataset.

        params: {"target_catalog_dataset": <Catalog Layer>, "input_items": <Workspace; Feature Layer; Image Service; Raster Layer; Mosaic Layer; LAS Dataset Layer; Layer File; CAD Drawing Dataset; ServerConnection; BIM File Workspace; TIN Layer>, "input_item_types": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{target_catalog_dataset.replace(' ', '_')}_Add_Items_To_Catalog_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Items To Catalog Dataset
            arcpy.AddItemsToCatalogDataset(target_catalog_dataset, input_items, input_item_types, include_subfolders, footprint_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_portal_items_to_catalog_dataset(self, params):
        """Add Portal Items To Catalog Dataset

Adds ArcGIS Online or ArcGIS Enterprise portal service items—such as feature, map, image, scene, and tile services—to an existing catalog dataset.

        params: {"target_catalog_dataset": <Catalog Layer>, "input_portal_itemtypes": <String>, "content": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{target_catalog_dataset.replace(' ', '_')}_Add_Portal_Items_To_Catalog_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Portal Items To Catalog Dataset
            arcpy.AddPortalItemsToCatalogDataset(target_catalog_dataset, input_portal_itemtypes, content, portal_folders, portal_groups, access_level)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_catalog_dataset(self, params):
        """Create Catalog Dataset

Creates a catalog dataset to which collections of layers, rasters, datasets, and other items can be added.

        params: {"out_path": <Workspace; Feature Dataset>, "out_name": <String>, "spatial_reference": <Spatial Reference>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Catalog_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Catalog Dataset
            arcpy.CreateCatalogDataset(out_path, out_name, spatial_reference, template, has_z, out_alias, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_feature_changes(self, params):
        """Detect Feature Changes

Finds where the update line features spatially match the base line features and detects spatial changes, attribute changes, or both, as well as no change. It then creates an output feature class containing matched update features with information about their changes, unmatched update features, and unmatched base features. Learn more about how feature matching works

        params: {"update_features": <Feature Layer>, "base_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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
        match_fieldssource_field_target_field = params.get("match_fieldssource_field_target_field")
        out_match_table = params.get("out_match_table")
        change_tolerance = params.get("change_tolerance")
        compare_fieldssource_field_target_field = params.get("compare_fieldssource_field_target_field")
        compare_line_direction = params.get("compare_line_direction")

            # Generate output name and path
            output_name = f"{update_features.replace(' ', '_')}_Detect_Feature_Changes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Feature Changes
            arcpy.DetectFeatureChanges(update_features, base_features, out_feature_class, search_distance, match_fieldssource_field_target_field, out_match_table, change_tolerance, compare_fieldssource_field_target_field, compare_line_direction)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_compare(self, params):
        """Feature Compare

Compares two feature classes or layers and returns the comparison results.

        params: {"in_base_features": <Feature Layer>, "in_test_features": <Feature Layer>, "sort_field": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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
        attribute_tolerancesfield_tolerance = params.get("attribute_tolerancesfield_tolerance")
        omit_field = params.get("omit_field")
        continue_compare = params.get("continue_compare")
        out_compare_file = params.get("out_compare_file")

            # Generate output name and path
            output_name = f"{in_base_features.replace(' ', '_')}_Feature_Compare"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Compare
            arcpy.FeatureCompare(in_base_features, in_test_features, sort_field, compare_type, ignore_options, xy_tolerance, m_tolerance, z_tolerance, attribute_tolerancesfield_tolerance, omit_field, continue_compare, out_compare_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def file_compare(self, params):
        """File Compare

Compares two files and returns the comparison results.

        params: {"in_base_file": <File>, "in_test_file": <File>, "file_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_base_file.replace(' ', '_')}_File_Compare"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute File Compare
            arcpy.FileCompare(in_base_file, in_test_file, file_type, continue_compare, out_compare_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_compare(self, params):
        """Raster Compare

Compares the properties of two raster datasets or two mosaic datasets.

        params: {"in_base_raster": <Raster Layer; Mosaic Layer>, "in_test_raster": <Raster Layer; Mosaic Layer>, "compare_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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
        parameter_tolerancesparameter_tolerance_type = params.get("parameter_tolerancesparameter_tolerance_type")
        attribute_tolerancesfield_tolerance = params.get("attribute_tolerancesfield_tolerance")
        omit_field = params.get("omit_field")

            # Generate output name and path
            output_name = f"{in_base_raster.replace(' ', '_')}_Raster_Compare"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster Compare
            arcpy.RasterCompare(in_base_raster, in_test_raster, compare_type, ignore_option, continue_compare, out_compare_file, parameter_tolerancesparameter_tolerance_type, attribute_tolerancesfield_tolerance, omit_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_compare(self, params):
        """Table Compare

Compares two tables or table views and returns the comparison results.

        params: {"in_base_table": <Table View; Raster Layer>, "in_test_table": <Table View ; Raster Layer>, "sort_field": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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
        attribute_tolerancesfield_tolerance = params.get("attribute_tolerancesfield_tolerance")
        omit_field = params.get("omit_field")
        continue_compare = params.get("continue_compare")
        out_compare_file = params.get("out_compare_file")

            # Generate output name and path
            output_name = f"{in_base_table.replace(' ', '_')}_Table_Compare"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table Compare
            arcpy.TableCompare(in_base_table, in_test_table, sort_field, compare_type, ignore_options, attribute_tolerancesfield_tolerance, omit_field, continue_compare, out_compare_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tin_compare(self, params):
        """TIN Compare

Compares two TINs and returns the comparison results.

        params: {"in_base_tin": <TIN Layer>, "in_test_tin": <TIN Layer>, "compare_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_base_tin.replace(' ', '_')}_TIN_Compare"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute TIN Compare
            arcpy.TINCompare(in_base_tin, in_test_tin, compare_type, continue_compare, out_compare_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_data_loading_workspace(self, params):
        """Create Data Loading Workspace

Creates a data loading workspace that can be used for data loading. The output workspace contains a collection of Microsoft Excel workbooks. These workbooks can be used to configure the source and target schema mapping. Learn more about data loading workspace concepts

        params: {"source_target_mapping": <Value Table>, "out_folder": <Folder>, "match_options": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        source_target_mapping = params.get("source_target_mapping")
        if source_target_mapping is None:
            return {"success": False, "error": "source_target_mapping parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        match_options = params.get("match_options")
        mapping_table = params.get("mapping_table")
        calc_stats = params.get("calc_stats")
        match_subtypes = params.get("match_subtypes")

            # Generate output name and path
            output_name = f"{source_target_mapping.replace(' ', '_')}_Create_Data_Loading_Workspace"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Data Loading Workspace
            arcpy.CreateDataLoadingWorkspace(source_target_mapping, out_folder, match_options, mapping_table, calc_stats, match_subtypes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_mapping_table(self, params):
        """Generate Mapping Table

Generates the Mapping Table based on a configured data loading workspace. The table includes a list of  predefined datasets, fields, and attribute domain coded value descriptions.
This output table is used as input to the Create Data Loading Workspace tool.

        params: {"in_workbook": <File>, "out_table": <Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workbook = params.get("in_workbook")
        if in_workbook is None:
            return {"success": False, "error": "in_workbook parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_workbook.replace(' ', '_')}_Generate_Mapping_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Mapping Table
            arcpy.GenerateMappingTable(in_workbook, out_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def load_data_to_preview(self, params):
        """Load Data To Preview

Uses a Data Loading Workspace to load data from a source to a preview geodatabase. Use this tool to preview the results before loading data to the target schema.

        params: {"in_workbook": <File>, "out_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workbook = params.get("in_workbook")
        if in_workbook is None:
            return {"success": False, "error": "in_workbook parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}

            # Generate output name and path
            output_name = f"{in_workbook.replace(' ', '_')}_Load_Data_To_Preview"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Load Data To Preview
            arcpy.LoadDataToPreview(in_workbook, out_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def load_data_using_workspace(self, params):
        """Load Data Using Workspace

Uses the Data Reference Workbook from the Data Loading Workspace to load data from a source to a target dataset.

        params: {"in_workbook": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workbook = params.get("in_workbook")
        if in_workbook is None:
            return {"success": False, "error": "in_workbook parameter is required"}

            # Generate output name and path
            output_name = f"{in_workbook.replace(' ', '_')}_Load_Data_Using_Workspace"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Load Data Using Workspace
            arcpy.LoadDataUsingWorkspace(in_workbook)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_data_loading_workspace_schema(self, params):
        """Update Data Loading Workspace Schema

Creates a copy of the  Data Loading Workspace and updates all the mapping and domain workbooks.

        params: {"in_workbook": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workbook = params.get("in_workbook")
        if in_workbook is None:
            return {"success": False, "error": "in_workbook parameter is required"}

            # Generate output name and path
            output_name = f"{in_workbook.replace(' ', '_')}_Update_Data_Loading_Workspace_Schema"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Data Loading Workspace Schema
            arcpy.UpdateDataLoadingWorkspaceSchema(in_workbook)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compare_replica_schema(self, params):
        """Compare Replica Schema

Generates an .xml file that describes schema differences between a replica geodatabase and the relative replica geodatabase.

        params: {"in_geodatabase": <Workspace; GeoDataServer>, "in_source_file": <File>, "output_replica_schema_changes_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        in_source_file = params.get("in_source_file")
        if in_source_file is None:
            return {"success": False, "error": "in_source_file parameter is required"}
        output_replica_schema_changes_file = params.get("output_replica_schema_changes_file")
        if output_replica_schema_changes_file is None:
            return {"success": False, "error": "output_replica_schema_changes_file parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Compare_Replica_Schema"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compare Replica Schema
            arcpy.CompareReplicaSchema(in_geodatabase, in_source_file, output_replica_schema_changes_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_replica(self, params):
        """Create Replica

Creates a replica in a geodatabase from a specified list of feature classes, layers, datasets, and tables in an enterprise geodatabase.

        params: {"in_data": <Table View; Dataset>, "in_type": <String>, "out_geodatabase": <Workspace; GeoDataServer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        in_type = params.get("in_type")
        if in_type is None:
            return {"success": False, "error": "in_type parameter is required"}
        out_geodatabase = params.get("out_geodatabase")
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        access_type = params.get("access_type")
        initial_data_sender = params.get("initial_data_sender")
        expand_feature_classes_and_tables = params.get("expand_feature_classes_and_tables")
        reuse_schema = params.get("reuse_schema")
        get_related_data = params.get("get_related_data")
        geometry_features = params.get("geometry_features")
        archiving = params.get("archiving")
        register_existing_data = params.get("register_existing_data")
        out_type = params.get("out_type")
        out_xml = params.get("out_xml")
        all_records_for_tables = params.get("all_records_for_tables")
        out_filegdb_folder_path = params.get("out_filegdb_folder_path")
        out_filegdb_name = params.get("out_filegdb_name")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Create_Replica"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Replica
            arcpy.CreateReplica(in_data, in_type, out_geodatabase, out_name, access_type, initial_data_sender, expand_feature_classes_and_tables, reuse_schema, get_related_data, geometry_features, archiving, register_existing_data, out_type, out_xml, all_records_for_tables, out_filegdb_folder_path, out_filegdb_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_replica_from_server(self, params):
        """Create Replica From Server

Creates a replica using a specified list of feature classes, layers, feature datasets, and tables from a remote geodatabase using a geodata service published on ArcGIS Server.

        params: {"in_geodataservice": <GeoDataServer>, "datasetsdataset_name": <String>, "in_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodataservice = params.get("in_geodataservice")
        if in_geodataservice is None:
            return {"success": False, "error": "in_geodataservice parameter is required"}
        datasetsdataset_name = params.get("datasetsdataset_name")
        if datasetsdataset_name is None:
            return {"success": False, "error": "datasetsdataset_name parameter is required"}
        in_type = params.get("in_type")
        if in_type is None:
            return {"success": False, "error": "in_type parameter is required"}
        out_geodatabase = params.get("out_geodatabase")
        if out_geodatabase is None:
            return {"success": False, "error": "out_geodatabase parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        access_type = params.get("access_type")
        initial_data_sender = params.get("initial_data_sender")
        expand_feature_classes_and_tables = params.get("expand_feature_classes_and_tables")
        reuse_schema = params.get("reuse_schema")
        get_related_data = params.get("get_related_data")
        geometry_features = params.get("geometry_features")
        archiving = params.get("archiving")
        all_records_for_tables = params.get("all_records_for_tables")

            # Generate output name and path
            output_name = f"{in_geodataservice.replace(' ', '_')}_Create_Replica_From_Server"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Replica From Server
            arcpy.CreateReplicaFromServer(in_geodataservice, datasetsdataset_name, in_type, out_geodatabase, out_name, access_type, initial_data_sender, expand_feature_classes_and_tables, reuse_schema, get_related_data, geometry_features, archiving, all_records_for_tables)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_replica_tracking(self, params):
        """Disable Replica Tracking

Disables replica tracking on data. Replica tracking is automatically disabled when a versioned dataset is unregistered as versioned or a nonversioned dataset has archiving disabled.

        params: {"in_dataset": <Table; Feature Class; Feature Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Disable_Replica_Tracking"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disable Replica Tracking
            arcpy.DisableReplicaTracking(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_replica_tracking(self, params):
        """Enable Replica Tracking

Enables replica tracking on data, allowing you to work with  offline maps and in distributed collaborations. Replica tracking applies to services that are configured with the sync capability with the option of creating a version for each downloaded map. To disable replica tracking on data, use the Disable Replica Tracking tool. Learn more about preparing data for offline use

        params: {"in_dataset": <Table; Feature Class; Feature Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Enable_Replica_Tracking"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Replica Tracking
            arcpy.EnableReplicaTracking(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_acknowledgement_message(self, params):
        """Export Acknowledgement Message

Creates an output acknowledgement file to acknowledge the reception of previously received data change messages.

        params: {"in_geodatabase": <Workspace ; GeoDataServer>, "out_acknowledgement_file": <File>, "in_replica": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        out_acknowledgement_file = params.get("out_acknowledgement_file")
        if out_acknowledgement_file is None:
            return {"success": False, "error": "out_acknowledgement_file parameter is required"}
        in_replica = params.get("in_replica")
        if in_replica is None:
            return {"success": False, "error": "in_replica parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Export_Acknowledgement_Message"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Acknowledgement Message
            arcpy.ExportAcknowledgementMessage(in_geodatabase, out_acknowledgement_file, in_replica)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_data_change_message(self, params):
        """Export Data Change Message

Creates an output delta file containing updates from an input replica.

        params: {"in_geodatabase": <Workspace;GeoDataServer>, "out_data_changes_file": <File>, "in_replica": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        out_data_changes_file = params.get("out_data_changes_file")
        if out_data_changes_file is None:
            return {"success": False, "error": "out_data_changes_file parameter is required"}
        in_replica = params.get("in_replica")
        if in_replica is None:
            return {"success": False, "error": "in_replica parameter is required"}
        switch_to_receiver = params.get("switch_to_receiver")
        if switch_to_receiver is None:
            return {"success": False, "error": "switch_to_receiver parameter is required"}
        include_unacknowledged_changes = params.get("include_unacknowledged_changes")
        if include_unacknowledged_changes is None:
            return {"success": False, "error": "include_unacknowledged_changes parameter is required"}
        include_new_changes = params.get("include_new_changes")
        if include_new_changes is None:
            return {"success": False, "error": "include_new_changes parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Export_Data_Change_Message"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Data Change Message
            arcpy.ExportDataChangeMessage(in_geodatabase, out_data_changes_file, in_replica, switch_to_receiver, include_unacknowledged_changes, include_new_changes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_replica_schema(self, params):
        """Export Replica Schema

Creates a replica schema file with the schema of an input one- or two-way replica.

        params: {"in_geodatabase": <Workspace; GeoDataServer>, "output_replica_schema_file": <File>, "in_replica": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        output_replica_schema_file = params.get("output_replica_schema_file")
        if output_replica_schema_file is None:
            return {"success": False, "error": "output_replica_schema_file parameter is required"}
        in_replica = params.get("in_replica")
        if in_replica is None:
            return {"success": False, "error": "in_replica parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Export_Replica_Schema"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Replica Schema
            arcpy.ExportReplicaSchema(in_geodatabase, output_replica_schema_file, in_replica)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_message(self, params):
        """Import Message

Imports changes from a delta file into a replica geodatabase or imports an acknowledgment message into a replica geodatabase.

        params: {"in_geodatabase": <Workspace; GeoDataServer>, "source_delta_file": <Workspace ; File>, "output_acknowledgement_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        source_delta_file = params.get("source_delta_file")
        if source_delta_file is None:
            return {"success": False, "error": "source_delta_file parameter is required"}
        output_acknowledgement_file = params.get("output_acknowledgement_file")
        conflict_policy = params.get("conflict_policy")
        conflict_definition = params.get("conflict_definition")

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Import_Message"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import Message
            arcpy.ImportMessage(in_geodatabase, source_delta_file, output_acknowledgement_file, conflict_policy, conflict_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_replica_schema(self, params):
        """Import Replica Schema

Applies replica schema differences using an input replica geodatabase and an XML schema file.

        params: {"in_geodatabase": <Workspace; GeoDataServer>, "in_source": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        in_source = params.get("in_source")
        if in_source is None:
            return {"success": False, "error": "in_source parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Import_Replica_Schema"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import Replica Schema
            arcpy.ImportReplicaSchema(in_geodatabase, in_source)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def re_export_unacknowledged_messages(self, params):
        """Re-export Unacknowledged Messages

Creates an output delta file containing unacknowledged replica updates from a one-way or two-way replica geodatabase.

        params: {"in_geodatabase": <Workspace; GeoDataServer>, "output_delta_file": <File>, "in_replica": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        output_delta_file = params.get("output_delta_file")
        if output_delta_file is None:
            return {"success": False, "error": "output_delta_file parameter is required"}
        in_replica = params.get("in_replica")
        if in_replica is None:
            return {"success": False, "error": "in_replica parameter is required"}
        in_export_option = params.get("in_export_option")
        if in_export_option is None:
            return {"success": False, "error": "in_export_option parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Re-export_Unacknowledged_Messages"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Re-export Unacknowledged Messages
            arcpy.ReexportUnacknowledgedMessages(in_geodatabase, output_delta_file, in_replica, in_export_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def synchronize_changes(self, params):
        """Synchronize Changes

Synchronizes updates between two replica geodatabases in a specified direction.

        params: {"geodatabase_1": <Workspace; GeoDataServer>, "in_replica": <String>, "geodatabase_2": <Workspace; GeoDataServer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        geodatabase_1 = params.get("geodatabase_1")
        if geodatabase_1 is None:
            return {"success": False, "error": "geodatabase_1 parameter is required"}
        in_replica = params.get("in_replica")
        if in_replica is None:
            return {"success": False, "error": "in_replica parameter is required"}
        geodatabase_2 = params.get("geodatabase_2")
        if geodatabase_2 is None:
            return {"success": False, "error": "geodatabase_2 parameter is required"}
        in_direction = params.get("in_direction")
        if in_direction is None:
            return {"success": False, "error": "in_direction parameter is required"}
        conflict_policy = params.get("conflict_policy")
        if conflict_policy is None:
            return {"success": False, "error": "conflict_policy parameter is required"}
        conflict_definition = params.get("conflict_definition")
        if conflict_definition is None:
            return {"success": False, "error": "conflict_definition parameter is required"}
        reconcile = params.get("reconcile")
        if reconcile is None:
            return {"success": False, "error": "reconcile parameter is required"}

            # Generate output name and path
            output_name = f"{geodatabase_1.replace(' ', '_')}_Synchronize_Changes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Synchronize Changes
            arcpy.SynchronizeChanges(geodatabase_1, in_replica, geodatabase_2, in_direction, conflict_policy, conflict_definition, reconcile)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def unregister_replica(self, params):
        """Unregister Replica

Unregisters a replica from an enterprise geodatabase.

        params: {"in_geodatabase": <Workspace>, "in_replica": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geodatabase = params.get("in_geodatabase")
        if in_geodatabase is None:
            return {"success": False, "error": "in_geodatabase parameter is required"}
        in_replica = params.get("in_replica")
        if in_replica is None:
            return {"success": False, "error": "in_replica parameter is required"}

            # Generate output name and path
            output_name = f"{in_geodatabase.replace(' ', '_')}_Unregister_Replica"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Unregister Replica
            arcpy.UnregisterReplica(in_geodatabase, in_replica)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_coded_value_to_domain(self, params):
        """Add Coded Value To Domain

Adds a value to a domain's coded value list.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "code": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        code = params.get("code")
        if code is None:
            return {"success": False, "error": "code parameter is required"}
        code_description = params.get("code_description")
        if code_description is None:
            return {"success": False, "error": "code_description parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Add_Coded_Value_To_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Coded Value To Domain
            arcpy.AddCodedValueToDomain(in_workspace, domain_name, code, code_description)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_domain(self, params):
        """Alter Domain

Alters the properties of an existing attribute domain in a workspace.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "new_domain_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        new_domain_name = params.get("new_domain_name")
        new_domain_description = params.get("new_domain_description")
        split_policy = params.get("split_policy")
        merge_policy = params.get("merge_policy")
        new_domain_owner = params.get("new_domain_owner")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Alter_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Alter Domain
            arcpy.AlterDomain(in_workspace, domain_name, new_domain_name, new_domain_description, split_policy, merge_policy, new_domain_owner)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def assign_domain_to_field(self, params):
        """Assign Domain To Field

Sets the domain for a particular field and, optionally, for a subtype. If no subtype is specified, the domain is only assigned to the specified field.

        params: {"in_table": <Table View>, "field_name": <Field>, "domain_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field_name = params.get("field_name")
        if field_name is None:
            return {"success": False, "error": "field_name parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        subtype_code = params.get("subtype_code")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Assign_Domain_To_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Assign Domain To Field
            arcpy.AssignDomainToField(in_table, field_name, domain_name, subtype_code)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_domain(self, params):
        """Create Domain

Creates an attribute domain in the specified workspace.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "domain_description": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        domain_description = params.get("domain_description")
        field_type = params.get("field_type")
        domain_type = params.get("domain_type")
        split_policy = params.get("split_policy")
        merge_policy = params.get("merge_policy")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Create_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Domain
            arcpy.CreateDomain(in_workspace, domain_name, domain_description, field_type, domain_type, split_policy, merge_policy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_coded_value_from_domain(self, params):
        """Delete Coded Value From Domain

Removes a value from a coded value domain.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "code": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        code = params.get("code")
        if code is None:
            return {"success": False, "error": "code parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Delete_Coded_Value_From_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Coded Value From Domain
            arcpy.DeleteCodedValueFromDomain(in_workspace, domain_name, code)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_domain(self, params):
        """Delete Domain

Deletes a domain from a workspace.

        params: {"in_workspace": <Workspace>, "domain_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Delete_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Domain
            arcpy.DeleteDomain(in_workspace, domain_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def domain_to_table(self, params):
        """Domain To Table

Creates a table from an attribute domain.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "out_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        code_field = params.get("code_field")
        if code_field is None:
            return {"success": False, "error": "code_field parameter is required"}
        description_field = params.get("description_field")
        if description_field is None:
            return {"success": False, "error": "description_field parameter is required"}
        configuration_keyword = params.get("configuration_keyword")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Domain_To_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Domain To Table
            arcpy.DomainToTable(in_workspace, domain_name, out_table, code_field, description_field, configuration_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_domain_from_field(self, params):
        """Remove Domain From Field

Removes an attribute domain association from a feature class or table field.

        params: {"in_table": <Table View>, "field_name": <Field>, "subtype_code": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field_name = params.get("field_name")
        if field_name is None:
            return {"success": False, "error": "field_name parameter is required"}
        subtype_code = params.get("subtype_code")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Remove_Domain_From_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Domain From Field
            arcpy.RemoveDomainFromField(in_table, field_name, subtype_code)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_value_for_range_domain(self, params):
        """Set Value For Range Domain

Sets the minimum and maximum values for an existing Range domain.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "min_value": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        min_value = params.get("min_value")
        if min_value is None:
            return {"success": False, "error": "min_value parameter is required"}
        max_value = params.get("max_value")
        if max_value is None:
            return {"success": False, "error": "max_value parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Set_Value_For_Range_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Value For Range Domain
            arcpy.SetValueForRangeDomain(in_workspace, domain_name, min_value, max_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sort_coded_value_domain(self, params):
        """Sort Coded Value Domain

Sorts the code or description of a coded value domain in either ascending or descending order.

        params: {"in_workspace": <Workspace>, "domain_name": <String>, "sort_by": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        sort_by = params.get("sort_by")
        if sort_by is None:
            return {"success": False, "error": "sort_by parameter is required"}
        sort_order = params.get("sort_order")
        if sort_order is None:
            return {"success": False, "error": "sort_order parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Sort_Coded_Value_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sort Coded Value Domain
            arcpy.SortCodedValueDomain(in_workspace, domain_name, sort_by, sort_order)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_domain(self, params):
        """Table To Domain

Creates or updates a coded value domain with values from a table.

        params: {"in_table": <Table View>, "code_field": <Field>, "description_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        code_field = params.get("code_field")
        if code_field is None:
            return {"success": False, "error": "code_field parameter is required"}
        description_field = params.get("description_field")
        if description_field is None:
            return {"success": False, "error": "description_field parameter is required"}
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        domain_name = params.get("domain_name")
        if domain_name is None:
            return {"success": False, "error": "domain_name parameter is required"}
        domain_description = params.get("domain_description")
        update_option = params.get("update_option")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Table_To_Domain"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To Domain
            arcpy.TableToDomain(in_table, code_field, description_field, in_workspace, domain_name, domain_description, update_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_feature_binning(self, params):
        """Disable Feature Binning

Disables database computed feature binning on a feature class.

        params: {"in_features": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Disable_Feature_Binning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disable Feature Binning
            arcpy.DisableFeatureBinning(in_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_feature_binning(self, params):
        """Enable Feature Binning

Enables database computation for feature binning on a point feature class. Feature binning is an advanced visualization capability that allows you to explore and visualize large datasets. It also helps you observe patterns at macro and micro levels with out-of-the-box mapping options. Feature binning aggregates large amounts of features into dynamic polygon bins that vary through scaled levels of detail. A single bin represents all features within its boundaries at that level of detail. Feature binning can improve both drawing performance and data comprehension. Learn more about binned feature layers

        params: {"in_features": <Feature Layer>, "bin_type": <String>, "bin_coord_sys": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        bin_type = params.get("bin_type")
        bin_coord_sys = params.get("bin_coord_sys")
        summary_statsfield_statistic_type = params.get("summary_statsfield_statistic_type")
        generate_static_cache = params.get("generate_static_cache")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Enable_Feature_Binning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Feature Binning
            arcpy.EnableFeatureBinning(in_features, bin_type, bin_coord_sys, summary_statsfield_statistic_type, generate_static_cache)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def manage_feature_bin_cache(self, params):
        """Manage Feature Bin Cache

Manages the feature binning cache for data that has database computed feature binning enabled. Feature binning aggregates large amounts of features into dynamic polygon bins that vary through scaled levels of detail. Learn how to enable database computed feature binning and work with binned feature layers.

        params: {"in_features": <Feature Layer>, "bin_type": <String>, "max_lod": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        bin_type = params.get("bin_type")
        max_lod = params.get("max_lod")
        add_cache_statisticsfield_statistic_type = params.get("add_cache_statisticsfield_statistic_type")
        delete_cache_statistics = params.get("delete_cache_statistics")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Manage_Feature_Bin_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Manage Feature Bin Cache
            arcpy.ManageFeatureBinCache(in_features, bin_type, max_lod, add_cache_statisticsfield_statistic_type, delete_cache_statistics)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def append_annotation_feature_classes(self, params):
        """Append Annotation Feature Classes

Creates a geodatabase annotation feature class or appends to an existing annotation feature class by combining annotation from multiple input geodatabase annotation feature classes into a single feature class with annotation classes.

        params: {"input_features": <Feature Layer>, "output_featureclass": <Feature Class>, "reference_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_featureclass = params.get("output_featureclass")
        if output_featureclass is None:
            return {"success": False, "error": "output_featureclass parameter is required"}
        reference_scale = params.get("reference_scale")
        if reference_scale is None:
            return {"success": False, "error": "reference_scale parameter is required"}
        create_single_class = params.get("create_single_class")
        require_symbol_from_table = params.get("require_symbol_from_table")
        create_annotation_when_feature_added = params.get("create_annotation_when_feature_added")
        update_annotation_when_feature_modified = params.get("update_annotation_when_feature_modified")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Append_Annotation_Feature_Classes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Append Annotation Feature Classes
            arcpy.AppendAnnotationFeatureClasses(input_features, output_featureclass, reference_scale, create_single_class, require_symbol_from_table, create_annotation_when_feature_added, update_annotation_when_feature_modified)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_feature_class(self, params):
        """Create Feature Class

Creates an empty feature class in a geodatabase or a shapefile in a folder.

        params: {"out_path": <Workspace; Feature Dataset>, "out_name": <String>, "geometry_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        geometry_type = params.get("geometry_type")
        template = params.get("template")
        has_m = params.get("has_m")
        has_z = params.get("has_z")
        spatial_reference = params.get("spatial_reference")
        config_keyword = params.get("config_keyword")
        spatial_grid_1 = params.get("spatial_grid_1")
        spatial_grid_2 = params.get("spatial_grid_2")
        spatial_grid_3 = params.get("spatial_grid_3")
        out_alias = params.get("out_alias")
        oid_type = params.get("oid_type")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Feature Class
            arcpy.CreateFeatureClass(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3, out_alias, oid_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_unregistered_feature_class(self, params):
        """Create Unregistered Feature Class

Creates an empty feature class in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The feature class is not registered with the geodatabase.

        params: {"out_path": <Workspace; Feature Dataset>, "out_name": <String>, "geometry_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        geometry_type = params.get("geometry_type")
        template = params.get("template")
        has_m = params.get("has_m")
        has_z = params.get("has_z")
        spatial_reference = params.get("spatial_reference")
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Unregistered_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Unregistered Feature Class
            arcpy.CreateUnregisteredFeatureClass(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def integrate(self, params):
        """Integrate

Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect. Integrate performs
the following processing tasks: Vertices within the x,y tolerance of one another will be assigned the same coordinate location.When a vertex of one feature is within the x,y tolerance of an edge of any other feature, a new vertex will be inserted on the edge.When line segments intersect, a vertex will be inserted at the point of intersection for each feature involved in the intersection. An alternate tool is available for vector data integration. See the Pairwise Integrate documentation for details.

        params: {"in_featuresfeature_layer_long": <Value Table>, "cluster_tolerance": <Linear Unit>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_featuresfeature_layer_long = params.get("in_featuresfeature_layer_long")
        if in_featuresfeature_layer_long is None:
            return {"success": False, "error": "in_featuresfeature_layer_long parameter is required"}
        cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_featuresfeature_layer_long.replace(' ', '_')}_Integrate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Integrate
            arcpy.Integrate(in_featuresfeature_layer_long, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def recalculate_feature_class_extent(self, params):
        """Recalculate Feature Class Extent

Recalculates the xy, z, and m extent properties of a feature class based on the features in the feature class. A feature class has a spatial extent that is based on all the coordinates in the feature class. This spatial extent is used when adding a feature class to a map to recenter and display all the features. Rather than examining every feature in the feature class each time the feature class is added to a map (a potentially long process), a feature class has an extent property containing the last known spatial extent. However, this extent property is not always updated when features in the feature class are edited. This means that the values in the extent property may not contain the actual spatial extent of the features. The Recalculate Feature Class Extent tool reads all the features and updates the extent property. XY, Z, and M extents are not the same as spatial reference domains. The XY, Z, and M domains in a spatial reference define the valid range of coordinate values that can be stored in a feature class. The feature class extents reflect the actual range of coordinate values that exist in the feature class. These extents cannot be larger than the domains.

        params: {"in_features": <Feature Layer>, "store_extent": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        store_extent = params.get("store_extent")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Recalculate_Feature_Class_Extent"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Recalculate Feature Class Extent
            arcpy.RecalculateFeatureClassExtent(in_features, store_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_feature_class_split_model(self, params):
        """Set Feature Class Split Model

Defines the behavior of a split operation on a feature class. Learn more about setting the split model for a feature class

        params: {"in_feature_class": <Feature Layer>, "split_model": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        split_model = params.get("split_model")

            # Generate output name and path
            output_name = f"{in_feature_class.replace(' ', '_')}_Set_Feature_Class_Split_Model"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Feature Class Split Model
            arcpy.SetFeatureClassSplitModel(in_feature_class, split_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_xy_coordinates(self, params):
        """Add XY Coordinates

Adds the fields POINT_X and POINT_Y to the point input features and calculates their values. The tool also appends the POINT_Z and POINT_M fields if the input features are z- and m-enabled.

        params: {"in_features": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Add_XY_Coordinates"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add XY Coordinates
            arcpy.AddXYCoordinates(in_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def adjust_3d_z(self, params):
        """Adjust 3D Z

Modifies z-values of 3D features.

        params: {"in_features": <Feature Layer>, "reverse_sign": <String>, "adjust_value": <Double; Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        reverse_sign = params.get("reverse_sign")
        adjust_value = params.get("adjust_value")
        from_units = params.get("from_units")
        to_units = params.get("to_units")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Adjust_3D_Z"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Adjust 3D Z
            arcpy.Adjust3DZ(in_features, reverse_sign, adjust_value, from_units, to_units)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bearing_distance_to_line(self, params):
        """Bearing Distance To Line

Creates a feature class containing geodetic or planar line features from the values in an x-coordinate field, y-coordinate field, bearing field, and distance field of a table.

        params: {"in_table": <Table View>, "out_featureclass": <Feature Class>, "x_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        x_field = params.get("x_field")
        if x_field is None:
            return {"success": False, "error": "x_field parameter is required"}
        y_field = params.get("y_field")
        if y_field is None:
            return {"success": False, "error": "y_field parameter is required"}
        distance_field = params.get("distance_field")
        if distance_field is None:
            return {"success": False, "error": "distance_field parameter is required"}
        distance_units = params.get("distance_units")
        bearing_field = params.get("bearing_field")
        if bearing_field is None:
            return {"success": False, "error": "bearing_field parameter is required"}
        bearing_units = params.get("bearing_units")
        line_type = params.get("line_type")
        id_field = params.get("id_field")
        spatial_reference = params.get("spatial_reference")
        attributes = params.get("attributes")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Bearing_Distance_To_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bearing Distance To Line
            arcpy.BearingDistanceToLine(in_table, out_featureclass, x_field, y_field, distance_field, distance_units, bearing_field, bearing_units, line_type, id_field, spatial_reference, attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_geometry_attributes(self, params):
        """Calculate Geometry Attributes

Adds information to a feature's attribute fields representing the spatial or geometric characteristics and location of each feature, such as length or area and x-, y-, z-coordinates, and m-values.

        params: {"in_features": <Feature Layer>, "geometry_propertyfield_property": <Value Table>, "length_unit": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        geometry_propertyfield_property = params.get("geometry_propertyfield_property")
        if geometry_propertyfield_property is None:
            return {"success": False, "error": "geometry_propertyfield_property parameter is required"}
        length_unit = params.get("length_unit")
        area_unit = params.get("area_unit")
        coordinate_system = params.get("coordinate_system")
        coordinate_format = params.get("coordinate_format")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Geometry_Attributes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Geometry Attributes
            arcpy.CalculateGeometryAttributes(in_features, geometry_propertyfield_property, length_unit, area_unit, coordinate_system, coordinate_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def check_geometry(self, params):
        """Check Geometry

Generates a report of geometry problems in a feature class. For additional information regarding geometry problems, their impact on the software, and potential sources, see Tools for checking and repairing geometries.

        params: {"in_features": <Feature Layer>, "out_table": <Table>, "validation_method": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_table = params.get("out_table")
        validation_method = params.get("validation_method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Check_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Check Geometry
            arcpy.CheckGeometry(in_features, out_table, validation_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy_features(self, params):
        """Copy Features

Copies features from the input feature class or layer to a new feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "config_keyword": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        config_keyword = params.get("config_keyword")
        spatial_grid_1 = params.get("spatial_grid_1")
        spatial_grid_2 = params.get("spatial_grid_2")
        spatial_grid_3 = params.get("spatial_grid_3")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Copy_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy Features
            arcpy.CopyFeatures(in_features, out_feature_class, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_features(self, params):
        """Delete Features

Deletes all or the selected subset of features from the input. The deletion of all features or a subset of features depends on the following:If the input is a feature class, all features will be deleted.
If the input is a layer with no selection, all features will be deleted.
If the input is a layer with a selection, only the
selected features will be deleted.

        params: {"in_features": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Delete_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Features
            arcpy.DeleteFeatures(in_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def dice(self, params):
        """Dice

Subdivides a feature into smaller features based on a specified vertex limit. This tool is intended as a way to subdivide extremely large features that cause issues with drawing, analysis, editing, and/or performance but are difficult to split up with standard editing and geoprocessing tools. This tool should not be used in any cases other than those where tools are failing to complete successfully due to the size of features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "vertex_limit": <Long>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        vertex_limit = params.get("vertex_limit")
        if vertex_limit is None:
            return {"success": False, "error": "vertex_limit parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Dice"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Dice
            arcpy.Dice(in_features, out_feature_class, vertex_limit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_envelope_to_polygon(self, params):
        """Feature Envelope To Polygon

Creates a feature class containing polygons, each of which represents the envelope of an input feature.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "single_envelope": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        single_envelope = params.get("single_envelope")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_Envelope_To_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Envelope To Polygon
            arcpy.FeatureEnvelopeToPolygon(in_features, out_feature_class, single_envelope)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_to_line(self, params):
        """Feature To Line

Creates a feature class containing lines generated by converting polygon boundaries to lines, or splitting line, polygon, or both features at their intersections.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "cluster_tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        cluster_tolerance = params.get("cluster_tolerance")
        attributes = params.get("attributes")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_To_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature To Line
            arcpy.FeatureToLine(in_features, out_feature_class, cluster_tolerance, attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_to_point(self, params):
        """Feature To Point

Creates a feature class containing points generated from the centroids of the input features or placed within the input features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "point_location": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        point_location = params.get("point_location")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_To_Point"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature To Point
            arcpy.FeatureToPoint(in_features, out_feature_class, point_location)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_to_polygon(self, params):
        """Feature To Polygon

Creates a feature class containing polygons generated from areas enclosed by input line or polygon features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "cluster_tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        cluster_tolerance = params.get("cluster_tolerance")
        attributes = params.get("attributes")
        label_features = params.get("label_features")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_To_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature To Polygon
            arcpy.FeatureToPolygon(in_features, out_feature_class, cluster_tolerance, attributes, label_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_vertices_to_points(self, params):
        """Feature Vertices To Points

Creates a feature class containing points generated from specified vertices or locations of the input features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "point_location": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        point_location = params.get("point_location")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_Vertices_To_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Vertices To Points
            arcpy.FeatureVerticesToPoints(in_features, out_feature_class, point_location)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def geodetic_densify(self, params):
        """Geodetic Densify

Creates new features by replacing the segments of the input features with densified approximations of geodesic segments. The following types of geodesic segments can be constructed: geodesic, great elliptic, loxodrome, and normal section.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "geodetic_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        geodetic_type = params.get("geodetic_type")
        if geodetic_type is None:
            return {"success": False, "error": "geodetic_type parameter is required"}
        distance = params.get("distance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Geodetic_Densify"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Geodetic Densify
            arcpy.GeodeticDensify(in_features, out_feature_class, geodetic_type, distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def minimum_bounding_geometry(self, params):
        """Minimum Bounding Geometry

Creates a feature class containing polygons which represent a specified minimum bounding geometry enclosing each input feature or each group of input features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "geometry_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        geometry_type = params.get("geometry_type")
        group_option = params.get("group_option")
        group_field = params.get("group_field")
        mbg_fields_option = params.get("mbg_fields_option")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Minimum_Bounding_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Minimum Bounding Geometry
            arcpy.MinimumBoundingGeometry(in_features, out_feature_class, geometry_type, group_option, group_field, mbg_fields_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multipart_to_singlepart(self, params):
        """Multipart To Singlepart

Creates a feature class of singlepart features by separating multipart input features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Multipart_To_Singlepart"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multipart To Singlepart
            arcpy.MultipartToSinglepart(in_features, out_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def points_to_line(self, params):
        """Points To Line

Creates line features from points.

        params: {"input_features": <Feature Layer>, "output_feature_class": <Feature Class>, "line_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        line_field = params.get("line_field")
        sort_field = params.get("sort_field")
        close_line = params.get("close_line")
        line_construction_method = params.get("line_construction_method")
        attribute_source = params.get("attribute_source")
        transfer_fields = params.get("transfer_fields")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Points_To_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Points To Line
            arcpy.PointsToLine(input_features, output_feature_class, line_field, sort_field, close_line, line_construction_method, attribute_source, transfer_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def polygon_to_line(self, params):
        """Polygon To Line

Creates a line feature class converted from polygon boundaries. You can set the tool parameters so shared segments and their neighboring polygon feature IDs will be analyzed. Alternatively, you can set the tool parameters so an enclosed line feature will be created for each input polygon.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "neighbor_option": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        neighbor_option = params.get("neighbor_option")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Polygon_To_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Polygon To Line
            arcpy.PolygonToLine(in_features, out_feature_class, neighbor_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def repair_geometry(self, params):
        """Repair Geometry

Inspects features for geometry problems and repairs them. If a problem is found, a repair will be performed, and a one-line description will identify the feature, as well as the geometry problem that was repaired. This tool uses the same logic as the Check Geometry tool to repair geometry problems. Learn more about checking and repairing geometries

        params: {"in_features": <Feature Layer>, "delete_null": <Boolean>, "validation_method": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        delete_null = params.get("delete_null")
        validation_method = params.get("validation_method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Repair_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Repair Geometry
            arcpy.RepairGeometry(in_features, delete_null, validation_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def split_line_at_point(self, params):
        """Split Line At Point

Splits line features based on intersection or proximity to point features.

        params: {"in_features": <Feature Layer>, "point_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        point_features = params.get("point_features")
        if point_features is None:
            return {"success": False, "error": "point_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        search_radius = params.get("search_radius")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Split_Line_At_Point"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Split Line At Point
            arcpy.SplitLineAtPoint(in_features, point_features, out_feature_class, search_radius)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def split_line_at_vertices(self, params):
        """Split Line At Vertices

Creates a polyline feature class by splitting input lines or polygons at their vertices.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Split_Line_At_Vertices"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Split Line At Vertices
            arcpy.SplitLineAtVertices(in_features, out_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def subdivide_polygon(self, params):
        """Subdivide Polygon

Divides polygon features into a number of equal areas or parts.

        params: {"in_polygons": <Feature Layer>, "out_feature_class": <Feature Class>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_polygons = params.get("in_polygons")
        if in_polygons is None:
            return {"success": False, "error": "in_polygons parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        num_areas = params.get("num_areas")
        target_area = params.get("target_area")
        target_width = params.get("target_width")
        split_angle = params.get("split_angle")
        subdivision_type = params.get("subdivision_type")

            # Generate output name and path
            output_name = f"{in_polygons.replace(' ', '_')}_Subdivide_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Subdivide Polygon
            arcpy.SubdividePolygon(in_polygons, out_feature_class, method, num_areas, target_area, target_width, split_angle, subdivision_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_ellipse(self, params):
        """Table To Ellipse

Creates a feature class containing geodetic or planar ellipses from the values in an x-coordinate field, y-coordinate field, major axis and minor axis fields, and azimuth field of a table.

        params: {"in_table": <Table View>, "out_featureclass": <Feature Class>, "x_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        x_field = params.get("x_field")
        if x_field is None:
            return {"success": False, "error": "x_field parameter is required"}
        y_field = params.get("y_field")
        if y_field is None:
            return {"success": False, "error": "y_field parameter is required"}
        major_field = params.get("major_field")
        if major_field is None:
            return {"success": False, "error": "major_field parameter is required"}
        minor_field = params.get("minor_field")
        if minor_field is None:
            return {"success": False, "error": "minor_field parameter is required"}
        distance_units = params.get("distance_units")
        if distance_units is None:
            return {"success": False, "error": "distance_units parameter is required"}
        azimuth_field = params.get("azimuth_field")
        azimuth_units = params.get("azimuth_units")
        id_field = params.get("id_field")
        spatial_reference = params.get("spatial_reference")
        attributes = params.get("attributes")
        geometry_type = params.get("geometry_type")
        method = params.get("method")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Table_To_Ellipse"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To Ellipse
            arcpy.TableToEllipse(in_table, out_featureclass, x_field, y_field, major_field, minor_field, distance_units, azimuth_field, azimuth_units, id_field, spatial_reference, attributes, geometry_type, method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def unsplit_line(self, params):
        """Unsplit Line

Aggregates line features that have coincident endpoints and, optionally, common attribute values.

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
        concatenation_separator = params.get("concatenation_separator")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Unsplit_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Unsplit Line
            arcpy.UnsplitLine(in_features, out_feature_class, dissolve_field, statistics_fieldsfield_statistic_type, concatenation_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def xy_table_to_point(self, params):
        """XY Table To Point

Creates a point feature class based on x-, y-, and z-coordinates from a table.

        params: {"in_table": <Table View>, "out_feature_class": <Feature Class>, "x_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        x_field = params.get("x_field")
        if x_field is None:
            return {"success": False, "error": "x_field parameter is required"}
        y_field = params.get("y_field")
        if y_field is None:
            return {"success": False, "error": "y_field parameter is required"}
        z_field = params.get("z_field")
        coordinate_system = params.get("coordinate_system")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_XY_Table_To_Point"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute XY Table To Point
            arcpy.XYTableToPoint(in_table, out_feature_class, x_field, y_field, z_field, coordinate_system)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def xy_to_line(self, params):
        """XY To Line

Creates a feature class containing geodetic or planar line features from the values in a start x-coordinate field, start y-coordinate field, end x-coordinate field, and end y-coordinate field of a table.

        params: {"in_table": <Table View>, "out_featureclass": <Feature Class>, "startx_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        startx_field = params.get("startx_field")
        if startx_field is None:
            return {"success": False, "error": "startx_field parameter is required"}
        starty_field = params.get("starty_field")
        if starty_field is None:
            return {"success": False, "error": "starty_field parameter is required"}
        endx_field = params.get("endx_field")
        if endx_field is None:
            return {"success": False, "error": "endx_field parameter is required"}
        endy_field = params.get("endy_field")
        if endy_field is None:
            return {"success": False, "error": "endy_field parameter is required"}
        line_type = params.get("line_type")
        id_field = params.get("id_field")
        spatial_reference = params.get("spatial_reference")
        attributes = params.get("attributes")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_XY_To_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute XY To Line
            arcpy.XYToLine(in_table, out_featureclass, startx_field, starty_field, endx_field, endy_field, line_type, id_field, spatial_reference, attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_field(self, params):
        """Add Field

Adds a new field to a table or the table of a feature class or feature layer, as well as to rasters with attribute tables.

        params: {"in_table": <Mosaic Layer; Raster Layer; Table View>, "field_name": <String>, "field_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field_name = params.get("field_name")
        if field_name is None:
            return {"success": False, "error": "field_name parameter is required"}
        field_type = params.get("field_type")
        if field_type is None:
            return {"success": False, "error": "field_type parameter is required"}
        field_precision = params.get("field_precision")
        field_scale = params.get("field_scale")
        field_length = params.get("field_length")
        field_alias = params.get("field_alias")
        field_is_nullable = params.get("field_is_nullable")
        field_is_required = params.get("field_is_required")
        field_domain = params.get("field_domain")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Add_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Field
            arcpy.AddField(in_table, field_name, field_type, field_precision, field_scale, field_length, field_alias, field_is_nullable, field_is_required, field_domain)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_fields_(multiple)(self, params):
        """Add Fields (multiple)

Adds new fields to a table, feature class, or raster.

        params: {"in_table": <Table View; Raster Layer; Mosaic Layer>, "template": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        template = params.get("template")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Add_Fields_(multiple)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Fields (multiple)
            arcpy.AddFields(multiple)(in_table, template)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_field(self, params):
        """Alter Field

Renames fields and field aliases or alters field properties.

        params: {"in_table": <Table View; Raster Layer; Mosaic Layer>, "field": <Field>, "new_field_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field = params.get("field")
        if field is None:
            return {"success": False, "error": "field parameter is required"}
        new_field_name = params.get("new_field_name")
        new_field_alias = params.get("new_field_alias")
        field_type = params.get("field_type")
        field_length = params.get("field_length")
        field_is_nullable = params.get("field_is_nullable")
        clear_field_alias = params.get("clear_field_alias")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Alter_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Alter Field
            arcpy.AlterField(in_table, field, new_field_name, new_field_alias, field_type, field_length, field_is_nullable, clear_field_alias)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_fields(self, params):
        """Alter Fields

Alters the field properties of multiple fields in a feature class or table.

        params: {"in_table": <Table View; Raster Layer; Mosaic Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Alter_Fields"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Alter Fields
            arcpy.AlterFields(in_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def assign_default_to_field(self, params):
        """Assign Default To Field

Creates a default value for a specified field.  When a new row is added to the table or feature class, the specified field will be set to this default value.

        params: {"in_table": <Mosaic Layer; Raster Layer; Table View>, "field_name": <Field>, "default_value": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field_name = params.get("field_name")
        if field_name is None:
            return {"success": False, "error": "field_name parameter is required"}
        default_value = params.get("default_value")
        subtype_code = params.get("subtype_code")
        clear_value = params.get("clear_value")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Assign_Default_To_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Assign Default To Field
            arcpy.AssignDefaultToField(in_table, field_name, default_value, subtype_code, clear_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def batch_update_fields(self, params):
        """Batch Update Fields

Transforms fields in a table or feature class based on schema defined in the definition table and creates a new table or feature class. You can do the following using this tool: Add new fields.Update existing fields.Reorder fields.Change field types.Change field properties.Assign or update field aliases.Calculate field values based on existing fields using Python.Remove fields.

        params: {"in_table": <Table View>, "out_table": <Table>, "field_definition_table": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        field_definition_table = params.get("field_definition_table")
        if field_definition_table is None:
            return {"success": False, "error": "field_definition_table parameter is required"}
        script_file = params.get("script_file")
        output_field_name = params.get("output_field_name")
        source_field_name = params.get("source_field_name")
        output_field_type = params.get("output_field_type")
        output_field_decimals_or_length = params.get("output_field_decimals_or_length")
        output_field_alias = params.get("output_field_alias")
        output_field_script = params.get("output_field_script")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Batch_Update_Fields"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Batch Update Fields
            arcpy.BatchUpdateFields(in_table, out_table, field_definition_table, script_file, output_field_name, source_field_name, output_field_type, output_field_decimals_or_length, output_field_alias, output_field_script)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_field(self, params):
        """Calculate Field

Calculates the values of a field for a feature class, feature layer, or raster.

        params: {"in_table": <Mosaic Layer; Raster Layer; Table View>, "field": <Field>, "expression": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field = params.get("field")
        if field is None:
            return {"success": False, "error": "field parameter is required"}
        expression = params.get("expression")
        if expression is None:
            return {"success": False, "error": "expression parameter is required"}
        expression_type = params.get("expression_type")
        code_block = params.get("code_block")
        field_type = params.get("field_type")
        enforce_domains = params.get("enforce_domains")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Calculate_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Field
            arcpy.CalculateField(in_table, field, expression, expression_type, code_block, field_type, enforce_domains)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_fields_(multiple)(self, params):
        """Calculate Fields (multiple)

Calculates the values of two or more fields for a feature class, feature layer, or raster.

        params: {"in_table": <Table View; Raster Layer; Mosaic Layer>, "expression_type": <String>, "code_block": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        expression_type = params.get("expression_type")
        if expression_type is None:
            return {"success": False, "error": "expression_type parameter is required"}
        code_block = params.get("code_block")
        enforce_domains = params.get("enforce_domains")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Calculate_Fields_(multiple)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Fields (multiple)
            arcpy.CalculateFields(multiple)(in_table, expression_type, code_block, enforce_domains)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_field(self, params):
        """Delete Field

Deletes one or more fields from a table, feature class, feature layer, or raster dataset.

        params: {"in_table": <Mosaic Layer; Raster Layer; Table View>, "drop_field": <Field>, "method": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        drop_field = params.get("drop_field")
        if drop_field is None:
            return {"success": False, "error": "drop_field parameter is required"}
        method = params.get("method")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Delete_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Field
            arcpy.DeleteField(in_table, drop_field, method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def migrate_text_field(self, params):
        """Migrate Text Field

Migrates text fields in an  Oracle table from Unicode to non-Unicode types.

        params: {"in_table": <Table View>, "fields": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Migrate_Text_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Migrate Text Field
            arcpy.MigrateTextField(in_table, fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compact(self, params):
        """Compact

Compacts a file or mobile geodatabase, SQLite database, or Open Geospatial Consortium (OGC) GeoPackage file. Compacting rearranges data storage, often reducing the file's size and improving performance.

        params: {"in_workspace": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Compact"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compact
            arcpy.Compact(in_workspace)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compress_file_geodatabase_data(self, params):
        """Compress File Geodatabase Data

Compresses all the contents in a geodatabase, all the contents in a feature dataset, or an individual stand-alone feature class or table.

        params: {"in_data": <Feature Dataset; Geometric Network; Raster Layer; Table View; Workspace>, "lossless": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        lossless = params.get("lossless")
        if lossless is None:
            return {"success": False, "error": "lossless parameter is required"}

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Compress_File_Geodatabase_Data"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compress File Geodatabase Data
            arcpy.CompressFileGeodatabaseData(in_data, lossless)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_file_geodatabase_license(self, params):
        """Generate File Geodatabase License

Generates a license file (.sdlic) for displaying the contents in a licensed file geodatabase created by the Generate Licensed File Geodatabase tool. Note:Licensing is not supported for geodatabases created earlier than version 10.1.

        params: {"in_lic_def_file": <File>, "out_lic_file": <File>, "allow_export": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_lic_def_file = params.get("in_lic_def_file")
        if in_lic_def_file is None:
            return {"success": False, "error": "in_lic_def_file parameter is required"}
        out_lic_file = params.get("out_lic_file")
        if out_lic_file is None:
            return {"success": False, "error": "out_lic_file parameter is required"}
        allow_export = params.get("allow_export")
        exp_date = params.get("exp_date")

            # Generate output name and path
            output_name = f"{in_lic_def_file.replace(' ', '_')}_Generate_File_Geodatabase_License"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate File Geodatabase License
            arcpy.GenerateFileGeodatabaseLicense(in_lic_def_file, out_lic_file, allow_export, exp_date)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_licensed_file_geodatabase(self, params):
        """Generate Licensed File Geodatabase

Generates a license definition file (.licdef) that defines and restricts the display of contents in a file geodatabase.  The contents of the licensed file geodatabase can be viewed by creating  a license file (*.sdlic) and configuring the ArcGIS clients to recognize it.  The license file is created using the Generate File Geodatabase License tool. Licensing is not supported for geodatabases created earlier than version 10.1.

        params: {"in_fgdb": <Workspace>, "out_fgdb": <Workspace>, "out_lic_def": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_fgdb = params.get("in_fgdb")
        if in_fgdb is None:
            return {"success": False, "error": "in_fgdb parameter is required"}
        out_fgdb = params.get("out_fgdb")
        if out_fgdb is None:
            return {"success": False, "error": "out_fgdb parameter is required"}
        out_lic_def = params.get("out_lic_def")
        if out_lic_def is None:
            return {"success": False, "error": "out_lic_def parameter is required"}

            # Generate output name and path
            output_name = f"{in_fgdb.replace(' ', '_')}_Generate_Licensed_File_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Licensed File Geodatabase
            arcpy.GenerateLicensedFileGeodatabase(in_fgdb, out_fgdb, out_lic_def)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def recover_file_geodatabase(self, params):
        """Recover File Geodatabase

Recovers data from a file geodatabase that has become corrupt. Learn more about how Recover File Geodatabase works

        params: {"input_file_gdb": <Workspace>, "output_location": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_file_gdb = params.get("input_file_gdb")
        if input_file_gdb is None:
            return {"success": False, "error": "input_file_gdb parameter is required"}
        output_location = params.get("output_location")
        if output_location is None:
            return {"success": False, "error": "output_location parameter is required"}

            # Generate output name and path
            output_name = f"{input_file_gdb.replace(' ', '_')}_Recover_File_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Recover File Geodatabase
            arcpy.RecoverFileGeodatabase(input_file_gdb, output_location)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def uncompress_file_geodatabase_data(self, params):
        """Uncompress File Geodatabase Data

Uncompresses all the contents in a geodatabase, all the contents in a feature dataset, or an individual stand-alone feature class or table.

        params: {"in_data": <Workspace; Feature Dataset; Table View; Raster Layer; Geometric Network>, "config_keyword": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Uncompress_File_Geodatabase_Data"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Uncompress File Geodatabase Data
            arcpy.UncompressFileGeodatabaseData(in_data, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_file_geodatabase(self, params):
        """Create File Geodatabase

Creates a file geodatabase in a folder.

        params: {"out_folder_path": <Folder>, "out_name": <String>, "out_version": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        out_version = params.get("out_version")

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_File_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create File Geodatabase
            arcpy.CreateFileGeodatabase(out_folder_path, out_name, out_version)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def append(self, params):
        """Append

Appends to, or optionally updates, an existing target dataset with multiple input datasets. Input datasets can be feature classes, tables, shapefiles, rasters, or annotation or dimension feature classes. To combine input datasets into a new output dataset, use the Merge tool.

        params: {"inputs": <Table View; Raster Layer>, "target": <Table View; Raster Layer>, "schema_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        inputs = params.get("inputs")
        if inputs is None:
            return {"success": False, "error": "inputs parameter is required"}
        target = params.get("target")
        if target is None:
            return {"success": False, "error": "target parameter is required"}
        schema_type = params.get("schema_type")
        field_mapping = params.get("field_mapping")
        subtype = params.get("subtype")
        expression = params.get("expression")
        match_fieldstarget_field_input_field = params.get("match_fieldstarget_field_input_field")
        update_geometry = params.get("update_geometry")
        enforce_domains = params.get("enforce_domains")
        feature_service_mode = params.get("feature_service_mode")

            # Generate output name and path
            output_name = f"{inputs.replace(' ', '_')}_Append"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Append
            arcpy.Append(inputs, target, schema_type, field_mapping, subtype, expression, match_fieldstarget_field_input_field, update_geometry, enforce_domains, feature_service_mode)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy(self, params):
        """Copy

Copies the input data to an output workspace of the same data type as the input workspace.

        params: {"in_data": <Data Element>, "out_data": <Data Element>, "data_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        out_data = params.get("out_data")
        if out_data is None:
            return {"success": False, "error": "out_data parameter is required"}
        data_type = params.get("data_type")
        associated_datafrom_name_data_type_to_name_config_keyword = params.get("associated_datafrom_name_data_type_to_name_config_keyword")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Copy"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy
            arcpy.Copy(in_data, out_data, data_type, associated_datafrom_name_data_type_to_name_config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_ai_service_connection_file(self, params):
        """Create AI Service Connection File

Creates a connection file for hosted AI services in ArcGIS Pro.

        params: {"out_folder_path": <Folder>, "out_name": <String>, "service_provider": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        service_provider = params.get("service_provider")
        connection_parameters = params.get("connection_parameters")
        secret_param_key = params.get("secret_param_key")
        secret_param_value = params.get("secret_param_value")

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_AI_Service_Connection_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create AI Service Connection File
            arcpy.CreateAIServiceConnectionFile(out_folder_path, out_name, service_provider, connection_parameters, secret_param_key, secret_param_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_database_view(self, params):
        """Create Database View

Creates a view in a database based on an SQL expression.

        params: {"input_database": <Workspace>, "view_name": <String>, "view_definition": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        view_name = params.get("view_name")
        if view_name is None:
            return {"success": False, "error": "view_name parameter is required"}
        view_definition = params.get("view_definition")
        if view_definition is None:
            return {"success": False, "error": "view_definition parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Create_Database_View"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Database View
            arcpy.CreateDatabaseView(input_database, view_name, view_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete(self, params):
        """Delete

Permanently deletes data. All types of geographic data supported by ArcGIS, as well as toolboxes and workspaces (folders and geodatabases), can be deleted. If the specified item is a workspace, all contained items will also be deleted.

        params: {"in_data": <Data Element; Graph; Layer; Table View; Utility Network>, "data_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        data_type = params.get("data_type")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Delete"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete
            arcpy.Delete(in_data, data_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_identical(self, params):
        """Delete Identical

Deletes records from a feature class or table that have identical values in a set of fields. If the geometry field is selected, feature geometries are compared. The Find Identical tool can be used to report which records are considered identical without deleting them.

        params: {"in_dataset": <Table View>, "fields": <Field>, "xy_tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}
        xy_tolerance = params.get("xy_tolerance")
        z_tolerance = params.get("z_tolerance")
        out_mapping_table = params.get("out_mapping_table")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Delete_Identical"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Identical
            arcpy.DeleteIdentical(in_dataset, fields, xy_tolerance, z_tolerance, out_mapping_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_multiple(self, params):
        """Delete Multiple

Permanently deletes multiple data items of the same or different data types. All types of geographic data supported by ArcGIS, as well as toolboxes and workspaces (folders and geodatabases), can be deleted. If a  specified item is a workspace, all contained items will also be deleted.

        params: {"in_datainput_data_element_data_type": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_datainput_data_element_data_type = params.get("in_datainput_data_element_data_type")
        if in_datainput_data_element_data_type is None:
            return {"success": False, "error": "in_datainput_data_element_data_type parameter is required"}

            # Generate output name and path
            output_name = f"{in_datainput_data_element_data_type.replace(' ', '_')}_Delete_Multiple"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Multiple
            arcpy.DeleteMultiple(in_datainput_data_element_data_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disable_last_edit_time(self, params):
        """Disable Last Edit Time

Disables the last edit time property on an enterprise geodatabase dataset. Disabling the last edit time property on a dataset will stop the recording of timestamps of when the data was last edited.

        params: {"in_dataset": <Table View; Feature Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Disable_Last_Edit_Time"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disable Last Edit Time
            arcpy.DisableLastEditTime(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_last_edit_time(self, params):
        """Enable Last Edit Time

Enables the last edit time property on an enterprise geodatabase dataset. Enabling the last edit time property on a dataset will enable the recording of timestamps of when the data was last edited. This supports a feature service and other clients to request from the geodatabase the timestamp of when the dataset was last edited. Knowing the last edit time is valuable for a feature service as it allows for response caching and other query enhancement.

        params: {"in_dataset": <Table View; Feature Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Enable_Last_Edit_Time"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Last Edit Time
            arcpy.EnableLastEditTime(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_data_from_geodatabase(self, params):
        """Extract Data From Geodatabase

Extracts a subset of data from one geodatabase to another geodatabase or an .xml file. Learn more about extracting data from a geodatabase

        params: {"in_data": <Table View; Dataset>, "extract_type": <String>, "out_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        extract_type = params.get("extract_type")
        out_type = params.get("out_type")
        out_geodatabase = params.get("out_geodatabase")
        out_xml = params.get("out_xml")
        out_folder_path = params.get("out_folder_path")
        out_name = params.get("out_name")
        expand_feature_classes_and_tables = params.get("expand_feature_classes_and_tables")
        reuse_schema = params.get("reuse_schema")
        get_related_data = params.get("get_related_data")
        extract_using_geometry_features = params.get("extract_using_geometry_features")
        geometry_filter_type = params.get("geometry_filter_type")
        all_records_for_tables = params.get("all_records_for_tables")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Extract_Data_From_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Data From Geodatabase
            arcpy.ExtractDataFromGeodatabase(in_data, extract_type, out_type, out_geodatabase, out_xml, out_folder_path, out_name, expand_feature_classes_and_tables, reuse_schema, get_related_data, extract_using_geometry_features, geometry_filter_type, all_records_for_tables)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def find_identical(self, params):
        """Find Identical

Reports any records in a feature class or table that have identical values in a list of fields, and generates a table listing the identical records. If the Shape field is specified, feature geometries will be compared. The Delete Identical tool can be used to find and delete identical records.

        params: {"in_dataset": <Table View>, "out_dataset": <Table>, "fields": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_dataset = params.get("out_dataset")
        if out_dataset is None:
            return {"success": False, "error": "out_dataset parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}
        xy_tolerance = params.get("xy_tolerance")
        z_tolerance = params.get("z_tolerance")
        output_record_option = params.get("output_record_option")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Find_Identical"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Find Identical
            arcpy.FindIdentical(in_dataset, out_dataset, fields, xy_tolerance, z_tolerance, output_record_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def merge(self, params):
        """Merge

Combines multiple input datasets into a single, new output dataset. This tool can combine point, line, or polygon feature classes or tables. Use the Append tool to combine input datasets with an existing dataset.

        params: {"inputs": <Table View>, "output": <Feature Class;Table>, "field_mappings": <Field Mappings>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        inputs = params.get("inputs")
        if inputs is None:
            return {"success": False, "error": "inputs parameter is required"}
        output = params.get("output")
        if output is None:
            return {"success": False, "error": "output parameter is required"}
        field_mappings = params.get("field_mappings")
        add_source = params.get("add_source")
        field_match_mode = params.get("field_match_mode")

            # Generate output name and path
            output_name = f"{inputs.replace(' ', '_')}_Merge"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Merge
            arcpy.Merge(inputs, output, field_mappings, add_source, field_match_mode)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rename(self, params):
        """Rename

Changes the name of a dataset.  This includes a variety of data types, including feature dataset, raster, table, and shapefile.

        params: {"in_data": <Data Element>, "out_data": <Data Element>, "data_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        out_data = params.get("out_data")
        if out_data is None:
            return {"success": False, "error": "out_data parameter is required"}
        data_type = params.get("data_type")
        if data_type is None:
            return {"success": False, "error": "data_type parameter is required"}

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Rename"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rename
            arcpy.Rename(in_data, out_data, data_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sort(self, params):
        """Sort

Reorders records in a feature class or table, in ascending or descending order, based on one or multiple fields. The reordered result is written to a new dataset. Learn more about how Sort works

        params: {"in_dataset": <Table View>, "out_dataset": <Feature Class; Table>, "sort_field_direction": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_dataset = params.get("out_dataset")
        if out_dataset is None:
            return {"success": False, "error": "out_dataset parameter is required"}
        sort_field_direction = params.get("sort_field_direction")
        if sort_field_direction is None:
            return {"success": False, "error": "sort_field_direction parameter is required"}
        spatial_sort_method = params.get("spatial_sort_method")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Sort"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sort
            arcpy.Sort(in_dataset, out_dataset, sort_field_direction, spatial_sort_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def transfer_files(self, params):
        """Transfer Files

Transfers files between a file system and a cloud storage workspace.

        params: {"input_paths": <Raster Dataset; File; Folder>, "output_folder": <Folder>, "file_filter": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_paths = params.get("input_paths")
        if input_paths is None:
            return {"success": False, "error": "input_paths parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        file_filter = params.get("file_filter")

            # Generate output name and path
            output_name = f"{input_paths.replace(' ', '_')}_Transfer_Files"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Transfer Files
            arcpy.TransferFiles(input_paths, output_folder, file_filter)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def upload_file_to_portal(self, params):
        """Upload File To Portal

Uploads a file to the active portal.

        params: {"in_file": <File>, "title": <String>, "folder": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_file = params.get("in_file")
        if in_file is None:
            return {"success": False, "error": "in_file parameter is required"}
        title = params.get("title")
        if title is None:
            return {"success": False, "error": "title parameter is required"}
        folder = params.get("folder")
        summary = params.get("summary")
        tags = params.get("tags")
        sharing_level = params.get("sharing_level")
        groups = params.get("groups")

            # Generate output name and path
            output_name = f"{in_file.replace(' ', '_')}_Upload_File_To_Portal"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Upload File To Portal
            arcpy.UploadFileToPortal(in_file, title, folder, summary, tags, sharing_level, groups)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def dissolve(self, params):
        """Dissolve

Aggregates features based on specified attributes. An alternate tool is available for dissolve operations. See the Pairwise Dissolve tool documentation for details. Learn more about how Dissolve works

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
        unsplit_lines = params.get("unsplit_lines")
        concatenation_separator = params.get("concatenation_separator")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Dissolve"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Dissolve
            arcpy.Dissolve(in_features, out_feature_class, dissolve_field, statistics_fieldsfield_statistic_type, multi_part, unsplit_lines, concatenation_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def eliminate(self, params):
        """Eliminate

Eliminates polygons by merging them with neighboring polygons that have the largest area or the longest shared border. This tool is often used to remove small sliver polygons that are the result of overlay operations, such as those performed by Intersect and Union tools.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "selection": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        selection = params.get("selection")
        ex_where_clause = params.get("ex_where_clause")
        ex_features = params.get("ex_features")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Eliminate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Eliminate
            arcpy.Eliminate(in_features, out_feature_class, selection, ex_where_clause, ex_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def eliminate_polygon_part(self, params):
        """Eliminate Polygon Part

Creates a new output feature class containing the features from the input polygons with some parts or holes of a specified size deleted.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "condition": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        condition = params.get("condition")
        part_area = params.get("part_area")
        part_area_percent = params.get("part_area_percent")
        part_option = params.get("part_option")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Eliminate_Polygon_Part"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Eliminate Polygon Part
            arcpy.EliminatePolygonPart(in_features, out_feature_class, condition, part_area, part_area_percent, part_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze_datasets(self, params):
        """Analyze Datasets

Updates database statistics of base tables, delta tables, and archive tables, along with the statistics on the indexes of those tables. This tool is used in enterprise geodatabases to help get optimal performance from the relational database management system (RDBMS) query optimizer. Stale statistics can affect geodatabase performance.

        params: {"input_database": <Workspace>, "include_system": <Boolean>, "in_datasets": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        include_system = params.get("include_system")
        if include_system is None:
            return {"success": False, "error": "include_system parameter is required"}
        in_datasets = params.get("in_datasets")
        analyze_base = params.get("analyze_base")
        analyze_delta = params.get("analyze_delta")
        analyze_archive = params.get("analyze_archive")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Analyze_Datasets"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Analyze Datasets
            arcpy.AnalyzeDatasets(input_database, include_system, in_datasets, analyze_base, analyze_delta, analyze_archive)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def change_privileges(self, params):
        """Change Privileges

Establishes or changes user access privileges on the input enterprise database datasets, stand-alone feature classes, or tables.

        params: {"in_dataset": <Layer; Table View; Dataset; Address Locator>, "user": <String>, "view": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        user = params.get("user")
        if user is None:
            return {"success": False, "error": "user parameter is required"}
        view = params.get("view")
        edit = params.get("edit")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Change_Privileges"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Change Privileges
            arcpy.ChangePrivileges(in_dataset, user, view, edit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compress(self, params):
        """Compress

Compresses an enterprise geodatabase by removing states not referenced by a version and redundant rows.

        params: {"in_workspace": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Compress"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compress
            arcpy.Compress(in_workspace)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def configure_geodatabase_log_file_tables(self, params):
        """Configure Geodatabase Log File Tables

Alters the type of log file tables used by an earlier release enterprise geodatabase to maintain lists of records cached by ArcGIS.

        params: {"input_database": <Workspace>, "log_file_type": <String>, "log_file_pool_size": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        log_file_type = params.get("log_file_type")
        if log_file_type is None:
            return {"success": False, "error": "log_file_type parameter is required"}
        log_file_pool_size = params.get("log_file_pool_size")
        use_tempdb = params.get("use_tempdb")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Configure_Geodatabase_Log_File_Tables"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Configure Geodatabase Log File Tables
            arcpy.ConfigureGeodatabaseLogFileTables(input_database, log_file_type, log_file_pool_size, use_tempdb)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_database_sequence(self, params):
        """Create Database Sequence

Creates a database sequence in a geodatabase. You can use the sequences in custom applications that access the geodatabase.

        params: {"in_workspace": <Workspace>, "seq_name": <String>, "seq_start_id": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        seq_name = params.get("seq_name")
        if seq_name is None:
            return {"success": False, "error": "seq_name parameter is required"}
        seq_start_id = params.get("seq_start_id")
        seq_inc_value = params.get("seq_inc_value")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Create_Database_Sequence"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Database Sequence
            arcpy.CreateDatabaseSequence(in_workspace, seq_name, seq_start_id, seq_inc_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_database_user(self, params):
        """Create Database User

Creates a database user with privileges sufficient to create data in the database.

        params: {"input_database": <Workspace>, "user_authentication_type": <Boolean>, "user_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        user_authentication_type = params.get("user_authentication_type")
        user_name = params.get("user_name")
        if user_name is None:
            return {"success": False, "error": "user_name parameter is required"}
        user_password = params.get("user_password")
        role = params.get("role")
        tablespace_name = params.get("tablespace_name")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Create_Database_User"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Database User
            arcpy.CreateDatabaseUser(input_database, user_authentication_type, user_name, user_password, role, tablespace_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_enterprise_geodatabase(self, params):
        """Create Enterprise Geodatabase

Creates a database, storage locations, and a database user to act as the geodatabase administrator and owner of the geodatabase. Functionality varies depending on the database management system used. The tool grants the geodatabase administrator the privileges required to create a geodatabase; it then creates a geodatabase in the database.

        params: {"database_platform": <String>, "instance_name": <String>, "database_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        database_platform = params.get("database_platform")
        if database_platform is None:
            return {"success": False, "error": "database_platform parameter is required"}
        instance_name = params.get("instance_name")
        if instance_name is None:
            return {"success": False, "error": "instance_name parameter is required"}
        database_name = params.get("database_name")
        account_authentication = params.get("account_authentication")
        database_admin = params.get("database_admin")
        database_admin_password = params.get("database_admin_password")
        sde_schema = params.get("sde_schema")
        gdb_admin_name = params.get("gdb_admin_name")
        gdb_admin_password = params.get("gdb_admin_password")
        tablespace_name = params.get("tablespace_name")
        authorization_file = params.get("authorization_file")
        if authorization_file is None:
            return {"success": False, "error": "authorization_file parameter is required"}
        spatial_type = params.get("spatial_type")

            # Generate output name and path
            output_name = f"{database_platform.replace(' ', '_')}_Create_Enterprise_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Enterprise Geodatabase
            arcpy.CreateEnterpriseGeodatabase(database_platform, instance_name, database_name, account_authentication, database_admin, database_admin_password, sde_schema, gdb_admin_name, gdb_admin_password, tablespace_name, authorization_file, spatial_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_role(self, params):
        """Create Role

Creates a database role, allowing you to add users to or remove them from the role.

        params: {"input_database": <Workspace>, "role": <String>, "grant_revoke": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        role = params.get("role")
        if role is None:
            return {"success": False, "error": "role parameter is required"}
        grant_revoke = params.get("grant_revoke")
        user_name = params.get("user_name")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Create_Role"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Role
            arcpy.CreateRole(input_database, role, grant_revoke, user_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_database_sequence(self, params):
        """Delete Database Sequence

Deletes a database sequence from a geodatabase.

        params: {"in_workspace": <Workspace>, "seq_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        seq_name = params.get("seq_name")
        if seq_name is None:
            return {"success": False, "error": "seq_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Delete_Database_Sequence"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Database Sequence
            arcpy.DeleteDatabaseSequence(in_workspace, seq_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_schema_geodatabase(self, params):
        """Delete Schema Geodatabase

Deletes a geodatabase from a user's schema in Oracle.

        params: {"input_database": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Delete_Schema_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Schema Geodatabase
            arcpy.DeleteSchemaGeodatabase(input_database)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def diagnose_version_metadata(self, params):
        """Diagnose Version Metadata

Identifies inconsistencies in the system tables used to manage traditional versions and states in a geodatabase.

        params: {"input_database": <Workspace>, "out_log": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        out_log = params.get("out_log")
        if out_log is None:
            return {"success": False, "error": "out_log parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Diagnose_Version_Metadata"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Diagnose Version Metadata
            arcpy.DiagnoseVersionMetadata(input_database, out_log)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def diagnose_version_tables(self, params):
        """Diagnose Version Tables

Identifies inconsistencies in the delta (A and D) tables of datasets that are registered for traditional versioning.

        params: {"input_database": <Workspace>, "out_log": <File>, "target_version": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        out_log = params.get("out_log")
        if out_log is None:
            return {"success": False, "error": "out_log parameter is required"}
        target_version = params.get("target_version")
        input_tables = params.get("input_tables")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Diagnose_Version_Tables"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Diagnose Version Tables
            arcpy.DiagnoseVersionTables(input_database, out_log, target_version, input_tables)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_enterprise_geodatabase(self, params):
        """Enable Enterprise Geodatabase

Creates geodatabase system tables, stored procedures, functions, and types in an existing database, which enable geodatabase functionality in the database.

        params: {"input_database": <Workspace>, "authorization_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        authorization_file = params.get("authorization_file")
        if authorization_file is None:
            return {"success": False, "error": "authorization_file parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Enable_Enterprise_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Enterprise Geodatabase
            arcpy.EnableEnterpriseGeodatabase(input_database, authorization_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_geodatabase_configuration_keywords(self, params):
        """Export Geodatabase Configuration Keywords

Exports the configuration keywords, parameters, and values from the specified enterprise geodatabase to an editable file. Change parameter values or add custom configuration keywords to the file and use the Import Geodatabase Configuration Keywords tool to import the changes to the geodatabase.

        params: {"input_database": <Workspace>, "out_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        out_file = params.get("out_file")
        if out_file is None:
            return {"success": False, "error": "out_file parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Export_Geodatabase_Configuration_Keywords"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Geodatabase Configuration Keywords
            arcpy.ExportGeodatabaseConfigurationKeywords(input_database, out_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_geodatabase_configuration_keywords(self, params):
        """Import Geodatabase Configuration Keywords

Defines data storage parameters for an enterprise geodatabase by importing a file containing configuration keywords, parameters, and values.

        params: {"input_database": <Workspace>, "in_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        in_file = params.get("in_file")
        if in_file is None:
            return {"success": False, "error": "in_file parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Import_Geodatabase_Configuration_Keywords"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import Geodatabase Configuration Keywords
            arcpy.ImportGeodatabaseConfigurationKeywords(input_database, in_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def migrate_object_id_to_64_bit(self, params):
        """Migrate Object ID To 64-Bit

Migrates a dataset's or multiple datasets' ObjectID field to 64-bit object IDs. Learn more about migrating to 64-bit object IDs

        params: {"in_datasets": <Table View; Feature Dataset; Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_datasets = params.get("in_datasets")
        if in_datasets is None:
            return {"success": False, "error": "in_datasets parameter is required"}

            # Generate output name and path
            output_name = f"{in_datasets.replace(' ', '_')}_Migrate_Object_ID_To_64-Bit"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Migrate Object ID To 64-Bit
            arcpy.MigrateObjectIDTo64Bit(in_datasets)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def migrate_storage(self, params):
        """Migrate Storage

Migrates the data from a binary, spatial, or spatial attribute column of one data type to a new column of a different data type in geodatabases in Oracle and SQL Server. The configuration keyword you specify when migrating determines the data type used for the new column. After migrating the data type, you must disconnect from and reconnect to the geodatabase to reload the columns. If you do not, subsequent actions run on the newly migrated datasets may fail.

        params: {"in_datasets": <Table View; Raster Layer; Feature Dataset>, "config_keyword": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_datasets = params.get("in_datasets")
        if in_datasets is None:
            return {"success": False, "error": "in_datasets parameter is required"}
        config_keyword = params.get("config_keyword")
        if config_keyword is None:
            return {"success": False, "error": "config_keyword parameter is required"}

            # Generate output name and path
            output_name = f"{in_datasets.replace(' ', '_')}_Migrate_Storage"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Migrate Storage
            arcpy.MigrateStorage(in_datasets, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rebuild_indexes(self, params):
        """Rebuild Indexes

Rebuild existing attribute or spatial indexes in enterprise geodatabases.  Indexes  can also be rebuilt on  states and state_lineage geodatabase system tables and the delta tables of datasets that are registered to participate in traditional versioning. Out-of-date indexes can lead to poor query performance.

        params: {"input_database": <Workspace>, "include_system": <Boolean>, "delta_only": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        include_system = params.get("include_system")
        if include_system is None:
            return {"success": False, "error": "include_system parameter is required"}
        delta_only = params.get("delta_only")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Rebuild_Indexes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rebuild Indexes
            arcpy.RebuildIndexes(input_database, include_system, delta_only)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def register_with_geodatabase(self, params):
        """Register With Geodatabase

Registers feature classes, tables, views, and raster layers with the geodatabase. Registering is used for data created in the database with third-party tools using SQL or in ArcGIS Pro with tools that do not register with the geodatabase (Create Unregistered Feature Class, Create Unregistered Table, and  Create Database View  tools). Only limited functionality is available from ArcGIS clients and services for data is that is  not registered. Registration stores information about the items—such as table and column names, spatial extent, and geometry type—in the geodatabase's system tables. This allows the registered items to participate in geodatabase functionality. Learn more about how to register a table or view with the geodatabase

        params: {"in_dataset": <Table View; Raster Layer>, "in_object_id_field": <Field>, "in_shape_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        in_object_id_field = params.get("in_object_id_field")
        in_shape_field = params.get("in_shape_field")
        in_geometry_type = params.get("in_geometry_type")
        in_spatial_reference = params.get("in_spatial_reference")
        in_extent = params.get("in_extent")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Register_With_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Register With Geodatabase
            arcpy.RegisterWithGeodatabase(in_dataset, in_object_id_field, in_shape_field, in_geometry_type, in_spatial_reference, in_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_unregistered_feature_class(self, params):
        """Create Unregistered Feature Class

Creates an empty feature class in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The feature class is not registered with the geodatabase.

        params: {"out_path": <Workspace; Feature Dataset>, "out_name": <String>, "geometry_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        geometry_type = params.get("geometry_type")
        template = params.get("template")
        has_m = params.get("has_m")
        has_z = params.get("has_z")
        spatial_reference = params.get("spatial_reference")
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Unregistered_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Unregistered Feature Class
            arcpy.CreateUnregisteredFeatureClass(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_unregistered_table(self, params):
        """Create Unregistered Table

Creates an empty table in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The table is not registered with the geodatabase.

        params: {"out_path": <Workspace>, "out_name": <String>, "template": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        template = params.get("template")
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Unregistered_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Unregistered Table
            arcpy.CreateUnregisteredTable(out_path, out_name, template, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_database_view(self, params):
        """Create Database View

Creates a view in a database based on an SQL expression.

        params: {"input_database": <Workspace>, "view_name": <String>, "view_definition": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        view_name = params.get("view_name")
        if view_name is None:
            return {"success": False, "error": "view_name parameter is required"}
        view_definition = params.get("view_definition")
        if view_definition is None:
            return {"success": False, "error": "view_definition parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Create_Database_View"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Database View
            arcpy.CreateDatabaseView(input_database, view_name, view_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def repair_version_metadata(self, params):
        """Repair Version Metadata

Repairs inconsistencies in the versioning system tables of a geodatabase that contains traditional versions.

        params: {"input_database": <Workspace>, "out_log": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        out_log = params.get("out_log")
        if out_log is None:
            return {"success": False, "error": "out_log parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Repair_Version_Metadata"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Repair Version Metadata
            arcpy.RepairVersionMetadata(input_database, out_log)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def repair_version_tables(self, params):
        """Repair Version Tables

Repairs inconsistencies in the delta (A and D) tables of datasets that are registered for traditional versioning.

        params: {"input_database": <Workspace>, "out_log": <File>, "target_version": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        out_log = params.get("out_log")
        if out_log is None:
            return {"success": False, "error": "out_log parameter is required"}
        target_version = params.get("target_version")
        input_tables = params.get("input_tables")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Repair_Version_Tables"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Repair Version Tables
            arcpy.RepairVersionTables(input_database, out_log, target_version, input_tables)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_enterprise_geodatabase_license(self, params):
        """Update Enterprise Geodatabase License

Updates the ArcGIS Server license in an enterprise geodatabase. If your organization licenses ArcGIS Server for a set time period, the geodatabase administrator can run the Update Enterprise Geodatabase License tool with a new  ArcGIS Server authorization file to update license information in the geodatabase before the existing license expires. This allows clients to continue working with the geodatabase without interruptions caused by expired licenses.

        params: {"input_database": <Workspace>, "authorization_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        authorization_file = params.get("authorization_file")
        if authorization_file is None:
            return {"success": False, "error": "authorization_file parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Update_Enterprise_Geodatabase_License"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Enterprise Geodatabase License
            arcpy.UpdateEnterpriseGeodatabaseLicense(input_database, authorization_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_portal_dataset_owner(self, params):
        """Update Portal Dataset Owner

Updates the portal owner of a dataset to another user. Certain datasets in an enterprise geodatabase store the active portal user account as the owner of the dataset, in addition to the data owner. The owner is determined based on the active portal user when the dataset is created. This ownership is stored in the metadata of the dataset and is used to control access for administrative tasks on the dataset. If the existing portal dataset owner leaves the organization, the portal owner must be changed to another user. This user should possess the same user type and privilege as the original owner. The following are examples of a portal dataset owner:Utility Network—Portal utility network ownerTrace Network—Portal trace network owner

        params: {"in_dataset": <Utility Network; Utility Network Layer; Trace Network; Trace Network Layer>, "target_owner": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        target_owner = params.get("target_owner")
        if target_owner is None:
            return {"success": False, "error": "target_owner parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Update_Portal_Dataset_Owner"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Portal Dataset Owner
            arcpy.UpdatePortalDatasetOwner(in_dataset, target_owner)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def upgrade_dataset(self, params):
        """Upgrade Dataset

Upgrades the schema of a mosaic dataset, network dataset, annotation dataset, dimension dataset, parcel fabric, trace network, utility network, or 3D object feature class to the current ArcGIS release. Upgrading a dataset enables it to use new functionality in the current software release.

        params: {"in_dataset": <Parcel Fabric Layer for ArcMap; Parcel Layer; Mosaic Layer; Network Dataset Layer; Trace Network Layer; Utility Network Layer; Annotation Layer; Dimension Layer; Catalog Layer; 3D Object Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Upgrade_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Upgrade Dataset
            arcpy.UpgradeDataset(in_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def upgrade_geodatabase(self, params):
        """Upgrade Geodatabase

Upgrades a geodatabase to the latest ArcGIS release to take advantage of new functionality.

        params: {"input_workspace": <Workspace>, "input_prerequisite_check": <Boolean>, "input_upgradegdb_check": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_workspace = params.get("input_workspace")
        if input_workspace is None:
            return {"success": False, "error": "input_workspace parameter is required"}
        input_prerequisite_check = params.get("input_prerequisite_check")
        if input_prerequisite_check is None:
            return {"success": False, "error": "input_prerequisite_check parameter is required"}
        input_upgradegdb_check = params.get("input_upgradegdb_check")
        if input_upgradegdb_check is None:
            return {"success": False, "error": "input_upgradegdb_check parameter is required"}

            # Generate output name and path
            output_name = f"{input_workspace.replace(' ', '_')}_Upgrade_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Upgrade Geodatabase
            arcpy.UpgradeGeodatabase(input_workspace, input_prerequisite_check, input_upgradegdb_check)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_attribute_index(self, params):
        """Add Attribute Index

Adds an attribute index to an existing table, feature class, shapefile, or attributed relationship class. Attribute indexes are used by ArcGIS to quickly locate records that match an attribute query.

        params: {"in_table": <Mosaic Layer; Raster Layer; Table View>, "fields": <Field>, "index_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}
        index_name = params.get("index_name")
        unique = params.get("unique")
        ascending = params.get("ascending")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Add_Attribute_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Attribute Index
            arcpy.AddAttributeIndex(in_table, fields, index_name, unique, ascending)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_full_text_index(self, params):
        """Add Full-Text Index

Adds a full-text index to specified text fields to support searching by an individual column or by multiple columns. Learn more about using full-text indexes in the geodatabase

        params: {"in_table": <Table View>, "fields": <Field>, "index_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}
        index_name = params.get("index_name")
        catalog_name = params.get("catalog_name")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Add_Full-Text_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Full-Text Index
            arcpy.AddFullTextIndex(in_table, fields, index_name, catalog_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_spatial_index(self, params):
        """Add Spatial Index

Adds a spatial index to a shapefile, file geodatabase, mobile geodatabase, or enterprise geodatabase feature class.   Use this tool to either add a spatial index to a shapefile or feature class that does not already have one or to re-create an existing spatial index. Learn more about spatial indexes in the geodatabase

        params: {"in_features": <Feature Layer; Mosaic Layer>, "spatial_grid_1": <Double>, "spatial_grid_2": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        spatial_grid_1 = params.get("spatial_grid_1")
        spatial_grid_2 = params.get("spatial_grid_2")
        spatial_grid_3 = params.get("spatial_grid_3")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Add_Spatial_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Spatial Index
            arcpy.AddSpatialIndex(in_features, spatial_grid_1, spatial_grid_2, spatial_grid_3)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_attribute_index(self, params):
        """Remove Attribute Index

Deletes an attribute index from an existing table, feature class, shapefile, or attributed relationship class. Attribute indexes are used by ArcGIS to quickly locate records that match an attribute query.

        params: {"in_table": <Table View; Raster Layer; Mosaic Layer>, "index_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        index_name = params.get("index_name")
        if index_name is None:
            return {"success": False, "error": "index_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Remove_Attribute_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Attribute Index
            arcpy.RemoveAttributeIndex(in_table, index_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_spatial_index(self, params):
        """Remove Spatial Index

Deletes the spatial index from a shapefile or file geodatabase, mobile geodatabase, or an enterprise geodatabase feature class. Spatial indexes are used by ArcGIS to quickly locate features that match a spatial query.

        params: {"in_features": <Feature Layer; Mosaic Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Remove_Spatial_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Spatial Index
            arcpy.RemoveSpatialIndex(in_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_join(self, params):
        """Add Join

Joins a layer to another layer or table based on a common field. Feature layers, table views, and raster layers with a raster attribute table are supported. The records in the Join Table parameter value will be matched to the records in the  Input Table parameter value. A match is made when the input field and join field values are equal. This join is temporary.

        params: {"in_layer_or_view": <Mosaic Layer; Raster Layer; Table View>, "in_field": <Field>, "join_table": <Mosaic Layer; Raster Layer; Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer_or_view = params.get("in_layer_or_view")
        if in_layer_or_view is None:
            return {"success": False, "error": "in_layer_or_view parameter is required"}
        in_field = params.get("in_field")
        if in_field is None:
            return {"success": False, "error": "in_field parameter is required"}
        join_table = params.get("join_table")
        if join_table is None:
            return {"success": False, "error": "join_table parameter is required"}
        join_field = params.get("join_field")
        if join_field is None:
            return {"success": False, "error": "join_field parameter is required"}
        join_type = params.get("join_type")
        index_join_fields = params.get("index_join_fields")
        rebuild_index = params.get("rebuild_index")
        join_operation = params.get("join_operation")

            # Generate output name and path
            output_name = f"{in_layer_or_view.replace(' ', '_')}_Add_Join"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Join
            arcpy.AddJoin(in_layer_or_view, in_field, join_table, join_field, join_type, index_join_fields, rebuild_index, join_operation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_relate(self, params):
        """Add Relate

Relates a layer to another layer or table based on a field value. Feature layers, table views, subtype value layers or tables, and raster layers with a raster attribute table are supported. The records in the Relate Table parameter value are matched to the records in the input Layer Name or Table View parameter value. A match occurs when a field value in the Input Relate Field parameter value and a field value in the Output Relate Field parameter value are equal.

        params: {"in_layer_or_view": <Mosaic Layer; Raster Layer; Table View>, "in_field": <Field>, "relate_table": <Mosaic Layer; Raster Layer; Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer_or_view = params.get("in_layer_or_view")
        if in_layer_or_view is None:
            return {"success": False, "error": "in_layer_or_view parameter is required"}
        in_field = params.get("in_field")
        if in_field is None:
            return {"success": False, "error": "in_field parameter is required"}
        relate_table = params.get("relate_table")
        if relate_table is None:
            return {"success": False, "error": "relate_table parameter is required"}
        relate_field = params.get("relate_field")
        if relate_field is None:
            return {"success": False, "error": "relate_field parameter is required"}
        relate_name = params.get("relate_name")
        if relate_name is None:
            return {"success": False, "error": "relate_name parameter is required"}
        cardinality = params.get("cardinality")

            # Generate output name and path
            output_name = f"{in_layer_or_view.replace(' ', '_')}_Add_Relate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Relate
            arcpy.AddRelate(in_layer_or_view, in_field, relate_table, relate_field, relate_name, cardinality)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_spatial_join(self, params):
        """Add Spatial Join

Joins attributes from one feature to another based on the spatial relationship. The target features and the joined attributes from the join features will be joined. See Select By Location graphic examples for more information.

        params: {"target_features": <Feature Layer>, "join_features": <Feature Layer>, "join_operation": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        target_features = params.get("target_features")
        if target_features is None:
            return {"success": False, "error": "target_features parameter is required"}
        join_features = params.get("join_features")
        if join_features is None:
            return {"success": False, "error": "join_features parameter is required"}
        join_operation = params.get("join_operation")
        join_type = params.get("join_type")
        field_mapping = params.get("field_mapping")
        match_option = params.get("match_option")
        search_radius = params.get("search_radius")
        distance_field_name = params.get("distance_field_name")
        permanent_join = params.get("permanent_join")
        match_fieldsjoin_field_target_field = params.get("match_fieldsjoin_field_target_field")

            # Generate output name and path
            output_name = f"{target_features.replace(' ', '_')}_Add_Spatial_Join"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Spatial Join
            arcpy.AddSpatialJoin(target_features, join_features, join_operation, join_type, field_mapping, match_option, search_radius, distance_field_name, permanent_join, match_fieldsjoin_field_target_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def join_field(self, params):
        """Join Field

Permanently joins the contents of a table to another table based on a common attribute field. The input table is updated to contain the fields from the join table. You can select which fields from the join table will be added to the input table.

        params: {"in_data": <Mosaic Layer; Raster Layer; Table View>, "in_field": <Field>, "join_table": <Mosaic Layer; Raster Layer; Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        in_field = params.get("in_field")
        if in_field is None:
            return {"success": False, "error": "in_field parameter is required"}
        join_table = params.get("join_table")
        if join_table is None:
            return {"success": False, "error": "join_table parameter is required"}
        join_field = params.get("join_field")
        if join_field is None:
            return {"success": False, "error": "join_field parameter is required"}
        fields = params.get("fields")
        fm_option = params.get("fm_option")
        field_mapping = params.get("field_mapping")
        index_join_fields = params.get("index_join_fields")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Join_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Join Field
            arcpy.JoinField(in_data, in_field, join_table, join_field, fields, fm_option, field_mapping, index_join_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_join(self, params):
        """Remove Join

Removes a join from a feature layer or table view.

        params: {"in_layer_or_view": <Mosaic Layer; Raster Layer; Table View>, "join_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer_or_view = params.get("in_layer_or_view")
        if in_layer_or_view is None:
            return {"success": False, "error": "in_layer_or_view parameter is required"}
        join_name = params.get("join_name")

            # Generate output name and path
            output_name = f"{in_layer_or_view.replace(' ', '_')}_Remove_Join"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Join
            arcpy.RemoveJoin(in_layer_or_view, join_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_relate(self, params):
        """Remove Relate

Removes a relate from a feature layer or a table view.

        params: {"in_layer_or_view": <Mosaic Layer; Raster Layer; Table View>, "relate_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer_or_view = params.get("in_layer_or_view")
        if in_layer_or_view is None:
            return {"success": False, "error": "in_layer_or_view parameter is required"}
        relate_name = params.get("relate_name")
        if relate_name is None:
            return {"success": False, "error": "relate_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_layer_or_view.replace(' ', '_')}_Remove_Relate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Relate
            arcpy.RemoveRelate(in_layer_or_view, relate_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def validate_join(self, params):
        """Validate Join

Validates a  join between two layers or tables to determine if the layers or tables have valid field names and Object ID fields, if the join produces matching records, if the join is a one-to-one or one-to-many join, and other properties of the join. This tool does not produce a join; it analyzes a potential join with the current data.  Since all joins can potentially become one-to-many, the layer properties will always show cardinality one-to-many.  A join can change from one-to-one to one-to-many if the data changes. The join being validated by this tool can be created using the Add Join or Join Field tool. This tool will report the join validation results as messages and optionally as an output table.

        params: {"in_layer_or_view": <Mosaic Layer; Raster Layer; Table View>, "in_field": <Field>, "join_table": <Mosaic Layer; Raster Layer; Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer_or_view = params.get("in_layer_or_view")
        if in_layer_or_view is None:
            return {"success": False, "error": "in_layer_or_view parameter is required"}
        in_field = params.get("in_field")
        if in_field is None:
            return {"success": False, "error": "in_field parameter is required"}
        join_table = params.get("join_table")
        if join_table is None:
            return {"success": False, "error": "join_table parameter is required"}
        join_field = params.get("join_field")
        if join_field is None:
            return {"success": False, "error": "join_field parameter is required"}
        output_msg = params.get("output_msg")

            # Generate output name and path
            output_name = f"{in_layer_or_view.replace(' ', '_')}_Validate_Join"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Validate Join
            arcpy.ValidateJoin(in_layer_or_view, in_field, join_table, join_field, output_msg)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_files_to_las_dataset(self, params):
        """Add Files To LAS Dataset

Adds references for one or more LAS files and  surface constraint features to a LAS dataset.

        params: {"in_las_dataset": <LAS Dataset Layer>, "in_files": <LAS Dataset Layer; Folder; File>, "folder_recursion": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        in_files = params.get("in_files")
        folder_recursion = params.get("folder_recursion")
        in_surface_constraintsin_feature_class_height_field_sf_type = params.get("in_surface_constraintsin_feature_class_height_field_sf_type")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_Add_Files_To_LAS_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Files To LAS Dataset
            arcpy.AddFilesToLASDataset(in_las_dataset, in_files, folder_recursion, in_surface_constraintsin_feature_class_height_field_sf_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_las_dataset_pyramid(self, params):
        """Build LAS Dataset Pyramid

Constructs or updates a LAS dataset display cache, which optimizes its rendering performance. Learn more about the LAS dataset pyramid

        params: {"in_las_dataset": <LAS Dataset Layer>, "point_selection_method": <String>, "class_codes_weights": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        point_selection_method = params.get("point_selection_method")
        class_codes_weights = params.get("class_codes_weights")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_Build_LAS_Dataset_Pyramid"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build LAS Dataset Pyramid
            arcpy.BuildLASDatasetPyramid(in_las_dataset, point_selection_method, class_codes_weights)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_las_dataset(self, params):
        """Create LAS Dataset

Creates a LAS dataset referencing one or more .las files and optional surface constraint features.

        params: {"input": <LAS Dataset Layer; File; Folder>, "out_las_dataset": <LAS Dataset>, "folder_recursion": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input = params.get("input")
        if input is None:
            return {"success": False, "error": "input parameter is required"}
        out_las_dataset = params.get("out_las_dataset")
        if out_las_dataset is None:
            return {"success": False, "error": "out_las_dataset parameter is required"}
        folder_recursion = params.get("folder_recursion")
        in_surface_constraintsin_feature_class_height_field_sf_type = params.get("in_surface_constraintsin_feature_class_height_field_sf_type")
        spatial_reference = params.get("spatial_reference")
        compute_stats = params.get("compute_stats")
        relative_paths = params.get("relative_paths")
        create_las_prj = params.get("create_las_prj")
        if create_las_prj is None:
            return {"success": False, "error": "create_las_prj parameter is required"}
        extent = params.get("extent")
        boundary = params.get("boundary")
        add_only_contained_files = params.get("add_only_contained_files")

            # Generate output name and path
            output_name = f"{input.replace(' ', '_')}_Create_LAS_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create LAS Dataset
            arcpy.CreateLASDataset(input, out_las_dataset, folder_recursion, in_surface_constraintsin_feature_class_height_field_sf_type, spatial_reference, compute_stats, relative_paths, create_las_prj, extent, boundary, add_only_contained_files)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def las_dataset_statistics(self, params):
        """LAS Dataset Statistics

Calculates or updates statistics for a LAS dataset and generates an optional statistics report.

        params: {"in_las_dataset": <LAS Dataset Layer>, "calculation_type": <Boolean>, "out_file": <Text File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        calculation_type = params.get("calculation_type")
        out_file = params.get("out_file")
        summary_level = params.get("summary_level")
        delimiter = params.get("delimiter")
        decimal_separator = params.get("decimal_separator")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_LAS_Dataset_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute LAS Dataset Statistics
            arcpy.LASDatasetStatistics(in_las_dataset, calculation_type, out_file, summary_level, delimiter, decimal_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def las_point_statistics_as_raster(self, params):
        """LAS Point Statistics As Raster

Creates a raster whose cell values reflect statistical information about LAS points.

        params: {"in_las_dataset": <LAS Dataset Layer>, "out_raster": <Raster Dataset>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        method = params.get("method")
        sampling_type = params.get("sampling_type")
        sampling_value = params.get("sampling_value")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_LAS_Point_Statistics_As_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute LAS Point Statistics As Raster
            arcpy.LASPointStatisticsAsRaster(in_las_dataset, out_raster, method, sampling_type, sampling_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def project_las(self, params):
        """Project LAS

Projects .las or .zlas files from one coordinate system to another.

        params: {"in_las_dataset": <LAS Dataset Layer>, "target_folder": <Folder>, "coordinate_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        target_folder = params.get("target_folder")
        if target_folder is None:
            return {"success": False, "error": "target_folder parameter is required"}
        coordinate_system = params.get("coordinate_system")
        if coordinate_system is None:
            return {"success": False, "error": "coordinate_system parameter is required"}
        geographic_transform = params.get("geographic_transform")
        compression = params.get("compression")
        las_options = params.get("las_options")
        name_modifier = params.get("name_modifier")
        out_las_dataset = params.get("out_las_dataset")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_Project_LAS"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Project LAS
            arcpy.ProjectLAS(in_las_dataset, target_folder, coordinate_system, geographic_transform, compression, las_options, name_modifier, out_las_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_files_from_las_dataset(self, params):
        """Remove Files From LAS Dataset

Removes one or more LAS files and surface constraint features from a LAS dataset.

        params: {"in_las_dataset": <LAS Dataset Layer>, "in_files": <String>, "in_surface_constraints": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        in_files = params.get("in_files")
        in_surface_constraints = params.get("in_surface_constraints")
        delete_pyramid = params.get("delete_pyramid")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_Remove_Files_From_LAS_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Files From LAS Dataset
            arcpy.RemoveFilesFromLASDataset(in_las_dataset, in_files, in_surface_constraints, delete_pyramid)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_symbology_from_layer(self, params):
        """Apply Symbology From Layer

Applies the symbology from a specified layer or layer file to the input. It can be applied to feature, raster, network analysis, TIN, and geostatistical layers.

        params: {"in_layer": <Feature Layer; Raster Layer; Layer>, "in_symbology_layer": <Layer>, "symbology_fieldsfield_type_source_field_target_field": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        in_symbology_layer = params.get("in_symbology_layer")
        if in_symbology_layer is None:
            return {"success": False, "error": "in_symbology_layer parameter is required"}
        symbology_fieldsfield_type_source_field_target_field = params.get("symbology_fieldsfield_type_source_field_target_field")
        update_symbology = params.get("update_symbology")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Apply_Symbology_From_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Symbology From Layer
            arcpy.ApplySymbologyFromLayer(in_layer, in_symbology_layer, symbology_fieldsfield_type_source_field_target_field, update_symbology)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_definition_query_from_selection(self, params):
        """Generate Definition Query From Selection

Creates a definition query (in SQL format) from the selected features or rows of the layer or table.

        params: {"in_table": <Table View>, "method": <String>, "field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        method = params.get("method")
        field = params.get("field")
        query_name = params.get("query_name")
        invert_where_clause = params.get("invert_where_clause")
        append_active_query = params.get("append_active_query")
        overwrite_where_clause = params.get("overwrite_where_clause")
        where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Generate_Definition_Query_From_Selection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Definition Query From Selection
            arcpy.GenerateDefinitionQueryFromSelection(in_table, method, field, query_name, invert_where_clause, append_active_query, overwrite_where_clause, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_aggregation_query_layer(self, params):
        """Make Aggregation Query Layer

Creates a query layer that summarizes, aggregates,  and filters DBMS tables dynamically based on time, range, and attribute queries from a related table, and joins the result to a feature layer. Learn more about aggregating values into related features

        params: {"target_feature_class": <Feature Class>, "target_join_field": <Field>, "related_table": <Table; Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        target_feature_class = params.get("target_feature_class")
        if target_feature_class is None:
            return {"success": False, "error": "target_feature_class parameter is required"}
        target_join_field = params.get("target_join_field")
        if target_join_field is None:
            return {"success": False, "error": "target_join_field parameter is required"}
        related_table = params.get("related_table")
        if related_table is None:
            return {"success": False, "error": "related_table parameter is required"}
        related_join_field = params.get("related_join_field")
        if related_join_field is None:
            return {"success": False, "error": "related_join_field parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        statisticsstatistic_type_field = params.get("statisticsstatistic_type_field")
        oid_fields = params.get("oid_fields")
        shape_type = params.get("shape_type")
        srid = params.get("srid")
        spatial_reference = params.get("spatial_reference")
        m_values = params.get("m_values")
        z_values = params.get("z_values")
        extent = params.get("extent")

            # Generate output name and path
            output_name = f"{target_feature_class.replace(' ', '_')}_Make_Aggregation_Query_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Aggregation Query Layer
            arcpy.MakeAggregationQueryLayer(target_feature_class, target_join_field, related_table, related_join_field, out_layer, statisticsstatistic_type_field, oid_fields, shape_type, srid, spatial_reference, m_values, z_values, extent)

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


    def make_feature_layer(self, params):
        """Make Feature Layer

Creates a feature layer from a feature class or layer file. The layer that is created is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.

        params: {"in_features": <Feature Layer>, "out_layer": <Feature Layer>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        where_clause = params.get("where_clause")
        workspace = params.get("workspace")
        field_info = params.get("field_info")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Make_Feature_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Feature Layer
            arcpy.MakeFeatureLayer(in_features, out_layer, where_clause, workspace, field_info)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_image_server_layer(self, params):
        """Make Image Server Layer

Creates a temporary raster layer from an image service. The layer that is created will not persist after the session ends unless the document is saved. The input can also be a SOAP URL to an image server.

        params: {"out_imageserver_layer": <Raster Layer>, "template": <Extent>, "band_indexid": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_imageserver_layer = params.get("out_imageserver_layer")
        if out_imageserver_layer is None:
            return {"success": False, "error": "out_imageserver_layer parameter is required"}
        template = params.get("template")
        band_indexid = params.get("band_indexid")
        mosaic_method = params.get("mosaic_method")
        order_field = params.get("order_field")
        order_base_value = params.get("order_base_value")
        lock_rasterid = params.get("lock_rasterid")
        cell_size = params.get("cell_size")
        where_clause = params.get("where_clause")
        processing_template = params.get("processing_template")

            # Generate output name and path
            output_name = f"{out_imageserver_layer.replace(' ', '_')}_Make_Image_Server_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Image Server Layer
            arcpy.MakeImageServerLayer(out_imageserver_layer, template, band_indexid, mosaic_method, order_field, order_base_value, lock_rasterid, cell_size, where_clause, processing_template)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_las_dataset_layer(self, params):
        """Make LAS Dataset Layer

Creates a  LAS dataset layer that can apply  filters to LAS points and control the enforcement of surface constraint features.

        params: {"in_las_dataset": <LAS Dataset Layer>, "out_layer": <LAS Dataset Layer>, "class_code": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        class_code = params.get("class_code")
        return_values = params.get("return_values")
        no_flag = params.get("no_flag")
        synthetic = params.get("synthetic")
        keypoint = params.get("keypoint")
        withheld = params.get("withheld")
        surface_constraints = params.get("surface_constraints")
        overlap = params.get("overlap")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_Make_LAS_Dataset_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make LAS Dataset Layer
            arcpy.MakeLASDatasetLayer(in_las_dataset, out_layer, class_code, return_values, no_flag, synthetic, keypoint, withheld, surface_constraints, overlap)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_mosaic_layer(self, params):
        """Make Mosaic Layer

Creates a  mosaic layer from a mosaic dataset or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved as a layer file or the map  is saved. This tool can be used to make a  layer so you can work with a specified subset of bands in a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "out_mosaic_layer": <Mosaic Layer>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_mosaic_layer = params.get("out_mosaic_layer")
        if out_mosaic_layer is None:
            return {"success": False, "error": "out_mosaic_layer parameter is required"}
        where_clause = params.get("where_clause")
        template = params.get("template")
        band_indexid = params.get("band_indexid")
        mosaic_method = params.get("mosaic_method")
        order_field = params.get("order_field")
        order_base_value = params.get("order_base_value")
        lock_rasterid = params.get("lock_rasterid")
        sort_order = params.get("sort_order")
        mosaic_operator = params.get("mosaic_operator")
        cell_size = params.get("cell_size")
        processing_template = params.get("processing_template")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Make_Mosaic_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Mosaic Layer
            arcpy.MakeMosaicLayer(in_mosaic_dataset, out_mosaic_layer, where_clause, template, band_indexid, mosaic_method, order_field, order_base_value, lock_rasterid, sort_order, mosaic_operator, cell_size, processing_template)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_query_layer(self, params):
        """Make Query Layer

Creates a query layer  from a DBMS table based on an input SQL select statement.

        params: {"input_database": <Workspace>, "out_layer_name": <String>, "query": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        out_layer_name = params.get("out_layer_name")
        if out_layer_name is None:
            return {"success": False, "error": "out_layer_name parameter is required"}
        query = params.get("query")
        if query is None:
            return {"success": False, "error": "query parameter is required"}
        oid_fields = params.get("oid_fields")
        shape_type = params.get("shape_type")
        srid = params.get("srid")
        spatial_reference = params.get("spatial_reference")
        spatial_properties = params.get("spatial_properties")
        m_values = params.get("m_values")
        z_values = params.get("z_values")
        extent = params.get("extent")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Make_Query_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Query Layer
            arcpy.MakeQueryLayer(input_database, out_layer_name, query, oid_fields, shape_type, srid, spatial_reference, spatial_properties, m_values, z_values, extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_query_table(self, params):
        """Make Query Table

Applies an SQL query to a database, and the results are represented in either a layer or table view. The query can be used to join several tables or return a subset of fields or rows from the original data in the database. This tool accepts data from a geodatabase or an OLE DB connection.

        params: {"in_table": <Table View; Raster Layer>, "out_table": <Table View; Raster Layer>, "in_key_field_option": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        in_key_field_option = params.get("in_key_field_option")
        if in_key_field_option is None:
            return {"success": False, "error": "in_key_field_option parameter is required"}
        in_key_field = params.get("in_key_field")
        in_field_alias = params.get("in_field_alias")
        where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Make_Query_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Query Table
            arcpy.MakeQueryTable(in_table, out_table, in_key_field_option, in_key_field, in_field_alias, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_raster_layer(self, params):
        """Make Raster Layer

Creates a raster layer from an input raster dataset or layer file. The layer created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved. This tool can be used to make a temporary layer, so you can work with a specified subset of bands within a raster dataset.

        params: {"in_raster": <Composite Geodataset>, "out_rasterlayer": <Raster Layer>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_rasterlayer = params.get("out_rasterlayer")
        if out_rasterlayer is None:
            return {"success": False, "error": "out_rasterlayer parameter is required"}
        where_clause = params.get("where_clause")
        envelope = params.get("envelope")
        band_index = params.get("band_index")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Make_Raster_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Raster Layer
            arcpy.MakeRasterLayer(in_raster, out_rasterlayer, where_clause, envelope, band_index)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_scene_layer(self, params):
        """Make Scene Layer

Creates a scene layer from a scene layer package (.slpk) or scene service.

        params: {"in_dataset": <Scene Layer; Building Scene Layer; File>, "out_layer": <Scene Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Make_Scene_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Scene Layer
            arcpy.MakeSceneLayer(in_dataset, out_layer)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_table_view(self, params):
        """Make Table View

Creates a table view from an input table or feature class. The table view that is created is temporary and will not persist after the session ends unless the document is saved.

        params: {"in_table": <Table View; Raster Layer>, "out_view": <Table View; Raster Layer>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_view = params.get("out_view")
        if out_view is None:
            return {"success": False, "error": "out_view parameter is required"}
        where_clause = params.get("where_clause")
        workspace = params.get("workspace")
        field_info = params.get("field_info")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Make_Table_View"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Table View
            arcpy.MakeTableView(in_table, out_view, where_clause, workspace, field_info)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_tin_layer(self, params):
        """Make TIN Layer

Creates a triangulated irregular network (TIN) layer from an input TIN dataset or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.

        params: {"in_tin": <TIN Layer>, "out_layer": <TIN Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_tin = params.get("in_tin")
        if in_tin is None:
            return {"success": False, "error": "in_tin parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}

            # Generate output name and path
            output_name = f"{in_tin.replace(' ', '_')}_Make_TIN_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make TIN Layer
            arcpy.MakeTINLayer(in_tin, out_layer)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_wcs_layer(self, params):
        """Make WCS Layer

Creates a temporary raster layer from a WCS service.

        params: {"out_wcs_layer": <Raster Layer>, "template": <Extent>, "band_index": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_wcs_layer = params.get("out_wcs_layer")
        if out_wcs_layer is None:
            return {"success": False, "error": "out_wcs_layer parameter is required"}
        template = params.get("template")
        band_index = params.get("band_index")

            # Generate output name and path
            output_name = f"{out_wcs_layer.replace(' ', '_')}_Make_WCS_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make WCS Layer
            arcpy.MakeWCSLayer(out_wcs_layer, template, band_index)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_xy_event_layer(self, params):
        """Make XY Event Layer

Creates a point event layer from  a table containing fields with x- and y-coordinate values, and optionally, z-coordinate (elevation) values.

        params: {"table": <Table View>, "in_x_field": <Field>, "in_y_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        table = params.get("table")
        if table is None:
            return {"success": False, "error": "table parameter is required"}
        in_x_field = params.get("in_x_field")
        if in_x_field is None:
            return {"success": False, "error": "in_x_field parameter is required"}
        in_y_field = params.get("in_y_field")
        if in_y_field is None:
            return {"success": False, "error": "in_y_field parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        spatial_reference = params.get("spatial_reference")
        in_z_field = params.get("in_z_field")

            # Generate output name and path
            output_name = f"{table.replace(' ', '_')}_Make_XY_Event_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make XY Event Layer
            arcpy.MakeXYEventLayer(table, in_x_field, in_y_field, out_layer, spatial_reference, in_z_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def match_layer_symbology_to_a_style(self, params):
        """Match Layer Symbology To A Style

Creates unique value symbology for the input layer based on the input field or expression by matching input field or expression strings to symbol names from the input style.

        params: {"in_layer": <Feature Layer>, "match_values": <Calculator Expression>, "in_style": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        match_values = params.get("match_values")
        if match_values is None:
            return {"success": False, "error": "match_values parameter is required"}
        in_style = params.get("in_style")
        if in_style is None:
            return {"success": False, "error": "in_style parameter is required"}

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Match_Layer_Symbology_To_A_Style"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Match Layer Symbology To A Style
            arcpy.MatchLayerSymbologyToAStyle(in_layer, match_values, in_style)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def save_to_layer_file(self, params):
        """Save To Layer File

Creates an output layer file (.lyrx) from a map layer. The layer file stores many properties of the input layer such as symbology, labeling, and custom pop-ups.

        params: {"in_layer": <Layer; Table View>, "out_layer": <Layer File>, "is_relative_path": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        is_relative_path = params.get("is_relative_path")
        version = params.get("version")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Save_To_Layer_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Save To Layer File
            arcpy.SaveToLayerFile(in_layer, out_layer, is_relative_path, version)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select_layer_by_attribute(self, params):
        """Select Layer By Attribute

Adds, updates, or removes a selection based on an attribute query.

        params: {"in_layer_or_view": <Table View; Raster Layer; Mosaic Layer>, "selection_type": <String>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer_or_view = params.get("in_layer_or_view")
        if in_layer_or_view is None:
            return {"success": False, "error": "in_layer_or_view parameter is required"}
        selection_type = params.get("selection_type")
        where_clause = params.get("where_clause")
        invert_where_clause = params.get("invert_where_clause")

            # Generate output name and path
            output_name = f"{in_layer_or_view.replace(' ', '_')}_Select_Layer_By_Attribute"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select Layer By Attribute
            arcpy.SelectLayerByAttribute(in_layer_or_view, selection_type, where_clause, invert_where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select_layer_by_location(self, params):
        """Select Layer By Location

Selects features  based on a spatial relationship to features in another dataset or the same dataset. Each feature in the Input Features parameter is evaluated using the features in the  Selecting Features parameter. If the specified Relationship parameter value is met, the input feature is selected. Learn more about Select By Location including image examples of relationships

        params: {"in_layer": <Feature Layer; Raster Layer; Mosaic Layer>, "overlap_type": <String>, "select_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        overlap_type = params.get("overlap_type")
        select_features = params.get("select_features")
        search_distance = params.get("search_distance")
        selection_type = params.get("selection_type")
        invert_spatial_relationship = params.get("invert_spatial_relationship")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Select_Layer_By_Location"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select Layer By Location
            arcpy.SelectLayerByLocation(in_layer, overlap_type, select_features, search_distance, selection_type, invert_spatial_relationship)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def share_package(self, params):
        """Share Package

Shares a package by uploading it to ArcGIS Online or ArcGIS Enterprise.

        params: {"in_package": <File>, "username": <String>, "password": <Encrypted String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_package = params.get("in_package")
        if in_package is None:
            return {"success": False, "error": "in_package parameter is required"}
        username = params.get("username")
        if username is None:
            return {"success": False, "error": "username parameter is required"}
        password = params.get("password")
        if password is None:
            return {"success": False, "error": "password parameter is required"}
        summary = params.get("summary")
        tags = params.get("tags")
        credits = params.get("credits")
        public = params.get("public")
        groupsgroup_name = params.get("groupsgroup_name")
        organization = params.get("organization")
        publish_web_layer = params.get("publish_web_layer")
        portal_folder = params.get("portal_folder")

            # Generate output name and path
            output_name = f"{in_package.replace(' ', '_')}_Share_Package"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Share Package
            arcpy.SharePackage(in_package, username, password, summary, tags, credits, public, groupsgroup_name, organization, publish_web_layer, portal_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def consolidate_layer(self, params):
        """Consolidate Layer

Consolidates one or more layers by copying all referenced data sources  into a single folder.

        params: {"in_layer": <Layer>, "output_folder": <Folder>, "convert_data": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        convert_data = params.get("convert_data")
        convert_arcsde_data = params.get("convert_arcsde_data")
        extent = params.get("extent")
        apply_extent_to_arcsde = params.get("apply_extent_to_arcsde")
        schema_only = params.get("schema_only")
        select_related_rows = params.get("select_related_rows")
        preserve_sqlite = params.get("preserve_sqlite")
        exclude_network_dataset = params.get("exclude_network_dataset")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Consolidate_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Consolidate Layer
            arcpy.ConsolidateLayer(in_layer, output_folder, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only, select_related_rows, preserve_sqlite, exclude_network_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def consolidate_locator(self, params):
        """Consolidate Locator

Consolidate a locator or composite locator  by copying all locators into a single folder.

        params: {"in_locator": <Address Locator>, "output_folder": <Folder>, "copy_arcsde_locator": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_locator = params.get("in_locator")
        if in_locator is None:
            return {"success": False, "error": "in_locator parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        copy_arcsde_locator = params.get("copy_arcsde_locator")

            # Generate output name and path
            output_name = f"{in_locator.replace(' ', '_')}_Consolidate_Locator"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Consolidate Locator
            arcpy.ConsolidateLocator(in_locator, output_folder, copy_arcsde_locator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def consolidate_map(self, params):
        """Consolidate Map

Consolidates a map and all referenced data sources to a specified output folder.

        params: {"in_map": <Map>, "output_folder": <Folder>, "convert_data": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        convert_data = params.get("convert_data")
        convert_arcsde_data = params.get("convert_arcsde_data")
        extent = params.get("extent")
        apply_extent_to_arcsde = params.get("apply_extent_to_arcsde")
        preserve_sqlite = params.get("preserve_sqlite")
        select_related_rows = params.get("select_related_rows")
        consolidate_to_one_fgdb = params.get("consolidate_to_one_fgdb")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Consolidate_Map"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Consolidate Map
            arcpy.ConsolidateMap(in_map, output_folder, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, preserve_sqlite, select_related_rows, consolidate_to_one_fgdb)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def consolidate_project(self, params):
        """Consolidate Project

Consolidates an ArcGIS Pro project (.aprx file) and referenced maps and data into a folder.

        params: {"in_project": <File>, "output_folder": <Folder>, "sharing_internal": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_project = params.get("in_project")
        if in_project is None:
            return {"success": False, "error": "in_project parameter is required"}
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}
        sharing_internal = params.get("sharing_internal")
        extent = params.get("extent")
        apply_extent_to_enterprise_geo = params.get("apply_extent_to_enterprise_geo")
        package_as_template = params.get("package_as_template")
        preserve_sqlite = params.get("preserve_sqlite")
        version = params.get("version")
        select_related_rows = params.get("select_related_rows")

            # Generate output name and path
            output_name = f"{in_project.replace(' ', '_')}_Consolidate_Project"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Consolidate Project
            arcpy.ConsolidateProject(in_project, output_folder, sharing_internal, extent, apply_extent_to_enterprise_geo, package_as_template, preserve_sqlite, version, select_related_rows)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_map_tile_package(self, params):
        """Create Map Tile Package

Generates tiles from a map and packages them as a single tile package or multiple smaller tile packages.

        params: {"in_map": <Map>, "service_type": <Boolean>, "output_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        service_type = params.get("service_type")
        if service_type is None:
            return {"success": False, "error": "service_type parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        format_type = params.get("format_type")
        if format_type is None:
            return {"success": False, "error": "format_type parameter is required"}
        level_of_detail = params.get("level_of_detail")
        if level_of_detail is None:
            return {"success": False, "error": "level_of_detail parameter is required"}
        service_file = params.get("service_file")
        summary = params.get("summary")
        tags = params.get("tags")
        extent = params.get("extent")
        compression_quality = params.get("compression_quality")
        package_type = params.get("package_type")
        min_level_of_detail = params.get("min_level_of_detail")
        area_of_interest = params.get("area_of_interest")
        create_multiple_packages = params.get("create_multiple_packages")
        output_folder = params.get("output_folder")
        if output_folder is None:
            return {"success": False, "error": "output_folder parameter is required"}

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Create_Map_Tile_Package"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Map Tile Package
            arcpy.CreateMapTilePackage(in_map, service_type, output_file, format_type, level_of_detail, service_file, summary, tags, extent, compression_quality, package_type, min_level_of_detail, area_of_interest, create_multiple_packages, output_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_mobile_map_package(self, params):
        """Create Mobile Map Package

Packages maps and basemaps along with all referenced data sources into a single .mmpk file.

        params: {"in_map": <Map>, "output_file": <File>, "in_locator": <Address Locator>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        in_locator = params.get("in_locator")
        area_of_interest = params.get("area_of_interest")
        extent = params.get("extent")
        clip_features = params.get("clip_features")
        title = params.get("title")
        summary = params.get("summary")
        description = params.get("description")
        tags = params.get("tags")
        credits = params.get("credits")
        use_limitations = params.get("use_limitations")
        enable_map_expiration = params.get("enable_map_expiration")
        map_expiration_type = params.get("map_expiration_type")
        expiration_date = params.get("expiration_date")
        expiration_message = params.get("expiration_message")
        select_related_rows = params.get("select_related_rows")
        reference_online_content = params.get("reference_online_content")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Create_Mobile_Map_Package"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Mobile Map Package
            arcpy.CreateMobileMapPackage(in_map, output_file, in_locator, area_of_interest, extent, clip_features, title, summary, description, tags, credits, use_limitations, enable_map_expiration, map_expiration_type, expiration_date, expiration_message, select_related_rows, reference_online_content)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_mobile_scene_package(self, params):
        """Create Mobile Scene Package

Creates a mobile scene package file (.mspk) from one or more scenes for use across the ArcGIS system.

        params: {"in_scene": <Map>, "output_file": <File>, "in_locator": <Address Locator>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_scene = params.get("in_scene")
        if in_scene is None:
            return {"success": False, "error": "in_scene parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        in_locator = params.get("in_locator")
        area_of_interest = params.get("area_of_interest")
        extent = params.get("extent")
        clip_features = params.get("clip_features")
        title = params.get("title")
        summary = params.get("summary")
        description = params.get("description")
        tags = params.get("tags")
        credits = params.get("credits")
        use_limitations = params.get("use_limitations")
        anonymous_use = params.get("anonymous_use")
        texture_optimization = params.get("texture_optimization")
        enable_scene_expiration = params.get("enable_scene_expiration")
        scene_expiration_type = params.get("scene_expiration_type")
        expiration_date = params.get("expiration_date")
        expiration_message = params.get("expiration_message")
        select_related_rows = params.get("select_related_rows")
        reference_online_content = params.get("reference_online_content")

            # Generate output name and path
            output_name = f"{in_scene.replace(' ', '_')}_Create_Mobile_Scene_Package"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Mobile Scene Package
            arcpy.CreateMobileScenePackage(in_scene, output_file, in_locator, area_of_interest, extent, clip_features, title, summary, description, tags, credits, use_limitations, anonymous_use, texture_optimization, enable_scene_expiration, scene_expiration_type, expiration_date, expiration_message, select_related_rows, reference_online_content)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_vector_tile_index(self, params):
        """Create Vector Tile Index

Creates a multiscale mesh of polygons that can be used as index polygons when creating vector tile packages.

        params: {"in_map": <Map>, "out_featureclass": <Feature Class>, "service_type": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        service_type = params.get("service_type")
        if service_type is None:
            return {"success": False, "error": "service_type parameter is required"}
        tiling_scheme = params.get("tiling_scheme")
        vertex_count = params.get("vertex_count")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Create_Vector_Tile_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Vector Tile Index
            arcpy.CreateVectorTileIndex(in_map, out_featureclass, service_type, tiling_scheme, vertex_count)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_vector_tile_package(self, params):
        """Create Vector Tile Package

Generates vector tiles from a map or basemap and packages the tiles in a single .vtpk file.

        params: {"in_map": <Map>, "output_file": <File>, "service_type": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        service_type = params.get("service_type")
        if service_type is None:
            return {"success": False, "error": "service_type parameter is required"}
        tiling_scheme = params.get("tiling_scheme")
        tile_structure = params.get("tile_structure")
        min_cached_scale = params.get("min_cached_scale")
        max_cached_scale = params.get("max_cached_scale")
        index_polygons = params.get("index_polygons")
        summary = params.get("summary")
        tags = params.get("tags")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Create_Vector_Tile_Package"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Vector Tile Package
            arcpy.CreateVectorTilePackage(in_map, output_file, service_type, tiling_scheme, tile_structure, min_cached_scale, max_cached_scale, index_polygons, summary, tags)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_package(self, params):
        """Extract Package

Extracts the contents of a package to a specified folder. The output folder will be  updated with the extracted contents of the input package.

        params: {"in_package": <File>, "output_folder": <Folder>, "cache_package": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_package = params.get("in_package")
        if in_package is None:
            return {"success": False, "error": "in_package parameter is required"}
        output_folder = params.get("output_folder")
        cache_package = params.get("cache_package")
        storage_format_type = params.get("storage_format_type")
        create_ready_to_serve_format = params.get("create_ready_to_serve_format")
        target_cloud_connection = params.get("target_cloud_connection")

            # Generate output name and path
            output_name = f"{in_package.replace(' ', '_')}_Extract_Package"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Package
            arcpy.ExtractPackage(in_package, output_folder, cache_package, storage_format_type, create_ready_to_serve_format, target_cloud_connection)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def package_3d_tiles(self, params):
        """Package 3D Tiles

Packages a 3D tiles layer or folder of 3D tiles content into a 3D tiles archive file.

        params: {"in_3dtiles": <3D Tiles Layer; Folder; Layer File>, "out_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_3dtiles = params.get("in_3dtiles")
        if in_3dtiles is None:
            return {"success": False, "error": "in_3dtiles parameter is required"}
        out_file = params.get("out_file")
        if out_file is None:
            return {"success": False, "error": "out_file parameter is required"}

            # Generate output name and path
            output_name = f"{in_3dtiles.replace(' ', '_')}_Package_3D_Tiles"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Package 3D Tiles
            arcpy.Package3DTiles(in_3dtiles, out_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def package_layer(self, params):
        """Package Layer

Packages one or more layers and all referenced data sources to create a single compressed .lpkx file.

        params: {"in_layer": <Layer; Table View>, "output_file": <File>, "convert_data": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        convert_data = params.get("convert_data")
        convert_arcsde_data = params.get("convert_arcsde_data")
        extent = params.get("extent")
        apply_extent_to_arcsde = params.get("apply_extent_to_arcsde")
        schema_only = params.get("schema_only")
        version = params.get("version")
        additional_files = params.get("additional_files")
        summary = params.get("summary")
        tags = params.get("tags")
        select_related_rows = params.get("select_related_rows")
        preserve_sqlite = params.get("preserve_sqlite")
        exclude_network_dataset = params.get("exclude_network_dataset")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Package_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Package Layer
            arcpy.PackageLayer(in_layer, output_file, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only, version, additional_files, summary, tags, select_related_rows, preserve_sqlite, exclude_network_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def package_locator(self, params):
        """Package Locator

Packages a locator or composite locator  and creates a single compressed .gcpk file. Learn more about sharing an address locator as a locator package

        params: {"in_locator": <Address Locator>, "output_file": <File>, "copy_arcsde_locator": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_locator = params.get("in_locator")
        if in_locator is None:
            return {"success": False, "error": "in_locator parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        copy_arcsde_locator = params.get("copy_arcsde_locator")
        additional_files = params.get("additional_files")
        summary = params.get("summary")
        tags = params.get("tags")

            # Generate output name and path
            output_name = f"{in_locator.replace(' ', '_')}_Package_Locator"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Package Locator
            arcpy.PackageLocator(in_locator, output_file, copy_arcsde_locator, additional_files, summary, tags)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def package_map(self, params):
        """Package Map

Packages a map and all referenced data sources to create a single compressed .mpkx file.

        params: {"in_map": <Map>, "output_file": <File>, "convert_data": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_map = params.get("in_map")
        if in_map is None:
            return {"success": False, "error": "in_map parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        convert_data = params.get("convert_data")
        convert_arcsde_data = params.get("convert_arcsde_data")
        extent = params.get("extent")
        apply_extent_to_arcsde = params.get("apply_extent_to_arcsde")
        arcgisruntime = params.get("arcgisruntime")
        reference_all_data = params.get("reference_all_data")
        version = params.get("version")
        additional_files = params.get("additional_files")
        summary = params.get("summary")
        tags = params.get("tags")
        select_related_rows = params.get("select_related_rows")
        preserve_sqlite = params.get("preserve_sqlite")
        consolidate_to_one_fgdb = params.get("consolidate_to_one_fgdb")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Package_Map"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Package Map
            arcpy.PackageMap(in_map, output_file, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, arcgisruntime, reference_all_data, version, additional_files, summary, tags, select_related_rows, preserve_sqlite, consolidate_to_one_fgdb)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def package_project(self, params):
        """Package Project

Consolidates and packages an ArcGIS Pro project (.aprx) and its contents (maps and data) to a  packaged project file (.ppkx).

        params: {"in_project": <File>, "output_file": <File>, "sharing_internal": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_project = params.get("in_project")
        if in_project is None:
            return {"success": False, "error": "in_project parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        sharing_internal = params.get("sharing_internal")
        package_as_template = params.get("package_as_template")
        extent = params.get("extent")
        apply_extent_to_arcsde = params.get("apply_extent_to_arcsde")
        additional_files = params.get("additional_files")
        summary = params.get("summary")
        tags = params.get("tags")
        version = params.get("version")
        include_toolboxes = params.get("include_toolboxes")
        include_history_items = params.get("include_history_items")
        read_only = params.get("read_only")
        select_related_rows = params.get("select_related_rows")
        preserve_sqlite = params.get("preserve_sqlite")

            # Generate output name and path
            output_name = f"{in_project.replace(' ', '_')}_Package_Project"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Package Project
            arcpy.PackageProject(in_project, output_file, sharing_internal, package_as_template, extent, apply_extent_to_arcsde, additional_files, summary, tags, version, include_toolboxes, include_history_items, read_only, select_related_rows, preserve_sqlite)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def package_result(self, params):
        """Package Result

Packages one or more geoprocessing results, including all tools and input and output datasets, into a single compressed file (.gpkx).

        params: {"in_result": <File; String>, "output_file": <File>, "convert_data": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_result = params.get("in_result")
        if in_result is None:
            return {"success": False, "error": "in_result parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        convert_data = params.get("convert_data")
        convert_arcsde_data = params.get("convert_arcsde_data")
        extent = params.get("extent")
        apply_extent_to_arcsde = params.get("apply_extent_to_arcsde")
        schema_only = params.get("schema_only")
        arcgisruntime = params.get("arcgisruntime")
        additional_files = params.get("additional_files")
        summary = params.get("summary")
        tags = params.get("tags")
        version = params.get("version")
        select_related_rows = params.get("select_related_rows")

            # Generate output name and path
            output_name = f"{in_result.replace(' ', '_')}_Package_Result"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Package Result
            arcpy.PackageResult(in_result, output_file, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only, arcgisruntime, additional_files, summary, tags, version, select_related_rows)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_3d_object_scene_layer_content(self, params):
        """Create 3D Object Scene Layer Content

Creates a scene layer package (.slpk) or scene layer content (.i3sREST) from a multipatch or 3D object feature layer input.

        params: {"in_dataset": <Layer File; Feature Layer>, "out_slpk": <File>, "out_coor_system": <Spatial Reference>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_slpk = params.get("out_slpk")
        if out_slpk is None:
            return {"success": False, "error": "out_slpk parameter is required"}
        out_coor_system = params.get("out_coor_system")
        transform_method = params.get("transform_method")
        if transform_method is None:
            return {"success": False, "error": "transform_method parameter is required"}
        texture_optimization = params.get("texture_optimization")
        target_cloud_connection = params.get("target_cloud_connection")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_3D_Object_Scene_Layer_Content"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create 3D Object Scene Layer Content
            arcpy.Create3DObjectSceneLayerContent(in_dataset, out_slpk, out_coor_system, transform_method, texture_optimization, target_cloud_connection)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_building_scene_layer_content(self, params):
        """Create Building Scene Layer Content

Creates a scene layer package (.slpk) or scene layer content (.i3sREST) from a building layer input.

        params: {"in_dataset": <Building Layer; Layer File>, "out_slpk": <File>, "out_coor_system": <Spatial Reference>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_slpk = params.get("out_slpk")
        if out_slpk is None:
            return {"success": False, "error": "out_slpk parameter is required"}
        out_coor_system = params.get("out_coor_system")
        transform_method = params.get("transform_method")
        texture_optimization = params.get("texture_optimization")
        target_cloud_connection = params.get("target_cloud_connection")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Building_Scene_Layer_Content"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Building Scene Layer Content
            arcpy.CreateBuildingSceneLayerContent(in_dataset, out_slpk, out_coor_system, transform_method, texture_optimization, target_cloud_connection)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_integrated_mesh_scene_layer_content(self, params):
        """Create Integrated Mesh Scene Layer Content

Creates  scene layer content (.slpk or .i3sREST) from OpenSceneGraph binary (OSGB) data.

        params: {"in_dataset": <File; Folder>, "out_slpk": <File>, "anchor_point": <Feature Layer; File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_slpk = params.get("out_slpk")
        anchor_point = params.get("anchor_point")
        file_suffix = params.get("file_suffix")
        out_coor_system = params.get("out_coor_system")
        max_texture_size = params.get("max_texture_size")
        texture_optimization = params.get("texture_optimization")
        target_cloud_connection = params.get("target_cloud_connection")
        out_name = params.get("out_name")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Integrated_Mesh_Scene_Layer_Content"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Integrated Mesh Scene Layer Content
            arcpy.CreateIntegratedMeshSceneLayerContent(in_dataset, out_slpk, anchor_point, file_suffix, out_coor_system, max_texture_size, texture_optimization, target_cloud_connection, out_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_point_cloud_scene_layer_content(self, params):
        """Create Point Cloud Scene Layer Content

Creates a point cloud scene layer package (.slpk) or scene layer content (.i3sREST) in the cloud from LAS, zLAS, LAZ, or LAS dataset input.

        params: {"in_dataset": <Layer File; LAS Dataset Layer; Folder; File>, "out_slpk": <File>, "out_coor_system": <Spatial Reference>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_slpk = params.get("out_slpk")
        out_coor_system = params.get("out_coor_system")
        transform_method = params.get("transform_method")
        attributes = params.get("attributes")
        point_size_m = params.get("point_size_m")
        xy_max_error_m = params.get("xy_max_error_m")
        z_max_error_m = params.get("z_max_error_m")
        in_coor_system = params.get("in_coor_system")
        scene_layer_version = params.get("scene_layer_version")
        target_cloud_connection = params.get("target_cloud_connection")
        out_name = params.get("out_name")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Point_Cloud_Scene_Layer_Content"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Point Cloud Scene Layer Content
            arcpy.CreatePointCloudSceneLayerContent(in_dataset, out_slpk, out_coor_system, transform_method, attributes, point_size_m, xy_max_error_m, z_max_error_m, in_coor_system, scene_layer_version, target_cloud_connection, out_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_point_scene_layer_content(self, params):
        """Create Point Scene Layer Content

Creates a point scene layer package (.slpk) or scene layer content (.i3sREST) from a point feature layer.

        params: {"in_dataset": <Layer File; Feature Layer>, "out_slpk": <File>, "out_coor_system": <Spatial Reference>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_slpk = params.get("out_slpk")
        if out_slpk is None:
            return {"success": False, "error": "out_slpk parameter is required"}
        out_coor_system = params.get("out_coor_system")
        transform_method = params.get("transform_method")
        target_cloud_connection = params.get("target_cloud_connection")
        support_symbol_referencing = params.get("support_symbol_referencing")
        if support_symbol_referencing is None:
            return {"success": False, "error": "support_symbol_referencing parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Point_Scene_Layer_Content"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Point Scene Layer Content
            arcpy.CreatePointSceneLayerContent(in_dataset, out_slpk, out_coor_system, transform_method, target_cloud_connection, support_symbol_referencing)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_voxel_scene_layer_content(self, params):
        """Create Voxel Scene Layer Content

Creates a scene layer package (.slpk file) from a voxel layer input.

        params: {"in_dataset": <Voxel Layer; Layer File>, "out_slpk": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_slpk = params.get("out_slpk")
        if out_slpk is None:
            return {"success": False, "error": "out_slpk parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Voxel_Scene_Layer_Content"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Voxel Scene Layer Content
            arcpy.CreateVoxelSceneLayerContent(in_dataset, out_slpk)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_level_of_detail(self, params):
        """Generate Level of Detail

Generates a new scene layer package with properly defined levels of detail. Only the finest level of detail is maintained; all other levels of detail are discarded. The finest level of detail is reorganized into  tiles that generate new coarse levels of detail.

        params: {"in_dataset": <File>, "out_dataset": <File>, "texture_optimization": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_dataset = params.get("out_dataset")
        if out_dataset is None:
            return {"success": False, "error": "out_dataset parameter is required"}
        texture_optimization = params.get("texture_optimization")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Generate_Level_of_Detail"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Level of Detail
            arcpy.GenerateLevelofDetail(in_dataset, out_dataset, texture_optimization)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def upgrade_scene_layer(self, params):
        """Upgrade Scene Layer

Upgrades a scene layer package to the current I3S version in SLPK format or output to i3sREST  format for use in ArcGIS Enterprise.

        params: {"in_dataset": <File>, "out_folder_path": <Folder>, "out_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        out_log = params.get("out_log")
        texture_optimization = params.get("texture_optimization")
        date_format = params.get("date_format")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Upgrade_Scene_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Upgrade Scene Layer
            arcpy.UpgradeSceneLayer(in_dataset, out_folder_path, out_name, out_log, texture_optimization, date_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def validate_scene_layer(self, params):
        """Validate Scene Layer

Evaluates a scene layer package (*.slpk or *.i3sREST) in a cloud store to determine its conformity to I3S specifications.

        params: {"in_slpk": <File>, "out_report": <File>, "in_folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_slpk = params.get("in_slpk")
        out_report = params.get("out_report")
        if out_report is None:
            return {"success": False, "error": "out_report parameter is required"}
        in_folder = params.get("in_folder")

            # Generate output name and path
            output_name = f"{out_report.replace(' ', '_')}_Validate_Scene_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Validate Scene Layer
            arcpy.ValidateSceneLayer(in_slpk, out_report, in_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def geotagged_photos_to_points(self, params):
        """GeoTagged Photos To Points

Creates points from the x-, y-, and z-coordinates stored in the metadata of geotagged photo files (.jpg or .tif). You can  add the photo files to the output features as geodatabase attachments.

        params: {"input_folder": <Folder>, "output_feature_class": <Feature Class>, "invalid_photos_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_folder = params.get("input_folder")
        if input_folder is None:
            return {"success": False, "error": "input_folder parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        invalid_photos_table = params.get("invalid_photos_table")
        include_non_geotagged_photos = params.get("include_non_geotagged_photos")
        add_photos_attachments = params.get("add_photos_attachments")

            # Generate output name and path
            output_name = f"{input_folder.replace(' ', '_')}_GeoTagged_Photos_To_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GeoTagged Photos To Points
            arcpy.GeoTaggedPhotosToPoints(input_folder, output_feature_class, invalid_photos_table, include_non_geotagged_photos, add_photos_attachments)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def match_photos_to_rows_by_time(self, params):
        """Match Photos To Rows By Time

Matches photo files to table or feature class rows according to the photo and row time stamps. The row with the time stamp closest to the capture time of a photo will be matched to that photo. A new table is created that contains the object ID values from the input rows and their matching photo paths. You can also use this tool to add matching photo files to the rows of the input table as geodatabase attachments.

        params: {"input_folder": <Folder>, "input_table": <Table View>, "time_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_folder = params.get("input_folder")
        if input_folder is None:
            return {"success": False, "error": "input_folder parameter is required"}
        input_table = params.get("input_table")
        if input_table is None:
            return {"success": False, "error": "input_table parameter is required"}
        time_field = params.get("time_field")
        if time_field is None:
            return {"success": False, "error": "time_field parameter is required"}
        output_table = params.get("output_table")
        if output_table is None:
            return {"success": False, "error": "output_table parameter is required"}
        unmatched_photos_table = params.get("unmatched_photos_table")
        add_photos_attachments = params.get("add_photos_attachments")
        time_tolerance = params.get("time_tolerance")
        clock_offset = params.get("clock_offset")

            # Generate output name and path
            output_name = f"{input_folder.replace(' ', '_')}_Match_Photos_To_Rows_By_Time"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Match Photos To Rows By Time
            arcpy.MatchPhotosToRowsByTime(input_folder, input_table, time_field, output_table, unmatched_photos_table, add_photos_attachments, time_tolerance, clock_offset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def batch_project(self, params):
        """Batch Project

Changes the coordinate system of a set of input feature classes or feature datasets to a common coordinate system. To change the coordinate system of a single feature class or dataset use the Project tool.

        params: {"input_feature_class_or_dataset": <Feature Layer; Feature Dataset>, "output_workspace": <Feature Dataset; Workspace>, "output_coordinate_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class_or_dataset = params.get("input_feature_class_or_dataset")
        if input_feature_class_or_dataset is None:
            return {"success": False, "error": "input_feature_class_or_dataset parameter is required"}
        output_workspace = params.get("output_workspace")
        if output_workspace is None:
            return {"success": False, "error": "output_workspace parameter is required"}
        output_coordinate_system = params.get("output_coordinate_system")
        template_dataset = params.get("template_dataset")
        transformation = params.get("transformation")

            # Generate output name and path
            output_name = f"{input_feature_class_or_dataset.replace(' ', '_')}_Batch_Project"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Batch Project
            arcpy.BatchProject(input_feature_class_or_dataset, output_workspace, output_coordinate_system, template_dataset, transformation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def project(self, params):
        """Project

Projects spatial data from one coordinate system to another.

        params: {"in_dataset": <Feature Layer; Feature Dataset; Scene Layer; Building Scene Layer; File>, "out_dataset": <Feature Class; Feature Dataset; File>, "out_coor_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_dataset = params.get("out_dataset")
        if out_dataset is None:
            return {"success": False, "error": "out_dataset parameter is required"}
        out_coor_system = params.get("out_coor_system")
        if out_coor_system is None:
            return {"success": False, "error": "out_coor_system parameter is required"}
        transform_method = params.get("transform_method")
        in_coor_system = params.get("in_coor_system")
        preserve_shape = params.get("preserve_shape")
        max_deviation = params.get("max_deviation")
        vertical = params.get("vertical")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Project"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Project
            arcpy.Project(in_dataset, out_dataset, out_coor_system, transform_method, in_coor_system, preserve_shape, max_deviation, vertical)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_coordinate_notation(self, params):
        """Convert Coordinate Notation

Converts coordinate notations contained in one or two fields from one notation format to another. Learn more about supported notation formats

        params: {"in_table": <Table View>, "out_featureclass": <Feature Class>, "x_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        x_field = params.get("x_field")
        if x_field is None:
            return {"success": False, "error": "x_field parameter is required"}
        y_field = params.get("y_field")
        if y_field is None:
            return {"success": False, "error": "y_field parameter is required"}
        input_coordinate_format = params.get("input_coordinate_format")
        if input_coordinate_format is None:
            return {"success": False, "error": "input_coordinate_format parameter is required"}
        output_coordinate_format = params.get("output_coordinate_format")
        if output_coordinate_format is None:
            return {"success": False, "error": "output_coordinate_format parameter is required"}
        id_field = params.get("id_field")
        spatial_reference = params.get("spatial_reference")
        in_coor_system = params.get("in_coor_system")
        exclude_invalid_records = params.get("exclude_invalid_records")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Convert_Coordinate_Notation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Coordinate Notation
            arcpy.ConvertCoordinateNotation(in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, id_field, spatial_reference, in_coor_system, exclude_invalid_records)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_custom_geographic_transformation(self, params):
        """Create Custom Geographic Transformation

Creates a transformation definition for converting data between two geographic coordinate systems or datums. The output of this tool can be used as a transformation for any tool with a parameter that requires a geographic transformation.

        params: {"geot_name": <String>, "in_coor_system": <Coordinate System>, "out_coor_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        geot_name = params.get("geot_name")
        if geot_name is None:
            return {"success": False, "error": "geot_name parameter is required"}
        in_coor_system = params.get("in_coor_system")
        if in_coor_system is None:
            return {"success": False, "error": "in_coor_system parameter is required"}
        out_coor_system = params.get("out_coor_system")
        if out_coor_system is None:
            return {"success": False, "error": "out_coor_system parameter is required"}
        custom_geot = params.get("custom_geot")
        if custom_geot is None:
            return {"success": False, "error": "custom_geot parameter is required"}
        extent = params.get("extent")
        accuracy = params.get("accuracy")

            # Generate output name and path
            output_name = f"{geot_name.replace(' ', '_')}_Create_Custom_Geographic_Transformation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Custom Geographic Transformation
            arcpy.CreateCustomGeographicTransformation(geot_name, in_coor_system, out_coor_system, custom_geot, extent, accuracy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_custom_vertical_transformation(self, params):
        """Create Custom Vertical Transformation

Creates a transformation definition for converting data between two vertical coordinate systems or datums. The output of this tool can be used as a transformation object for any tool with a parameter that requires a vertical transformation.

        params: {"vt_name": <String>, "source_vt_coor_system": <String>, "target_vt_coor_system": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        vt_name = params.get("vt_name")
        if vt_name is None:
            return {"success": False, "error": "vt_name parameter is required"}
        source_vt_coor_system = params.get("source_vt_coor_system")
        if source_vt_coor_system is None:
            return {"success": False, "error": "source_vt_coor_system parameter is required"}
        target_vt_coor_system = params.get("target_vt_coor_system")
        if target_vt_coor_system is None:
            return {"success": False, "error": "target_vt_coor_system parameter is required"}
        interpolation_gcs = params.get("interpolation_gcs")
        custom_vt = params.get("custom_vt")
        extent = params.get("extent")
        accuracy = params.get("accuracy")

            # Generate output name and path
            output_name = f"{vt_name.replace(' ', '_')}_Create_Custom_Vertical_Transformation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Custom Vertical Transformation
            arcpy.CreateCustomVerticalTransformation(vt_name, source_vt_coor_system, target_vt_coor_system, interpolation_gcs, custom_vt, extent, accuracy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_spatial_reference(self, params):
        """Create Spatial Reference

Creates a spatial reference for use in ModelBuilder.

        params: {"spatial_reference": <Spatial Reference>, "spatial_reference_template": <Feature Layer; Raster Dataset>, "xy_domain": <Envelope>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        spatial_reference = params.get("spatial_reference")
        spatial_reference_template = params.get("spatial_reference_template")
        xy_domain = params.get("xy_domain")
        z_domain = params.get("z_domain")
        m_domain = params.get("m_domain")
        template = params.get("template")
        expand_ratio = params.get("expand_ratio")

            # Generate output name and path
            output_name = f"{params.replace(' ', '_')}_Create_Spatial_Reference"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Spatial Reference
            arcpy.CreateSpatialReference(spatial_reference, spatial_reference_template, xy_domain, z_domain, m_domain, template, expand_ratio)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def define_projection(self, params):
        """Define Projection

Overwrites the coordinate system information (map projection and datum) stored with a dataset. This tool is intended for datasets that have an unknown or incorrect coordinate system defined.

        params: {"in_dataset": <Feature Layer; Geodataset>, "coor_system": <Coordinate System>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        coor_system = params.get("coor_system")
        if coor_system is None:
            return {"success": False, "error": "coor_system parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Define_Projection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Define Projection
            arcpy.DefineProjection(in_dataset, coor_system)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def flip(self, params):
        """Flip

Reorients the raster by turning it over, from top to bottom, along the horizontal axis through the center of the raster. This may be useful to correct raster datasets that are upside down.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Flip"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flip
            arcpy.Flip(in_raster, out_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mirror(self, params):
        """Mirror

Reorients the raster by turning it over, from left to right, along the vertical axis through the center of the raster.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Mirror"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mirror
            arcpy.Mirror(in_raster, out_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def project_raster(self, params):
        """Project Raster

Transforms a raster dataset from one coordinate system to another. Learn more about how Project Raster works

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>, "out_coor_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        out_coor_system = params.get("out_coor_system")
        if out_coor_system is None:
            return {"success": False, "error": "out_coor_system parameter is required"}
        resampling_type = params.get("resampling_type")
        cell_size = params.get("cell_size")
        geographic_transform = params.get("geographic_transform")
        registration_point = params.get("registration_point")
        in_coor_system = params.get("in_coor_system")
        vertical = params.get("vertical")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Project_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Project Raster
            arcpy.ProjectRaster(in_raster, out_raster, out_coor_system, resampling_type, cell_size, geographic_transform, registration_point, in_coor_system, vertical)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def register_raster(self, params):
        """Register Raster

Automatically aligns a raster to a reference image or uses a control point file for georegistration. If the input dataset is a mosaic dataset, the tool will operate on each mosaic dataset item. To automatically register the image, the input raster and the reference raster must be in a relatively close geographic area. The tool will run faster if the raster datasets are in close alignment. You may need to create a link file, also known as a control point file, with a few links to get your input raster into the same map space.

        params: {"in_raster": <Mosaic Layer; Raster Dataset; Raster Layer>, "register_mode": <String>, "reference_raster": <Image Service; Internet Tiled Layer; Map Server Layer; Map Server; Mosaic Layer; Raster Dataset; Raster Layer; WMS Map>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        register_mode = params.get("register_mode")
        if register_mode is None:
            return {"success": False, "error": "register_mode parameter is required"}
        reference_raster = params.get("reference_raster")
        input_link_file = params.get("input_link_file")
        transformation_type = params.get("transformation_type")
        output_cpt_link_file = params.get("output_cpt_link_file")
        maximum_rms_value = params.get("maximum_rms_value")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Register_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Register Raster
            arcpy.RegisterRaster(in_raster, register_mode, reference_raster, input_link_file, transformation_type, output_cpt_link_file, maximum_rms_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rescale(self, params):
        """Rescale

Resizes a raster by the specified x and y scale factors.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>, "x_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        x_scale = params.get("x_scale")
        if x_scale is None:
            return {"success": False, "error": "x_scale parameter is required"}
        y_scale = params.get("y_scale")
        if y_scale is None:
            return {"success": False, "error": "y_scale parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Rescale"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rescale
            arcpy.Rescale(in_raster, out_raster, x_scale, y_scale)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rotate(self, params):
        """Rotate

Turns a raster dataset around a specified pivot point.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>, "angle": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        angle = params.get("angle")
        if angle is None:
            return {"success": False, "error": "angle parameter is required"}
        pivot_point = params.get("pivot_point")
        resampling_type = params.get("resampling_type")
        clipping_extent = params.get("clipping_extent")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Rotate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rotate
            arcpy.Rotate(in_raster, out_raster, angle, pivot_point, resampling_type, clipping_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def shift(self, params):
        """Shift

Moves (slides) the raster to a new geographic location based on x and y shift values. This tool is helpful if your raster dataset needs to be shifted to align with another data file.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>, "x_value": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        x_value = params.get("x_value")
        if x_value is None:
            return {"success": False, "error": "x_value parameter is required"}
        y_value = params.get("y_value")
        if y_value is None:
            return {"success": False, "error": "y_value parameter is required"}
        in_snap_raster = params.get("in_snap_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Shift"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Shift
            arcpy.Shift(in_raster, out_raster, x_value, y_value, in_snap_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def warp(self, params):
        """Warp

Transforms a raster dataset using source and target control points. This is similar to georeferencing.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "source_control_pointssource_control_point": <Point>, "target_control_pointstarget_control_point": <Point>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        source_control_pointssource_control_point = params.get("source_control_pointssource_control_point")
        if source_control_pointssource_control_point is None:
            return {"success": False, "error": "source_control_pointssource_control_point parameter is required"}
        target_control_pointstarget_control_point = params.get("target_control_pointstarget_control_point")
        if target_control_pointstarget_control_point is None:
            return {"success": False, "error": "target_control_pointstarget_control_point parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        transformation_type = params.get("transformation_type")
        resampling_type = params.get("resampling_type")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Warp"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Warp
            arcpy.Warp(in_raster, source_control_pointssource_control_point, target_control_pointstarget_control_point, out_raster, transformation_type, resampling_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def warp_from_file(self, params):
        """Warp From File

Transforms a raster dataset using an existing text file containing source and target control points.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "out_raster": <Raster Dataset>, "link_file": <Text File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        link_file = params.get("link_file")
        if link_file is None:
            return {"success": False, "error": "link_file parameter is required"}
        transformation_type = params.get("transformation_type")
        resampling_type = params.get("resampling_type")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Warp_From_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Warp From File
            arcpy.WarpFromFile(in_raster, out_raster, link_file, transformation_type, resampling_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def clip(self, params):
        """Clip

Cuts out a portion of a raster dataset, mosaic dataset, or image service layer.

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Dataset; Raster Layer>, "rectangle": <Envelope; Feature Class; Feature Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        rectangle = params.get("rectangle")
        if rectangle is None:
            return {"success": False, "error": "rectangle parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        in_template_dataset = params.get("in_template_dataset")
        nodata_value = params.get("nodata_value")
        clipping_geometry = params.get("clipping_geometry")
        maintain_clipping_extent = params.get("maintain_clipping_extent")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Clip"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Clip
            arcpy.Clip(in_raster, rectangle, out_raster, in_template_dataset, nodata_value, clipping_geometry, maintain_clipping_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_rasters_to_mosaic_dataset(self, params):
        """Add Rasters To Mosaic Dataset

Adds raster datasets to a mosaic dataset from various sources, including a file, folder, table, or web service.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "raster_type": <Raster Type>, "input_path": <File; Image Service; LAS Dataset Layer; Layer File; Map Server; Mosaic Layer; Raster Layer; Table View; Terrain Layer; WCS Coverage; WMS Map; Workspace>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        raster_type = params.get("raster_type")
        if raster_type is None:
            return {"success": False, "error": "raster_type parameter is required"}
        input_path = params.get("input_path")
        if input_path is None:
            return {"success": False, "error": "input_path parameter is required"}
        update_cellsize_ranges = params.get("update_cellsize_ranges")
        update_boundary = params.get("update_boundary")
        update_overviews = params.get("update_overviews")
        maximum_pyramid_levels = params.get("maximum_pyramid_levels")
        maximum_cell_size = params.get("maximum_cell_size")
        minimum_dimension = params.get("minimum_dimension")
        spatial_reference = params.get("spatial_reference")
        filter = params.get("filter")
        sub_folder = params.get("sub_folder")
        duplicate_items_action = params.get("duplicate_items_action")
        build_pyramids = params.get("build_pyramids")
        calculate_statistics = params.get("calculate_statistics")
        build_thumbnails = params.get("build_thumbnails")
        operation_description = params.get("operation_description")
        force_spatial_reference = params.get("force_spatial_reference")
        estimate_statistics = params.get("estimate_statistics")
        enable_pixel_cache = params.get("enable_pixel_cache")
        cache_location = params.get("cache_location")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Add_Rasters_To_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Rasters To Mosaic Dataset
            arcpy.AddRastersToMosaicDataset(in_mosaic_dataset, raster_type, input_path, update_cellsize_ranges, update_boundary, update_overviews, maximum_pyramid_levels, maximum_cell_size, minimum_dimension, spatial_reference, filter, sub_folder, duplicate_items_action, build_pyramids, calculate_statistics, build_thumbnails, operation_description, force_spatial_reference, estimate_statistics, enable_pixel_cache, cache_location)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_mosaic_dataset_schema(self, params):
        """Alter Mosaic Dataset Schema

Defines the editing operations that nonowners  have when editing a mosaic dataset in an enterprise geodatabase. This tool prevents schema-locking issues that can occur when a mosaic dataset is stored in an enterprise geodatabase. The owner of the geodatabase runs this tool to create side tables and fields that may be needed by the user. The owner must also  grant the proper permissions to allow users to insert, update, or delete records.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "side_tablesoperation": <String>, "raster_type_namesraster_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        side_tablesoperation = params.get("side_tablesoperation")
        raster_type_namesraster_type = params.get("raster_type_namesraster_type")
        editor_tracking = params.get("editor_tracking")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Alter_Mosaic_Dataset_Schema"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Alter Mosaic Dataset Schema
            arcpy.AlterMosaicDatasetSchema(in_mosaic_dataset, side_tablesoperation, raster_type_namesraster_type, editor_tracking)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze_mosaic_dataset(self, params):
        """Analyze Mosaic Dataset

Performs checks on a mosaic dataset for errors and possible improvements.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "checker_keywords": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        checker_keywords = params.get("checker_keywords")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Analyze_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Analyze Mosaic Dataset
            arcpy.AnalyzeMosaicDataset(in_mosaic_dataset, where_clause, checker_keywords)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_boundary(self, params):
        """Build Boundary

Updates the extent of the boundary when adding new raster datasets to a mosaic dataset that extend beyond its previous coverage.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "append_to_existing": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        append_to_existing = params.get("append_to_existing")
        simplification_method = params.get("simplification_method")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Build_Boundary"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Boundary
            arcpy.BuildBoundary(in_mosaic_dataset, where_clause, append_to_existing, simplification_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_footprints(self, params):
        """Build Footprints

Computes the extent of every raster in a mosaic dataset. This tool is used when you have added or removed raster datasets from a mosaic dataset and want to recompute the footprints.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "reset_footprint": <Boolean; String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        reset_footprint = params.get("reset_footprint")
        min_data_value = params.get("min_data_value")
        max_data_value = params.get("max_data_value")
        approx_num_vertices = params.get("approx_num_vertices")
        shrink_distance = params.get("shrink_distance")
        maintain_edges = params.get("maintain_edges")
        skip_derived_images = params.get("skip_derived_images")
        update_boundary = params.get("update_boundary")
        request_size = params.get("request_size")
        min_region_size = params.get("min_region_size")
        simplification_method = params.get("simplification_method")
        edge_tolerance = params.get("edge_tolerance")
        max_sliver_size = params.get("max_sliver_size")
        min_thinness_ratio = params.get("min_thinness_ratio")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Build_Footprints"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Footprints
            arcpy.BuildFootprints(in_mosaic_dataset, where_clause, reset_footprint, min_data_value, max_data_value, approx_num_vertices, shrink_distance, maintain_edges, skip_derived_images, update_boundary, request_size, min_region_size, simplification_method, edge_tolerance, max_sliver_size, min_thinness_ratio)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_mosaic_dataset_item_cache(self, params):
        """Build Mosaic Dataset Item Cache

Inserts the Cached Raster function as the final step in all function chains within a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "define_cache": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        define_cache = params.get("define_cache")
        generate_cache = params.get("generate_cache")
        item_cache_folder = params.get("item_cache_folder")
        compression_method = params.get("compression_method")
        compression_quality = params.get("compression_quality")
        max_allowed_rows = params.get("max_allowed_rows")
        max_allowed_columns = params.get("max_allowed_columns")
        request_size_type = params.get("request_size_type")
        request_size = params.get("request_size")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Build_Mosaic_Dataset_Item_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Mosaic Dataset Item Cache
            arcpy.BuildMosaicDatasetItemCache(in_mosaic_dataset, where_clause, define_cache, generate_cache, item_cache_folder, compression_method, compression_quality, max_allowed_rows, max_allowed_columns, request_size_type, request_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_overviews(self, params):
        """Build Overviews

Defines and generates overviews on a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "define_missing_tiles": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        define_missing_tiles = params.get("define_missing_tiles")
        generate_overviews = params.get("generate_overviews")
        generate_missing_images = params.get("generate_missing_images")
        regenerate_stale_images = params.get("regenerate_stale_images")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Build_Overviews"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Overviews
            arcpy.BuildOverviews(in_mosaic_dataset, where_clause, define_missing_tiles, generate_overviews, generate_missing_images, regenerate_stale_images)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_seamlines(self, params):
        """Build Seamlines

Generate or update seamlines for your mosaic dataset. Seamlines are used to sort overlapping imagery and produce a smoother-looking mosaic. You can use this tool to do the following:

        params: {"in_mosaic_dataset": <Mosaic Layer>, "cell_size": <Double>, "sort_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        cell_size = params.get("cell_size")
        if cell_size is None:
            return {"success": False, "error": "cell_size parameter is required"}
        sort_method = params.get("sort_method")
        sort_order = params.get("sort_order")
        order_by_attribute = params.get("order_by_attribute")
        order_by_base_value = params.get("order_by_base_value")
        view_point = params.get("view_point")
        computation_method = params.get("computation_method")
        blend_width = params.get("blend_width")
        blend_type = params.get("blend_type")
        request_size = params.get("request_size")
        request_size_type = params.get("request_size_type")
        blend_width_units = params.get("blend_width_units")
        area_of_interest = params.get("area_of_interest")
        where_clause = params.get("where_clause")
        update_existing = params.get("update_existing")
        min_region_size = params.get("min_region_size")
        min_thinness_ratio = params.get("min_thinness_ratio")
        max_sliver_size = params.get("max_sliver_size")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Build_Seamlines"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Seamlines
            arcpy.BuildSeamlines(in_mosaic_dataset, cell_size, sort_method, sort_order, order_by_attribute, order_by_base_value, view_point, computation_method, blend_width, blend_type, request_size, request_size_type, blend_width_units, area_of_interest, where_clause, update_existing, min_region_size, min_thinness_ratio, max_sliver_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_cell_size_ranges(self, params):
        """Calculate Cell Size Ranges

Computes the visibility levels of raster datasets in a mosaic dataset based on the spatial resolution.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "do_compute_min": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        do_compute_min = params.get("do_compute_min")
        do_compute_max = params.get("do_compute_max")
        max_range_factor = params.get("max_range_factor")
        cell_size_tolerance_factor = params.get("cell_size_tolerance_factor")
        update_missing_only = params.get("update_missing_only")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Calculate_Cell_Size_Ranges"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Cell Size Ranges
            arcpy.CalculateCellSizeRanges(in_mosaic_dataset, where_clause, do_compute_min, do_compute_max, max_range_factor, cell_size_tolerance_factor, update_missing_only)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def clear_pixel_cache(self, params):
        """Clear Pixel Cache

Clears the pixel cache associated with a mosaic dataset. The pixel cache for a mosaic dataset can be generated by running the Add Rasters to Mosaic Dataset tool with the Enable Pixel Cache parameter checked. The pixel cache improves the performance when viewing and performing analysis on a mosaic that references rasters on cloud or slow Network  Attached  Storage  (NAS). The cache is stored on the local machine, improving performance.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "generated_before": <Date>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        generated_before = params.get("generated_before")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Clear_Pixel_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Clear Pixel Cache
            arcpy.ClearPixelCache(in_mosaic_dataset, generated_before)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def color_balance_mosaic_dataset(self, params):
        """Color Balance Mosaic Dataset

Color balances a mosaic dataset so that the tiles appear seamless.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "balancing_method": <String>, "color_surface_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        balancing_method = params.get("balancing_method")
        color_surface_type = params.get("color_surface_type")
        target_raster = params.get("target_raster")
        exclude_raster = params.get("exclude_raster")
        stretch_type = params.get("stretch_type")
        gamma = params.get("gamma")
        block_field = params.get("block_field")
        in_dem_raster = params.get("in_dem_raster")
        zfactor = params.get("zfactor")
        zoffset = params.get("zoffset")
        geoid = params.get("geoid")
        solution_points = params.get("solution_points")
        target_objectid = params.get("target_objectid")
        refine_estimation = params.get("refine_estimation")
        reduce_shadow = params.get("reduce_shadow")
        reduce_cloud = params.get("reduce_cloud")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Color_Balance_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Color Balance Mosaic Dataset
            arcpy.ColorBalanceMosaicDataset(in_mosaic_dataset, balancing_method, color_surface_type, target_raster, exclude_raster, stretch_type, gamma, block_field, in_dem_raster, zfactor, zoffset, geoid, solution_points, target_objectid, refine_estimation, reduce_shadow, reduce_cloud)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_dirty_area(self, params):
        """Compute Dirty Area

Identifies areas within a mosaic dataset that have changed since a specified point in time. This is used commonly when a mosaic dataset is updated or synchronized, or when  derived products, such as cache, need to be updated. This tool will enable you to limit such processes to only the areas that have changed.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "timestamp": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        timestamp = params.get("timestamp")
        if timestamp is None:
            return {"success": False, "error": "timestamp parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Dirty_Area"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Dirty Area
            arcpy.ComputeDirtyArea(in_mosaic_dataset, where_clause, timestamp, out_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_mosaic_candidates(self, params):
        """Compute Mosaic Candidates

Finds the image candidates in a mosaic dataset that best represent the mosaic area. Densely overlapped images are necessary in many projects but may make it difficult to determine which images in a mosaic dataset should be used in an analysis. This tool finds the optimal images based on areas of maximum overlap and area excluded. The input mosaic dataset will include a new Candidate field in the mosaic dataset footprint table. This field determines which images will be used in certain operations, such as color balancing,  seamline generation, ortho mapping, and mosaic methods.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "maximum_overlap": <Double>, "maximum_area_loss": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        maximum_overlap = params.get("maximum_overlap")
        maximum_area_loss = params.get("maximum_area_loss")
        maximum_obliqueness_angle = params.get("maximum_obliqueness_angle")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Mosaic_Candidates"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Mosaic Candidates
            arcpy.ComputeMosaicCandidates(in_mosaic_dataset, maximum_overlap, maximum_area_loss, maximum_obliqueness_angle)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_mosaic_dataset(self, params):
        """Create Mosaic Dataset

Creates an empty mosaic dataset in a geodatabase.

        params: {"in_workspace": <Workspace>, "in_mosaicdataset_name": <String>, "coordinate_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        in_mosaicdataset_name = params.get("in_mosaicdataset_name")
        if in_mosaicdataset_name is None:
            return {"success": False, "error": "in_mosaicdataset_name parameter is required"}
        coordinate_system = params.get("coordinate_system")
        if coordinate_system is None:
            return {"success": False, "error": "coordinate_system parameter is required"}
        num_bands = params.get("num_bands")
        pixel_type = params.get("pixel_type")
        product_definition = params.get("product_definition")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Create_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Mosaic Dataset
            arcpy.CreateMosaicDataset(in_workspace, in_mosaicdataset_name, coordinate_system, num_bands, pixel_type, product_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_referenced_mosaic_dataset(self, params):
        """Create Referenced Mosaic Dataset

Creates a separate mosaic dataset from items in an existing mosaic dataset.

        params: {"in_dataset": <Mosaic Layer; Mosaic Dataset>, "out_mosaic_dataset": <Mosaic Dataset>, "coordinate_system": <Coordinate System>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_mosaic_dataset = params.get("out_mosaic_dataset")
        if out_mosaic_dataset is None:
            return {"success": False, "error": "out_mosaic_dataset parameter is required"}
        coordinate_system = params.get("coordinate_system")
        number_of_bands = params.get("number_of_bands")
        pixel_type = params.get("pixel_type")
        where_clause = params.get("where_clause")
        in_template_dataset = params.get("in_template_dataset")
        extent = params.get("extent")
        select_using_features = params.get("select_using_features")
        lod_field = params.get("lod_field")
        minps_field = params.get("minps_field")
        maxps_field = params.get("maxps_field")
        pixelsize = params.get("pixelsize")
        build_boundary = params.get("build_boundary")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Referenced_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Referenced Mosaic Dataset
            arcpy.CreateReferencedMosaicDataset(in_dataset, out_mosaic_dataset, coordinate_system, number_of_bands, pixel_type, where_clause, in_template_dataset, extent, select_using_features, lod_field, minps_field, maxps_field, pixelsize, build_boundary)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def define_mosaic_dataset_nodata(self, params):
        """Define Mosaic Dataset NoData

Specifies one or more values to be represented as NoData.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "num_bands": <Long>, "bands_for_nodata_valueband_nodata_value": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        num_bands = params.get("num_bands")
        if num_bands is None:
            return {"success": False, "error": "num_bands parameter is required"}
        bands_for_nodata_valueband_nodata_value = params.get("bands_for_nodata_valueband_nodata_value")
        bands_for_valid_data_rangeband_minimum_value_maximum_value = params.get("bands_for_valid_data_rangeband_minimum_value_maximum_value")
        where_clause = params.get("where_clause")
        composite_nodata_value = params.get("composite_nodata_value")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Define_Mosaic_Dataset_NoData"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Define Mosaic Dataset NoData
            arcpy.DefineMosaicDatasetNoData(in_mosaic_dataset, num_bands, bands_for_nodata_valueband_nodata_value, bands_for_valid_data_rangeband_minimum_value_maximum_value, where_clause, composite_nodata_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def define_overviews(self, params):
        """Define Overviews

Lets you set how mosaic dataset overviews are generated. The settings made with this tool are used by the Build Overviews tool.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "overview_image_folder": <Workspace>, "in_template_dataset": <Raster Layer; Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        overview_image_folder = params.get("overview_image_folder")
        in_template_dataset = params.get("in_template_dataset")
        extent = params.get("extent")
        pixel_size = params.get("pixel_size")
        number_of_levels = params.get("number_of_levels")
        tile_rows = params.get("tile_rows")
        tile_cols = params.get("tile_cols")
        overview_factor = params.get("overview_factor")
        force_overview_tiles = params.get("force_overview_tiles")
        resampling_method = params.get("resampling_method")
        compression_method = params.get("compression_method")
        compression_quality = params.get("compression_quality")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Define_Overviews"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Define Overviews
            arcpy.DefineOverviews(in_mosaic_dataset, overview_image_folder, in_template_dataset, extent, pixel_size, number_of_levels, tile_rows, tile_cols, overview_factor, force_overview_tiles, resampling_method, compression_method, compression_quality)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_mosaic_dataset(self, params):
        """Delete Mosaic Dataset

Deletes a mosaic dataset, its overviews, and its item cache from disk.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "delete_overview_images": <Boolean>, "delete_item_cache": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        delete_overview_images = params.get("delete_overview_images")
        delete_item_cache = params.get("delete_item_cache")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Delete_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Mosaic Dataset
            arcpy.DeleteMosaicDataset(in_mosaic_dataset, delete_overview_images, delete_item_cache)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def edit_raster_function(self, params):
        """Edit Raster Function

Adds, replaces, or removes a function chain in a mosaic dataset or a raster layer that contains a raster function.

        params: {"in_mosaic_dataset": <Mosaic Layer; Raster Layer>, "edit_mosaic_dataset_item": <Boolean>, "function_chain_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        edit_mosaic_dataset_item = params.get("edit_mosaic_dataset_item")
        function_chain_definition = params.get("function_chain_definition")
        location_function_name = params.get("location_function_name")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Edit_Raster_Function"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Edit Raster Function
            arcpy.EditRasterFunction(in_mosaic_dataset, edit_mosaic_dataset_item, function_chain_definition, location_function_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_mosaic_dataset_geometry(self, params):
        """Export Mosaic Dataset Geometry

Creates a feature class showing the footprints, boundary, seamlines or spatial resolutions of a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "geometry_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        geometry_type = params.get("geometry_type")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Export_Mosaic_Dataset_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Mosaic Dataset Geometry
            arcpy.ExportMosaicDatasetGeometry(in_mosaic_dataset, where_clause, geometry_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_mosaic_dataset_items(self, params):
        """Export Mosaic Dataset Items

Saves a copy of processed images in a mosaic dataset to a specified folder and raster file format. The following are the two common workflows that use this tool: 
Export each selected item of a mosaic dataset to a new file. This allows you to have each processed item as a stand-alone file. You must set the appropriate NoData value for the exported items so there are no dark borders.Export each selected image within a time series mosaic dataset based on an area of interest. This allows you to only export the area of interest from each time slice.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "out_folder": <Folder>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        where_clause = params.get("where_clause")
        format = params.get("format")
        nodata_value = params.get("nodata_value")
        clip_type = params.get("clip_type")
        template_dataset = params.get("template_dataset")
        cell_size = params.get("cell_size")
        image_space = params.get("image_space")
        remove_distortion = params.get("remove_distortion")
        band_method = params.get("band_method")
        band_name_selection = params.get("band_name_selection")
        band_id_selection = params.get("band_id_selection")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Export_Mosaic_Dataset_Items"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Mosaic Dataset Items
            arcpy.ExportMosaicDatasetItems(in_mosaic_dataset, out_folder, where_clause, format, nodata_value, clip_type, template_dataset, cell_size, image_space, remove_distortion, band_method, band_name_selection, band_id_selection)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_mosaic_dataset_paths(self, params):
        """Export Mosaic Dataset Paths

Creates a table of the file path for each item in a mosaic dataset. You can specify whether the table contains all the file paths or just the ones that are broken.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "out_table": <Table>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        where_clause = params.get("where_clause")
        export_mode = params.get("export_mode")
        types_of_pathstype_of_path = params.get("types_of_pathstype_of_path")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Export_Mosaic_Dataset_Paths"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Mosaic Dataset Paths
            arcpy.ExportMosaicDatasetPaths(in_mosaic_dataset, out_table, where_clause, export_mode, types_of_pathstype_of_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_exclude_area(self, params):
        """Generate Exclude Area

Masks pixels based on their color or by clipping a range of values. The output of this tool is used as an input to the Color Balance Mosaic Dataset tool to eliminate areas such as clouds and water that can skew the statistics used to color balance multiple images.

        params: {"in_raster": <Mosaic Dataset; Raster Dataset; Raster Layer>, "out_raster": <Raster Dataset>, "pixel_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        pixel_type = params.get("pixel_type")
        if pixel_type is None:
            return {"success": False, "error": "pixel_type parameter is required"}
        generate_method = params.get("generate_method")
        if generate_method is None:
            return {"success": False, "error": "generate_method parameter is required"}
        max_red = params.get("max_red")
        max_green = params.get("max_green")
        max_blue = params.get("max_blue")
        max_white = params.get("max_white")
        max_black = params.get("max_black")
        max_magenta = params.get("max_magenta")
        max_cyan = params.get("max_cyan")
        max_yellow = params.get("max_yellow")
        percentage_low = params.get("percentage_low")
        percentage_high = params.get("percentage_high")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Generate_Exclude_Area"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Exclude Area
            arcpy.GenerateExcludeArea(in_raster, out_raster, pixel_type, generate_method, max_red, max_green, max_blue, max_white, max_black, max_magenta, max_cyan, max_yellow, percentage_low, percentage_high)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_raster_collection(self, params):
        """Generate Raster Collection

Performs batch analysis or processing on image collections contained in a mosaic dataset. The images in the input mosaic dataset can be processed individually or as groups. The rules of processing can be defined through the Collection Builder parameter and raster function parameters. It generates a new mosaic dataset of processed images. You can optionally choose to save the processed images to disk as separate files. The default condition  is to append the input raster function to the mosaic dataset's existing images' function chain, and add it to the output mosaic dataset.

        params: {"out_raster_collection": <Mosaic Dataset>, "collection_builder": <String>, "raster_function": <String; File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_raster_collection = params.get("out_raster_collection")
        if out_raster_collection is None:
            return {"success": False, "error": "out_raster_collection parameter is required"}
        collection_builder = params.get("collection_builder")
        if collection_builder is None:
            return {"success": False, "error": "collection_builder parameter is required"}
        raster_function = params.get("raster_function")
        generate_rasters = params.get("generate_rasters")
        out_workspace = params.get("out_workspace")
        format = params.get("format")
        out_base_name = params.get("out_base_name")

            # Generate output name and path
            output_name = f"{out_raster_collection.replace(' ', '_')}_Generate_Raster_Collection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Raster Collection
            arcpy.GenerateRasterCollection(out_raster_collection, collection_builder, raster_function, generate_rasters, out_workspace, format, out_base_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_mosaic_dataset_geometry(self, params):
        """Import Mosaic Dataset Geometry

Modifies the geometry for the footprints, boundary, or seamlines in a mosaic dataset to match those in a feature class.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "target_featureclass_type": <String>, "target_join_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        target_featureclass_type = params.get("target_featureclass_type")
        if target_featureclass_type is None:
            return {"success": False, "error": "target_featureclass_type parameter is required"}
        target_join_field = params.get("target_join_field")
        if target_join_field is None:
            return {"success": False, "error": "target_join_field parameter is required"}
        input_featureclass = params.get("input_featureclass")
        if input_featureclass is None:
            return {"success": False, "error": "input_featureclass parameter is required"}
        input_join_field = params.get("input_join_field")
        if input_join_field is None:
            return {"success": False, "error": "input_join_field parameter is required"}

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Import_Mosaic_Dataset_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import Mosaic Dataset Geometry
            arcpy.ImportMosaicDatasetGeometry(in_mosaic_dataset, target_featureclass_type, target_join_field, input_featureclass, input_join_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def merge_mosaic_dataset_items(self, params):
        """Merge Mosaic Dataset Items

Groups multiple items in a mosaic dataset together as one item.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "block_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        block_field = params.get("block_field")
        max_rows_per_merged_items = params.get("max_rows_per_merged_items")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Merge_Mosaic_Dataset_Items"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Merge Mosaic Dataset Items
            arcpy.MergeMosaicDatasetItems(in_mosaic_dataset, where_clause, block_field, max_rows_per_merged_items)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mosaic_dataset_to_mobile_mosaic_dataset(self, params):
        """Mosaic Dataset To Mobile Mosaic Dataset

Converts a mosaic dataset into a mobile mosaic dataset that's compatible with ArcGIS Maps SDKs for Native Apps. A mobile mosaic dataset resides in a mobile geodatabase.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "out_mobile_gdb": <File>, "mosaic_dataset_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_mobile_gdb = params.get("out_mobile_gdb")
        if out_mobile_gdb is None:
            return {"success": False, "error": "out_mobile_gdb parameter is required"}
        mosaic_dataset_name = params.get("mosaic_dataset_name")
        if mosaic_dataset_name is None:
            return {"success": False, "error": "mosaic_dataset_name parameter is required"}
        where_clause = params.get("where_clause")
        selection_feature = params.get("selection_feature")
        out_data_folder = params.get("out_data_folder")
        convert_rasters = params.get("convert_rasters")
        out_name_prefix = params.get("out_name_prefix")
        format = params.get("format")
        compression_method = params.get("compression_method")
        compression_quality = params.get("compression_quality")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Mosaic_Dataset_To_Mobile_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mosaic Dataset To Mobile Mosaic Dataset
            arcpy.MosaicDatasetToMobileMosaicDataset(in_mosaic_dataset, out_mobile_gdb, mosaic_dataset_name, where_clause, selection_feature, out_data_folder, convert_rasters, out_name_prefix, format, compression_method, compression_quality)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_rasters_from_mosaic_dataset(self, params):
        """Remove Rasters From Mosaic Dataset

Removes selected rasters from a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "update_boundary": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        update_boundary = params.get("update_boundary")
        mark_overviews_items = params.get("mark_overviews_items")
        delete_overview_images = params.get("delete_overview_images")
        delete_item_cache = params.get("delete_item_cache")
        remove_items = params.get("remove_items")
        update_cellsize_ranges = params.get("update_cellsize_ranges")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Remove_Rasters_From_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Rasters From Mosaic Dataset
            arcpy.RemoveRastersFromMosaicDataset(in_mosaic_dataset, where_clause, update_boundary, mark_overviews_items, delete_overview_images, delete_item_cache, remove_items, update_cellsize_ranges)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def repair_mosaic_dataset_paths(self, params):
        """Repair Mosaic Dataset Paths

Resets paths to source imagery if you have moved or copied a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "paths_listoriginal_path_new_path": <Value Table>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        paths_listoriginal_path_new_path = params.get("paths_listoriginal_path_new_path")
        if paths_listoriginal_path_new_path is None:
            return {"success": False, "error": "paths_listoriginal_path_new_path parameter is required"}
        where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Repair_Mosaic_Dataset_Paths"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Repair Mosaic Dataset Paths
            arcpy.RepairMosaicDatasetPaths(in_mosaic_dataset, paths_listoriginal_path_new_path, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_mosaic_dataset_properties(self, params):
        """Set Mosaic Dataset Properties

Defines the defaults for displaying a mosaic dataset and serving it as an image service.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "rows_maximum_imagesize": <Long>, "columns_maximum_imagesize": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        rows_maximum_imagesize = params.get("rows_maximum_imagesize")
        columns_maximum_imagesize = params.get("columns_maximum_imagesize")
        allowed_compressions = params.get("allowed_compressions")
        default_compression_type = params.get("default_compression_type")
        jpeg_quality = params.get("jpeg_quality")
        lerc_tolerance = params.get("lerc_tolerance")
        resampling_type = params.get("resampling_type")
        clip_to_footprints = params.get("clip_to_footprints")
        footprints_may_contain_nodata = params.get("footprints_may_contain_nodata")
        clip_to_boundary = params.get("clip_to_boundary")
        color_correction = params.get("color_correction")
        allowed_mensuration_capabilities = params.get("allowed_mensuration_capabilities")
        default_mensuration_capabilities = params.get("default_mensuration_capabilities")
        allowed_mosaic_methods = params.get("allowed_mosaic_methods")
        default_mosaic_method = params.get("default_mosaic_method")
        order_field = params.get("order_field")
        order_base = params.get("order_base")
        sorting_order = params.get("sorting_order")
        mosaic_operator = params.get("mosaic_operator")
        blend_width = params.get("blend_width")
        view_point_x = params.get("view_point_x")
        view_point_y = params.get("view_point_y")
        max_num_per_mosaic = params.get("max_num_per_mosaic")
        cell_size_tolerance = params.get("cell_size_tolerance")
        cell_size = params.get("cell_size")
        metadata_level = params.get("metadata_level")
        use_time = params.get("use_time")
        start_time_field = params.get("start_time_field")
        end_time_field = params.get("end_time_field")
        time_format = params.get("time_format")
        geographic_transform = params.get("geographic_transform")
        max_num_of_download_items = params.get("max_num_of_download_items")
        max_num_of_records_returned = params.get("max_num_of_records_returned")
        data_source_type = params.get("data_source_type")
        minimum_pixel_contribution = params.get("minimum_pixel_contribution")
        processing_templates = params.get("processing_templates")
        default_processing_template = params.get("default_processing_template")
        time_interval = params.get("time_interval")
        time_interval_units = params.get("time_interval_units")
        product_definition = params.get("product_definition")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Set_Mosaic_Dataset_Properties"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Mosaic Dataset Properties
            arcpy.SetMosaicDatasetProperties(in_mosaic_dataset, rows_maximum_imagesize, columns_maximum_imagesize, allowed_compressions, default_compression_type, jpeg_quality, lerc_tolerance, resampling_type, clip_to_footprints, footprints_may_contain_nodata, clip_to_boundary, color_correction, allowed_mensuration_capabilities, default_mensuration_capabilities, allowed_mosaic_methods, default_mosaic_method, order_field, order_base, sorting_order, mosaic_operator, blend_width, view_point_x, view_point_y, max_num_per_mosaic, cell_size_tolerance, cell_size, metadata_level, use_time, start_time_field, end_time_field, time_format, geographic_transform, max_num_of_download_items, max_num_of_records_returned, data_source_type, minimum_pixel_contribution, processing_templates, default_processing_template, time_interval, time_interval_units, product_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def split_mosaic_dataset_items(self, params):
        """Split Mosaic Dataset Items

Splits mosaic dataset items that were merged together using Merge Mosaic Dataset Items.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Split_Mosaic_Dataset_Items"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Split Mosaic Dataset Items
            arcpy.SplitMosaicDatasetItems(in_mosaic_dataset, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def synchronize_mosaic_dataset(self, params):
        """Synchronize Mosaic Dataset

Synchronizes a mosaic dataset to keep it up to date. In addition to syncing data, you can update overviews if the underlying imagery has been changed, generate new overviews and cache, and restore the original configuration of mosaic dataset items. You can also remove paths to source data with this tool. To repair paths, use the Repair Mosaic Dataset Paths  tool. Synchronization is a one-way operation: changes in the source data can be 
synchronized to the mosaic dataset’s attribute table, thereby updating the mosaic dataset's attribute table.  Changes in the mosaic dataset's attribute table will not affect the source data. Changes made by synchronization cannot be undone. Create a backup  of your mosaic dataset if you've made modifications to the data that you don't want overwritten.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "new_items": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        new_items = params.get("new_items")
        sync_only_stale = params.get("sync_only_stale")
        update_cellsize_ranges = params.get("update_cellsize_ranges")
        update_boundary = params.get("update_boundary")
        update_overviews = params.get("update_overviews")
        build_pyramids = params.get("build_pyramids")
        calculate_statistics = params.get("calculate_statistics")
        build_thumbnails = params.get("build_thumbnails")
        build_item_cache = params.get("build_item_cache")
        rebuild_raster = params.get("rebuild_raster")
        update_fields = params.get("update_fields")
        fields_to_updatefield_to_update = params.get("fields_to_updatefield_to_update")
        existing_items = params.get("existing_items")
        broken_items = params.get("broken_items")
        skip_existing_items = params.get("skip_existing_items")
        refresh_aggregate_info = params.get("refresh_aggregate_info")
        estimate_statistics = params.get("estimate_statistics")
        if estimate_statistics is None:
            return {"success": False, "error": "estimate_statistics parameter is required"}

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Synchronize_Mosaic_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Synchronize Mosaic Dataset
            arcpy.SynchronizeMosaicDataset(in_mosaic_dataset, where_clause, new_items, sync_only_stale, update_cellsize_ranges, update_boundary, update_overviews, build_pyramids, calculate_statistics, build_thumbnails, build_item_cache, rebuild_raster, update_fields, fields_to_updatefield_to_update, existing_items, broken_items, skip_existing_items, refresh_aggregate_info, estimate_statistics)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze_control_points(self, params):
        """Analyze Control Points

Analyzes the control point coverage and identifies the areas that need additional control points to improve the block adjust result. The tool will check each image and provide the following:The number of control points
for each imageThe percentage of image covered by the control
points (point distribution)The overlap
areasThe number of control
points within overlap areas

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "in_control_points": <Feature Layer>, "out_coverage_table": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        in_control_points = params.get("in_control_points")
        if in_control_points is None:
            return {"success": False, "error": "in_control_points parameter is required"}
        out_coverage_table = params.get("out_coverage_table")
        if out_coverage_table is None:
            return {"success": False, "error": "out_coverage_table parameter is required"}
        out_overlap_table = params.get("out_overlap_table")
        if out_overlap_table is None:
            return {"success": False, "error": "out_overlap_table parameter is required"}
        in_mask_dataset = params.get("in_mask_dataset")
        minimum_area = params.get("minimum_area")
        maximum_level = params.get("maximum_level")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Analyze_Control_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Analyze Control Points
            arcpy.AnalyzeControlPoints(in_mosaic_dataset, in_control_points, out_coverage_table, out_overlap_table, in_mask_dataset, minimum_area, maximum_level)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def append_control_points(self, params):
        """Append Control Points

Combines control points to an existing control point table. The points to be appended are the results from either the Compute Tie Points tool or the Compute Control Points tool, or a point feature class.

        params: {"in_master_control_points": <Feature Class; Feature Layer>, "in_input_control_points": <Feature Class; Feature Layer; File; String>, "in_tag_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_master_control_points = params.get("in_master_control_points")
        if in_master_control_points is None:
            return {"success": False, "error": "in_master_control_points parameter is required"}
        in_input_control_points = params.get("in_input_control_points")
        if in_input_control_points is None:
            return {"success": False, "error": "in_input_control_points parameter is required"}
        in_tag_field = params.get("in_tag_field")
        in_xy_accuracy = params.get("in_xy_accuracy")
        in_z_accuracy = params.get("in_z_accuracy")
        geoid = params.get("geoid")
        area_of_interest = params.get("area_of_interest")
        append_option = params.get("append_option")

            # Generate output name and path
            output_name = f"{in_master_control_points.replace(' ', '_')}_Append_Control_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Append Control Points
            arcpy.AppendControlPoints(in_master_control_points, in_input_control_points, in_tag_field, in_xy_accuracy, in_z_accuracy, geoid, area_of_interest, append_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_block_adjustment(self, params):
        """Apply Block Adjustment

Applies the geographic adjustments to the mosaic dataset items. This tool uses the solution table from the Compute Block Adjustments tool. This tool can also reset the geographic adjustments back to the original location.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "adjustment_operation": <String>, "input_solution_table": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        adjustment_operation = params.get("adjustment_operation")
        if adjustment_operation is None:
            return {"success": False, "error": "adjustment_operation parameter is required"}
        input_solution_table = params.get("input_solution_table")
        pan_to_ms_scaling_factor = params.get("pan_to_ms_scaling_factor")
        dem = params.get("dem")
        zoffset = params.get("zoffset")
        control_point_table = params.get("control_point_table")
        adjust_footprints = params.get("adjust_footprints")
        solution_point_table = params.get("solution_point_table")
        adjust_tiepoints = params.get("adjust_tiepoints")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Apply_Block_Adjustment"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Block Adjustment
            arcpy.ApplyBlockAdjustment(in_mosaic_dataset, adjustment_operation, input_solution_table, pan_to_ms_scaling_factor, dem, zoffset, control_point_table, adjust_footprints, solution_point_table, adjust_tiepoints)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_block_adjustments(self, params):
        """Compute Block Adjustments

Computes the adjustments to the mosaic dataset. This tool will create a solution table that can be used to apply the actual adjustments.

        params: {"in_mosaic_dataset": <Mosaic Layer; Mosaic Dataset>, "in_control_points": <Feature Layer>, "transformation_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        in_control_points = params.get("in_control_points")
        if in_control_points is None:
            return {"success": False, "error": "in_control_points parameter is required"}
        transformation_type = params.get("transformation_type")
        if transformation_type is None:
            return {"success": False, "error": "transformation_type parameter is required"}
        out_solution_table = params.get("out_solution_table")
        if out_solution_table is None:
            return {"success": False, "error": "out_solution_table parameter is required"}
        out_solution_point_table = params.get("out_solution_point_table")
        maximum_residual_value = params.get("maximum_residual_value")
        adjustment_optionsname_value = params.get("adjustment_optionsname_value")
        location_accuracy = params.get("location_accuracy")
        out_quality_table = params.get("out_quality_table")
        dem = params.get("dem")
        elevation_accuracy = params.get("elevation_accuracy")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Block_Adjustments"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Block Adjustments
            arcpy.ComputeBlockAdjustments(in_mosaic_dataset, in_control_points, transformation_type, out_solution_table, out_solution_point_table, maximum_residual_value, adjustment_optionsname_value, location_accuracy, out_quality_table, dem, elevation_accuracy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_stereo_model(self, params):
        """Build Stereo Model

Builds a stereo model of a mosaic dataset based on a user-provided stereo pair. A stereo model of a mosaic dataset is required for stereo feature collection and 3D point cloud generation.  A stereo model, as one of the tables in a mosaic dataset, defines the stereo pairs. The stereo model stores the overlapping polygons, the corresponding image identifiers, and image IDs that comprise each pair. The stereo model can be accessed from the context menu of a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "minimum_angle": <Double>, "maximum_angle": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        minimum_angle = params.get("minimum_angle")
        maximum_angle = params.get("maximum_angle")
        minimum_overlap = params.get("minimum_overlap")
        maximum_diff_op = params.get("maximum_diff_op")
        maximum_diff_gsd = params.get("maximum_diff_gsd")
        group_by = params.get("group_by")
        same_flight = params.get("same_flight")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Build_Stereo_Model"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Stereo Model
            arcpy.BuildStereoModel(in_mosaic_dataset, minimum_angle, maximum_angle, minimum_overlap, maximum_diff_op, maximum_diff_gsd, group_by, same_flight)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_block_adjustment(self, params):
        """Compute Block Adjustment

Computes the adjustments to the mosaic dataset. This tool will create a solution table that can be used to apply the actual adjustments.

        params: {"in_mosaic_dataset": <Mosaic Layer; Mosaic Dataset>, "in_control_points": <Feature Layer>, "transformation_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        in_control_points = params.get("in_control_points")
        if in_control_points is None:
            return {"success": False, "error": "in_control_points parameter is required"}
        transformation_type = params.get("transformation_type")
        if transformation_type is None:
            return {"success": False, "error": "transformation_type parameter is required"}
        out_solution_table = params.get("out_solution_table")
        if out_solution_table is None:
            return {"success": False, "error": "out_solution_table parameter is required"}
        out_solution_point_table = params.get("out_solution_point_table")
        maximum_residual_value = params.get("maximum_residual_value")
        adjustment_optionsname_value = params.get("adjustment_optionsname_value")
        location_accuracy = params.get("location_accuracy")
        out_quality_table = params.get("out_quality_table")
        dem = params.get("dem")
        elevation_accuracy = params.get("elevation_accuracy")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Block_Adjustment"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Block Adjustment
            arcpy.ComputeBlockAdjustment(in_mosaic_dataset, in_control_points, transformation_type, out_solution_table, out_solution_point_table, maximum_residual_value, adjustment_optionsname_value, location_accuracy, out_quality_table, dem, elevation_accuracy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_camera_model(self, params):
        """Compute Camera Model

Estimates the exterior camera model and interior camera model from the EXIF header of the raw image and refines the camera models. The model is then applied to the mosaic dataset with an option to use a tool-generated, high-resolution digital surface model (DSM) to achieve better orthorectification. This is especially helpful for UAV and UAS images in which the exterior and interior camera models are coarse or undefined.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "out_dsm": <Raster Dataset>, "gps_accuracy": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_dsm = params.get("out_dsm")
        gps_accuracy = params.get("gps_accuracy")
        estimate = params.get("estimate")
        refine = params.get("refine")
        apply_adjustment = params.get("apply_adjustment")
        maximum_residual = params.get("maximum_residual")
        initial_tiepoint_resolution = params.get("initial_tiepoint_resolution")
        out_control_points = params.get("out_control_points")
        out_solution_table = params.get("out_solution_table")
        out_solution_point_table = params.get("out_solution_point_table")
        out_flight_path = params.get("out_flight_path")
        maximum_overlap = params.get("maximum_overlap")
        minimum_coverage = params.get("minimum_coverage")
        remove = params.get("remove")
        in_control_points = params.get("in_control_points")
        options = params.get("options")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Camera_Model"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Camera Model
            arcpy.ComputeCameraModel(in_mosaic_dataset, out_dsm, gps_accuracy, estimate, refine, apply_adjustment, maximum_residual, initial_tiepoint_resolution, out_control_points, out_solution_table, out_solution_point_table, out_flight_path, maximum_overlap, minimum_coverage, remove, in_control_points, options)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_control_points(self, params):
        """Compute Control Points

Creates the control points between the mosaic dataset and the reference image. The control points can then be used in conjunction with tie points to compute the adjustments for the mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "in_reference_images": <Raster Layer; Raster Dataset; Image Service; Map Server; WMS Map; Mosaic Layer; Internet Tiled Layer; Map Server Layer>, "out_control_points": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        in_reference_images = params.get("in_reference_images")
        if in_reference_images is None:
            return {"success": False, "error": "in_reference_images parameter is required"}
        out_control_points = params.get("out_control_points")
        if out_control_points is None:
            return {"success": False, "error": "out_control_points parameter is required"}
        similarity = params.get("similarity")
        out_image_feature_points = params.get("out_image_feature_points")
        density = params.get("density")
        if density is None:
            return {"success": False, "error": "density parameter is required"}
        distribution = params.get("distribution")
        if distribution is None:
            return {"success": False, "error": "distribution parameter is required"}
        area_of_interest = params.get("area_of_interest")
        if area_of_interest is None:
            return {"success": False, "error": "area_of_interest parameter is required"}
        location_accuracy = params.get("location_accuracy")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Control_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Control Points
            arcpy.ComputeControlPoints(in_mosaic_dataset, in_reference_images, out_control_points, similarity, out_image_feature_points, density, distribution, area_of_interest, location_accuracy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_depth_map(self, params):
        """Compute Depth Map

Computes a more accurate CenterZ field value based on the depth map for each image comprising a mosaic dataset. Control points and solution points are used to compute a depth map for each image comprising a mosaic dataset to improve image-to-ground (map) transformation, especially in high oblique cases. Image inspection, typically performed in image space, allows you to discover defects, perform measurement, and generate inspection reports for rectified imagery.  You can measure distance, area, and height of objects in either map space or image space, and an inspection report can be generated to share the inspection results. An important component of the inspection workflow is the transformation from image to ground (map) space, that allows the defects, points, lines, polygons, on images to be more accurately located and measured. The image-to-ground transformation, especially for high oblique images, uses a depth map, which is the distance from the camera location to the ground location for each pixel.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "control_point_table": <Feature Class; Table View>, "solution_point_table": <Feature Class; Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        control_point_table = params.get("control_point_table")
        if control_point_table is None:
            return {"success": False, "error": "control_point_table parameter is required"}
        solution_point_table = params.get("solution_point_table")
        if solution_point_table is None:
            return {"success": False, "error": "solution_point_table parameter is required"}
        where_clause = params.get("where_clause")
        skip_existing = params.get("skip_existing")
        adjust_footprints = params.get("adjust_footprints")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Depth_Map"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Depth Map
            arcpy.ComputeDepthMap(in_mosaic_dataset, control_point_table, solution_point_table, where_clause, skip_existing, adjust_footprints)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_fiducials(self, params):
        """Compute Fiducials

Computes the fiducial coordinates in image and film space for each image in a mosaic dataset. Fiducials are marks, normally four or eight, in aerial photos used as reference. They are an important factor for determining the image transformation from image to film known as interior orientation. This tool is used to automatically find the image coordinates of the fiducials for each images in a mosaic dataset based on a user-provided fiducial template file. A fiducial template file is a table that has required fields for storing either fiducial pictures or paths to the pictures. For more information about fiducials, see Refine Interior Orientation Using Fiducials.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "out_fiducial_table": <Table>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_fiducial_table = params.get("out_fiducial_table")
        if out_fiducial_table is None:
            return {"success": False, "error": "out_fiducial_table parameter is required"}
        where_clause = params.get("where_clause")
        fiducial_templates = params.get("fiducial_templates")
        film_coordinate_system = params.get("film_coordinate_system")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Fiducials"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Fiducials
            arcpy.ComputeFiducials(in_mosaic_dataset, out_fiducial_table, where_clause, fiducial_templates, film_coordinate_system)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_tie_points(self, params):
        """Compute Tie Points

Computes the tie points between overlapped mosaic dataset items. The tie points can then be used to compute the block adjustments for the mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Layer; Mosaic Dataset>, "out_control_points": <Feature Class>, "similarity": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        out_control_points = params.get("out_control_points")
        if out_control_points is None:
            return {"success": False, "error": "out_control_points parameter is required"}
        similarity = params.get("similarity")
        in_mask_dataset = params.get("in_mask_dataset")
        out_image_features = params.get("out_image_features")
        density = params.get("density")
        if density is None:
            return {"success": False, "error": "density parameter is required"}
        distribution = params.get("distribution")
        if distribution is None:
            return {"success": False, "error": "distribution parameter is required"}
        location_accuracy = params.get("location_accuracy")
        if location_accuracy is None:
            return {"success": False, "error": "location_accuracy parameter is required"}
        options = params.get("options")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Compute_Tie_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Tie Points
            arcpy.ComputeTiePoints(in_mosaic_dataset, out_control_points, similarity, in_mask_dataset, out_image_features, density, distribution, location_accuracy, options)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_frame_and_camera_parameters(self, params):
        """Export Frame and Camera Parameters

Exports frame and camera parameters from a mosaic dataset that contains frame imagery.

        params: {"input_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "output_file": <File>, "output_format": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_mosaic_dataset = params.get("input_mosaic_dataset")
        if input_mosaic_dataset is None:
            return {"success": False, "error": "input_mosaic_dataset parameter is required"}
        output_file = params.get("output_file")
        if output_file is None:
            return {"success": False, "error": "output_file parameter is required"}
        output_format = params.get("output_format")

            # Generate output name and path
            output_name = f"{input_mosaic_dataset.replace(' ', '_')}_Export_Frame_and_Camera_Parameters"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Frame and Camera Parameters
            arcpy.ExportFrameandCameraParameters(input_mosaic_dataset, output_file, output_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_block_adjustment_report(self, params):
        """Generate Block Adjustment Report

Generates a  report after performing an ortho mapping block adjustment on a mosaic dataset. The report is useful when evaluating the quality and accuracy of the ortho mapping products.

        params: {"input_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "input_solution_table": <Table View>, "input_solution_point": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_mosaic_dataset = params.get("input_mosaic_dataset")
        if input_mosaic_dataset is None:
            return {"success": False, "error": "input_mosaic_dataset parameter is required"}
        input_solution_table = params.get("input_solution_table")
        if input_solution_table is None:
            return {"success": False, "error": "input_solution_table parameter is required"}
        input_solution_point = params.get("input_solution_point")
        if input_solution_point is None:
            return {"success": False, "error": "input_solution_point parameter is required"}
        output_report = params.get("output_report")
        if output_report is None:
            return {"success": False, "error": "output_report parameter is required"}
        input_control_point_for_adjustment = params.get("input_control_point_for_adjustment")
        report_format = params.get("report_format")

            # Generate output name and path
            output_name = f"{input_mosaic_dataset.replace(' ', '_')}_Generate_Block_Adjustment_Report"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Block Adjustment Report
            arcpy.GenerateBlockAdjustmentReport(input_mosaic_dataset, input_solution_table, input_solution_point, output_report, input_control_point_for_adjustment, report_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_point_cloud(self, params):
        """Generate Point Cloud

Generates 3D points from stereo pairs and outputs a point cloud as a set of LAS files. The tiling of the LAS files is based on 1,000 by 1,000 ground spacing. The points in each LAS tile are computed by selecting pairs, based on user-defined criteria, and filter points from the selected pairs. The input of this tool is  a mosaic dataset that contains a stereo model. The output of this tool can be used to generate a digital terrain model (DTM) or a digital surface model (DSM).

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "matching_method": <String>, "out_folder": <Folder>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        matching_method = params.get("matching_method")
        if matching_method is None:
            return {"success": False, "error": "matching_method parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        out_base_name = params.get("out_base_name")
        if out_base_name is None:
            return {"success": False, "error": "out_base_name parameter is required"}
        object_size = params.get("object_size")
        ground_spacing = params.get("ground_spacing")
        minimum_pairs = params.get("minimum_pairs")
        minimum_area = params.get("minimum_area")
        minimum_adjustment_quality = params.get("minimum_adjustment_quality")
        maximum_diff_gsd = params.get("maximum_diff_gsd")
        maximum_diff_op = params.get("maximum_diff_op")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Generate_Point_Cloud"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Point Cloud
            arcpy.GeneratePointCloud(in_mosaic_dataset, matching_method, out_folder, out_base_name, object_size, ground_spacing, minimum_pairs, minimum_area, minimum_adjustment_quality, maximum_diff_gsd, maximum_diff_op)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def interpolate_from_point_cloud(self, params):
        """Interpolate From Point Cloud

Interpolates a digital terrain model (DTM) or a digital surface model (DSM) from a point cloud.

        params: {"in_container": <Folder; File; Feature Class; Feature Layer>, "out_raster": <Raster Dataset>, "cell_size": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_container = params.get("in_container")
        if in_container is None:
            return {"success": False, "error": "in_container parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        cell_size = params.get("cell_size")
        if cell_size is None:
            return {"success": False, "error": "cell_size parameter is required"}
        interpolation_method = params.get("interpolation_method")
        smooth_method = params.get("smooth_method")
        surface_type = params.get("surface_type")
        fill_dem = params.get("fill_dem")
        optionsname_value = params.get("optionsname_value")

            # Generate output name and path
            output_name = f"{in_container.replace(' ', '_')}_Interpolate_From_Point_Cloud"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Interpolate From Point Cloud
            arcpy.InterpolateFromPointCloud(in_container, out_raster, cell_size, interpolation_method, smooth_method, surface_type, fill_dem, optionsname_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def match_control_points(self, params):
        """Match Control Points

Creates matching tie points for a given ground control point and initial tie point in one of the overlapping images. The ortho mapping block adjustment workflow often involves adding ground control points for a more accurate adjustment. One ground control point is typically associated with a tie point in each overlapping image. When there are many overlapping images for one ground control point, manually creating tie points for each image is labor intensive.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "in_control_points": <File; Feature Class; Feature Layer; String>, "out_control_points": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        in_control_points = params.get("in_control_points")
        if in_control_points is None:
            return {"success": False, "error": "in_control_points parameter is required"}
        out_control_points = params.get("out_control_points")
        if out_control_points is None:
            return {"success": False, "error": "out_control_points parameter is required"}
        similarity = params.get("similarity")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Match_Control_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Match Control Points
            arcpy.MatchControlPoints(in_mosaic_dataset, in_control_points, out_control_points, similarity)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_depth_map(self, params):
        """Remove Depth Map

Removes the depth map from a mosaic dataset.  Other than the depth map removal, the tool will not update the mosaic dataset. Depth maps are created by running the Compute Depth Map tool.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Remove_Depth_Map"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Depth Map
            arcpy.RemoveDepthMap(in_mosaic_dataset, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_interior_orientation(self, params):
        """Update Interior Orientation

Refines the interior orientation for each image in the mosaic dataset by constructing an affine transformation from a fiducial table.

        params: {"in_mosaic_dataset": <Mosaic Layer>, "where_clause": <SQL Expression>, "fiducial_table": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        where_clause = params.get("where_clause")
        fiducial_table = params.get("fiducial_table")
        if fiducial_table is None:
            return {"success": False, "error": "fiducial_table parameter is required"}
        film_coordinate_system = params.get("film_coordinate_system")
        if film_coordinate_system is None:
            return {"success": False, "error": "film_coordinate_system parameter is required"}
        update_footprints = params.get("update_footprints")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Update_Interior_Orientation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Interior Orientation
            arcpy.UpdateInteriorOrientation(in_mosaic_dataset, where_clause, fiducial_table, film_coordinate_system, update_footprints)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy_raster(self, params):
        """Copy Raster

Saves a copy of a raster dataset or converts a mosaic dataset into a single raster dataset.

        params: {"in_raster": <Raster Dataset; Mosaic Dataset; Mosaic Layer; Raster Layer; File; Image Service>, "out_rasterdataset": <Raster Dataset>, "config_keyword": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_rasterdataset = params.get("out_rasterdataset")
        if out_rasterdataset is None:
            return {"success": False, "error": "out_rasterdataset parameter is required"}
        config_keyword = params.get("config_keyword")
        background_value = params.get("background_value")
        nodata_value = params.get("nodata_value")
        onebit_to_eightbit = params.get("onebit_to_eightbit")
        colormap_to_rgb = params.get("colormap_to_rgb")
        pixel_type = params.get("pixel_type")
        scale_pixel_value = params.get("scale_pixel_value")
        rgb_to_colormap = params.get("rgb_to_colormap")
        format = params.get("format")
        transform = params.get("transform")
        process_as_multidimensional = params.get("process_as_multidimensional")
        build_multidimensional_transpose = params.get("build_multidimensional_transpose")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Copy_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy Raster
            arcpy.CopyRaster(in_raster, out_rasterdataset, config_keyword, background_value, nodata_value, onebit_to_eightbit, colormap_to_rgb, pixel_type, scale_pixel_value, rgb_to_colormap, format, transform, process_as_multidimensional, build_multidimensional_transpose)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_random_raster(self, params):
        """Create Random Raster

Creates a raster dataset of random values with a distribution you define.

        params: {"out_path": <Workspace>, "out_name": <String>, "distribution": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        distribution = params.get("distribution")
        raster_extent = params.get("raster_extent")
        cellsize = params.get("cellsize")
        build_rat = params.get("build_rat")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Random_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Random Raster
            arcpy.CreateRandomRaster(out_path, out_name, distribution, raster_extent, cellsize, build_rat)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_raster_dataset(self, params):
        """Create Raster Dataset

Creates an empty raster dataset.

        params: {"out_path": <Workspace>, "out_name": <String>, "cellsize": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        cellsize = params.get("cellsize")
        pixel_type = params.get("pixel_type")
        if pixel_type is None:
            return {"success": False, "error": "pixel_type parameter is required"}
        raster_spatial_reference = params.get("raster_spatial_reference")
        number_of_bands = params.get("number_of_bands")
        if number_of_bands is None:
            return {"success": False, "error": "number_of_bands parameter is required"}
        config_keyword = params.get("config_keyword")
        pyramids = params.get("pyramids")
        tile_size = params.get("tile_size")
        compression = params.get("compression")
        pyramid_origin = params.get("pyramid_origin")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Raster_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Raster Dataset
            arcpy.CreateRasterDataset(out_path, out_name, cellsize, pixel_type, raster_spatial_reference, number_of_bands, config_keyword, pyramids, tile_size, compression, pyramid_origin)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def download_rasters(self, params):
        """Download Rasters

Downloads the source  files from an image service or mosaic dataset.

        params: {"in_image_service": <Image Service; Mosaic Layer; Raster Layer; String>, "out_folder": <Folder>, "where_clause": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_image_service = params.get("in_image_service")
        if in_image_service is None:
            return {"success": False, "error": "in_image_service parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        where_clause = params.get("where_clause")
        selection_feature = params.get("selection_feature")
        clipping = params.get("clipping")
        convert_rasters = params.get("convert_rasters")
        format = params.get("format")
        compression_method = params.get("compression_method")
        compression_quality = params.get("compression_quality")
        maintain_folder = params.get("maintain_folder")

            # Generate output name and path
            output_name = f"{in_image_service.replace(' ', '_')}_Download_Rasters"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Download Rasters
            arcpy.DownloadRasters(in_image_service, out_folder, where_clause, selection_feature, clipping, convert_rasters, format, compression_method, compression_quality, maintain_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_raster_from_raster_function(self, params):
        """Generate Raster From Raster Function

Generates a raster dataset from an input raster function or function chain.

        params: {"raster_function": <File; String>, "out_raster_dataset": <Raster Dataset>, "format": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        raster_function = params.get("raster_function")
        if raster_function is None:
            return {"success": False, "error": "raster_function parameter is required"}
        out_raster_dataset = params.get("out_raster_dataset")
        if out_raster_dataset is None:
            return {"success": False, "error": "out_raster_dataset parameter is required"}
        format = params.get("format")
        process_as_multidimensional = params.get("process_as_multidimensional")

            # Generate output name and path
            output_name = f"{raster_function.replace(' ', '_')}_Generate_Raster_From_Raster_Function"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Raster From Raster Function
            arcpy.GenerateRasterFromRasterFunction(raster_function, out_raster_dataset, format, process_as_multidimensional)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mosaic(self, params):
        """Mosaic

Merges multiple existing raster datasets or mosaic datasets into an existing raster dataset.

        params: {"inputsinput": <Mosaic Dataset; Raster Dataset; Raster Layer>, "target": <Raster Dataset>, "mosaic_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        inputsinput = params.get("inputsinput")
        if inputsinput is None:
            return {"success": False, "error": "inputsinput parameter is required"}
        target = params.get("target")
        if target is None:
            return {"success": False, "error": "target parameter is required"}
        mosaic_type = params.get("mosaic_type")
        colormap = params.get("colormap")
        background_value = params.get("background_value")
        nodata_value = params.get("nodata_value")
        onebit_to_eightbit = params.get("onebit_to_eightbit")
        mosaicking_tolerance = params.get("mosaicking_tolerance")
        matchingmethod = params.get("matchingmethod")

            # Generate output name and path
            output_name = f"{inputsinput.replace(' ', '_')}_Mosaic"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mosaic
            arcpy.Mosaic(inputsinput, target, mosaic_type, colormap, background_value, nodata_value, onebit_to_eightbit, mosaicking_tolerance, matchingmethod)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mosaic_to_new_raster(self, params):
        """Mosaic To New Raster

Merges multiple raster datasets into a new raster dataset.

        params: {"input_rastersinput_raster": <Mosaic Dataset; Raster Dataset; Raster Layer>, "output_location": <Workspace>, "raster_dataset_name_with_extension": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_rastersinput_raster = params.get("input_rastersinput_raster")
        if input_rastersinput_raster is None:
            return {"success": False, "error": "input_rastersinput_raster parameter is required"}
        output_location = params.get("output_location")
        if output_location is None:
            return {"success": False, "error": "output_location parameter is required"}
        raster_dataset_name_with_extension = params.get("raster_dataset_name_with_extension")
        if raster_dataset_name_with_extension is None:
            return {"success": False, "error": "raster_dataset_name_with_extension parameter is required"}
        coordinate_system_for_the_raster = params.get("coordinate_system_for_the_raster")
        pixel_type = params.get("pixel_type")
        cellsize = params.get("cellsize")
        number_of_bands = params.get("number_of_bands")
        if number_of_bands is None:
            return {"success": False, "error": "number_of_bands parameter is required"}
        mosaic_method = params.get("mosaic_method")
        mosaic_colormap_mode = params.get("mosaic_colormap_mode")

            # Generate output name and path
            output_name = f"{input_rastersinput_raster.replace(' ', '_')}_Mosaic_To_New_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mosaic To New Raster
            arcpy.MosaicToNewRaster(input_rastersinput_raster, output_location, raster_dataset_name_with_extension, coordinate_system_for_the_raster, pixel_type, cellsize, number_of_bands, mosaic_method, mosaic_colormap_mode)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def workspace_to_raster_dataset(self, params):
        """Workspace To Raster Dataset

Merges all of the raster datasets in a folder into one raster dataset.

        params: {"in_workspace": <Workspace>, "in_raster_dataset": <Raster Dataset>, "include_subdirectories": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        in_raster_dataset = params.get("in_raster_dataset")
        if in_raster_dataset is None:
            return {"success": False, "error": "in_raster_dataset parameter is required"}
        include_subdirectories = params.get("include_subdirectories")
        mosaic_type = params.get("mosaic_type")
        colormap = params.get("colormap")
        background_value = params.get("background_value")
        nodata_value = params.get("nodata_value")
        onebit_to_eightbit = params.get("onebit_to_eightbit")
        mosaicking_tolerance = params.get("mosaicking_tolerance")
        matchingmethod = params.get("matchingmethod")
        colormap_to_rgb = params.get("colormap_to_rgb")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Workspace_To_Raster_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Workspace To Raster Dataset
            arcpy.WorkspaceToRasterDataset(in_workspace, in_raster_dataset, include_subdirectories, mosaic_type, colormap, background_value, nodata_value, onebit_to_eightbit, mosaicking_tolerance, matchingmethod, colormap_to_rgb)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def clip_raster(self, params):
        """Clip Raster

Cuts out a portion of a raster dataset, mosaic dataset, or image service layer.

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Dataset; Raster Layer>, "rectangle": <Envelope; Feature Class; Feature Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        rectangle = params.get("rectangle")
        if rectangle is None:
            return {"success": False, "error": "rectangle parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        in_template_dataset = params.get("in_template_dataset")
        nodata_value = params.get("nodata_value")
        clipping_geometry = params.get("clipping_geometry")
        maintain_clipping_extent = params.get("maintain_clipping_extent")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Clip_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Clip Raster
            arcpy.ClipRaster(in_raster, rectangle, out_raster, in_template_dataset, nodata_value, clipping_geometry, maintain_clipping_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def composite_bands(self, params):
        """Composite Bands

Creates a single raster dataset from multiple bands.

        params: {"in_rasters": <Mosaic Dataset ; Mosaic Layer ; Raster Dataset ; Raster Layer>, "out_raster": <Raster Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters = params.get("in_rasters")
        if in_rasters is None:
            return {"success": False, "error": "in_rasters parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_rasters.replace(' ', '_')}_Composite_Bands"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Composite Bands
            arcpy.CompositeBands(in_rasters, out_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_pansharpen_weights(self, params):
        """Compute Pansharpen Weights

Calculates an optimal set of pan sharpened weights for new or custom sensor data.

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Dataset; Raster Layer>, "in_panchromatic_image": <Raster Layer>, "band_indexes": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_panchromatic_image = params.get("in_panchromatic_image")
        if in_panchromatic_image is None:
            return {"success": False, "error": "in_panchromatic_image parameter is required"}
        band_indexes = params.get("band_indexes")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Compute_Pansharpen_Weights"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Pansharpen Weights
            arcpy.ComputePansharpenWeights(in_raster, in_panchromatic_image, band_indexes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_color_composite(self, params):
        """Create Color Composite

Creates a three-band raster dataset from a multiband raster dataset.

        params: {"in_raster": <Raster Dataset; Raster Layer>, "out_raster": <Raster Dataset>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        red_expression = params.get("red_expression")
        if red_expression is None:
            return {"success": False, "error": "red_expression parameter is required"}
        green_expression = params.get("green_expression")
        if green_expression is None:
            return {"success": False, "error": "green_expression parameter is required"}
        blue_expression = params.get("blue_expression")
        if blue_expression is None:
            return {"success": False, "error": "blue_expression parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Create_Color_Composite"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Color Composite
            arcpy.CreateColorComposite(in_raster, out_raster, method, red_expression, green_expression, blue_expression)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_ortho_corrected_raster_dataset(self, params):
        """Create Ortho Corrected Raster Dataset

Creates an orthocorrected raster dataset using a digital elevation model (DEM) and control data to accurately align imagery.

        params: {"in_raster": <Raster Dataset; Mosaic Dataset; Mosaic Layer; Raster Layer>, "out_raster_dataset": <Raster Dataset>, "ortho_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster_dataset = params.get("out_raster_dataset")
        if out_raster_dataset is None:
            return {"success": False, "error": "out_raster_dataset parameter is required"}
        ortho_type = params.get("ortho_type")
        if ortho_type is None:
            return {"success": False, "error": "ortho_type parameter is required"}
        constant_elevation = params.get("constant_elevation")
        if constant_elevation is None:
            return {"success": False, "error": "constant_elevation parameter is required"}
        in_dem_raster = params.get("in_dem_raster")
        zfactor = params.get("zfactor")
        zoffset = params.get("zoffset")
        geoid = params.get("geoid")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Create_Ortho_Corrected_Raster_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Ortho Corrected Raster Dataset
            arcpy.CreateOrthoCorrectedRasterDataset(in_raster, out_raster_dataset, ortho_type, constant_elevation, in_dem_raster, zfactor, zoffset, geoid)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_pansharpened_raster_dataset(self, params):
        """Create Pansharpened Raster Dataset

Combines a high-resolution panchromatic raster dataset with a lower-resolution multiband raster dataset to create a high-resolution multiband  raster dataset for visual analysis. Learn more about pan sharpening

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Dataset; Raster Layer>, "red_channel": <Long>, "green_channel": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        red_channel = params.get("red_channel")
        if red_channel is None:
            return {"success": False, "error": "red_channel parameter is required"}
        green_channel = params.get("green_channel")
        if green_channel is None:
            return {"success": False, "error": "green_channel parameter is required"}
        blue_channel = params.get("blue_channel")
        if blue_channel is None:
            return {"success": False, "error": "blue_channel parameter is required"}
        infrared_channel = params.get("infrared_channel")
        out_raster_dataset = params.get("out_raster_dataset")
        if out_raster_dataset is None:
            return {"success": False, "error": "out_raster_dataset parameter is required"}
        in_panchromatic_image = params.get("in_panchromatic_image")
        if in_panchromatic_image is None:
            return {"success": False, "error": "in_panchromatic_image parameter is required"}
        pansharpening_type = params.get("pansharpening_type")
        if pansharpening_type is None:
            return {"success": False, "error": "pansharpening_type parameter is required"}
        red_weight = params.get("red_weight")
        green_weight = params.get("green_weight")
        blue_weight = params.get("blue_weight")
        infrared_weight = params.get("infrared_weight")
        sensor = params.get("sensor")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Create_Pansharpened_Raster_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Pansharpened Raster Dataset
            arcpy.CreatePansharpenedRasterDataset(in_raster, red_channel, green_channel, blue_channel, infrared_channel, out_raster_dataset, in_panchromatic_image, pansharpening_type, red_weight, green_weight, blue_weight, infrared_weight, sensor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_subdataset(self, params):
        """Extract Subdataset

Creates a new raster dataset from a selection of an HDF or NITF dataset.

        params: {"in_raster": <Raster Layer>, "out_raster": <Raster Dataset>, "subdataset_index": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        subdataset_index = params.get("subdataset_index")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Extract_Subdataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Subdataset
            arcpy.ExtractSubdataset(in_raster, out_raster, subdataset_index)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_table_from_raster_function(self, params):
        """Generate Table From Raster Function

Converts a raster function dataset to a table or feature class.  The input raster function should be a raster function designed to output a table or feature class.

        params: {"raster_function": <String; File>, "out_table": <Table>, "raster_function_arguments": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        raster_function = params.get("raster_function")
        if raster_function is None:
            return {"success": False, "error": "raster_function parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        raster_function_arguments = params.get("raster_function_arguments")

            # Generate output name and path
            output_name = f"{raster_function.replace(' ', '_')}_Generate_Table_From_Raster_Function"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Table From Raster Function
            arcpy.GenerateTableFromRasterFunction(raster_function, out_table, raster_function_arguments)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_to_dted(self, params):
        """Raster To DTED

Splits a raster dataset into separate files based on the DTED tiling structure.

        params: {"in_raster": <Raster Layer>, "out_folder": <Folder>, "dted_level": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        dted_level = params.get("dted_level")
        if dted_level is None:
            return {"success": False, "error": "dted_level parameter is required"}
        resampling_type = params.get("resampling_type")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Raster_To_DTED"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster To DTED
            arcpy.RasterToDTED(in_raster, out_folder, dted_level, resampling_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def resample(self, params):
        """Resample

Changes the spatial resolution of a raster dataset and sets rules for aggregating or interpolating values across the new pixel sizes.

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Dataset; Raster Layer>, "out_raster": <Raster Dataset>, "cell_size": <Cell Size XY>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        cell_size = params.get("cell_size")
        resampling_type = params.get("resampling_type")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Resample"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Resample
            arcpy.Resample(in_raster, out_raster, cell_size, resampling_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def split_raster(self, params):
        """Split Raster

Divides a raster dataset  into smaller pieces, by tiles or features from a polygon.

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Layer>, "out_folder": <Folder>, "out_base_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        out_base_name = params.get("out_base_name")
        if out_base_name is None:
            return {"success": False, "error": "out_base_name parameter is required"}
        split_method = params.get("split_method")
        if split_method is None:
            return {"success": False, "error": "split_method parameter is required"}
        format = params.get("format")
        if format is None:
            return {"success": False, "error": "format parameter is required"}
        resampling_type = params.get("resampling_type")
        num_rasters = params.get("num_rasters")
        tile_size = params.get("tile_size")
        overlap = params.get("overlap")
        units = params.get("units")
        cell_size = params.get("cell_size")
        origin = params.get("origin")
        split_polygon_feature_class = params.get("split_polygon_feature_class")
        clip_type = params.get("clip_type")
        template_extent = params.get("template_extent")
        nodata_value = params.get("nodata_value")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Split_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Split Raster
            arcpy.SplitRaster(in_raster, out_folder, out_base_name, split_method, format, resampling_type, num_rasters, tile_size, overlap, units, cell_size, origin, split_polygon_feature_class, clip_type, template_extent, nodata_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_colormap(self, params):
        """Add Colormap

Adds a new color map or replaces an existing color map on a raster dataset.

        params: {"in_raster": <Raster Layer>, "in_template_raster": <Raster Layer>, "input_clr_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_template_raster = params.get("in_template_raster")
        input_clr_file = params.get("input_clr_file")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Add_Colormap"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Colormap
            arcpy.AddColormap(in_raster, in_template_raster, input_clr_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def batch_build_pyramids(self, params):
        """Batch Build Pyramids

Builds pyramids for multiple raster datasets.

        params: {"input_raster_datasets": <Raster Dataset>, "pyramid_levels": <Long>, "skip_first_level": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_raster_datasets = params.get("input_raster_datasets")
        if input_raster_datasets is None:
            return {"success": False, "error": "input_raster_datasets parameter is required"}
        pyramid_levels = params.get("pyramid_levels")
        skip_first_level = params.get("skip_first_level")
        pyramid_resampling_technique = params.get("pyramid_resampling_technique")
        pyramid_compression_type = params.get("pyramid_compression_type")
        compression_quality = params.get("compression_quality")
        skip_existing = params.get("skip_existing")

            # Generate output name and path
            output_name = f"{input_raster_datasets.replace(' ', '_')}_Batch_Build_Pyramids"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Batch Build Pyramids
            arcpy.BatchBuildPyramids(input_raster_datasets, pyramid_levels, skip_first_level, pyramid_resampling_technique, pyramid_compression_type, compression_quality, skip_existing)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def batch_calculate_statistics(self, params):
        """Batch Calculate Statistics

Calculates statistics for  multiple raster datasets.

        params: {"input_raster_datasetsinput_raster_dataset": <Raster Dataset>, "number_of_columns_to_skip": <Long>, "number_of_rows_to_skip": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_raster_datasetsinput_raster_dataset = params.get("input_raster_datasetsinput_raster_dataset")
        if input_raster_datasetsinput_raster_dataset is None:
            return {"success": False, "error": "input_raster_datasetsinput_raster_dataset parameter is required"}
        number_of_columns_to_skip = params.get("number_of_columns_to_skip")
        number_of_rows_to_skip = params.get("number_of_rows_to_skip")
        ignore_valuesignore_value = params.get("ignore_valuesignore_value")
        skip_existing = params.get("skip_existing")

            # Generate output name and path
            output_name = f"{input_raster_datasetsinput_raster_dataset.replace(' ', '_')}_Batch_Calculate_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Batch Calculate Statistics
            arcpy.BatchCalculateStatistics(input_raster_datasetsinput_raster_dataset, number_of_columns_to_skip, number_of_rows_to_skip, ignore_valuesignore_value, skip_existing)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_pyramids(self, params):
        """Build Pyramids

Builds raster pyramids for your raster dataset. This tool can also be used to delete pyramids. To delete pyramids, set the Pyramids Levels parameter to 0.

        params: {"in_raster_dataset": <Raster Dataset; Raster Layer>, "pyramid_level": <Long>, "skip_first": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_dataset = params.get("in_raster_dataset")
        if in_raster_dataset is None:
            return {"success": False, "error": "in_raster_dataset parameter is required"}
        pyramid_level = params.get("pyramid_level")
        skip_first = params.get("skip_first")
        resample_technique = params.get("resample_technique")
        compression_type = params.get("compression_type")
        compression_quality = params.get("compression_quality")
        skip_existing = params.get("skip_existing")

            # Generate output name and path
            output_name = f"{in_raster_dataset.replace(' ', '_')}_Build_Pyramids"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Pyramids
            arcpy.BuildPyramids(in_raster_dataset, pyramid_level, skip_first, resample_technique, compression_type, compression_quality, skip_existing)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_pyramids_and_statistics(self, params):
        """Build Pyramids And Statistics

Traverses a folder structure, building pyramids and calculating statistics for all the raster datasets it contains. It can also build pyramids and calculate statistics for all the items in a mosaic dataset.

        params: {"in_workspace": <Text File; Workspace; Raster Layer; Mosaic Layer>, "include_subdirectories": <Boolean>, "build_pyramids": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        include_subdirectories = params.get("include_subdirectories")
        build_pyramids = params.get("build_pyramids")
        calculate_statistics = params.get("calculate_statistics")
        build_on_source = params.get("build_on_source")
        block_field = params.get("block_field")
        estimate_statistics = params.get("estimate_statistics")
        x_skip_factor = params.get("x_skip_factor")
        y_skip_factor = params.get("y_skip_factor")
        ignore_valuesignore_value = params.get("ignore_valuesignore_value")
        pyramid_level = params.get("pyramid_level")
        skip_first = params.get("skip_first")
        resample_technique = params.get("resample_technique")
        compression_type = params.get("compression_type")
        compression_quality = params.get("compression_quality")
        skip_existing = params.get("skip_existing")
        where_clause = params.get("where_clause")
        sips_mode = params.get("sips_mode")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Build_Pyramids_And_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Pyramids And Statistics
            arcpy.BuildPyramidsAndStatistics(in_workspace, include_subdirectories, build_pyramids, calculate_statistics, build_on_source, block_field, estimate_statistics, x_skip_factor, y_skip_factor, ignore_valuesignore_value, pyramid_level, skip_first, resample_technique, compression_type, compression_quality, skip_existing, where_clause, sips_mode)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_raster_attribute_table(self, params):
        """Build Raster Attribute Table

Adds a raster attribute table to a raster dataset or updates an existing one. This is used primarily with discrete data.

        params: {"in_raster": <Raster Layer>, "overwrite": <Boolean>, "convert_colormap": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        overwrite = params.get("overwrite")
        convert_colormap = params.get("convert_colormap")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Build_Raster_Attribute_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Raster Attribute Table
            arcpy.BuildRasterAttributeTable(in_raster, overwrite, convert_colormap)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_statistics(self, params):
        """Calculate Statistics

Calculates statistics for a raster dataset or a mosaic dataset. Statistics are required for raster and mosaic datasets to perform certain tasks, such as applying a contrast stretch or classifying data.

        params: {"in_raster_dataset": <Mosaic Dataset; Mosaic Layer; Raster Dataset>, "x_skip_factor": <Long>, "y_skip_factor": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_dataset = params.get("in_raster_dataset")
        if in_raster_dataset is None:
            return {"success": False, "error": "in_raster_dataset parameter is required"}
        x_skip_factor = params.get("x_skip_factor")
        y_skip_factor = params.get("y_skip_factor")
        ignore_valuesignore_value = params.get("ignore_valuesignore_value")
        skip_existing = params.get("skip_existing")
        area_of_interest = params.get("area_of_interest")

            # Generate output name and path
            output_name = f"{in_raster_dataset.replace(' ', '_')}_Calculate_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Statistics
            arcpy.CalculateStatistics(in_raster_dataset, x_skip_factor, y_skip_factor, ignore_valuesignore_value, skip_existing, area_of_interest)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_raster_function__template(self, params):
        """Convert Raster Function  Template

Converts a raster function template between formats (rft.xml, json, and binary).

        params: {"in_raster_function_template": <File; String>, "out_raster_function_template_file": <File>, "format": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_function_template = params.get("in_raster_function_template")
        if in_raster_function_template is None:
            return {"success": False, "error": "in_raster_function_template parameter is required"}
        out_raster_function_template_file = params.get("out_raster_function_template_file")
        if out_raster_function_template_file is None:
            return {"success": False, "error": "out_raster_function_template_file parameter is required"}
        format = params.get("format")

            # Generate output name and path
            output_name = f"{in_raster_function_template.replace(' ', '_')}_Convert_Raster_Function__Template"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Raster Function  Template
            arcpy.ConvertRasterFunctionTemplate(in_raster_function_template, out_raster_function_template_file, format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_colormap(self, params):
        """Delete Colormap

Removes the color map associated with a raster dataset.

        params: {"in_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Delete_Colormap"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Colormap
            arcpy.DeleteColormap(in_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_raster_attribute_table(self, params):
        """Delete Raster Attribute Table

Removes the raster attribute table associated with a raster dataset.

        params: {"in_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Delete_Raster_Attribute_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Raster Attribute Table
            arcpy.DeleteRasterAttributeTable(in_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_raster_world_file(self, params):
        """Export Raster World File

Creates a world file based on the pixel size and the location of the upper left pixel.

        params: {"in_raster_dataset": <Raster Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_dataset = params.get("in_raster_dataset")
        if in_raster_dataset is None:
            return {"success": False, "error": "in_raster_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_dataset.replace(' ', '_')}_Export_Raster_World_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Raster World File
            arcpy.ExportRasterWorldFile(in_raster_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def get_cell_value(self, params):
        """Get Cell Value

Retrieves the value of a given pixel using its x, y coordinates.

        params: {"in_raster": <Mosaic Dataset; Mosaic Layer; Raster Layer>, "location_point": <Point>, "band_index": <Value Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        location_point = params.get("location_point")
        if location_point is None:
            return {"success": False, "error": "location_point parameter is required"}
        band_index = params.get("band_index")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Get_Cell_Value"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Get Cell Value
            arcpy.GetCellValue(in_raster, location_point, band_index)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def get_raster_properties(self, params):
        """Get Raster Properties

Retrieves  information from the metadata and descriptive statistics about a raster dataset.

        params: {"in_raster": <Composite Geodataset>, "band_index": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        band_index = params.get("band_index")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Get_Raster_Properties"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Get Raster Properties
            arcpy.GetRasterProperties(in_raster, band_index)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_raster_properties(self, params):
        """Set Raster Properties

Sets the data type, statistics, and NoData values on a raster or mosaic dataset.

        params: {"in_raster": <Mosaic Layer ; Raster Layer>, "data_type": <String>, "statisticsband_index_min_max_mean_std_dev": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        data_type = params.get("data_type")
        statisticsband_index_min_max_mean_std_dev = params.get("statisticsband_index_min_max_mean_std_dev")
        stats_file = params.get("stats_file")
        nodataband_index_nodata_value = params.get("nodataband_index_nodata_value")
        multidimensional_info = params.get("multidimensional_info")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Set_Raster_Properties"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Raster Properties
            arcpy.SetRasterProperties(in_raster, data_type, statisticsband_index_min_max_mean_std_dev, stats_file, nodataband_index_nodata_value, multidimensional_info)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_rule_to_relationship_class(self, params):
        """Add Rule To Relationship Class

Adds a rule to a relationship class. A relationship class is created with one-to-one, one-to-many, or many-to-many cardinality. A relationship class can be defined in more restrictive terms by adding a rule to a relationship class. Once a rule is added to a relationship class, that rule becomes the only valid relationship that can exist. To make other relationship combinations and cardinalities valid, additional relationship rules must be added. Learn more about relationship rules

        params: {"in_rel_class": <Relationship Class>, "origin_subtype": <String>, "origin_minimum": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rel_class = params.get("in_rel_class")
        if in_rel_class is None:
            return {"success": False, "error": "in_rel_class parameter is required"}
        origin_subtype = params.get("origin_subtype")
        origin_minimum = params.get("origin_minimum")
        origin_maximum = params.get("origin_maximum")
        destination_subtype = params.get("destination_subtype")
        destination_minimum = params.get("destination_minimum")
        destination_maximum = params.get("destination_maximum")

            # Generate output name and path
            output_name = f"{in_rel_class.replace(' ', '_')}_Add_Rule_To_Relationship_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Rule To Relationship Class
            arcpy.AddRuleToRelationshipClass(in_rel_class, origin_subtype, origin_minimum, origin_maximum, destination_subtype, destination_minimum, destination_maximum)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_relationship_class(self, params):
        """Create Relationship Class

Creates a relationship class to store an association between fields or features in the origin table and the destination table.

        params: {"origin_table": <Table View>, "destination_table": <Table View>, "out_relationship_class": <Relationship Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        origin_table = params.get("origin_table")
        if origin_table is None:
            return {"success": False, "error": "origin_table parameter is required"}
        destination_table = params.get("destination_table")
        if destination_table is None:
            return {"success": False, "error": "destination_table parameter is required"}
        out_relationship_class = params.get("out_relationship_class")
        if out_relationship_class is None:
            return {"success": False, "error": "out_relationship_class parameter is required"}
        relationship_type = params.get("relationship_type")
        if relationship_type is None:
            return {"success": False, "error": "relationship_type parameter is required"}
        forward_label = params.get("forward_label")
        if forward_label is None:
            return {"success": False, "error": "forward_label parameter is required"}
        backward_label = params.get("backward_label")
        if backward_label is None:
            return {"success": False, "error": "backward_label parameter is required"}
        message_direction = params.get("message_direction")
        if message_direction is None:
            return {"success": False, "error": "message_direction parameter is required"}
        cardinality = params.get("cardinality")
        if cardinality is None:
            return {"success": False, "error": "cardinality parameter is required"}
        attributed = params.get("attributed")
        if attributed is None:
            return {"success": False, "error": "attributed parameter is required"}
        origin_primary_key = params.get("origin_primary_key")
        if origin_primary_key is None:
            return {"success": False, "error": "origin_primary_key parameter is required"}
        origin_foreign_key = params.get("origin_foreign_key")
        if origin_foreign_key is None:
            return {"success": False, "error": "origin_foreign_key parameter is required"}
        destination_primary_key = params.get("destination_primary_key")
        destination_foreign_key = params.get("destination_foreign_key")

            # Generate output name and path
            output_name = f"{origin_table.replace(' ', '_')}_Create_Relationship_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Relationship Class
            arcpy.CreateRelationshipClass(origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, attributed, origin_primary_key, origin_foreign_key, destination_primary_key, destination_foreign_key)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def migrate_relationship_class(self, params):
        """Migrate Relationship Class

Migrates an object ID-based relationship class to a global ID-based relationship class.

        params: {"in_relationship_class": <Relationship Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_relationship_class = params.get("in_relationship_class")
        if in_relationship_class is None:
            return {"success": False, "error": "in_relationship_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_relationship_class.replace(' ', '_')}_Migrate_Relationship_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Migrate Relationship Class
            arcpy.MigrateRelationshipClass(in_relationship_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_rule_from_relationship_class(self, params):
        """Remove Rule From Relationship Class

Removes a rule from a relationship class. Learn more about relationship rules

        params: {"in_rel_class": <Relationship Class>, "origin_subtype": <String>, "destination_subtype": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rel_class = params.get("in_rel_class")
        if in_rel_class is None:
            return {"success": False, "error": "in_rel_class parameter is required"}
        origin_subtype = params.get("origin_subtype")
        destination_subtype = params.get("destination_subtype")
        remove_all = params.get("remove_all")

            # Generate output name and path
            output_name = f"{in_rel_class.replace(' ', '_')}_Remove_Rule_From_Relationship_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Rule From Relationship Class
            arcpy.RemoveRuleFromRelationshipClass(in_rel_class, origin_subtype, destination_subtype, remove_all)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_relationship_class_split_policy(self, params):
        """Set Relationship Class Split Policy

Defines the split policy for related features. Learn more about the split policy for a relationship class

        params: {"in_rel_class": <Relationship Class>, "split_policy": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rel_class = params.get("in_rel_class")
        if in_rel_class is None:
            return {"success": False, "error": "in_rel_class parameter is required"}
        split_policy = params.get("split_policy")
        if split_policy is None:
            return {"success": False, "error": "split_policy parameter is required"}

            # Generate output name and path
            output_name = f"{in_rel_class.replace(' ', '_')}_Set_Relationship_Class_Split_Policy"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Relationship Class Split Policy
            arcpy.SetRelationshipClassSplitPolicy(in_rel_class, split_policy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def table_to_relationship_class(self, params):
        """Table To Relationship Class

Creates an attributed relationship class from the origin, destination, and relationship tables.

        params: {"origin_table": <Table View>, "destination_table": <Table View>, "out_relationship_class": <Relationship Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        origin_table = params.get("origin_table")
        if origin_table is None:
            return {"success": False, "error": "origin_table parameter is required"}
        destination_table = params.get("destination_table")
        if destination_table is None:
            return {"success": False, "error": "destination_table parameter is required"}
        out_relationship_class = params.get("out_relationship_class")
        if out_relationship_class is None:
            return {"success": False, "error": "out_relationship_class parameter is required"}
        relationship_type = params.get("relationship_type")
        if relationship_type is None:
            return {"success": False, "error": "relationship_type parameter is required"}
        forward_label = params.get("forward_label")
        if forward_label is None:
            return {"success": False, "error": "forward_label parameter is required"}
        backward_label = params.get("backward_label")
        if backward_label is None:
            return {"success": False, "error": "backward_label parameter is required"}
        message_direction = params.get("message_direction")
        if message_direction is None:
            return {"success": False, "error": "message_direction parameter is required"}
        cardinality = params.get("cardinality")
        if cardinality is None:
            return {"success": False, "error": "cardinality parameter is required"}
        relationship_table = params.get("relationship_table")
        if relationship_table is None:
            return {"success": False, "error": "relationship_table parameter is required"}
        attribute_fields = params.get("attribute_fields")
        if attribute_fields is None:
            return {"success": False, "error": "attribute_fields parameter is required"}
        origin_primary_key = params.get("origin_primary_key")
        if origin_primary_key is None:
            return {"success": False, "error": "origin_primary_key parameter is required"}
        origin_foreign_key = params.get("origin_foreign_key")
        if origin_foreign_key is None:
            return {"success": False, "error": "origin_foreign_key parameter is required"}
        destination_primary_key = params.get("destination_primary_key")
        if destination_primary_key is None:
            return {"success": False, "error": "destination_primary_key parameter is required"}
        destination_foreign_key = params.get("destination_foreign_key")
        if destination_foreign_key is None:
            return {"success": False, "error": "destination_foreign_key parameter is required"}

            # Generate output name and path
            output_name = f"{origin_table.replace(' ', '_')}_Table_To_Relationship_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Table To Relationship Class
            arcpy.TableToRelationshipClass(origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, relationship_table, attribute_fields, origin_primary_key, origin_foreign_key, destination_primary_key, destination_foreign_key)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_report_to_excel(self, params):
        """Export Report To Excel

Exports an ArcGIS Pro report or a report file to a Microsoft Excel file  (.xlsx). Learn more about reports

        params: {"in_report": <Report; File>, "out_xlsx_file": <File>, "expression": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_report = params.get("in_report")
        if in_report is None:
            return {"success": False, "error": "in_report parameter is required"}
        out_xlsx_file = params.get("out_xlsx_file")
        if out_xlsx_file is None:
            return {"success": False, "error": "out_xlsx_file parameter is required"}
        expression = params.get("expression")
        adjust_row_height = params.get("adjust_row_height")
        merge_cells = params.get("merge_cells")
        remove_vertical_whitespace = params.get("remove_vertical_whitespace")
        display_gridlines = params.get("display_gridlines")
        export_unsupported_formats_as_text = params.get("export_unsupported_formats_as_text")
        sheet_export = params.get("sheet_export")
        page_range_type = params.get("page_range_type")
        custom_page_range = params.get("custom_page_range")
        initial_page_number = params.get("initial_page_number")
        final_page_number = params.get("final_page_number")

            # Generate output name and path
            output_name = f"{in_report.replace(' ', '_')}_Export_Report_To_Excel"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Report To Excel
            arcpy.ExportReportToExcel(in_report, out_xlsx_file, expression, adjust_row_height, merge_cells, remove_vertical_whitespace, display_gridlines, export_unsupported_formats_as_text, sheet_export, page_range_type, custom_page_range, initial_page_number, final_page_number)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_report_to_pdf(self, params):
        """Export Report To PDF

Exports an ArcGIS Pro report or a report file (.rptx) to a .pdf file. Learn more about reports

        params: {"in_report": <Report; File>, "out_pdf_file": <File>, "expression": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_report = params.get("in_report")
        if in_report is None:
            return {"success": False, "error": "in_report parameter is required"}
        out_pdf_file = params.get("out_pdf_file")
        if out_pdf_file is None:
            return {"success": False, "error": "out_pdf_file parameter is required"}
        expression = params.get("expression")
        resolution = params.get("resolution")
        image_quality = params.get("image_quality")
        embed_font = params.get("embed_font")
        compress_vector_graphics = params.get("compress_vector_graphics")
        image_compression = params.get("image_compression")
        password_protect = params.get("password_protect")
        pdf_password = params.get("pdf_password")
        page_range_type = params.get("page_range_type")
        custom_page_range = params.get("custom_page_range")
        initial_page_number = params.get("initial_page_number")
        final_page_number = params.get("final_page_number")
        selection_symbology = params.get("selection_symbology")

            # Generate output name and path
            output_name = f"{in_report.replace(' ', '_')}_Export_Report_To_PDF"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Report To PDF
            arcpy.ExportReportToPDF(in_report, out_pdf_file, expression, resolution, image_quality, embed_font, compress_vector_graphics, image_compression, password_protect, pdf_password, page_range_type, custom_page_range, initial_page_number, final_page_number, selection_symbology)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_fishnet(self, params):
        """Create Fishnet

Creates a fishnet of rectangular cells.  The output can be polyline or polygon features. Learn more about how Create Fishnet works

        params: {"out_feature_class": <Feature Class>, "origin_coord": <Point>, "y_axis_coord": <Point>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        origin_coord = params.get("origin_coord")
        if origin_coord is None:
            return {"success": False, "error": "origin_coord parameter is required"}
        y_axis_coord = params.get("y_axis_coord")
        if y_axis_coord is None:
            return {"success": False, "error": "y_axis_coord parameter is required"}
        cell_width = params.get("cell_width")
        if cell_width is None:
            return {"success": False, "error": "cell_width parameter is required"}
        cell_height = params.get("cell_height")
        if cell_height is None:
            return {"success": False, "error": "cell_height parameter is required"}
        number_rows = params.get("number_rows")
        if number_rows is None:
            return {"success": False, "error": "number_rows parameter is required"}
        number_columns = params.get("number_columns")
        if number_columns is None:
            return {"success": False, "error": "number_columns parameter is required"}
        corner_coord = params.get("corner_coord")
        labels = params.get("labels")
        template = params.get("template")
        geometry_type = params.get("geometry_type")

            # Generate output name and path
            output_name = f"{out_feature_class.replace(' ', '_')}_Create_Fishnet"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Fishnet
            arcpy.CreateFishnet(out_feature_class, origin_coord, y_axis_coord, cell_width, cell_height, number_rows, number_columns, corner_coord, labels, template, geometry_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_random_points(self, params):
        """Create Random Points

Creates a specified number of random point features. Random points can be generated in an extent window, inside polygon features, on point features, or along line features. Learn more about how Create Random Points works

        params: {"out_path": <Feature Dataset;Workspace>, "out_name": <String>, "constraining_feature_class": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        constraining_feature_class = params.get("constraining_feature_class")
        constraining_extent = params.get("constraining_extent")
        number_of_points_or_field = params.get("number_of_points_or_field")
        minimum_allowed_distance = params.get("minimum_allowed_distance")
        create_multipoint_output = params.get("create_multipoint_output")
        multipoint_size = params.get("multipoint_size")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Random_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Random Points
            arcpy.CreateRandomPoints(out_path, out_name, constraining_feature_class, constraining_extent, number_of_points_or_field, minimum_allowed_distance, create_multipoint_output, multipoint_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_spatially_balanced_points(self, params):
        """Create Spatially Balanced Points

Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design. This tool is typically used for designing a monitoring network by suggesting locations to take samples, and a preference for particular locations can be defined using an inclusion probability raster. Learn more about how Create Spatially Balanced Points works

        params: {"in_probability_raster": <Raster Layer; Mosaic Layer>, "number_output_points": <Long>, "out_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_probability_raster = params.get("in_probability_raster")
        if in_probability_raster is None:
            return {"success": False, "error": "in_probability_raster parameter is required"}
        number_output_points = params.get("number_output_points")
        if number_output_points is None:
            return {"success": False, "error": "number_output_points parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_probability_raster.replace(' ', '_')}_Create_Spatially_Balanced_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Spatially Balanced Points
            arcpy.CreateSpatiallyBalancedPoints(in_probability_raster, number_output_points, out_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_spatial_sampling_locations(self, params):
        """Create Spatial Sampling Locations

Creates sample locations within a continuous study area using simple random, stratified, systematic (gridded), or cluster sampling designs. Sampling is the process of selecting individuals from a population to study them and make inferences about the entire population.  Continuous spatial sampling treats the population as a continuous area from which any location or area can be sampled.  For example, you can use this tool to create sample locations for trees within a dense forest or to collect soil moisture measurements in a crop field.  This tool is not appropriate for sampling discrete populations such as households, animals, or cities.

        params: {"in_study_area": <Feature Layer; Raster Layer>, "out_features": <Feature Class>, "sampling_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_study_area = params.get("in_study_area")
        if in_study_area is None:
            return {"success": False, "error": "in_study_area parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        sampling_method = params.get("sampling_method")
        strata_id_field = params.get("strata_id_field")
        strata_count_method = params.get("strata_count_method")
        bin_shape = params.get("bin_shape")
        bin_size = params.get("bin_size")
        h3_resolution = params.get("h3_resolution")
        num_samples = params.get("num_samples")
        num_samples_per_strata = params.get("num_samples_per_strata")
        population_field = params.get("population_field")
        geometry_type = params.get("geometry_type")
        min_distance = params.get("min_distance")
        spatial_relationship = params.get("spatial_relationship")

            # Generate output name and path
            output_name = f"{in_study_area.replace(' ', '_')}_Create_Spatial_Sampling_Locations"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Spatial Sampling Locations
            arcpy.CreateSpatialSamplingLocations(in_study_area, out_features, sampling_method, strata_id_field, strata_count_method, bin_shape, bin_size, h3_resolution, num_samples, num_samples_per_strata, population_field, geometry_type, min_distance, spatial_relationship)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_points_along_lines(self, params):
        """Generate Points Along Lines

Creates point features along lines or polygons.

        params: {"input_features": <Feature Layer>, "output_feature_class": <Feature Class>, "point_placement": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        point_placement = params.get("point_placement")
        if point_placement is None:
            return {"success": False, "error": "point_placement parameter is required"}
        distance = params.get("distance")
        percentage = params.get("percentage")
        include_end_points = params.get("include_end_points")
        add_chainage_fields = params.get("add_chainage_fields")
        distance_field = params.get("distance_field")
        distance_method = params.get("distance_method")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Generate_Points_Along_Lines"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Points Along Lines
            arcpy.GeneratePointsAlongLines(input_features, output_feature_class, point_placement, distance, percentage, include_end_points, add_chainage_fields, distance_field, distance_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_rectangles_along_lines(self, params):
        """Generate Rectangles Along Lines

Creates a series of rectangular polygons that follow a single linear feature or a group of linear features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "length_along_line": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        length_along_line = params.get("length_along_line")
        spatial_sort_method = params.get("spatial_sort_method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generate_Rectangles_Along_Lines"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Rectangles Along Lines
            arcpy.GenerateRectanglesAlongLines(in_features, out_feature_class, length_along_line, spatial_sort_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_tessellation(self, params):
        """Generate Tessellation

Generates a tessellated grid of regular polygon features to cover a given extent.  The tessellation can be of triangles, squares, diamonds, hexagons, H3 hexagons, or transverse hexagons.

        params: {"output_feature_class": <Feature Class>, "extent": <Extent>, "shape_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        extent = params.get("extent")
        if extent is None:
            return {"success": False, "error": "extent parameter is required"}
        shape_type = params.get("shape_type")
        size = params.get("size")
        spatial_reference = params.get("spatial_reference")
        h3_resolution = params.get("h3_resolution")

            # Generate output name and path
            output_name = f"{output_feature_class.replace(' ', '_')}_Generate_Tessellation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Tessellation
            arcpy.GenerateTessellation(output_feature_class, extent, shape_type, size, spatial_reference, h3_resolution)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_transects_along_lines(self, params):
        """Generate Transects Along Lines

Creates perpendicular transect lines at a regular interval along lines.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "interval": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        interval = params.get("interval")
        if interval is None:
            return {"success": False, "error": "interval parameter is required"}
        transect_length = params.get("transect_length")
        if transect_length is None:
            return {"success": False, "error": "transect_length parameter is required"}
        include_ends = params.get("include_ends")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generate_Transects_Along_Lines"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Transects Along Lines
            arcpy.GenerateTransectsAlongLines(in_features, out_feature_class, interval, transect_length, include_ends)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def subset_features(self, params):
        """Subset Features

Divides the records of a feature class or table into two subsets: one subset to be used as training data, and one subset to be used as test features to compare and validate the output surface.

        params: {"in_features": <Table View>, "out_training_feature_class": <Feature Class; Table>, "out_test_feature_class": <Feature Class; Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_training_feature_class = params.get("out_training_feature_class")
        if out_training_feature_class is None:
            return {"success": False, "error": "out_training_feature_class parameter is required"}
        out_test_feature_class = params.get("out_test_feature_class")
        size_of_training_dataset = params.get("size_of_training_dataset")
        subset_size_units = params.get("subset_size_units")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Subset_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Subset Features
            arcpy.SubsetFeatures(in_features, out_training_feature_class, out_test_feature_class, size_of_training_dataset, subset_size_units)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_subtype(self, params):
        """Add Subtype

Adds a new subtype to the subtypes in the input table.

        params: {"in_table": <Table View>, "subtype_code": <Long>, "subtype_description": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        subtype_code = params.get("subtype_code")
        if subtype_code is None:
            return {"success": False, "error": "subtype_code parameter is required"}
        subtype_description = params.get("subtype_description")
        if subtype_description is None:
            return {"success": False, "error": "subtype_description parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Add_Subtype"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Subtype
            arcpy.AddSubtype(in_table, subtype_code, subtype_description)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_subtype(self, params):
        """Remove Subtype

Removes a subtype from the input table using its code.

        params: {"in_table": <Table View>, "subtype_code": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        subtype_code = params.get("subtype_code")
        if subtype_code is None:
            return {"success": False, "error": "subtype_code parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Remove_Subtype"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Subtype
            arcpy.RemoveSubtype(in_table, subtype_code)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_default_subtype(self, params):
        """Set Default Subtype

Sets the default value or code for the input table's subtype.

        params: {"in_table": <Table View>, "subtype_code": <Long>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        subtype_code = params.get("subtype_code")
        if subtype_code is None:
            return {"success": False, "error": "subtype_code parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Set_Default_Subtype"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Default Subtype
            arcpy.SetDefaultSubtype(in_table, subtype_code)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_subtype_field(self, params):
        """Set Subtype Field

Defines the field in the input table or feature class that stores the subtype codes.

        params: {"in_table": <Table View>, "field": <Field>, "clear_value": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field = params.get("field")
        clear_value = params.get("clear_value")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Set_Subtype_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Subtype Field
            arcpy.SetSubtypeField(in_table, field, clear_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze(self, params):
        """Analyze

Updates database statistics of business tables, feature tables, and delta tables, along with the statistics of those tables' indexes.

        params: {"in_dataset": <Layer; Table View; Dataset>, "components": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        components = params.get("components")
        if components is None:
            return {"success": False, "error": "components parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Analyze"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Analyze
            arcpy.Analyze(in_dataset, components)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy_rows(self, params):
        """Copy Rows

Copies the rows of a table  to a different table.

        params: {"in_rows": <Table View; Raster Layer>, "out_table": <Table>, "config_keyword": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rows = params.get("in_rows")
        if in_rows is None:
            return {"success": False, "error": "in_rows parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{in_rows.replace(' ', '_')}_Copy_Rows"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy Rows
            arcpy.CopyRows(in_rows, out_table, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_table(self, params):
        """Create Table

Creates a geodatabase table or a dBASE table.

        params: {"out_path": <Workspace>, "out_name": <String>, "template": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        template = params.get("template")
        config_keyword = params.get("config_keyword")
        out_alias = params.get("out_alias")
        oid_type = params.get("oid_type")
        if oid_type is None:
            return {"success": False, "error": "oid_type parameter is required"}

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Table
            arcpy.CreateTable(out_path, out_name, template, config_keyword, out_alias, oid_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_unregistered_table(self, params):
        """Create Unregistered Table

Creates an empty table in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The table is not registered with the geodatabase.

        params: {"out_path": <Workspace>, "out_name": <String>, "template": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        template = params.get("template")
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{out_path.replace(' ', '_')}_Create_Unregistered_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Unregistered Table
            arcpy.CreateUnregisteredTable(out_path, out_name, template, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_rows(self, params):
        """Delete Rows

Deletes all or the selected subset of rows from the input. The deletion of all rows or a subset of rows depends on the following:If the input is a feature class or table, all rows will be deleted.
If the input is a layer or table view with no selection, all rows
will be deleted.
If the input is a layer or table view with a selection, only the
selected rows will be deleted.

        params: {"in_rows": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rows = params.get("in_rows")
        if in_rows is None:
            return {"success": False, "error": "in_rows parameter is required"}

            # Generate output name and path
            output_name = f"{in_rows.replace(' ', '_')}_Delete_Rows"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Rows
            arcpy.DeleteRows(in_rows)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def get_count(self, params):
        """Get Count

Returns the total number of rows for a table.

        params: {"in_rows": <Table View; Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rows = params.get("in_rows")
        if in_rows is None:
            return {"success": False, "error": "in_rows parameter is required"}

            # Generate output name and path
            output_name = f"{in_rows.replace(' ', '_')}_Get_Count"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Get Count
            arcpy.GetCount(in_rows)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pivot_table(self, params):
        """Pivot Table

Creates a table from the input table by reducing redundancy  in records and flattening one-to-many relationships.

        params: {"in_table": <Table View>, "fields": <Field>, "pivot_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}
        pivot_field = params.get("pivot_field")
        if pivot_field is None:
            return {"success": False, "error": "pivot_field parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Pivot_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pivot Table
            arcpy.PivotTable(in_table, fields, pivot_field, value_field, out_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def truncate_table(self, params):
        """Truncate Table

Removes all rows from a database table or feature class using truncate procedures in the database.

        params: {"in_table": <Table View>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Truncate_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Truncate Table
            arcpy.TruncateTable(in_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_tile_cache(self, params):
        """Export Tile Cache

Exports tiles from an existing tile cache to a new tile cache or a tile package. The tiles can be either independently imported into other caches or accessed from ArcGIS Pro or mobile devices.

        params: {"in_cache_source": <Raster Layer; Raster Dataset>, "in_target_cache_folder": <Folder>, "in_target_cache_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_cache_source = params.get("in_cache_source")
        if in_cache_source is None:
            return {"success": False, "error": "in_cache_source parameter is required"}
        in_target_cache_folder = params.get("in_target_cache_folder")
        if in_target_cache_folder is None:
            return {"success": False, "error": "in_target_cache_folder parameter is required"}
        in_target_cache_name = params.get("in_target_cache_name")
        if in_target_cache_name is None:
            return {"success": False, "error": "in_target_cache_name parameter is required"}
        export_cache_type = params.get("export_cache_type")
        storage_format_type = params.get("storage_format_type")
        scalesscale = params.get("scalesscale")
        area_of_interest = params.get("area_of_interest")

            # Generate output name and path
            output_name = f"{in_cache_source.replace(' ', '_')}_Export_Tile_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Tile Cache
            arcpy.ExportTileCache(in_cache_source, in_target_cache_folder, in_target_cache_name, export_cache_type, storage_format_type, scalesscale, area_of_interest)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_tile_cache_tiling_scheme(self, params):
        """Generate Tile Cache Tiling Scheme

Creates a tiling scheme file based on the information from the source dataset. The tiling scheme file will then be used in the Manage Tile Cache tool when creating cache tiles. This tool can be used to edit the properties of an existing tiling scheme, such as tile format, storage format, tile size, and so on. In addition, you can also use it to add new scale levels to an existing tiling scheme.

        params: {"in_dataset": <Raster Layer; Mosaic Layer; Map>, "out_tiling_scheme": <File>, "tiling_scheme_generation_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_tiling_scheme = params.get("out_tiling_scheme")
        if out_tiling_scheme is None:
            return {"success": False, "error": "out_tiling_scheme parameter is required"}
        tiling_scheme_generation_method = params.get("tiling_scheme_generation_method")
        if tiling_scheme_generation_method is None:
            return {"success": False, "error": "tiling_scheme_generation_method parameter is required"}
        number_of_scales = params.get("number_of_scales")
        if number_of_scales is None:
            return {"success": False, "error": "number_of_scales parameter is required"}
        predefined_tiling_scheme = params.get("predefined_tiling_scheme")
        scalesscale = params.get("scalesscale")
        scales_type = params.get("scales_type")
        tile_origin = params.get("tile_origin")
        dpi = params.get("dpi")
        tile_size = params.get("tile_size")
        tile_format = params.get("tile_format")
        tile_compression_quality = params.get("tile_compression_quality")
        storage_format = params.get("storage_format")
        lerc_error = params.get("lerc_error")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Generate_Tile_Cache_Tiling_Scheme"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Tile Cache Tiling Scheme
            arcpy.GenerateTileCacheTilingScheme(in_dataset, out_tiling_scheme, tiling_scheme_generation_method, number_of_scales, predefined_tiling_scheme, scalesscale, scales_type, tile_origin, dpi, tile_size, tile_format, tile_compression_quality, storage_format, lerc_error)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_tile_cache(self, params):
        """Import Tile Cache

Imports tiles from an existing tile cache or a tile package. The target cache must have the same tiling scheme, spatial reference, and  storage format as the source tile cache.

        params: {"in_cache_target": <Raster Layer>, "in_cache_source": <Raster Layer; File>, "scales": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_cache_target = params.get("in_cache_target")
        if in_cache_target is None:
            return {"success": False, "error": "in_cache_target parameter is required"}
        in_cache_source = params.get("in_cache_source")
        if in_cache_source is None:
            return {"success": False, "error": "in_cache_source parameter is required"}
        scales = params.get("scales")
        area_of_interest = params.get("area_of_interest")
        overwrite = params.get("overwrite")

            # Generate output name and path
            output_name = f"{in_cache_target.replace(' ', '_')}_Import_Tile_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import Tile Cache
            arcpy.ImportTileCache(in_cache_target, in_cache_source, scales, area_of_interest, overwrite)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def manage_tile_cache(self, params):
        """Manage Tile Cache

Creates a tile cache or updates tiles in an existing tile cache. You can use this tool to create tiles, replace missing tiles, overwrite outdated tiles, and delete tiles.

        params: {"in_cache_location": <Folder; Raster Layer>, "manage_mode": <String>, "in_cache_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_cache_location = params.get("in_cache_location")
        if in_cache_location is None:
            return {"success": False, "error": "in_cache_location parameter is required"}
        manage_mode = params.get("manage_mode")
        if manage_mode is None:
            return {"success": False, "error": "manage_mode parameter is required"}
        in_cache_name = params.get("in_cache_name")
        in_datasource = params.get("in_datasource")
        tiling_scheme = params.get("tiling_scheme")
        import_tiling_scheme = params.get("import_tiling_scheme")
        scalesscale = params.get("scalesscale")
        area_of_interest = params.get("area_of_interest")
        max_cell_size = params.get("max_cell_size")
        min_cached_scale = params.get("min_cached_scale")
        max_cached_scale = params.get("max_cached_scale")
        ready_to_serve_format = params.get("ready_to_serve_format")

            # Generate output name and path
            output_name = f"{in_cache_location.replace(' ', '_')}_Manage_Tile_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Manage Tile Cache
            arcpy.ManageTileCache(in_cache_location, manage_mode, in_cache_name, in_datasource, tiling_scheme, import_tiling_scheme, scalesscale, area_of_interest, max_cell_size, min_cached_scale, max_cached_scale, ready_to_serve_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_feature_class_to_topology(self, params):
        """Add Feature Class To Topology

Adds a feature class to a topology.

        params: {"in_topology": <Topology Layer>, "in_featureclass": <Feature Layer>, "xy_rank": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        in_featureclass = params.get("in_featureclass")
        if in_featureclass is None:
            return {"success": False, "error": "in_featureclass parameter is required"}
        xy_rank = params.get("xy_rank")
        if xy_rank is None:
            return {"success": False, "error": "xy_rank parameter is required"}
        z_rank = params.get("z_rank")
        if z_rank is None:
            return {"success": False, "error": "z_rank parameter is required"}

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Add_Feature_Class_To_Topology"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Feature Class To Topology
            arcpy.AddFeatureClassToTopology(in_topology, in_featureclass, xy_rank, z_rank)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_rule_to_topology(self, params):
        """Add Rule To Topology

Adds a rule to a topology. The rules you choose to add depend on the spatial relationships that you wish to monitor for the feature classes that participate in the topology. For a complete list and description of the available topology rules, see geodatabase topology rules and topology error fixes for points, lines, or polygons.

        params: {"in_topology": <Topology Layer>, "rule_type": <String>, "in_featureclass": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        rule_type = params.get("rule_type")
        if rule_type is None:
            return {"success": False, "error": "rule_type parameter is required"}
        in_featureclass = params.get("in_featureclass")
        if in_featureclass is None:
            return {"success": False, "error": "in_featureclass parameter is required"}
        subtype = params.get("subtype")
        in_featureclass2 = params.get("in_featureclass2")
        subtype2 = params.get("subtype2")

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Add_Rule_To_Topology"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Rule To Topology
            arcpy.AddRuleToTopology(in_topology, rule_type, in_featureclass, subtype, in_featureclass2, subtype2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_topology(self, params):
        """Create Topology

Creates a topology. The topology will not contain any feature classes or rules. Use the Add Feature Class To Topology and the Add Rule To Topology tools to add feature classes and rules to the topology.

        params: {"in_dataset": <Feature Dataset>, "out_name": <String>, "in_cluster_tolerance": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        in_cluster_tolerance = params.get("in_cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Create_Topology"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Topology
            arcpy.CreateTopology(in_dataset, out_name, in_cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_topology_errors(self, params):
        """Export Topology Errors

Exports the errors and exceptions from a geodatabase topology to the target geodatabase.  All information associated with the errors and exceptions, such as the features referenced by the error or exception, is exported. Once the errors and exceptions are exported, the feature classes can be accessed using any license level of ArcGIS.  The feature classes can be used with the Select Layer By Location tool and can be shared with other users who do not have access to the topology.

        params: {"in_topology": <Topology Layer>, "out_path": <Feature Dataset; Workspace>, "out_basename": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        out_path = params.get("out_path")
        if out_path is None:
            return {"success": False, "error": "out_path parameter is required"}
        out_basename = params.get("out_basename")
        if out_basename is None:
            return {"success": False, "error": "out_basename parameter is required"}

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Export_Topology_Errors"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Topology Errors
            arcpy.ExportTopologyErrors(in_topology, out_path, out_basename)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select_layer_by_location(self, params):
        """Select Layer By Location

Selects features  based on a spatial relationship to features in another dataset or the same dataset. Each feature in the Input Features parameter is evaluated using the features in the  Selecting Features parameter. If the specified Relationship parameter value is met, the input feature is selected. Learn more about Select By Location including image examples of relationships

        params: {"in_layer": <Feature Layer; Raster Layer; Mosaic Layer>, "overlap_type": <String>, "select_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        overlap_type = params.get("overlap_type")
        select_features = params.get("select_features")
        search_distance = params.get("search_distance")
        selection_type = params.get("selection_type")
        invert_spatial_relationship = params.get("invert_spatial_relationship")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Select_Layer_By_Location"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select Layer By Location
            arcpy.SelectLayerByLocation(in_layer, overlap_type, select_features, search_distance, selection_type, invert_spatial_relationship)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_feature_class_from_topology(self, params):
        """Remove Feature Class From Topology

Removes a feature class from a topology.

        params: {"in_topology": <Topology Layer>, "in_featureclass": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        in_featureclass = params.get("in_featureclass")
        if in_featureclass is None:
            return {"success": False, "error": "in_featureclass parameter is required"}

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Remove_Feature_Class_From_Topology"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Feature Class From Topology
            arcpy.RemoveFeatureClassFromTopology(in_topology, in_featureclass)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_rule_from_topology(self, params):
        """Remove Rule From Topology

Removes a rule from a topology.

        params: {"in_topology": <Topology Layer>, "in_rule": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        in_rule = params.get("in_rule")
        if in_rule is None:
            return {"success": False, "error": "in_rule parameter is required"}

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Remove_Rule_From_Topology"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Rule From Topology
            arcpy.RemoveRuleFromTopology(in_topology, in_rule)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_cluster_tolerance(self, params):
        """Set Cluster Tolerance

Sets the cluster tolerance of a topology.

        params: {"in_topology": <Topology Layer>, "cluster_tolerance": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        cluster_tolerance = params.get("cluster_tolerance")
        if cluster_tolerance is None:
            return {"success": False, "error": "cluster_tolerance parameter is required"}

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Set_Cluster_Tolerance"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Cluster Tolerance
            arcpy.SetClusterTolerance(in_topology, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def validate_topology(self, params):
        """Validate Topology

Validates a geodatabase topology. This tool performs the following operations:Cracking and clustering of feature vertices to find features that share geometry (have common coordinates)Inserting common coordinate vertices into features that share geometryRunning a set of integrity checks to identify any violations of the rules that have been defined for the topology

        params: {"in_topology": <Topology Layer>, "visible_extent": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topology = params.get("in_topology")
        if in_topology is None:
            return {"success": False, "error": "in_topology parameter is required"}
        visible_extent = params.get("visible_extent")

            # Generate output name and path
            output_name = f"{in_topology.replace(' ', '_')}_Validate_Topology"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Validate Topology
            arcpy.ValidateTopology(in_topology, visible_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_data_to_trajectory_dataset(self, params):
        """Add Data To Trajectory Dataset

Adds trajectory data to an existing  trajectory dataset.

        params: {"in_trajectory_dataset": <Trajectory Layer>, "trajectory_type": <Raster Type>, "input_path": <Workspace; File; WCS Coverage; Image Service; Map Server; WMS Map; Table View; Raster Layer; Mosaic Layer; Terrain Layer; LAS Dataset Layer; Layer File; WMTS Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_trajectory_dataset = params.get("in_trajectory_dataset")
        if in_trajectory_dataset is None:
            return {"success": False, "error": "in_trajectory_dataset parameter is required"}
        trajectory_type = params.get("trajectory_type")
        if trajectory_type is None:
            return {"success": False, "error": "trajectory_type parameter is required"}
        input_path = params.get("input_path")
        if input_path is None:
            return {"success": False, "error": "input_path parameter is required"}
        filter = params.get("filter")
        sub_folder = params.get("sub_folder")
        aux_inputs = params.get("aux_inputs")

            # Generate output name and path
            output_name = f"{in_trajectory_dataset.replace(' ', '_')}_Add_Data_To_Trajectory_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Data To Trajectory Dataset
            arcpy.AddDataToTrajectoryDataset(in_trajectory_dataset, trajectory_type, input_path, filter, sub_folder, aux_inputs)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_trajectory_dataset(self, params):
        """Create Trajectory Dataset

Creates an empty trajectory dataset in a geodatabase.

        params: {"in_workspace": <Workspace>, "in_dataset_name": <String>, "coordinate_system": <Coordinate System>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        in_dataset_name = params.get("in_dataset_name")
        if in_dataset_name is None:
            return {"success": False, "error": "in_dataset_name parameter is required"}
        coordinate_system = params.get("coordinate_system")
        if coordinate_system is None:
            return {"success": False, "error": "coordinate_system parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Create_Trajectory_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Trajectory Dataset
            arcpy.CreateTrajectoryDataset(in_workspace, in_dataset_name, coordinate_system)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def repair_trajectory_dataset_paths(self, params):
        """Repair Trajectory Dataset Paths

Repairs paths to source data for a trajectory dataset.

        params: {"in_trajectory_dataset": <Trajectory Layer>, "paths_list": <Value Table>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_trajectory_dataset = params.get("in_trajectory_dataset")
        if in_trajectory_dataset is None:
            return {"success": False, "error": "in_trajectory_dataset parameter is required"}
        paths_list = params.get("paths_list")
        if paths_list is None:
            return {"success": False, "error": "paths_list parameter is required"}
        where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{in_trajectory_dataset.replace(' ', '_')}_Repair_Trajectory_Dataset_Paths"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Repair Trajectory Dataset Paths
            arcpy.RepairTrajectoryDatasetPaths(in_trajectory_dataset, paths_list, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_field_conflict_filter(self, params):
        """Add Field Conflict Filter

Adds a field conflict filter for a given field in a geodatabase table or feature class. Field conflict filters can be applied to versioned tables or feature classes to prevent conflicts from being identified when the same attribute is updated in the parent and child versions. Field conflict filters only apply for reconciles in which conflicts are defined by attribute.

        params: {"table": <Table View>, "fields": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        table = params.get("table")
        if table is None:
            return {"success": False, "error": "table parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}

            # Generate output name and path
            output_name = f"{table.replace(' ', '_')}_Add_Field_Conflict_Filter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Field Conflict Filter
            arcpy.AddFieldConflictFilter(table, fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def alter_version(self, params):
        """Alter Version

Alters the properties of a geodatabase version.

        params: {"in_workspace": <Workspace>, "in_version": <String>, "name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        in_version = params.get("in_version")
        if in_version is None:
            return {"success": False, "error": "in_version parameter is required"}
        name = params.get("name")
        description = params.get("description")
        access = params.get("access")
        target_owner = params.get("target_owner")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Alter_Version"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Alter Version
            arcpy.AlterVersion(in_workspace, in_version, name, description, access, target_owner)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def change_version(self, params):
        """Change Version

Modifies the workspace of a  layer or table view to connect to the specified version.

        params: {"in_features": <Feature Layer; Table View; Topology Layer; Parcel Layer; Utility Network Layer; Trace Network Layer>, "version_type": <String>, "version_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        version_type = params.get("version_type")
        if version_type is None:
            return {"success": False, "error": "version_type parameter is required"}
        version_name = params.get("version_name")
        date = params.get("date")
        include_participating = params.get("include_participating")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Change_Version"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Change Version
            arcpy.ChangeVersion(in_features, version_type, version_name, date, include_participating)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_version(self, params):
        """Create Version

Creates a new version in a specified geodatabase or feature service.

        params: {"in_workspace": <Workspace>, "parent_version": <String>, "version_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        parent_version = params.get("parent_version")
        if parent_version is None:
            return {"success": False, "error": "parent_version parameter is required"}
        version_name = params.get("version_name")
        if version_name is None:
            return {"success": False, "error": "version_name parameter is required"}
        access_permission = params.get("access_permission")
        version_description = params.get("version_description")

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Create_Version"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Version
            arcpy.CreateVersion(in_workspace, parent_version, version_name, access_permission, version_description)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_version(self, params):
        """Delete Version

Deletes the specified version from the input enterprise geodatabase.

        params: {"in_workspace": <Workspace>, "version_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}
        version_name = params.get("version_name")
        if version_name is None:
            return {"success": False, "error": "version_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Delete_Version"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Version
            arcpy.DeleteVersion(in_workspace, version_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def prune_branch_history(self, params):
        """Prune Branch History

Removes retired archive records from branch-versioned datasets. Learn more about prune branch history

        params: {"in_dataset": <Table View; Feature Dataset>, "out_log": <File>, "report_only": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_log = params.get("out_log")
        if out_log is None:
            return {"success": False, "error": "out_log parameter is required"}
        report_only = params.get("report_only")
        system_tables_only = params.get("system_tables_only")
        if system_tables_only is None:
            return {"success": False, "error": "system_tables_only parameter is required"}
        prune_before_date = params.get("prune_before_date")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Prune_Branch_History"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Prune Branch History
            arcpy.PruneBranchHistory(in_dataset, out_log, report_only, system_tables_only, prune_before_date)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def reconcile_versions(self, params):
        """Reconcile Versions

Reconciles a version or multiple versions with a target version. Learn more about how to reconcile and post versions

        params: {"input_database": <Workspace>, "reconcile_mode": <String>, "target_version": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        reconcile_mode = params.get("reconcile_mode")
        if reconcile_mode is None:
            return {"success": False, "error": "reconcile_mode parameter is required"}
        target_version = params.get("target_version")
        edit_versions = params.get("edit_versions")
        acquire_locks = params.get("acquire_locks")
        abort_if_conflicts = params.get("abort_if_conflicts")
        conflict_definition = params.get("conflict_definition")
        conflict_resolution = params.get("conflict_resolution")
        out_log = params.get("out_log")
        proceed_if_conflicts_not_reviewed = params.get("proceed_if_conflicts_not_reviewed")
        reconcile_checkout_versions = params.get("reconcile_checkout_versions")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Reconcile_Versions"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Reconcile Versions
            arcpy.ReconcileVersions(input_database, reconcile_mode, target_version, edit_versions, acquire_locks, abort_if_conflicts, conflict_definition, conflict_resolution, out_log, proceed_if_conflicts_not_reviewed, reconcile_checkout_versions)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def register_as_versioned(self, params):
        """Register As Versioned

Registers an enterprise geodatabase dataset as versioned. Learn more about how to register data as branch versioned and traditional versioned.

        params: {"in_dataset": <Table View; Feature Dataset>, "edit_to_base": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        edit_to_base = params.get("edit_to_base")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Register_As_Versioned"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Register As Versioned
            arcpy.RegisterAsVersioned(in_dataset, edit_to_base)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_field_conflict_filter(self, params):
        """Remove Field Conflict Filter

Removes a field conflict filter for a given field in a geodatabase table or feature class. Field conflict filters can be applied to versioned tables or feature classes to prevent conflicts from being identified when the same attribute is updated in the parent and child versions. Field conflict filters only apply for reconciles in which conflicts are defined by attribute.

        params: {"table": <Table View>, "fields": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        table = params.get("table")
        if table is None:
            return {"success": False, "error": "table parameter is required"}
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}

            # Generate output name and path
            output_name = f"{table.replace(' ', '_')}_Remove_Field_Conflict_Filter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Field Conflict Filter
            arcpy.RemoveFieldConflictFilter(table, fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def unregister_as_versioned(self, params):
        """Unregister As Versioned

Unregisters an enterprise geodatabase dataset as versioned.

        params: {"in_dataset": <Table View; Feature Dataset>, "keep_edit": <Boolean>, "compress_default": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        keep_edit = params.get("keep_edit")
        compress_default = params.get("compress_default")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Unregister_As_Versioned"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Unregister As Versioned
            arcpy.UnregisterAsVersioned(in_dataset, keep_edit, compress_default)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def clear_workspace_cache(self, params):
        """Clear Workspace Cache

Clears information about a workspace that has been cached in memory.

        params: {"in_data": <Data Element; Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")

            # Generate output name and path
            output_name = f"{params.replace(' ', '_')}_Clear_Workspace_Cache"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Clear Workspace Cache
            arcpy.ClearWorkspaceCache(in_data)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_schema_report(self, params):
        """Convert Schema Report

Converts a JSON or XLSX formatted schema report to another schema report format or to an XML workspace document that can be used to create a geodatabase.

        params: {"schema_report": <File>, "out_location": <Folder>, "name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        schema_report = params.get("schema_report")
        if schema_report is None:
            return {"success": False, "error": "schema_report parameter is required"}
        out_location = params.get("out_location")
        if out_location is None:
            return {"success": False, "error": "out_location parameter is required"}
        name = params.get("name")
        if name is None:
            return {"success": False, "error": "name parameter is required"}
        formats = params.get("formats")
        if formats is None:
            return {"success": False, "error": "formats parameter is required"}

            # Generate output name and path
            output_name = f"{schema_report.replace(' ', '_')}_Convert_Schema_Report"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Schema Report
            arcpy.ConvertSchemaReport(schema_report, out_location, name, formats)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_cloud_storage_connection_file(self, params):
        """Create Cloud Storage Connection File

Creates a connection file for ArcGIS-supported cloud storage. This tool allows existing raster geoprocessing tools to write cloud raster format (CRF) datasets into the cloud storage bucket or read raster datasets (not limited to CRF) stored in the cloud storage as input. The tool also creates a cloud storage connection file that you can use to access Apache Parquet files for mapping.

        params: {"out_folder_path": <Folder>, "out_name": <String>, "service_provider": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        service_provider = params.get("service_provider")
        if service_provider is None:
            return {"success": False, "error": "service_provider parameter is required"}
        bucket_name = params.get("bucket_name")
        if bucket_name is None:
            return {"success": False, "error": "bucket_name parameter is required"}
        access_key_id = params.get("access_key_id")
        secret_access_key = params.get("secret_access_key")
        region = params.get("region")
        end_point = params.get("end_point")
        folder = params.get("folder")
        authentication = params.get("authentication")

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_Cloud_Storage_Connection_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Cloud Storage Connection File
            arcpy.CreateCloudStorageConnectionFile(out_folder_path, out_name, service_provider, bucket_name, access_key_id, secret_access_key, region, end_point, folder, authentication)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_database_connection(self, params):
        """Create Database Connection

Creates a file that ArcGIS uses to connect to a database, a cloud data warehouse, or an enterprise geodatabase.

        params: {"out_folder_path": <Folder>, "out_name": <String>, "database_platform": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        database_platform = params.get("database_platform")
        if database_platform is None:
            return {"success": False, "error": "database_platform parameter is required"}
        instance = params.get("instance")
        account_authentication = params.get("account_authentication")
        username = params.get("username")
        password = params.get("password")
        save_user_pass = params.get("save_user_pass")
        database = params.get("database")
        schema = params.get("schema")
        version_type = params.get("version_type")
        version = params.get("version")
        date = params.get("date")
        auth_type = params.get("auth_type")
        project_id = params.get("project_id")
        default_dataset = params.get("default_dataset")
        refresh_token = params.get("refresh_token")
        key_file = params.get("key_file")
        role = params.get("role")
        warehouse = params.get("warehouse")
        advanced_options = params.get("advanced_options")
        host_url = params.get("host_url")

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_Database_Connection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Database Connection
            arcpy.CreateDatabaseConnection(out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass, database, schema, version_type, version, date, auth_type, project_id, default_dataset, refresh_token, key_file, role, warehouse, advanced_options, host_url)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_database_connection_string(self, params):
        """Create Database Connection String

Creates a connection string that geoprocessing tools can use to connect to a database or an enterprise geodatabase.

        params: {"database_platform": <String>, "instance": <String>, "account_authentication": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        database_platform = params.get("database_platform")
        if database_platform is None:
            return {"success": False, "error": "database_platform parameter is required"}
        instance = params.get("instance")
        if instance is None:
            return {"success": False, "error": "instance parameter is required"}
        account_authentication = params.get("account_authentication")
        username = params.get("username")
        password = params.get("password")
        database = params.get("database")
        object_name = params.get("object_name")
        data_type = params.get("data_type")
        feature_dataset = params.get("feature_dataset")
        schema = params.get("schema")
        version_type = params.get("version_type")
        version = params.get("version")
        date = params.get("date")

            # Generate output name and path
            output_name = f"{database_platform.replace(' ', '_')}_Create_Database_Connection_String"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Database Connection String
            arcpy.CreateDatabaseConnectionString(database_platform, instance, account_authentication, username, password, database, object_name, data_type, feature_dataset, schema, version_type, version, date)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_feature_dataset(self, params):
        """Create Feature Dataset

Creates a feature dataset in the output location: an existing enterprise,  file, or mobile geodatabase.

        params: {"out_dataset_path": <Workspace>, "out_name": <String>, "spatial_reference": <Spatial Reference>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_dataset_path = params.get("out_dataset_path")
        if out_dataset_path is None:
            return {"success": False, "error": "out_dataset_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        spatial_reference = params.get("spatial_reference")

            # Generate output name and path
            output_name = f"{out_dataset_path.replace(' ', '_')}_Create_Feature_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Feature Dataset
            arcpy.CreateFeatureDataset(out_dataset_path, out_name, spatial_reference)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_file_geodatabase(self, params):
        """Create File Geodatabase

Creates a file geodatabase in a folder.

        params: {"out_folder_path": <Folder>, "out_name": <String>, "out_version": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        out_version = params.get("out_version")

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_File_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create File Geodatabase
            arcpy.CreateFileGeodatabase(out_folder_path, out_name, out_version)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_folder(self, params):
        """Create Folder

Creates a folder in the specified location.

        params: {"out_folder_path": <Folder>, "out_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_Folder"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Folder
            arcpy.CreateFolder(out_folder_path, out_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_mobile_geodatabase(self, params):
        """Create Mobile Geodatabase

Creates a mobile geodatabase. Learn more about creating and using mobile geodatabases

        params: {"out_folder_path": <Folder>, "out_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_folder_path = params.get("out_folder_path")
        if out_folder_path is None:
            return {"success": False, "error": "out_folder_path parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}

            # Generate output name and path
            output_name = f"{out_folder_path.replace(' ', '_')}_Create_Mobile_Geodatabase"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Mobile Geodatabase
            arcpy.CreateMobileGeodatabase(out_folder_path, out_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_spatial_type(self, params):
        """Create Spatial Type

Adds the ST_Geometry SQL type, subtypes, and functions to an Oracle or a PostgreSQL database. This allows you to use the ST_Geometry SQL type to store geometries in a database that does not contain a geodatabase. You can also use this tool to upgrade the existing ST_Geometry type, subtypes, and functions in an Oracle or a PostgreSQL database.

        params: {"input_database": <Workspace>, "sde_user_password": <Encrypted String>, "tablespace_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}
        sde_user_password = params.get("sde_user_password")
        if sde_user_password is None:
            return {"success": False, "error": "sde_user_password parameter is required"}
        tablespace_name = params.get("tablespace_name")
        st_shape_library_path = params.get("st_shape_library_path")

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Create_Spatial_Type"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Spatial Type
            arcpy.CreateSpatialType(input_database, sde_user_password, tablespace_name, st_shape_library_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_sqlite_database(self, params):
        """Create SQLite Database

Creates a GeoPackage or an SQLite database that contains the ST_Geometry or SpatiaLite spatial type.

        params: {"out_database_name": <File>, "spatial_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_database_name = params.get("out_database_name")
        if out_database_name is None:
            return {"success": False, "error": "out_database_name parameter is required"}
        spatial_type = params.get("spatial_type")

            # Generate output name and path
            output_name = f"{out_database_name.replace(' ', '_')}_Create_SQLite_Database"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create SQLite Database
            arcpy.CreateSQLiteDatabase(out_database_name, spatial_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enable_editing_templates(self, params):
        """Enable Editing Templates

Enables a file or mobile geodatabase to store editing templates.

        params: {"in_workspace": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_workspace = params.get("in_workspace")
        if in_workspace is None:
            return {"success": False, "error": "in_workspace parameter is required"}

            # Generate output name and path
            output_name = f"{in_workspace.replace(' ', '_')}_Enable_Editing_Templates"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enable Editing Templates
            arcpy.EnableEditingTemplates(in_workspace)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_xml_workspace_document(self, params):
        """Export XML Workspace Document

Creates a readable XML document of the geodatabase contents. The XML workspace document is useful for sharing geodatabase schemas or copying geodatabase schemas from one type to another.

        params: {"in_data": <Feature Class; Feature Dataset; Raster Dataset; Table; Workspace>, "out_file": <File>, "export_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        out_file = params.get("out_file")
        if out_file is None:
            return {"success": False, "error": "out_file parameter is required"}
        export_type = params.get("export_type")
        storage_type = params.get("storage_type")
        export_metadata = params.get("export_metadata")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Export_XML_Workspace_Document"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export XML Workspace Document
            arcpy.ExportXMLWorkspaceDocument(in_data, out_file, export_type, storage_type, export_metadata)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_schema_report(self, params):
        """Generate Schema Report

Generates an Excel, JSON, PDF, or HTML representation of the geodatabase schema. These formats are output to a target destination folder. Learn more about generating a schema report

        params: {"in_dataset": <Workspace; Feature Dataset; Feature Layer; Table View>, "out_location": <Folder>, "name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_location = params.get("out_location")
        if out_location is None:
            return {"success": False, "error": "out_location parameter is required"}
        name = params.get("name")
        if name is None:
            return {"success": False, "error": "name parameter is required"}
        formats = params.get("formats")
        if formats is None:
            return {"success": False, "error": "formats parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Generate_Schema_Report"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Schema Report
            arcpy.GenerateSchemaReport(in_dataset, out_location, name, formats)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_xml_workspace_document(self, params):
        """Import XML Workspace Document

Imports the contents of an XML workspace document into an existing geodatabase.

        params: {"target_geodatabase": <Workspace>, "in_file": <File>, "import_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        target_geodatabase = params.get("target_geodatabase")
        if target_geodatabase is None:
            return {"success": False, "error": "target_geodatabase parameter is required"}
        in_file = params.get("in_file")
        if in_file is None:
            return {"success": False, "error": "in_file parameter is required"}
        import_type = params.get("import_type")
        config_keyword = params.get("config_keyword")

            # Generate output name and path
            output_name = f"{target_geodatabase.replace(' ', '_')}_Import_XML_Workspace_Document"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import XML Workspace Document
            arcpy.ImportXMLWorkspaceDocument(target_geodatabase, in_file, import_type, config_keyword)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def refresh_excel(self, params):
        """Refresh Excel

Refreshes a Microsoft Excel file  in ArcGIS Pro.

        params: {"in_excel_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_excel_file = params.get("in_excel_file")
        if in_excel_file is None:
            return {"success": False, "error": "in_excel_file parameter is required"}

            # Generate output name and path
            output_name = f"{in_excel_file.replace(' ', '_')}_Refresh_Excel"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Refresh Excel
            arcpy.RefreshExcel(in_excel_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_geodatabase_connection_properties_to_branch(self, params):
        """Update Geodatabase Connection Properties To Branch

Updates an enterprise geodatabase connection to work with branch versioning. Learn more about branch versioning

        params: {"input_database": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_database = params.get("input_database")
        if input_database is None:
            return {"success": False, "error": "input_database parameter is required"}

            # Generate output name and path
            output_name = f"{input_database.replace(' ', '_')}_Update_Geodatabase_Connection_Properties_To_Branch"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Geodatabase Connection Properties To Branch
            arcpy.UpdateGeodatabaseConnectionPropertiesToBranch(input_database)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
