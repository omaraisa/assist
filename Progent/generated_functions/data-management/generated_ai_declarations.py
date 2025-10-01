# Generated ArcGIS Pro data-management AI Function Declarations
# Generated on 2025-10-01T14:27:18.446262
# Total tools: 400

functions_declarations = {
    "add_3d_formats_to_multipatch": {
        "name": "add_3d_formats_to_multipatch",
        "description": "Converts a multipatch to a 3D object feature layer by linking the feature class with one or more 3D model formats.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input geodatabase multipatch feature that will be converted to a 3D object feature layer."
                },
                "multipatch_materials": {
                        "type": "string",
                        "description": "Note:This parameter is no longer supported. The option to\r\ncontrol whether multipatch materials were used was removed to\r\nimprove this tool's usability. Materials will always be used when\r\nthey are av...",
                        "default": None
                },
                "formats": {
                        "type": "string",
                        "description": "Specifies the 3D formats that will be associated with the multipatch features. Each input feature will be duplicated for each selected format. The available options depend on the codecs installed on t...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "export_3d_objects": {
        "name": "export_3d_objects",
        "description": "Exports 3D object features to one or more 3D model file formats.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The 3D object feature layer that will be exported."
                },
                "target_folder": {
                        "type": "string",
                        "description": "The existing directory that will contain the output 3D models."
                },
                "formats": {
                        "type": "string",
                        "description": "Specifies the 3D formats that will be exported.\r\n FMT3D_DAE\u2014The COLLADA format will be exported.FMT3D_DWG\u2014The DWG format will be exported.FMT3D_FBX\u2014The Autodesk FilmBox format will be exported.FMT3D_G..."
                },
                "name_field": {
                        "type": "string",
                        "description": "The text field in the input feature's attribute table that contains the name to be used for each output folder. If no name field is provided, the output folder will be named after the object ID of the...",
                        "default": None
                },
                "overwrite": {
                        "type": "string",
                        "description": "Specifies whether existing 3D models in the output directory will be overwritten.OVERWRITE\u2014Existing 3D models in the output directory will be overwritten.NO_OVERWRITE\u2014Existing 3D models in the output ..."
                }
        },
        "required": [
                "in_features",
                "target_folder",
                "formats",
                "overwrite"
        ]
},
    "import_3d_objects": {
        "name": "import_3d_objects",
        "description": "Imports 3D models from one or more 3D file formats and creates or updates a 3D object feature layer.",
        "parameters": {
                "files_and_folders": {
                        "type": "string",
                        "description": "The 3D files or folders containing 3D files that will be imported.\r\nWhen a folder is provided, all supported 3D models contained in it and its subdirectories will be imported. The following models are..."
                },
                "updated_features": {
                        "type": "string",
                        "description": "The 3D object feature layer that will be created or updated."
                },
                "update": {
                        "type": "string",
                        "description": "Specifies how an existing 3D object feature class will be updated.REPLACE_ALL\u2014All existing features in the 3D object feature class will be removed and only the 3D models that are specified as input wi...",
                        "default": None
                },
                "translate": {
                        "type": "string",
                        "description": "The x- and y-coordinate offset that will be applied to the imported models.",
                        "default": None
                },
                "elevation": {
                        "type": "string",
                        "description": "The height offset that will be applied to the imported models.",
                        "default": None
                },
                "scale": {
                        "type": "string",
                        "description": "The scale factor that will be used to resize the 3D models being imported.",
                        "default": None
                },
                "rotate": {
                        "type": "string",
                        "description": "The degree rotation angle \r\nthat will be applied to the imported models. Rotation is applied with the assumption of  zero degrees (0\u00b0) representing north and angular values incrementing in the clockwi...",
                        "default": None
                },
                "y_is_up": {
                        "type": "string",
                        "description": "Specifies whether y coordinates will be interpreted as height or along the horizontal plane. This parameter is only supported for Wavefront Object files (.obj).Y_IS_UP\u2014Y coordinates will be interprete..."
                }
        },
        "required": [
                "files_and_folders",
                "updated_features",
                "y_is_up"
        ]
},
    "remove_3d_formats_from_multipatch": {
        "name": "remove_3d_formats_from_multipatch",
        "description": "Removes the 3D formats  referenced by a 3D object feature layer.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The multipatch feature class that was converted to a 3D object feature class."
                },
                "multipatch_materials": {
                        "type": "string",
                        "description": "Note:This parameter is no longer supported. The option to\r\ncontrol whether multipatch materials were used was removed to\r\nimprove this tool's usability. Materials will always be used when\r\nthey are av...",
                        "default": None
                },
                "formats": {
                        "type": "string",
                        "description": "Specifies the 3D model formats referenced by the 3D object feature layer that will be removed. Only the formats that have been linked to the input features can be specified.FMT3D_DAE\u2014The COLLADA forma...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "disable_archiving": {
        "name": "disable_archiving",
        "description": "Disables archiving on a geodatabase feature class, table, or feature dataset. Learn more about the process of disabling archiving",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The geodatabase feature class, table, or feature dataset for which archiving will be disabled."
                },
                "preserve_history": {
                        "type": "string",
                        "description": "Specifies whether records that are not from the current moment will be preserved.If the table or feature class is versioned, the history table or feature will become enabled.For nonversioned data, a t...",
                        "default": None
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "enable_archiving": {
        "name": "enable_archiving",
        "description": "Enables archiving on a table, feature class, or feature dataset. Learn more about the process of enabling  archiving",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The name of the dataset on which archiving will be enabled."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "trim_archive_history": {
        "name": "trim_archive_history",
        "description": "Deletes retired archive records from nonversioned archive-enabled datasets. Over time, the archive history of a table can increase exponentially as the edit history is maintained. This can affect storage and backup management decisions and may affect performance if the data becomes too large for the system in place. Some organizations may use nonversioned archiving because it is required for certain functionality and have no need for historical records, or they may want to remove older data that is no longer relevant. This tool allows you to delete all retired rows or the retired rows older than a specified date. Learn more about trimming the archive history",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The nonversioned archive-enabled table with the archive history to be  trimmed."
                },
                "trim_mode": {
                        "type": "string",
                        "description": "Specifies the trim mode that will be used to trim the archive history.Note:At the current version of ArcGIS Pro, only the delete trim mode is available.DELETE\u2014The archive records will be deleted."
                },
                "trim_before_date": {
                        "type": "string",
                        "description": "Archive records older than this date and time will be deleted. The date and time must be in UTC. If no date is provided, all archive records will be deleted.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "trim_mode"
        ]
},
    "add_attachments": {
        "name": "add_attachments",
        "description": "Adds file attachments to the records of a geodatabase feature class or table. The attachments are stored in the geodatabase in a separate attachment table that maintains linkage to the target dataset. Attachments are added to the target dataset using a match table that indicates for each input record (or an attribute group of records) the path to a file to add as an attachment to that record. Learn more about working with the  tools in the Attachments toolset",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The geodatabase table or feature class where attachments will be added. Attachments are not added directly to this table, but to a related attachment table that maintains linkage to the input dataset...."
                },
                "in_join_field": {
                        "type": "string",
                        "description": "A field from the in_dataset parameter value that has matching values in the in_match_join_field parameter value. Records with matching values will have attachments added. This field can be an Object I..."
                },
                "in_match_table": {
                        "type": "string",
                        "description": "A table that identifies which input records will have attachments added and the paths to those attachments."
                },
                "in_match_join_field": {
                        "type": "string",
                        "description": "A field from the in_match_table parameter value that indicates which records in the in_dataset parameter value will have specified attachments added."
                },
                "in_match_path_field": {
                        "type": "string",
                        "description": "A field from the Match Table parameter value that contains paths to the attachments to add to the records of the Input Dataset parameter value.\r\n A field from the in_match_table parameter value that c..."
                },
                "in_working_folder": {
                        "type": "string",
                        "description": "A folder or workspace where attachment files are centralized. By specifying a working folder, the paths in the in_match_path_field parameter value can be the short names of files relative to the worki...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "in_join_field",
                "in_match_table",
                "in_match_join_field",
                "in_match_path_field"
        ]
},
    "disable_attachments": {
        "name": "disable_attachments",
        "description": "Disables attachments on a geodatabase feature class or table. The tool deletes the attachment relationship class and attachment table.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The geodatabase table or feature class for which attachments will be disabled. The input must be in a version 10 or later geodatabase."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "downgrade_attachments": {
        "name": "downgrade_attachments",
        "description": "Downgrades the attachments functionality of a feature class or table.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The feature class or table that will have its attachments functionality downgraded."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "enable_attachments": {
        "name": "enable_attachments",
        "description": "Enables attachments on a geodatabase feature class or table. The tool creates the necessary attachment relationship class and attachment table that will store attachment files internally. Learn more about working with the Attachments geoprocessing tools",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The geodatabase table or feature class for which attachments will be enabled. The input must be in a version 10 or later geodatabase."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "export_attachments": {
        "name": "export_attachments",
        "description": "Exports file attachments from the records of a geodatabase feature class or table to a specified folder. Attachments can also be exported to  subdirectories  based on an attribute value from a specified attribute column. Exported attachments can be renamed using one or more field attribute values. Learn more about working with the Attachments geoprocessing tools",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The geodatabase table or feature class from which attachments will be exported.The input must be stored in a version 10.0 or later geodatabase, and the table must have attachments enabled."
                },
                "out_location": {
                        "type": "string",
                        "description": "The folder where the attachment files will be exported."
                },
                "subdirectory_field": {
                        "type": "string",
                        "description": "A field from the in_dataset   \r\nparameter value that    will be used to create subdirectory names.",
                        "default": None
                },
                "name_format": {
                        "type": "string",
                        "description": "Specifies the format that will be used for naming exported attachments.ORIGINAL\u2014The output file names will use the original file names stored in the geodatabase.REPLACE\u2014The output file names will use ...",
                        "default": None
                },
                "name_fields": {
                        "type": "string",
                        "description": "The fields from the in_dataset parameter value that will be used to rename the exported attachments. If multiple fields are specified, the output files will use the field values concatenated with an u...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_location"
        ]
},
    "generate_attachment_match_table": {
        "name": "generate_attachment_match_table",
        "description": "Creates a match table to be used with the Add Attachments and Remove Attachments tools. Learn more about working with the Attachments geoprocessing tools",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "A dataset containing records that will have files attached."
                },
                "in_folder": {
                        "type": "string",
                        "description": "A folder containing files to attach."
                },
                "out_match_table": {
                        "type": "string",
                        "description": "The output match table with the MATCHID and FILENAME fields."
                },
                "in_key_field": {
                        "type": "string",
                        "description": "The field from which values will be used to  match the names of the files from  the input folder. The matching behavior will compare field values with each  file name, disregarding the file extension...."
                },
                "in_file_filter": {
                        "type": "string",
                        "description": "A data filter that will be used to limit the files considered for matching. Wild cards (*) can be used for more flexible filtering options. Multiple filters delimited by semicolons are also supported....",
                        "default": None
                },
                "in_use_relative_paths": {
                        "type": "string",
                        "description": "Specifies whether the output match table field FILENAME will contain full paths or only the file names.\r\nRELATIVE\u2014The field will contain only the file names (relative paths). This is the default.ABSOL...",
                        "default": None
                },
                "match_pattern": {
                        "type": "string",
                        "description": "Specifies the type of match pattern that will be used to match file names with the specified key_field parameter value.\r\nEXACT\u2014File names that are an exact match to the values in the key field will be...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "in_folder",
                "out_match_table",
                "in_key_field"
        ]
},
    "remove_attachments": {
        "name": "remove_attachments",
        "description": "Removes attachments from geodatabase feature class or table records. Since attachments are not actually stored in the input dataset, no changes will be made to that feature class or table. Changes will be made to the related geodatabase table that stores the attachments and maintains linkage with the input dataset. A match table is used to identify the input records (or attribute groups of records) that will have attachments removed. Learn more about working with the tools in the Attachments toolset",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "A geodatabase table or feature class from which attachments will be removed. Attachments are not removed directly from this table; they are removed from the related attachment table that stores the at..."
                },
                "in_join_field": {
                        "type": "string",
                        "description": "A field from the in_dataset parameter value that contains values that match the values in the in_match_join_field parameter value. Records that have join field values that match the in_dataset paramet..."
                },
                "in_match_table": {
                        "type": "string",
                        "description": "A table that identifies which input records will have attachments removed."
                },
                "in_match_join_field": {
                        "type": "string",
                        "description": "A field from the match table that indicates which records in the in_dataset parameter value will have specified attachments removed. This field can have values that match the in_dataset Object ID fiel..."
                },
                "in_match_name_field": {
                        "type": "string",
                        "description": "A field from the match table that contains the names of the attachments that will be removed from the in_dataset parameter value's records. If no name field is specified, all attachments will be remov...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "in_join_field",
                "in_match_table",
                "in_match_join_field"
        ]
},
    "upgrade_attachments": {
        "name": "upgrade_attachments",
        "description": "Upgrades the attachments functionality on the data. When attachments are enabled on a feature class, an attachment table and relationship class are created to store the attachment data when an attachment is added to a feature. The attachment\r\ntable that is created includes fields that are used to store information about the attachment.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The feature class with attachments enabled."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "add_attribute_rule": {
        "name": "add_attribute_rule",
        "description": "Adds an attribute rule to a dataset. Attribute rules are user-defined rules that can be added to a dataset to enhance the editing experience and help enforce data integrity. These rules can be used to populate attribute values or constrain permissible feature configurations and are enforced during feature editing. If a rule is violated when editing a feature, an error message will be returned. Learn more about attribute rules Learn about the ArcGIS Arcade scripting language",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or feature class that will have the new rule applied."
                },
                "name": {
                        "type": "string",
                        "description": "A  unique name for the new rule."
                },
                "type": {
                        "type": "string",
                        "description": "Specifies the type of attribute rule that will be added.\r\nCALCULATION\u2014Attribute values will be automatically populated for features when another attribute is set on a feature. These rules are applied ..."
                },
                "script_expression": {
                        "type": "string",
                        "description": "The Arcade expression that defines the rule."
                },
                "is_editable": {
                        "type": "string",
                        "description": "Specifies whether the attribute value can be edited. Attribute rules can be configured to either block or allow editors to edit the attribute values of the field being calculated.\r\nThis parameter is o...",
                        "default": None
                },
                "triggering_events": {
                        "type": "string",
                        "description": "Specifies the editing events that will trigger the attribute rule to take effect. This parameter is valid for calculation and constraint rule types only. At least one triggering event must be provided...",
                        "default": None
                },
                "error_number": {
                        "type": "string",
                        "description": "An error number that will be returned when this rule is violated. This value is not required to be unique, so the same custom error number may be returned for multiple rules. This parameter is require...",
                        "default": None
                },
                "error_message": {
                        "type": "string",
                        "description": "An error message that will be returned when this rule is violated. It is recommended that you use a descriptive message to help the editor understand the violation when it occurs. The message is limit...",
                        "default": None
                },
                "description": {
                        "type": "string",
                        "description": "The description of the new attribute rule. The description is limited to 256 characters.",
                        "default": None
                },
                "subtype": {
                        "type": "string",
                        "description": "The subtype or subtypes to which the rule will be applied.",
                        "default": None
                },
                "field": {
                        "type": "string",
                        "description": "The name of an existing field to which the rule will be applied. This parameter is only applicable for the calculation attribute rule type.",
                        "default": None
                },
                "exclude_from_client_evaluation": {
                        "type": "string",
                        "description": "Specifies whether the application will evaluate the rule locally before applying the edits to the workspace. Not all clients have the capability to run all of the available rules, so authors can exclu...",
                        "default": None
                },
                "batch": {
                        "type": "string",
                        "description": "Specifies whether the rule evaluation will be run in batch mode.BATCH\u2014The rule evaluation will be run in batch mode at a later time by running validate.NOT_BATCH\u2014The rule evaluation will not be run in...",
                        "default": None
                },
                "severity": {
                        "type": "string",
                        "description": "The severity of the error. A value within the range of 1 through 5 can be provided to define the severity of the rule. A value of 1 is high, being the most severe, and a value of 5 is low, being the l...",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "A set of tags that identify the rule (for searching and indexing) as a way to map to a functional requirement in a data model.\r\nTo enter multiple tags, use a semicolon delimiter, for example, Tag1;Tag...",
                        "default": None
                },
                "triggering_fields": {
                        "type": "string",
                        "description": "The fields that will trigger an attribute rule to run when an editing event occurs during an update trigger for calculation and constraint attribute rules. If no fields are specified, all fields will ...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "name",
                "type",
                "script_expression"
        ]
},
    "alter_attribute_rule": {
        "name": "alter_attribute_rule",
        "description": "Alters the properties of an attribute rule.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the attribute rule that will be altered."
                },
                "name": {
                        "type": "string",
                        "description": "The name of the attribute rule that will be altered."
                },
                "description": {
                        "type": "string",
                        "description": "The description of the attribute rule.To keep the existing value of the description, leave this parameter empty. To clear the existing value of the description, use the RESET keyword. RESET\u2014The existi...",
                        "default": None
                },
                "error_number": {
                        "type": "string",
                        "description": "The error number of the attribute rule.To keep the existing error number value, leave this parameter empty. To clear the existing error number value  for a calculation rule, use the RESET keyword. Err...",
                        "default": None
                },
                "error_message": {
                        "type": "string",
                        "description": "The error message of the attribute rule.To keep the existing error message value, leave this parameter empty. To clear the existing error message value  for a calculation rule, use the RESET keyword. ...",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tags for the attribute rule.The new values will replace all existing tags; to keep any current tags, include them in this list. For multiple tags, use a semicolon delimiter, for example, Tag1;Tag2...",
                        "default": None
                },
                "triggering_events": {
                        "type": "string",
                        "description": "Specifies the editing events that will trigger the attribute rule to take effect. Triggering events are only applicable for constraint rules and immediate calculation rules.The new values will replace...",
                        "default": None
                },
                "script_expression": {
                        "type": "string",
                        "description": "An ArcGIS Arcade expression that defines the rule. \r\nTo keep the existing expression, leave this parameter empty. If an expression is provided for this parameter, it will replace the existing Arcade e...",
                        "default": None
                },
                "exclude_from_client_evaluation": {
                        "type": "string",
                        "description": "Specifies whether the application will evaluate the rule locally before applying the edits to the workspace.  The default for this parameter corresponds to the existing value set for the rule. That is...",
                        "default": None
                },
                "triggering_fields": {
                        "type": "string",
                        "description": "A list of fields that will trigger an attribute rule to run when an editing event occurs during an update trigger for calculation and constraint attribute rules. If no fields are specified, all fields...",
                        "default": None
                },
                "subtype": {
                        "type": "string",
                        "description": "The subtype or subtypes to which the rule will be applied.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "name"
        ]
},
    "delete_attribute_rule": {
        "name": "delete_attribute_rule",
        "description": "Deletes one or more attribute rules from a dataset. Learn more about attribute rules",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or feature class containing the attribute rules that will be deleted."
                },
                "names": {
                        "type": "string",
                        "description": "The names of the rules that will be deleted from the dataset."
                },
                "type": {
                        "type": "string",
                        "description": "Specifies the type of attribute rules that will be deleted.CALCULATION\u2014Calculation rules will be deleted.CONSTRAINT\u2014Constraint rules will be deleted.VALIDATION\u2014Validation rules will be deleted.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "names"
        ]
},
    "disable_attribute_rules": {
        "name": "disable_attribute_rules",
        "description": "Disables one or more attribute rules for a dataset.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or feature class that contains the attribute rule to be disabled."
                },
                "names": {
                        "type": "string",
                        "description": "The names of the rules to disable for the dataset."
                },
                "type": {
                        "type": "string",
                        "description": "Specifies the type of attribute rules to disable. The tool will verify that the type of rule specified in this parameter matches the rule type specified. If they do not match, the rule will not be dis...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "names"
        ]
},
    "enable_attribute_rules": {
        "name": "enable_attribute_rules",
        "description": "Enables one or more attribute rules in a dataset",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or feature class that contains the attribute rule to be enabled."
                },
                "names": {
                        "type": "string",
                        "description": "The names of the rules to enable for the dataset."
                },
                "type": {
                        "type": "string",
                        "description": "Specifies the type of attribute rules to enable. The tool will verify that the type of rule specified  in this parameter matches the rule type specified. If they do not match, the rule will not be ena...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "names"
        ]
},
    "evaluate_rules": {
        "name": "evaluate_rules",
        "description": "Evaluates geodatabase rules and functionality. Learn more about evaluating attribute rules",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "A file geodatabase, mobile geodatabase, or feature service URL. An example of a feature service URL is https://myserver/server/rest/services/myservicename/FeatureServer."
                },
                "evaluation_types": {
                        "type": "string",
                        "description": "Specifies the types of evaluation that will be used.CALCULATION_RULES\u2014Batch calculation attribute rules will be evaluated.VALIDATION_RULES\u2014Validation attribute rules will be evaluated."
                },
                "extent": {
                        "type": "string",
                        "description": "The extent to be evaluated. If there is a selection in the map, only selected features within the specified extent will be evaluated.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minim...",
                        "default": None
                },
                "run_async": {
                        "type": "string",
                        "description": "Specifies whether the evaluation will run synchronously or asynchronously. \r\nThis parameter is only supported when the input workspace is a feature service.ASYNC\u2014The evaluation will run asynchronously...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "evaluation_types"
        ]
},
    "export_attribute_rules": {
        "name": "export_attribute_rules",
        "description": "Exports attribute rules from a dataset to a comma-separated values file (.csv).",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or feature class from which the attribute rules will be exported."
                },
                "out_csv_file": {
                        "type": "string",
                        "description": "The folder location and name of the .csv file that will be created."
                }
        },
        "required": [
                "in_table",
                "out_csv_file"
        ]
},
    "import_attribute_rules": {
        "name": "import_attribute_rules",
        "description": "Imports attribute rules from  comma-separated value files (.csv) to a dataset.",
        "parameters": {
                "target_table": {
                        "type": "string",
                        "description": "The table or feature class to which the attribute rules will be applied. The dataset must have all the features specified in the rule definition."
                },
                "csv_file": {
                        "type": "string",
                        "description": "The .csv files containing the rules to import."
                }
        },
        "required": [
                "target_table",
                "csv_file"
        ]
},
    "reorder_attribute_rule": {
        "name": "reorder_attribute_rule",
        "description": "Reorders the evaluation order of an attribute rule. The evaluation order controls the sequence in which rules are evaluated. The evaluation order is important when there are dependencies on calculated fields, since the result may be impacted if the rules are in a different order. Learn more about attribute rule evaluation order",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table that contains the attribute rule with the evaluation order that will be updated."
                },
                "name": {
                        "type": "string",
                        "description": "The name of the calculation rule that will have its evaluation order updated."
                },
                "evaluation_order": {
                        "type": "string",
                        "description": "The new evaluation order for the rule. For example, if there are five rules and a particular rule is in position 5 (the fifth order position, to be evaluated last) but you want it to be evaluated in p..."
                }
        },
        "required": [
                "in_table",
                "name",
                "evaluation_order"
        ]
},
    "add_items_to_catalog_dataset": {
        "name": "add_items_to_catalog_dataset",
        "description": "Adds workspace items and layers\u2014such as geodatabase datasets, raster layers, feature layers, mosaic layers, and other items\u2014to an existing catalog dataset.",
        "parameters": {
                "target_catalog_dataset": {
                        "type": "string",
                        "description": "The catalog dataset to which the items will be added."
                },
                "input_items": {
                        "type": "string",
                        "description": "The workspace items, layers, and files  from which items will be added to the catalog dataset. The workspace can be a folder, file geodatabase, feature dataset, enterprise database, or a service from ..."
                },
                "input_item_types": {
                        "type": "string",
                        "description": "Specifies the item types that will be added to the catalog dataset from any  input workspaces. All supported item types will be  added by default.BIM_FILE_WORKSPACE\u2014BIM file workspaces will be added.B...",
                        "default": None
                },
                "include_subfolders": {
                        "type": "string",
                        "description": "Specifies whether the contents of folders or workspaces specified in the input_items parameter value will be recursively searched and added to the catalog dataset. This parameter is not applicable to ...",
                        "default": None
                },
                "footprint_type": {
                        "type": "string",
                        "description": "Specifies whether the reference item's footprint will be the full extent or a convex hull representing the smallest convex polygon for all features.ENVELOPE\u2014The footprint will be a rectangle covering ...",
                        "default": None
                }
        },
        "required": [
                "target_catalog_dataset",
                "input_items"
        ]
},
    "add_portal_items_to_catalog_dataset": {
        "name": "add_portal_items_to_catalog_dataset",
        "description": "Adds ArcGIS Online or ArcGIS Enterprise portal service items\u2014such as feature, map, image, scene, and tile services\u2014to an existing catalog dataset.",
        "parameters": {
                "target_catalog_dataset": {
                        "type": "string",
                        "description": "The catalog dataset to which portal items will be added."
                },
                "input_portal_itemtypes": {
                        "type": "string",
                        "description": "Specifies the item types that will be added to the catalog dataset from the portal. All supported item types will be added by default.FEATURE_SERVICE\u2014Feature layers will be added. This option does not...",
                        "default": None
                },
                "content": {
                        "type": "string",
                        "description": "Specifies the collection in the active portal from which items will be added to the catalog dataset.MY_CONTENT\u2014 Items from your My Content collection will be added. This is the default.MY_GROUPS\u2014Items...",
                        "default": None
                },
                "portal_folders": {
                        "type": "string",
                        "description": "The portal folders from which items will be added to the catalog dataset.",
                        "default": None
                },
                "portal_groups": {
                        "type": "string",
                        "description": "The portal groups from which items will be added to the catalog dataset.",
                        "default": None
                },
                "access_level": {
                        "type": "string",
                        "description": "Specifies the sharing level that portal items must have to be added to the catalog dataset.PUBLIC\u2014 Items that are shared with the public will be added to the catalog dataset. This is the default.ORG\u2014I...",
                        "default": None
                }
        },
        "required": [
                "target_catalog_dataset"
        ]
},
    "create_catalog_dataset": {
        "name": "create_catalog_dataset",
        "description": "Creates a catalog dataset to which collections of layers, rasters, datasets, and other items can be added.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The enterprise, mobile, or file geodatabase in which the output catalog dataset will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the catalog dataset that will be created."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the catalog dataset.",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "The feature class or table that will be used as a template to define the attribute fields of the new catalog dataset.",
                        "default": None
                },
                "has_z": {
                        "type": "string",
                        "description": "Specifies whether the catalog dataset will contain elevation values (z-values).DISABLED\u2014The output catalog dataset will not contain z-values. This is the default.ENABLED\u2014The output catalog dataset wil...",
                        "default": None
                },
                "out_alias": {
                        "type": "string",
                        "description": "The alias name of the catalog dataset.",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The configuration keyword determines the storage parameters of the database table.\r\nThe configuration keyword applies to enterprise data only.",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "detect_feature_changes": {
        "name": "detect_feature_changes",
        "description": "Finds where the update line features spatially match the base line features and detects spatial changes, attribute changes, or both, as well as no change. It then creates an output feature class containing matched update features with information about their changes, unmatched update features, and unmatched base features. Learn more about how feature matching works",
        "parameters": {
                "update_features": {
                        "type": "string",
                        "description": "The line features that will be compared to the base features."
                },
                "base_features": {
                        "type": "string",
                        "description": "The line features that will be compared to the update features for change detection."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output line feature class \r\ncontaining the change information. The output contains all\r\nparticipating update features (matched and unmatched) and any unmatched\r\nbase features."
                },
                "search_distance": {
                        "type": "string",
                        "description": "The distance that will be used to search for match candidates. \r\nA distance must be specified and it must be greater than zero.\r\nYou can choose a preferred unit. The default is the feature unit."
                },
                "match_fieldssource_field_target_field": {
                        "type": "string",
                        "description": "The match fields from the update and base features. If specified, each pair of fields are compared for match candidates to help determine the right match.",
                        "default": None
                },
                "out_match_table": {
                        "type": "string",
                        "description": "The output table containing complete feature matching information.",
                        "default": None
                },
                "change_tolerance": {
                        "type": "string",
                        "description": "The distance used to determine if there is a spatial change.   All matched update features and base features are compared to this tolerance. If any portions of the update  or the base features fall ou...",
                        "default": None
                },
                "compare_fieldssource_field_target_field": {
                        "type": "string",
                        "description": "The fields that will determine if there is an attribute change between the matched update and base features.",
                        "default": None
                },
                "compare_line_direction": {
                        "type": "string",
                        "description": "Specifies whether line directions will be compared for matched features.NO_COMPARE_DIRECTION\u2014Line directions will not be compared for matched features. This is the default.COMPARE_DIRECTION\u2014Line direc...",
                        "default": None
                }
        },
        "required": [
                "update_features",
                "base_features",
                "out_feature_class",
                "search_distance"
        ]
},
    "feature_compare": {
        "name": "feature_compare",
        "description": "Compares two feature classes or layers and returns the comparison results.",
        "parameters": {
                "in_base_features": {
                        "type": "string",
                        "description": "The data that will be compared with the in_test_features parameter value. This parameter value is data that you have declared valid. This base data has the correct content and information."
                },
                "in_test_features": {
                        "type": "string",
                        "description": "The data that will be compared with the in_base_features parameter value. This parameter value is data that you have made changes to by editing or compiling new information."
                },
                "sort_field": {
                        "type": "string",
                        "description": "The field or fields that will be used to sort records in the inputs. The records are sorted in ascending order. Sorting by a common field in both inputs ensures that you are comparing the same row fro..."
                },
                "compare_type": {
                        "type": "string",
                        "description": "Specifies the comparison type that will be used.ALL\u2014All properties of the feature classes will be compared. This is the default.GEOMETRY_ONLY\u2014Only the geometries of the feature classes will be compare...",
                        "default": None
                },
                "ignore_options": {
                        "type": "string",
                        "description": "Specifies the properties that will not be compared.IGNORE_M\u2014Measure properties will not be compared.IGNORE_Z\u2014Elevation properties will not be compared.IGNORE_POINTID\u2014Point ID properties will not be co...",
                        "default": None
                },
                "xy_tolerance": {
                        "type": "string",
                        "description": "The distance that will determine the range in which features will be considered equal. To minimize error, the parameter value should be as small as possible. By default, the compare tolerance is the x...",
                        "default": None
                },
                "m_tolerance": {
                        "type": "string",
                        "description": "The minimum distance between measures before they will be considered equal.",
                        "default": None
                },
                "z_tolerance": {
                        "type": "string",
                        "description": "The minimum distance between z-coordinates before they will be considered equal.",
                        "default": None
                },
                "attribute_tolerancesfield_tolerance": {
                        "type": "string",
                        "description": "The numeric value that will determine the range in which attribute values are considered equal. This parameter only applies to numeric field types.",
                        "default": None
                },
                "omit_field": {
                        "type": "string",
                        "description": "The field or fields that will be omitted during comparison. The field definitions and the tabular values for these fields will be ignored.",
                        "default": None
                },
                "continue_compare": {
                        "type": "string",
                        "description": "Specifies whether the comparison will continue after encountering the first difference between the inputs.NO_CONTINUE_COMPARE\u2014The tool will stop after encountering the first difference. This is the de...",
                        "default": None
                },
                "out_compare_file": {
                        "type": "string",
                        "description": "The output file that will contain all similarities and differences between the  inputs. This file is a comma-delimited text file that can be viewed and used as a table in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_base_features",
                "in_test_features",
                "sort_field"
        ]
},
    "file_compare": {
        "name": "file_compare",
        "description": "Compares two files and returns the comparison results.",
        "parameters": {
                "in_base_file": {
                        "type": "string",
                        "description": "The file that will be compared with the in_test_file parameter value. This parameter value is a file that you have declared valid. This base file has the correct content and information."
                },
                "in_test_file": {
                        "type": "string",
                        "description": "The file that will be compared with the in_base_file parameter value. This parameter value is a file that you have made changes to by editing or compiling new information."
                },
                "file_type": {
                        "type": "string",
                        "description": "Specifies the type of comparison that will be used for the files. ASCII\u2014The files will be compared using ASCII characters. This is the default.BINARY\u2014The files will be compared using a binary compare.",
                        "default": None
                },
                "continue_compare": {
                        "type": "string",
                        "description": "Specifies whether the comparison will continue after encountering the first difference between the inputs.NO_CONTINUE_COMPARE\u2014The tool will stop after encountering the first difference. This is the de...",
                        "default": None
                },
                "out_compare_file": {
                        "type": "string",
                        "description": "The output file that will contain all similarities and differences between the  inputs. This file is a comma-delimited text file that can be viewed and used as a table in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_base_file",
                "in_test_file"
        ]
},
    "raster_compare": {
        "name": "raster_compare",
        "description": "Compares the properties of two raster datasets or two mosaic datasets.",
        "parameters": {
                "in_base_raster": {
                        "type": "string",
                        "description": "The raster or mosaic dataset that will be compared with the in_test_raster parameter value. This parameter value is data that you have declared valid. This base data has the correct content and inform..."
                },
                "in_test_raster": {
                        "type": "string",
                        "description": "The raster or mosaic dataset that will be compared with the in_base_raster parameter value. This parameter value is data that you have made changes to by editing or compiling new information."
                },
                "compare_type": {
                        "type": "string",
                        "description": "Specifies the type of rasters that will be compared.RASTER_DATASET\u2014Two raster datasets will be compared. GDB_RASTER_DATASET\u2014Two raster datasets in a geodatabase will be compared. MOSAIC_DATASET\u2014Two mo...",
                        "default": None
                },
                "ignore_option": {
                        "type": "string",
                        "description": "Specifies the properties that will be ignored in the comparison.BandCount\u2014The number of bands will be ignored.Extent\u2014The extent will be ignored.Columns And Rows\u2014The number of columns and rows will be ...",
                        "default": None
                },
                "continue_compare": {
                        "type": "string",
                        "description": "Specifies whether the comparison will continue after encountering the first difference between the inputs.NO_CONTINUE_COMPARE\u2014The tool will stop after encountering the first difference. This is the de...",
                        "default": None
                },
                "out_compare_file": {
                        "type": "string",
                        "description": "The output file that will contain all similarities and differences between the  inputs. This file is a comma-delimited text file that can be viewed and used as a table in ArcGIS.",
                        "default": None
                },
                "parameter_tolerancesparameter_tolerance_type": {
                        "type": "string",
                        "description": "The tolerances that determine the range in which values will be considered equal.\r\nThe same tolerance can be applied to all parameters, or  different tolerances can be applied to individual\r\nparameter...",
                        "default": None
                },
                "attribute_tolerancesfield_tolerance": {
                        "type": "string",
                        "description": "The numeric value that will determine the range in which attribute values are considered equal. This parameter only applies to numeric field types.",
                        "default": None
                },
                "omit_field": {
                        "type": "string",
                        "description": "The field or fields that will be omitted during comparison. The field definitions and the tabular values for these fields will be ignored.",
                        "default": None
                }
        },
        "required": [
                "in_base_raster",
                "in_test_raster"
        ]
},
    "table_compare": {
        "name": "table_compare",
        "description": "Compares two tables or table views and returns the comparison results.",
        "parameters": {
                "in_base_table": {
                        "type": "string",
                        "description": "The data that will be compared with the in_test_table parameter value. This parameter value is data that you have declared valid. This base data has the correct content and information."
                },
                "in_test_table": {
                        "type": "string",
                        "description": "The data that will be compared with the in_base_table parameter value. This parameter value is data that you have made changes to by editing or compiling new information."
                },
                "sort_field": {
                        "type": "string",
                        "description": "The field or fields that will be used to sort records in the inputs. The records are sorted in ascending order. Sorting by a common field in both inputs ensures that you are comparing the same row fro..."
                },
                "compare_type": {
                        "type": "string",
                        "description": "Specifies the comparison type that will be used.ALL\u2014All properties will be compared. This is the default.ATTRIBUTES_ONLY\u2014Only the attributes and their values will be compared.SCHEMA_ONLY\u2014Only the sche...",
                        "default": None
                },
                "ignore_options": {
                        "type": "string",
                        "description": "Specifies the table properties that will not be compared.IGNORE_EXTENSION_PROPERTIES\u2014Extension properties will not be compared.IGNORE_SUBTYPES\u2014Subtypes will not be compared.IGNORE_RELATIONSHIPCLASSES\u2014...",
                        "default": None
                },
                "attribute_tolerancesfield_tolerance": {
                        "type": "string",
                        "description": "The numeric value that will determine the range in which attribute values are considered equal. This parameter only applies to numeric field types.",
                        "default": None
                },
                "omit_field": {
                        "type": "string",
                        "description": "The field or fields that will be omitted during comparison. The field definitions and the tabular values for these fields will be ignored.",
                        "default": None
                },
                "continue_compare": {
                        "type": "string",
                        "description": "Specifies whether the comparison will continue after encountering the first difference between the inputs.NO_CONTINUE_COMPARE\u2014The tool will stop after encountering the first difference. This is the de...",
                        "default": None
                },
                "out_compare_file": {
                        "type": "string",
                        "description": "The output file that will contain all similarities and differences between the  inputs. This file is a comma-delimited text file that can be viewed and used as a table in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_base_table",
                "in_test_table",
                "sort_field"
        ]
},
    "tin_compare": {
        "name": "tin_compare",
        "description": "Compares two TINs and returns the comparison results.",
        "parameters": {
                "in_base_tin": {
                        "type": "string",
                        "description": "The data that will be compared with the in_test_tin parameter value. This parameter value is data that you have declared valid. This base data has the correct content and information."
                },
                "in_test_tin": {
                        "type": "string",
                        "description": "The data that will be compared with the in_base_tin parameter value. This parameter value is data that you have made changes to by editing or compiling new information."
                },
                "compare_type": {
                        "type": "string",
                        "description": "Specifies the comparison type that will be used.ALL\u2014All properties will be compared. This is the default. PROPERTIES_ONLY\u2014Both geometry and TIN tag values, if any, that are assigned to nodes and trian...",
                        "default": None
                },
                "continue_compare": {
                        "type": "string",
                        "description": "Specifies whether the comparison will continue after encountering the first difference between the inputs.NO_CONTINUE_COMPARE\u2014The tool will stop after encountering the first difference. This is the de...",
                        "default": None
                },
                "out_compare_file": {
                        "type": "string",
                        "description": "The output file that will contain all similarities and differences between the  inputs. This file is a comma-delimited text file that can be viewed and used as a table in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_base_tin",
                "in_test_tin"
        ]
},
    "create_data_loading_workspace": {
        "name": "create_data_loading_workspace",
        "description": "Creates a data loading workspace that can be used for data loading. The output workspace contains a collection of Microsoft Excel workbooks. These workbooks can be used to configure the source and target schema mapping. Learn more about data loading workspace concepts",
        "parameters": {
                "source_target_mapping": {
                        "type": "string",
                        "description": "Defines how source data will be mapped to the target schema. Both workspaces and individual classes are supported as source or target inputs. When workspaces are used, name similarity is used to match..."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The output folder where the data loading workspace will be created."
                },
                "match_options": {
                        "type": "string",
                        "description": "Specifies whether field names or domain value descriptions will be matched.MATCH_FIELDS\u2014Field names will be matched based on similarity between the source and\r\ntarget fields.MATCH_VALUES\u2014Attribute dom...",
                        "default": None
                },
                "mapping_table": {
                        "type": "string",
                        "description": "A table that will be used to perform substring matching for datasets, values, and attribute domain coded value descriptions. Use the table to create matches or block them.",
                        "default": None
                },
                "calc_stats": {
                        "type": "string",
                        "description": "Specifies whether the count and percentage of filled-in values will be calculated for fields in the source schema.CALC_STATS\u2014The count and percentage of filled-in values will be calculated.NO_STATS\u2014No...",
                        "default": None
                },
                "match_subtypes": {
                        "type": "string",
                        "description": "Specifies whether separate data mapping workbooks will be created by subtype if they exist.MATCH_SUBTYPES\u2014Separate data mapping workbooks will be created for each match if they exist. The class name w...",
                        "default": None
                }
        },
        "required": [
                "source_target_mapping",
                "out_folder"
        ]
},
    "generate_mapping_table": {
        "name": "generate_mapping_table",
        "description": "Generates the Mapping Table based on a configured data loading workspace. The table includes a list of  predefined datasets, fields, and attribute domain coded value descriptions.\r\nThis output table is used as input to the Create Data Loading Workspace tool.",
        "parameters": {
                "in_workbook": {
                        "type": "string",
                        "description": "The Data Reference Workbook that will be used to generate a Mapping Table."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table, which will include a list of datasets, fields, and attribute domain coded value descriptions based on the source and target mapping from a Data Loading Workspace. Use this table in t..."
                }
        },
        "required": [
                "in_workbook",
                "out_table"
        ]
},
    "load_data_to_preview": {
        "name": "load_data_to_preview",
        "description": "Uses a Data Loading Workspace to load data from a source to a preview geodatabase. Use this tool to preview the results before loading data to the target schema.",
        "parameters": {
                "in_workbook": {
                        "type": "string",
                        "description": "The path to the Data Reference Workbook defining the data source, target, and mapping workbook paths."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The output folder where the preview geodatabase will be created."
                }
        },
        "required": [
                "in_workbook",
                "out_folder"
        ]
},
    "load_data_using_workspace": {
        "name": "load_data_using_workspace",
        "description": "Uses the Data Reference Workbook from the Data Loading Workspace to load data from a source to a target dataset.",
        "parameters": {
                "in_workbook": {
                        "type": "string",
                        "description": "The path to the Data Reference Workbook defining the data source, target, and mapping workbook paths."
                }
        },
        "required": [
                "in_workbook"
        ]
},
    "update_data_loading_workspace_schema": {
        "name": "update_data_loading_workspace_schema",
        "description": "Creates a copy of the  Data Loading Workspace and updates all the mapping and domain workbooks.",
        "parameters": {
                "in_workbook": {
                        "type": "string",
                        "description": "The path to Data Reference Workbook defining the data source, target, and mapping workbook paths."
                }
        },
        "required": [
                "in_workbook"
        ]
},
    "compare_replica_schema": {
        "name": "compare_replica_schema",
        "description": "Generates an .xml file that describes schema differences between a replica geodatabase and the relative replica geodatabase.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The replica geodatabase to which the replica schema will be compared. The geodatabase can be a local geodatabase or a geodata service."
                },
                "in_source_file": {
                        "type": "string",
                        "description": "The file that contains the relative replica schema that will be used for the comparison."
                },
                "output_replica_schema_changes_file": {
                        "type": "string",
                        "description": "The file that will contain a description of the schema differences."
                }
        },
        "required": [
                "in_geodatabase",
                "in_source_file",
                "output_replica_schema_changes_file"
        ]
},
    "create_replica": {
        "name": "create_replica",
        "description": "Creates a replica in a geodatabase from a specified list of feature classes, layers, datasets, and tables in an enterprise geodatabase.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The data that will be replicated. This list consists of layers and tables referencing versioned, editable data from an enterprise geodatabase."
                },
                "in_type": {
                        "type": "string",
                        "description": "Specifies the type of replica that will be created.TWO_WAY_REPLICA\u2014 Changes will be sent between child and parent replicas in both directions.ONE_WAY_REPLICA\u2014Changes will be sent from the parent repli..."
                },
                "out_geodatabase": {
                        "type": "string",
                        "description": "The geodatabase that will host the child replica. Geodata services are used to represent remote geodatabases. The geodatabase can be an enterprise or file geodatabase. For two-way and one-way-child-to...",
                        "default": None
                },
                "out_name": {
                        "type": "string",
                        "description": "The name that identifies the replica."
                },
                "access_type": {
                        "type": "string",
                        "description": "Specifies the type of replica access.FULL\u2014Complex types such as topologies, are supported and the data must be versioned. This is the default.SIMPLE\u2014The data on the child is not versioned and must be ...",
                        "default": None
                },
                "initial_data_sender": {
                        "type": "string",
                        "description": "Specifies which replica will send changes when in disconnected mode. If you are working in a connected mode, this parameter is inconsequential. This ensures that the relative replica will not send upd...",
                        "default": None
                },
                "expand_feature_classes_and_tables": {
                        "type": "string",
                        "description": "Specifies whether expanded feature classes and tables\u2014such as those in networks, topologies, or relationship classes\u2014will be added.USE_DEFAULTS\u2014The expanded feature classes and tables related to the f...",
                        "default": None
                },
                "reuse_schema": {
                        "type": "string",
                        "description": "Specifies whether a geodatabase that contains the schema of the data to be replicated will be reused. This reduces the amount of time required to replicate the data. This parameter is only available f...",
                        "default": None
                },
                "get_related_data": {
                        "type": "string",
                        "description": "Specifies whether rows related to rows existing in the replica will be replicated. For example, a feature (f1) is inside the replication filter and a related feature (f2) from another class is outside...",
                        "default": None
                },
                "geometry_features": {
                        "type": "string",
                        "description": "The features that will be used to define the area to replicate.",
                        "default": None
                },
                "archiving": {
                        "type": "string",
                        "description": "Specifies whether the archive class will be used to track changes instead of the versioning delta tables. This is only available for one-way replicas.ARCHIVING\u2014Archiving will be used to track changes....",
                        "default": None
                },
                "register_existing_data": {
                        "type": "string",
                        "description": "Specifies whether existing \r\ndata in the child geodatabase will be used to register the replica datasets. The datasets in the child geodatabase must have the same names as the datasets in the parent g...",
                        "default": None
                },
                "out_type": {
                        "type": "string",
                        "description": "Specifies the output type of the data that will be replicated.\r\nGEODATABASE\u2014The data will be replicated to an existing geodatabase. This is the default.XML_FILE\u2014The data will be replicated to an XML w...",
                        "default": None
                },
                "out_xml": {
                        "type": "string",
                        "description": "The name and location of the .xml file that will be created. \r\nThis parameter is required if the out_type parameter is set to XML_FILE.",
                        "default": None
                },
                "all_records_for_tables": {
                        "type": "string",
                        "description": "Specifies whether all records or only the schema will be copied to the child geodatabase for tables that do not have filters applied (such as selections or definition queries).Tables with applied filt...",
                        "default": None
                },
                "out_filegdb_folder_path": {
                        "type": "string",
                        "description": "The location of the file  geodatabase that will be created to host the child replica. This parameter is required if the out_type parameter is set to NEW_FILE_GEODATABASE and is only valid for one-way ...",
                        "default": None
                },
                "out_filegdb_name": {
                        "type": "string",
                        "description": "The name of the file  geodatabase that will be created to host the child replica. This parameter is required if the out_type parameter is set to NEW_FILE_GEODATABASE and is only valid for one-way and ...",
                        "default": None
                }
        },
        "required": [
                "in_data",
                "in_type",
                "out_name"
        ]
},
    "create_replica_from_server": {
        "name": "create_replica_from_server",
        "description": "Creates a replica using a specified list of feature classes, layers, feature datasets, and tables from a remote geodatabase using a geodata service published on ArcGIS Server.",
        "parameters": {
                "in_geodataservice": {
                        "type": "string",
                        "description": "The geodata service representing the geodatabase from which the replica will be created. The geodatabase referenced by the geodata service must be an enterprise geodatabase."
                },
                "datasetsdataset_name": {
                        "type": "string",
                        "description": "The list of the feature datasets, stand-alone feature classes, tables, and stand-alone attributed relationship classes from the geodata service that will be replicated."
                },
                "in_type": {
                        "type": "string",
                        "description": "Specifies the type of replica that will be created.TWO_WAY_REPLICA\u2014 Changes will be sent between child and parent replicas in both directions.ONE_WAY_REPLICA\u2014Changes will be sent from the parent repli..."
                },
                "out_geodatabase": {
                        "type": "string",
                        "description": "The local geodatabase that will host the child replica. Geodata services are used to represent remote geodatabases. The geodatabase can be an enterprise or file geodatabase. For two-way replicas, the ..."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name that identifies the replica."
                },
                "access_type": {
                        "type": "string",
                        "description": "Specifies the type of replica access.FULL\u2014Complex types such as topologies, are supported and the data must be versioned. This is the default.SIMPLE\u2014The data on the child is not versioned and must be ...",
                        "default": None
                },
                "initial_data_sender": {
                        "type": "string",
                        "description": "Specifies which replica will send changes when in disconnected mode. If you are working in a connected mode, this parameter is inconsequential. This ensures that the relative replica will not send upd...",
                        "default": None
                },
                "expand_feature_classes_and_tables": {
                        "type": "string",
                        "description": "Specifies whether expanded feature classes and tables\u2014such as those in networks, topologies, or relationship classes\u2014will be added.USE_DEFAULTS\u2014The expanded feature classes and tables related to the f...",
                        "default": None
                },
                "reuse_schema": {
                        "type": "string",
                        "description": "Specifies whether a geodatabase that contains the schema of the data to be replicated will be reused. This reduces the amount of time required to replicate the data. This parameter is only available f...",
                        "default": None
                },
                "get_related_data": {
                        "type": "string",
                        "description": "Specifies whether rows related to rows existing in the replica will be replicated. For example, a feature (f1) is inside the replication filter and a related feature (f2) from another class is outside...",
                        "default": None
                },
                "geometry_features": {
                        "type": "string",
                        "description": "The features that will be used to define the area to replicate.",
                        "default": None
                },
                "archiving": {
                        "type": "string",
                        "description": "Specifies whether the archive class will be used to track changes instead of the versioning delta tables. This is only available for one-way replicas.ARCHIVING\u2014Archiving will be used to track changes....",
                        "default": None
                },
                "all_records_for_tables": {
                        "type": "string",
                        "description": "Specifies whether all records or only the schema will be copied to the child geodatabase for tables that do not have filters applied (such as selections or definition queries).Tables with applied filt...",
                        "default": None
                }
        },
        "required": [
                "in_geodataservice",
                "datasetsdataset_name",
                "in_type",
                "out_geodatabase",
                "out_name"
        ]
},
    "disable_replica_tracking": {
        "name": "disable_replica_tracking",
        "description": "Disables replica tracking on data. Replica tracking is automatically disabled when a versioned dataset is unregistered as versioned or a nonversioned dataset has archiving disabled.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The enterprise geodatabase table, feature class, feature dataset, attributed relationship class, or many-to-many relationship class on which to disable replica tracking."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "enable_replica_tracking": {
        "name": "enable_replica_tracking",
        "description": "Enables replica tracking on data, allowing you to work with  offline maps and in distributed collaborations. Replica tracking applies to services that are configured with the sync capability with the option of creating a version for each downloaded map. To disable replica tracking on data, use the Disable Replica Tracking tool. Learn more about preparing data for offline use",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The enterprise geodatabase table, feature class, feature dataset, attributed relationship class, or many-to-many relationship class on which replica tracking will be enabled."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "export_acknowledgement_message": {
        "name": "export_acknowledgement_message",
        "description": "Creates an output acknowledgement file to acknowledge the reception of previously received data change messages.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "Specifies the replica geodatabase from which to export the acknowledgement message. The geodatabase may be local or remote."
                },
                "out_acknowledgement_file": {
                        "type": "string",
                        "description": "Specifies the delta file to export to."
                },
                "in_replica": {
                        "type": "string",
                        "description": "The replica from which the acknowledgement message will be exported."
                }
        },
        "required": [
                "in_geodatabase",
                "out_acknowledgement_file",
                "in_replica"
        ]
},
    "export_data_change_message": {
        "name": "export_data_change_message",
        "description": "Creates an output delta file containing updates from an input replica.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The replica geodatabase from which the data change message will be exported. The geodatabase can be local or remote."
                },
                "out_data_changes_file": {
                        "type": "string",
                        "description": "The output delta file."
                },
                "in_replica": {
                        "type": "string",
                        "description": "The replica containing the updates to be exported."
                },
                "switch_to_receiver": {
                        "type": "string",
                        "description": "Specifies whether the replica will be changed from a sender to a receiver. The receiver may not send replica updates until updates from the relative replica sender arrive.DO_NOT_SWITCH\u2014The replica rol..."
                },
                "include_unacknowledged_changes": {
                        "type": "string",
                        "description": "Specifies whether data changes that were previously exported for which no acknowledgment message was received will be included.NO_UNACKNOWLEDGED\u2014Data changes that were previously sent will not be incl..."
                },
                "include_new_changes": {
                        "type": "string",
                        "description": "Specifies whether all data changes made since the last exported data change message will be included.NO_NEW_CHANGES\u2014Data changes made since the last exported data change message will not be included.N..."
                }
        },
        "required": [
                "in_geodatabase",
                "out_data_changes_file",
                "in_replica",
                "switch_to_receiver",
                "include_unacknowledged_changes",
                "include_new_changes"
        ]
},
    "export_replica_schema": {
        "name": "export_replica_schema",
        "description": "Creates a replica schema file with the schema of an input one- or two-way replica.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The replica geodatabase from which the replica schema will be exported. The geodatabase can be a local or remote geodatabase."
                },
                "output_replica_schema_file": {
                        "type": "string",
                        "description": "The file to which the replica schema will be exported."
                },
                "in_replica": {
                        "type": "string",
                        "description": "The replica from which the schema will be exported."
                }
        },
        "required": [
                "in_geodatabase",
                "output_replica_schema_file",
                "in_replica"
        ]
},
    "import_message": {
        "name": "import_message",
        "description": "Imports changes from a delta file into a replica geodatabase or imports an acknowledgment message into a replica geodatabase.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The replica geodatabase that will receive the imported message. The geodatabase can be local or remote."
                },
                "source_delta_file": {
                        "type": "string",
                        "description": "The file from which the message will be imported."
                },
                "output_acknowledgement_file": {
                        "type": "string",
                        "description": "The file that will contain the acknowledgement message. When importing data changes, you can also export a message to acknowledge the import of a data change message. This parameter is only supported ...",
                        "default": None
                },
                "conflict_policy": {
                        "type": "string",
                        "description": "Specifies how conflicts will be resolved when they are encountered while importing a data change message.MANUAL\u2014Conflicts must be manually resolved in the versioning reconcile environment. IN_FAVOR_OF...",
                        "default": None
                },
                "conflict_definition": {
                        "type": "string",
                        "description": "Specifies whether the conditions required for a conflict to occur will be detected by object (row) or by attribute (column).BY_OBJECT\u2014Conflicts will be detected by row.BY_ATTRIBUTE\u2014Conflicts will be d...",
                        "default": None
                }
        },
        "required": [
                "in_geodatabase",
                "source_delta_file"
        ]
},
    "import_replica_schema": {
        "name": "import_replica_schema",
        "description": "Applies replica schema differences using an input replica geodatabase and an XML schema file.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The replica geodatabase to which the replica schema will be imported. The geodatabase can be a local geodatabase or a geodata service."
                },
                "in_source": {
                        "type": "string",
                        "description": "The file that contains the replica schema differences that will be imported."
                }
        },
        "required": [
                "in_geodatabase",
                "in_source"
        ]
},
    "re_export_unacknowledged_messages": {
        "name": "re_export_unacknowledged_messages",
        "description": "Creates an output delta file containing unacknowledged replica updates from a one-way or two-way replica geodatabase.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The replica geodatabase from which the unacknowledged messages will be reexported. The geodatabase can be a local geodatabase or a geodata service."
                },
                "output_delta_file": {
                        "type": "string",
                        "description": "The delta file to which data changes will be reexported."
                },
                "in_replica": {
                        "type": "string",
                        "description": "The replica from which the unacknowledged messages will be reexported."
                },
                "in_export_option": {
                        "type": "string",
                        "description": "Specifies the changes that will be reexported.ALL_UNACKNOWLEDGED\u2014All changes with unacknowledged messages will be reexported.MOST_RECENT\u2014Only those changes made since the last set of exported changes ..."
                }
        },
        "required": [
                "in_geodatabase",
                "output_delta_file",
                "in_replica",
                "in_export_option"
        ]
},
    "synchronize_changes": {
        "name": "synchronize_changes",
        "description": "Synchronizes updates between two replica geodatabases in a specified direction.",
        "parameters": {
                "geodatabase_1": {
                        "type": "string",
                        "description": "The geodatabase hosting the replica to synchronize. The geodatabase can be local or remote."
                },
                "in_replica": {
                        "type": "string",
                        "description": "A valid replica with a parent contained in one input geodatabase and a child in the other input geodatabase."
                },
                "geodatabase_2": {
                        "type": "string",
                        "description": "The geodatabase hosting the relative replica. The geodatabase can be local or remote."
                },
                "in_direction": {
                        "type": "string",
                        "description": "Specifies the direction in which the changes will be synchronized: from geodatabase 1 to geodatabase 2, from geodatabase 2 to geodatabase 1, or in both directions. For check-out/check-in replicas or o..."
                },
                "conflict_policy": {
                        "type": "string",
                        "description": "Specifies how conflicts will be resolved when they are encountered.MANUAL\u2014Conflicts will be resolved manually in the versioning reconcile environment.IN_FAVOR_OF_GDB1\u2014Conflicts will be resolved in fav..."
                },
                "conflict_definition": {
                        "type": "string",
                        "description": "Specifies how conflicts will be defined.BY_OBJECT\u2014Changes to the same row or feature in the parent and child versions will conflict during reconcile. This is the default.BY_ATTRIBUTE\u2014 Only changes to ..."
                },
                "reconcile": {
                        "type": "string",
                        "description": "Specifies whether to automatically reconcile once data changes are sent to the parent replica if there are no conflicts present. This option is only available for check-out/check-in replicas.DO_NOT_RE..."
                }
        },
        "required": [
                "geodatabase_1",
                "in_replica",
                "geodatabase_2",
                "in_direction",
                "conflict_policy",
                "conflict_definition",
                "reconcile"
        ]
},
    "unregister_replica": {
        "name": "unregister_replica",
        "description": "Unregisters a replica from an enterprise geodatabase.",
        "parameters": {
                "in_geodatabase": {
                        "type": "string",
                        "description": "The enterprise geodatabase that contains the replica to unregister."
                },
                "in_replica": {
                        "type": "string",
                        "description": "The name or ID of the replica that will be unregistered. If providing the replica name, it must be fully qualified, for example, myuser.myreplica."
                }
        },
        "required": [
                "in_geodatabase",
                "in_replica"
        ]
},
    "add_coded_value_to_domain": {
        "name": "add_coded_value_to_domain",
        "description": "Adds a value to a domain's coded value list.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase containing the domain to be updated."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the attribute domain that will have a value added to its coded value list."
                },
                "code": {
                        "type": "string",
                        "description": "The value to be added to the specified domain's coded value list."
                },
                "code_description": {
                        "type": "string",
                        "description": "A description of what the coded value represents."
                }
        },
        "required": [
                "in_workspace",
                "domain_name",
                "code",
                "code_description"
        ]
},
    "alter_domain": {
        "name": "alter_domain",
        "description": "Alters the properties of an existing attribute domain in a workspace.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase that contains the domain that will be altered."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the domain the will be altered."
                },
                "new_domain_name": {
                        "type": "string",
                        "description": "The new name of the domain.",
                        "default": None
                },
                "new_domain_description": {
                        "type": "string",
                        "description": "The new description of the domain.",
                        "default": None
                },
                "split_policy": {
                        "type": "string",
                        "description": "Specifies the split policy that will used for the domain. The behavior of an attribute's values when a feature is split is controlled by its split policy.\r\nDEFAULT\u2014The attributes of the two resulting ...",
                        "default": None
                },
                "merge_policy": {
                        "type": "string",
                        "description": "Specifies the merge policy that will be used for the domain. When two features are merged into a single feature, merge policies will control attribute values in the new feature.\r\nThis parameter is onl...",
                        "default": None
                },
                "new_domain_owner": {
                        "type": "string",
                        "description": "The name of the database user that the domain ownership will be transferred to.\r\nEnsure that the new domain owner exists in the database; the tool does not check the validity of the owner name specifi...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "domain_name"
        ]
},
    "assign_domain_to_field": {
        "name": "assign_domain_to_field",
        "description": "Sets the domain for a particular field and, optionally, for a subtype. If no subtype is specified, the domain is only assigned to the specified field.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The name of the table or feature class containing the field that will be assigned a domain."
                },
                "field_name": {
                        "type": "string",
                        "description": "The name of the field that will be assigned a domain."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of a geodatabase domain that will be assigned to the field name. Available domains will be loaded automatically."
                },
                "subtype_code": {
                        "type": "string",
                        "description": "The subtype code that will be assigned a domain.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field_name",
                "domain_name"
        ]
},
    "create_domain": {
        "name": "create_domain",
        "description": "Creates an attribute domain in the specified workspace.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase that will contain the new domain."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the domain that will be created."
                },
                "domain_description": {
                        "type": "string",
                        "description": "The description of the domain that will be created.",
                        "default": None
                },
                "field_type": {
                        "type": "string",
                        "description": "Specifies the type of attribute domain that will be created. Attribute domains are rules that describe the accepted values of a field type. Specify a field type that matches the data type of the field...",
                        "default": None
                },
                "domain_type": {
                        "type": "string",
                        "description": "Specifies the domain type that will be created.CODED\u2014A coded type domain will be created that contains a valid set of values for an attribute. This is the default. For example, a coded value domain ca...",
                        "default": None
                },
                "split_policy": {
                        "type": "string",
                        "description": "Specifies the split policy that will be used for the created domain. The behavior of an attribute's values when a feature that is split is controlled by its split policy.DEFAULT\u2014The attributes of the ...",
                        "default": None
                },
                "merge_policy": {
                        "type": "string",
                        "description": "Specifies the merge policy that will be used for the created domain. When two features are merged into a single feature, merge policies control attribute values in the new feature.DEFAULT\u2014The attribut...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "domain_name"
        ]
},
    "delete_coded_value_from_domain": {
        "name": "delete_coded_value_from_domain",
        "description": "Removes a value from a coded value domain.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The workspace containing the domain to be updated."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the coded value domain to be updated."
                },
                "code": {
                        "type": "string",
                        "description": "The values to be deleted from the specified domain."
                }
        },
        "required": [
                "in_workspace",
                "domain_name",
                "code"
        ]
},
    "delete_domain": {
        "name": "delete_domain",
        "description": "Deletes a domain from a workspace.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase that contains the domain to be deleted."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the domain to be deleted."
                }
        },
        "required": [
                "in_workspace",
                "domain_name"
        ]
},
    "domain_to_table": {
        "name": "domain_to_table",
        "description": "Creates a table from an attribute domain.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The workspace containing the attribute domain to be converted to a table."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the existing attribute domain."
                },
                "out_table": {
                        "type": "string",
                        "description": "The table to be created."
                },
                "code_field": {
                        "type": "string",
                        "description": "The name of the field in the created table that will store code values."
                },
                "description_field": {
                        "type": "string",
                        "description": "The name of the field in the created table that will store code value descriptions."
                },
                "configuration_keyword": {
                        "type": "string",
                        "description": "For geodatabase tables, the custom storage keywords for creating the table.",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "domain_name",
                "out_table",
                "code_field",
                "description_field"
        ]
},
    "remove_domain_from_field": {
        "name": "remove_domain_from_field",
        "description": "Removes an attribute domain association from a feature class or table field.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table containing the attribute domain that will be removed."
                },
                "field_name": {
                        "type": "string",
                        "description": "The field that will no longer be associated with an attribute domain."
                },
                "subtype_code": {
                        "type": "string",
                        "description": "The subtype code(s) that will no longer be associated with an attribute domain.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field_name"
        ]
},
    "set_value_for_range_domain": {
        "name": "set_value_for_range_domain",
        "description": "Sets the minimum and maximum values for an existing Range domain.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase containing the domain to be updated."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the range domain to be updated."
                },
                "min_value": {
                        "type": "string",
                        "description": "The minimum value of the range domain."
                },
                "max_value": {
                        "type": "string",
                        "description": "The maximum value of the range domain."
                }
        },
        "required": [
                "in_workspace",
                "domain_name",
                "min_value",
                "max_value"
        ]
},
    "sort_coded_value_domain": {
        "name": "sort_coded_value_domain",
        "description": "Sorts the code or description of a coded value domain in either ascending or descending order.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase containing the domain to be sorted."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the coded value domain to be sorted."
                },
                "sort_by": {
                        "type": "string",
                        "description": "Specifies whether the code or description will be used to sort the domain. CODE\u2014Records are sorted based on the code value for the domain.DESCRIPTION\u2014Records are sorted based on the description value ..."
                },
                "sort_order": {
                        "type": "string",
                        "description": "Specifies the direction the records will be sorted. ASCENDING\u2014Records are sorted from low value to high value.DESCENDING\u2014Records are sorted from high value to low value."
                }
        },
        "required": [
                "in_workspace",
                "domain_name",
                "sort_by",
                "sort_order"
        ]
},
    "table_to_domain": {
        "name": "table_to_domain",
        "description": "Creates or updates a coded value domain with values from a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The database table from which the domain values will be derived."
                },
                "code_field": {
                        "type": "string",
                        "description": "The field in the database table from which the domain code values will be derived."
                },
                "description_field": {
                        "type": "string",
                        "description": "The field in the database table from which the domain description values will be derived."
                },
                "in_workspace": {
                        "type": "string",
                        "description": "The workspace that contains the domain that will be created or updated."
                },
                "domain_name": {
                        "type": "string",
                        "description": "The name of the domain that will be created or updated."
                },
                "domain_description": {
                        "type": "string",
                        "description": "The description of the domain that will be created or updated. Domain descriptions of existing domains are not updated.",
                        "default": None
                },
                "update_option": {
                        "type": "string",
                        "description": "Specifies how the domain will be updated when you're using an existing domain.APPEND\u2014The values from the input table will be appended to the existing domain values. This is the default.REPLACE\u2014The exi...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "code_field",
                "description_field",
                "in_workspace",
                "domain_name"
        ]
},
    "disable_feature_binning": {
        "name": "disable_feature_binning",
        "description": "Disables database computed feature binning on a feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class for which database computed feature binning will be disabled."
                }
        },
        "required": [
                "in_features"
        ]
},
    "enable_feature_binning": {
        "name": "enable_feature_binning",
        "description": "Enables database computation for feature binning on a point feature class. Feature binning is an advanced visualization capability that allows you to explore and visualize large datasets. It also helps you observe patterns at macro and micro levels with out-of-the-box mapping options. Feature binning aggregates large amounts of features into dynamic polygon bins that vary through scaled levels of detail. A single bin represents all features within its boundaries at that level of detail. Feature binning can improve both drawing performance and data comprehension. Learn more about binned feature layers",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class for which database computed feature binning will be enabled. Supported input types are point feature classes stored in a mobile geodatabase, enterprise geodatabase or database, or cl..."
                },
                "bin_type": {
                        "type": "string",
                        "description": "Specifies the type of binning that will be enabled. If you are using SAP HANA data, only the SQUARE, FLAT_HEXAGON, and POINTY_HEXAGON options are supported.  If you are using Snowflake or Redshift dat...",
                        "default": None
                },
                "bin_coord_sys": {
                        "type": "string",
                        "description": "The coordinate systems that will be used to visualize the aggregated output feature layer.\r\nYou can specify up to two coordinate systems to visualize the output layer. By default, the coordinate syste...",
                        "default": None
                },
                "summary_statsfield_statistic_type": {
                        "type": "string",
                        "description": "Specifies the statistics that will be summarized and stored in the bin cache. Statistics are used to symbolize bins and provide aggregate information for all the features in a bin.\r\nOne summary statis...",
                        "default": None
                },
                "generate_static_cache": {
                        "type": "string",
                        "description": "Specifies whether a static cache\r\nof the aggregated results will be generated or visualizations will be aggregated on the fly. The cache is not necessarily created for all levels of detail.STATIC_CACH...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "manage_feature_bin_cache": {
        "name": "manage_feature_bin_cache",
        "description": "Manages the feature binning cache for data that has database computed feature binning enabled. Feature binning aggregates large amounts of features into dynamic polygon bins that vary through scaled levels of detail. Learn how to enable database computed feature binning and work with binned feature layers.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The binned feature class that will have its static cache updated."
                },
                "bin_type": {
                        "type": "string",
                        "description": "Specifies the type of feature binning visualization that will be enabled.FLAT_HEXAGON\u2014The flat hexagon binning scheme, also known as flat geohex or flat hexbinning, will be enabled. The tiles are a te...",
                        "default": None
                },
                "max_lod": {
                        "type": "string",
                        "description": "Specifies the maximum level of detail that will be used for the cache.Tiling schemes are a continuum of scale ranges. Depending on the map, you may want to forego caching of some of the extremely larg...",
                        "default": None
                },
                "add_cache_statisticsfield_statistic_type": {
                        "type": "string",
                        "description": "Specifies the statistics that will be summarized and stored in the bin cache. Statistics are used to symbolize bins and provide aggregate information for all the features in a bin.\r\nOne summary statis...",
                        "default": None
                },
                "delete_cache_statistics": {
                        "type": "string",
                        "description": "The summary statistic that will be deleted from the cache. You cannot delete the default COUNT summary statistic.",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "append_annotation_feature_classes": {
        "name": "append_annotation_feature_classes",
        "description": "Creates a geodatabase annotation feature class or appends to an existing annotation feature class by combining annotation from multiple input geodatabase annotation feature classes into a single feature class with annotation classes.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The input annotation features that will form an annotation class in the output feature class."
                },
                "output_featureclass": {
                        "type": "string",
                        "description": "A new or existing annotation feature class that will contain an annotation class for each input annotation feature class."
                },
                "reference_scale": {
                        "type": "string",
                        "description": "The reference scale set in the output feature class. Input features created at a different reference scale will be transformed to match this output reference scale."
                },
                "create_single_class": {
                        "type": "string",
                        "description": "Specifies how annotation features will be added to the output feature class.ONE_CLASS_ONLY\u2014All annotation features will be aggregated into one annotation class in the output feature class.CREATE_CLASS...",
                        "default": None
                },
                "require_symbol_from_table": {
                        "type": "string",
                        "description": "Specifies how symbols can be selected for newly created annotation features.REQUIRE_SYMBOL\u2014Only the list of symbols in the symbol collection of the output feature class can be used when creating annot...",
                        "default": None
                },
                "create_annotation_when_feature_added": {
                        "type": "string",
                        "description": "Specifies whether feature-linked annotation will be created when a feature is added.AUTO_CREATE\u2014Feature-linked annotation will be created using the label engine when a linked feature is added. The is ...",
                        "default": None
                },
                "update_annotation_when_feature_modified": {
                        "type": "string",
                        "description": "Specifies whether feature-linked annotation will be updated when a linked feature changes.AUTO_UPDATE\u2014Feature-linked annotation will be updated using the label engine when a linked feature changes. Th...",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_featureclass",
                "reference_scale"
        ]
},
    "create_feature_class": {
        "name": "create_feature_class",
        "description": "Creates an empty feature class in a geodatabase or a shapefile in a folder.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The enterprise or file geodatabase or the folder in which the output feature class will be created. This workspace must already exist."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the feature class to be created."
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type of the output feature class.POINT\u2014The geometry type will be point. MULTIPOINT\u2014The geometry type will be multipoint. POLYGON\u2014The geometry type will be polygon. POLYLINE\u2014The ...",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "An existing  dataset or a list of datasets used as templates to define the attribute fields of the new feature class.",
                        "default": None
                },
                "has_m": {
                        "type": "string",
                        "description": "Specifies whether the feature class will have  linear measurement values (m-values).DISABLED\u2014The output feature class will not have m-values. This is the default.ENABLED\u2014The output feature class will ...",
                        "default": None
                },
                "has_z": {
                        "type": "string",
                        "description": "Specifies whether the feature class will have  elevation values (z-values).DISABLED\u2014The output feature class will not have z-values. This is the default.ENABLED\u2014The output feature class will have z-va...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature dataset. You can specify the spatial reference in the following ways: Enter the path to a .prj file, such as C:/workspace/watershed.prj. Reference a feature...",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The configuration keyword applies to enterprise geodatabase data only. It determines the storage parameters of the database table.",
                        "default": None
                },
                "spatial_grid_1": {
                        "type": "string",
                        "description": "This parameter is not supported.  Any value provided will be ignored.",
                        "default": None
                },
                "spatial_grid_2": {
                        "type": "string",
                        "description": "This parameter is not supported.  Any value provided will be ignored.",
                        "default": None
                },
                "spatial_grid_3": {
                        "type": "string",
                        "description": "This parameter is not supported.  Any value provided will be ignored.",
                        "default": None
                },
                "out_alias": {
                        "type": "string",
                        "description": "The alternate name for the output feature class that will be created.",
                        "default": None
                },
                "oid_type": {
                        "type": "string",
                        "description": "Specifies whether the output Object ID field will be 32 bit or 64 bit.SAME_AS_TEMPLATE\u2014The output Object ID field type (32 bit or 64 bit) will be the same as the Object ID field of the first template ...",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "create_unregistered_feature_class": {
        "name": "create_unregistered_feature_class",
        "description": "Creates an empty feature class in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The feature class is not registered with the geodatabase.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The enterprise database or enterprise  geodatabase in which the feature class  will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the feature class that will be created."
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type of the feature class. This parameter is only relevant for those geometry types that store dimensionality metadata, such as ST_Geometry in PostgreSQL, PostGIS Geometry, and ...",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "An existing feature class or list of feature classes with fields and attribute schema that will be used to define the fields in the output feature class.",
                        "default": None
                },
                "has_m": {
                        "type": "string",
                        "description": "Specifies whether the feature class will have  linear measurement values (m-values).DISABLED\u2014The output feature class will not have m-values. This is the default.ENABLED\u2014The output feature class will ...",
                        "default": None
                },
                "has_z": {
                        "type": "string",
                        "description": "Specifies whether the feature class will have  elevation values (z-values).DISABLED\u2014The output feature class will not have z-values. This is the default.ENABLED\u2014The output feature class will have z-va...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature dataset. You can specify the spatial reference in the following ways: Enter the path to a .prj file, such as C:/workspace/watershed.prj. Reference a feature...",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Specifies the default storage parameters (configurations) for geodatabases in a relational database management system (RDBMS). This setting is applicable only when using enterprise geodatabase tables....",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "integrate": {
        "name": "integrate",
        "description": "Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect. Integrate performs\r\nthe following processing tasks: Vertices within the x,y tolerance of one another will be assigned the same coordinate location.When a vertex of one feature is within the x,y tolerance of an edge of any other feature, a new vertex will be inserted on the edge.When line segments intersect, a vertex will be inserted at the point of intersection for each feature involved in the intersection. An alternate tool is available for vector data integration. See the Pairwise Integrate documentation for details.",
        "parameters": {
                "in_featuresfeature_layer_long": {
                        "type": "string",
                        "description": "The feature classes that will be integrated. When the distance between features is small in comparison to the tolerance, the vertices or points will be clustered (moved to be coincident).The feature c..."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The distance that determines the range in which feature vertices are made coincident. To minimize undesired movement of vertices, the x,y tolerance should be small. If no value is provided, the x,y to...",
                        "default": None
                }
        },
        "required": [
                "in_featuresfeature_layer_long"
        ]
},
    "recalculate_feature_class_extent": {
        "name": "recalculate_feature_class_extent",
        "description": "Recalculates the xy, z, and m extent properties of a feature class based on the features in the feature class. A feature class has a spatial extent that is based on all the coordinates in the feature class. This spatial extent is used when adding a feature class to a map to recenter and display all the features. Rather than examining every feature in the feature class each time the feature class is added to a map (a potentially long process), a feature class has an extent property containing the last known spatial extent. However, this extent property is not always updated when features in the feature class are edited. This means that the values in the extent property may not contain the actual spatial extent of the features. The Recalculate Feature Class Extent tool reads all the features and updates the extent property. XY, Z, and M extents are not the same as spatial reference domains. The XY, Z, and M domains in a spatial reference define the valid range of coordinate values that can be stored in a feature class. The feature class extents reflect the actual range of coordinate values that exist in the feature class. These extents cannot be larger than the domains.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The shapefile or geodatabase feature class that will be updated."
                },
                "store_extent": {
                        "type": "string",
                        "description": "Specifies whether the extent will be stored for feature classes that are not registered.  This parameter is only supported when the input feature class is an unregistered spatial table in a database o...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "set_feature_class_split_model": {
        "name": "set_feature_class_split_model",
        "description": "Defines the behavior of a split operation on a feature class. Learn more about setting the split model for a feature class",
        "parameters": {
                "in_feature_class": {
                        "type": "string",
                        "description": "The  feature class on which the split model will be set."
                },
                "split_model": {
                        "type": "string",
                        "description": "Specifies the split model that will be applied to the input feature class.\r\nDELETE_INSERT_INSERT\u2014The original feature will be deleted, and both parts of the split feature will be inserted as new featu...",
                        "default": None
                }
        },
        "required": [
                "in_feature_class"
        ]
},
    "add_xy_coordinates": {
        "name": "add_xy_coordinates",
        "description": "Adds the fields POINT_X and POINT_Y to the point input features and calculates their values. The tool also appends the POINT_Z and POINT_M fields if the input features are z- and m-enabled.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point features whose x,y coordinates will be appended as POINT_X and POINT_Y fields."
                }
        },
        "required": [
                "in_features"
        ]
},
    "adjust_3d_z": {
        "name": "adjust_3d_z",
        "description": "Modifies z-values of 3D features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The 3D features with the z-values that will be modified."
                },
                "reverse_sign": {
                        "type": "string",
                        "description": "Specifies whether features will be inverted along the z-axis.REVERSE\u2014The sign of z-values will be inverted causing the feature to flip upside down.NO_REVERSE\u2014The sign of z-values will not be inverted;...",
                        "default": None
                },
                "adjust_value": {
                        "type": "string",
                        "description": "A numeric value or field from the input features that will be used to adjust the z of each vertex in the input features.   A positive value will shift the feature higher, while a negative number will ...",
                        "default": None
                },
                "from_units": {
                        "type": "string",
                        "description": "Specifies the existing units of the z-values. This parameter is used in conjunction with the to_units parameter.  MILLIMETERS\u2014The units will be millimeters.CENTIMETERS\u2014The units will be centimeters.ME...",
                        "default": None
                },
                "to_units": {
                        "type": "string",
                        "description": "Specifies the units that existing z-values will be converted to.\r\n\r\nMILLIMETERS\u2014The units will be millimeters.CENTIMETERS\u2014The units will be centimeters.METERS\u2014The units will be meters.INCHES\u2014The units...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "bearing_distance_to_line": {
        "name": "bearing_distance_to_line",
        "description": "Creates a feature class containing geodetic or planar line features from the values in an x-coordinate field, y-coordinate field, bearing field, and distance field of a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table. It can be a text file, CSV file, Excel file, dBASE table, or geodatabase table."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The output feature class containing geodetic or planar lines."
                },
                "x_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the x-coordinates (or longitudes) of the starting points of lines to be positioned in the output coordinate system specified by the spatial_reference pa..."
                },
                "y_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the y-coordinates (or latitudes) of the starting points of lines to be positioned in the output coordinate system specified by the spatial_reference par..."
                },
                "distance_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the distances from the starting points for creating the output lines."
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used for the distance_field parameter.METERS\u2014The units will be meters.KILOMETERS\u2014The units will be kilometers.MILES\u2014The units will be miles.NAUTICAL_MILES\u2014The units wi...",
                        "default": None
                },
                "bearing_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing bearing angle values for the output line rotation.\r\nThe angles are measured clockwise from north."
                },
                "bearing_units": {
                        "type": "string",
                        "description": "Specifies the units of the bearing_field parameter values. DEGREES\u2014 The units will be decimal degrees. This is the default.MILS\u2014The units will be mils.RADS\u2014The units will be radians.GRADS\u2014The units wi...",
                        "default": None
                },
                "line_type": {
                        "type": "string",
                        "description": "Specifies the type of line that will be constructed.GEODESIC\u2014 A type of geodetic line that most accurately represents the shortest distance between any two points on the surface of the earth will be c...",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "A field in the input table. This field and the values are included in the output and can be used to join the output features with the records in the input table.",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature class. A spatial reference can be specified as any of the following: \r\n The path to a .prj file, such as C:/workspace/watershed.prj The path to a feature cl...",
                        "default": None
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies whether the remaining input fields will be added to the output feature class.NO_ATTRIBUTES\u2014The remaining input fields will not be added to the output feature class. This is the default.ATTRI...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_featureclass",
                "x_field",
                "y_field",
                "distance_field",
                "bearing_field"
        ]
},
    "calculate_geometry_attributes": {
        "name": "calculate_geometry_attributes",
        "description": "Adds information to a feature's attribute fields representing the spatial or geometric characteristics and location of each feature, such as length or area and x-, y-, z-coordinates, and m-values.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features with a field that will be updated with geometry calculations."
                },
                "geometry_propertyfield_property": {
                        "type": "string",
                        "description": "The fields in which the specified geometry properties will be calculated. You can select an existing field or provide a new field name. If a new field name is provided, the field type is determined by..."
                },
                "length_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used to calculate length.\r\nKILOMETERS\u2014The length unit will be kilometers.METERS\u2014The length unit will be meters.MILES_INT\u2014The length unit will be statute miles.NAUTICAL_...",
                        "default": None
                },
                "area_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used to calculate area.\r\nSQUARE_KILOMETERS\u2014The area unit will be square kilometers.HECTARES\u2014The area unit will be hectares.SQUARE_METERS\u2014The area unit will be square me...",
                        "default": None
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system in which the coordinates, length, and area will be calculated. The coordinate system of the input features is used by default.",
                        "default": None
                },
                "coordinate_format": {
                        "type": "string",
                        "description": "Specifies the coordinate format in which the x- and y-coordinates will be calculated. The coordinate format matching the input features' spatial reference units is used by default. \r\nSeveral coordinat...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "geometry_propertyfield_property"
        ]
},
    "check_geometry": {
        "name": "check_geometry",
        "description": "Generates a report of geometry problems in a feature class. For additional information regarding geometry problems, their impact on the software, and potential sources, see Tools for checking and repairing geometries.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class or layer that will be processed.License:A Desktop Basic license only allows shapefiles and feature classes stored in a file geodatabase, GeoPackage, or SpatiaLite database as valid i..."
                },
                "out_table": {
                        "type": "string",
                        "description": "The report (as a table) of the problems discovered.",
                        "default": None
                },
                "validation_method": {
                        "type": "string",
                        "description": "Specifies the geometry validation method that will be used to identify geometry problems.ESRI\u2014The Esri geometry validation method will be used. This is the default.OGC\u2014The   OGC geometry validation me...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "copy_features": {
        "name": "copy_features",
        "description": "Copies features from the input feature class or layer to a new feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features to be copied."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class which will be created and to which the features will be copied."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Geodatabase configuration keyword to be applied if the output is a geodatabase.",
                        "default": None
                },
                "spatial_grid_1": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                },
                "spatial_grid_2": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                },
                "spatial_grid_3": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "delete_features": {
        "name": "delete_features",
        "description": "Deletes all or the selected subset of features from the input. The deletion of all features or a subset of features depends on the following:If the input is a feature class, all features will be deleted.\r\nIf the input is a layer with no selection, all features will be deleted.\r\nIf the input is a layer with a selection, only the\r\nselected features will be deleted.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class, shapefile, or layer containing features to be deleted."
                }
        },
        "required": [
                "in_features"
        ]
},
    "dice": {
        "name": "dice",
        "description": "Subdivides a feature into smaller features based on a specified vertex limit. This tool is intended as a way to subdivide extremely large features that cause issues with drawing, analysis, editing, and/or performance but are difficult to split up with standard editing and geoprocessing tools. This tool should not be used in any cases other than those where tools are failing to complete successfully due to the size of features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or feature layer. The geometry type must be multipoint, line, or polygon."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class of diced features."
                },
                "vertex_limit": {
                        "type": "string",
                        "description": "Features with geometries that exceed this vertex limit will be subdivided before being written to the output feature class."
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "vertex_limit"
        ]
},
    "feature_envelope_to_polygon": {
        "name": "feature_envelope_to_polygon",
        "description": "Creates a feature class containing polygons, each of which represents the envelope of an input feature.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that can be multipoint, line, polygon, or annotation."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class."
                },
                "single_envelope": {
                        "type": "string",
                        "description": "Specifies whether to use one envelope for each entire multipart feature or one envelope per part of a multipart feature. This parameter will affect the results of multipart input features only.SINGLEP...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "feature_to_line": {
        "name": "feature_to_line",
        "description": "Creates a feature class containing lines generated by converting polygon boundaries to lines, or splitting line, polygon, or both features at their intersections.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that can be line or polygon, or both."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output line feature class."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates, and the distance a coordinate can move in X, Y, or both during spatial computation. The default XY tolerance is set to 0.001 meter or its equiv...",
                        "default": None
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies whether to preserve or omit the input attributes in the output feature class.ATTRIBUTES\u2014Preserves the input attributes in the output features. This is the default.NO_ATTRIBUTES\u2014Omits the inp...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "feature_to_point": {
        "name": "feature_to_point",
        "description": "Creates a feature class containing points generated from the centroids of the input features or placed within the input features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features, which can be multipoint, line,  polygon, or annotation."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output point feature class."
                },
                "point_location": {
                        "type": "string",
                        "description": "Specifies whether an output point will be located within the input feature or at the centroid of the input feature.CENTROID\u2014The output point will be located at the centroid of the input feature. The o...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "feature_to_polygon": {
        "name": "feature_to_polygon",
        "description": "Creates a feature class containing polygons generated from areas enclosed by input line or polygon features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features, which can be line, polygon, or both."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates, and the distance a coordinate can move in X, Y, or both during spatial computation. The default XY tolerance is set to 0.001 meter or its equiv...",
                        "default": None
                },
                "attributes": {
                        "type": "string",
                        "description": "Note:This parameter is no longer supported. The parameter remains for backward compatibility of scripts and models. See the Usage section for more information.",
                        "default": None
                },
                "label_features": {
                        "type": "string",
                        "description": "The optional input point features that contain the attributes to be transferred to the output polygon features.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "feature_vertices_to_points": {
        "name": "feature_vertices_to_points",
        "description": "Creates a feature class containing points generated from specified vertices or locations of the input features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that can be line or polygon."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output point feature class."
                },
                "point_location": {
                        "type": "string",
                        "description": "Specifies where an output point will be created.ALL\u2014A point will be created at each input feature vertex. This is the default. MID\u2014A point will be created at the midpoint, not necessarily a vertex, of...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "geodetic_densify": {
        "name": "geodetic_densify",
        "description": "Creates new features by replacing the segments of the input features with densified approximations of geodesic segments. The following types of geodesic segments can be constructed: geodesic, great elliptic, loxodrome, and normal section.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input line or polygon features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the densified geodesic features."
                },
                "geodetic_type": {
                        "type": "string",
                        "description": "Specifies the type of geodetic segments that will be created.  Geodetic calculations are performed on the ellipsoid associated with the input data's coordinate system.GEODESIC\u2014The segments will be the..."
                },
                "distance": {
                        "type": "string",
                        "description": "The distance between vertices along the output geodesic segment.  The default value is 50 kilometers.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "geodetic_type"
        ]
},
    "minimum_bounding_geometry": {
        "name": "minimum_bounding_geometry",
        "description": "Creates a feature class containing polygons which represent a specified minimum bounding geometry enclosing each input feature or each group of input features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that can be point, multipoint, line, polygon, or multipatch."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class."
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies what type of minimum bounding geometry the output polygons will represent.RECTANGLE_BY_AREA\u2014The rectangle of the smallest area enclosing an input feature. This is the default.RECTANGLE_BY_WI...",
                        "default": None
                },
                "group_option": {
                        "type": "string",
                        "description": "Specifies how the input features will be grouped; each group will be enclosed with one output polygon.NONE\u2014Input features will not be grouped. This is the default. This option is not available for poi...",
                        "default": None
                },
                "group_field": {
                        "type": "string",
                        "description": "The field or fields in the input features that will be used to group features, when LIST is specified as group_option. At least one group field is required for LIST option. All features that have the ...",
                        "default": None
                },
                "mbg_fields_option": {
                        "type": "string",
                        "description": "Specifies whether to add the geometric attributes in the output feature class or omit them in the output feature class.NO_MBG_FIELDS\u2014Omits any input attributes in the output feature class. This is the...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "multipart_to_singlepart": {
        "name": "multipart_to_singlepart",
        "description": "Creates a feature class of singlepart features by separating multipart input features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that can be any feature type."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing features that vary by input feature type."
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "points_to_line": {
        "name": "points_to_line",
        "description": "Creates line features from points.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The point features that will be used to construct lines."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The line feature class that will be created from the input points."
                },
                "line_field": {
                        "type": "string",
                        "description": "The field that will be used to identify unique attribute values so line features can be constructed using points of the same values.If no field is specified, lines will be constructed without using un...",
                        "default": None
                },
                "sort_field": {
                        "type": "string",
                        "description": "The field that will be used to sort the order of the points.If no field is specified, points used to create output line features will be sorted in the order they are found. This is the default.",
                        "default": None
                },
                "close_line": {
                        "type": "string",
                        "description": "Specifies whether the output line features will be closed.CLOSE\u2014For a\r\ncontinuous line, an extra segment connecting the last point with\r\nthe first point will be included to form a closed line. For\r\ntw...",
                        "default": None
                },
                "line_construction_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to construct the line\r\nfeatures.\r\nCONTINUOUS\u2014Line features will be created by connecting points continuously. This is the default.TWO_POINT\u2014Line features will be...",
                        "default": None
                },
                "attribute_source": {
                        "type": "string",
                        "description": "Specifies how the specified attributes will be\r\ntransferred.\r\nNONE\u2014No attributes will be transferred. This is the default.BOTH_ENDS\u2014The attributes from the start and end points of the line will be tra...",
                        "default": None
                },
                "transfer_fields": {
                        "type": "string",
                        "description": "The fields containing values that will be transferred from the source points to the output lines. If no fields are selected, no attributes will be transferred.If the Attribute_Source parameter value i...",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_feature_class"
        ]
},
    "polygon_to_line": {
        "name": "polygon_to_line",
        "description": "Creates a line feature class converted from polygon boundaries. You can set the tool parameters so shared segments and their neighboring polygon feature IDs will be analyzed. Alternatively, you can set the tool parameters so an enclosed line feature will be created for each input polygon.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygon features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output line feature class."
                },
                "neighbor_option": {
                        "type": "string",
                        "description": "Specifies whether polygon neighboring relationships will be identified and stored in the output.IDENTIFY_NEIGHBORS\u2014Polygon neighboring relationships will be identified and stored in the output. If dif...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "repair_geometry": {
        "name": "repair_geometry",
        "description": "Inspects features for geometry problems and repairs them. If a problem is found, a repair will be performed, and a one-line description will identify the feature, as well as the geometry problem that was repaired. This tool uses the same logic as the Check Geometry tool to repair geometry problems. Learn more about checking and repairing geometries",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class or layer that will be processed.License:A Desktop Basic license only allows shapefiles and feature classes stored in a file geodatabase, GeoPackage, or SpatiaLite database as valid i..."
                },
                "delete_None": {
                        "type": "string",
                        "description": "Specifies whether features with None geometries will be deleted.DELETE_NULL\u2014 Features with None geometry will be deleted from the input. This is the default.KEEP_NULL\u2014 Features with None geometry will...",
                        "default": None
                },
                "validation_method": {
                        "type": "string",
                        "description": "Specifies the geometry validation method that will be used to identify geometry problems.ESRI\u2014The Esri geometry validation method will be used. This is the default.OGC\u2014The   OGC geometry validation me...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "split_line_at_point": {
        "name": "split_line_at_point",
        "description": "Splits line features based on intersection or proximity to point features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input line features that will be split."
                },
                "point_features": {
                        "type": "string",
                        "description": "The input point features whose locations will be used to split the input lines."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain the split lines."
                },
                "search_radius": {
                        "type": "string",
                        "description": "The distance that will be used to split lines by their proximity to point features. Points within the search distance to an input line will be used to split those lines at the nearest location to the ...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "point_features",
                "out_feature_class"
        ]
},
    "split_line_at_vertices": {
        "name": "split_line_at_vertices",
        "description": "Creates a polyline feature class by splitting input lines or polygons at their vertices.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input line or polygon features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output line feature class."
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "subdivide_polygon": {
        "name": "subdivide_polygon",
        "description": "Divides polygon features into a number of equal areas or parts.",
        "parameters": {
                "in_polygons": {
                        "type": "string",
                        "description": "The polygon features to be subdivided."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class of subdivided polygons."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to divide the polygons.NUMBER_OF_EQUAL_PARTS\u2014 Polygons will be divided evenly into a number of parts. This is the default.EQUAL_AREAS\u2014Polygons will be divided in..."
                },
                "num_areas": {
                        "type": "string",
                        "description": "The number of areas into which the polygon will be divided if the NUMBER_OF_EQUAL_PARTS subdivision method is specified.",
                        "default": None
                },
                "target_area": {
                        "type": "string",
                        "description": "The area of the equal parts\r\nif the EQUAL_AREAS subdivision method is specified.\r\nIf the target_area is larger than the area of the input polygon, the polygon will not be subdivided.",
                        "default": None
                },
                "target_width": {
                        "type": "string",
                        "description": "This parameter is not yet supported.",
                        "default": None
                },
                "split_angle": {
                        "type": "string",
                        "description": "The angle that will be used to draw the lines that divide the polygon.\r\nThe default is 0.",
                        "default": None
                },
                "subdivision_type": {
                        "type": "string",
                        "description": "Specifies how the polygons will be divided.STRIPS\u2014 Polygons will be divided into strips. This is the default.STACKED_BLOCKS\u2014Polygons will be divided into stacked blocks.",
                        "default": None
                }
        },
        "required": [
                "in_polygons",
                "out_feature_class",
                "method"
        ]
},
    "table_to_ellipse": {
        "name": "table_to_ellipse",
        "description": "Creates a feature class containing geodetic or planar ellipses from the values in an x-coordinate field, y-coordinate field, major axis and minor axis fields, and azimuth field of a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table. It can be a text file, CSV file, Excel file, dBASE table, or geodatabase table."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The output feature class that will contain geodetic or planar ellipses."
                },
                "x_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the x-coordinates (or longitudes) of the center points of ellipses to be positioned in the output coordinate system specified by the spatial_reference p..."
                },
                "y_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the y-coordinates (or latitudes) of the center points of ellipses to be positioned in the output coordinate system specified by the spatial_reference pa..."
                },
                "major_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing major axis lengths of the ellipses."
                },
                "minor_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing minor axis lengths of the ellipses."
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used for the major_field and minor_field parameters. METERS\u2014The units will be meters.KILOMETERS\u2014The units will be kilometers.MILES\u2014The units will be miles.NAUTICAL_MIL..."
                },
                "azimuth_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing azimuth angle values for the major axis rotations of the output ellipses.\r\nThe values are measured clockwise from north.",
                        "default": None
                },
                "azimuth_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used for the azimuth_field parameter.DEGREES\u2014 The units will be decimal degrees. This is the default.MILS\u2014The units will be mils.RADS\u2014The units will be radians.GRADS\u2014T...",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "A field in the input table. This field and the values are included in the output and can be used to join the output features with the records in the input table.",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature class. A spatial reference can be specified as any of the following: \r\n The path to a .prj file, such as C:/workspace/watershed.prj The path to a feature cl...",
                        "default": None
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies whether the remaining input fields will be added to the output feature class.NO_ATTRIBUTES\u2014The remaining input fields will not be added to the output feature class. This is the default.ATTRI...",
                        "default": None
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type for the output feature class.LINE\u2014An output polyline feature class will be created. This is the default.POLYGON\u2014An output polygon feature class will be created.",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether  the ellipse will be generated based on geodesic or planar measurements.GEODESIC\u2014A geodesic ellipse will be generated. The ellipse will accurately represent the shape on the surface ...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_featureclass",
                "x_field",
                "y_field",
                "major_field",
                "minor_field",
                "distance_units"
        ]
},
    "unsplit_line": {
        "name": "unsplit_line",
        "description": "Aggregates line features that have coincident endpoints and, optionally, common attribute values.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The line features to be aggregated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class to be created that will contain the aggregated features."
                },
                "dissolve_field": {
                        "type": "string",
                        "description": "The field or fields on which features will be aggregated. If no fields are specified, the tool will dissolve all features together.",
                        "default": None
                },
                "statistics_fieldsfield_statistic_type": {
                        "type": "string",
                        "description": "Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are exclud...",
                        "default": None
                },
                "concatenation_separator": {
                        "type": "string",
                        "description": "A character or characters that will be used to concatenate values when the CONCATENATION option is used for the statistics_fields parameter. By default, the tool will concatenate values without a sepa...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "xy_table_to_point": {
        "name": "xy_table_to_point",
        "description": "Creates a point feature class based on x-, y-, and z-coordinates from a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the x- and y-coordinates that define the locations of the point features that will be created."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the output point features."
                },
                "x_field": {
                        "type": "string",
                        "description": "The field in the input table that contains the x-coordinates (longitude)."
                },
                "y_field": {
                        "type": "string",
                        "description": "The field in the input table that contains the y-coordinates (latitude)."
                },
                "z_field": {
                        "type": "string",
                        "description": "The field in the input table that contains the z-coordinates.",
                        "default": None
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system of the x- and y-coordinates. This will be the coordinate system of the output feature class.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_feature_class",
                "x_field",
                "y_field"
        ]
},
    "xy_to_line": {
        "name": "xy_to_line",
        "description": "Creates a feature class containing geodetic or planar line features from the values in a start x-coordinate field, start y-coordinate field, end x-coordinate field, and end y-coordinate field of a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table. It can be a text file, CSV file, Excel file, dBASE table, or geodatabase table."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The output feature class containing geodetic or planar lines."
                },
                "startx_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the x-coordinates (or longitudes) of the starting points of lines to be positioned in the output coordinate system specified by the spatial_reference pa..."
                },
                "starty_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the y-coordinates (or latitudes) of the starting points of lines to be positioned in the output coordinate system specified by the spatial_reference par..."
                },
                "endx_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the x-coordinates (or longitudes) of the ending points of lines to be positioned in the output coordinate system specified by the spatial_reference para..."
                },
                "endy_field": {
                        "type": "string",
                        "description": "A numerical field in the input table containing the y-coordinates (or latitudes) of the ending points of lines to be positioned in the output coordinate system specified by the spatial_reference param..."
                },
                "line_type": {
                        "type": "string",
                        "description": "Specifies the type of line that will be constructed.GEODESIC\u2014 A type of geodetic line that most accurately represents the shortest distance between any two points on the surface of the earth will be c...",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "A field in the input table. This field and the values are included in the output and can be used to join the output features with the records in the input table.",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature class. A spatial reference can be specified as any of the following: \r\n The path to a .prj file, such as C:/workspace/watershed.prj The path to a feature cl...",
                        "default": None
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies whether the remaining input fields will be added to the output feature class.NO_ATTRIBUTES\u2014The remaining input fields will not be added to the output feature class. This is the default.ATTRI...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_featureclass",
                "startx_field",
                "starty_field",
                "endx_field",
                "endy_field"
        ]
},
    "add_field": {
        "name": "add_field",
        "description": "Adds a new field to a table or the table of a feature class or feature layer, as well as to rasters with attribute tables.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table where the specified field will be added. The field will be added to the existing input table and will not create a new output table.Fields can be added to feature classes in geodatabas..."
                },
                "field_name": {
                        "type": "string",
                        "description": "The name of the field that will be added to the input table."
                },
                "field_type": {
                        "type": "string",
                        "description": "Specifies the field type of the new field.SHORT\u2014The field type will be short. Short fields support whole numbers between -32,768 and 32,767.LONG\u2014The field type will be long. Long fields support whole ..."
                },
                "field_precision": {
                        "type": "string",
                        "description": "The number of digits that can be stored in the field. All digits are counted regardless of which side of the decimal they are on.This parameter is only applicable to numeric field types.If the input t...",
                        "default": None
                },
                "field_scale": {
                        "type": "string",
                        "description": "The number of decimal places stored in a field.This parameter is only applicable to fields of type float or double.If the input table is in a file geodatabase, the field scale value will be ignored.",
                        "default": None
                },
                "field_length": {
                        "type": "string",
                        "description": "The length of the field. This sets the maximum number of allowable characters for each record of the field. If no field length is provided, a length of 255 will be used.This parameter is only applicab...",
                        "default": None
                },
                "field_alias": {
                        "type": "string",
                        "description": "The alternate name for the field. This name is used to describe cryptic field names. This parameter only applies to geodatabases.",
                        "default": None
                },
                "field_is_Noneable": {
                        "type": "string",
                        "description": "Specifies whether the field can contain None values. Null values are different from zero or empty fields and are only supported for fields in a geodatabase.NULLABLE\u2014The field can contain None values. ...",
                        "default": None
                },
                "field_is_required": {
                        "type": "string",
                        "description": "Specifies whether the field being created is a required field for the table. Required fields are only supported in a geodatabase.NON_REQUIRED\u2014The field is not a required field. This is the default. RE...",
                        "default": None
                },
                "field_domain": {
                        "type": "string",
                        "description": "Constrains the values allowed in any particular attribute for a table, feature class, or subtype in a geodatabase. You must specify the name of an existing domain for it to be applied to the field.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field_name",
                "field_type"
        ]
},
    "add_fields_(multiple)": {
        "name": "add_fields_(multiple)",
        "description": "Adds new fields to a table, feature class, or raster.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table where the fields will be added.  The fields will be added to the existing input table and will not create a new output table. Fields can be added to feature classes in geodatabases, sh..."
                },
                "template": {
                        "type": "string",
                        "description": "The feature classes or tables that will be used as a template to define the attribute fields to add.\r\n Fields from the inputs specified by this parameter will be added to the in_table value in additio...",
                        "default": None
                }
        },
        "required": [
                "in_table"
        ]
},
    "alter_field": {
        "name": "alter_field",
        "description": "Renames fields and field aliases or alters field properties.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input geodatabase table or feature class that contains the field that will be altered."
                },
                "field": {
                        "type": "string",
                        "description": "The name of the field that will be altered. If the field is a required field, only the field alias will be altered."
                },
                "new_field_name": {
                        "type": "string",
                        "description": "The new name for the field.",
                        "default": None
                },
                "new_field_alias": {
                        "type": "string",
                        "description": "The new  field alias for the field.",
                        "default": None
                },
                "field_type": {
                        "type": "string",
                        "description": "Specifies the new  field type for the field.\r\nThis parameter is only applicable if the input table is empty (does not contain records).SHORT\u2014The field type will be short. Short fields support whole nu...",
                        "default": None
                },
                "field_length": {
                        "type": "string",
                        "description": "The new length of the field. This sets the maximum number of allowable characters for each record of the field. This parameter is only applicable to fields of type TEXT or BLOB. If the table is empty,...",
                        "default": None
                },
                "field_is_Noneable": {
                        "type": "string",
                        "description": "Specifies whether the field can contain None values.  Null values are only supported for fields in a geodatabase. This parameter is only applicable if the input table is empty (does not contain record...",
                        "default": None
                },
                "clear_field_alias": {
                        "type": "string",
                        "description": "Specifies whether the alias for the input field will be cleared. The new_field_alias parameter must be empty to clear the alias of the field.CLEAR_ALIAS\u2014The field alias will be cleared (set to None).D...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field"
        ]
},
    "alter_fields": {
        "name": "alter_fields",
        "description": "Alters the field properties of multiple fields in a feature class or table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input geodatabase table or feature class that contains the field that will be altered."
                }
        },
        "required": [
                "in_table"
        ]
},
    "assign_default_to_field": {
        "name": "assign_default_to_field",
        "description": "Creates a default value for a specified field.  When a new row is added to the table or feature class, the specified field will be set to this default value.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table or feature class that will have a default value added to one of its fields."
                },
                "field_name": {
                        "type": "string",
                        "description": "The field to which the default value will be added each time a new row is added to the table or feature class."
                },
                "default_value": {
                        "type": "string",
                        "description": "The default value to be added to each new table or feature class. The value entered must match the data type of the field.",
                        "default": None
                },
                "subtype_code": {
                        "type": "string",
                        "description": "The subtypes that can participate in the default value.",
                        "default": None
                },
                "clear_value": {
                        "type": "string",
                        "description": "Specifies whether the default value for either the field or the subtype will be cleared. To clear the default value, the default_value parameter must be passed in as an empty string. To clear the defa...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field_name"
        ]
},
    "batch_update_fields": {
        "name": "batch_update_fields",
        "description": "Transforms fields in a table or feature class based on schema defined in the definition table and creates a new table or feature class. You can do the following using this tool: Add new fields.Update existing fields.Reorder fields.Change field types.Change field properties.Assign or update field aliases.Calculate field values based on existing fields using Python.Remove fields.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table or feature class."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table or feature class containing the updated fields."
                },
                "field_definition_table": {
                        "type": "string",
                        "description": "A\r\ntable containing the field definitions and calculations that will be used to create the output."
                },
                "script_file": {
                        "type": "string",
                        "description": "A Python file that stores multiline Python functions to perform calculations for the out_table parameter fields.",
                        "default": None
                },
                "output_field_name": {
                        "type": "string",
                        "description": "The field name from the definition table that contains the target field names for the output table.",
                        "default": None
                },
                "source_field_name": {
                        "type": "string",
                        "description": "The field name from the definition table that contains the source field names from the input table.",
                        "default": None
                },
                "output_field_type": {
                        "type": "string",
                        "description": "The field in the Output Schema Definition Table parameter value that defines the data types for the output table. The field is expected to be of Text type. The field in the field_definition_table para...",
                        "default": None
                },
                "output_field_decimals_or_length": {
                        "type": "string",
                        "description": "The field name from the  definition table that defines the number of decimals or the length of the field for the output fields.",
                        "default": None
                },
                "output_field_alias": {
                        "type": "string",
                        "description": "The field name from the  definition table that defines the alias names for the fields of the output table.",
                        "default": None
                },
                "output_field_script": {
                        "type": "string",
                        "description": "The field name from the definition table that defines the calculations for the output fields.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_table",
                "field_definition_table"
        ]
},
    "calculate_field": {
        "name": "calculate_field",
        "description": "Calculates the values of a field for a feature class, feature layer, or raster.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the field that will be updated with the new calculation."
                },
                "field": {
                        "type": "string",
                        "description": "The field that will be updated with the new calculation.If a field with the specified name does not exist in the input table, it will be added."
                },
                "expression": {
                        "type": "string",
                        "description": "The simple calculation expression used to create a value that will populate the selected rows."
                },
                "expression_type": {
                        "type": "string",
                        "description": "Specifies the type of expression that will be used.PYTHON3\u2014The Python expression type will be used.ARCADE\u2014The Arcade expression type will be used.SQL\u2014The SQL expression type will be used.VB\u2014The VBScri...",
                        "default": None
                },
                "code_block": {
                        "type": "string",
                        "description": "A block of code that will be used for complex Python or VBScript expressions.",
                        "default": None
                },
                "field_type": {
                        "type": "string",
                        "description": "Specifies the field type of the new field. This parameter is only used when the field name does not exist in the input table.If\r\nthe field is of type text, the field will have a length of 512,\r\nunless...",
                        "default": None
                },
                "enforce_domains": {
                        "type": "string",
                        "description": "Specifies whether field domain rules will be enforced.ENFORCE_DOMAINS\u2014Field domain rules will be enforced.NO_ENFORCE_DOMAINS\u2014Field domain rules will not be enforced. This is the default.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field",
                "expression"
        ]
},
    "calculate_fields_(multiple)": {
        "name": "calculate_fields_(multiple)",
        "description": "Calculates the values of two or more fields for a feature class, feature layer, or raster.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the fields that will be updated with the new calculations."
                },
                "expression_type": {
                        "type": "string",
                        "description": "Specifies the type of expression that will be used.PYTHON3\u2014The Python expression type will be used.ARCADE\u2014The Arcade expression type will be used.SQL\u2014The SQL expression type will be used.VB\u2014The VBScri..."
                },
                "code_block": {
                        "type": "string",
                        "description": "A block of code that will be used for complex expressions. A function cannot be used to return multiple values.",
                        "default": None
                },
                "enforce_domains": {
                        "type": "string",
                        "description": "Specifies whether field domain rules will be enforced.ENFORCE_DOMAINS\u2014Field domain rules will be enforced.NO_ENFORCE_DOMAINS\u2014Field domain rules will not be enforced. This is the default.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "expression_type"
        ]
},
    "delete_field": {
        "name": "delete_field",
        "description": "Deletes one or more fields from a table, feature class, feature layer, or raster dataset.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the fields to be deleted. The existing input table will be modified."
                },
                "drop_field": {
                        "type": "string",
                        "description": "The fields to be dropped or kept from the input table, as specified by the method parameter. Only nonrequired fields can be deleted."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the fields specified by the drop_field parameter will be deleted or kept.DELETE_FIELDS\u2014The fields specified by the drop_field parameter will be deleted. This is the default.KEEP_FIEL...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "drop_field"
        ]
},
    "migrate_text_field": {
        "name": "migrate_text_field",
        "description": "Migrates text fields in an  Oracle table from Unicode to non-Unicode types.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The Oracle dataset from which eligible text fields will be migrated."
                },
                "fields": {
                        "type": "string",
                        "description": "The Unicode text fields that will be migrated to non-Unicode text fields."
                }
        },
        "required": [
                "in_table",
                "fields"
        ]
},
    "compact": {
        "name": "compact",
        "description": "Compacts a file or mobile geodatabase, SQLite database, or Open Geospatial Consortium (OGC) GeoPackage file. Compacting rearranges data storage, often reducing the file's size and improving performance.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The file or mobile geodatabase, SQLite database, or GeoPackage that will be compacted."
                }
        },
        "required": [
                "in_workspace"
        ]
},
    "compress_file_geodatabase_data": {
        "name": "compress_file_geodatabase_data",
        "description": "Compresses all the contents in a geodatabase, all the contents in a feature dataset, or an individual stand-alone feature class or table.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The geodatabase, feature dataset, feature class, or table that will be compressed."
                },
                "lossless": {
                        "type": "string",
                        "description": "Specifies whether lossless compression will be used.Lossless compression\u2014Lossless compression will be used. This is the default.Non-lossless compression\u2014Lossless compression will not be used.This para..."
                }
        },
        "required": [
                "in_data",
                "lossless"
        ]
},
    "generate_file_geodatabase_license": {
        "name": "generate_file_geodatabase_license",
        "description": "Generates a license file (.sdlic) for displaying the contents in a licensed file geodatabase created by the Generate Licensed File Geodatabase tool. Note:Licensing is not supported for geodatabases created earlier than version 10.1.",
        "parameters": {
                "in_lic_def_file": {
                        "type": "string",
                        "description": "The license definition file (.licdef) created by the Generate Licensed File Geodatabase tool."
                },
                "out_lic_file": {
                        "type": "string",
                        "description": "The license file (.sdlic) for distribution."
                },
                "allow_export": {
                        "type": "string",
                        "description": "Specifies whether the export of  vector data will be  allowed.DENY_EXPORT\u2014Vector data cannot be exported with the data license file (.sdlic) installed. This is the default.ALLOW_EXPORT\u2014 Vector data ca...",
                        "default": None
                },
                "exp_date": {
                        "type": "string",
                        "description": "The expiration date  of the data license file,   after which  the file geodatabase\u2019s contents can no longer be displayed.  The default value is empty (blank), which means the data license file will ne...",
                        "default": None
                }
        },
        "required": [
                "in_lic_def_file",
                "out_lic_file"
        ]
},
    "generate_licensed_file_geodatabase": {
        "name": "generate_licensed_file_geodatabase",
        "description": "Generates a license definition file (.licdef) that defines and restricts the display of contents in a file geodatabase.  The contents of the licensed file geodatabase can be viewed by creating  a license file (*.sdlic) and configuring the ArcGIS clients to recognize it.  The license file is created using the Generate File Geodatabase License tool. Licensing is not supported for geodatabases created earlier than version 10.1.",
        "parameters": {
                "in_fgdb": {
                        "type": "string",
                        "description": "The unlicensed file geodatabase that will be licensed."
                },
                "out_fgdb": {
                        "type": "string",
                        "description": "The name and location of the generated licensed file geodatabase."
                },
                "out_lic_def": {
                        "type": "string",
                        "description": "The license definition file."
                }
        },
        "required": [
                "in_fgdb",
                "out_fgdb",
                "out_lic_def"
        ]
},
    "recover_file_geodatabase": {
        "name": "recover_file_geodatabase",
        "description": "Recovers data from a file geodatabase that has become corrupt. Learn more about how Recover File Geodatabase works",
        "parameters": {
                "input_file_gdb": {
                        "type": "string",
                        "description": "Input corrupt file geodatabase."
                },
                "output_location": {
                        "type": "string",
                        "description": "Output folder location for the recovered \r\nfile geodatabase."
                }
        },
        "required": [
                "input_file_gdb",
                "output_location"
        ]
},
    "uncompress_file_geodatabase_data": {
        "name": "uncompress_file_geodatabase_data",
        "description": "Uncompresses all the contents in a geodatabase, all the contents in a feature dataset, or an individual stand-alone feature class or table.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The geodatabase, feature dataset, feature class, or table to uncompress."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The configuration keyword defining how the data will store once uncompressed",
                        "default": None
                }
        },
        "required": [
                "in_data"
        ]
},
    "create_file_geodatabase": {
        "name": "create_file_geodatabase",
        "description": "Creates a file geodatabase in a folder.",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The folder where the file geodatabase will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the file geodatabase to be created."
                },
                "out_version": {
                        "type": "string",
                        "description": "Specifies the ArcGIS version for the new geodatabase.CURRENT\u2014A geodatabase compatible with the currently installed version of ArcGIS will be created. This is the default.10.0\u2014A geodatabase compatible ...",
                        "default": None
                }
        },
        "required": [
                "out_folder_path",
                "out_name"
        ]
},
    "append": {
        "name": "append",
        "description": "Appends to, or optionally updates, an existing target dataset with multiple input datasets. Input datasets can be feature classes, tables, shapefiles, rasters, or annotation or dimension feature classes. To combine input datasets into a new output dataset, use the Merge tool.",
        "parameters": {
                "inputs": {
                        "type": "string",
                        "description": "The input datasets containing the data that will be appended to the target dataset. Input datasets can be point, line, or polygon feature classes, tables, rasters, annotation feature classes, or dimen..."
                },
                "target": {
                        "type": "string",
                        "description": "The existing dataset where the data of the input datasets will be appended."
                },
                "schema_type": {
                        "type": "string",
                        "description": "Specifies whether the fields of the input datasets must match the fields of the target dataset for data to be appended.TEST\u2014Fields of the input datasets must match the fields of the target dataset. An...",
                        "default": None
                },
                "field_mapping": {
                        "type": "string",
                        "description": "The field map parameter controls the transfer or mapping of fields from the input datasets to the target dataset. It can only be used when the schema_type parameter is set to NO_TEST.Because the input...",
                        "default": None
                },
                "subtype": {
                        "type": "string",
                        "description": "The subtype description that will be assigned to all new data that is appended to the target dataset.",
                        "default": None
                },
                "expression": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of the input datasets' records.  If multiple input datasets are specified, they will all be evaluated using the expression. If no records match ...",
                        "default": None
                },
                "match_fieldstarget_field_input_field": {
                        "type": "string",
                        "description": "The fields from the input datasets that will be used to match to the target dataset. If the values of these fields match, records from the input datasets will update the corresponding records of the t...",
                        "default": None
                },
                "update_geometry": {
                        "type": "string",
                        "description": "Specifies whether geometry in the target dataset will be updated with geometry from the input datasets if the match_fields parameter field values match.UPDATE_GEOMETRY\u2014Geometry in the target dataset w...",
                        "default": None
                },
                "enforce_domains": {
                        "type": "string",
                        "description": "Specifies whether field domain rules will be enforced.ENFORCE_DOMAINS\u2014Field domain rules will be enforced.NO_ENFORCE_DOMAINS\u2014Field domain rules will not be enforced. This is the default.",
                        "default": None
                },
                "feature_service_mode": {
                        "type": "string",
                        "description": "Specifies whether performance will be optimized when the target dataset is an ArcGIS Online or ArcGIS Enterprise  feature service. This parameter is only active when the target dataset supports optimi...",
                        "default": None
                }
        },
        "required": [
                "inputs",
                "target"
        ]
},
    "copy": {
        "name": "copy",
        "description": "Copies the input data to an output workspace of the same data type as the input workspace.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The data that will be copied."
                },
                "out_data": {
                        "type": "string",
                        "description": "The location and name of the output data. The file name extension of the output data must match the extension of the input data. For example, if you are copying a file geodatabase, the output data ele..."
                },
                "data_type": {
                        "type": "string",
                        "description": "The type of the data on disk that will be copied. This parameter is only necessary in the event of a name conflict\r\nbetween two different data types. For example, a geodatabase can\r\ncontain\r\na relatio...",
                        "default": None
                },
                "associated_datafrom_name_data_type_to_name_config_keyword": {
                        "type": "string",
                        "description": "When the input has associated data,  this parameter can be used to control the associated output data's name and config keyword.from_name\u2014The data associated with the input data, which will also be co...",
                        "default": None
                }
        },
        "required": [
                "in_data",
                "out_data"
        ]
},
    "create_ai_service_connection_file": {
        "name": "create_ai_service_connection_file",
        "description": "Creates a connection file for hosted AI services in ArcGIS Pro.",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The folder path where the connection file will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the AI service  connection file."
                },
                "service_provider": {
                        "type": "string",
                        "description": "Specifies the cloud service provider that will be used.AWS\u2014The cloud service provider will be Amazon Web Services (AWS). AWS offers a comprehensive suite of\r\ncloud-based machine learning and AI servic...",
                        "default": None
                },
                "connection_parameters": {
                        "type": "string",
                        "description": "The connection parameters that will be added to the output connection file. The keys and values are unique for each service provider.Key\u2014The name of the connection parameter key.Value\u2014The value of the...",
                        "default": None
                },
                "secret_param_key": {
                        "type": "string",
                        "description": "The key whose value contains sensitive information, such as API keys or authentication tokens.",
                        "default": None
                },
                "secret_param_value": {
                        "type": "string",
                        "description": "The secret access key string to authenticate the connection.\r\nCaution:This is sensitive information and should only be shared with trusted service providers. The key provided is stored in the Windows ...",
                        "default": None
                }
        },
        "required": [
                "out_folder_path",
                "out_name"
        ]
},
    "create_database_view": {
        "name": "create_database_view",
        "description": "Creates a view in a database based on an SQL expression.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database that contains the tables or feature classes used to construct the view. This database is also where the view will be created."
                },
                "view_name": {
                        "type": "string",
                        "description": "The name of the view that will be created in the database."
                },
                "view_definition": {
                        "type": "string",
                        "description": "An SQL statement that will be used to construct the view."
                }
        },
        "required": [
                "input_database",
                "view_name",
                "view_definition"
        ]
},
    "delete": {
        "name": "delete",
        "description": "Permanently deletes data. All types of geographic data supported by ArcGIS, as well as toolboxes and workspaces (folders and geodatabases), can be deleted. If the specified item is a workspace, all contained items will also be deleted.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The input data that will be deleted."
                },
                "data_type": {
                        "type": "string",
                        "description": "The type of data on disk to be deleted.This parameter is only necessary in the event of a name conflict\r\nbetween two different data types. For example, a geodatabase can\r\ncontain\r\na relationship class...",
                        "default": None
                }
        },
        "required": [
                "in_data"
        ]
},
    "delete_identical": {
        "name": "delete_identical",
        "description": "Deletes records from a feature class or table that have identical values in a set of fields. If the geometry field is selected, feature geometries are compared. The Find Identical tool can be used to report which records are considered identical without deleting them.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The table or feature class that will have identical records deleted."
                },
                "fields": {
                        "type": "string",
                        "description": "The field or fields whose values will be compared to find identical records."
                },
                "xy_tolerance": {
                        "type": "string",
                        "description": "The x,y tolerance that will be applied to each vertex when evaluating whether there is an identical vertex in another feature.",
                        "default": None
                },
                "z_tolerance": {
                        "type": "string",
                        "description": "The z-tolerance that will be applied to each vertex when evaluating whether there is an identical vertex in another feature.",
                        "default": None
                },
                "out_mapping_table": {
                        "type": "string",
                        "description": "An optional output table that will include the object ID values of all records from the input that have a duplicate, matched with the object ID values of the representative record that was retained.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "fields"
        ]
},
    "delete_multiple": {
        "name": "delete_multiple",
        "description": "Permanently deletes multiple data items of the same or different data types. All types of geographic data supported by ArcGIS, as well as toolboxes and workspaces (folders and geodatabases), can be deleted. If a  specified item is a workspace, all contained items will also be deleted.",
        "parameters": {
                "in_datainput_data_element_data_type": {
                        "type": "string",
                        "description": "The input data that will be deleted.\r\n\r\nThe data type is necessary in the event of a name conflict between data types. For example, a geodatabase can\r\ncontain a feature\r\nclass with an identical name t..."
                }
        },
        "required": [
                "in_datainput_data_element_data_type"
        ]
},
    "disable_last_edit_time": {
        "name": "disable_last_edit_time",
        "description": "Disables the last edit time property on an enterprise geodatabase dataset. Disabling the last edit time property on a dataset will stop the recording of timestamps of when the data was last edited.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The enterprise geodatabase table, feature class, feature dataset, attributed relationship class, or many-to-many relationship class that will have the last edit time property disabled."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "enable_last_edit_time": {
        "name": "enable_last_edit_time",
        "description": "Enables the last edit time property on an enterprise geodatabase dataset. Enabling the last edit time property on a dataset will enable the recording of timestamps of when the data was last edited. This supports a feature service and other clients to request from the geodatabase the timestamp of when the dataset was last edited. Knowing the last edit time is valuable for a feature service as it allows for response caching and other query enhancement.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The enterprise geodatabase table, feature class, feature dataset, attributed relationship class, or many-to-many relationship class that will have the last edit time property enabled."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "extract_data_from_geodatabase": {
        "name": "extract_data_from_geodatabase",
        "description": "Extracts a subset of data from one geodatabase to another geodatabase or an .xml file. Learn more about extracting data from a geodatabase",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The data that will be extracted."
                },
                "extract_type": {
                        "type": "string",
                        "description": "Specifies whether the schema and rows of the data or only the schema will be extracted.\r\nDATA\u2014The schema and rows will be extracted. This is the default.SCHEMA_ONLY\u2014Only the schema will be extracted.",
                        "default": None
                },
                "out_type": {
                        "type": "string",
                        "description": "Specifies the output type the data will be extracted to.\r\nGEODATABASE\u2014The data will be extracted to an existing geodatabase. This is the default.XML_FILE\u2014The data will be extracted to an XML workspace...",
                        "default": None
                },
                "out_geodatabase": {
                        "type": "string",
                        "description": "The geodatabase that will contain the extracted data when the out_type parameter is set to GEODATABASE.",
                        "default": None
                },
                "out_xml": {
                        "type": "string",
                        "description": "The name and location of the .xml file that will be created when the out_type parameter is set to XML_FILE.",
                        "default": None
                },
                "out_folder_path": {
                        "type": "string",
                        "description": "The location of the file or mobile  geodatabase that will be created for the extracted data. This parameter is required when the out_type parameter is set to NEW_FILE_GEODATABASE or NEW_MOBILE_GEODATA...",
                        "default": None
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the file  or mobile geodatabase that will be created for the extracted data. This parameter is required when the out_type parameter is set to NEW_FILE_GEODATABASE or NEW_MOBILE_GEODATABASE...",
                        "default": None
                },
                "expand_feature_classes_and_tables": {
                        "type": "string",
                        "description": "Specifies whether expanded feature classes and tables\u2014such as those in networks, topologies, or relationship classes\u2014will be added.USE_DEFAULTS\u2014The expanded feature classes and tables related to the f...",
                        "default": None
                },
                "reuse_schema": {
                        "type": "string",
                        "description": "Specifies whether a geodatabase that contains the schema of the data to be extracted will be reused. Reusing the schema reduces the amount of time required to extract the data.\t\t\t\t\t\tDO_NOT_REUSE\u2014The s...",
                        "default": None
                },
                "get_related_data": {
                        "type": "string",
                        "description": "Specifies whether rows related to rows existing in the data will be extracted. For example, a feature (f1) is inside the geometry filter and a related feature (f2) from another class is outside the fi...",
                        "default": None
                },
                "extract_using_geometry_features": {
                        "type": "string",
                        "description": "The features that will be used to define the area to extract.",
                        "default": None
                },
                "geometry_filter_type": {
                        "type": "string",
                        "description": "Specifies the spatial relationship between the extract_using_geometry_features and in_data parameter values and how that relationship will be filtered. The spatial relationship is applied to data in a...",
                        "default": None
                },
                "all_records_for_tables": {
                        "type": "string",
                        "description": "Specifies whether all records or only the schema will be extracted for tables that do not have filters applied (such as selections or definition queries).\t\t\t\t\t\tTables with applied filters will be hono...",
                        "default": None
                }
        },
        "required": [
                "in_data"
        ]
},
    "find_identical": {
        "name": "find_identical",
        "description": "Reports any records in a feature class or table that have identical values in a list of fields, and generates a table listing the identical records. If the Shape field is specified, feature geometries will be compared. The Delete Identical tool can be used to find and delete identical records.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The table or feature class for which identical records will be found."
                },
                "out_dataset": {
                        "type": "string",
                        "description": "The output table reporting identical records. The FEAT_SEQ field in the output table will have the same value for identical records."
                },
                "fields": {
                        "type": "string",
                        "description": "The field or fields whose values will be compared to find identical records."
                },
                "xy_tolerance": {
                        "type": "string",
                        "description": "The x,y tolerance that will be applied to each vertex when evaluating whether there is an identical vertex in another feature.This parameter is enabled when the fields parameter value includes the Sha...",
                        "default": None
                },
                "z_tolerance": {
                        "type": "string",
                        "description": "The z-tolerance that will be applied to each vertex when evaluating whether there is an identical vertex in another feature.This parameter is enabled when the fields parameter value includes the Shape...",
                        "default": None
                },
                "output_record_option": {
                        "type": "string",
                        "description": "Specifies whether only duplicated records will be included in the output table.ALL\u2014All input records will have corresponding records in the output table. This is the default.ONLY_DUPLICATES\u2014Only dupli...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_dataset",
                "fields"
        ]
},
    "merge": {
        "name": "merge",
        "description": "Combines multiple input datasets into a single, new output dataset. This tool can combine point, line, or polygon feature classes or tables. Use the Append tool to combine input datasets with an existing dataset.",
        "parameters": {
                "inputs": {
                        "type": "string",
                        "description": "The input datasets that will be merged into a new output dataset. Input datasets can be point, line, or polygon feature classes or tables. Input feature classes must all be of the same geometry type.T..."
                },
                "output": {
                        "type": "string",
                        "description": "The output dataset that will contain all combined input datasets."
                },
                "field_mappings": {
                        "type": "string",
                        "description": "Use the field map to reconcile schema differences and match attribute fields between multiple datasets.\r\nThe output includes all fields from the input\r\ndatasets by default.Use the field map to add, de...",
                        "default": None
                },
                "add_source": {
                        "type": "string",
                        "description": "Specifies whether source information will be added to the output dataset in a new MERGE_SRC text field. The values in the MERGE_SRC  field will indicate the input dataset path or layer name that is th...",
                        "default": None
                },
                "field_match_mode": {
                        "type": "string",
                        "description": "Specifies how fields from the input dataset will be transferred to the output datasetAUTOMATIC\u2014Fields of the same name will be automatically mapped together in the output. Fields that are unique to th...",
                        "default": None
                }
        },
        "required": [
                "inputs",
                "output"
        ]
},
    "rename": {
        "name": "rename",
        "description": "Changes the name of a dataset.  This includes a variety of data types, including feature dataset, raster, table, and shapefile.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The input data to be renamed."
                },
                "out_data": {
                        "type": "string",
                        "description": "The name of the output data."
                },
                "data_type": {
                        "type": "string",
                        "description": "The type of data to be renamed.\r\n\r\nThis parameter is only necessary in the event of a name conflict\r\nbetween two different data types. For example, a geodatabase can\r\ncontain\r\na relationship class wit..."
                }
        },
        "required": [
                "in_data",
                "out_data",
                "data_type"
        ]
},
    "sort": {
        "name": "sort",
        "description": "Reorders records in a feature class or table, in ascending or descending order, based on one or multiple fields. The reordered result is written to a new dataset. Learn more about how Sort works",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input dataset with the records that will be reordered based on the field values in the sort field or fields."
                },
                "out_dataset": {
                        "type": "string",
                        "description": "The output feature class or table."
                },
                "sort_field_direction": {
                        "type": "string",
                        "description": "The field or fields whose values will be used to reorder the input records and the direction the records will be sorted. License:Sorting by the Shape field or by multiple fields is only available with..."
                },
                "spatial_sort_method": {
                        "type": "string",
                        "description": "Specifies how features will be spatially sorted. The sort method is only enabled when the Shape field is designated as one of the sort fields.UR\u2014Sorting will start at the upper right corner. This is t...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_dataset",
                "sort_field_direction"
        ]
},
    "transfer_files": {
        "name": "transfer_files",
        "description": "Transfers files between a file system and a cloud storage workspace.",
        "parameters": {
                "input_paths": {
                        "type": "string",
                        "description": "The list of input files or folders that will be copied to the output folder. The path can be a file system path or cloud storage path where the .acs file can be used."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder path where the files will be copied."
                },
                "file_filter": {
                        "type": "string",
                        "description": "A file pattern filter that will limit the number of files that need to be copied, such as .tif, .crf, and similar image file types.",
                        "default": None
                }
        },
        "required": [
                "input_paths",
                "output_folder"
        ]
},
    "upload_file_to_portal": {
        "name": "upload_file_to_portal",
        "description": "Uploads a file to the active portal.",
        "parameters": {
                "in_file": {
                        "type": "string",
                        "description": "The file that will be uploaded to the active portal. Supported file\r\ntypes are layer (.lyrx), layout (.pagx), map (.mapx),  PDF (.pdf), presentation (.prsx), report\r\n(.rptx), report template (.rptt), ..."
                },
                "title": {
                        "type": "string",
                        "description": "The title of the portal item."
                },
                "folder": {
                        "type": "string",
                        "description": "The name of an existing folder or a new folder on the portal.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "A short description of the item.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The keywords or terms that describe the item. Separate individual tags with a comma.",
                        "default": None
                },
                "sharing_level": {
                        "type": "string",
                        "description": "Specifies the sharing level of the item.OWNER\u2014Only the owner of the item will have access.ORGANIZATION\u2014All members of the organization will have accessEVERYONE\u2014Everyone, including people outside the o...",
                        "default": None
                },
                "groups": {
                        "type": "string",
                        "description": "The groups with which the item will be shared.",
                        "default": None
                }
        },
        "required": [
                "in_file",
                "title"
        ]
},
    "dissolve": {
        "name": "dissolve",
        "description": "Aggregates features based on specified attributes. An alternate tool is available for dissolve operations. See the Pairwise Dissolve tool documentation for details. Learn more about how Dissolve works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features to be aggregated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class to be created that will contain the aggregated features."
                },
                "dissolve_field": {
                        "type": "string",
                        "description": "The field or fields on which features will be aggregated. If no fields are specified, the tool will dissolve all features together.",
                        "default": None
                },
                "statistics_fieldsfield_statistic_type": {
                        "type": "string",
                        "description": "Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are exclud...",
                        "default": None
                },
                "multi_part": {
                        "type": "string",
                        "description": "Specifies whether multipart features will be allowed in the output feature class.MULTI_PART\u2014Multipart features will be allowed in the output feature class. This is the default. SINGLE_PART\u2014Multipart f...",
                        "default": None
                },
                "unsplit_lines": {
                        "type": "string",
                        "description": "Specifies how line features will be dissolved.DISSOLVE_LINES\u2014Lines will be dissolved into a single feature. This is the default. UNSPLIT_LINES\u2014Lines will only be dissolved when two lines have an end v...",
                        "default": None
                },
                "concatenation_separator": {
                        "type": "string",
                        "description": "A character or characters that will be used to concatenate values when the CONCATENATION option is used for the statistics_fields parameter. By default, the tool will concatenate values without a sepa...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "eliminate": {
        "name": "eliminate",
        "description": "Eliminates polygons by merging them with neighboring polygons that have the largest area or the longest shared border. This tool is often used to remove small sliver polygons that are the result of overlay operations, such as those performed by Intersect and Union tools.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The layer with the polygons that will be merged with neighboring polygons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class to be created."
                },
                "selection": {
                        "type": "string",
                        "description": "Specifies whether the selected polygon will be merged with a polygon with the longest shared border or the largest area.LENGTH\u2014The selected polygon will be merged with the neighboring polygon with the...",
                        "default": None
                },
                "ex_where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will be used to identify features that will not be altered. For more information on SQL syntax, see the SQL reference for elements used in query expressions help topic.",
                        "default": None
                },
                "ex_features": {
                        "type": "string",
                        "description": "An input polyline or polygon feature class or layer that defines polygon boundaries, or portions thereof, that will not be eliminated.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "eliminate_polygon_part": {
        "name": "eliminate_polygon_part",
        "description": "Creates a new output feature class containing the features from the input polygons with some parts or holes of a specified size deleted.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer whose features will be copied to the output feature class, with some parts or holes eliminated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class containing the remaining parts."
                },
                "condition": {
                        "type": "string",
                        "description": "Specifies how the parts to be eliminated will be determined. AREA\u2014Parts with an area less than that specified will be eliminated.PERCENT\u2014Parts with a percent of the total outer area less than that spe...",
                        "default": None
                },
                "part_area": {
                        "type": "string",
                        "description": "Eliminate parts smaller than this area.",
                        "default": None
                },
                "part_area_percent": {
                        "type": "string",
                        "description": "Eliminate parts smaller than this percentage of a feature's total outer area.",
                        "default": None
                },
                "part_option": {
                        "type": "string",
                        "description": "Determines what parts can be eliminated.CONTAINED_ONLY\u2014Only parts totally contained by other parts can be eliminated. This is the default. ANY\u2014Any parts can be eliminated.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "analyze_datasets": {
        "name": "analyze_datasets",
        "description": "Updates database statistics of base tables, delta tables, and archive tables, along with the statistics on the indexes of those tables. This tool is used in enterprise geodatabases to help get optimal performance from the relational database management system (RDBMS) query optimizer. Stale statistics can affect geodatabase performance.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database that contains the data to be analyzed."
                },
                "include_system": {
                        "type": "string",
                        "description": "Specifies whether statistics will be gathered on the states and state lineages tables.\r\nNote:You must be the geodatabase administrator to use this parameter.This parameter only applies to geodatabases..."
                },
                "in_datasets": {
                        "type": "string",
                        "description": "The names of the datasets that will be analyzed. An individual dataset or a Python list of datasets can be used. Dataset names use paths relative to the input workspace; full paths are not valid input...",
                        "default": None
                },
                "analyze_base": {
                        "type": "string",
                        "description": "Specifies whether the selected dataset base tables will be analyzed.This parameter only applies to geodatabases. If the input workspace is a database, this parameter will be ignored.ANALYZE_BASE\u2014 Stat...",
                        "default": None
                },
                "analyze_delta": {
                        "type": "string",
                        "description": "Specifies whether the selected dataset delta tables will be analyzed.This parameter only applies to geodatabases that contain traditional versions. If the input workspace is a database or does not par...",
                        "default": None
                },
                "analyze_archive": {
                        "type": "string",
                        "description": "Specifies whether the selected dataset archive tables will be analyzed.This parameter only applies to geodatabases that contain archive-enabled datasets. If the input workspace is a database, this par...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "include_system"
        ]
},
    "change_privileges": {
        "name": "change_privileges",
        "description": "Establishes or changes user access privileges on the input enterprise database datasets, stand-alone feature classes, or tables.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The datasets, feature classes, or tables whose access privileges will be changed."
                },
                "user": {
                        "type": "string",
                        "description": "The database username whose privileges will be modified."
                },
                "view": {
                        "type": "string",
                        "description": "Specifies the user's view privileges.AS_IS\u2014No changes will be made to the user's existing view privileges. If the user has view privileges, they will continue to have view privileges. If the user does...",
                        "default": None
                },
                "edit": {
                        "type": "string",
                        "description": "Specifies the user's edit privileges.AS_IS\u2014 No changes will be made to the user's existing edit privileges. If the user has edit privileges, they will continue to have edit privileges. If the user doe...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "user"
        ]
},
    "compress": {
        "name": "compress",
        "description": "Compresses an enterprise geodatabase by removing states not referenced by a version and redundant rows.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The database connection file that connects to the enterprise geodatabase to be compressed. Connect as the geodatabase administrator."
                }
        },
        "required": [
                "in_workspace"
        ]
},
    "configure_geodatabase_log_file_tables": {
        "name": "configure_geodatabase_log_file_tables",
        "description": "Alters the type of log file tables used by an earlier release enterprise geodatabase to maintain lists of records cached by ArcGIS.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "A database connection (.sde file) to the enterprise \r\ngeodatabase where the log file table configuration will be changed. The connection must be made as the geodatabase administrator."
                },
                "log_file_type": {
                        "type": "string",
                        "description": "Specifies the type of log file tables the geodatabase will use.SESSION_LOG_FILE\u2014Session-based log file tables for selection sets will be used. Session-based log file tables are dedicated to a single s..."
                },
                "log_file_pool_size": {
                        "type": "string",
                        "description": "The number of tables included in the pool that the geodatabase will use if a pool of session-based log file tables owned by the geodatabase administrator is used.",
                        "default": None
                },
                "use_tempdb": {
                        "type": "string",
                        "description": "This parameter is no longer applicable in any supported ArcGIS release.",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "log_file_type"
        ]
},
    "create_database_sequence": {
        "name": "create_database_sequence",
        "description": "Creates a database sequence in a geodatabase. You can use the sequences in custom applications that access the geodatabase.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The file, mobile, or enterprise geodatabase in which the sequence will be created. For an enterprise geodatabase, the workspace is the database connection file (.sde) to connect to the enterprise geod..."
                },
                "seq_name": {
                        "type": "string",
                        "description": "The name that will be assigned to the database sequence. For enterprise geodatabases, the name must meet sequence name requirements for the database platform you're using and must be unique in the dat..."
                },
                "seq_start_id": {
                        "type": "string",
                        "description": "The starting number of the sequence. If you do not provide a starting number, the sequence starts with 1. If you do provide a starting number, it must be greater than 0.",
                        "default": None
                },
                "seq_inc_value": {
                        "type": "string",
                        "description": "Describes how the sequence numbers will increment. For example, if the sequence starts at 10 and the increment value is 5, the next value in the sequence is 15, and the next value after that is 20. If...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "seq_name"
        ]
},
    "create_database_user": {
        "name": "create_database_user",
        "description": "Creates a database user with privileges sufficient to create data in the database.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The connection file to an Oracle, PostgreSQL, or SQL Server database or an enterprise geodatabase in those databases. Ensure that the connection is made as a user with privileges to create users in th..."
                },
                "user_authentication_type": {
                        "type": "string",
                        "description": "Specifies the authentication type for the user. If you specify OPERATING_SYSTEM_USER, an operating system login must already exist for the user you will create. Operating system users are only support...",
                        "default": None
                },
                "user_name": {
                        "type": "string",
                        "description": "The name of the new database user.If you  create a database user for an operating system login, the username must be the same as the login name."
                },
                "user_password": {
                        "type": "string",
                        "description": "The password for the new user. The password policy of the underlying database is enforced.If you  create a database user for an operating system login, no input is required.",
                        "default": None
                },
                "role": {
                        "type": "string",
                        "description": "The name of the existing database role to which the new user will be added.",
                        "default": None
                },
                "tablespace_name": {
                        "type": "string",
                        "description": "The name of the tablespace that will be used as the default tablespace for the new user in an Oracle database. You can specify a preconfigured tablespace, or, if the tablespace does not exist,  it wil...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "user_name"
        ]
},
    "create_enterprise_geodatabase": {
        "name": "create_enterprise_geodatabase",
        "description": "Creates a database, storage locations, and a database user to act as the geodatabase administrator and owner of the geodatabase. Functionality varies depending on the database management system used. The tool grants the geodatabase administrator the privileges required to create a geodatabase; it then creates a geodatabase in the database.",
        "parameters": {
                "database_platform": {
                        "type": "string",
                        "description": "Specifies the type of database management system to which a connection to create a geodatabase will be made.Oracle\u2014Connection to an Oracle instance will be made.PostgreSQL\u2014Connection to a PostgreSQL d..."
                },
                "instance_name": {
                        "type": "string",
                        "description": "The name of the instance.For SQL Server, provide the SQL Server instance name. Case-sensitive or binary collation SQL Server instances are not supported.For Oracle, provide either the TNS name or the ..."
                },
                "database_name": {
                        "type": "string",
                        "description": "The name of the database.This parameter is valid for PostgreSQL and SQL Server. You can provide either the name of an existing, preconfigured database or a name for a database that the tool will creat...",
                        "default": None
                },
                "account_authentication": {
                        "type": "string",
                        "description": "Specifies the type of authentication that will be used for the database connection.OPERATING_SYSTEM_AUTH\u2014Operating system authentication will be used. The login information that you provide for the co...",
                        "default": None
                },
                "database_admin": {
                        "type": "string",
                        "description": "The database administrator user for database authentication. For Oracle, use the sys user. For PostgreSQL, specify a user with superuser status. For SQL Server, specify any member of the sysadmin fixe...",
                        "default": None
                },
                "database_admin_password": {
                        "type": "string",
                        "description": "The database administrator password for database authentication.",
                        "default": None
                },
                "sde_schema": {
                        "type": "string",
                        "description": "This parameter is only relevant to SQL Server and specifies whether the geodatabase will be created in the schema of a user named sde or in the dbo schema in the database. If creating a dbo-schema geo...",
                        "default": None
                },
                "gdb_admin_name": {
                        "type": "string",
                        "description": "The name of the geodatabase administrator user.If you are using PostgreSQL, this value must be sde. \r\nIf the sde login role does not exist, this tool will create it and grant it superuser status in th...",
                        "default": None
                },
                "gdb_admin_password": {
                        "type": "string",
                        "description": "The password for the geodatabase administrator user. If  the geodatabase administrator user exists in the database management system, the password you provide must match the existing password.\r\nIf the...",
                        "default": None
                },
                "tablespace_name": {
                        "type": "string",
                        "description": "The name of the tablespace.This parameter is only valid for Oracle and PostgreSQL database management system types. For Oracle, do one of the following: Provide the name of an existing tablespace. Thi...",
                        "default": None
                },
                "authorization_file": {
                        "type": "string",
                        "description": "The keycodes file that was created when ArcGIS Server was authorized. If you have not done so, authorize ArcGIS Server to create this file.This file is in the &lt;drive&gt;\\Program Files\\ESRI\\License&..."
                },
                "spatial_type": {
                        "type": "string",
                        "description": "Specifies the spatial type that will be used. This is only applicable to PostgreSQL databases.ST_GEOMETRY\u2014The ST_Geometry spatial type will be used. This is the default.POSTGIS\u2014The PostGIS spatial typ...",
                        "default": None
                }
        },
        "required": [
                "database_platform",
                "instance_name",
                "authorization_file"
        ]
},
    "create_role": {
        "name": "create_role",
        "description": "Creates a database role, allowing you to add users to or remove them from the role.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The connection file to a database or enterprise geodatabase. Connect as a database administrator user."
                },
                "role": {
                        "type": "string",
                        "description": "The name of the database role to create. If it's an existing role, type the name for the role you want to add users to or remove them from."
                },
                "grant_revoke": {
                        "type": "string",
                        "description": "Specifies whether the role will be added to a  user or list of users\r\nor a user or list of users will be removed from the role.GRANT\u2014The role will be granted to the specified user or users, making the...",
                        "default": None
                },
                "user_name": {
                        "type": "string",
                        "description": "The name of the user whose role membership will change. To specify multiple users, type the user names separated by commas (no spaces).",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "role"
        ]
},
    "delete_database_sequence": {
        "name": "delete_database_sequence",
        "description": "Deletes a database sequence from a geodatabase.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The full path to the location of the file or mobile geodatabase from which you want to delete a sequence or\r\nthe database connection file (.sde) to connect to the enterprise geodatabase from which you..."
                },
                "seq_name": {
                        "type": "string",
                        "description": "The name of the database sequence you want to delete. Once deleted, the sequence cannot be used to generate sequence IDs when called from existing custom applications or expressions."
                }
        },
        "required": [
                "in_workspace",
                "seq_name"
        ]
},
    "delete_schema_geodatabase": {
        "name": "delete_schema_geodatabase",
        "description": "Deletes a geodatabase from a user's schema in Oracle.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database connection file (.sde) of the user-schema geodatabase to be deleted. You must connect as the schema owner."
                }
        },
        "required": [
                "input_database"
        ]
},
    "diagnose_version_metadata": {
        "name": "diagnose_version_metadata",
        "description": "Identifies inconsistencies in the system tables used to manage traditional versions and states in a geodatabase.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database connection (.sde file) to the enterprise \r\ngeodatabase in which traditional versioning system table inconsistencies may exist.The connection must be made as the geodatabase administrator."
                },
                "out_log": {
                        "type": "string",
                        "description": "The name and location of the output log file.The log file is an ASCII\r\nfile containing\r\na list of the system tables in the specified version that contain inconsistent  records, as well as the database..."
                }
        },
        "required": [
                "input_database",
                "out_log"
        ]
},
    "diagnose_version_tables": {
        "name": "diagnose_version_tables",
        "description": "Identifies inconsistencies in the delta (A and D) tables of datasets that are registered for traditional versioning.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database connection (.sde file) to the enterprise \r\ngeodatabase in which delta table inconsistencies may exist. The connection must be made as the geodatabase administrator."
                },
                "out_log": {
                        "type": "string",
                        "description": "The path and name of the output log file. The log file is an ASCII\r\nfile containing\r\na list of the tables in the specified version that contain inconsistent records, as well as information about the c..."
                },
                "target_version": {
                        "type": "string",
                        "description": "The geodatabase version with the delta tables that will be checked for inconsistencies. If no version is specified, all versions are processed.",
                        "default": None
                },
                "input_tables": {
                        "type": "string",
                        "description": "A single table or  a text file containing a\r\nlist of versioned tables with the associated delta tables to be checked for inconsistencies. Use fully-qualified table names in the text file, and place on...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "out_log"
        ]
},
    "enable_enterprise_geodatabase": {
        "name": "enable_enterprise_geodatabase",
        "description": "Creates geodatabase system tables, stored procedures, functions, and types in an existing database, which enable geodatabase functionality in the database.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The path and database connection file (.sde) name for the database in which geodatabase functionality will be enabled. The database connection must connect as a user that qualifies as a geodatabase ad..."
                },
                "authorization_file": {
                        "type": "string",
                        "description": "The keycodes file that was created when ArcGIS Server was authorized. If you have not done so, authorize ArcGIS Server to create this file.This file is in the &lt;drive&gt;\\Program Files\\ESRI\\License&..."
                }
        },
        "required": [
                "input_database",
                "authorization_file"
        ]
},
    "export_geodatabase_configuration_keywords": {
        "name": "export_geodatabase_configuration_keywords",
        "description": "Exports the configuration keywords, parameters, and values from the specified enterprise geodatabase to an editable file. Change parameter values or add custom configuration keywords to the file and use the Import Geodatabase Configuration Keywords tool to import the changes to the geodatabase.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The connection file for the enterprise geodatabase from which you want to export configuration keywords, parameters, and values. You must connect as the geodatabase administrator."
                },
                "out_file": {
                        "type": "string",
                        "description": "The full path to and name of the ASCII text file to be created. The file will contain all the configuration keywords, parameters, and values from the enterprise geodatabase's DBTUNE (or SDE_DBTUNE) sy..."
                }
        },
        "required": [
                "input_database",
                "out_file"
        ]
},
    "import_geodatabase_configuration_keywords": {
        "name": "import_geodatabase_configuration_keywords",
        "description": "Defines data storage parameters for an enterprise geodatabase by importing a file containing configuration keywords, parameters, and values.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The connection file for the enterprise geodatabase to which you want to import the configuration file. You must connect as the geodatabase administrator."
                },
                "in_file": {
                        "type": "string",
                        "description": "The path to and name of the ASCII text file containing configuration keywords, parameters, and values to import."
                }
        },
        "required": [
                "input_database",
                "in_file"
        ]
},
    "migrate_object_id_to_64_bit": {
        "name": "migrate_object_id_to_64_bit",
        "description": "Migrates a dataset's or multiple datasets' ObjectID field to 64-bit object IDs. Learn more about migrating to 64-bit object IDs",
        "parameters": {
                "in_datasets": {
                        "type": "string",
                        "description": "The datasets that will have their ObjectID field migrated to 64 bit."
                }
        },
        "required": [
                "in_datasets"
        ]
},
    "migrate_storage": {
        "name": "migrate_storage",
        "description": "Migrates the data from a binary, spatial, or spatial attribute column of one data type to a new column of a different data type in geodatabases in Oracle and SQL Server. The configuration keyword you specify when migrating determines the data type used for the new column. After migrating the data type, you must disconnect from and reconnect to the geodatabase to reload the columns. If you do not, subsequent actions run on the newly migrated datasets may fail.",
        "parameters": {
                "in_datasets": {
                        "type": "string",
                        "description": "The datasets to be migrated. The connection you use to access the datasets must be connecting as the dataset owner."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The configuration keyword containing the appropriate parameter values for the migration. Parameter values are set by the geodatabase administrator. Contact your geodatabase administrator if you are un..."
                }
        },
        "required": [
                "in_datasets",
                "config_keyword"
        ]
},
    "rebuild_indexes": {
        "name": "rebuild_indexes",
        "description": "Rebuild existing attribute or spatial indexes in enterprise geodatabases.  Indexes  can also be rebuilt on  states and state_lineage geodatabase system tables and the delta tables of datasets that are registered to participate in traditional versioning. Out-of-date indexes can lead to poor query performance.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The connection (.sde file) to the database or geodatabase that contains the data for which you want to rebuild indexes."
                },
                "include_system": {
                        "type": "string",
                        "description": "Indicates whether indexes will be rebuilt on the states and state lineages tables.Note:You  must connect as the geodatabase administrator in the connection file you specified for the input_database fo..."
                },
                "delta_only": {
                        "type": "string",
                        "description": "Indicates how the indexes will be rebuilt on the selected datasets. This option has no effect if in_datasets is empty.This option only applies to geodatabases. If the input workspace is a database, th...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "include_system"
        ]
},
    "register_with_geodatabase": {
        "name": "register_with_geodatabase",
        "description": "Registers feature classes, tables, views, and raster layers with the geodatabase. Registering is used for data created in the database with third-party tools using SQL or in ArcGIS Pro with tools that do not register with the geodatabase (Create Unregistered Feature Class, Create Unregistered Table, and  Create Database View  tools). Only limited functionality is available from ArcGIS clients and services for data is that is  not registered. Registration stores information about the items\u2014such as table and column names, spatial extent, and geometry type\u2014in the geodatabase's system tables. This allows the registered items to participate in geodatabase functionality. Learn more about how to register a table or view with the geodatabase",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The feature class, table, view, or raster created using third-party tools or SQL, or the view created using the Create Database View tool that will be registered with the geodatabase. The dataset must..."
                },
                "in_object_id_field": {
                        "type": "string",
                        "description": "The field that will be used as the ObjectID field. When using an existing field from the input datasets, an integer data type is required. If an existing field is not used, an ObjectID field will be c...",
                        "default": None
                },
                "in_shape_field": {
                        "type": "string",
                        "description": "The field that identifies the shape of the features. If the input dataset contains a spatial data type column, include this field during the registration process.",
                        "default": None
                },
                "in_geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type. If the in_shape_field parameter value is provided, you must specify a geometry type. If the dataset being registered contains existing features, the geometry type specifie...",
                        "default": None
                },
                "in_spatial_reference": {
                        "type": "string",
                        "description": "If the in_shape_field parameter value is provided and the table is empty, specify the coordinate system to be used for features.  If the dataset being registered contains existing features, the coordi...",
                        "default": None
                },
                "in_extent": {
                        "type": "string",
                        "description": "If the in_shape_field parameter value is provided, specify the allowable coordinate range for x,y coordinates in the following order: \"XMin YMin XMax YMax\". If the dataset being registered contains ex...",
                        "default": None
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "create_unregistered_feature_class": {
        "name": "create_unregistered_feature_class",
        "description": "Creates an empty feature class in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The feature class is not registered with the geodatabase.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The enterprise database or enterprise  geodatabase in which the feature class  will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the feature class that will be created."
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies the geometry type of the feature class. This parameter is only relevant for those geometry types that store dimensionality metadata, such as ST_Geometry in PostgreSQL, PostGIS Geometry, and ...",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "An existing feature class or list of feature classes with fields and attribute schema that will be used to define the fields in the output feature class.",
                        "default": None
                },
                "has_m": {
                        "type": "string",
                        "description": "Specifies whether the feature class will have  linear measurement values (m-values).DISABLED\u2014The output feature class will not have m-values. This is the default.ENABLED\u2014The output feature class will ...",
                        "default": None
                },
                "has_z": {
                        "type": "string",
                        "description": "Specifies whether the feature class will have  elevation values (z-values).DISABLED\u2014The output feature class will not have z-values. This is the default.ENABLED\u2014The output feature class will have z-va...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature dataset. You can specify the spatial reference in the following ways: Enter the path to a .prj file, such as C:/workspace/watershed.prj. Reference a feature...",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Specifies the default storage parameters (configurations) for geodatabases in a relational database management system (RDBMS). This setting is applicable only when using enterprise geodatabase tables....",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "create_unregistered_table": {
        "name": "create_unregistered_table",
        "description": "Creates an empty table in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The table is not registered with the geodatabase.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The enterprise database or enterprise geodatabase in which the table will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the table that will be created."
                },
                "template": {
                        "type": "string",
                        "description": "An existing dataset or list of datasets with fields and attribute schema that will be used to define the fields in the output table.",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Specifies the default storage parameters (configurations) for geodatabases in a relational database management system (RDBMS). This setting is applicable only when using enterprise geodatabase tables....",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "create_database_view": {
        "name": "create_database_view",
        "description": "Creates a view in a database based on an SQL expression.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database that contains the tables or feature classes used to construct the view. This database is also where the view will be created."
                },
                "view_name": {
                        "type": "string",
                        "description": "The name of the view that will be created in the database."
                },
                "view_definition": {
                        "type": "string",
                        "description": "An SQL statement that will be used to construct the view."
                }
        },
        "required": [
                "input_database",
                "view_name",
                "view_definition"
        ]
},
    "repair_version_metadata": {
        "name": "repair_version_metadata",
        "description": "Repairs inconsistencies in the versioning system tables of a geodatabase that contains traditional versions.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database connection (.sde file) to the enterprise \r\ngeodatabase in which versioning system table inconsistencies exist. The connection must be made as the geodatabase administrator."
                },
                "out_log": {
                        "type": "string",
                        "description": "The  output log file. The log file is an ASCII\r\nfile containing\r\nthe results of the repair\r\noperation."
                }
        },
        "required": [
                "input_database",
                "out_log"
        ]
},
    "repair_version_tables": {
        "name": "repair_version_tables",
        "description": "Repairs inconsistencies in the delta (A and D) tables of datasets that are registered for traditional versioning.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database connection (.sde file) to the enterprise \r\ngeodatabase in which delta table inconsistencies exist. The connection must be made as the geodatabase administrator."
                },
                "out_log": {
                        "type": "string",
                        "description": "The location where the log file will be written and the name of the log file. The log file is an ASCII\r\nfile containing\r\nthe results of the repair\r\noperation."
                },
                "target_version": {
                        "type": "string",
                        "description": "The geodatabase version to be repaired. If no version is specified, all versions are processed.",
                        "default": None
                },
                "input_tables": {
                        "type": "string",
                        "description": "A single table or  a text file containing a\r\nlist of versioned tables with the associated delta tables to be repaired. Use fully-qualified table names in the text file, and place one table name per li...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "out_log"
        ]
},
    "update_enterprise_geodatabase_license": {
        "name": "update_enterprise_geodatabase_license",
        "description": "Updates the ArcGIS Server license in an enterprise geodatabase. If your organization licenses ArcGIS Server for a set time period, the geodatabase administrator can run the Update Enterprise Geodatabase License tool with a new  ArcGIS Server authorization file to update license information in the geodatabase before the existing license expires. This allows clients to continue working with the geodatabase without interruptions caused by expired licenses.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "A database connection (.sde file) to the enterprise geodatabase to authorize with a new ArcGIS Server enterprise authorization file.The database connection file must connect to the database as the geo..."
                },
                "authorization_file": {
                        "type": "string",
                        "description": "The path and file name of the keycodes file generated when ArcGIS Server enterprise was authorized. If necessary, copy the file from the ArcGIS Server machine to a directory that the tool can access. ..."
                }
        },
        "required": [
                "input_database",
                "authorization_file"
        ]
},
    "update_portal_dataset_owner": {
        "name": "update_portal_dataset_owner",
        "description": "Updates the portal owner of a dataset to another user. Certain datasets in an enterprise geodatabase store the active portal user account as the owner of the dataset, in addition to the data owner. The owner is determined based on the active portal user when the dataset is created. This ownership is stored in the metadata of the dataset and is used to control access for administrative tasks on the dataset. If the existing portal dataset owner leaves the organization, the portal owner must be changed to another user. This user should possess the same user type and privilege as the original owner. The following are examples of a portal dataset owner:Utility Network\u2014Portal utility network ownerTrace Network\u2014Portal trace network owner",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input dataset for which the portal owner will be updated."
                },
                "target_owner": {
                        "type": "string",
                        "description": "The name of the portal user who will be the new portal owner of the dataset."
                }
        },
        "required": [
                "in_dataset",
                "target_owner"
        ]
},
    "upgrade_dataset": {
        "name": "upgrade_dataset",
        "description": "Upgrades the schema of a mosaic dataset, network dataset, annotation dataset, dimension dataset, parcel fabric, trace network, utility network, or 3D object feature class to the current ArcGIS release. Upgrading a dataset enables it to use new functionality in the current software release.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The dataset that will be upgraded to the current ArcGIS client release."
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "upgrade_geodatabase": {
        "name": "upgrade_geodatabase",
        "description": "Upgrades a geodatabase to the latest ArcGIS release to take advantage of new functionality.",
        "parameters": {
                "input_workspace": {
                        "type": "string",
                        "description": "The  geodatabase that will be upgraded. When upgrading an enterprise geodatabase, specify a database connection file (.sde) that connects to the geodatabase as the geodatabase administrator."
                },
                "input_prerequisite_check": {
                        "type": "string",
                        "description": "Specifies whether the prerequisite check will be run before upgrading the geodatabase.NO_PREREQUISITE_CHECK\u2014The prerequisite check  will not be run. PREREQUISITE_CHECK\u2014The prerequisite check  will be ..."
                },
                "input_upgradegdb_check": {
                        "type": "string",
                        "description": "Specifies whether the input geodatabase will be upgraded.NO_UPGRADE\u2014The geodatabase will not be upgraded.UPGRADE\u2014The geodatabase will be upgraded. This is the default."
                }
        },
        "required": [
                "input_workspace",
                "input_prerequisite_check",
                "input_upgradegdb_check"
        ]
},
    "add_attribute_index": {
        "name": "add_attribute_index",
        "description": "Adds an attribute index to an existing table, feature class, shapefile, or attributed relationship class. Attribute indexes are used by ArcGIS to quickly locate records that match an attribute query.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the fields to be indexed."
                },
                "fields": {
                        "type": "string",
                        "description": "The list of fields that will be indexed. Any number of fields can be specified."
                },
                "index_name": {
                        "type": "string",
                        "description": "The name of the new index. An index name is necessary when adding an index to geodatabase feature classes and tables. For other types of input, the name is ignored.",
                        "default": None
                },
                "unique": {
                        "type": "string",
                        "description": "Specifies whether the values in the index are unique.NON_UNIQUE\u2014No values in the index are unique. This is the default.UNIQUE\u2014All values in the index are unique.",
                        "default": None
                },
                "ascending": {
                        "type": "string",
                        "description": "Specifies whether values will be indexed in ascending order.NON_ASCENDING\u2014Values will not be indexed in ascending order. This is the default. ASCENDING\u2014Values will be indexed in ascending order.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "fields"
        ]
},
    "add_full_text_index": {
        "name": "add_full_text_index",
        "description": "Adds a full-text index to specified text fields to support searching by an individual column or by multiple columns. Learn more about using full-text indexes in the geodatabase",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the fields that will be indexed."
                },
                "fields": {
                        "type": "string",
                        "description": "The text fields that will be indexed.Some databases only support a single field for full-text index creation. Support for creation of a multiple field full-text index varies based on the database."
                },
                "index_name": {
                        "type": "string",
                        "description": "The name of the index that will be created. For SQL Server, SQLite, and mobile geodatabases, this parameter will be ignored.",
                        "default": None
                },
                "catalog_name": {
                        "type": "string",
                        "description": "The existing full-text catalog name. This parameter is only applicable for SQL Server. When the SQL Server database has a default full-text catalog defined, the tool will use the default catalog, and ...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "fields"
        ]
},
    "add_spatial_index": {
        "name": "add_spatial_index",
        "description": "Adds a spatial index to a shapefile, file geodatabase, mobile geodatabase, or enterprise geodatabase feature class.   Use this tool to either add a spatial index to a shapefile or feature class that does not already have one or to re-create an existing spatial index. Learn more about spatial indexes in the geodatabase",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "An enterprise geodatabase feature class, file geodatabase feature class, mobile geodatabase feature class, or shapefile to which a spatial index is to be added or rebuilt."
                },
                "spatial_grid_1": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter will be ignored.",
                        "default": None
                },
                "spatial_grid_2": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter will be ignored.",
                        "default": None
                },
                "spatial_grid_3": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter will be ignored.",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "remove_attribute_index": {
        "name": "remove_attribute_index",
        "description": "Deletes an attribute index from an existing table, feature class, shapefile, or attributed relationship class. Attribute indexes are used by ArcGIS to quickly locate records that match an attribute query.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input containing the index or indexes that will be deleted. The input can be a table, a feature class, or an attributed relationship class."
                },
                "index_name": {
                        "type": "string",
                        "description": "The name of the index or indexes that will be deleted."
                }
        },
        "required": [
                "in_table",
                "index_name"
        ]
},
    "remove_spatial_index": {
        "name": "remove_spatial_index",
        "description": "Deletes the spatial index from a shapefile or file geodatabase, mobile geodatabase, or an enterprise geodatabase feature class. Spatial indexes are used by ArcGIS to quickly locate features that match a spatial query.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The shapefile or file geodatabase, mobile geodatabase, or an enterprise geodatabase feature class from which a spatial index will be removed."
                }
        },
        "required": [
                "in_features"
        ]
},
    "add_join": {
        "name": "add_join",
        "description": "Joins a layer to another layer or table based on a common field. Feature layers, table views, and raster layers with a raster attribute table are supported. The records in the Join Table parameter value will be matched to the records in the  Input Table parameter value. A match is made when the input field and join field values are equal. This join is temporary.",
        "parameters": {
                "in_layer_or_view": {
                        "type": "string",
                        "description": "The layer or table view to which the join table will be joined."
                },
                "in_field": {
                        "type": "string",
                        "description": "The field in the input layer or table view on which the join will be based."
                },
                "join_table": {
                        "type": "string",
                        "description": "The table or table view that will be joined to the input layer or table view."
                },
                "join_field": {
                        "type": "string",
                        "description": "The field in the join table that contains the values on which the join will be based."
                },
                "join_type": {
                        "type": "string",
                        "description": "Specifies whether only records in the input that match a record in the join table will be included in the output or all records in the input layer or table view will be included.KEEP_ALL\u2014All records i...",
                        "default": None
                },
                "index_join_fields": {
                        "type": "string",
                        "description": "Specifies whether table attribute indexes will be added to the input field and join field.INDEX_JOIN_FIELDS\u2014Both fields will be indexed.  If the table has an existing index, a new index will not be ad...",
                        "default": None
                },
                "rebuild_index": {
                        "type": "string",
                        "description": "Specifies whether the indexes of the input field and join field will be removed and rebuilt.REBUILD_INDEX\u2014 Existing indexes will be removed and a new index will be added.NO_REBUILD_INDEX\u2014 Existing ind...",
                        "default": None
                },
                "join_operation": {
                        "type": "string",
                        "description": "Specifies whether the join will be a one-to-many join or a one-to-first join when the data has a one-to-many cardinality.One-to-many join operations are supported when the input and join table are in ...",
                        "default": None
                }
        },
        "required": [
                "in_layer_or_view",
                "in_field",
                "join_table",
                "join_field"
        ]
},
    "add_relate": {
        "name": "add_relate",
        "description": "Relates a layer to another layer or table based on a field value. Feature layers, table views, subtype value layers or tables, and raster layers with a raster attribute table are supported. The records in the Relate Table parameter value are matched to the records in the input Layer Name or Table View parameter value. A match occurs when a field value in the Input Relate Field parameter value and a field value in the Output Relate Field parameter value are equal.",
        "parameters": {
                "in_layer_or_view": {
                        "type": "string",
                        "description": "The layer or table view to which the relate table will be related."
                },
                "in_field": {
                        "type": "string",
                        "description": "The primary key field  in the input layer or table view on which the relate will be based."
                },
                "relate_table": {
                        "type": "string",
                        "description": "The table or table view to be related to the input layer or table view."
                },
                "relate_field": {
                        "type": "string",
                        "description": "The foreign key field in the relate table that will be used to match the primary key."
                },
                "relate_name": {
                        "type": "string",
                        "description": "The unique name of a relate."
                },
                "cardinality": {
                        "type": "string",
                        "description": "Specifies the cardinality of the relationship. ONE_TO_ONE\u2014The relationship between the input table and related table will be one to one. For example, one record in the input table will have only one m...",
                        "default": None
                }
        },
        "required": [
                "in_layer_or_view",
                "in_field",
                "relate_table",
                "relate_field",
                "relate_name"
        ]
},
    "add_spatial_join": {
        "name": "add_spatial_join",
        "description": "Joins attributes from one feature to another based on the spatial relationship. The target features and the joined attributes from the join features will be joined. See Select By Location graphic examples for more information.",
        "parameters": {
                "target_features": {
                        "type": "string",
                        "description": "The attributes from the target features and the attributes from the join features will be joined to the target features layer. However, a subset of attributes can be defined using the field_mapping pa..."
                },
                "join_features": {
                        "type": "string",
                        "description": "The attributes from the join features will be joined to the attributes of the target features. See the explanation of the join_operation parameter for details on how the aggregation of joined attribut..."
                },
                "join_operation": {
                        "type": "string",
                        "description": "This parameter is not supported. All joins will be performed as a one-to-one join. If you are using positional arguments in Python, use a None type, an empty string (\"\" or ''), or the JOIN_ONE_TO_ONE ...",
                        "default": None
                },
                "join_type": {
                        "type": "string",
                        "description": "Specifies whether only target features with a spatial relationship with a join feature (known as an inner join) will be preserved or all target features will be preserved, even without a spatial relat...",
                        "default": None
                },
                "field_mapping": {
                        "type": "string",
                        "description": "The fields that will be temporarily joined to the target dataset with their respective properties and source fields. All fields from the join dataset will be included by default. Use the field map to ...",
                        "default": None
                },
                "match_option": {
                        "type": "string",
                        "description": "Specifies the criteria that will be used to match rows.INTERSECT\u2014The features in the join features will be matched if they intersect a target  feature. This is the default. Specify the distance in the...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "Join features within this distance of a target feature will be considered for the spatial join. A search radius is only valid when the spatial relationship is specified (the match_option parameter is ...",
                        "default": None
                },
                "distance_field_name": {
                        "type": "string",
                        "description": "The name of the field that contains the distance between the target feature and the closest join feature. This field will be added to the join. This parameter is only valid when the spatial relationsh...",
                        "default": None
                },
                "permanent_join": {
                        "type": "string",
                        "description": "Specifies whether fields from the join feature class will be temporarily added to the layer or permanently added to the target feature class.NO_PERMANENT_FIELDS\u2014The fields from the join feature class ...",
                        "default": None
                },
                "match_fieldsjoin_field_target_field": {
                        "type": "string",
                        "description": "Pairs of fields from the join features and target features that will be used for attribute matching. Only the records from the join features that share match field values with the target features will...",
                        "default": None
                }
        },
        "required": [
                "target_features",
                "join_features"
        ]
},
    "join_field": {
        "name": "join_field",
        "description": "Permanently joins the contents of a table to another table based on a common attribute field. The input table is updated to contain the fields from the join table. You can select which fields from the join table will be added to the input table.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The table or feature class to which the join table will be joined."
                },
                "in_field": {
                        "type": "string",
                        "description": "The field in the input table on which the join will be based."
                },
                "join_table": {
                        "type": "string",
                        "description": "The table that will be joined to the input table."
                },
                "join_field": {
                        "type": "string",
                        "description": "The field in the join table that contains the values on which the join will be based."
                },
                "fields": {
                        "type": "string",
                        "description": "The fields from the join table that will be transferred to the input table based on a join between the input table and the join table.",
                        "default": None
                },
                "fm_option": {
                        "type": "string",
                        "description": "Specifies how joining fields and field types will be transferred to the output.NOT_USE_FM\u2014Fields and field types from the joined table will be transferred to the output. This is the default.USE_FM\u2014The...",
                        "default": None
                },
                "field_mapping": {
                        "type": "string",
                        "description": "The fields that will be joined to the input table with their respective properties and source fields. All fields from the join table will be included by default. Use the field map to add, delete, rena...",
                        "default": None
                },
                "index_join_fields": {
                        "type": "string",
                        "description": "Specifies whether attribute indexes will be added or replaced for the input field and join field.NO_INDEXES\u2014Attribute indexes will not be added. This is the default.NEW_INDEXES\u2014An attribute index will...",
                        "default": None
                }
        },
        "required": [
                "in_data",
                "in_field",
                "join_table",
                "join_field"
        ]
},
    "remove_join": {
        "name": "remove_join",
        "description": "Removes a join from a feature layer or table view.",
        "parameters": {
                "in_layer_or_view": {
                        "type": "string",
                        "description": "The layer or table view from which the join will be removed."
                },
                "join_name": {
                        "type": "string",
                        "description": "The name of the join to be removed.If no name is provided, the tool will remove all joins from the input.",
                        "default": None
                }
        },
        "required": [
                "in_layer_or_view"
        ]
},
    "remove_relate": {
        "name": "remove_relate",
        "description": "Removes a relate from a feature layer or a table view.",
        "parameters": {
                "in_layer_or_view": {
                        "type": "string",
                        "description": "The layer or table view from which to remove the relate."
                },
                "relate_name": {
                        "type": "string",
                        "description": "The name of the relate to remove."
                }
        },
        "required": [
                "in_layer_or_view",
                "relate_name"
        ]
},
    "validate_join": {
        "name": "validate_join",
        "description": "Validates a  join between two layers or tables to determine if the layers or tables have valid field names and Object ID fields, if the join produces matching records, if the join is a one-to-one or one-to-many join, and other properties of the join. This tool does not produce a join; it analyzes a potential join with the current data.  Since all joins can potentially become one-to-many, the layer properties will always show cardinality one-to-many.  A join can change from one-to-one to one-to-many if the data changes. The join being validated by this tool can be created using the Add Join or Join Field tool. This tool will report the join validation results as messages and optionally as an output table.",
        "parameters": {
                "in_layer_or_view": {
                        "type": "string",
                        "description": "The layer or table view with the join to the join table that will be validated."
                },
                "in_field": {
                        "type": "string",
                        "description": "The field in the input layer or table view on which the join will be based."
                },
                "join_table": {
                        "type": "string",
                        "description": "The table or table view with the join to the input layer or table view that will be validated."
                },
                "join_field": {
                        "type": "string",
                        "description": "The field in the join table that contains the values on which the join will be based."
                },
                "output_msg": {
                        "type": "string",
                        "description": "The output table containing the validation messages in a tabular form.",
                        "default": None
                }
        },
        "required": [
                "in_layer_or_view",
                "in_field",
                "join_table",
                "join_field"
        ]
},
    "add_files_to_las_dataset": {
        "name": "add_files_to_las_dataset",
        "description": "Adds references for one or more LAS files and  surface constraint features to a LAS dataset.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be processed."
                },
                "in_files": {
                        "type": "string",
                        "description": "Inputs that can include any combination of .las files, .zlas files, LAS datasets, and  folders containing  .las or  .zlas data. When a LAS dataset is specified as input, all  .las and .zlas files that...",
                        "default": None
                },
                "folder_recursion": {
                        "type": "string",
                        "description": "Specifies whether lidar files residing in the subdirectories of an input folder will be added to the LAS dataset.\t\t\t\t\tNO_RECURSION\u2014Only lidar files residing in an input folder will be added to the LAS...",
                        "default": None
                },
                "in_surface_constraintsin_feature_class_height_field_sf_type": {
                        "type": "string",
                        "description": "The features that will be referenced by the LAS dataset when generating a triangulated surface. Each feature must have the following properties defined:              in_feature_class\u2014The feature  to b...",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset"
        ]
},
    "build_las_dataset_pyramid": {
        "name": "build_las_dataset_pyramid",
        "description": "Constructs or updates a LAS dataset display cache, which optimizes its rendering performance. Learn more about the LAS dataset pyramid",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The input LAS dataset.It is only possible to construct a LAS dataset pyramid if the LAS dataset has an .lasd extension. The pyramid construction process does not support individual .las or .zlas files..."
                },
                "point_selection_method": {
                        "type": "string",
                        "description": "Specifies how the point in each binned region will be selected to construct the pyramid. This parameter is disabled if the LAS dataset contains a pyramid.Z_MIN\u2014The point with the lowest z-value will b...",
                        "default": None
                },
                "class_codes_weights": {
                        "type": "string",
                        "description": "The weights assigned to each class code that determine which points are retained in each thinning region.\r\nThis parameter is only enabled when the Class Code Weights option is specified in the Point S...",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset"
        ]
},
    "create_las_dataset": {
        "name": "create_las_dataset",
        "description": "Creates a LAS dataset referencing one or more .las files and optional surface constraint features.",
        "parameters": {
                "input": {
                        "type": "string",
                        "description": "The .las files, LAS datasets, and folders containing .las files that will be referenced by the LAS dataset. This information can be supplied as a string containing all the input data or a list of stri..."
                },
                "out_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be created."
                },
                "folder_recursion": {
                        "type": "string",
                        "description": "Specifies whether lidar files residing in the subdirectories of an input folder will be added to the LAS dataset.\t\t\t\t\tNO_RECURSION\u2014Only lidar files residing in an input folder will be added to the LAS...",
                        "default": None
                },
                "in_surface_constraintsin_feature_class_height_field_sf_type": {
                        "type": "string",
                        "description": "The features that will be referenced by the LAS dataset when generating a triangulated surface. Each feature must have the following properties defined:              in_feature_class\u2014The feature  to b...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the  LAS dataset. If no spatial reference is explicitly assigned, the LAS dataset will use the coordinate system of the first input .las file. If the input files do not contai...",
                        "default": None
                },
                "compute_stats": {
                        "type": "string",
                        "description": "Specifies whether statistics for the .las files will be computed and a spatial index generated for the LAS dataset.   The presence of statistics allows the LAS dataset layer's filtering and symbology ...",
                        "default": None
                },
                "relative_paths": {
                        "type": "string",
                        "description": "Specifies whether lidar files and surface constraint features will be referenced by the LAS dataset through relative or absolute paths.  Using relative paths may be convenient for cases in which the L...",
                        "default": None
                },
                "create_las_prj": {
                        "type": "string",
                        "description": "Specifies whether .prj files will be created for the .las files referenced by the LAS dataset.            NO_FILES\u2014No .prj files will be created. This is the default.FILES_MISSING_PROJECTION\u2014Correspon..."
                },
                "extent": {
                        "type": "string",
                        "description": "The processing extent will be used to select a subset of .las files from the list of files and folders in the input parameter value. Any .las files that fall entirely outside of this extent will be ex...",
                        "default": None
                },
                "boundary": {
                        "type": "string",
                        "description": "The polygon features whose boundary will be used to select a subset of .las files from the list of files and folders in the input parameter. Any .las files that fall entirely outside of the polygon fe...",
                        "default": None
                },
                "add_only_contained_files": {
                        "type": "string",
                        "description": "Specifies whether the .las files that will be added to the LAS dataset must be fully or partially contained by either the processing extent, the processing boundary polygon, or the intersection of bot...",
                        "default": None
                }
        },
        "required": [
                "input",
                "out_las_dataset",
                "create_las_prj"
        ]
},
    "las_dataset_statistics": {
        "name": "las_dataset_statistics",
        "description": "Calculates or updates statistics for a LAS dataset and generates an optional statistics report.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be processed."
                },
                "calculation_type": {
                        "type": "string",
                        "description": "Specifies whether statistics will be calculated for all lidar files or only for those that do not have statistics:\r\nSKIP_EXISTING_STATS\u2014LAS files with up-to-date statistics will be skipped, and statis...",
                        "default": None
                },
                "out_file": {
                        "type": "string",
                        "description": "The output text file that will contain the  summary of the LAS dataset statistics.",
                        "default": None
                },
                "summary_level": {
                        "type": "string",
                        "description": "Specify the type of summary contained in the report.\r\nDATASET\u2014The report will summarize statistics for the entire LAS dataset. This is the default.LAS_FILES\u2014The report will summarize statistics for th...",
                        "default": None
                },
                "delimiter": {
                        "type": "string",
                        "description": "The delimiter that will be used to indicate the separation of entries in the columns of the text file table.\t\t\t\t\tSPACE\u2014A space will be used to delimit field values. This is the default.COMMA\u2014A comma w...",
                        "default": None
                },
                "decimal_separator": {
                        "type": "string",
                        "description": "The decimal character that will be used in the text file to differentiate the integer of a number from its fractional part.\t\t\t\t\tDECIMAL_POINT\u2014A point will be used as the decimal character. This is the...",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset"
        ]
},
    "las_point_statistics_as_raster": {
        "name": "las_point_statistics_as_raster",
        "description": "Creates a raster whose cell values reflect statistical information about LAS points.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be processed."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The location and name of the output raster. When storing a raster dataset in a geodatabase or in a folder such as an Esri Grid, do not add a file extension to the name of the raster dataset. A file ex..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the type of statistics that will be collected about the LAS points in each cell of the output raster.\r\nPULSE_COUNT\u2014The number of last return points will be collected.POINT_COUNT\u2014The number o...",
                        "default": None
                },
                "sampling_type": {
                        "type": "string",
                        "description": "Specifies how the Sampling Value parameter will be interpreted to define the output raster's cell size.\t\t\t\t\tOBSERVATIONS\u2014The Sampling Value will define the number of columns or rows in the output rast...",
                        "default": None
                },
                "sampling_value": {
                        "type": "string",
                        "description": "The value used in conjunction with the Sampling Type parameter to define the output raster's cell size.",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset",
                "out_raster"
        ]
},
    "project_las": {
        "name": "project_las",
        "description": "Projects .las or .zlas files from one coordinate system to another.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The input .las or .zlas files that will be projected. A LAS dataset can also be provided to process all of the .las and .zlas files it references."
                },
                "target_folder": {
                        "type": "string",
                        "description": "The existing folder where the output .las files will be written."
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system of the output LAS format files. Valid values are a Spatial Reference object, a file with a .prj extension, or a string representation of a coordinate system."
                },
                "geographic_transform": {
                        "type": "string",
                        "description": "This method can be used for converting data between two geographic coordinate systems or datums. This optional parameter may be required if the input and output coordinate systems have different datum...",
                        "default": None
                },
                "compression": {
                        "type": "string",
                        "description": "Specifies whether the output file will be written using the compressed ZLAS format or the uncompressed LAS format. \r\nSAME_AS_INPUT\u2014The output will be written using the same compression as the input fi...",
                        "default": None
                },
                "las_options": {
                        "type": "string",
                        "description": "Specifies the operations that will be performed on the .las files.REARRANGE\u2014The points will be rearranged. Rearranging points can improve how the output data will be processed when retrieving its poin...",
                        "default": None
                },
                "name_modifier": {
                        "type": "string",
                        "description": "Modifies the output file names by adding characters to the beginning and end of their existing file names.",
                        "default": None
                },
                "out_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will reference the newly created .las or .zlas files. This parameter provides a way to further interact with the output files. Relative paths will be used to reference the output ...",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset",
                "target_folder",
                "coordinate_system"
        ]
},
    "remove_files_from_las_dataset": {
        "name": "remove_files_from_las_dataset",
        "description": "Removes one or more LAS files and surface constraint features from a LAS dataset.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be processed."
                },
                "in_files": {
                        "type": "string",
                        "description": "The name of the LAS files or folders containing LAS files whose reference will be removed from the LAS dataset.",
                        "default": None
                },
                "in_surface_constraints": {
                        "type": "string",
                        "description": "The name of the surface constraint features that will be removed from the LAS dataset.",
                        "default": None
                },
                "delete_pyramid": {
                        "type": "string",
                        "description": "Specifies whether the LAS dataset's display pyramid will be deleted.DELETE_PYRAMID\u2014The LAS dataset's display pyramid will be deleted.NO_DELETE_PYRAMID\u2014The LAS dataset's display pyramid will not be del...",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset"
        ]
},
    "apply_symbology_from_layer": {
        "name": "apply_symbology_from_layer",
        "description": "Applies the symbology from a specified layer or layer file to the input. It can be applied to feature, raster, network analysis, TIN, and geostatistical layers.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The layer to which the symbology will be applied."
                },
                "in_symbology_layer": {
                        "type": "string",
                        "description": "The layer containing the symbology that will be applied to the input layer. Both .lyrx and .lyr files are supported."
                },
                "symbology_fieldsfield_type_source_field_target_field": {
                        "type": "string",
                        "description": "The fields from the input layer that match the symbology fields used in the symbology layer. Symbology fields contain three properties:Field type\u2014The field type: symbology value, normalization, or oth...",
                        "default": None
                },
                "update_symbology": {
                        "type": "string",
                        "description": "Specifies whether symbology ranges will be updated.DEFAULT\u2014Symbology ranges will be updated, except in the following situations:When the input layer is emptyWhen the symbology layer uses class breaks ...",
                        "default": None
                }
        },
        "required": [
                "in_layer",
                "in_symbology_layer"
        ]
},
    "generate_definition_query_from_selection": {
        "name": "generate_definition_query_from_selection",
        "description": "Creates a definition query (in SQL format) from the selected features or rows of the layer or table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The layer or table \r\nview from which  the definition query will be generated."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to generate the definition query.MATCH_SELECTION\u2014The input table's ObjectID field (or GlobalID field if present) will be used to generate the query with values p...",
                        "default": None
                },
                "field": {
                        "type": "string",
                        "description": "The field in the table or table view that will be used to generate values for the query. Accepted field types are Short, Long, Text, and GUID.This parameter is required when the method parameter is se...",
                        "default": None
                },
                "query_name": {
                        "type": "string",
                        "description": "The unique name of the query that will be generated.",
                        "default": None
                },
                "invert_where_clause": {
                        "type": "string",
                        "description": "Specifies whether the generated definition query (where clause) will be inverted and include all unselected values or include all selected values of the input table.INVERT\u2014The where clause will be inv...",
                        "default": None
                },
                "append_active_query": {
                        "type": "string",
                        "description": "Specifies whether the generated definition query  will be appended to the active queryThis parameter is available when a layer or table has an active definition query and the method parameter is set t...",
                        "default": None
                },
                "overwrite_where_clause": {
                        "type": "string",
                        "description": "Specifies whether the definition query can be modified using the where_clause parameter before it is generated.OVERWRITE\u2014The query can be modified before it is generated.NOT_OVERWRITE\u2014The query cannot...",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "The definition query that will override the other parameter values.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_table"
        ]
},
    "make_aggregation_query_layer": {
        "name": "make_aggregation_query_layer",
        "description": "Creates a query layer that summarizes, aggregates,  and filters DBMS tables dynamically based on time, range, and attribute queries from a related table, and joins the result to a feature layer. Learn more about aggregating values into related features",
        "parameters": {
                "target_feature_class": {
                        "type": "string",
                        "description": "The feature class or spatial table from an enterprise database."
                },
                "target_join_field": {
                        "type": "string",
                        "description": "The field in the target feature class on which the join will be based."
                },
                "related_table": {
                        "type": "string",
                        "description": "The input table containing the fields that will be used to calculate statistics.\r\n Statistics are joined to the out_layer value."
                },
                "related_join_field": {
                        "type": "string",
                        "description": "A field in the summary table that contains the values on which the\r\njoin will be based.\r\nAggregation or summary statistics are also calculated separately for each unique attribute value from this fiel..."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The output name of the query layer that will be created."
                },
                "statisticsstatistic_type_field": {
                        "type": "string",
                        "description": "Specifies the numeric field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values ar...",
                        "default": None
                },
                "oid_fields": {
                        "type": "string",
                        "description": "The unique identifier fields that will be used to\r\nuniquely identify each row in the table.",
                        "default": None
                },
                "shape_type": {
                        "type": "string",
                        "description": "Specifies the shape type of the query layer. Only those records from the result set of the query that match the specified shape type will be used in the output query layer. By default, the shape type ...",
                        "default": None
                },
                "srid": {
                        "type": "string",
                        "description": "The spatial reference identifier (SRID) value for queries that return geometry. Only those records from the result set of the query that match the specified SRID value will be used in the output query...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The coordinate system that will be used by the output query layer. \r\nBy default, the spatial reference of the first record in the result set will be used. This parameter is ignored if the result set o...",
                        "default": None
                },
                "m_values": {
                        "type": "string",
                        "description": "Specifies whether the output layer will include linear measurements (m-values).INCLUDE_M_VALUES\u2014The layer will include m-values.DO_NOT_INCLUDE_M_VALUES\u2014The layer will not include m-values. This is the...",
                        "default": None
                },
                "z_values": {
                        "type": "string",
                        "description": "Specifies whether the output layer will include elevation values (z-values).INCLUDE_Z_VALUES\u2014The layer will include z-values.DO_NOT_INCLUDE_Z_VALUES\u2014The layer will not include z-values. This is the de...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent of the layer.  The extent must include all features in the table.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPL...",
                        "default": None
                }
        },
        "required": [
                "target_feature_class",
                "target_join_field",
                "related_table",
                "related_join_field",
                "out_layer"
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
                        "default": None
                },
                "identifier": {
                        "type": "string",
                        "description": "A unique building identifier that will be added to all output feature classes. The identifier allows you to add unique names to each building to be used at a later time.",
                        "default": None
                },
                "include_floorplan": {
                        "type": "string",
                        "description": "Specifies whether the output dataset will include the floorplan feature classes.INCLUDE_FLOORPLAN\u2014The output dataset will include the floorplan feature classes. This is the default.EXCLUDE_FLOORPLAN\u2014T...",
                        "default": None
                }
        },
        "required": [
                "in_bim_file_workspace",
                "out_gdb_path",
                "out_dataset_name"
        ]
},
    "make_feature_layer": {
        "name": "make_feature_layer",
        "description": "Creates a feature layer from a feature class or layer file. The layer that is created is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which the new layer will be made. Complex feature classes, such as annotation and dimensions, are not valid inputs."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The name of the feature layer to be created. The layer can be used as input to any geoprocessing tool that accepts a feature layer as input."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of features.  For more information on SQL syntax  see the help topic SQL reference for query expressions used in ArcGIS.\r\n\r\nIf the input is a layer with an ex...",
                        "default": None
                },
                "workspace": {
                        "type": "string",
                        "description": "Legacy:This parameter is not used.In ArcGIS Desktop, output field names are validated based on this workspace. In ArcGIS Pro, this tool does not support changing the field names because layers do\r\nnot...",
                        "default": None
                },
                "field_info": {
                        "type": "string",
                        "description": "The fields from the input features that will be included in the output layer. You can remove input fields by making them not visible, and you can set numeric fields to have a ratio split policy. Renam...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_layer"
        ]
},
    "make_image_server_layer": {
        "name": "make_image_server_layer",
        "description": "Creates a temporary raster layer from an image service. The layer that is created will not persist after the session ends unless the document is saved. The input can also be a SOAP URL to an image server.",
        "parameters": {
                "out_imageserver_layer": {
                        "type": "string",
                        "description": "The name of the output image layer."
                },
                "template": {
                        "type": "string",
                        "description": "The output extent of the image layer.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equal to the visible display.Lay...",
                        "default": None
                },
                "band_indexid": {
                        "type": "string",
                        "description": "The bands that will be exported for the layer. If no bands are specified, all the bands will be used in the output.",
                        "default": None
                },
                "mosaic_method": {
                        "type": "string",
                        "description": "The mosaic method defines how the mosaic is created from different rasters.SEAMLINE\u2014Smooth transitions between images using seamlines.NORTH_WEST\u2014Display imagery that is closest to the northwest corner...",
                        "default": None
                },
                "order_field": {
                        "type": "string",
                        "description": "The default field to use to order the rasters when the mosaic method is By_Attribute. The list of fields is defined as those in the service table that are of type metadata and are integer (for example...",
                        "default": None
                },
                "order_base_value": {
                        "type": "string",
                        "description": "The images are sorted based on the difference between this input value and the attribute value in the specified field.",
                        "default": None
                },
                "lock_rasterid": {
                        "type": "string",
                        "description": "The raster ID or raster name to which the service should be locked, such that only the specified rasters are displayed. If left blank (undefined), it will be similar to the system default. Multiple ID...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size for the output image service layer.",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "Define a query using SQL.",
                        "default": None
                },
                "processing_template": {
                        "type": "string",
                        "description": "The raster function processing template that can be applied on the output image service layer.\r\nNone\u2014No processing template.",
                        "default": None
                }
        },
        "required": [
                "out_imageserver_layer"
        ]
},
    "make_las_dataset_layer": {
        "name": "make_las_dataset_layer",
        "description": "Creates a  LAS dataset layer that can apply  filters to LAS points and control the enforcement of surface constraint features.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset that will be processed."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The name of the resulting LAS dataset layer.\r\nA backslash or forward slash can be used to denote a group layer."
                },
                "class_code": {
                        "type": "string",
                        "description": "Specifies the classification codes that will be used to filter LAS points. All class codes will be selected by default.0\u2014Never processed by a classification method1\u2014Processed by a classification metho...",
                        "default": None
                },
                "return_values": {
                        "type": "string",
                        "description": "Specifies the ordinal pulse return values that will be used to filter LAS points. All returns will be used when no value is specified. Return information is only available for LAS point clouds collect...",
                        "default": None
                },
                "no_flag": {
                        "type": "string",
                        "description": "Specifies whether data points that do not have classification flags assigned will be included for display and analysis.INCLUDE_UNFLAGGED\u2014Unflagged points will be included. This is the default.EXCLUDE_...",
                        "default": None
                },
                "synthetic": {
                        "type": "string",
                        "description": "Specifies whether data points flagged as synthetic will be included. Synthetic points refer to LAS points that originated from a data source other than a lidar scanner.INCLUDE_SYNTHETIC\u2014Synthetic poin...",
                        "default": None
                },
                "keypoint": {
                        "type": "string",
                        "description": "Specifies whether data points flagged as model key points will be included. Model key points refer to LAS points that are significant for modeling the object they are associated with. INCLUDE_KEYPOINT...",
                        "default": None
                },
                "withheld": {
                        "type": "string",
                        "description": "Specifies whether data points flagged as withheld will be included. Withheld points represent erroneous or undesired measurements captured in the LAS points.INCLUDE_WITHHELD\u2014Withheld points will be in...",
                        "default": None
                },
                "surface_constraints": {
                        "type": "string",
                        "description": "The name of the surface constraint features that will be enabled in the layer. All constraints are enabled by default.",
                        "default": None
                },
                "overlap": {
                        "type": "string",
                        "description": "Specifies whether data points flagged as overlap will be included. Overlap points refer to points collected in overlapping scans that typically have a larger scan angle. Filtering overlap points can h...",
                        "default": None
                }
        },
        "required": [
                "in_las_dataset",
                "out_layer"
        ]
},
    "make_mosaic_layer": {
        "name": "make_mosaic_layer",
        "description": "Creates a  mosaic layer from a mosaic dataset or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved as a layer file or the map  is saved. This tool can be used to make a  layer so you can work with a specified subset of bands in a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The path and name of the input mosaic dataset."
                },
                "out_mosaic_layer": {
                        "type": "string",
                        "description": "The name of the  output mosaic layer."
                },
                "where_clause": {
                        "type": "string",
                        "description": "Define a query using SQL.",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "The output extent can be specified by defining the four coordinates or by using the extent of an existing layer.\r\nMAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to a...",
                        "default": None
                },
                "band_indexid": {
                        "type": "string",
                        "description": "The bands that will be exported for the layer. If no bands are specified, all the bands will be used in the output.",
                        "default": None
                },
                "mosaic_method": {
                        "type": "string",
                        "description": "Choose the mosaic method. The mosaic method defines how the layer is created\r\nfrom different rasters in the mosaic dataset.CLOSEST_TO_CENTER\u2014Sorts rasters based on an order where\r\nrasters that have th...",
                        "default": None
                },
                "order_field": {
                        "type": "string",
                        "description": "Choose the order field. When the mosaic method is BY_ATTRIBUTE, the default field to use when ordering rasters needs to be set. The list of fields is defined as those in the service table that are of ...",
                        "default": None
                },
                "order_base_value": {
                        "type": "string",
                        "description": "The order base value.\r\nThe images are sorted based on the difference between this value and the attribute value in the specified field.",
                        "default": None
                },
                "lock_rasterid": {
                        "type": "string",
                        "description": "The Raster ID or raster name to which the service should be locked so that only the specified rasters are displayed. If left undefined, it will be similar to the system default. Multiple IDs can be de...",
                        "default": None
                },
                "sort_order": {
                        "type": "string",
                        "description": "Choose whether the sort order is ascending or descending.\r\nASCENDING\u2014The sort order will be ascending. This is the default.DESCENDING\u2014The sort order will be descending.",
                        "default": None
                },
                "mosaic_operator": {
                        "type": "string",
                        "description": "Choose the mosaic operator to use. When two or more rasters have the same sort priority, this parameter is used to further refine the sort order.FIRST\u2014The first raster in the list will be on top. This...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output mosaic layer.",
                        "default": None
                },
                "processing_template": {
                        "type": "string",
                        "description": "The raster function processing template that can be applied on the output mosaic layer.\r\nNone\u2014No processing template.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "out_mosaic_layer"
        ]
},
    "make_query_layer": {
        "name": "make_query_layer",
        "description": "Creates a query layer  from a DBMS table based on an input SQL select statement.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The database connection file that contains the data to be queried."
                },
                "out_layer_name": {
                        "type": "string",
                        "description": "The output name of the feature layer or table view to be created."
                },
                "query": {
                        "type": "string",
                        "description": "The SQL statement that defines the select query to be issued to the database."
                },
                "oid_fields": {
                        "type": "string",
                        "description": "One or more fields from the SELECT statement SELECT list that will generate a dynamic, unique row identifier.",
                        "default": None
                },
                "shape_type": {
                        "type": "string",
                        "description": "Specifies the shape type of the query layer. Only those records from the result set of the query that match the specified shape type will be used in the output query layer. Tool validation will attemp...",
                        "default": None
                },
                "srid": {
                        "type": "string",
                        "description": "The spatial reference identifier (SRID) value for queries that return geometry. Only those records from the result set of the query that match the specified SRID value will be used in the output query...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The coordinate system that will be used by the output query layer. \r\nTool validation will attempt to set this property based on the first record in the result set. This can be changed before running t...",
                        "default": None
                },
                "spatial_properties": {
                        "type": "string",
                        "description": "Specifies how the spatial properties for the layer will be defined.\r\n During the validation process, dimensionality, geometry type, spatial reference, SRID, and unique\r\nidentifier properties will be s...",
                        "default": None
                },
                "m_values": {
                        "type": "string",
                        "description": "Specifies whether the layer will have  m-values.INCLUDE_M_VALUES\u2014The layer will have m-values.DO_NOT_INCLUDE_M_VALUES\u2014The layer will not have m-values. This is the default.",
                        "default": None
                },
                "z_values": {
                        "type": "string",
                        "description": "Specifies whether the layer will have z-values.INCLUDE_Z_VALUES\u2014The layer will have z-values.DO_NOT_INCLUDE_Z_VALUES\u2014The layer will not have z-values. This is the default.",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "The extent of the layer. This parameter is only used if the Define the spatial properties of the\r\nlayer parameter is checked (spatial_properties = DEFINE_SPATIAL_PROPERTIES in Python). The extent must...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "out_layer_name",
                "query"
        ]
},
    "make_query_table": {
        "name": "make_query_table",
        "description": "Applies an SQL query to a database, and the results are represented in either a layer or table view. The query can be used to join several tables or return a subset of fields or rows from the original data in the database. This tool accepts data from a geodatabase or an OLE DB connection.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The name of the table or tables to be used in the query. If several tables are listed, the where_clause parameter can be used to define how they will be joined.The input table can be from a geodatabas..."
                },
                "out_table": {
                        "type": "string",
                        "description": "The name of the layer or table view that will be created."
                },
                "in_key_field_option": {
                        "type": "string",
                        "description": "Specifies how an Object ID field will be generated (if at all) for the query.  Layers and table views in  ArcGIS require an Object ID field. An Object ID field is an integer field that uniquely identi..."
                },
                "in_key_field": {
                        "type": "string",
                        "description": "A field or combination of fields that will be used to uniquely identify a row in the query. This parameter is used only when the in_key_field_option parameter is set to  USE_KEY_FIELDS.",
                        "default": None
                },
                "in_field_alias": {
                        "type": "string",
                        "description": "The fields that will be included in the layer or table view. If an alias is set for a field, this is the name that appears. If no fields are specified, all fields from all tables are included. If a Sh...",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of records.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_table",
                "in_key_field_option"
        ]
},
    "make_raster_layer": {
        "name": "make_raster_layer",
        "description": "Creates a raster layer from an input raster dataset or layer file. The layer created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved. This tool can be used to make a temporary layer, so you can work with a specified subset of bands within a raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The path and name of the input raster dataset.You can use a raster layer from  a GeoPackage as the input. To reference a raster within a GeoPackage, type the name of the path, followed by the name of ..."
                },
                "out_rasterlayer": {
                        "type": "string",
                        "description": "The name of the layer to create."
                },
                "where_clause": {
                        "type": "string",
                        "description": "Define a query using SQL.",
                        "default": None
                },
                "envelope": {
                        "type": "string",
                        "description": "The output extent can be specified by defining the four coordinates or by using the extent of an existing layer.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all...",
                        "default": None
                },
                "band_index": {
                        "type": "string",
                        "description": "The bands that will be exported for the layer. If no bands are specified, all the bands will be used in the output.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_rasterlayer"
        ]
},
    "make_scene_layer": {
        "name": "make_scene_layer",
        "description": "Creates a scene layer from a scene layer package (.slpk) or scene service.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input scene layer package (.slpk) or scene service from which the new scene layer will be created."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The name of the scene layer to be created."
                }
        },
        "required": [
                "in_dataset",
                "out_layer"
        ]
},
    "make_table_view": {
        "name": "make_table_view",
        "description": "Creates a table view from an input table or feature class. The table view that is created is temporary and will not persist after the session ends unless the document is saved.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table or feature class."
                },
                "out_view": {
                        "type": "string",
                        "description": "The name of the table view to be created."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of features.  For more information on SQL syntax  see the help topic SQL reference for query expressions used in ArcGIS.",
                        "default": None
                },
                "workspace": {
                        "type": "string",
                        "description": "This parameter is not used.In ArcGIS Desktop, output field names are validated based on this workspace. In ArcGIS Pro, this tool does not support changing the field names because table views do\r\nnot s...",
                        "default": None
                },
                "field_info": {
                        "type": "string",
                        "description": "The fields from the input table that will be included in the output layer. You can remove input fields by setting them to not visible. Renaming fields and the use of split policies are not supported.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_view"
        ]
},
    "make_tin_layer": {
        "name": "make_tin_layer",
        "description": "Creates a triangulated irregular network (TIN) layer from an input TIN dataset or layer file. The layer that is created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.",
        "parameters": {
                "in_tin": {
                        "type": "string",
                        "description": "The input TIN dataset or layer from which the new layer will be created."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The name\r\nof the TIN layer to be created. The output layer can be used as an input to any geoprocessing tool that accepts a TIN layer as input."
                }
        },
        "required": [
                "in_tin",
                "out_layer"
        ]
},
    "make_wcs_layer": {
        "name": "make_wcs_layer",
        "description": "Creates a temporary raster layer from a WCS service.",
        "parameters": {
                "out_wcs_layer": {
                        "type": "string",
                        "description": "The name of the output WCS layer."
                },
                "template": {
                        "type": "string",
                        "description": "The output extent of the WCS layer.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equal to the visible display.Layer...",
                        "default": None
                },
                "band_index": {
                        "type": "string",
                        "description": "The bands that will be exported for the layer. If no bands are specified, all the bands will be used in the output.",
                        "default": None
                }
        },
        "required": [
                "out_wcs_layer"
        ]
},
    "make_xy_event_layer": {
        "name": "make_xy_event_layer",
        "description": "Creates a point event layer from  a table containing fields with x- and y-coordinate values, and optionally, z-coordinate (elevation) values.",
        "parameters": {
                "table": {
                        "type": "string",
                        "description": "The table containing the x- and y-coordinates that define the locations of the point features that will be created."
                },
                "in_x_field": {
                        "type": "string",
                        "description": "The field in the input table that contains the x-coordinates (longitude)."
                },
                "in_y_field": {
                        "type": "string",
                        "description": "The field in the input table that contains the y-coordinates (latitude)."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The name of the output event layer."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The coordinate system  of the coordinates specified in the in_x_field and in_y_field parameters. This will be the output event layer's coordinate system.",
                        "default": None
                },
                "in_z_field": {
                        "type": "string",
                        "description": "The field in the input table that contains the z-coordinates.",
                        "default": None
                }
        },
        "required": [
                "table",
                "in_x_field",
                "in_y_field",
                "out_layer"
        ]
},
    "match_layer_symbology_to_a_style": {
        "name": "match_layer_symbology_to_a_style",
        "description": "Creates unique value symbology for the input layer based on the input field or expression by matching input field or expression strings to symbol names from the input style.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The input layer or layer file to which matched symbols are applied as unique values symbol classes.\r\nThe input layer can contain point, line, polygon, multipoint, or multipatch symbology. Existing sym..."
                },
                "match_values": {
                        "type": "string",
                        "description": "The field or expression on which the input layer is symbolized. The field values or resultant expression values are matched to symbol names in the specified style to assign symbols to the resulting sy..."
                },
                "in_style": {
                        "type": "string",
                        "description": "The style containing symbols with names matching the field or expression values."
                }
        },
        "required": [
                "in_layer",
                "match_values",
                "in_style"
        ]
},
    "save_to_layer_file": {
        "name": "save_to_layer_file",
        "description": "Creates an output layer file (.lyrx) from a map layer. The layer file stores many properties of the input layer such as symbology, labeling, and custom pop-ups.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The map layer that will be saved to disk as a layer file."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The output layer file (.lyrx) that will be created."
                },
                "is_relative_path": {
                        "type": "string",
                        "description": "Specifies whether the output layer  file will store a relative path to the source data stored on disk or an absolute path.\r\nABSOLUTE\u2014The output layer file will store an absolute path to the source dat...",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "Specifies the version of the output layer file. \r\nLegacy: This parameter is no longer supported. It remains only for the backward compatibility of scripts and models.Layer files created in a particula...",
                        "default": None
                }
        },
        "required": [
                "in_layer",
                "out_layer"
        ]
},
    "select_layer_by_attribute": {
        "name": "select_layer_by_attribute",
        "description": "Adds, updates, or removes a selection based on an attribute query.",
        "parameters": {
                "in_layer_or_view": {
                        "type": "string",
                        "description": "The data to which the selection will be applied."
                },
                "selection_type": {
                        "type": "string",
                        "description": "Specifies how the selection will be applied and what to do if a selection already exists.NEW_SELECTION\u2014The resulting selection will replace the current selection. This is the default. ADD_TO_SELECTION...",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of records.",
                        "default": None
                },
                "invert_where_clause": {
                        "type": "string",
                        "description": "Specifies whether the expression will be used as is, or the opposite of the expression will be used.NON_INVERT\u2014The query will be used as is. This is the default.INVERT\u2014The opposite of the query will b...",
                        "default": None
                }
        },
        "required": [
                "in_layer_or_view"
        ]
},
    "select_layer_by_location": {
        "name": "select_layer_by_location",
        "description": "Selects features  based on a spatial relationship to features in another dataset or the same dataset. Each feature in the Input Features parameter is evaluated using the features in the  Selecting Features parameter. If the specified Relationship parameter value is met, the input feature is selected. Learn more about Select By Location including image examples of relationships",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The features that will be evaluated using the select_features parameter values.  The selection will be applied to these features."
                },
                "overlap_type": {
                        "type": "string",
                        "description": "Specifies the spatial relationship that will be evaluated.INTERSECT\u2014The features in the input layer will be selected if they intersect a selecting feature. This is the default. INTERSECT_3D\u2014The featur...",
                        "default": None
                },
                "select_features": {
                        "type": "string",
                        "description": "The features in the Input Features parameter will be selected based on their relationship to the features from this layer or feature class.",
                        "default": None
                },
                "search_distance": {
                        "type": "string",
                        "description": "The distance that will be searched. This parameter is only valid if the overlap_type  parameter is set to INTERSECT, INTERSECT_3D, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_3D, WITHIN_A_DISTANCE_GEODESIC, ...",
                        "default": None
                },
                "selection_type": {
                        "type": "string",
                        "description": "Specifies how the selection will be applied to the input and how it will be combined with an existing selection.  This tool does not include an option to clear an existing selection; use the  Select L...",
                        "default": None
                },
                "invert_spatial_relationship": {
                        "type": "string",
                        "description": "Specifies whether the spatial relationship evaluation result or the opposite result will be used.  For example, this parameter can be used to get a list of features that do not intersect or are not wi...",
                        "default": None
                }
        },
        "required": [
                "in_layer"
        ]
},
    "share_package": {
        "name": "share_package",
        "description": "Shares a package by uploading it to ArcGIS Online or ArcGIS Enterprise.",
        "parameters": {
                "in_package": {
                        "type": "string",
                        "description": "The input layer (.lpk or .lpkx), scene layer (.slpk), map (.mpk or .mpkx), geoprocessing (.gpk or .gpkx), tile (.tpk or .tpkx),  mobile map (.mmpk), vector tile (.vtpk), address locator (.gcpk), or pr..."
                },
                "username": {
                        "type": "string",
                        "description": "The ArcGIS Online or ArcGIS Enterprise username.\r\nThis parameter has been deprecated and should consist of an empty string. Before running the Python script, you must sign in to the active portal from..."
                },
                "password": {
                        "type": "string",
                        "description": "The\r\nArcGIS Online or ArcGIS Enterprise password. This parameter has been deprecated and should consist of an empty string.\r\nBefore running the Python script, you must sign in to the active portal fro..."
                },
                "summary": {
                        "type": "string",
                        "description": "The summary of  the package.  The summary is displayed in the item information of the package on ArcGIS Online or ArcGIS Enterprise.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tags used to describe and identify the  package.  Separate multiple tags with a comma.",
                        "default": None
                },
                "credits": {
                        "type": "string",
                        "description": "The credits for the package. This is generally the name of the organization that is given credit for authoring and providing the content for the package.",
                        "default": None
                },
                "public": {
                        "type": "string",
                        "description": "Specifies whether the input package will be shared  with and available to the public. EVERYBODY\u2014 The input package will be shared with the public. Anyone can access and see it. MYGROUPS\u2014  The input pa...",
                        "default": None
                },
                "groupsgroup_name": {
                        "type": "string",
                        "description": "The  groups the package will be shared with.",
                        "default": None
                },
                "organization": {
                        "type": "string",
                        "description": "Specifies whether the input package will be available within your organization only or shared publicly with everyone.\r\nEVERYBODY\u2014 The package will be shared with the public. Anyone can access and see ...",
                        "default": None
                },
                "publish_web_layer": {
                        "type": "string",
                        "description": "Specifies whether the package will be published as a web layer to your portal. Only tile packages, vector tile packages, and scene layer packages are supported.FALSE\u2014The package will be uploaded witho...",
                        "default": None
                },
                "portal_folder": {
                        "type": "string",
                        "description": "An existing folder or the name of a new folder on the portal for the package. If a web layer is published, it is stored in this folder.",
                        "default": None
                }
        },
        "required": [
                "in_package",
                "username",
                "password"
        ]
},
    "consolidate_layer": {
        "name": "consolidate_layer",
        "description": "Consolidates one or more layers by copying all referenced data sources  into a single folder.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The input layers that will be consolidated."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder that will contain the layer files and consolidated data.  If the specified folder does not exist, a new folder will be created."
                },
                "convert_data": {
                        "type": "string",
                        "description": "Specifies whether input layers will be converted to a file geodatabase or preserved in their original format.CONVERT\u2014 Data will be converted to a file geodatabase. This option does not apply to enterp...",
                        "default": None
                },
                "convert_arcsde_data": {
                        "type": "string",
                        "description": "Specifies whether input enterprise geodatabase layers will be converted to a file geodatabase or preserved in their original format. CONVERT_ARCSDE\u2014 Enterprise geodatabase data will be converted to a ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_arcsde": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The specified extent will be applied to all layers. This is the default.ARCSDE_ONLY\u2014T...",
                        "default": None
                },
                "schema_only": {
                        "type": "string",
                        "description": "Specifies whether only the schema of the input layers will be consolidated or packaged.ALL\u2014 All features and records will be consolidated or packaged. This is the default.SCHEMA_ONLY\u2014 Only the schema ...",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "preserve_sqlite": {
                        "type": "string",
                        "description": "Specifies whether mobile geodatabase data will be preserved in the output or written to file geodatabase format. If the input data is a mobile geodatabase network dataset, the output will be a mobile ...",
                        "default": None
                },
                "exclude_network_dataset": {
                        "type": "string",
                        "description": "For network analysis layers, specifies whether the network dataset will also be consolidated.INCLUDE_NETWORK_DATASET\u2014The network dataset will be included and consolidated. This is the default.EXCLUDE_...",
                        "default": None
                }
        },
        "required": [
                "in_layer",
                "output_folder"
        ]
},
    "consolidate_locator": {
        "name": "consolidate_locator",
        "description": "Consolidate a locator or composite locator  by copying all locators into a single folder.",
        "parameters": {
                "in_locator": {
                        "type": "string",
                        "description": "The input locator or composite locator  that will be consolidated."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder that will contain the consolidated locator or composite locator with its participating locators. \r\n If the specified folder does not exist, a new folder will be created."
                },
                "copy_arcsde_locator": {
                        "type": "string",
                        "description": "This parameter has no effect in ArcGIS Pro.  It remains only to support backward compatibility.",
                        "default": None
                }
        },
        "required": [
                "in_locator",
                "output_folder"
        ]
},
    "consolidate_map": {
        "name": "consolidate_map",
        "description": "Consolidates a map and all referenced data sources to a specified output folder.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The map (.mapx file) that will be consolidated.  When running this tool in  ArcGIS Pro, the input can be a map, scene, or basemap."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder that will contain the consolidated map  and data. If the specified folder does not exist, a folder will be created."
                },
                "convert_data": {
                        "type": "string",
                        "description": "Specifies whether input layers will be converted to a file geodatabase or preserved in their original format.CONVERT\u2014 Data will be converted to a file geodatabase. This option does not apply to enterp...",
                        "default": None
                },
                "convert_arcsde_data": {
                        "type": "string",
                        "description": "Specifies whether input enterprise geodatabase layers will be converted to a file geodatabase or preserved in their original format. CONVERT_ARCSDE\u2014 Enterprise geodatabase data will be converted to a ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_arcsde": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The specified extent will be applied to all layers. This is the default.ARCSDE_ONLY\u2014T...",
                        "default": None
                },
                "preserve_sqlite": {
                        "type": "string",
                        "description": "Specifies whether input mobile geodatabase data will be preserved as mobile geodatabase in the output. If the input data is a mobile geodatabase network dataset, the output will always be mobile geoda...",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "consolidate_to_one_fgdb": {
                        "type": "string",
                        "description": "Specifies whether map layers will be consolidated to a single file geodatabase or to multiple file geodatabases based on the number of unique data sources in the input map.SINGLE_OUTPUT_WORKSPACE\u2014All ...",
                        "default": None
                }
        },
        "required": [
                "in_map",
                "output_folder"
        ]
},
    "consolidate_project": {
        "name": "consolidate_project",
        "description": "Consolidates an ArcGIS Pro project (.aprx file) and referenced maps and data into a folder.",
        "parameters": {
                "in_project": {
                        "type": "string",
                        "description": "The project (.aprx file) that will be consolidated."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder that will contain the consolidated project and data.\r\n If the specified folder does not exist, a folder will be created."
                },
                "sharing_internal": {
                        "type": "string",
                        "description": "Specifies whether the project and all data will be consolidated into a single folder (for sharing outside your organization) or  referenced to network data (for sharing within your organization).INTER...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_enterprise_geo": {
                        "type": "string",
                        "description": "Specifies whether the extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The extent will be applied to all layers. This is the default.ENTERPRISE_ONLY\u2014The extent will b...",
                        "default": None
                },
                "package_as_template": {
                        "type": "string",
                        "description": "Specifies whether the project\r\nwill be consolidated as a template or a regular project. Templates can include maps, layouts, connections to databases and servers, and so on.  A project template allows...",
                        "default": None
                },
                "preserve_sqlite": {
                        "type": "string",
                        "description": "Specifies whether mobile geodatabases will be preserved or converted to file geodatabases.Note:This parameter applies only to mobile geodatabases (.geodatabase) used primarily for offline workflows in...",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "Specifies the ArcGIS Pro version to which objects such as projects, maps, and layers will be persisted. Saving to an earlier version  is useful if the project will be used with earlier versions of Arc...",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                }
        },
        "required": [
                "in_project",
                "output_folder"
        ]
},
    "create_map_tile_package": {
        "name": "create_map_tile_package",
        "description": "Generates tiles from a map and packages them as a single tile package or multiple smaller tile packages.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The map from which tiles will be generated and packaged."
                },
                "service_type": {
                        "type": "string",
                        "description": "Specifies whether the tiling scheme will be generated from  an existing map service or whether map tiles will be generated for ArcGIS Online, Bing Maps, and Google Maps.\r\nEXISTING\u2014A tiling scheme from..."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output path and file name for the map tile package."
                },
                "format_type": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the generated tiles.PNG\u2014The correct format (PNG 8, PNG 24, or PNG 32) will be used based on the specified Maximum Level Of Detail parameter value. This is th..."
                },
                "level_of_detail": {
                        "type": "string",
                        "description": "The integer representation corresponding to the number of scales used to define a cache tiling scheme. This scale value defines the maximum level up to which the cache tiles will be generated in the t..."
                },
                "service_file": {
                        "type": "string",
                        "description": "The name of the map service or the .xml files that will be used for the tiling scheme. This parameter is required only when the \r\n service_type parameter is set to EXISTING.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The summary information that will be added to the properties of the package.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be added to the properties of the package. Multiple tags can be added, separated by a comma or semicolon.",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "A value between 1 and 100 for the JPEG compression quality. The\r\ndefault value is 75 for JPEG tile format and zero for other\r\nformats.Compression is supported only for JPEG and mixed formats. A higher...",
                        "default": None
                },
                "package_type": {
                        "type": "string",
                        "description": "Specifies the type of tile package that will be created.\r\ntpk\u2014A  .tpk file will be created. Tiles will be stored using Compact storage format. This format is supported across ArcGIS.tpkx\u2014A .tpkx file ...",
                        "default": None
                },
                "min_level_of_detail": {
                        "type": "string",
                        "description": "The integer representation corresponding to the number of scales used to define a cache tiling scheme. This scale value defines the level at which the cache tiles begin to be available and generated i...",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "A feature set that constrains where tiles will be created. Use an area of interest to create  tiles for irregularly shaped areas or multipart features. The areas outside the bounding box of area of in...",
                        "default": None
                },
                "create_multiple_packages": {
                        "type": "string",
                        "description": "Specifies whether a single large tile package or multiple small tile packages will be generated. This parameter is not available when the parallelProcessingFactor  environment variable is 0 or when th...",
                        "default": None
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder where the multiple tile packages will be generated. If the output folder is not empty, a subfolder will be created in the output folder to store the tiles. An automatically generated..."
                }
        },
        "required": [
                "in_map",
                "service_type",
                "output_file",
                "format_type",
                "level_of_detail",
                "output_folder"
        ]
},
    "create_mobile_map_package": {
        "name": "create_mobile_map_package",
        "description": "Packages maps and basemaps along with all referenced data sources into a single .mmpk file.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "One or more maps or basemaps that will be packaged into a single .mmpk file."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output mobile map package (.mmpk)."
                },
                "in_locator": {
                        "type": "string",
                        "description": "One or more locators (.loc) that will be included in the mobile map package.Note:Locators have the following restrictions:The locator cannot have an unknown coordinate system.The locator or any partic...",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "A polygon layer that defines the AOI. Only those features that intersect this value will be included in the mobile map package.",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "clip_features": {
                        "type": "string",
                        "description": "Specifies whether the geometry of the output features will be clipped to the specified area_of_interest or extent parameter value, or remain unaltered.CLIP\u2014The geometry of the features will be clipped...",
                        "default": None
                },
                "title": {
                        "type": "string",
                        "description": "The title information that will be added to the properties of the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The text that will be used as the output package's summary property.",
                        "default": None
                },
                "description": {
                        "type": "string",
                        "description": "The description information that will be added to the properties of the package.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be added to the properties of the package. Multiple tags can be added, separated by a comma or semicolon.",
                        "default": None
                },
                "credits": {
                        "type": "string",
                        "description": "The credit information that will be added to the properties of the package.",
                        "default": None
                },
                "use_limitations": {
                        "type": "string",
                        "description": "The use limitations that will be added to the properties of the package.",
                        "default": None
                },
                "enable_map_expiration": {
                        "type": "string",
                        "description": "Specifies whether a time-out will be enabled on the mobile map package.ENABLE_MAP_EXPIRATION\u2014A time-out will be enabled on the mobile map package.DISABLE_MAP_EXPIRATION\u2014A time-out will not be enabled ...",
                        "default": None
                },
                "map_expiration_type": {
                        "type": "string",
                        "description": "Specifies the type of access a user will have to the expired mobile map package.ALLOW_TO_OPEN\u2014A user of the package will be warned that the map has expired but will be allowed to open it. This is the ...",
                        "default": None
                },
                "expiration_date": {
                        "type": "string",
                        "description": "The date the mobile map package will expire.License:This optional parameter is only available with the Publisher extension.",
                        "default": None
                },
                "expiration_message": {
                        "type": "string",
                        "description": "A text message that will display when an expired map is accessed.\r\nLicense:This optional parameter is only available with the Publisher extension.",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "reference_online_content": {
                        "type": "string",
                        "description": "Specifies whether service layers will be referenced in the package.INCLUDE_SERVICE_LAYERS\u2014Service layers will be referenced in the mobile package.EXCLUDE_SERVICE_LAYERS\u2014Service layers will not be refe...",
                        "default": None
                }
        },
        "required": [
                "in_map",
                "output_file"
        ]
},
    "create_mobile_scene_package": {
        "name": "create_mobile_scene_package",
        "description": "Creates a mobile scene package file (.mspk) from one or more scenes for use across the ArcGIS system.",
        "parameters": {
                "in_scene": {
                        "type": "string",
                        "description": "One or more local or global scenes that will be packaged into a single .mspk file. Active scenes and .mapx files can be added as input."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output mobile scene package .mspk file."
                },
                "in_locator": {
                        "type": "string",
                        "description": "One or more locators (.loc file) that will be included in the mobile scene package.\r\nNote:Locators have the following restrictions:The locator cannot have an unknown coordinate system.The locator or a...",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "A polygon layer that defines the area of interest. Only those features that intersect the area of interest will be included in the mobile scene package.",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "clip_features": {
                        "type": "string",
                        "description": "Specifies whether the output features will be clipped to the given area of interest or extent.\r\nChecked\u2014The geometry of the features will be clipped to the given area of interest or extent.Unchecked\u2014F...",
                        "default": None
                },
                "title": {
                        "type": "string",
                        "description": "Title information that will be added to the properties of the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "Summary information that will be added to the properties of the package.",
                        "default": None
                },
                "description": {
                        "type": "string",
                        "description": "Description information that will be added to the properties of the package.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "Tag information that will be added to the properties of the package. Multiple\r\ntags can be added, separated by a comma or semicolon.",
                        "default": None
                },
                "credits": {
                        "type": "string",
                        "description": "Credit information that will be added to the properties of the package.",
                        "default": None
                },
                "use_limitations": {
                        "type": "string",
                        "description": "Use limitations that will be added to the properties of the package.",
                        "default": None
                },
                "anonymous_use": {
                        "type": "string",
                        "description": "Specifies whether the mobile scenes can be used by anyone or only those with an ArcGIS account.ANONYMOUS_USE\u2014Anyone with access to the package can use the mobile scene without signing in with an Esri ...",
                        "default": None
                },
                "texture_optimization": {
                        "type": "string",
                        "description": "Specifies the textures that will be optimized according to the target platform where the scene layer package is used.Caution:Optimizations that include KTX2 may take significant time to process. For f...",
                        "default": None
                },
                "enable_scene_expiration": {
                        "type": "string",
                        "description": "Specifies whether the mobile scene package will time out.ENABLE_SCENE_EXPIRATION\u2014Time-out functionality will be enabled on the mobile scene package.DISABLE_SCENE_EXPIRATION\u2014Time-out functionality will...",
                        "default": None
                },
                "scene_expiration_type": {
                        "type": "string",
                        "description": "Specifies the type of scene access that will be used for the expired mobile scene package.ALLOW_TO_OPEN\u2014The user of the package will be warned that the scene has expired and allowed to open the scene....",
                        "default": None
                },
                "expiration_date": {
                        "type": "string",
                        "description": "The date the mobile scene package will expire.License:This optional parameter is only available with the Publisher extension.",
                        "default": None
                },
                "expiration_message": {
                        "type": "string",
                        "description": "The text message that will appear when an expired scene is accessed.\r\nLicense:This optional parameter is only available with the Publisher extension.",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "reference_online_content": {
                        "type": "string",
                        "description": "Specifies whether service layers will be referenced in the package.INCLUDE_SERVICE_LAYERS\u2014Service layers will be referenced in the mobile package.EXCLUDE_SERVICE_LAYERS\u2014Service layers will not be refe...",
                        "default": None
                }
        },
        "required": [
                "in_scene",
                "output_file"
        ]
},
    "create_vector_tile_index": {
        "name": "create_vector_tile_index",
        "description": "Creates a multiscale mesh of polygons that can be used as index polygons when creating vector tile packages.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The input map with the feature distribution and vertex density that determine \r\nthe size and arrangement of output polygons. The input map is typically one that you will subsequently use to create vec..."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The output polygon feature class of indexed tiles at each level of detail. \r\nEach tile encloses a manageable number of input vertices not exceeding the number specified by the vertex_count  parameter."
                },
                "service_type": {
                        "type": "string",
                        "description": "Specifies whether the tiling scheme will be generated from an existing map service or for ArcGIS Online, Bing Maps, and Google Maps. \r\n ONLINE\u2014The ArcGIS Online/Bing Maps/Google Maps tiling scheme wil..."
                },
                "tiling_scheme": {
                        "type": "string",
                        "description": "The vector tile service or tiling scheme file that will be used if  the service_type parameter is set to EXISTING. \r\n The tiling scheme tile size must be 512 by 512 and must have consecutive scales in...",
                        "default": None
                },
                "vertex_count": {
                        "type": "string",
                        "description": "The ideal number of vertices from all visible layers to be enclosed by each polygon in the output feature class. The default value is the recommended count of 10,000 vertices.",
                        "default": None
                }
        },
        "required": [
                "in_map",
                "out_featureclass",
                "service_type"
        ]
},
    "create_vector_tile_package": {
        "name": "create_vector_tile_package",
        "description": "Generates vector tiles from a map or basemap and packages the tiles in a single .vtpk file.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The map from which tiles will be  generated and packaged. The input map must have  metadata description and tags."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output vector tile package. The file extension of the package will be .vtpk."
                },
                "service_type": {
                        "type": "string",
                        "description": "Specifies whether the tiling scheme will be generated from an existing map service or if map tiles will be generated for ArcGIS Online, Bing Maps, and Google Maps. \r\n ONLINE\u2014The ArcGIS Online/Bing Map..."
                },
                "tiling_scheme": {
                        "type": "string",
                        "description": "A vector tile service or tiling scheme file that will be used if  the service_type parameter is set to EXISTING. \r\n The tiling scheme tile size must be 512 by 512 and must have consecutive scales in a...",
                        "default": None
                },
                "tile_structure": {
                        "type": "string",
                        "description": "Specifies whether the tile generation structure will be optimized with an indexed structure or  as a flat array of all tiles at all levels of detail. The optimized indexed structure is the default and...",
                        "default": None
                },
                "min_cached_scale": {
                        "type": "string",
                        "description": "The minimum (smallest) scale at which tiles will be generated. This does not need to be the smallest scale in the tiling scheme.\r\nThe minimum cached scale determines which scales will be used to gener...",
                        "default": None
                },
                "max_cached_scale": {
                        "type": "string",
                        "description": "The maximum (largest) scale at which tiles will be generated. This does not need to be the largest scale in the tiling scheme.\r\nThe maximum cached scale determines which scales will be used to generat...",
                        "default": None
                },
                "index_polygons": {
                        "type": "string",
                        "description": "An index of tiles based on feature density.Use the Create Vector Tile Index tool to create index polygons. If no index polygons are specified for this parameter, optimized index polygons will be gener...",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The summary information that will be added to properties of the output vector tile package.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be  added to the properties of the output vector tile package. \r\nSeparate multiple tags with commas or semicolons.",
                        "default": None
                }
        },
        "required": [
                "in_map",
                "output_file",
                "service_type"
        ]
},
    "extract_package": {
        "name": "extract_package",
        "description": "Extracts the contents of a package to a specified folder. The output folder will be  updated with the extracted contents of the input package.",
        "parameters": {
                "in_package": {
                        "type": "string",
                        "description": "The input package that will be extracted."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The output folder that will contain the contents of the package.\r\n If the specified folder does not exist, a folder will be created.",
                        "default": None
                },
                "cache_package": {
                        "type": "string",
                        "description": "Specifies whether a copy of the package will be cached to your profile. When extracting a package, the output is first extracted to your user profile and appended with a unique ID before a copy is mad...",
                        "default": None
                },
                "storage_format_type": {
                        "type": "string",
                        "description": "Specifies the storage format that will be used for the extracted cache.\r\nThis parameter is applicable only when the input package is a \r\nvector tile  package (.vtpk).COMPACT\u2014 The tiles will be grouped...",
                        "default": None
                },
                "create_ready_to_serve_format": {
                        "type": "string",
                        "description": "Specifies whether a ready-to-serve format for ArcGIS Enterprise will be created. This parameter is enabled only  when the input package is a \r\nvector tile  package (.vtpk) or a tile  package (.tpkx).R...",
                        "default": None
                },
                "target_cloud_connection": {
                        "type": "string",
                        "description": "The target .acs file to which the package contents will be extracted. This parameter is enabled only  when the input package is a scene layer package (.slpk),  \r\na vector tile  package (.vtpk), or a t...",
                        "default": None
                }
        },
        "required": [
                "in_package"
        ]
},
    "package_3d_tiles": {
        "name": "package_3d_tiles",
        "description": "Packages a 3D tiles layer or folder of 3D tiles content into a 3D tiles archive file.",
        "parameters": {
                "in_3dtiles": {
                        "type": "string",
                        "description": "The input 3D tiles layer or folder."
                },
                "out_file": {
                        "type": "string",
                        "description": "The output 3D tiles archive file."
                }
        },
        "required": [
                "in_3dtiles",
                "out_file"
        ]
},
    "package_layer": {
        "name": "package_layer",
        "description": "Packages one or more layers and all referenced data sources to create a single compressed .lpkx file.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The  layers that will be packaged."
                },
                "output_file": {
                        "type": "string",
                        "description": "The location and name of the output package file (.lpkx) that will be created."
                },
                "convert_data": {
                        "type": "string",
                        "description": "Specifies whether input layers will be converted to a file geodatabase or preserved in their original format.CONVERT\u2014 Data will be converted to a file geodatabase. This option does not apply to enterp...",
                        "default": None
                },
                "convert_arcsde_data": {
                        "type": "string",
                        "description": "Specifies whether input enterprise geodatabase layers will be converted to a file geodatabase or preserved in their original format. CONVERT_ARCSDE\u2014 Enterprise geodatabase data will be converted to a ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_arcsde": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The specified extent will be applied to all layers. This is the default.ARCSDE_ONLY\u2014T...",
                        "default": None
                },
                "schema_only": {
                        "type": "string",
                        "description": "Specifies whether only the schema of the input layers will be consolidated or packaged.ALL\u2014 All features and records will be consolidated or packaged. This is the default.SCHEMA_ONLY\u2014 Only the schema ...",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "Specifies the ArcGIS Pro version the layer files will be compatible with and persisted to. Certain objects such as projects,\r\n maps, and layers can be persisted to a specific version. Saving to an ear...",
                        "default": None
                },
                "additional_files": {
                        "type": "string",
                        "description": "The additional files that will be included in the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The text that will be used as the output package's summary property.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be added to the properties of the package. Multiple tags can be added, separated by a comma or semicolon.",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "preserve_sqlite": {
                        "type": "string",
                        "description": "Specifies whether mobile geodatabase data will be preserved in the output or written to file geodatabase format. If the input data is a mobile geodatabase network dataset, the output will be a mobile ...",
                        "default": None
                },
                "exclude_network_dataset": {
                        "type": "string",
                        "description": "For network analysis layers, specifies whether the network dataset will also be packaged.INCLUDE_NETWORK_DATASET\u2014The network dataset will be included and packaged. This is the default.EXCLUDE_NETWORK_...",
                        "default": None
                }
        },
        "required": [
                "in_layer",
                "output_file"
        ]
},
    "package_locator": {
        "name": "package_locator",
        "description": "Packages a locator or composite locator  and creates a single compressed .gcpk file. Learn more about sharing an address locator as a locator package",
        "parameters": {
                "in_locator": {
                        "type": "string",
                        "description": "The locator or composite locator that will be packaged."
                },
                "output_file": {
                        "type": "string",
                        "description": "The name and location of the output locator package (.gcpk)."
                },
                "copy_arcsde_locator": {
                        "type": "string",
                        "description": "This parameter has no effect in ArcGIS Pro.  It remains only to support backward compatibility.",
                        "default": None
                },
                "additional_files": {
                        "type": "string",
                        "description": "The additional files that will be included in the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The text that will be used as the output package's summary property.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be added to the properties of the package. Multiple tags can be added, separated by a comma or semicolon.",
                        "default": None
                }
        },
        "required": [
                "in_locator",
                "output_file"
        ]
},
    "package_map": {
        "name": "package_map",
        "description": "Packages a map and all referenced data sources to create a single compressed .mpkx file.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The  map that will be packaged. When running this tool in  ArcGIS Pro, the input can be a map, scene, or basemap."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output map package (.mpkx file)."
                },
                "convert_data": {
                        "type": "string",
                        "description": "Specifies whether input layers will be converted to a file geodatabase or preserved in their original format.CONVERT\u2014 Data will be converted to a file geodatabase. This option does not apply to enterp...",
                        "default": None
                },
                "convert_arcsde_data": {
                        "type": "string",
                        "description": "Specifies whether input enterprise geodatabase layers will be converted to a file geodatabase or preserved in their original format. CONVERT_ARCSDE\u2014 Enterprise geodatabase data will be converted to a ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_arcsde": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The specified extent will be applied to all layers. This is the default.ARCSDE_ONLY\u2014T...",
                        "default": None
                },
                "arcgisruntime": {
                        "type": "string",
                        "description": "Specifies whether the package will support ArcGIS Maps SDKs. To support ArcGIS Maps SDKs, all data sources will be converted to a file geodatabase, and an .msd file will be created in the output packa...",
                        "default": None
                },
                "reference_all_data": {
                        "type": "string",
                        "description": "Specifies whether a package that references the necessary data will be created rather than copying the data. This is helpful when trying to package large datasets that are available from a central loc...",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "Specifies the version of the geodatabases that will be created in the resulting package. Specifying a version allows packages to be shared with earlier versions of ArcGIS and supports backward compati...",
                        "default": None
                },
                "additional_files": {
                        "type": "string",
                        "description": "The additional files that will be included in the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The text that will be used as the output package's summary property.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be added to the properties of the package. Multiple tags can be added, separated by a comma or semicolon.",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "preserve_sqlite": {
                        "type": "string",
                        "description": "Specifies whether mobile geodatabase data will be preserved in the output or written to file geodatabase format. If the input data is a mobile geodatabase network dataset, the output will be a mobile ...",
                        "default": None
                },
                "consolidate_to_one_fgdb": {
                        "type": "string",
                        "description": "Specifies whether map layers will be consolidated to a single file geodatabase or to multiple file geodatabases based on the number of unique data sources in the input map.SINGLE_OUTPUT_WORKSPACE\u2014All ...",
                        "default": None
                }
        },
        "required": [
                "in_map",
                "output_file"
        ]
},
    "package_project": {
        "name": "package_project",
        "description": "Consolidates and packages an ArcGIS Pro project (.aprx) and its contents (maps and data) to a  packaged project file (.ppkx).",
        "parameters": {
                "in_project": {
                        "type": "string",
                        "description": "The project (.aprx file) that will be packaged."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output project package (.ppkx file)."
                },
                "sharing_internal": {
                        "type": "string",
                        "description": "Specifies whether the project and all data will be consolidated, converted, or copied into the package (for sharing outside your organization) or referenced as is without converting or including them ...",
                        "default": None
                },
                "package_as_template": {
                        "type": "string",
                        "description": "Specifies whether a project template or a project package will be created. Project templates can include maps, layouts, connections to databases and servers, and so on.  A project template can be used...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_arcsde": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The specified extent will be applied to all layers. This is the default.ENTERPRISE_ON...",
                        "default": None
                },
                "additional_files": {
                        "type": "string",
                        "description": "The additional files that will be included in the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The summary information that will be added to the properties of the package.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tags that will be added to the properties of the package. Separate multiple tags with a comma or semicolon.",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "Specifies the ArcGIS Pro version that certain objects such as projects, maps, and layers will be compatible with and persisted to.  Saving to an earlier version  can be helpful if the project will be ...",
                        "default": None
                },
                "include_toolboxes": {
                        "type": "string",
                        "description": "Specifies whether project toolboxes will be consolidated and included in the output package. All projects require a default toolbox, which will be included in the output package regardless of this set...",
                        "default": None
                },
                "include_history_items": {
                        "type": "string",
                        "description": "Specifies whether geoprocessing history items will be consolidated and included in the output package. Included history items will consolidate the data required to reprocess the history item.\r\nHISTORY...",
                        "default": None
                },
                "read_only": {
                        "type": "string",
                        "description": "Specifies whether the project will be read-only. Read-only projects cannot be modified or saved.\r\nREAD_ONLY\u2014The project will be read-only.READ_WRITE\u2014The project will be writable. This is the default.",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                },
                "preserve_sqlite": {
                        "type": "string",
                        "description": "Specifies whether mobile geodatabase data will be preserved in the output or written to file geodatabase format. If the input data is a mobile geodatabase network dataset, the output will be a mobile ...",
                        "default": None
                }
        },
        "required": [
                "in_project",
                "output_file"
        ]
},
    "package_result": {
        "name": "package_result",
        "description": "Packages one or more geoprocessing results, including all tools and input and output datasets, into a single compressed file (.gpkx).",
        "parameters": {
                "in_result": {
                        "type": "string",
                        "description": "The result that will be packaged.\r\n The input can be either a result  from the history  of the current project or a Result  object's resultID property when the tool is being used in a Python script."
                },
                "output_file": {
                        "type": "string",
                        "description": "The name  and location of the output package file (.gpkx)."
                },
                "convert_data": {
                        "type": "string",
                        "description": "Specifies whether input layers will be converted to a file geodatabase or preserved in their original format.CONVERT\u2014 Data will be converted to a file geodatabase. This option does not apply to enterp...",
                        "default": None
                },
                "convert_arcsde_data": {
                        "type": "string",
                        "description": "Specifies whether input enterprise geodatabase layers will be converted to a file geodatabase or preserved in their original format. CONVERT_ARCSDE\u2014 Enterprise geodatabase data will be converted to a ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used to select or clip features.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equ...",
                        "default": None
                },
                "apply_extent_to_arcsde": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to all layers or to enterprise geodatabase layers only.ALL\u2014 The specified extent will be applied to all layers. This is the default.ARCSDE_ONLY\u2014T...",
                        "default": None
                },
                "schema_only": {
                        "type": "string",
                        "description": "Specifies whether all records for input and output datasets or only the schema of input and output datasets will be consolidated or packaged.ALL\u2014 All records for input and output datasets will be cons...",
                        "default": None
                },
                "arcgisruntime": {
                        "type": "string",
                        "description": "Specifies whether the package will support ArcGIS Maps SDKs.   To support ArcGIS Maps SDKs, all data sources will be converted to a file geodatabase.DESKTOP\u2014The output package will not support ArcGIS ...",
                        "default": None
                },
                "additional_files": {
                        "type": "string",
                        "description": "The additional files that will be included in the package.",
                        "default": None
                },
                "summary": {
                        "type": "string",
                        "description": "The text that will be used as the output package's summary property.",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tag information that will be added to the properties of the package. Multiple tags can be added, separated by a comma or semicolon.",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "Specifies the ArcGIS Pro version that certain objects such as projects, maps, and layers will be compatible with and persisted to.  Saving to an earlier version  can be helpful if the project will be ...",
                        "default": None
                },
                "select_related_rows": {
                        "type": "string",
                        "description": "Specifies whether the specified extent will be applied to related data sources.KEEP_ONLY_RELATED_ROWS\u2014Only related data corresponding to records within the specified\r\nextent will be consolidated.KEEP_...",
                        "default": None
                }
        },
        "required": [
                "in_result",
                "output_file"
        ]
},
    "create_3d_object_scene_layer_content": {
        "name": "create_3d_object_scene_layer_content",
        "description": "Creates a scene layer package (.slpk) or scene layer content (.i3sREST) from a multipatch or 3D object feature layer input.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input multipatch or 3D object feature layer."
                },
                "out_slpk": {
                        "type": "string",
                        "description": "The output scene layer package (.slpk)."
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the output scene layer package. It can be any projected  or custom coordinate system. Supported geographic coordinate systems include WGS84 and China Geodetic Coordinate Syste...",
                        "default": None
                },
                "transform_method": {
                        "type": "string",
                        "description": "The datum transformation method that will be used when the input layer's coordinate system uses a datum that differs from the output coordinate system. All transformations are bidirectional, regardles..."
                },
                "texture_optimization": {
                        "type": "string",
                        "description": "Specifies the textures that will be optimized according to the target platform where the scene layer package will be used.Caution:Optimizations that include KTX2 may take significant time to process. ...",
                        "default": None
                },
                "target_cloud_connection": {
                        "type": "string",
                        "description": "The target cloud connection file (.acs) where the scene layer content (.i3sREST) will be output.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_slpk",
                "transform_method"
        ]
},
    "create_building_scene_layer_content": {
        "name": "create_building_scene_layer_content",
        "description": "Creates a scene layer package (.slpk) or scene layer content (.i3sREST) from a building layer input.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input building layer or layer file (.lyrx)."
                },
                "out_slpk": {
                        "type": "string",
                        "description": "The output scene layer package (.slpk)."
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the output scene layer package. It can be any projected  or custom coordinate system. Supported geographic coordinate systems include WGS84 and China Geodetic Coordinate Syste...",
                        "default": None
                },
                "transform_method": {
                        "type": "string",
                        "description": "The datum transformation method that will be used when the input layer's coordinate system uses a datum that differs from the output coordinate system. All transformations are bidirectional, regardles...",
                        "default": None
                },
                "texture_optimization": {
                        "type": "string",
                        "description": "Specifies the textures that will be optimized according to the target platform where the scene layer package is used.Caution:Optimizations that include KTX2 may take significant time to process. For f...",
                        "default": None
                },
                "target_cloud_connection": {
                        "type": "string",
                        "description": "The target cloud connection file (.acs) where the scene layer content (.i3sREST) will be output.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_slpk"
        ]
},
    "create_integrated_mesh_scene_layer_content": {
        "name": "create_integrated_mesh_scene_layer_content",
        "description": "Creates  scene layer content (.slpk or .i3sREST) from OpenSceneGraph binary (OSGB) data.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The \r\nOSGB format files, or folders containing OSGB format files, that will be imported into the integrated mesh scene layer package. This parameter allows a selection of multiple OSGB format files or..."
                },
                "out_slpk": {
                        "type": "string",
                        "description": "The integrated mesh scene layer package that will be created. This parameter is required if the Target Cloud Connection parameter value is not specified.",
                        "default": None
                },
                "anchor_point": {
                        "type": "string",
                        "description": "The point feature or .3mx, .xml, or .wld3  file that will be used to position the center of the OSGB model. If there are multiple points in the feature class, only the first point will be used to geor...",
                        "default": None
                },
                "file_suffix": {
                        "type": "string",
                        "description": "Specifies the files that will be processed for the input dataset.*\u2014All binary files, regardless of their extension, will be processed to determine if they are in the OSGB format.osgb\u2014Only files with t...",
                        "default": None
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the output scene layer package. It can be any projected  or custom coordinate system. Supported geographic coordinate systems include WGS84 and China Geodetic Coordinate Syste...",
                        "default": None
                },
                "max_texture_size": {
                        "type": "string",
                        "description": "The maximum texture size in pixels for each scene layer node.",
                        "default": None
                },
                "texture_optimization": {
                        "type": "string",
                        "description": "Specifies the textures that will be optimized according to the target platform where the scene layer package is used.Caution:Optimizations that include KTX2 may take significant time to process. For f...",
                        "default": None
                },
                "target_cloud_connection": {
                        "type": "string",
                        "description": "The target cloud connection file (.acs) where the scene layer content (.i3sREST) will be output.",
                        "default": None
                },
                "out_name": {
                        "type": "string",
                        "description": "The output name of the scene layer content when output to a cloud store. This parameter is only available when the target_cloud_connection parameter value is specified.",
                        "default": None
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "create_point_cloud_scene_layer_content": {
        "name": "create_point_cloud_scene_layer_content",
        "description": "Creates a point cloud scene layer package (.slpk) or scene layer content (.i3sREST) in the cloud from LAS, zLAS, LAZ, or LAS dataset input.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The lidar data (LAS, zLAS, LAZ, or LAS dataset) that will be used to create  a scene layer package. The lidar data can also be specified by selecting the parent folder that contains the files."
                },
                "out_slpk": {
                        "type": "string",
                        "description": "The output scene layer package (.slpk).",
                        "default": None
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the output scene layer package. It can be any projected  or custom coordinate system. Supported geographic coordinate systems include WGS84 and China Geodetic Coordinate Syste...",
                        "default": None
                },
                "transform_method": {
                        "type": "string",
                        "description": "The datum transformation method that will be used when the input layer's coordinate system uses a datum that differs from the output coordinate system. All transformations are bidirectional, regardles...",
                        "default": None
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies the source data attributes that will be included in the scene layer package. These values will be accessible when the content is consumed in other viewers. Select attributes that are require...",
                        "default": None
                },
                "point_size_m": {
                        "type": "string",
                        "description": "The point size of the lidar data.\r\n For airborne lidar data, the default of 0 or a value close to the average point spacing is usually best. For terrestrial lidar data, the point size should match the...",
                        "default": None
                },
                "xy_max_error_m": {
                        "type": "string",
                        "description": "The maximum x,y error tolerated. A higher tolerance will result in better data compression and more efficient data transfer. Values are expressed in meters. The default is 0.001.",
                        "default": None
                },
                "z_max_error_m": {
                        "type": "string",
                        "description": "The maximum z-error tolerated. A higher tolerance will result in better data compression and more efficient data transfer. Values are expressed in meters. The default is 0.001.",
                        "default": None
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the input .laz files. This parameter is only used for .laz files that do not contain spatial reference information in their header or have a .prj file in the same location.",
                        "default": None
                },
                "scene_layer_version": {
                        "type": "string",
                        "description": "The Indexed 3D Scene Layer (I3S) version of the resulting point cloud scene layer package. Specifying a version supports backward compatibility and allows scene layer packages to be shared with earlie...",
                        "default": None
                },
                "target_cloud_connection": {
                        "type": "string",
                        "description": "The target cloud connection file (.acs) where the scene layer content (.i3sREST) will be output.",
                        "default": None
                },
                "out_name": {
                        "type": "string",
                        "description": "The output name of the scene layer content when output to a cloud store. This parameter is only available when a target_cloud_connection parameter value is specified.",
                        "default": None
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "create_point_scene_layer_content": {
        "name": "create_point_scene_layer_content",
        "description": "Creates a point scene layer package (.slpk) or scene layer content (.i3sREST) from a point feature layer.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input point feature layer."
                },
                "out_slpk": {
                        "type": "string",
                        "description": "The output scene layer package (.slpk)."
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the output scene layer package. It can be any projected  or custom coordinate system. Supported geographic coordinate systems include WGS84 and China Geodetic Coordinate Syste...",
                        "default": None
                },
                "transform_method": {
                        "type": "string",
                        "description": "The datum transformation method that will be used when the input layer's coordinate system  uses a datum that differs from the output coordinate system. All transformations are bidirectional, regardle...",
                        "default": None
                },
                "target_cloud_connection": {
                        "type": "string",
                        "description": "The target cloud connection file (.acs) where the scene layer content (.i3sREST) will be output.",
                        "default": None
                },
                "support_symbol_referencing": {
                        "type": "string",
                        "description": "Specifies whether Esri symbols will be referenced by the scene layer package or copied to it. SUPPORT_REFERENCING_SYMBOLS\u2014Esri symbols will be referenced by the scene layer package. Using this option ..."
                }
        },
        "required": [
                "in_dataset",
                "out_slpk",
                "support_symbol_referencing"
        ]
},
    "create_voxel_scene_layer_content": {
        "name": "create_voxel_scene_layer_content",
        "description": "Creates a scene layer package (.slpk file) from a voxel layer input.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input voxel layer or layer file."
                },
                "out_slpk": {
                        "type": "string",
                        "description": "The output scene layer package (.slpk file)."
                }
        },
        "required": [
                "in_dataset",
                "out_slpk"
        ]
},
    "generate_level_of_detail": {
        "name": "generate_level_of_detail",
        "description": "Generates a new scene layer package with properly defined levels of detail. Only the finest level of detail is maintained; all other levels of detail are discarded. The finest level of detail is reorganized into  tiles that generate new coarse levels of detail.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input integrated mesh scene layer package."
                },
                "out_dataset": {
                        "type": "string",
                        "description": "The output scene layer package."
                },
                "texture_optimization": {
                        "type": "string",
                        "description": "Specifies the textures that will be optimized according to the target platform where the scene layer package will be used.Caution:Optimizations that include KTX2 may take significant time to process. ...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_dataset"
        ]
},
    "upgrade_scene_layer": {
        "name": "upgrade_scene_layer",
        "description": "Upgrades a scene layer package to the current I3S version in SLPK format or output to i3sREST  format for use in ArcGIS Enterprise.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input scene layer package."
                },
                "out_folder_path": {
                        "type": "string",
                        "description": "The location where the output scene layer package will be created or the cloud connection file (.acs) to output to i3sREST format."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the output scene layer."
                },
                "out_log": {
                        "type": "string",
                        "description": "The output log file that will summarize the results of the evaluation.",
                        "default": None
                },
                "texture_optimization": {
                        "type": "string",
                        "description": "Specifies the textures that will be optimized according to the target platform where the scene layer package is used.Caution:Optimizations that include KTX2 may take significant time to process. For f...",
                        "default": None
                },
                "date_format": {
                        "type": "string",
                        "description": "The format of the date values in the scene layers date fields. This parameter is hidden if no date fields are encountered.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_folder_path",
                "out_name"
        ]
},
    "validate_scene_layer": {
        "name": "validate_scene_layer",
        "description": "Evaluates a scene layer package (*.slpk or *.i3sREST) in a cloud store to determine its conformity to I3S specifications.",
        "parameters": {
                "in_slpk": {
                        "type": "string",
                        "description": "The scene layer package (*.slpk) that will be evaluated.",
                        "default": None
                },
                "out_report": {
                        "type": "string",
                        "description": "The output log file that will summarize the results of the evaluation."
                },
                "in_folder": {
                        "type": "string",
                        "description": "The scene layer content (*.i3sREST) in a cloud store that will be evaluated.",
                        "default": None
                }
        },
        "required": [
                "out_report"
        ]
},
    "geotagged_photos_to_points": {
        "name": "geotagged_photos_to_points",
        "description": "Creates points from the x-, y-, and z-coordinates stored in the metadata of geotagged photo files (.jpg or .tif). You can  add the photo files to the output features as geodatabase attachments.",
        "parameters": {
                "input_folder": {
                        "type": "string",
                        "description": "The folder where photo files (.jpg or .tif) are located. This folder is scanned recursively for photo files; any photos in the base level of the folder, as well as in any subfolders, will be added to ..."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output point feature class."
                },
                "invalid_photos_table": {
                        "type": "string",
                        "description": "An output table that will list any photo files in the input folder with invalid Exif metadata or empty or invalid coordinates.If no value is specified, the table will not be created.",
                        "default": None
                },
                "include_non_geotagged_photos": {
                        "type": "string",
                        "description": "Specifies whether all photo files will be included in the output feature class or only those with valid coordinates.ALL_PHOTOS\u2014 All photos will be included as records in the output feature class. If a...",
                        "default": None
                },
                "add_photos_attachments": {
                        "type": "string",
                        "description": "Specifies whether the input photos will be added to the output features as geodatabase attachments.Note:Adding attachments requires that the  output feature class be in a version 10 or later geodataba...",
                        "default": None
                }
        },
        "required": [
                "input_folder",
                "output_feature_class"
        ]
},
    "match_photos_to_rows_by_time": {
        "name": "match_photos_to_rows_by_time",
        "description": "Matches photo files to table or feature class rows according to the photo and row time stamps. The row with the time stamp closest to the capture time of a photo will be matched to that photo. A new table is created that contains the object ID values from the input rows and their matching photo paths. You can also use this tool to add matching photo files to the rows of the input table as geodatabase attachments.",
        "parameters": {
                "input_folder": {
                        "type": "string",
                        "description": "The folder where photo files (.jpg or .tif) are located. This folder is scanned recursively for photo files; any photos in the base level of the folder, as well as in any subfolders, will be added to ..."
                },
                "input_table": {
                        "type": "string",
                        "description": "The table or feature class whose rows will be matched with photo files. The input table will typically be a point feature class representing GPS recordings."
                },
                "time_field": {
                        "type": "string",
                        "description": "The date field from the input table that indicates when each row was captured or created. The field must be of type date; it cannot be of type string or numeric."
                },
                "output_table": {
                        "type": "string",
                        "description": "The output table containing the object ID values from the input table that match a photo,  and the matching photo path. Only object ID values from the input table that match a photo are included in th..."
                },
                "unmatched_photos_table": {
                        "type": "string",
                        "description": "The optional output table that will list any photo files in the input folder with an invalid time stamp or any photos that cannot be matched because there is no input row within the time tolerance.If ...",
                        "default": None
                },
                "add_photos_attachments": {
                        "type": "string",
                        "description": "Specifies whether the photo files will be added to the rows of the input table as geodatabase attachments. Note:Adding attachments requires that the  output feature class be in a version 10 or later g...",
                        "default": None
                },
                "time_tolerance": {
                        "type": "string",
                        "description": "The maximum difference (in seconds) between the date/time of an input row and a photo file that will be matched. If an input row and a photo file have time  stamps that are different by more than this...",
                        "default": None
                },
                "clock_offset": {
                        "type": "string",
                        "description": "The difference (in seconds) between the internal clock of the digital camera used to capture the photos and the GPS unit. If the clock of the digital camera is behind the clock of the GPS unit, use a ...",
                        "default": None
                }
        },
        "required": [
                "input_folder",
                "input_table",
                "time_field",
                "output_table"
        ]
},
    "batch_project": {
        "name": "batch_project",
        "description": "Changes the coordinate system of a set of input feature classes or feature datasets to a common coordinate system. To change the coordinate system of a single feature class or dataset use the Project tool.",
        "parameters": {
                "input_feature_class_or_dataset": {
                        "type": "string",
                        "description": "The input feature classes or feature datasets whose coordinates are to be converted."
                },
                "output_workspace": {
                        "type": "string",
                        "description": "The location of each new output feature class or feature dataset."
                },
                "output_coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system to be used to project the inputs. Valid values are a SpatialReference object, a file with a .prj extension, or a string representation of a coordinate system.",
                        "default": None
                },
                "template_dataset": {
                        "type": "string",
                        "description": "The feature class or the feature dataset used to specify the output coordinate system used for projection.",
                        "default": None
                },
                "transformation": {
                        "type": "string",
                        "description": "The name of the geographic transformation to be applied to convert data between two geographic coordinate systems (datums).",
                        "default": None
                }
        },
        "required": [
                "input_feature_class_or_dataset",
                "output_workspace"
        ]
},
    "project": {
        "name": "project",
        "description": "Projects spatial data from one coordinate system to another.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The feature class, feature layer, feature dataset, scene layer, scene layer package, or OGC Geopackage to be projected."
                },
                "out_dataset": {
                        "type": "string",
                        "description": "The output dataset to which the results will be written."
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "Valid values are a SpatialReference object, a file with a .prj extension, or a string representation of a coordinate system."
                },
                "transform_method": {
                        "type": "string",
                        "description": "This method can be used to convert data between two geographic coordinate systems or datums. This optional parameter may be required if the input and output coordinate systems have different datums.To...",
                        "default": None
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the input feature class or dataset. When the input has an unknown or unspecified coordinate system, you can specify the data's coordinate system without having to modify the i...",
                        "default": None
                },
                "preserve_shape": {
                        "type": "string",
                        "description": "Specifies whether extra vertices will be added to the output lines or polygons so their projected shape is more accurate.NO_PRESERVE_SHAPE\u2014Extra vertices will not be added to the output lines or polyg...",
                        "default": None
                },
                "max_deviation": {
                        "type": "string",
                        "description": "The distance a projected line or polygon can deviate from its exact projected location when the preserve_shape parameter is set to PRESERVE_SHAPE. The default is 100 times the x,y tolerance of the spa...",
                        "default": None
                },
                "vertical": {
                        "type": "string",
                        "description": "Specifies whether a vertical transformation will be applied.This parameter is only enabled when the input and output coordinate systems have a vertical coordinate system and the input feature class co...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_dataset",
                "out_coor_system"
        ]
},
    "convert_coordinate_notation": {
        "name": "convert_coordinate_notation",
        "description": "Converts coordinate notations contained in one or two fields from one notation format to another. Learn more about supported notation formats",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table or text file. Point features are also valid."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The output point feature class.  The attribute table will contain all fields of the input table along with the fields containing converted values in the output format."
                },
                "x_field": {
                        "type": "string",
                        "description": "A field from the input table containing the longitude value. For the input_coordinate_format parameter's DD_2, DD_NUMERIC, DDM_2, and DMS_2 options, this is the longitude field. For the DD_1, DDM_1, a..."
                },
                "y_field": {
                        "type": "string",
                        "description": "A field from the input table containing the latitude value. For the input_coordinate_format parameter's DD_2, DD_NUMERIC, DDM_2, and DMS_2 options, this is the longitude field. This parameter is ignor..."
                },
                "input_coordinate_format": {
                        "type": "string",
                        "description": "Specifies the coordinate format of the input fields.DD_1\u2014Both longitude and latitude values are in a single field. Two values are separated by a space, a comma, or a slash. DD_2\u2014Longitude and latitude..."
                },
                "output_coordinate_format": {
                        "type": "string",
                        "description": "Specifies the coordinate format to which the input notations will be converted.DD_1\u2014Both longitude and latitude values are in a single field. Two values are separated by a space, a comma, or a slash. ..."
                },
                "id_field": {
                        "type": "string",
                        "description": "This parameter is ignored, as all fields are transferred to output table.",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature class. The default is GCS_WGS_1984.The tool projects the output  to the spatial reference specified. If the input and output coordinate systems are in a dif...",
                        "default": None
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The spatial reference of the input data. If the input spatial reference cannot be obtained from the input table, a default of GCS_WGS_1984 will be used.",
                        "default": None
                },
                "exclude_invalid_records": {
                        "type": "string",
                        "description": "Specifies whether to exclude records with invalid notation.EXCLUDE_INVALID\u2014Invalid records will be excluded and only valid records will be converted to points in the output. This is the default.INCLUD...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_featureclass",
                "x_field",
                "y_field",
                "input_coordinate_format",
                "output_coordinate_format"
        ]
},
    "create_custom_geographic_transformation": {
        "name": "create_custom_geographic_transformation",
        "description": "Creates a transformation definition for converting data between two geographic coordinate systems or datums. The output of this tool can be used as a transformation for any tool with a parameter that requires a geographic transformation.",
        "parameters": {
                "geot_name": {
                        "type": "string",
                        "description": "The name of the custom transformation definition."
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The starting geographic coordinate system. The coordinate system must be a geographic coordinate system; a projected coordinate system is invalid."
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The final geographic coordinate system. The coordinate system must be a geographic coordinate system; a projected coordinate system is invalid.\r\n The input and output geographic coordinate systems can..."
                },
                "custom_geot": {
                        "type": "string",
                        "description": "The custom transformation method that will be used.A list of the methods and parameters is available in the Geographic and Vertical Transformations pdf.Set the METHOD and PARAMETER values wrapped in a..."
                },
                "extent": {
                        "type": "string",
                        "description": "The geographic area where the transformation is applicable. Transformed data within the provided extent is guaranteed to be converted with the specified level of accuracy",
                        "default": None
                },
                "accuracy": {
                        "type": "string",
                        "description": "The expected difference between transformed (output) coordinates and their true values. Because any transformation in general degrades the quality of the dataset, the accuracy value is always the maxi...",
                        "default": None
                }
        },
        "required": [
                "geot_name",
                "in_coor_system",
                "out_coor_system",
                "custom_geot"
        ]
},
    "create_custom_vertical_transformation": {
        "name": "create_custom_vertical_transformation",
        "description": "Creates a transformation definition for converting data between two vertical coordinate systems or datums. The output of this tool can be used as a transformation object for any tool with a parameter that requires a vertical transformation.",
        "parameters": {
                "vt_name": {
                        "type": "string",
                        "description": "The name of the custom transformation definition."
                },
                "source_vt_coor_system": {
                        "type": "string",
                        "description": "The starting vertical coordinate system."
                },
                "target_vt_coor_system": {
                        "type": "string",
                        "description": "The final vertical coordinate system."
                },
                "interpolation_gcs": {
                        "type": "string",
                        "description": "The interpolation geographic coordinate system.This parameter is only active if a vertical transformation method requires it.The geographic coordinate system is used when interpolating the offset valu...",
                        "default": None
                },
                "custom_vt": {
                        "type": "string",
                        "description": "The vertical transformation method that will be used.From the drop-down list, choose the transformation method that will be used to transform the data from the input vertical coordinate system to the ...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "The area where the transformation is applicable. Use WGS84 (WKID: 4326) or another GNSS-based geographic coordinate system such as NAD 1983 or GDA2020 for the extent coordinate system. If a projected ...",
                        "default": None
                },
                "accuracy": {
                        "type": "string",
                        "description": "A general statement of accuracy in meters.",
                        "default": None
                }
        },
        "required": [
                "vt_name",
                "source_vt_coor_system",
                "target_vt_coor_system"
        ]
},
    "create_spatial_reference": {
        "name": "create_spatial_reference",
        "description": "Creates a spatial reference for use in ModelBuilder.",
        "parameters": {
                "spatial_reference": {
                        "type": "string",
                        "description": "The name of the spatial reference to be created.",
                        "default": None
                },
                "spatial_reference_template": {
                        "type": "string",
                        "description": "The feature class or layer to be used as a template to set the value for the spatial reference.",
                        "default": None
                },
                "xy_domain": {
                        "type": "string",
                        "description": "The allowable coordinate range for x,y coordinates.",
                        "default": None
                },
                "z_domain": {
                        "type": "string",
                        "description": "The allowable coordinate range for z-values.",
                        "default": None
                },
                "m_domain": {
                        "type": "string",
                        "description": "The allowable coordinate range for m-values.",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "The feature classes or layers that can be used to define the XY Domain.",
                        "default": None
                },
                "expand_ratio": {
                        "type": "string",
                        "description": "The percentage by which the XY Domain will be expanded.",
                        "default": None
                }
        },
        "required": []
},
    "define_projection": {
        "name": "define_projection",
        "description": "Overwrites the coordinate system information (map projection and datum) stored with a dataset. This tool is intended for datasets that have an unknown or incorrect coordinate system defined.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The dataset or feature class whose projection will be defined."
                },
                "coor_system": {
                        "type": "string",
                        "description": "The coordinate system that will be applied to the input. Valid values are a SpatialReference object, a file with a .prj extension, or a string representation of a coordinate system."
                }
        },
        "required": [
                "in_dataset",
                "coor_system"
        ]
},
    "flip": {
        "name": "flip",
        "description": "Reorients the raster by turning it over, from top to bottom, along the horizontal axis through the center of the raster. This may be useful to correct raster datasets that are upside down.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset.When storing the raster dataset in a file format, specify the file extension as follows:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.dat\u2014ENVI DAT.gif\u2014GIF.img\u2014ERDAS IMAGINE..."
                }
        },
        "required": [
                "in_raster",
                "out_raster"
        ]
},
    "mirror": {
        "name": "mirror",
        "description": "Reorients the raster by turning it over, from left to right, along the vertical axis through the center of the raster.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset.When storing the raster dataset in a file format, specify the file extension as follows:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.dat\u2014ENVI DAT.gif\u2014GIF.img\u2014ERDAS IMAGINE..."
                }
        },
        "required": [
                "in_raster",
                "out_raster"
        ]
},
    "project_raster": {
        "name": "project_raster",
        "description": "Transforms a raster dataset from one coordinate system to another. Learn more about how Project Raster works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset that will be transformed into a new projection."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The raster dataset with the new projection that will be created.When storing the raster dataset in a file format, specify the file extension as follows:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ...."
                },
                "out_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the new raster dataset.Valid values for this parameter are the following:An existing feature class, feature dataset, or raster dataset (basically anything with a coordinate sy..."
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Specifies the resampling technique that will be used. The default is Nearest.NEAREST\u2014 The nearest neighbor technique will be used. It minimizes changes to pixel values since no new values are created ...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the new raster using an existing raster dataset or by specifying its width (x) and height (y).",
                        "default": None
                },
                "geographic_transform": {
                        "type": "string",
                        "description": "The geographic transformation when\r\nprojecting from one geographic system or datum to another.\r\nA transformation is required when the input and output coordinate systems have different datums.",
                        "default": None
                },
                "registration_point": {
                        "type": "string",
                        "description": "The lower left point for\r\nanchoring the output cells. This point does not need to be a corner\r\ncoordinate or fall within the\r\nraster dataset.\r\nThe Snap Raster environment setting will take priority ov...",
                        "default": None
                },
                "in_coor_system": {
                        "type": "string",
                        "description": "The coordinate system of the input raster dataset.This parameter is only enabled when the input has an unknown coordinate system. When this is the case, specify a current coordinate system for the ras...",
                        "default": None
                },
                "vertical": {
                        "type": "string",
                        "description": "Specifies whether a vertical transformation will be applied.This parameter is enabled when the input and output coordinate systems have a vertical coordinate system and the input feature class coordin...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "out_coor_system"
        ]
},
    "register_raster": {
        "name": "register_raster",
        "description": "Automatically aligns a raster to a reference image or uses a control point file for georegistration. If the input dataset is a mosaic dataset, the tool will operate on each mosaic dataset item. To automatically register the image, the input raster and the reference raster must be in a relatively close geographic area. The tool will run faster if the raster datasets are in close alignment. You may need to create a link file, also known as a control point file, with a few links to get your input raster into the same map space.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster that you want to realign. Registering a mosaic dataset item will update that particular item within the mosaic dataset.A mosaic dataset item will have the path to the mosaic dataset followe..."
                },
                "register_mode": {
                        "type": "string",
                        "description": "Specifies the registration mode. You can either register the raster with  a transformation or reset the transformation.REGISTER\u2014Apply a geometric transformation to the input raster.REGISTER_MS\u2014Registe..."
                },
                "reference_raster": {
                        "type": "string",
                        "description": "The raster dataset that will align the input raster dataset. Leave this parameter empty if you want to register your multispectral mosaic dataset items to their associated  panchromatic raster dataset...",
                        "default": None
                },
                "input_link_file": {
                        "type": "string",
                        "description": "The file that has the coordinates to link the input raster dataset with the reference. The input link table works with one mosaic item in the mosaic layer. The input must specify which item is being p...",
                        "default": None
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Specifies the method for shifting the raster dataset.POLYORDER0\u2014 This method uses a zero-order polynomial to shift your data. This is commonly used when your data is already georeferenced, but a small...",
                        "default": None
                },
                "output_cpt_link_file": {
                        "type": "string",
                        "description": "If specified, a text file will be written containing the links created by this tool. This file can be used in the\r\nWarp From File tool. The output link table\r\nworks with one mosaic dataset item in the...",
                        "default": None
                },
                "maximum_rms_value": {
                        "type": "string",
                        "description": "The amount of modeled error (in pixels) that you want in the output. The default is 0.5, and values below 0.3 are not recommended as this leads to overfitting.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "register_mode"
        ]
},
    "rescale": {
        "name": "rescale",
        "description": "Resizes a raster by the specified x and y scale factors.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset.When storing the raster dataset in a file format, specify the file extension as follows:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.dat\u2014ENVI DAT.gif\u2014GIF.img\u2014ERDAS IMAGINE..."
                },
                "x_scale": {
                        "type": "string",
                        "description": "The factor by which to scale the cell size in the x direction.The factor must be greater than zero."
                },
                "y_scale": {
                        "type": "string",
                        "description": "The factor by which to scale the cell size in the y direction.The factor must be greater than zero."
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "x_scale",
                "y_scale"
        ]
},
    "rotate": {
        "name": "rotate",
        "description": "Turns a raster dataset around a specified pivot point.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to rotate."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format for the dataset you are creating. When storing a raster dataset in a geodatabase, do not add a file extension to the name of the raster dataset. When storing your raster..."
                },
                "angle": {
                        "type": "string",
                        "description": "Specify a value between 0 and 360 degrees the raster will be rotated in the clockwise direction. To rotate the raster in the counterclockwise direction, specify the angle as a negative value. The angl..."
                },
                "pivot_point": {
                        "type": "string",
                        "description": "The point the raster will rotate around. If left blank, the lower left corner of the input raster dataset will serve as the pivot.",
                        "default": None
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Specifies the resampling technique that will be used. The default is Nearest.NEAREST\u2014 The nearest neighbor technique will be used. It minimizes changes to pixel values since no new values are created ...",
                        "default": None
                },
                "clipping_extent": {
                        "type": "string",
                        "description": "The processing extent of the raster dataset.  The source data will be clipped to the specified extent before rotation.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "angle"
        ]
},
    "shift": {
        "name": "shift",
        "description": "Moves (slides) the raster to a new geographic location based on x and y shift values. This tool is helpful if your raster dataset needs to be shifted to align with another data file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset.When storing the raster dataset in a file format, specify the file extension as follows:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.dat\u2014ENVI DAT.gif\u2014GIF.img\u2014ERDAS IMAGINE..."
                },
                "x_value": {
                        "type": "string",
                        "description": "The value used to shift the x-coordinates."
                },
                "y_value": {
                        "type": "string",
                        "description": "The value used to shift the y-coordinates."
                },
                "in_snap_raster": {
                        "type": "string",
                        "description": "The raster dataset used to align the cells of the output raster dataset.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "x_value",
                "y_value"
        ]
},
    "warp": {
        "name": "warp",
        "description": "Transforms a raster dataset using source and target control points. This is similar to georeferencing.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster to be transformed."
                },
                "source_control_pointssource_control_point": {
                        "type": "string",
                        "description": "The coordinates of the raster to be warped."
                },
                "target_control_pointstarget_control_point": {
                        "type": "string",
                        "description": "The coordinates to which the source raster will be warped."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format for the dataset you are creating. When storing a raster dataset in a geodatabase, do not add a file extension to the name of the raster dataset. When storing your raster..."
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Specifies the transformation method for shifting the raster dataset.POLYORDER0\u2014 A zero-order polynomial will be used to shift the data. This is commonly used when the data is georeferenced, but a smal...",
                        "default": None
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Specifies the resampling technique that will be used. The default is Nearest.NEAREST\u2014 The nearest neighbor technique will be used. It minimizes changes to pixel values since no new values are created ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "source_control_pointssource_control_point",
                "target_control_pointstarget_control_point",
                "out_raster"
        ]
},
    "warp_from_file": {
        "name": "warp_from_file",
        "description": "Transforms a raster dataset using an existing text file containing source and target control points.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster to be transformed."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format for the dataset you are creating. When storing a raster dataset in a geodatabase, do not add a file extension to the name of the raster dataset. When storing your raster..."
                },
                "link_file": {
                        "type": "string",
                        "description": "The text, CSV file, or TAB file containing the coordinates to warp the input raster. This can be generated from the Register Raster tool or from the Georeferencing  tab."
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Specifies the transformation method for shifting the raster dataset.POLYORDER0\u2014 A zero-order polynomial will be used to shift the data. This is commonly used when the data is georeferenced, but a smal...",
                        "default": None
                },
                "resampling_type": {
                        "type": "string",
                        "description": "The resampling algorithm to be used.NEAREST\u2014 The nearest neighbor technique will be used. It minimizes changes to pixel values since no new values are created and is the fastest resampling technique. ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "link_file"
        ]
},
    "clip": {
        "name": "clip",
        "description": "Cuts out a portion of a raster dataset, mosaic dataset, or image service layer.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset, mosaic dataset, or image service to be clipped."
                },
                "rectangle": {
                        "type": "string",
                        "description": "The four coordinates that define the extent of the bounding box that will be used to clip the raster. Coordinates are expressed in the order of x-min, y-min, x-max, y-max.If the in_template_dataset pa..."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format of the dataset being created. Ensure that it can support the necessary bit depth.When storing the raster dataset in a file format, specify the file extension as follows:..."
                },
                "in_template_dataset": {
                        "type": "string",
                        "description": "A raster dataset or feature class\r\nthat will be used as the extent. The clip output\r\nincludes pixels that intersect the minimum bounding\r\nrectangle.\r\nIf a feature class is used as the output extent an...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "The value for pixels to be considered as NoData.",
                        "default": None
                },
                "clipping_geometry": {
                        "type": "string",
                        "description": "Specifies whether the minimum bounding rectangle or the geometry of the specified feature class will be used to clip the data.NONE\u2014The minimum bounding rectangle will be used to clip the data. This is...",
                        "default": None
                },
                "maintain_clipping_extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used in the clipping output.MAINTAIN_EXTENT\u2014The number of columns and rows will be adjusted and  the pixels will be resampled to exactly match the clipping extent spe...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "rectangle",
                "out_raster"
        ]
},
    "add_rasters_to_mosaic_dataset": {
        "name": "add_rasters_to_mosaic_dataset",
        "description": "Adds raster datasets to a mosaic dataset from various sources, including a file, folder, table, or web service.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The path and name of the mosaic dataset to which the raster data will be added."
                },
                "raster_type": {
                        "type": "string",
                        "description": "The type of raster that will be added. The raster type is specific to imagery products. It identifies metadata\u2014such as georeferencing, acquisition date, and sensor type\u2014along with a raster format.If y..."
                },
                "input_path": {
                        "type": "string",
                        "description": "Specifies the path and name of the input file, folder, raster dataset, mosaic dataset, table, or service.Not all input options will be available. The selected raster type determines the available opti..."
                },
                "update_cellsize_ranges": {
                        "type": "string",
                        "description": "Specifies whether the cell size ranges of each raster in the mosaic dataset will be calculated. These values will be written to the attribute table in the minPS and maxPS fields.UPDATE_CELL_SIZES\u2014The ...",
                        "default": None
                },
                "update_boundary": {
                        "type": "string",
                        "description": "Specifies whether the boundary polygon of a mosaic dataset will be generated or updated. By default, the boundary merges all the footprint polygons to create a single boundary representing the extent ...",
                        "default": None
                },
                "update_overviews": {
                        "type": "string",
                        "description": "Specifies whether overviews for a mosaic dataset will be defined and generated.UPDATE_OVERVIEWS\u2014Overviews will be defined and generated.NO_OVERVIEWS\u2014Overviews will not be defined or generated. This is...",
                        "default": None
                },
                "maximum_pyramid_levels": {
                        "type": "string",
                        "description": "The maximum number of pyramid levels that will be used in the mosaic dataset. For example, a value of 2 will use only the first two pyramid levels from the source  raster.  Leaving this parameter blan...",
                        "default": None
                },
                "maximum_cell_size": {
                        "type": "string",
                        "description": "The maximum pyramid cell size that will be used in the mosaic dataset.",
                        "default": None
                },
                "minimum_dimension": {
                        "type": "string",
                        "description": "The minimum dimensions of a raster pyramid that will be used in the mosaic dataset.",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference system of the input data.Specify a value if the data does not have a coordinate system; otherwise, the coordinate system of the mosaic dataset will be used. This can also be used...",
                        "default": None
                },
                "filter": {
                        "type": "string",
                        "description": "A filter for the data being added to the mosaic dataset. You can use SQL expressions to create the data filter. The wildcards for the filter work on the full path to the input data.For example, the fo...",
                        "default": None
                },
                "sub_folder": {
                        "type": "string",
                        "description": "Specifies whether subfolders will be recursively explored.SUBFOLDERS\u2014All subfolders will be explored for data. This is the default.NO_SUBFOLDERS\u2014Only the top-level folder will be explored for data.",
                        "default": None
                },
                "duplicate_items_action": {
                        "type": "string",
                        "description": "Specifies how duplicate rasters will be handled. A check will be performed to determine whether each raster has already been added, using the original path and file name. Specify the option to use whe...",
                        "default": None
                },
                "build_pyramids": {
                        "type": "string",
                        "description": "Specifies whether pyramids will be built for each source raster.NO_PYRAMIDS\u2014Pyramids will not be built. This is the default.BUILD_PYRAMIDS\u2014Pyramids will be built.",
                        "default": None
                },
                "calculate_statistics": {
                        "type": "string",
                        "description": "Specifies whether statistics will be calculated for each source raster.NO_STATISTICS\u2014Statistics will not be calculated. This is the default.CALCULATE_STATISTICS\u2014Statistics will be calculated.",
                        "default": None
                },
                "build_thumbnails": {
                        "type": "string",
                        "description": "Specifies whether thumbnails will be built for each source raster.NO_THUMBNAILS\u2014Thumbnails will not be built. This is the default.BUILD_THUMBNAILS\u2014Thumbnails will be built.",
                        "default": None
                },
                "operation_description": {
                        "type": "string",
                        "description": "The description that will be used to represent the operation of adding raster data. It will be added to the raster type table, which can be used as part of a search or as a reference at another time.",
                        "default": None
                },
                "force_spatial_reference": {
                        "type": "string",
                        "description": "Specifies the coordinate system that will be used. Use the coordinate system specified in the spatial_reference parameter for all the rasters when loading data into the mosaic dataset.NO_FORCE_SPATIAL...",
                        "default": None
                },
                "estimate_statistics": {
                        "type": "string",
                        "description": "Specifies whether statistics will be estimated on the mosaic dataset for faster rendering and processing at the mosaic dataset level.NO_STATISTICS\u2014Statistics will not be estimated. Statistics generate...",
                        "default": None
                },
                "enable_pixel_cache": {
                        "type": "string",
                        "description": "Specifies whether the pixel cache will be generated for faster display and processing of the mosaic dataset.NO_PIXEL_CACHE\u2014The pixel cache will not be generated. This is the default.USE_PIXEL_CACHE\u2014Th...",
                        "default": None
                },
                "cache_location": {
                        "type": "string",
                        "description": "The location of the pixel cache. If no location is provided, the cache will be written to C:\\Users\\&lt;Username&gt;\\AppData\\Local\\ESRI\\rasterproxies\\.\r\nOnce the location is provided, you do not need t...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "raster_type",
                "input_path"
        ]
},
    "alter_mosaic_dataset_schema": {
        "name": "alter_mosaic_dataset_schema",
        "description": "Defines the editing operations that nonowners  have when editing a mosaic dataset in an enterprise geodatabase. This tool prevents schema-locking issues that can occur when a mosaic dataset is stored in an enterprise geodatabase. The owner of the geodatabase runs this tool to create side tables and fields that may be needed by the user. The owner must also  grant the proper permissions to allow users to insert, update, or delete records.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset on which the permitted operations will be changed."
                },
                "side_tablesoperation": {
                        "type": "string",
                        "description": "Specifies the operations that will be permissible for a nonowner to perform on the mosaic dataset. ANALYSIS\u2014A nonowner will be  allowed to run the Analyze Mosaic Dataset  tool on the mosaic dataset.BO...",
                        "default": None
                },
                "raster_type_namesraster_type": {
                        "type": "string",
                        "description": "Specifies the raster types that nonowners can add to the mosaic dataset.To specify a custom raster type, provide the location of the custom raster type file.ADS\u2014The Leica ADS raster type can be added....",
                        "default": None
                },
                "editor_tracking": {
                        "type": "string",
                        "description": "Specifies whether editor tracking will be enabled.Editor tracking can help you maintain accountability and enforce quality-control standards. NO_EDITOR_TRACKING\u2014Editor tracking will not be enabled. Th...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "analyze_mosaic_dataset": {
        "name": "analyze_mosaic_dataset",
        "description": "Performs checks on a mosaic dataset for errors and possible improvements.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset you want to analyze."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL statement that confines your analysis to specific raster datasets within this mosaic dataset.",
                        "default": None
                },
                "checker_keywords": {
                        "type": "string",
                        "description": "Choose which parts of the mosaic dataset you want to analyze for known issues.\r\nFOOTPRINT\u2014 Analyze the footprint geometry of each selected mosaic dataset item. This is checked on by default.FUNCTION\u2014 ...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "build_boundary": {
        "name": "build_boundary",
        "description": "Updates the extent of the boundary when adding new raster datasets to a mosaic dataset that extend beyond its previous coverage.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "Select the mosaic dataset where you want to recompute the boundary."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL query to compute a boundary for select raster datasets. Use this option in conjunction with setting the append_to_existing parameter to APPEND to save time when adding new raster datasets.",
                        "default": None
                },
                "append_to_existing": {
                        "type": "string",
                        "description": "Set this to APPEND when adding new raster datasets to an existing mosaic dataset. Instead of calculating the entire boundary, APPEND will merge the boundary of the new raster datasets with the existin...",
                        "default": None
                },
                "simplification_method": {
                        "type": "string",
                        "description": "Specifies the simplification method that will be used to reduce the number of vertices, since a dense boundary can affect performance.Choose the simplification method to use to simplify the boundary.N...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "build_footprints": {
        "name": "build_footprints",
        "description": "Computes the extent of every raster in a mosaic dataset. This tool is used when you have added or removed raster datasets from a mosaic dataset and want to recompute the footprints.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that contains the raster datasets whose footprints you want to compute."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select specific raster datasets within the mosaic dataset.",
                        "default": None
                },
                "reset_footprint": {
                        "type": "string",
                        "description": "Refine the footprints using one of the following methods:RADIOMETRY\u2014 Exclude pixels with a value outside of a defined  range. This option is generally used to exclude border areas, which do not contai...",
                        "default": None
                },
                "min_data_value": {
                        "type": "string",
                        "description": "Exclude pixels with a value less than this number.",
                        "default": None
                },
                "max_data_value": {
                        "type": "string",
                        "description": "Exclude pixels with a value greater than this number.",
                        "default": None
                },
                "approx_num_vertices": {
                        "type": "string",
                        "description": "Choose between 4 and 10,000. More vertices will improve accuracy but can extend processing time. A value of -1 will calculate all vertices. More vertices will increase accuracy but also the processing...",
                        "default": None
                },
                "shrink_distance": {
                        "type": "string",
                        "description": "Clip the footprint by this distance. This can eliminate artifacts from using lossy compression, which causes the edges of the image to overlap into NoData areas.Shrinking of the polygon is used to cou...",
                        "default": None
                },
                "maintain_edges": {
                        "type": "string",
                        "description": "Use this parameter when using raster datasets that have been tiled and are adjacent (line up along the seams with little to no overlap).NO_MAINTAIN_EDGES\u2014Remove the sheet edges from all the footprints...",
                        "default": None
                },
                "skip_derived_images": {
                        "type": "string",
                        "description": "Adjust the footprints of overviews.SKIP_DERIVED_IMAGES\u2014Do not adjust the footprints of overviews. This is the default. NO_SKIP_DERIVED_IMAGES\u2014Adjust the footprints of overviews and associated raster d...",
                        "default": None
                },
                "update_boundary": {
                        "type": "string",
                        "description": "Update the boundary of the mosaic dataset if you have added or removed imagery that changes the extent.UPDATE_BOUNDARY\u2014Update the boundary. This is the default.NO_BOUNDARY\u2014Do not update the boundary.",
                        "default": None
                },
                "request_size": {
                        "type": "string",
                        "description": "Set the resampled extent (in columns and rows) for the raster when building footprints. Greater image resolution provides more detail in the raster dataset but increases the processing time. A value o...",
                        "default": None
                },
                "min_region_size": {
                        "type": "string",
                        "description": "Avoid small holes in your imagery when using pixel values to create a mask. For example, your imagery may have a range of values from 0 to 255, and to mask clouds, you've excluded values from 245 to 2...",
                        "default": None
                },
                "simplification_method": {
                        "type": "string",
                        "description": "Reduce the number of vertices in the footprint to improve performance.NONE\u2014Do not limit the number of vertices. This is the default.CONVEX_HULL\u2014Use the minimum bounding box to simplify the footprint.E...",
                        "default": None
                },
                "edge_tolerance": {
                        "type": "string",
                        "description": "Snap the footprint to the sheet edge if it is within this tolerance. Units are the same as those in the mosaic dataset coordinate system. This is used when maintain_edges is set to MAINTAIN_EDGES.By d...",
                        "default": None
                },
                "max_sliver_size": {
                        "type": "string",
                        "description": "Identify all polygons that are smaller than the square of this value. The  value is specified in pixels and is based on the request_size, not  the spatial resolution of the source raster.Regions less ...",
                        "default": None
                },
                "min_thinness_ratio": {
                        "type": "string",
                        "description": "Define the thinness of slivers on a scale from 0 to 1.0, where 1.0 represents a circle and 0.0 represents a polygon that approaches a straight line. Polygons that are below both the max_sliver_size an...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "build_mosaic_dataset_item_cache": {
        "name": "build_mosaic_dataset_item_cache",
        "description": "Inserts the Cached Raster function as the final step in all function chains within a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset where you want to apply the cache function."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An  SQL expression to select  specific raster datasets within the mosaic dataset on which you want the item cache built.",
                        "default": None
                },
                "define_cache": {
                        "type": "string",
                        "description": "Choose to define the mosaic dataset cache. A Cached  Raster function will be inserted to the selected items. If an item already has a Cached Raster function, it will not add another one.DEFINE_CACHE\u2014T...",
                        "default": None
                },
                "generate_cache": {
                        "type": "string",
                        "description": "Choose to generate the cache files based on the properties defined in the Cached Raster function, such as the location and the compression of the cache.GENERATE_CACHE\u2014Cache will be generated. This is ...",
                        "default": None
                },
                "item_cache_folder": {
                        "type": "string",
                        "description": "Choose to overwrite the default location to save your cache. If the mosaic dataset is inside of a file geodatabase, by default, the cache is saved in a folder with the same name as the geodatabase and...",
                        "default": None
                },
                "compression_method": {
                        "type": "string",
                        "description": "Choose how you want to compress your data for faster transmission.LOSSLESS\u2014 Retain the values of each pixel when generating cache. Lossless has a compression ratio of approximately 2:1.LOSSY\u2014 Appropri...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "Set a compression quality when using the lossy method. The compression quality value is between 1 and 100 percent, with 100 compressing the least.",
                        "default": None
                },
                "max_allowed_rows": {
                        "type": "string",
                        "description": "Limit the size of the cache dataset by number of rows. If value is more than the number of rows in the dataset, the cache will not generate.",
                        "default": None
                },
                "max_allowed_columns": {
                        "type": "string",
                        "description": "Limit the size of the cache dataset by number of columns. If value is more than the number of columns in the dataset, the cache will not generate.",
                        "default": None
                },
                "request_size_type": {
                        "type": "string",
                        "description": "Resample the cache using one of these two methods:PIXEL_SIZE_FACTOR\u2014 Set a scaling factor relative to the pixel size. To not resample the cache, choose PIXEL_SIZE_FACTOR and set the request_size param...",
                        "default": None
                },
                "request_size": {
                        "type": "string",
                        "description": "Set a value to apply to the request_size_type.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "build_overviews": {
        "name": "build_overviews",
        "description": "Defines and generates overviews on a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset where you want to build overviews."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL statement to select specific rasters within the mosaic dataset.  The selected rasters will have their overview built.",
                        "default": None
                },
                "define_missing_tiles": {
                        "type": "string",
                        "description": "Identify where overviews are needed and define them.DEFINE_MISSING_TILES\u2014Automatically identify where overviews are needed and define them. This is the default.NO_DEFINE_MISSING_TILES\u2014 Do not define n...",
                        "default": None
                },
                "generate_overviews": {
                        "type": "string",
                        "description": "Generate all overviews that need to be created or re-created. This includes missing overviews and stale overviews.GENERATE_OVERVIEWS\u2014Generate all overviews, including those that already exist. This is...",
                        "default": None
                },
                "generate_missing_images": {
                        "type": "string",
                        "description": "Use if overviews have been defined but not generated.GENERATE_MISSING_IMAGES\u2014Generate overviews that have been defined but not generated. This is the default.IGNORE_MISSING_IMAGES\u2014 Do not generate ove...",
                        "default": None
                },
                "regenerate_stale_images": {
                        "type": "string",
                        "description": "Overviews become stale when you change the underlying raster datasets or modify their properties.REGENERATE_STALE_IMAGES\u2014Identify and regenerate stale overviews. This is the default.IGNORE_STALE_IMAGE...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "build_seamlines": {
        "name": "build_seamlines",
        "description": "Generate or update seamlines for your mosaic dataset. Seamlines are used to sort overlapping imagery and produce a smoother-looking mosaic. You can use this tool to do the following:",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "Select the mosaic dataset on which to build seamlines."
                },
                "cell_size": {
                        "type": "string",
                        "description": "Generate seamlines for raster datasets that fall within the following range of spatial resolutions.  You can leave this parameter empty and the tool will automatically create  seamlines at the appropr..."
                },
                "sort_method": {
                        "type": "string",
                        "description": "Set a rule to determine which raster will be used to generate seamlines when images overlap.NORTH_WEST\u2014 Select the raster datasets that have center points closest to the northwest corner of the bounda...",
                        "default": None
                },
                "sort_order": {
                        "type": "string",
                        "description": "Choose whether to sort the rasters in ascending order or descending order.ASCENDING\u2014 Sort the rasters in ascending order. This is the default.DESCENDING\u2014 Sort the rasters in descending order.",
                        "default": None
                },
                "order_by_attribute": {
                        "type": "string",
                        "description": "Order the raster datasets based on this field when the sort method is BY_ATTRIBUTE. The default attribute is ObjectID.",
                        "default": None
                },
                "order_by_base_value": {
                        "type": "string",
                        "description": "Sort the rasters by their difference between this value and their value in the order_by_attribute  parameter.",
                        "default": None
                },
                "view_point": {
                        "type": "string",
                        "description": "Set the coordinate location to use when sort_method  is CLOSEST_TO_VIEWPOINT.",
                        "default": None
                },
                "computation_method": {
                        "type": "string",
                        "description": "Choose how to build seamlines.GEOMETRY\u2014Generate seamlines for overlapping areas based on the intersection of footprints. Areas with no overlapping imagery will merge the footprints. This is the defaul...",
                        "default": None
                },
                "blend_width": {
                        "type": "string",
                        "description": "Blending (feathering) occurs along a seamline between pixels where there are overlapping rasters. The blend width defines how many pixels will be blended.If the blend width value is 10, and you use BO...",
                        "default": None
                },
                "blend_type": {
                        "type": "string",
                        "description": "Determine how to blend one image into another, over the seamlines. Options are to blend inside the seamlines, outside the seamlines, or both inside and outside.BOTH\u2014 Blend using pixels on either side ...",
                        "default": None
                },
                "request_size": {
                        "type": "string",
                        "description": "Specify the number of\r\ncolumns and rows for resampling. The maximum value is\r\n5,000. Increase or decrease this\r\nvalue based on the complexity of your raster data. Greater image\r\nresolution provides mo...",
                        "default": None
                },
                "request_size_type": {
                        "type": "string",
                        "description": "Set the units for the Request Size.PIXELS\u2014Modify the request size based on the pixel size.This is the default option and resamples the closest image based on the raster pixel size.PIXELSIZE_FACTOR\u2014Mod...",
                        "default": None
                },
                "blend_width_units": {
                        "type": "string",
                        "description": "Specify the unit of measurement for blend width.PIXELS\u2014Measure using the number of pixels. This is the default.GROUND_UNITS\u2014Measure using the same units as the mosaic dataset.",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "Build seamlines on all the rasters that intersect this polygon. To select an area of interest, use an input feature class.",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "SQL expression to build seamlines on specific raster datasets within the mosaic dataset.",
                        "default": None
                },
                "update_existing": {
                        "type": "string",
                        "description": "Update seamlines that are affected by the addition or deletion of  the mosaic dataset items.IGNORE_EXISTING\u2014Regenerates seamlines for all items and ignores existing seamlines, if any. This is the defa...",
                        "default": None
                },
                "min_region_size": {
                        "type": "string",
                        "description": "Specify the minimum region size, in pixel units. Any polygons smaller than this specified threshold will be  removed in the seamline result.\r\nThe default is 100 pixels.  This parameter value should be...",
                        "default": None
                },
                "min_thinness_ratio": {
                        "type": "string",
                        "description": "Define how thin a  polygon can be, before it is considered a sliver. This is based on a scale from 0 to 1.0, where a value of 0.0 represents a polygon that is almost a straight line, and a value of 1....",
                        "default": None
                },
                "max_sliver_size": {
                        "type": "string",
                        "description": "Specify the maximum size a polygon can be to still be considered a sliver. This parameter is specified in pixels and is based on the request_size, not the spatial resolution of the source raster. Any ...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "cell_size"
        ]
},
    "calculate_cell_size_ranges": {
        "name": "calculate_cell_size_ranges",
        "description": "Computes the visibility levels of raster datasets in a mosaic dataset based on the spatial resolution.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset to calculate the visibility levels for."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select specific rasters in the mosaic dataset on which to calculate visibility levels.  If no query is specified, all the mosaic dataset items will have their cell size ranges cal...",
                        "default": None
                },
                "do_compute_min": {
                        "type": "string",
                        "description": "Compute the minimum pixel size for each selected raster in the mosaic dataset.MIN_CELL_SIZES\u2014Compute the minimum pixel size. This is the default. NO_MIN_CELL_SIZES\u2014Do not compute the minimum pixel siz...",
                        "default": None
                },
                "do_compute_max": {
                        "type": "string",
                        "description": "Compute the maximum pixel size for each selected raster in the mosaic dataset.MAX_CELL_SIZES\u2014Compute the maximum pixel size. This is the default.NO_MAX_CELL_SIZES\u2014Do not compute the maximum pixel size...",
                        "default": None
                },
                "max_range_factor": {
                        "type": "string",
                        "description": "Set a multiplication factor to apply to the\r\nnative resolution. The default is 10, meaning that an image with a\r\nresolution of 30 meters will be visible at a\r\nscale appropriate for 300 meters. The rel...",
                        "default": None
                },
                "cell_size_tolerance_factor": {
                        "type": "string",
                        "description": "Use this to group images with similar resolutions as having the same nominal resolution. For example 1 m imagery and 0.9 m imagery can be grouped together by setting this factor to 0.1, because they a...",
                        "default": None
                },
                "update_missing_only": {
                        "type": "string",
                        "description": "Calculate only the missing cell size range values.UPDATE_ALL\u2014Calculate cell size minimum and maximum values for selected rasters within the mosaic dataset. This is the default.UPDATE_MISSING_ONLY\u2014 Cal...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "clear_pixel_cache": {
        "name": "clear_pixel_cache",
        "description": "Clears the pixel cache associated with a mosaic dataset. The pixel cache for a mosaic dataset can be generated by running the Add Rasters to Mosaic Dataset tool with the Enable Pixel Cache parameter checked. The pixel cache improves the performance when viewing and performing analysis on a mosaic that references rasters on cloud or slow Network  Attached  Storage  (NAS). The cache is stored on the local machine, improving performance.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset with the pixel cache to be deleted."
                },
                "generated_before": {
                        "type": "string",
                        "description": "All cache generated before this date will be deleted.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "color_balance_mosaic_dataset": {
        "name": "color_balance_mosaic_dataset",
        "description": "Color balances a mosaic dataset so that the tiles appear seamless.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that will be color balanced."
                },
                "balancing_method": {
                        "type": "string",
                        "description": "Specifies the balancing method that will be used. DODGING\u2014Each pixel's value will be changed toward a target color. With this method, you must also choose the type of target color surface, which affec...",
                        "default": None
                },
                "color_surface_type": {
                        "type": "string",
                        "description": "Specifies how the target color of each pixel will be determined.This parameter is enabled when the balancing_method parameter is set to DODGING.SINGLE_COLOR\u2014 All the pixels will be altered toward a si...",
                        "default": None
                },
                "target_raster": {
                        "type": "string",
                        "description": "The raster that will be used to color balance the other images. The balance method and color surface type, if applicable, will be derived from this image.",
                        "default": None
                },
                "exclude_raster": {
                        "type": "string",
                        "description": "A raster that identifies the locations that will be excluded.Create a mask using the Generate Exclude Area tool.",
                        "default": None
                },
                "stretch_type": {
                        "type": "string",
                        "description": "Specifies how the range of values will be stretched before color balancing.NONE\u2014 The original pixel values will be used. This is the default.ADAPTIVE\u2014 An adaptive prestretch will be applied before any...",
                        "default": None
                },
                "gamma": {
                        "type": "string",
                        "description": "A numeric value that will adjust the overall brightness of an image. A low value will minimize the contrast between moderate values by making them appear darker. Higher values will increase the contra...",
                        "default": None
                },
                "block_field": {
                        "type": "string",
                        "description": "A field in the mosaic dataset's attribute table\r\nthat will be used to identify items that will be considered one item when performing some calculations and operations.",
                        "default": None
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "A DEM to help estimate the overlapped locations in the mosaic dataset.This parameter is enabled when the balancing_method parameter is set to GLOBAL_FIT.",
                        "default": None
                },
                "zfactor": {
                        "type": "string",
                        "description": "A conversion factor that adjusts the units of measure for the vertical (or elevation) units when they are different from the horizontal coordinate (x,y) units of the input surface DEM. It is the numbe...",
                        "default": None
                },
                "zoffset": {
                        "type": "string",
                        "description": "A base value that will be added to the elevation value in the DEM. This can be used to offset elevation values that do not start at sea level.This parameter is enabled when the in_DEM_raster parameter...",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the geoid correction required by rational polynomial coefficients ( RPC) that reference ellipsoidal heights will be made. Most elevation datasets are referenced to sea level orthomet...",
                        "default": None
                },
                "solution_points": {
                        "type": "string",
                        "description": "The solution points from block adjustment output to help accurately estimate the overlapped locations. This parameter is helpful when the image has less than 50 percent overlap with its neighbors. Usi...",
                        "default": None
                },
                "target_objectid": {
                        "type": "string",
                        "description": "The target raster object ID that will be used to color balance the other images. The balance method and color surface type, if applicable, will be derived from this image.This parameter is enabled whe...",
                        "default": None
                },
                "refine_estimation": {
                        "type": "string",
                        "description": "Specifies whether the color balancing estimation for corresponding locations in the overlapped areas will be refined using image correlation. This parameter is helpful for the exact color difference c...",
                        "default": None
                },
                "reduce_shadow": {
                        "type": "string",
                        "description": "Specifies whether the negative influence of shadows on the color balance output will be reduced.This parameter is enabled when the balancing_method parameter is set to GLOBAL_FIT.NO_REDUCE_SHADOW\u2014The ...",
                        "default": None
                },
                "reduce_cloud": {
                        "type": "string",
                        "description": "Specifies whether the negative influence of clouds on the color balance output will be reduced. This parameter is active when the balancing_method parameter is set to DODGING or GLOBAL_FIT.NO_REDUCE_C...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "compute_dirty_area": {
        "name": "compute_dirty_area",
        "description": "Identifies areas within a mosaic dataset that have changed since a specified point in time. This is used commonly when a mosaic dataset is updated or synchronized, or when  derived products, such as cache, need to be updated. This tool will enable you to limit such processes to only the areas that have changed.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that you want to analyze for changes."
                },
                "where_clause": {
                        "type": "string",
                        "description": "SQL expression to select specific rasters  within the mosaic dataset  on which to compute dirty areas.",
                        "default": None
                },
                "timestamp": {
                        "type": "string",
                        "description": "Compute the areas that have changed since the input time.XML time syntax:YYYY-MM-DDThh:mm:ssYYYY-MM-DDThh:mm:ss.ssssZ2002-10-10T12:00:00.ssss-00:002002-10-10T12:00:00+00:00Non-XML time syntax:2002/12/..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the areas that have changed."
                }
        },
        "required": [
                "in_mosaic_dataset",
                "timestamp",
                "out_feature_class"
        ]
},
    "compute_mosaic_candidates": {
        "name": "compute_mosaic_candidates",
        "description": "Finds the image candidates in a mosaic dataset that best represent the mosaic area. Densely overlapped images are necessary in many projects but may make it difficult to determine which images in a mosaic dataset should be used in an analysis. This tool finds the optimal images based on areas of maximum overlap and area excluded. The input mosaic dataset will include a new Candidate field in the mosaic dataset footprint table. This field determines which images will be used in certain operations, such as color balancing,  seamline generation, ortho mapping, and mosaic methods.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset with densely overlapped images."
                },
                "maximum_overlap": {
                        "type": "string",
                        "description": "The maximum amount of overlap between the mosaic dataset and the footprint of each image in the mosaic dataset. If the percentage of overlap is greater than this threshold, the image is excluded since...",
                        "default": None
                },
                "maximum_area_loss": {
                        "type": "string",
                        "description": "The maximum percentage of area that can be excluded by the candidate images. After the tool finds the best candidate images based on the maximum_overlap parameter value, it checks whether the maximum ...",
                        "default": None
                },
                "maximum_obliqueness_angle": {
                        "type": "string",
                        "description": "The maximum image obliqueness angle\r\nthat will be used to filter images. Any image with an obliqueness angle\r\nlarger than this value will not be used as a candidate. This parameter is measured in degr...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "create_mosaic_dataset": {
        "name": "create_mosaic_dataset",
        "description": "Creates an empty mosaic dataset in a geodatabase.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The path to the geodatabase.Starting at ArcGIS Pro 1.4, mosaic datasets created in Oracle, PostgreSQL, and SQL Server geodatabases will be created with the RASTERBLOB keyword. The RASTERBLOB keyword i..."
                },
                "in_mosaicdataset_name": {
                        "type": "string",
                        "description": "The name of the new mosaic dataset."
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system that will be used for all of the items in the mosaic dataset."
                },
                "num_bands": {
                        "type": "string",
                        "description": "The number of bands the raster datasets will have in the mosaic dataset.",
                        "default": None
                },
                "pixel_type": {
                        "type": "string",
                        "description": "Specifies the bit depth, or radiometric resolution, that will be used for the mosaic dataset. If not defined, the pixel type of the first raster dataset will be used.1_BIT\u2014The pixel type will be a 1-b...",
                        "default": None
                },
                "product_definition": {
                        "type": "string",
                        "description": "Specifies whether a template is specific to the type of imagery you are working with or is generic. The generic options include the following standard raster data types:NONE\u2014No band ordering is specif...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "in_mosaicdataset_name",
                "coordinate_system"
        ]
},
    "create_referenced_mosaic_dataset": {
        "name": "create_referenced_mosaic_dataset",
        "description": "Creates a separate mosaic dataset from items in an existing mosaic dataset.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset from which items will be selected."
                },
                "out_mosaic_dataset": {
                        "type": "string",
                        "description": "The referenced mosaic dataset to be created."
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The projection for the output mosaic dataset.",
                        "default": None
                },
                "number_of_bands": {
                        "type": "string",
                        "description": "The number of bands that the referenced mosaic dataset will have.",
                        "default": None
                },
                "pixel_type": {
                        "type": "string",
                        "description": "The bit depth, or radiometric resolution, of the mosaic dataset. If this is not defined, it will be taken from the first raster dataset.\r\n1_BIT\u2014The pixel type will be a 1-bit unsigned integer. The val...",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select raster datasets that will be included in the output mosaic dataset.",
                        "default": None
                },
                "in_template_dataset": {
                        "type": "string",
                        "description": "Select raster datasets based on the extent of another image or feature class. Raster datasets that lay along the defined extent will be included in the mosaic dataset. To manually input the minimum an...",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "The minimum and maximum coordinates for the extent.",
                        "default": None
                },
                "select_using_features": {
                        "type": "string",
                        "description": "Limit the extent to the shape or envelope when a feature class is specified in the in_template_dataset parameter.\r\nSELECT_USING_FEATURES\u2014Select using  the shape of the feature. This is the default.NO_...",
                        "default": None
                },
                "lod_field": {
                        "type": "string",
                        "description": "Legacy:This parameter has been deprecated and is ignored in tool execution.  It remains for backward compatibility reasons.",
                        "default": None
                },
                "minps_field": {
                        "type": "string",
                        "description": "Specify a field from the footprint  attribute table that defines the minimum cell size for displaying the mosaic dataset; otherwise, only a footprint will be displayed.",
                        "default": None
                },
                "maxps_field": {
                        "type": "string",
                        "description": "Specify a field from the footprint  attribute table that defines the maximum cell size for displaying the mosaic dataset; otherwise, only a footprint will be displayed.",
                        "default": None
                },
                "pixelsize": {
                        "type": "string",
                        "description": "Set a maximum cell size to display the mosaic  instead of specifying a field. If you zoom out beyond this cell size, only the footprint will be displayed.",
                        "default": None
                },
                "build_boundary": {
                        "type": "string",
                        "description": "Rebuild the boundary. If the selection covers a smaller area than the source mosaic dataset, this is recommended.This is only available if the mosaic dataset is created in a geodatabase.BUILD_BOUNDARY...",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_mosaic_dataset"
        ]
},
    "define_mosaic_dataset_nodata": {
        "name": "define_mosaic_dataset_nodata",
        "description": "Specifies one or more values to be represented as NoData.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset where you want to update the NoData values."
                },
                "num_bands": {
                        "type": "string",
                        "description": "The number of bands in the mosaic dataset."
                },
                "bands_for_nodata_valueband_nodata_value": {
                        "type": "string",
                        "description": "Define values for each or all bands. Each band can have a unique NoData value defined, or the same value can be specified for all bands. If you want to define multiple NoData values for each band sele...",
                        "default": None
                },
                "bands_for_valid_data_rangeband_minimum_value_maximum_value": {
                        "type": "string",
                        "description": "Specify a range of values to display for each band. Values outside of this range will be classified as NoData. When working with composite bands, the range will apply to all bands.",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL statement to select specific raster in the mosaic dataset.  Only the selected rasters will have their NoData values changed.",
                        "default": None
                },
                "composite_nodata_value": {
                        "type": "string",
                        "description": "Choose whether all bands must be NoData in order for the pixel to be classified as NoData.NO_COMPOSITE_NODATA\u2014If any of the bands  have pixels of NoData, then the pixel is classified as NoData. This i...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "num_bands"
        ]
},
    "define_overviews": {
        "name": "define_overviews",
        "description": "Lets you set how mosaic dataset overviews are generated. The settings made with this tool are used by the Build Overviews tool.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that you want to build overviews on."
                },
                "overview_image_folder": {
                        "type": "string",
                        "description": "The folder or geodatabase to store the overviews.",
                        "default": None
                },
                "in_template_dataset": {
                        "type": "string",
                        "description": "A raster dataset or feature class to define the extent of the overviews.",
                        "default": None
                },
                "extent": {
                        "type": "string",
                        "description": "Set the extent using minimum and maximum x and y coordinates. This is specified as space delimited in the following order: X-minimum X-maximum Y-minimum Y-maximum. The mosaic dataset boundary will det...",
                        "default": None
                },
                "pixel_size": {
                        "type": "string",
                        "description": "If you prefer not to use all the raster's pyramids, specify a base pixel size at which your overviews will be generated.The units for this parameter are the same as the spatial reference of the mosaic...",
                        "default": None
                },
                "number_of_levels": {
                        "type": "string",
                        "description": "Specify the number of levels of overviews that you want to generate overviews. A value of -1 will determine an optimal value for you.",
                        "default": None
                },
                "tile_rows": {
                        "type": "string",
                        "description": "Set the number of rows (in pixels) for each tile.Larger values will result in fewer, larger individual overviews, and increase the likelihood that you will need to regenerate lower level overviews. A ...",
                        "default": None
                },
                "tile_cols": {
                        "type": "string",
                        "description": "Set the number of columns (in pixels) for each tile.Larger values will result in fewer, larger individual overviews, and increase the likelihood that you will need to regenerate lower level overviews....",
                        "default": None
                },
                "overview_factor": {
                        "type": "string",
                        "description": "Set a ratio to determine the size of the next overview. For example, if the cell size of the first level is 10, and the overview factor is 3, then the next overview pixel size will be 30.",
                        "default": None
                },
                "force_overview_tiles": {
                        "type": "string",
                        "description": "Generate overviews at all levels, or only\r\nabove existing pyramid levels.NO_FORCE_OVERVIEW_TILES\u2014Create overviews above the raster pyramid levels. This is the default.FORCE_OVERVIEW_TILES\u2014  Create ove...",
                        "default": None
                },
                "resampling_method": {
                        "type": "string",
                        "description": "Choose an algorithm for aggregating pixel values in the overviews.NEAREST\u2014The fastest resampling method because it minimizes changes to pixel values. Suitable for discrete data, such as land cover. If...",
                        "default": None
                },
                "compression_method": {
                        "type": "string",
                        "description": "Define the type of data compression to store the overview images.JPEG\u2014A lossy compression. This is the default, unless the Raster Metadata Data Type is thematic. This compression method is only valid ...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "Choose a value from 1 - 100. Higher values generate better quality\r\noutputs, but they create larger files.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "delete_mosaic_dataset": {
        "name": "delete_mosaic_dataset",
        "description": "Deletes a mosaic dataset, its overviews, and its item cache from disk.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that you want to delete."
                },
                "delete_overview_images": {
                        "type": "string",
                        "description": "Delete all overviews associated with the mosaic dataset.DELETE_OVERVIEW_IMAGES\u2014Delete the overviews associated with the mosaic dataset. This is the default.NO_DELETE_OVERVIEW_IMAGES\u2014Do not delete the ...",
                        "default": None
                },
                "delete_item_cache": {
                        "type": "string",
                        "description": "Delete the item cache associated with the mosaic dataset.DELETE_ITEM_CACHE\u2014Delete the item cache associated with the mosaic dataset. This is the default.NO_DELETE_ITEM_CACHE\u2014Do not delete the item cac...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "edit_raster_function": {
        "name": "edit_raster_function",
        "description": "Adds, replaces, or removes a function chain in a mosaic dataset or a raster layer that contains a raster function.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset or a raster layer. If you use a raster layer, it must have a function applied."
                },
                "edit_mosaic_dataset_item": {
                        "type": "string",
                        "description": "Determines if edits affect functions or the entire mosaic dataset.EDIT_MOSAIC_DATASET\u2014Edits affect the functions associated with the mosaic dataset. This is the default. EDIT_MOSAIC_DATASET_ITEM\u2014Edits...",
                        "default": None
                },
                "function_chain_definition": {
                        "type": "string",
                        "description": "Choose the function chain (rft.xml file) that you want to insert or replace.",
                        "default": None
                },
                "location_function_name": {
                        "type": "string",
                        "description": "Choose where to insert, replace, or remove the function chain within the existing function chain.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "export_mosaic_dataset_geometry": {
        "name": "export_mosaic_dataset_geometry",
        "description": "Creates a feature class showing the footprints, boundary, seamlines or spatial resolutions of a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that you want to export the geometry from."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to export specific rasters in the mosaic dataset.",
                        "default": None
                },
                "geometry_type": {
                        "type": "string",
                        "description": "The type of geometry to export. FOOTPRINT\u2014 Create a feature class showing the footprints of each image.BOUNDARY\u2014 Create a feature class showing the boundary of the mosaic dataset.SEAMLINE\u2014 Create a fe...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "export_mosaic_dataset_items": {
        "name": "export_mosaic_dataset_items",
        "description": "Saves a copy of processed images in a mosaic dataset to a specified folder and raster file format. The following are the two common workflows that use this tool: \r\nExport each selected item of a mosaic dataset to a new file. This allows you to have each processed item as a stand-alone file. You must set the appropriate NoData value for the exported items so there are no dark borders.Export each selected image within a time series mosaic dataset based on an area of interest. This allows you to only export the area of interest from each time slice.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that contains the images that will be exported."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The folder where the images will be saved."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will be used to save selected images in the mosaic dataset. For more information about SQL syntax, see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                },
                "format": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the output raster datasets.TIFF\u2014TIFF format will be used. This is the default.Cloud Optimized GeoTIFF\u2014Cloud Optimized GeoTIFF format will be used.BMP\u2014BMP for...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "All the pixels with the specified value will be set to NoData in the output raster dataset.It is recommended that you specify a NoData value if the output images will be clipped.",
                        "default": None
                },
                "clip_type": {
                        "type": "string",
                        "description": "Specifies the output extent that will be used for the raster datasets. If you specify an extent or feature class that covers an area larger than the raster data, the output will have the larger extent...",
                        "default": None
                },
                "template_dataset": {
                        "type": "string",
                        "description": "The feature class or bounding box that will be used to limit the extent.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent ...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The horizontal (x) and vertical (y) dimensions of the output cells.If the cell size is not provided, the spatial resolution of the input will be used.",
                        "default": None
                },
                "image_space": {
                        "type": "string",
                        "description": "Specifies whether raster items will be exported in map space or image space.MAPSPACE\u2014Raster items will be exported in map space. This is the default.IMAGESPACE\u2014Raster items will be exported in image s...",
                        "default": None
                },
                "remove_distortion": {
                        "type": "string",
                        "description": "Specifies whether lens distortion will be removed from the exported raster in image space.REMOVED\u2014Lens distortion will be removed from the exported raster in image space.\r\nNOTREMOVE\u2014Lens distortion wi...",
                        "default": None
                },
                "band_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to select bands.This parameter is enabled  when the image_space parameter is set to IMAGESPACE.ALL_BANDS\u2014All bands will be exported. This is the default.BAND_IDS...",
                        "default": None
                },
                "band_name_selection": {
                        "type": "string",
                        "description": "The name of the band that will be exported from the input mosaic dataset.\r\nThis parameter is enabled when the band_method parameter is set to BAND_NAMES.",
                        "default": None
                },
                "band_id_selection": {
                        "type": "string",
                        "description": "The ID number of the band that will be exported from the input mosaic dataset.\r\nThis parameter is enabled when the band_method parameter is set to BAND_IDS.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "out_folder"
        ]
},
    "export_mosaic_dataset_paths": {
        "name": "export_mosaic_dataset_paths",
        "description": "Creates a table of the file path for each item in a mosaic dataset. You can specify whether the table contains all the file paths or just the ones that are broken.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset containing the file paths to export."
                },
                "out_table": {
                        "type": "string",
                        "description": "The table to create. The table can be a geodatabase table or a .dbf file.The SourceOID field in the output table is derived from the OID of the row in the original mosaic dataset table."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select specific rasters for export.",
                        "default": None
                },
                "export_mode": {
                        "type": "string",
                        "description": "Populate the table with either all of the paths, or only the broken paths.ALL\u2014Export all  paths to the table. This is the default.BROKEN\u2014Export only  broken paths to the table.",
                        "default": None
                },
                "types_of_pathstype_of_path": {
                        "type": "string",
                        "description": "Choose to export file paths from only the source raster, only the cache, or both. The default is to export all path types.RASTER\u2014Export file paths from rasters.ITEM_CACHE\u2014Export file paths from item c...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "out_table"
        ]
},
    "generate_exclude_area": {
        "name": "generate_exclude_area",
        "description": "Masks pixels based on their color or by clipping a range of values. The output of this tool is used as an input to the Color Balance Mosaic Dataset tool to eliminate areas such as clouds and water that can skew the statistics used to color balance multiple images.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster or mosaic dataset layer that you want to mask."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location and format for the dataset you are creating. When storing a raster dataset in a geodatabase, do not add a file extension to the name of the raster dataset. When storing your raster ..."
                },
                "pixel_type": {
                        "type": "string",
                        "description": "Choose the pixel depth of your input raster dataset. 8-bit is the default value; however, raster datasets with a greater bit-depth will need to have the color mask and histogram values scaled accordin..."
                },
                "generate_method": {
                        "type": "string",
                        "description": "Create your mask based on the color of the pixels or by clipping high and low values.COLOR_MASK\u2014Set the maximum color values to include in the output. This is the default.HISTOGRAM_PERCENTAGE\u2014Remove a..."
                },
                "max_red": {
                        "type": "string",
                        "description": "The maximum red value to exclude. The default is 255.",
                        "default": None
                },
                "max_green": {
                        "type": "string",
                        "description": "The maximum green value to exclude. The default is 255.",
                        "default": None
                },
                "max_blue": {
                        "type": "string",
                        "description": "The maximum blue value to exclude. The default is 255.",
                        "default": None
                },
                "max_white": {
                        "type": "string",
                        "description": "The maximum white value to exclude. The default is 255.",
                        "default": None
                },
                "max_black": {
                        "type": "string",
                        "description": "The maximum black value to exclude. The default is 0.",
                        "default": None
                },
                "max_magenta": {
                        "type": "string",
                        "description": "The maximum magenta value to exclude. The default is 255.",
                        "default": None
                },
                "max_cyan": {
                        "type": "string",
                        "description": "The maximum cyan value to exclude. The default is 255.",
                        "default": None
                },
                "max_yellow": {
                        "type": "string",
                        "description": "The maximum yellow value to exclude. The default is 255.",
                        "default": None
                },
                "percentage_low": {
                        "type": "string",
                        "description": "Exclude this percentage of the lowest pixel values. The default is 0.",
                        "default": None
                },
                "percentage_high": {
                        "type": "string",
                        "description": "Exclude this percentage of the highest pixel values. The default is 100.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "pixel_type",
                "generate_method"
        ]
},
    "generate_raster_collection": {
        "name": "generate_raster_collection",
        "description": "Performs batch analysis or processing on image collections contained in a mosaic dataset. The images in the input mosaic dataset can be processed individually or as groups. The rules of processing can be defined through the Collection Builder parameter and raster function parameters. It generates a new mosaic dataset of processed images. You can optionally choose to save the processed images to disk as separate files. The default condition  is to append the input raster function to the mosaic dataset's existing images' function chain, and add it to the output mosaic dataset.",
        "parameters": {
                "out_raster_collection": {
                        "type": "string",
                        "description": "The full path of the mosaic dataset to be created. The mosaic dataset  must be stored in a geodatabase."
                },
                "collection_builder": {
                        "type": "string",
                        "description": "The input image collection. It can be seen as a template\r\nthat contains arguments such as the source mosaic dataset path,\r\nfilters to extract a subset from the input data source, and so on.Currently, ..."
                },
                "raster_function": {
                        "type": "string",
                        "description": "The path to a raster function template file (.rft.xml or .rft.json). The raster function template will be applied to every item in the input mosaic dataset. The Function Editor can be used to create t...",
                        "default": None
                },
                "generate_rasters": {
                        "type": "string",
                        "description": "Choose to generate raster dataset files of the mosaic dataset items, after the application of the RFT.\r\nNO_GENERATE_RASTERS\u2014The processing defined by the raster function template will be appended to t...",
                        "default": None
                },
                "out_workspace": {
                        "type": "string",
                        "description": "Defines the output location for the persisted raster datasets, if the generate_rasters parameter is set to GENERATE_RASTERS.  The naming convention for the output raster files\r\nis oid_&lt;oid#&gt;_&lt...",
                        "default": None
                },
                "format": {
                        "type": "string",
                        "description": "The format type of the raster to be generated.TIFF\u2014Tagged Image File Format (TIFF)IMAGINE Image\u2014ERDAS IMAGINE fileCRF\u2014Cloud Raster Format. This is the default.MRF\u2014Meta Raster Format",
                        "default": None
                },
                "out_base_name": {
                        "type": "string",
                        "description": "Defines the output base name for the persisted raster datasets, if the generate_rasters parameter is set to GENERATE_RASTERS.",
                        "default": None
                }
        },
        "required": [
                "out_raster_collection",
                "collection_builder"
        ]
},
    "import_mosaic_dataset_geometry": {
        "name": "import_mosaic_dataset_geometry",
        "description": "Modifies the geometry for the footprints, boundary, or seamlines in a mosaic dataset to match those in a feature class.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset whose geometries you want to edit."
                },
                "target_featureclass_type": {
                        "type": "string",
                        "description": "The geometry that you want to change.FOOTPRINT\u2014The footprint polygons in the mosaic datasetSEAMLINE\u2014The seamline polygons in the mosaic datasetBOUNDARY\u2014The boundary polygon in the mosaic dataset"
                },
                "target_join_field": {
                        "type": "string",
                        "description": "The field in the mosaic dataset to use as a basis for the join."
                },
                "input_featureclass": {
                        "type": "string",
                        "description": "The feature class with the new geometry."
                },
                "input_join_field": {
                        "type": "string",
                        "description": "The field in the input_featureclass to use as a basis for the join.If the input_featureclass has more than 1,000 records, add an index on this field by running the Add_Attribute_Index tool. If your mo..."
                }
        },
        "required": [
                "in_mosaic_dataset",
                "target_featureclass_type",
                "target_join_field",
                "input_featureclass",
                "input_join_field"
        ]
},
    "merge_mosaic_dataset_items": {
        "name": "merge_mosaic_dataset_items",
        "description": "Groups multiple items in a mosaic dataset together as one item.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that has the items that you want to merge."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select specific rasters to merge  in the mosaic dataset.",
                        "default": None
                },
                "block_field": {
                        "type": "string",
                        "description": "The field in the attribute table that you want to use to group images. Only date, numeric, and string fields can be specified as Block fields.",
                        "default": None
                },
                "max_rows_per_merged_items": {
                        "type": "string",
                        "description": "Limits the number of items to merge. If the maximum is exceeded, the tool will create multiple merged items. The default is 1,000 rows.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "mosaic_dataset_to_mobile_mosaic_dataset": {
        "name": "mosaic_dataset_to_mobile_mosaic_dataset",
        "description": "Converts a mosaic dataset into a mobile mosaic dataset that's compatible with ArcGIS Maps SDKs for Native Apps. A mobile mosaic dataset resides in a mobile geodatabase.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that will be converted to a mobile mosaic dataset."
                },
                "out_mobile_gdb": {
                        "type": "string",
                        "description": "The  geodatabase where the converted mosaic dataset will be created."
                },
                "mosaic_dataset_name": {
                        "type": "string",
                        "description": "The name of the mobile mosaic dataset that will be created."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will be used to select specific items to add to the mobile mosaic dataset.",
                        "default": None
                },
                "selection_feature": {
                        "type": "string",
                        "description": "The mosaic dataset items that will be included in the output based on the extent of another image or feature class. Items that lay along the defined extent will be included in the mosaic dataset. They...",
                        "default": None
                },
                "out_data_folder": {
                        "type": "string",
                        "description": "The folder where a copy of the source data will be created. If the convert_rasters parameter is set to ALWAYS, any raster functions associated with the mosaic dataset will be processed before creating...",
                        "default": None
                },
                "convert_rasters": {
                        "type": "string",
                        "description": "Specifies whether the raster functions associated with the input mosaic dataset will be converted before creating the mobile mosaic dataset. If you have raster functions that are not supported by Nati...",
                        "default": None
                },
                "out_name_prefix": {
                        "type": "string",
                        "description": "Appends a prefix to each item, which is copied or converted into the output data folder.",
                        "default": None
                },
                "format": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the rasters  written to the output data folder.TIFF\u2014The TIFF format will be used.PNG\u2014The PNG format will be used.JPEG\u2014The JPEG format will be used.JP2\u2014The JP...",
                        "default": None
                },
                "compression_method": {
                        "type": "string",
                        "description": "Specifies the compression method that will be used for transmitting the mosaicked image from the computer to the display (or from the server to the client).NONE\u2014No compression will be used.JPEG\u2014Compre...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "The compression quality level, which is a value from 0 to 100. A higher number means better image quality but less compression. This parameter only applies when the format parameter is specified as JP...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "out_mobile_gdb",
                "mosaic_dataset_name"
        ]
},
    "remove_rasters_from_mosaic_dataset": {
        "name": "remove_rasters_from_mosaic_dataset",
        "description": "Removes selected rasters from a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset containing the rasters that will be removed."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select the raster datasets that will be removed from the mosaic dataset.You must specify a  selection or a query; otherwise, the tool will not run. To delete all the records from ...",
                        "default": None
                },
                "update_boundary": {
                        "type": "string",
                        "description": "Specifies whether the boundary polygon of the mosaic dataset will be updated. By default, the boundary merges all the footprint polygons to create a single boundary representing the extent of the vali...",
                        "default": None
                },
                "mark_overviews_items": {
                        "type": "string",
                        "description": "Specifies whether affected overviews will be identified.When the rasters in a mosaic dataset have been removed, overviews created using those rasters may no longer be accurate. Use this parameter to i...",
                        "default": None
                },
                "delete_overview_images": {
                        "type": "string",
                        "description": "Specifies whether the overviews associated with the selected rasters will be removed.DELETE_OVERVIEW_IMAGES\u2014The overviews associated with the selected rasters will be deleted. This is the default.NO_D...",
                        "default": None
                },
                "delete_item_cache": {
                        "type": "string",
                        "description": "Specifies whether the cache that is based on any source raster dataset that will be removed from the mosaic dataset will also be removed.DELETE_ITEM_CACHE\u2014The cache that is based on any source raster ...",
                        "default": None
                },
                "remove_items": {
                        "type": "string",
                        "description": "Specifies whether mosaic dataset items will be removed.REMOVE_MOSAICDATASET_ITEMS\u2014Mosaic dataset items will be removed.  This is the default.NO_REMOVE_MOSAICDATASET_ITEMS\u2014Mosaic dataset  items will no...",
                        "default": None
                },
                "update_cellsize_ranges": {
                        "type": "string",
                        "description": "Specifies whether the cell size ranges for the mosaic dataset will be updated.UPDATE_CELL_SIZES\u2014The cell size ranges for the mosaic dataset will be updated. Use this if you are removing all of the ima...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "repair_mosaic_dataset_paths": {
        "name": "repair_mosaic_dataset_paths",
        "description": "Resets paths to source imagery if you have moved or copied a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset with the broken paths."
                },
                "paths_listoriginal_path_new_path": {
                        "type": "string",
                        "description": "A \r\nlist of the paths to remap. Include the current path stored in the mosaic dataset and the path to which it will be changed. You can enter an asterisk (*) as the original path if you wish to change..."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to limit the repairs to selected rasters within the mosaic dataset.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "paths_listoriginal_path_new_path"
        ]
},
    "set_mosaic_dataset_properties": {
        "name": "set_mosaic_dataset_properties",
        "description": "Defines the defaults for displaying a mosaic dataset and serving it as an image service.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset with the properties that will be set."
                },
                "rows_maximum_imagesize": {
                        "type": "string",
                        "description": "The maximum number of rows for the mosaicked image, generated by the mosaic dataset for each request. This can help control how much work the server has to do when clients view the imagery. A higher n...",
                        "default": None
                },
                "columns_maximum_imagesize": {
                        "type": "string",
                        "description": "The maximum number of columns for the mosaicked image, generated by the mosaic dataset for each request. This can help control how much work the server has to do when clients view the imagery. A highe...",
                        "default": None
                },
                "allowed_compressions": {
                        "type": "string",
                        "description": "Specifies the compression methods that will be used to transmit the mosaicked image from the computer to the display (or from the server to the client).None\u2014No compression will be used.JPEG\u2014 Compressi...",
                        "default": None
                },
                "default_compression_type": {
                        "type": "string",
                        "description": "Specifies the default compression type. The default compression must be in the list of values used for the allowed_compressions parameter or must be set in the mosaic dataset's Allowed Compression Met...",
                        "default": None
                },
                "jpeg_quality": {
                        "type": "string",
                        "description": "The compression quality when using JPEG. Compression quality ranges from 1 to 100. A higher number means better image quality but less compression.",
                        "default": None
                },
                "lerc_tolerance": {
                        "type": "string",
                        "description": "The maximum per pixel error when using LERC compression. This value is specified in the units of the mosaic dataset. For example, if the error is 10 centimeters and the mosaic dataset is in meters, en...",
                        "default": None
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Specifies how pixel values will be calculated when the dataset is displayed at small scales. Choose an appropriate technique based on the type of data.NEAREST\u2014The value of each pixel will be from the ...",
                        "default": None
                },
                "clip_to_footprints": {
                        "type": "string",
                        "description": "Specifies whether rasters will be clipped to the footprint. Often the raster dataset and its footprint have the same extent. If they differ, the raster dataset can be clipped to the footprint.NOT_CLIP...",
                        "default": None
                },
                "footprints_may_contain_nodata": {
                        "type": "string",
                        "description": "Specifies whether pixels with NoData values will be shown.FOOTPRINTS_MAY_CONTAIN_NODATA\u2014Pixels with NoData values will be shown. This is the default.FOOTPRINTS_DO_NOT_CONTAIN_NODATA\u2014Pixels with NoData...",
                        "default": None
                },
                "clip_to_boundary": {
                        "type": "string",
                        "description": "Specifies whether the mosaicked image will be clipped to the boundary. Often the mosaic dataset and its boundary have the same extent. If they differ, the mosaic dataset can be clipped to the boundary...",
                        "default": None
                },
                "color_correction": {
                        "type": "string",
                        "description": "Specifies whether color correction will be used on the mosaic dataset.NOT_APPLY\u2014Color correction will not be used. This is the default.APPLY\u2014The color correction that has been set up for the mosaic da...",
                        "default": None
                },
                "allowed_mensuration_capabilities": {
                        "type": "string",
                        "description": "Specifies the measurements that will be performed on the mosaic dataset. The ability to perform vertical measurements is dependent on the imagery and may require a DEM.None\u2014No mensuration capabilities...",
                        "default": None
                },
                "default_mensuration_capabilities": {
                        "type": "string",
                        "description": "Specifies the default mensuration capability for the mosaic dataset. The default mensuration value must be set in the list of values used for the allowed_mensuration_capabilities parameter or be set i...",
                        "default": None
                },
                "allowed_mosaic_methods": {
                        "type": "string",
                        "description": "Specifies the rules for displaying overlapping imagery.None\u2014Rasters will be ordered based on the ObjectID field in the mosaic dataset attribute table.Center\u2014Imagery that is closest to the center of th...",
                        "default": None
                },
                "default_mosaic_method": {
                        "type": "string",
                        "description": "Specifies the default mosaic method that will be used for the mosaic dataset. The default mosaic method must be set in the list of values used for the allowed_mosaic_methods parameter or be set in the...",
                        "default": None
                },
                "order_field": {
                        "type": "string",
                        "description": "The field that will be used when ordering rasters using the ByAttribute value of the default_mosaic_method parameter. The list of fields is defined as those in the attribute table that are of type met...",
                        "default": None
                },
                "order_base": {
                        "type": "string",
                        "description": "Sorts the rasters based on their difference from this value in the field selected in the order_field parameterIf a Date attribute is used, it must be in one of the following formats:YYYY/MM/DD HH:mm:s...",
                        "default": None
                },
                "sorting_order": {
                        "type": "string",
                        "description": "Specifies whether the rasters will be sorted in an ascending or a descending order.ASCENDING\u2014Rasters will be sorted in an ascending order. This is the default.DESCENDING\u2014Rasters will be sorted in a de...",
                        "default": None
                },
                "mosaic_operator": {
                        "type": "string",
                        "description": "Specifies the rule that will be used for resolving overlapping pixels.FIRST\u2014The first image in the attribute table will be displayed.LAST\u2014The last image in the attribute table will be displayed.MIN\u2014Th...",
                        "default": None
                },
                "blend_width": {
                        "type": "string",
                        "description": "The number of pixels to which the BLEND  value of the mosaic_operator parameter will be applied.",
                        "default": None
                },
                "view_point_x": {
                        "type": "string",
                        "description": "A numeric value that will be used to horizontally shift the center of the image. The units are the same as the spatial reference system.This parameter is only applicable if the allowed_mosaic_methods ...",
                        "default": None
                },
                "view_point_y": {
                        "type": "string",
                        "description": "A numeric value that will be used to vertically shift the center of the image. The units are the same as the spatial reference system.This parameter is only applicable if the allowed_mosaic_methods pa...",
                        "default": None
                },
                "max_num_per_mosaic": {
                        "type": "string",
                        "description": "The maximum number of raster datasets that will be displayed at a given time in a mosaic dataset.",
                        "default": None
                },
                "cell_size_tolerance": {
                        "type": "string",
                        "description": "The maximum pixel size difference that is allowed before images are considered to have a different cell pixel.This allows images of similar spatial resolutions to be considered as having the same nomi...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the mosaic dataset using an existing raster dataset or its specified width (x) and height (y). If you specify the cell size, you can use a single value for a square cell size, or x an...",
                        "default": None
                },
                "metadata_level": {
                        "type": "string",
                        "description": "Specifies the level of metadata that will be exposed from the server to a client when publishing the mosaic dataset.FULL\u2014Metadata regarding the processing applied at the mosaic dataset level as well a...",
                        "default": None
                },
                "use_time": {
                        "type": "string",
                        "description": "Specifies whether the mosaic dataset will be time aware. If time is activated, the start and end fields and the time format must be specified.DISABLED\u2014The mosaic dataset will not be time aware. This i...",
                        "default": None
                },
                "start_time_field": {
                        "type": "string",
                        "description": "The field in the attribute table that shows the start time.",
                        "default": None
                },
                "end_time_field": {
                        "type": "string",
                        "description": "The field in the attribute table that shows the end time.",
                        "default": None
                },
                "time_format": {
                        "type": "string",
                        "description": "Specifies the time format that will be used for the mosaic dataset for parameters such as start_time_field and end_time_field.YYYY\u2014The time format will be year.YYYYMM\u2014The time format will be year and ...",
                        "default": None
                },
                "geographic_transform": {
                        "type": "string",
                        "description": "The geographic transformations that will be associated with the mosaic dataset.",
                        "default": None
                },
                "max_num_of_download_items": {
                        "type": "string",
                        "description": "The maximum number of raster datasets that will be downloaded per request.",
                        "default": None
                },
                "max_num_of_records_returned": {
                        "type": "string",
                        "description": "The maximum number of records that will be downloaded per request.",
                        "default": None
                },
                "data_source_type": {
                        "type": "string",
                        "description": "Specifies the type of imagery in the mosaic dataset.GENERIC\u2014The mosaic dataset contains no specified data type.THEMATIC\u2014The mosaic dataset contains thematic data with discrete values, such as land cov...",
                        "default": None
                },
                "minimum_pixel_contribution": {
                        "type": "string",
                        "description": "The minimum number of pixels required for a mosaic dataset item to be considered significant enough to be used in the mosaic dataset. Because of overlapping imagery, an item may display only a small s...",
                        "default": None
                },
                "processing_templates": {
                        "type": "string",
                        "description": "The function chains that will be used to process a mosaic dataset or the mosaic dataset items on the fly. You can add, remove, or reorder the function chains. All the template names that are added mus...",
                        "default": None
                },
                "default_processing_template": {
                        "type": "string",
                        "description": "The default function chain. The default function chain will be applied when the mosaic dataset is accessed.",
                        "default": None
                },
                "time_interval": {
                        "type": "string",
                        "description": "The duration of each time step interval.\r\nThe time step interval defines the granularity of the temporal data. The unit of time is specified in the time_interval_units parameter.",
                        "default": None
                },
                "time_interval_units": {
                        "type": "string",
                        "description": "Specifies the measurement unit that will be used for the time interval.\r\nNone\u2014No time unit exists or it is unknown.Milliseconds\u2014The time unit will be milliseconds.Seconds\u2014The time unit will be seconds...",
                        "default": None
                },
                "product_definition": {
                        "type": "string",
                        "description": "Specifies a template that is either specific to the type of imagery you are working with or generic. The generic options include the standard supported raster sensor types as follows:NONE\u2014No band orde...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "split_mosaic_dataset_items": {
        "name": "split_mosaic_dataset_items",
        "description": "Splits mosaic dataset items that were merged together using Merge Mosaic Dataset Items.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset containing the items to split."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select items to split.If the query does not contain any previously merged items, the tool will return an error.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "synchronize_mosaic_dataset": {
        "name": "synchronize_mosaic_dataset",
        "description": "Synchronizes a mosaic dataset to keep it up to date. In addition to syncing data, you can update overviews if the underlying imagery has been changed, generate new overviews and cache, and restore the original configuration of mosaic dataset items. You can also remove paths to source data with this tool. To repair paths, use the Repair Mosaic Dataset Paths  tool. Synchronization is a one-way operation: changes in the source data can be \r\nsynchronized to the mosaic dataset\u2019s attribute table, thereby updating the mosaic dataset's attribute table.  Changes in the mosaic dataset's attribute table will not affect the source data. Changes made by synchronization cannot be undone. Create a backup  of your mosaic dataset if you've made modifications to the data that you don't want overwritten.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that will be synchronized."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select which mosaic dataset items will be synchronized.  If an expression is not provided, all dataset items will be updated.",
                        "default": None
                },
                "new_items": {
                        "type": "string",
                        "description": "Specifies whether new items will be included when synchronizing as well as the options to use to update the new items.If you use this option, the item's workspace will be searched for new data. When d...",
                        "default": None
                },
                "sync_only_stale": {
                        "type": "string",
                        "description": "Specifies whether mosaic dataset items will be updated only when the underlying raster datasets have been modified due to synchronizing. For example, building pyramids or updating the georeferencing o...",
                        "default": None
                },
                "update_cellsize_ranges": {
                        "type": "string",
                        "description": "Specifies whether cell size ranges for the mosaic dataset will be recalculated. UPDATE_CELL_SIZES\u2014The cell size ranges for the entire mosaic dataset will be recalculated, but only for items that have ...",
                        "default": None
                },
                "update_boundary": {
                        "type": "string",
                        "description": "Specifies whether the boundary that shows the full extent of the mosaic dataset will be rebuilt. Choose  UPDATE_BOUNDARY if syncing will change the extent of the mosaic dataset.UPDATE_BOUNDARY\u2014 The bo...",
                        "default": None
                },
                "update_overviews": {
                        "type": "string",
                        "description": "Specifies whether obsolete overviews will be updated. The overview becomes obsolete if any underlying  rasters have been modified due to synchronizing.NO_OVERVIEWS\u2014 The overviews will not be updated. ...",
                        "default": None
                },
                "build_pyramids": {
                        "type": "string",
                        "description": "Specifies whether pyramids will be built for the specified mosaic dataset items. Pyramids can be built for each raster item in the mosaic dataset. Pyramids can improve the speed at which each raster i...",
                        "default": None
                },
                "calculate_statistics": {
                        "type": "string",
                        "description": "Specifies whether statistics will be calculated for the specified mosaic dataset items. Statistics are required for a mosaic dataset when performing certain tasks, such as applying a contrast stretch....",
                        "default": None
                },
                "build_thumbnails": {
                        "type": "string",
                        "description": "Specifies whether thumbnails will be built for the specified mosaic dataset items. Thumbnails are small, highly resampled images that can be created for each raster item in the mosaic definition. Thum...",
                        "default": None
                },
                "build_item_cache": {
                        "type": "string",
                        "description": "Choose whether to build a cache for the specified mosaic dataset items. A cache can be built when you've added data using the LAS, Terrain, or LAS dataset raster types. NO_ITEM_CACHE\u2014A cache  will not...",
                        "default": None
                },
                "rebuild_raster": {
                        "type": "string",
                        "description": "Specifies whether the raster items will be rebuilt from the data source using the original raster type.REBUILD_RASTER\u2014The rasters will be rebuilt from the source data.  Any changes that you have perfo...",
                        "default": None
                },
                "update_fields": {
                        "type": "string",
                        "description": "Specifies whether the fields in the table will be updated. This only affects items that will be synchronized.UPDATE_FIELDS\u2014The fields will be updated from the source files.  This is the default.NO_FIE...",
                        "default": None
                },
                "fields_to_updatefield_to_update": {
                        "type": "string",
                        "description": "The fields that will be updated. This parameter is only valid if the update_fields parameter  is set to UPDATE_FIELDS.If you made edits to some of the fields, make sure they are not listed.The RASTER ...",
                        "default": None
                },
                "existing_items": {
                        "type": "string",
                        "description": "Specifies whether existing items in the mosaic dataset will be updated.If you use this parameter, choose which existing parameters to update: sync_only_stale, build_pyramids, calculate_statistics, bui...",
                        "default": None
                },
                "broken_items": {
                        "type": "string",
                        "description": "Specifies whether items with broken links will be removed.Ensure that all network connections are working properly. This tool will remove any items that cannot be accessed.IGNORE_BROKEN_ITEMS\u2014Items wi...",
                        "default": None
                },
                "skip_existing_items": {
                        "type": "string",
                        "description": "Specifies whether existing mosaic dataset items will be skipped or updated with the modified files from disk. To use this parameter, the new_items parameter must be set to UPDATE_WITH_NEW_ITEMS.SKIP_E...",
                        "default": None
                },
                "refresh_aggregate_info": {
                        "type": "string",
                        "description": "Specifies whether data that may have been removed from the mosaic dataset will be included.\r\nTo use this parameter, the existing_items parameter must be set to IGNORE_EXISTING_ITEMS.NO_REFRESH_INFO\u2014Wh...",
                        "default": None
                },
                "estimate_statistics": {
                        "type": "string",
                        "description": "Specifies whether statistics on the mosaic dataset will be estimated.\r\nNO_STATISTICS\u2014When synchronizing, statistics on the mosaic dataset will not be estimated. This is the default.ESTIMATE_STATISTICS..."
                }
        },
        "required": [
                "in_mosaic_dataset",
                "estimate_statistics"
        ]
},
    "analyze_control_points": {
        "name": "analyze_control_points",
        "description": "Analyzes the control point coverage and identifies the areas that need additional control points to improve the block adjust result. The tool will check each image and provide the following:The number of control points\r\nfor each imageThe percentage of image covered by the control\r\npoints (point distribution)The overlap\r\nareasThe number of control\r\npoints within overlap areas",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset against which to analyze the control points."
                },
                "in_control_points": {
                        "type": "string",
                        "description": "The input control point feature class.It is normally created from the Compute Tie Points or the Compute Control Points tool."
                },
                "out_coverage_table": {
                        "type": "string",
                        "description": "A polygon feature class output that contains the control point coverage and the percentage of the area within the corresponding image."
                },
                "out_overlap_table": {
                        "type": "string",
                        "description": "A polygon feature class output that contains all the overlap areas between images."
                },
                "in_mask_dataset": {
                        "type": "string",
                        "description": "A polygon feature class used to exclude areas that you do not want in the analysis of the control points computation.The mask field can control the inclusion or exclusion of areas. A value of 1 indica...",
                        "default": None
                },
                "minimum_area": {
                        "type": "string",
                        "description": "Specify the minimum percent that the overlap area must be, in relation to the image. Areas that are lower than the specified percent threshold will be excluded from the analysis. Ensure that you do no...",
                        "default": None
                },
                "maximum_level": {
                        "type": "string",
                        "description": "The maximum \r\nnumber of images that can be overlapped when analyzing the control points.For example, if there are four images in your mosaic dataset, and a maximum overlap value of 3 was specified, th...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "in_control_points",
                "out_coverage_table",
                "out_overlap_table"
        ]
},
    "append_control_points": {
        "name": "append_control_points",
        "description": "Combines control points to an existing control point table. The points to be appended are the results from either the Compute Tie Points tool or the Compute Control Points tool, or a point feature class.",
        "parameters": {
                "in_master_control_points": {
                        "type": "string",
                        "description": "The input control point table. This is usually the output from the Compute Tie Points tool."
                },
                "in_input_control_points": {
                        "type": "string",
                        "description": "A point feature class that stores control points. It could be the control point table created from the Compute Control Points tool, the Compute Tie Points tool, or a point feature class that has groun..."
                },
                "in_tag_field": {
                        "type": "string",
                        "description": "A field in the input control point table that has a unique value. This field will be added to the target control point table, where the tag field can be used to bring in identifiers associated with gr...",
                        "default": None
                },
                "in_xy_accuracy": {
                        "type": "string",
                        "description": "The input accuracy for the X and Y coordinates. The accuracy is in the same units as the in_input_control_points.This information should be provided by the data provider. If the accuracy  information ...",
                        "default": None
                },
                "in_z_accuracy": {
                        "type": "string",
                        "description": "The input accuracy for the  vertical coordinates.\r\nThe accuracy is in the units of the in_input_control_points.This information should be provided by the data provider. If the accuracy  information is...",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "The geoid correction is required by  rational polynomial coefficients (RPC) that reference ellipsoidal heights. Most elevation datasets are referenced to sea level orthometric heights, so this correct...",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "Defines an area of interest  extent by entering minimum and maximum x- and y-coordinates in the spatial reference of the input control point table.",
                        "default": None
                },
                "append_option": {
                        "type": "string",
                        "description": "Specifies how control points will be appended to the control point table.ALL\u2014Add all points in the input control point table to the target control point table, including GCPs, check points, and all ti...",
                        "default": None
                }
        },
        "required": [
                "in_master_control_points",
                "in_input_control_points"
        ]
},
    "apply_block_adjustment": {
        "name": "apply_block_adjustment",
        "description": "Applies the geographic adjustments to the mosaic dataset items. This tool uses the solution table from the Compute Block Adjustments tool. This tool can also reset the geographic adjustments back to the original location.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset to adjust."
                },
                "adjustment_operation": {
                        "type": "string",
                        "description": "Specifies whether the mosaic dataset will be adjusted using the solution table or whether the mosaic dataset will be reset so there are no adjustments applied.ADJUST\u2014The mosaic dataset will be adjuste..."
                },
                "input_solution_table": {
                        "type": "string",
                        "description": "The solution table that will be used when adjusting the mosaic dataset. This is the output from the Compute Block Adjustments tool.",
                        "default": None
                },
                "pan_to_ms_scaling_factor": {
                        "type": "string",
                        "description": "The scaling factor between the pan-sharpened resolution and the multispectral resolution that will be used if the mosaic dataset contains pan-sharpened rasters.",
                        "default": None
                },
                "dem": {
                        "type": "string",
                        "description": "The DEM that will be used in the block adjustment. This DEM will only be used if it is a higher resolution than any existing DEM in the mosaic dataset.\r\n If this input DEM is used, the geometric funct...",
                        "default": None
                },
                "zoffset": {
                        "type": "string",
                        "description": "The  vertical offset that will be used to adjust the \r\nelevation layer within the mosaic dataset's Geometric function.",
                        "default": None
                },
                "control_point_table": {
                        "type": "string",
                        "description": "The input control point table that will have the same adjustments applied as the solution table adjustments.",
                        "default": None
                },
                "adjust_footprints": {
                        "type": "string",
                        "description": "Specifies whether the footprint \r\ngeometry will be updated using the same transformation that will be applied to the image.NO_ADJUST_FOOTPRINTS\u2014The footprint geometry will not be updated. This is the ...",
                        "default": None
                },
                "solution_point_table": {
                        "type": "string",
                        "description": "The solution point table that will be used to update the status field for the control point table. This parameter is only used when the control_point_table parameter value is provided.",
                        "default": None
                },
                "adjust_tiepoints": {
                        "type": "string",
                        "description": "Specifies whether the tie points will be updated when a solution point table is provided. This parameter is only used when the solution_point_table parameter value is provided.\r\nNO_ADJUST_TIEPOINTS\u2014Th...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "adjustment_operation"
        ]
},
    "compute_block_adjustments": {
        "name": "compute_block_adjustments",
        "description": "Computes the adjustments to the mosaic dataset. This tool will create a solution table that can be used to apply the actual adjustments.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset that will be adjusted."
                },
                "in_control_points": {
                        "type": "string",
                        "description": "The control point table that includes tie points and ground control points.This feature class is usually the output from the  Compute Tie Points tool."
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Specifies the type of transformation that will be used when adjusting the mosaic dataset.\r\nPOLYORDER0\u2014A zero-order polynomial will be used in the block adjustment computation. This is commonly used wh..."
                },
                "out_solution_table": {
                        "type": "string",
                        "description": "The output solution table containing the adjustments."
                },
                "out_solution_point_table": {
                        "type": "string",
                        "description": "The output solution points table. This will be saved as a polygon feature class. This output can be quite large.",
                        "default": None
                },
                "maximum_residual_value": {
                        "type": "string",
                        "description": "A threshold that is used in block adjustment computation; points with residuals exceeding the threshold will not be used. This parameter applies when the   transformation type is POLYORDER0,  POLYORDE...",
                        "default": None
                },
                "adjustment_optionsname_value": {
                        "type": "string",
                        "description": "Additional options that will be used to fine-tune the adjustment computation.Note:To set an option in the Geoprocessing pane, type the keyword and the corresponding value in the list box.MinResidual\u2014T...",
                        "default": None
                },
                "location_accuracy": {
                        "type": "string",
                        "description": "Specifies the geometric accuracy level of the images.This parameter is only enabled if the transformation_type parameter is specified as RPC.HIGH\u2014The accuracy will be 30 meters or less.MEDIUM\u2014The accu...",
                        "default": None
                },
                "out_quality_table": {
                        "type": "string",
                        "description": "An output  table used to store adjustment\r\nquality information.\r\nThis parameter is only enabled if the transformation_type parameter is specified as RPC.",
                        "default": None
                },
                "dem": {
                        "type": "string",
                        "description": "An input DEM from which elevations will be sampled as ground control\r\npoints for refining the geometric accuracy of the image network in\r\nthe adjustment.This parameter is only enabled when the transfo...",
                        "default": None
                },
                "elevation_accuracy": {
                        "type": "string",
                        "description": "The elevation accuracy of the input DEM. The accuracy value will be used as a weight for the sampled ground control points in the adjustment.This parameter is only enabled when the transformation_type...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "in_control_points",
                "transformation_type",
                "out_solution_table"
        ]
},
    "build_stereo_model": {
        "name": "build_stereo_model",
        "description": "Builds a stereo model of a mosaic dataset based on a user-provided stereo pair. A stereo model of a mosaic dataset is required for stereo feature collection and 3D point cloud generation.  A stereo model, as one of the tables in a mosaic dataset, defines the stereo pairs. The stereo model stores the overlapping polygons, the corresponding image identifiers, and image IDs that comprise each pair. The stereo model can be accessed from the context menu of a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset on which the stereo model will be built.Tip:Running the Apply Block Adjustment tool on the input mosaic dataset first will help create a more accurate stereo model."
                },
                "minimum_angle": {
                        "type": "string",
                        "description": "The value, in degrees, that defines the minimum angle the stereo pair must meet. The default is 10.",
                        "default": None
                },
                "maximum_angle": {
                        "type": "string",
                        "description": "The value, in degrees, that defines the maximum angle the stereo pair must meet. The default is 90.",
                        "default": None
                },
                "minimum_overlap": {
                        "type": "string",
                        "description": "The percentage of the overlapping area over the whole image. The default is 0.5.",
                        "default": None
                },
                "maximum_diff_op": {
                        "type": "string",
                        "description": "The maximum threshold for the Omega and Phi difference between the two image pairs. The Omega values and Phi values for the  image pairs are compared. If the difference between either the two Omega or...",
                        "default": None
                },
                "maximum_diff_gsd": {
                        "type": "string",
                        "description": "The threshold for the maximum GSD between two images in a pair. If the resolution ratio between the two images is greater than the threshold value, the pairs will not be built as a stereo pair. The de...",
                        "default": None
                },
                "group_by": {
                        "type": "string",
                        "description": "Builds the stereo model from raster items within the same group, defined by a mosaic dataset field such as RGB, Panchromatic, or Infrared.",
                        "default": None
                },
                "same_flight": {
                        "type": "string",
                        "description": "Specifies how the stereo models will be selected.SAMEFLIGHT\u2014Stereo pairs will be selected along the same flight line.NO_SAMEFLIGHT\u2014Stereo pairs will be selected across flight lines.Note:This parameter...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "compute_block_adjustment": {
        "name": "compute_block_adjustment",
        "description": "Computes the adjustments to the mosaic dataset. This tool will create a solution table that can be used to apply the actual adjustments.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset that will be adjusted."
                },
                "in_control_points": {
                        "type": "string",
                        "description": "The control point table that includes tie points and ground control points.This feature class is usually the output from the  Compute Tie Points tool."
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Specifies the type of transformation that will be used when adjusting the mosaic dataset.\r\nPOLYORDER0\u2014A zero-order polynomial will be used in the block adjustment computation. This is commonly used wh..."
                },
                "out_solution_table": {
                        "type": "string",
                        "description": "The output solution table containing the adjustments."
                },
                "out_solution_point_table": {
                        "type": "string",
                        "description": "The output solution points table. This will be saved as a polygon feature class. This output can be quite large.",
                        "default": None
                },
                "maximum_residual_value": {
                        "type": "string",
                        "description": "A threshold that is used in block adjustment computation; points with residuals exceeding the threshold will not be used. This parameter applies when the   transformation type is POLYORDER0,  POLYORDE...",
                        "default": None
                },
                "adjustment_optionsname_value": {
                        "type": "string",
                        "description": "Additional options that will be used to fine-tune the adjustment computation.Note:To set an option in the Geoprocessing pane, type the keyword and the corresponding value in the list box.MinResidual\u2014T...",
                        "default": None
                },
                "location_accuracy": {
                        "type": "string",
                        "description": "Specifies the geometric accuracy level of the images.This parameter is only enabled if the transformation_type parameter is specified as RPC.HIGH\u2014The accuracy will be 30 meters or less.MEDIUM\u2014The accu...",
                        "default": None
                },
                "out_quality_table": {
                        "type": "string",
                        "description": "An output  table used to store adjustment\r\nquality information.\r\nThis parameter is only enabled if the transformation_type parameter is specified as RPC.",
                        "default": None
                },
                "dem": {
                        "type": "string",
                        "description": "An input DEM from which elevations will be sampled as ground control\r\npoints for refining the geometric accuracy of the image network in\r\nthe adjustment.This parameter is only enabled when the transfo...",
                        "default": None
                },
                "elevation_accuracy": {
                        "type": "string",
                        "description": "The elevation accuracy of the input DEM. The accuracy value will be used as a weight for the sampled ground control points in the adjustment.This parameter is only enabled when the transformation_type...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "in_control_points",
                "transformation_type",
                "out_solution_table"
        ]
},
    "compute_camera_model": {
        "name": "compute_camera_model",
        "description": "Estimates the exterior camera model and interior camera model from the EXIF header of the raw image and refines the camera models. The model is then applied to the mosaic dataset with an option to use a tool-generated, high-resolution digital surface model (DSM) to achieve better orthorectification. This is especially helpful for UAV and UAS images in which the exterior and interior camera models are coarse or undefined.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset on which the camera model will be built and calculated."
                },
                "out_dsm": {
                        "type": "string",
                        "description": "A DSM raster dataset generated from the adjusted images in the mosaic dataset. If apply_adjustment is set to APPLY, this DSM will replace the DEM in the geometric function to achieve better orthorecti...",
                        "default": None
                },
                "gps_accuracy": {
                        "type": "string",
                        "description": "Specifies the accuracy level of the input images. The tool will search for images in the neighborhood to compute matching points and automatically apply an adjustment strategy based on the accuracy le...",
                        "default": None
                },
                "estimate": {
                        "type": "string",
                        "description": "Specifies whether the camera model will be estimated by computing the adjustment based on eight times the mosaic dataset's source resolution. Computing the adjustment at this level will be faster but ...",
                        "default": None
                },
                "refine": {
                        "type": "string",
                        "description": "Specifies whether the camera model will be refined by computing the adjustment at the mosaic dataset resolution. Computing the adjustment at this level will provide the most accurate result.REFINE\u2014The...",
                        "default": None
                },
                "apply_adjustment": {
                        "type": "string",
                        "description": "Specifies whether the calculated adjustment will be applied to the input mosaic dataset.APPLY\u2014The calculated adjustment will be applied to the input mosaic dataset. Although not required, it is recomm...",
                        "default": None
                },
                "maximum_residual": {
                        "type": "string",
                        "description": "The maximum residual value allowed to keep a computed control point as a valid control point. The default is 5.",
                        "default": None
                },
                "initial_tiepoint_resolution": {
                        "type": "string",
                        "description": "The resolution factor at which tie points will be generated when estimating the camera model. The default value is 8, which means eight times the source pixel resolution.For images with only minor dif...",
                        "default": None
                },
                "out_control_points": {
                        "type": "string",
                        "description": "The optional control points feature class.",
                        "default": None
                },
                "out_solution_table": {
                        "type": "string",
                        "description": "The optional adjustment solution table. The solution table contains the root mean square (RMS) of the adjustment error and solution matrix.",
                        "default": None
                },
                "out_solution_point_table": {
                        "type": "string",
                        "description": "The optional solution point feature class. The solution points are the final controls points used to generate the adjustment solution.",
                        "default": None
                },
                "out_flight_path": {
                        "type": "string",
                        "description": "The optional flight path line feature class.",
                        "default": None
                },
                "maximum_overlap": {
                        "type": "string",
                        "description": "The percentage of overlap between two images to consider them duplicates.For example, if the value is 0.9, it means if an image is 90 percent covered by another image, it will be considered a duplicat...",
                        "default": None
                },
                "minimum_coverage": {
                        "type": "string",
                        "description": "The percentage indicating the control point's coverage on an image. If the coverage is less than the minimum percentage, the image will\r\nbe unresolved and removed.\r\nThe default is 0.",
                        "default": None
                },
                "remove": {
                        "type": "string",
                        "description": "Specifies whether images will be automatically removed if they are too far from the flight strip.NO_REMOVE\u2014Images will not be removed. This is the default.REMOVE\u2014Images that are too far away from the ...",
                        "default": None
                },
                "in_control_points": {
                        "type": "string",
                        "description": "The tie point table that will be used to compute the camera model. If no tie point table is provided, the tool will compute the tie points and estimate the camera model.",
                        "default": None
                },
                "options": {
                        "type": "string",
                        "description": "Additional options for the adjustment engine. The specifications of many of the options are supplied by the data provider.The options include the following:CalibrateF\u2014The sensor's focal length will be...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "compute_control_points": {
        "name": "compute_control_points",
        "description": "Creates the control points between the mosaic dataset and the reference image. The control points can then be used in conjunction with tie points to compute the adjustments for the mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset that will be used to create control points."
                },
                "in_reference_images": {
                        "type": "string",
                        "description": "The reference images that will be used to create control points for your mosaic dataset. If you have multiple images, create a mosaic dataset from the images and use the mosaic dataset as the referenc..."
                },
                "out_control_points": {
                        "type": "string",
                        "description": "The output \r\ncontrol point table. This table will contain the control points that were created."
                },
                "similarity": {
                        "type": "string",
                        "description": "Specifies the similarity level that will be used for matching tie points.LOW\u2014The similarity criteria for the two matching points will be low. This option will  produce the most matching points, but so...",
                        "default": None
                },
                "out_image_feature_points": {
                        "type": "string",
                        "description": "The output image feature points table. This will be saved as a polygon feature class.\r\nThis output can be quite large.",
                        "default": None
                },
                "density": {
                        "type": "string",
                        "description": "Specifies the number of tie points to be created.\r\nLOW\u2014The density of points will be low, creating the fewest number of tie points.MEDIUM\u2014The density of points will be medium, creating a moderate numb..."
                },
                "distribution": {
                        "type": "string",
                        "description": "Specifies whether the points will have regular or random distribution. RANDOM\u2014Points will be generated randomly. Randomly generated points are better for overlapping areas\r\nwith irregular shapes.REGUL..."
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "Limit the area in which tie points are generated to only this polygon feature class."
                },
                "location_accuracy": {
                        "type": "string",
                        "description": "Specifies the keyword that describes the accuracy of the imagery.LOW\u2014Images have a large shift and a large rotation (&gt; 5 degrees).The SIFT algorithm will be used in the point-matching computation.M...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "in_reference_images",
                "out_control_points",
                "density",
                "distribution",
                "area_of_interest"
        ]
},
    "compute_depth_map": {
        "name": "compute_depth_map",
        "description": "Computes a more accurate CenterZ field value based on the depth map for each image comprising a mosaic dataset. Control points and solution points are used to compute a depth map for each image comprising a mosaic dataset to improve image-to-ground (map) transformation, especially in high oblique cases. Image inspection, typically performed in image space, allows you to discover defects, perform measurement, and generate inspection reports for rectified imagery.  You can measure distance, area, and height of objects in either map space or image space, and an inspection report can be generated to share the inspection results. An important component of the inspection workflow is the transformation from image to ground (map) space, that allows the defects, points, lines, polygons, on images to be more accurately located and measured. The image-to-ground transformation, especially for high oblique images, uses a depth map, which is the distance from the camera location to the ground location for each pixel.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The block adjusted input mosaic dataset.  The mosaic dataset must be adjusted before it is used as input for this tool. You can use an ortho mapping workflow in ArcGIS Pro, or a Reality for ArcGIS Pro..."
                },
                "control_point_table": {
                        "type": "string",
                        "description": "The input control point feature class. This point feature class is the output of the Compute Camera Model tool or the Compute Tie Points tool."
                },
                "solution_point_table": {
                        "type": "string",
                        "description": "The input solution point feature class. This point feature class is the output of the Compute Camera Model tool or the Compute Tie Points tool."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will be used to select items in the mosaic dataset to include in the depth map.",
                        "default": None
                },
                "skip_existing": {
                        "type": "string",
                        "description": "Specifies whether a depth map CenterZ value will be computed only for rasters without a CenterZ value, or computed for all mosaic dataset items including those with an existing CenterZ value.NO_SKIP_E...",
                        "default": None
                },
                "adjust_footprints": {
                        "type": "string",
                        "description": "Specifies whether the footprint \r\ngeometry will be updated using the same transformation that was applied to the image.NO_ADJUST_FOOTPRINTS\u2014The footprint geometry will not be updated. This is the defa...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "control_point_table",
                "solution_point_table"
        ]
},
    "compute_fiducials": {
        "name": "compute_fiducials",
        "description": "Computes the fiducial coordinates in image and film space for each image in a mosaic dataset. Fiducials are marks, normally four or eight, in aerial photos used as reference. They are an important factor for determining the image transformation from image to film known as interior orientation. This tool is used to automatically find the image coordinates of the fiducials for each images in a mosaic dataset based on a user-provided fiducial template file. A fiducial template file is a table that has required fields for storing either fiducial pictures or paths to the pictures. For more information about fiducials, see Refine Interior Orientation Using Fiducials.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset created from scanned aerial photos using scanned raster type or frame camera raster type."
                },
                "out_fiducial_table": {
                        "type": "string",
                        "description": "The output  table that stores all the fiducial coordinate information in image and film space."
                },
                "where_clause": {
                        "type": "string",
                        "description": "A query definition string that defines a subset of rasters for computing fiducials.",
                        "default": None
                },
                "fiducial_templates": {
                        "type": "string",
                        "description": "The\r\nfiducial template table that contains required fields for storing fiducial pictures and other properties.",
                        "default": None
                },
                "film_coordinate_system": {
                        "type": "string",
                        "description": "A keyword that defines the film coordinate system of the scanned aerial photograph.  It is used in computing fiducial information and affine transformation construction.\r\nNO_CHANGE\u2014Maintain the coordi...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "out_fiducial_table"
        ]
},
    "compute_tie_points": {
        "name": "compute_tie_points",
        "description": "Computes the tie points between overlapped mosaic dataset items. The tie points can then be used to compute the block adjustments for the mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset that will be used to create tie points."
                },
                "out_control_points": {
                        "type": "string",
                        "description": "The output control point table. The table will contain the tie points created by this tool."
                },
                "similarity": {
                        "type": "string",
                        "description": "Specifies the similarity level that will be used for matching tie points.LOW\u2014The similarity criteria for the two matching points will be low. This option will  produce the most matching points, but so...",
                        "default": None
                },
                "in_mask_dataset": {
                        "type": "string",
                        "description": "A polygon feature class used to exclude areas that will not be included in the computation of control points. The mask field can control the inclusion or exclusion of areas. A value of 1 indicates tha...",
                        "default": None
                },
                "out_image_features": {
                        "type": "string",
                        "description": "The output image feature points table. This will be saved as a polygon feature class.\r\nThis output can be quite large.",
                        "default": None
                },
                "density": {
                        "type": "string",
                        "description": "Specifies the number of tie points to be created.\r\nLOW\u2014The density of points will be low, creating the fewest number of tie points.MEDIUM\u2014The density of points will be medium, creating a moderate numb..."
                },
                "distribution": {
                        "type": "string",
                        "description": "Specifies whether the points will have regular or random distribution. RANDOM\u2014Points will be generated randomly. Randomly generated points are better for overlapping areas\r\nwith irregular shapes.REGUL..."
                },
                "location_accuracy": {
                        "type": "string",
                        "description": "Specifies the keyword that describes the accuracy of the imagery.LOW\u2014Images have a large shift and a large rotation (&gt; 5 degrees).The SIFT algorithm will be used in the point-matching computation.M..."
                },
                "options": {
                        "type": "string",
                        "description": "Additional options for the adjustment engine. The options are only used by third-party adjustment engines.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "out_control_points",
                "density",
                "distribution",
                "location_accuracy"
        ]
},
    "export_frame_and_camera_parameters": {
        "name": "export_frame_and_camera_parameters",
        "description": "Exports frame and camera parameters from a mosaic dataset that contains frame imagery.",
        "parameters": {
                "input_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset."
                },
                "output_file": {
                        "type": "string",
                        "description": "The output file containing the  frame and camera parameters. Supported file formats  include .csv and .txt."
                },
                "output_format": {
                        "type": "string",
                        "description": "Specifies the output file format for the frame and camera parameters.ESRI_FRAME_AND_CAMERA_TABLE\u2014The frame and camera parameters will be exported as an Esri  Frames and Camera table (.csv file). This ...",
                        "default": None
                }
        },
        "required": [
                "input_mosaic_dataset",
                "output_file"
        ]
},
    "generate_block_adjustment_report": {
        "name": "generate_block_adjustment_report",
        "description": "Generates a  report after performing an ortho mapping block adjustment on a mosaic dataset. The report is useful when evaluating the quality and accuracy of the ortho mapping products.",
        "parameters": {
                "input_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset path."
                },
                "input_solution_table": {
                        "type": "string",
                        "description": "The associated solution point table after block adjustment."
                },
                "input_solution_point": {
                        "type": "string",
                        "description": "The solution point feature class."
                },
                "output_report": {
                        "type": "string",
                        "description": "The output ortho mapping report file path and name. The supported output format for a website is HTML."
                },
                "input_control_point_for_adjustment": {
                        "type": "string",
                        "description": "The associated control points table, which may include tie points and ground control points.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the output format of the block\r\nadjustment report.HTML\u2014The adjustment report will be created in HTML format. This is the default.PDF\u2014The adjustment report will be created in PDF format.JSON\u2014...",
                        "default": None
                }
        },
        "required": [
                "input_mosaic_dataset",
                "input_solution_table",
                "input_solution_point",
                "output_report"
        ]
},
    "generate_point_cloud": {
        "name": "generate_point_cloud",
        "description": "Generates 3D points from stereo pairs and outputs a point cloud as a set of LAS files. The tiling of the LAS files is based on 1,000 by 1,000 ground spacing. The points in each LAS tile are computed by selecting pairs, based on user-defined criteria, and filter points from the selected pairs. The input of this tool is  a mosaic dataset that contains a stereo model. The output of this tool can be used to generate a digital terrain model (DTM) or a digital surface model (DSM).",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The input mosaic dataset, which must have completed the block adjustment process and have a stereo model.To block adjust the mosaic dataset, use the Apply Block Adjustment tool.  To build a stereo mod..."
                },
                "matching_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to generate 3D points.ETM\u2014Extended terrain matching, a feature-based\r\nstereo matching in which the Harris operator is used in detecting\r\nfeature points, will be ..."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The folder used to store the output LAS files, including cloud storage.If this tool is run multiple times with the same input parameters, the output may be slightly different due to random sampling."
                },
                "out_base_name": {
                        "type": "string",
                        "description": "A string used as a prefix to formulate the output LAS file names. For example, if name is used as the base, the output files will be named name1.las, name2.las, and so on."
                },
                "object_size": {
                        "type": "string",
                        "description": "A search radius within which surface objects, such as buildings or trees, will be identified. It is the linear size in map units.",
                        "default": None
                },
                "ground_spacing": {
                        "type": "string",
                        "description": "The  ground spacing, in meters,  at which the 3D points will be generated.The default is five times the  source image pixel size.",
                        "default": None
                },
                "minimum_pairs": {
                        "type": "string",
                        "description": "The maximum number of image pairs that an image can contribute to generate 3D points. The default value is a minimum of 8 image pairs.If the image is involved in more image pairs than specified, those...",
                        "default": None
                },
                "minimum_area": {
                        "type": "string",
                        "description": "The minimum overlap threshold area that is acceptable, which is a percentage of overlap between a pair of images. Image pairs with overlap areas smaller than this threshold will receive a score of 0 f...",
                        "default": None
                },
                "minimum_adjustment_quality": {
                        "type": "string",
                        "description": "The minimum adjustment quality that is acceptable. The threshold value will be compared to the adjustment quality value that is stored in the stereo model.  Image pairs with an adjustment quality less...",
                        "default": None
                },
                "maximum_diff_gsd": {
                        "type": "string",
                        "description": "The maximum allowable threshold for the ground sample distance (GSD) between two images in a pair. The resolution ratio between the two images will be compared to the threshold value. Image pairs with...",
                        "default": None
                },
                "maximum_diff_op": {
                        "type": "string",
                        "description": "The maximum threshold for the difference between the Omega values and Phi values for the two image pairs. The Omega values and Phi values for the  image pairs are compared. Image pairs with an Omega o...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "matching_method",
                "out_folder",
                "out_base_name"
        ]
},
    "interpolate_from_point_cloud": {
        "name": "interpolate_from_point_cloud",
        "description": "Interpolates a digital terrain model (DTM) or a digital surface model (DSM) from a point cloud.",
        "parameters": {
                "in_container": {
                        "type": "string",
                        "description": "The path and name of the input file, folder, feature layer, or LAS dataset. The input can be a folder of LAS files, a solution point table from Ortho mapping tools, or an LAS dataset. For cloud storag..."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster dataset location, name, and file extension. You can also save the output raster dataset by providing a cloud storage path such as C:\\Temp\\Cloud.acs\\lasfolder.The output can be create..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster dataset."
                },
                "interpolation_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to interpolate the output raster dataset from the point cloud. TRIANGULATION\u2014 The triangulation method will be used. It is also known as triangulated irregular n...",
                        "default": None
                },
                "smooth_method": {
                        "type": "string",
                        "description": "Specifies the filter that will be used to smooth the output raster dataset. GAUSS3x3\u2014A Gaussian filter with a 3 by 3 window will be used.GAUSS5x5\u2014A Gaussian filter with a 5 by 5 window will be used.GA...",
                        "default": None
                },
                "surface_type": {
                        "type": "string",
                        "description": "Specifies whether a digital terrain model or a digital surface model will be created.DTM\u2014A digital terrain model will be created by interpolating only the ground points.DSM\u2014A digital surface model wil...",
                        "default": None
                },
                "fill_dem": {
                        "type": "string",
                        "description": "A DEM raster input that is used to fill NoData areas. Areas of NoData may exist where  pixels do not have enough information from the input to generate values.",
                        "default": None
                },
                "optionsname_value": {
                        "type": "string",
                        "description": "Classify ground points from the input LAS data.This parameter is active when the surface_type parameter is set to DTM.Classify\u2014Classify the ground using different options depending on the type of terr...",
                        "default": None
                }
        },
        "required": [
                "in_container",
                "out_raster",
                "cell_size"
        ]
},
    "match_control_points": {
        "name": "match_control_points",
        "description": "Creates matching tie points for a given ground control point and initial tie point in one of the overlapping images. The ortho mapping block adjustment workflow often involves adding ground control points for a more accurate adjustment. One ground control point is typically associated with a tie point in each overlapping image. When there are many overlapping images for one ground control point, manually creating tie points for each image is labor intensive.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that contains the source imagery from which the tie points will be created."
                },
                "in_control_points": {
                        "type": "string",
                        "description": "The input control point set that contains a list of ground control point features and at least one initial tie point for each ground control point."
                },
                "out_control_points": {
                        "type": "string",
                        "description": "The output control point features that contain ground control points."
                },
                "similarity": {
                        "type": "string",
                        "description": "Specifies the similarity level that will be used for matching tie points.LOW\u2014The similarity criteria for the two matching points will be low. This option will  produce the most matching points, but so...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "in_control_points",
                "out_control_points"
        ]
},
    "remove_depth_map": {
        "name": "remove_depth_map",
        "description": "Removes the depth map from a mosaic dataset.  Other than the depth map removal, the tool will not update the mosaic dataset. Depth maps are created by running the Compute Depth Map tool.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that will have the depth map removed."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will be used to select items in the mosaic dataset depth map to be removed. If not specified, all depth map content in the source raster\u2019s folder will be removed.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset"
        ]
},
    "update_interior_orientation": {
        "name": "update_interior_orientation",
        "description": "Refines the interior orientation for each image in the mosaic dataset by constructing an affine transformation from a fiducial table.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that is created from scanned aerial photos using the scanned raster type or frame camera raster type."
                },
                "where_clause": {
                        "type": "string",
                        "description": "A query definition string that defines a subset of rasters for computing fiducials.",
                        "default": None
                },
                "fiducial_table": {
                        "type": "string",
                        "description": "The fiducial table created using the Compute Fiducials tool."
                },
                "film_coordinate_system": {
                        "type": "string",
                        "description": "Defines the film coordinate system of the scanned aerial photograph.  It is used in computing fiducial information and affine transformation construction.\r\nNO_CHANGE\u2014Maintain the coordinate system of ..."
                },
                "update_footprints": {
                        "type": "string",
                        "description": "Generates or updates the footprints of the digital photos in the mosaic dataset.UPDATE\u2014The footprints will be generated or updated.NO_UPDATE\u2014The footprints will not be generated or updated. This is th...",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "fiducial_table",
                "film_coordinate_system"
        ]
},
    "copy_raster": {
        "name": "copy_raster",
        "description": "Saves a copy of a raster dataset or converts a mosaic dataset into a single raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset or mosaic dataset to be copied."
                },
                "out_rasterdataset": {
                        "type": "string",
                        "description": "The name and format for the raster dataset being created..avif\u2014AVIF.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.crf\u2014CRF.dat\u2014ENVI DAT.img\u2014ERDAS IMAGINE.gif\u2014GIF.jpg\u2014JPEG.jxl\u2014JPEGXL.jp2\u2014JPEG 2000.mrf\u2014..."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The storage parameters (configuration) for a geodatabase. Configuration keywords are set up by your database administrator.",
                        "default": None
                },
                "background_value": {
                        "type": "string",
                        "description": "Remove the unwanted values created around the raster data. The value specified will be distinguished from other valuable data in the raster dataset. For example, a value of zero along the raster datas...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "All the pixels with the specified value will be set to NoData in the output raster dataset.",
                        "default": None
                },
                "onebit_to_eightbit": {
                        "type": "string",
                        "description": "Specifies whether the input 1-bit raster dataset will be converted to an 8-bit raster dataset. In this conversion, the value 1 in the input raster dataset will be changed to 255 in the output raster d...",
                        "default": None
                },
                "colormap_to_rgb": {
                        "type": "string",
                        "description": "Specifies whether the input raster dataset will be converted to a three-band output raster dataset if the input raster dataset includes a color map. This is useful when mosaicking rasters with differe...",
                        "default": None
                },
                "pixel_type": {
                        "type": "string",
                        "description": "Specifies the bit depth, or radiometric resolution, that will be used for the raster or mosaic dataset. If not defined, the value from the first raster dataset will be used.1_BIT\u2014The pixel type will b...",
                        "default": None
                },
                "scale_pixel_value": {
                        "type": "string",
                        "description": "Specifies whether pixel values will be scaled. When the output is a pixel type other than the input (such as 16 bit to 8 bit), you can scale the values to fit into the new range; otherwise, the values...",
                        "default": None
                },
                "rgb_to_colormap": {
                        "type": "string",
                        "description": "Specifies whether an 8-bit, 3-band (RGB) raster dataset will be converted to a single-band raster dataset with a color map.\r\nThis operation suppresses noise that is often found in scanned images and i...",
                        "default": None
                },
                "format": {
                        "type": "string",
                        "description": "Specifies the output raster format.AVIF\u2014The output format will be AVIF.TIFF\u2014The output format will be TIFF.COG\u2014The output format will be Cloud Optimized GeoTIFF.IMAGINE Image\u2014The output format will be...",
                        "default": None
                },
                "transform": {
                        "type": "string",
                        "description": "Specifies whether a transformation associated with the input raster will be applied to the output.\r\nThe input raster can have a transformation associated with it that is not saved in the input, such a...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies whether the input mosaic dataset will be processed as a multidimensional raster dataset.CURRENT_SLICE\u2014The input will not be processed as a multidimensional raster dataset. If the input is mu...",
                        "default": None
                },
                "build_multidimensional_transpose": {
                        "type": "string",
                        "description": "Specifies whether the transpose for the input multidimensional raster dataset will be built, which will chunk the data along each dimension to optimize performance when accessing pixel values across a...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_rasterdataset"
        ]
},
    "create_random_raster": {
        "name": "create_random_raster",
        "description": "Creates a raster dataset of random values with a distribution you define.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The folder or geodatabase where the output raster dataset will be stored."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name and format of the raster dataset you are creating.To store the output as a raster dataset in a geodatabase, do not add a file extension to the raster dataset name.For file-based rasters, use ..."
                },
                "distribution": {
                        "type": "string",
                        "description": "Specifies the random value distribution method to use.Each type has one or two settings to control the distribution.\r\nUNIFORM {Minimum}, {Maximum}\u2014A uniform distribution with the defined range. The de...",
                        "default": None
                },
                "raster_extent": {
                        "type": "string",
                        "description": "The extent of the output raster dataset.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is equal to the visible display....",
                        "default": None
                },
                "cellsize": {
                        "type": "string",
                        "description": "The spatial resolution of the output raster dataset.",
                        "default": None
                },
                "build_rat": {
                        "type": "string",
                        "description": "Specifies whether the tool will unconditionally build a raster attribute table for the output raster in which the selected distribution results in an integer output raster.This parameter has no effect...",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "create_raster_dataset": {
        "name": "create_raster_dataset",
        "description": "Creates an empty raster dataset.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The folder or geodatabase where the raster dataset will be stored."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name, location, and format for the newly created dataset.When storing the raster dataset in a file format, specify the file extension as follows:.bil for Esri BIL.bip for Esri BIP.bmp for BMP.bsq ..."
                },
                "cellsize": {
                        "type": "string",
                        "description": "The pixel size that will be used for the new raster dataset.",
                        "default": None
                },
                "pixel_type": {
                        "type": "string",
                        "description": "The bit depth (radiometric resolution) of the output raster dataset. If this is not specified, the raster dataset will be created with a default pixel type of 8-bit unsigned integer.Not all data types..."
                },
                "raster_spatial_reference": {
                        "type": "string",
                        "description": "The coordinate system for the output raster dataset.If this is not specified, the coordinate system set in the environment settings will be used.",
                        "default": None
                },
                "number_of_bands": {
                        "type": "string",
                        "description": "The number of bands of the output raster dataset."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The storage parameters (configuration) for a file or enterprise geodatabase.  Configuration keywords are set up by your database administrator.",
                        "default": None
                },
                "pyramids": {
                        "type": "string",
                        "description": "Creates pyramids.For Pyramid Levels, specify a number of -1 or higher. A value of 0 will not create pyramids, and a value of -1 will automatically determine the correct number of pyramid layers to cre...",
                        "default": None
                },
                "tile_size": {
                        "type": "string",
                        "description": "The size of the tiles.The tile width controls the number of pixels that can be stored in each tile. This is specified as a number of pixels in x. The default tile width is 128.The tile height controls...",
                        "default": None
                },
                "compression": {
                        "type": "string",
                        "description": "Specifies the type of compression that will be used to store the raster dataset.LZ77\u2014Lossless compression that preserves all raster cell values will be used.JPEG\u2014Lossy compression that uses the public...",
                        "default": None
                },
                "pyramid_origin": {
                        "type": "string",
                        "description": "The origination location of the raster pyramid. It is recommended that you specify this point if you plan to build large mosaics in a file geodatabase or enterprise geodatabase, especially if you plan...",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name",
                "pixel_type",
                "number_of_bands"
        ]
},
    "download_rasters": {
        "name": "download_rasters",
        "description": "Downloads the source  files from an image service or mosaic dataset.",
        "parameters": {
                "in_image_service": {
                        "type": "string",
                        "description": "The image service or mosaic dataset to download."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The destination for the image service or mosaic dataset."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to limit the download to raster datasets that satisfy the expression.",
                        "default": None
                },
                "selection_feature": {
                        "type": "string",
                        "description": "Limits the download to  an extent of a feature class or bounding box. All raster datasets that intersect the extent will be downloaded.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The min...",
                        "default": None
                },
                "clipping": {
                        "type": "string",
                        "description": "Specify if you want to clip the downloaded images based on the geometry of a feature. Any raster that intersects the clipping geometry will be clipped and then downloaded. This is useful when your are...",
                        "default": None
                },
                "convert_rasters": {
                        "type": "string",
                        "description": "Choose whether to always convert your rasters to the specified format, or to only convert when it is necessary.\r\nCONVERT_AS_REQUIRED\u2014Do not convert the raster datasets to a new format.ALWAYS_CONVERT\u2014C...",
                        "default": None
                },
                "format": {
                        "type": "string",
                        "description": "Choose a output  format for the downloaded raster datasets.TIFF\u2014Tagged Image File Format. This is the default.BIL\u2014Esri band interleaved by line.BSQ\u2014Esri band sequential.BIP\u2014Esri band interleaved by pi...",
                        "default": None
                },
                "compression_method": {
                        "type": "string",
                        "description": "Choose the compression method to use with the specified Output Format.NONE\u2014No compression will occur. This is the default.JPEG\u2014Lossy compression that uses the public JPEG compression algorithm. If you...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "Set a value from 1 - 100. Higher values will have better image quality, but less compression.",
                        "default": None
                },
                "maintain_folder": {
                        "type": "string",
                        "description": "Determines the folder structure of the downloaded rasters. MAINTAIN_FOLDER\u2014Replicate the hierarchical folder structure used to store the source raster datasets.NO_MAINTAIN_FOLDER\u2014Raster datasets will ...",
                        "default": None
                }
        },
        "required": [
                "in_image_service",
                "out_folder"
        ]
},
    "generate_raster_from_raster_function": {
        "name": "generate_raster_from_raster_function",
        "description": "Generates a raster dataset from an input raster function or function chain.",
        "parameters": {
                "raster_function": {
                        "type": "string",
                        "description": "The name of a raster function, raster function JSON object, or function chain (in .rft.xml format)."
                },
                "out_raster_dataset": {
                        "type": "string",
                        "description": "The output raster dataset."
                },
                "format": {
                        "type": "string",
                        "description": "The output raster format.The default format will be derived from the  file extension specified in the  output_raster_dataset value. TIFF\u2014Tagged Image File Format for raster datasets will be used.Cloud...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies whether the input mosaic dataset will be processed as a multidimensional raster dataset.CURRENT_SLICE\u2014The input will not be processed as a multidimensional raster dataset. If the input is mu...",
                        "default": None
                }
        },
        "required": [
                "raster_function",
                "out_raster_dataset"
        ]
},
    "mosaic": {
        "name": "mosaic",
        "description": "Merges multiple existing raster datasets or mosaic datasets into an existing raster dataset.",
        "parameters": {
                "inputsinput": {
                        "type": "string",
                        "description": "The raster datasets to be merged."
                },
                "target": {
                        "type": "string",
                        "description": "The raster to which the input rasters will be added. This must be an existing raster dataset. By default, the\r\ntarget raster is considered the first raster in the list of input\r\nraster datasets. You c..."
                },
                "mosaic_type": {
                        "type": "string",
                        "description": "Specifies the method that will be used to mosaic overlapping areas.FIRST\u2014The output cell value of the overlapping areas will be the value from the first raster dataset mosaicked into that location.LAS...",
                        "default": None
                },
                "colormap": {
                        "type": "string",
                        "description": "Specifies the method that will be used to choose which color map from the input rasters will be applied to the mosaic output.FIRST\u2014The color map from the first raster dataset in the list will be appli...",
                        "default": None
                },
                "background_value": {
                        "type": "string",
                        "description": "Remove the unwanted values created around the raster data. The value specified will be distinguished from other valuable data in the raster dataset. For example, a value of zero along the raster datas...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "All the pixels with the specified value will be set to NoData in the output raster dataset.",
                        "default": None
                },
                "onebit_to_eightbit": {
                        "type": "string",
                        "description": "Specifies whether the input 1-bit raster dataset will be converted to an 8-bit raster dataset. In this conversion, the value 1 in the input raster dataset will be changed to 255 in the output raster d...",
                        "default": None
                },
                "mosaicking_tolerance": {
                        "type": "string",
                        "description": "When mosaicking occurs, the target and the source pixels do not always line up exactly. When there is a misalignment of pixels, you need to decide whether to resample or shift the data. The mosaicking...",
                        "default": None
                },
                "matchingmethod": {
                        "type": "string",
                        "description": "Specifies the color matching method that will be applied to the rasters.NONE\u2014No color matching method will be applied when mosaicking the raster datasets.STATISTIC_MATCHING\u2014Descriptive statistics from...",
                        "default": None
                }
        },
        "required": [
                "inputsinput",
                "target"
        ]
},
    "mosaic_to_new_raster": {
        "name": "mosaic_to_new_raster",
        "description": "Merges multiple raster datasets into a new raster dataset.",
        "parameters": {
                "input_rastersinput_raster": {
                        "type": "string",
                        "description": "The raster datasets that you want to merge together. The inputs must have the same number of bands and same bit depth."
                },
                "output_location": {
                        "type": "string",
                        "description": "The folder or geodatabase to store the raster."
                },
                "raster_dataset_name_with_extension": {
                        "type": "string",
                        "description": "The name of the dataset you are creating. When storing the raster dataset in a file format, specify the file extension as follows:\r\n.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.dat\u2014ENVI DAT.gif\u2014GIF..."
                },
                "coordinate_system_for_the_raster": {
                        "type": "string",
                        "description": "The coordinate system for the output raster dataset.",
                        "default": None
                },
                "pixel_type": {
                        "type": "string",
                        "description": "The bit depth, or radiometric resolution of\r\nthe mosaic dataset.If you do not set the\r\npixel type, the 8-bit default will be used and your output may be\r\nincorrect.\r\n\r\n1_BIT\u2014The pixel type will be a 1...",
                        "default": None
                },
                "cellsize": {
                        "type": "string",
                        "description": "The pixel size that will be used for the new raster dataset.",
                        "default": None
                },
                "number_of_bands": {
                        "type": "string",
                        "description": "The number of bands that the output raster will have."
                },
                "mosaic_method": {
                        "type": "string",
                        "description": "The method used to mosaic overlapping areas.FIRST\u2014The output cell value of the overlapping areas will be the value from the first raster dataset mosaicked into that location.LAST\u2014The output cell value...",
                        "default": None
                },
                "mosaic_colormap_mode": {
                        "type": "string",
                        "description": "Applies when the input raster datasets have a colormap.Specifies the method that will be used to choose which color map from the input rasters will be applied to the mosaic output.FIRST\u2014The color map ...",
                        "default": None
                }
        },
        "required": [
                "input_rastersinput_raster",
                "output_location",
                "raster_dataset_name_with_extension",
                "number_of_bands"
        ]
},
    "workspace_to_raster_dataset": {
        "name": "workspace_to_raster_dataset",
        "description": "Merges all of the raster datasets in a folder into one raster dataset.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The folder containing the raster datasets to merge."
                },
                "in_raster_dataset": {
                        "type": "string",
                        "description": "An existing raster dataset in which to merge all of the raster datasets from the input workspace."
                },
                "include_subdirectories": {
                        "type": "string",
                        "description": "Specifies whether subdirectories will be included.NONE\u2014Subdirectories will not be included. This is the default.INCLUDE_SUBDIRECTORIES\u2014All raster datasets in the subdirectories will be included when l...",
                        "default": None
                },
                "mosaic_type": {
                        "type": "string",
                        "description": "Specifies the method that will be used to mosaic overlapping areas.FIRST\u2014The output cell value of the overlapping areas will be the value from the first raster dataset mosaicked into that location.LAS...",
                        "default": None
                },
                "colormap": {
                        "type": "string",
                        "description": "Specifies the method that will be used to choose which color map from the input rasters will be applied to the mosaic output.FIRST\u2014The color map from the first raster dataset in the list will be appli...",
                        "default": None
                },
                "background_value": {
                        "type": "string",
                        "description": "Remove the unwanted values created around the raster data. The value specified will be distinguished from other valuable data in the raster dataset. For example, a value of zero along the raster datas...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "All the pixels with the specified value will be set to NoData in the output raster dataset.",
                        "default": None
                },
                "onebit_to_eightbit": {
                        "type": "string",
                        "description": "Specifies whether the input 1-bit raster dataset will be converted to an 8-bit raster dataset. In this conversion, the value 1 in the input raster dataset will be changed to 255 in the output raster d...",
                        "default": None
                },
                "mosaicking_tolerance": {
                        "type": "string",
                        "description": "When mosaicking occurs, the target and the source pixels do not always line up exactly. When there is a misalignment of pixels, you need to decide whether to resample or shift the data. The mosaicking...",
                        "default": None
                },
                "matchingmethod": {
                        "type": "string",
                        "description": "The color matching method to apply to the rasters.NONE\u2014This option will not use the color matching operation when mosaicking your raster datasets.STATISTIC_MATCHING\u2014This method will use descriptive st...",
                        "default": None
                },
                "colormap_to_rgb": {
                        "type": "string",
                        "description": "Specifies whether the input raster dataset will be converted to a three-band output raster dataset if the input raster dataset includes a color map. This is useful when mosaicking rasters with differe...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "in_raster_dataset"
        ]
},
    "clip_raster": {
        "name": "clip_raster",
        "description": "Cuts out a portion of a raster dataset, mosaic dataset, or image service layer.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset, mosaic dataset, or image service to be clipped."
                },
                "rectangle": {
                        "type": "string",
                        "description": "The four coordinates that define the extent of the bounding box that will be used to clip the raster. Coordinates are expressed in the order of x-min, y-min, x-max, y-max.If the in_template_dataset pa..."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format of the dataset being created. Ensure that it can support the necessary bit depth.When storing the raster dataset in a file format, specify the file extension as follows:..."
                },
                "in_template_dataset": {
                        "type": "string",
                        "description": "A raster dataset or feature class\r\nthat will be used as the extent. The clip output\r\nincludes pixels that intersect the minimum bounding\r\nrectangle.\r\nIf a feature class is used as the output extent an...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "The value for pixels to be considered as NoData.",
                        "default": None
                },
                "clipping_geometry": {
                        "type": "string",
                        "description": "Specifies whether the minimum bounding rectangle or the geometry of the specified feature class will be used to clip the data.NONE\u2014The minimum bounding rectangle will be used to clip the data. This is...",
                        "default": None
                },
                "maintain_clipping_extent": {
                        "type": "string",
                        "description": "Specifies the extent that will be used in the clipping output.MAINTAIN_EXTENT\u2014The number of columns and rows will be adjusted and  the pixels will be resampled to exactly match the clipping extent spe...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "rectangle",
                "out_raster"
        ]
},
    "composite_bands": {
        "name": "composite_bands",
        "description": "Creates a single raster dataset from multiple bands.",
        "parameters": {
                "in_rasters": {
                        "type": "string",
                        "description": "The raster datasets that you want to use as the bands."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location and format for the raster dataset you are creating. Make sure that it can support the necessary bit-depth.When storing the raster dataset in a file format, specify the file extensio..."
                }
        },
        "required": [
                "in_rasters",
                "out_raster"
        ]
},
    "compute_pansharpen_weights": {
        "name": "compute_pansharpen_weights",
        "description": "Calculates an optimal set of pan sharpened weights for new or custom sensor data.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "A multispectral raster that has a panchromatic band."
                },
                "in_panchromatic_image": {
                        "type": "string",
                        "description": "The panchromatic band associated with the multispectral raster."
                },
                "band_indexes": {
                        "type": "string",
                        "description": "The band order for the pan sharpened weights.If a raster product is used as the in_raster parameter, the band order within the raster product template will be used.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_panchromatic_image"
        ]
},
    "create_color_composite": {
        "name": "create_color_composite",
        "description": "Creates a three-band raster dataset from a multiband raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input multiband raster data."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output three-band composite raster."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the\r\nmethod that will be used to extract bands.BAND_NAMES\u2014The band name representing the wavelength\r\ninterval on the electromagnetic spectrum (such as Red, Near Infrared,\r\nor Thermal Infrare..."
                },
                "red_expression": {
                        "type": "string",
                        "description": "The calculation \r\nthat will be assigned to the first band.A band name, band ID, or an algebraic expression using the bands.The supported operators are unary: plus (+), minus (-), times (*), and divide..."
                },
                "green_expression": {
                        "type": "string",
                        "description": "The calculation \r\nthat will be assigned to the second band.A band name, band ID, or an algebraic expression using the bands.The supported operators are unary: plus (+), minus (-), times (*), and divid..."
                },
                "blue_expression": {
                        "type": "string",
                        "description": "The calculation \r\nthat will be assigned to the third band.\r\nA band name, band ID, or an algebraic expression using the bands.The supported operators are unary: plus (+), minus (-), times (*), and divi..."
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "method",
                "red_expression",
                "green_expression",
                "blue_expression"
        ]
},
    "create_ortho_corrected_raster_dataset": {
        "name": "create_ortho_corrected_raster_dataset",
        "description": "Creates an orthocorrected raster dataset using a digital elevation model (DEM) and control data to accurately align imagery.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset or mosaic dataset that will be orthorectified."
                },
                "out_raster_dataset": {
                        "type": "string",
                        "description": "The name, location, and format of the dataset that will be created.When storing the raster dataset in a file format, specify the file extension as follows:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri B..."
                },
                "ortho_type": {
                        "type": "string",
                        "description": "Specifies whether the orthorectification type will be a DEM or a specified value that represents the average elevation across the image. CONSTANT_ELEVATION\u2014A specified elevation value will be used.DEM..."
                },
                "constant_elevation": {
                        "type": "string",
                        "description": "The constant elevation value that will be used when the Ortho_type parameter is  CONSTANT_ELEVATION.If a DEM is used in the orthocorrection process, this parameter value is not used."
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The DEM raster that will be used for orthorectification when the Ortho_type parameter is DEM.",
                        "default": None
                },
                "zfactor": {
                        "type": "string",
                        "description": "The scaling factor that will be used to convert the elevation values in the DEM.If the vertical units are meters, set the parameter to 1. If the vertical units are feet, set the parameter to 0.3048. I...",
                        "default": None
                },
                "zoffset": {
                        "type": "string",
                        "description": "The base value that will be added to the elevation value in the DEM. This can be used to offset elevation values that do not start at sea level.",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the geoid correction required by  RPCs that reference ellipsoidal heights will be made. Most elevation datasets are referenced to sea level orthometric heights, so this correction is...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster_dataset",
                "ortho_type",
                "constant_elevation"
        ]
},
    "create_pansharpened_raster_dataset": {
        "name": "create_pansharpened_raster_dataset",
        "description": "Combines a high-resolution panchromatic raster dataset with a lower-resolution multiband raster dataset to create a high-resolution multiband  raster dataset for visual analysis. Learn more about pan sharpening",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset that will be pan sharpened."
                },
                "red_channel": {
                        "type": "string",
                        "description": "The input raster band that will display with the red color channel."
                },
                "green_channel": {
                        "type": "string",
                        "description": "The input raster band that will display with the green color channel."
                },
                "blue_channel": {
                        "type": "string",
                        "description": "The input raster band that will display with the blue color channel."
                },
                "infrared_channel": {
                        "type": "string",
                        "description": "The input raster band that will display with the infrared color channel.",
                        "default": None
                },
                "out_raster_dataset": {
                        "type": "string",
                        "description": "The name, location, and format of the raster dataset that will be created.When storing the raster dataset in a file format, specify the file extension as follows:When storing a raster dataset in a geo..."
                },
                "in_panchromatic_image": {
                        "type": "string",
                        "description": "The  higher-resolution panchromatic image."
                },
                "pansharpening_type": {
                        "type": "string",
                        "description": "Specifies the algorithm that will be used to combine the panchromatic and multispectral bands.IHS\u2014Intensity, Hue, and Saturation color space will be used.BROVEY\u2014The Brovey algorithm based on spectral ..."
                },
                "red_weight": {
                        "type": "string",
                        "description": "A value from 0 to 1 that will be used to weight the red band.",
                        "default": None
                },
                "green_weight": {
                        "type": "string",
                        "description": "A value from 0 to 1 that will be used to weight the green band.",
                        "default": None
                },
                "blue_weight": {
                        "type": "string",
                        "description": "A value from 0 to 1 that will be used to weight the blue band.",
                        "default": None
                },
                "infrared_weight": {
                        "type": "string",
                        "description": "A value from 0 to 1 that will be used to weight the infrared band.",
                        "default": None
                },
                "sensor": {
                        "type": "string",
                        "description": "Specifies the sensor of the multiband raster input.You can specify the sensor when the  pansharpening_type parameter is set to Gram-Schmidt. Specifying the sensor will set appropriate  band weights.UN...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "red_channel",
                "green_channel",
                "blue_channel",
                "out_raster_dataset",
                "in_panchromatic_image",
                "pansharpening_type"
        ]
},
    "extract_subdataset": {
        "name": "extract_subdataset",
        "description": "Creates a new raster dataset from a selection of an HDF or NITF dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The HDF or NITF dataset that has the layers you want to extract."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format for the dataset you are creating.When storing the raster dataset in a file format, you need to specify the file extension:.bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ..."
                },
                "subdataset_index": {
                        "type": "string",
                        "description": "The  subdatasets that you want to extract.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster"
        ]
},
    "generate_table_from_raster_function": {
        "name": "generate_table_from_raster_function",
        "description": "Converts a raster function dataset to a table or feature class.  The input raster function should be a raster function designed to output a table or feature class.",
        "parameters": {
                "raster_function": {
                        "type": "string",
                        "description": "The function template or function JSON object that outputs a table or feature class."
                },
                "out_table": {
                        "type": "string",
                        "description": "The path, file name, and type (extension) of the output table or feature class."
                },
                "raster_function_arguments": {
                        "type": "string",
                        "description": "The function arguments and their values to be set. Each raster function has its own arguments and values, which are listed in the dialog of the tool.",
                        "default": None
                }
        },
        "required": [
                "raster_function",
                "out_table"
        ]
},
    "raster_to_dted": {
        "name": "raster_to_dted",
        "description": "Splits a raster dataset into separate files based on the DTED tiling structure.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "Select a single band raster dataset that represents elevation."
                },
                "out_folder": {
                        "type": "string",
                        "description": "Select a destination where\r\nthe folder structure and DTED files will be created."
                },
                "dted_level": {
                        "type": "string",
                        "description": "Select an appropriate level based on the resolution of your elevation data.DTED_0\u2014 900 mDTED_1\u2014 90 mDTED_2\u201430 m"
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Choose an appropriate technique based on the type of data you have.NEAREST\u2014The fastest resampling method, and it minimizes changes to pixel values. Suitable for discrete data, such as land cover.BILIN...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_folder",
                "dted_level"
        ]
},
    "resample": {
        "name": "resample",
        "description": "Changes the spatial resolution of a raster dataset and sets rules for aggregating or interpolating values across the new pixel sizes.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset with the spatial resolution to be changed."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The name, location, and format of the dataset being created..bil\u2014Esri BIL.bip\u2014Esri BIP.bmp\u2014BMP.bsq\u2014Esri BSQ.dat\u2014ENVI DAT.gif\u2014GIF.img\u2014ERDAS IMAGINE.jpg\u2014JPEG.jp2\u2014JPEG 2000.png\u2014PNG.tif\u2014TIFF.mrf\u2014MRF.crf\u2014C..."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the new raster using an existing raster dataset or by specifying its width (x) and height (y).\r\nYou can specify the cell size in the following ways: Use a single number specifying a s...",
                        "default": None
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Specifies the resampling technique to be used.NEAREST\u2014 The nearest neighbor technique will be used. It minimizes changes to pixel values since no new values are created and is the fastest resampling t...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster"
        ]
},
    "split_raster": {
        "name": "split_raster",
        "description": "Divides a raster dataset  into smaller pieces, by tiles or features from a polygon.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster to split."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The destination for the new raster datasets."
                },
                "out_base_name": {
                        "type": "string",
                        "description": "The prefix for each of the raster datasets you will create. A number will be appended to each prefix, starting with 0."
                },
                "split_method": {
                        "type": "string",
                        "description": "Determines how to split the raster dataset.SIZE_OF_TILE\u2014Specify the width and height of the tile.NUMBER_OF_TILES\u2014 Specify the number of raster tiles to create by breaking the dataset into a number of ..."
                },
                "format": {
                        "type": "string",
                        "description": "The format for the output raster datasets.TIFF\u2014Tagged Image File Format. This is the default.BMP\u2014Microsoft Bitmap.ENVI\u2014ENVI DAT.Esri BIL\u2014Esri Band Interleaved by Line.Esri BIP\u2014Esri Band Interleaved by..."
                },
                "resampling_type": {
                        "type": "string",
                        "description": "Choose an appropriate technique based on the type of data you have.NEAREST\u2014The fastest resampling method, and it minimizes changes to pixel values. Suitable for discrete data, such as land cover.BILIN...",
                        "default": None
                },
                "num_rasters": {
                        "type": "string",
                        "description": "The number of columns (x) and rows (y) to split the raster dataset into. This is a point whose X and Y coordinates define number of rows and columns. The X coordinate is the number of columns and the ...",
                        "default": None
                },
                "tile_size": {
                        "type": "string",
                        "description": "The x and y dimensions\r\nof the output tiles. The default unit of measurement is in pixels.\r\nYou can change this with the units parameter. This is a point whose X and Y coordinates define the dimension...",
                        "default": None
                },
                "overlap": {
                        "type": "string",
                        "description": "The tiles do not have to line up perfectly; set\r\nthe amount of overlap between tiles with this parameter. The default unit of measurement is in pixels. You\r\ncan change this with the units parameter.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "Set the units of measurement for the tile_size and the overlap  parameters.PIXELS\u2014The unit is in pixels. This is the default.METERS\u2014The unit is in meters.FEET\u2014The unit is in feet.DEGREES\u2014The unit is i...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The spatial resolution of the output\r\nraster. If left blank, the output cell size will match the input\r\nraster. When you change the cell size\r\nvalues, the tile size\r\nis reset to the image size\r\nand th...",
                        "default": None
                },
                "origin": {
                        "type": "string",
                        "description": "Change the coordinates for\r\nthe lower left origin point, where the tiling scheme will begin. If\r\nleft blank, the lower left origin would be the same as the input\r\nraster.",
                        "default": None
                },
                "split_polygon_feature_class": {
                        "type": "string",
                        "description": "A feature class that will be used to split the raster dataset.",
                        "default": None
                },
                "clip_type": {
                        "type": "string",
                        "description": "Limits the extent of your raster dataset before you split it.NONE\u2014 Use the full extent of the input raster dataset.EXTENT\u2014Specify bounding box as your clipping boundary.FEATURE_CLASS\u2014Specify a feature...",
                        "default": None
                },
                "template_extent": {
                        "type": "string",
                        "description": "An extent or a  dataset used to define the clipping boundary. The dataset can be a raster or feature class.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inpu...",
                        "default": None
                },
                "nodata_value": {
                        "type": "string",
                        "description": "All the pixels with the specified value will be set to NoData in the output raster dataset.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_folder",
                "out_base_name",
                "split_method",
                "format"
        ]
},
    "add_colormap": {
        "name": "add_colormap",
        "description": "Adds a new color map or replaces an existing color map on a raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to add or replace a color map."
                },
                "in_template_raster": {
                        "type": "string",
                        "description": "A raster dataset that has a color map that you want to apply to the input raster dataset. If this is entered the input_CLR_file parameter is ignored.",
                        "default": None
                },
                "input_clr_file": {
                        "type": "string",
                        "description": "Specify a .clr or .act file to use as the color map.",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "batch_build_pyramids": {
        "name": "batch_build_pyramids",
        "description": "Builds pyramids for multiple raster datasets.",
        "parameters": {
                "input_raster_datasets": {
                        "type": "string",
                        "description": "The raster datasets for which raster pyramids will be built.Each input should have more than 1,024 rows and 1,024 columns."
                },
                "pyramid_levels": {
                        "type": "string",
                        "description": "The number of reduced-resolution dataset layers that will be built. The default value is -1, which will build full pyramids. A value of 0 will result in no pyramid levels.",
                        "default": None
                },
                "skip_first_level": {
                        "type": "string",
                        "description": "Specifies whether the first pyramid level will be skipped. Skipping the first level will take up slightly less disk space but will slow down performance at these scales.NONE\u2014The first pyramid level wi...",
                        "default": None
                },
                "pyramid_resampling_technique": {
                        "type": "string",
                        "description": "Specifies the resampling technique that will be used to build the pyramids.NEAREST\u2014The new value of a cell will be based on the closest cell when resampling. This is the default.BILINEAR\u2014The new value...",
                        "default": None
                },
                "pyramid_compression_type": {
                        "type": "string",
                        "description": "Specifies the compression type that will be used when building the pyramids.DEFAULT\u2014If the source data is compressed using a wavelet compression, pyramids will be built with the JPEG compression type;...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "The compression quality that will be used when pyramids are built with the JPEG compression type.\r\nThe value must be between 0 and 100. The values closer to 100 will produce a higher-quality image, bu...",
                        "default": None
                },
                "skip_existing": {
                        "type": "string",
                        "description": "Specifies whether pyramids will be built only if they do not exist or built even if they exist. OVERWRITE\u2014Pyramids will be built even if they already exist; existing pyramids will be overwritten. This...",
                        "default": None
                }
        },
        "required": [
                "input_raster_datasets"
        ]
},
    "batch_calculate_statistics": {
        "name": "batch_calculate_statistics",
        "description": "Calculates statistics for  multiple raster datasets.",
        "parameters": {
                "input_raster_datasetsinput_raster_dataset": {
                        "type": "string",
                        "description": "The input raster datasets."
                },
                "number_of_columns_to_skip": {
                        "type": "string",
                        "description": "The number of horizontal pixels between samples.A skip factor controls the portion of the raster that is used when calculating the statistics. The input value indicates the horizontal or vertical skip...",
                        "default": None
                },
                "number_of_rows_to_skip": {
                        "type": "string",
                        "description": "The number of vertical pixels between samples.A skip factor controls the portion of the raster that is used when calculating the statistics. The input value indicates the horizontal or vertical skip f...",
                        "default": None
                },
                "ignore_valuesignore_value": {
                        "type": "string",
                        "description": "The pixel values that are not to be included in the statistics calculation.The default is no value.",
                        "default": None
                },
                "skip_existing": {
                        "type": "string",
                        "description": "Specifies whether statistics will be calculated only when they are missing or will be regenerated even if they exist.OVERWRITE\u2014Statistics will be calculated even if they already exist, and existing st...",
                        "default": None
                }
        },
        "required": [
                "input_raster_datasetsinput_raster_dataset"
        ]
},
    "build_pyramids": {
        "name": "build_pyramids",
        "description": "Builds raster pyramids for your raster dataset. This tool can also be used to delete pyramids. To delete pyramids, set the Pyramids Levels parameter to 0.",
        "parameters": {
                "in_raster_dataset": {
                        "type": "string",
                        "description": "The raster dataset for which you want to build pyramids.The input should have more than 1,024 rows and 1,024 columns."
                },
                "pyramid_level": {
                        "type": "string",
                        "description": "The number of reduced-resolution dataset layers that will be built. The default value is -1, which will build full pyramids. A value of 0 will result in no pyramid levels.To delete pyramids, set the n...",
                        "default": None
                },
                "skip_first": {
                        "type": "string",
                        "description": "Specifies whether the first pyramid level will be skipped. Skipping the first level will take up slightly less disk space but will slow down performance at these scales.NONE\u2014The first pyramid level wi...",
                        "default": None
                },
                "resample_technique": {
                        "type": "string",
                        "description": "Specifies the resampling technique that will be used to build the pyramids.NEAREST\u2014The value of the closest pixel will be used to assign a value to the output pixel when resampling. This is the defaul...",
                        "default": None
                },
                "compression_type": {
                        "type": "string",
                        "description": "Specifies the compression type that will be used when building the raster pyramids.DEFAULT\u2014If the source data is compressed using a wavelet compression, it will build pyramids with the JPEG compressio...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "The compression quality that will be used when pyramids are built with the JPEG compression type.\r\nThe value must be between 0 and 100. The values closer to 100 will produce a higher-quality image, bu...",
                        "default": None
                },
                "skip_existing": {
                        "type": "string",
                        "description": "Specifies whether pyramids will be built only when they are missing or \r\nwill be regenerated even if they exist.OVERWRITE\u2014Pyramids will be built even if they already exist, and existing pyramids will ...",
                        "default": None
                }
        },
        "required": [
                "in_raster_dataset"
        ]
},
    "build_pyramids_and_statistics": {
        "name": "build_pyramids_and_statistics",
        "description": "Traverses a folder structure, building pyramids and calculating statistics for all the raster datasets it contains. It can also build pyramids and calculate statistics for all the items in a mosaic dataset.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The workspace that contains all the raster datasets or mosaic datasets to be processed.If the workspace includes a mosaic dataset, only the statistics associated with the mosaic dataset will be includ..."
                },
                "include_subdirectories": {
                        "type": "string",
                        "description": "Specifies whether subdirectories will be included.NONE\u2014Does not include subdirectories. INCLUDE_SUBDIRECTORIES\u2014Includes all the raster datasets within the subdirectories when loading. This is the defa...",
                        "default": None
                },
                "build_pyramids": {
                        "type": "string",
                        "description": "Specifies whether pyramids will be built.NONE\u2014Pyramids will not be built.BUILD_PYRAMIDS\u2014Pyramids will be built. This is the default.",
                        "default": None
                },
                "calculate_statistics": {
                        "type": "string",
                        "description": "Specify whether to calculate statistics.NONE\u2014Does not calculate statistics.CALCULATE_STATISTICS\u2014Calculates statistics. This is the default.",
                        "default": None
                },
                "build_on_source": {
                        "type": "string",
                        "description": "Specify whether to calculate statistics on the source raster datasets, or calculate statistics on the raster items in a mosaic dataset.\r\nThis option only applies to mosaic datasets. NONE\u2014Statistics wi...",
                        "default": None
                },
                "block_field": {
                        "type": "string",
                        "description": "The name of the field within a mosaic dataset's attribute table\r\nused to identify items that should be considered one item when performing some calculations and operations.",
                        "default": None
                },
                "estimate_statistics": {
                        "type": "string",
                        "description": "Specify whether to calculate statistics for the mosaic dataset (not the rasters within it). The statistics are derived from the existing statistics that have been calculated for each raster in the mos...",
                        "default": None
                },
                "x_skip_factor": {
                        "type": "string",
                        "description": "The number of horizontal pixels between samples.A skip factor controls the portion of the raster that is used when calculating the statistics. The input value indicates the horizontal or vertical skip...",
                        "default": None
                },
                "y_skip_factor": {
                        "type": "string",
                        "description": "The number of vertical pixels between samples.A skip factor controls the portion of the raster that is used when calculating the statistics. The input value indicates the horizontal or vertical skip f...",
                        "default": None
                },
                "ignore_valuesignore_value": {
                        "type": "string",
                        "description": "The pixel values that are not to be included in the statistics calculation.The default is no value.",
                        "default": None
                },
                "pyramid_level": {
                        "type": "string",
                        "description": "The number of reduced-resolution dataset layers that will be built. The default value is -1, which will build full pyramids. A value of 0 will result in no pyramid levels.The maximum number of pyramid...",
                        "default": None
                },
                "skip_first": {
                        "type": "string",
                        "description": "Specifies whether the first pyramid level will be skipped. Skipping the first level will take up slightly less disk space but will slow down performance at these scales.NONE\u2014The first pyramid level wi...",
                        "default": None
                },
                "resample_technique": {
                        "type": "string",
                        "description": "Specifies the resampling technique that will be used to build the pyramids.NEAREST\u2014The value of the closest pixel will be used to assign a value to the output pixel when resampling. This is the defaul...",
                        "default": None
                },
                "compression_type": {
                        "type": "string",
                        "description": "Specifies the compression type that will be used when building the raster pyramids.DEFAULT\u2014If the source data is compressed using a wavelet compression, pyramids will be built using the JPEG compressi...",
                        "default": None
                },
                "compression_quality": {
                        "type": "string",
                        "description": "The compression quality that will be used when pyramids are built with the JPEG compression type.\r\nThe value must be between 0 and 100. The values closer to 100 will produce a higher-quality image, bu...",
                        "default": None
                },
                "skip_existing": {
                        "type": "string",
                        "description": "Specify whether to calculate statistics only where they are missing, or regenerate them even if they exist.SKIP_EXISTING\u2014Statistics will only be calculated if they do not already exist. This is the de...",
                        "default": None
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression to select raster datasets that will be processed.",
                        "default": None
                },
                "sips_mode": {
                        "type": "string",
                        "description": "Specifies whether  to enable building of pyramid files using key processes and algorithms defined in the Softcopy Image Processing Standard (SIPS), NGA.STND.0014.NONE\u2014Pyramids will be built using stan...",
                        "default": None
                }
        },
        "required": [
                "in_workspace"
        ]
},
    "build_raster_attribute_table": {
        "name": "build_raster_attribute_table",
        "description": "Adds a raster attribute table to a raster dataset or updates an existing one. This is used primarily with discrete data.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset to which a table will be added. This tool will not run if the pixel type is floating point or double precision."
                },
                "overwrite": {
                        "type": "string",
                        "description": "Specifies whether the existing table will be overwritten.NONE\u2014The existing raster attribute table will not be overwritten and any edits will be appended to it. This is the default.Overwrite\u2014The existi...",
                        "default": None
                },
                "convert_colormap": {
                        "type": "string",
                        "description": "Specifies whether the color map will be converted to a raster attribute table. The output raster attribute table will include Red, Green, and Blue fields containing color values from the color map. Th...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "calculate_statistics": {
        "name": "calculate_statistics",
        "description": "Calculates statistics for a raster dataset or a mosaic dataset. Statistics are required for raster and mosaic datasets to perform certain tasks, such as applying a contrast stretch or classifying data.",
        "parameters": {
                "in_raster_dataset": {
                        "type": "string",
                        "description": "The input raster dataset or mosaic dataset."
                },
                "x_skip_factor": {
                        "type": "string",
                        "description": "The number of horizontal pixels between samples.A skip factor controls the portion of the raster that is used when calculating the statistics. The input value indicates the horizontal or vertical skip...",
                        "default": None
                },
                "y_skip_factor": {
                        "type": "string",
                        "description": "The number of vertical pixels between samples.A skip factor controls the portion of the raster that is used when calculating the statistics. The input value indicates the horizontal or vertical skip f...",
                        "default": None
                },
                "ignore_valuesignore_value": {
                        "type": "string",
                        "description": "The pixel values that are not to be included in the statistics calculation.The default is no value or the last ignore value used.",
                        "default": None
                },
                "skip_existing": {
                        "type": "string",
                        "description": "Specifies whether statistics will be calculated only when they are missing or will be regenerated even if they exist.OVERWRITE\u2014Statistics will be calculated even if they already exist, and existing st...",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "The feature class that represents the area in the dataset that will be used to calculate statistics, so they are not generated from the entire dataset.",
                        "default": None
                }
        },
        "required": [
                "in_raster_dataset"
        ]
},
    "convert_raster_function__template": {
        "name": "convert_raster_function__template",
        "description": "Converts a raster function template between formats (rft.xml, json, and binary).",
        "parameters": {
                "in_raster_function_template": {
                        "type": "string",
                        "description": "The input raster function template file. The input template file can be XML, JSON, or binary format."
                },
                "out_raster_function_template_file": {
                        "type": "string",
                        "description": "The output raster function template file path and file name."
                },
                "format": {
                        "type": "string",
                        "description": "The output function template file format.\r\nXML\u2014XML output format.JSON\u2014JSON output format. This is the default.BINARY\u2014Binary output format.",
                        "default": None
                }
        },
        "required": [
                "in_raster_function_template",
                "out_raster_function_template_file"
        ]
},
    "delete_colormap": {
        "name": "delete_colormap",
        "description": "Removes the color map associated with a raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset that containing the color map you want to remove."
                }
        },
        "required": [
                "in_raster"
        ]
},
    "delete_raster_attribute_table": {
        "name": "delete_raster_attribute_table",
        "description": "Removes the raster attribute table associated with a raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset containing the attribute table you want to remove."
                }
        },
        "required": [
                "in_raster"
        ]
},
    "export_raster_world_file": {
        "name": "export_raster_world_file",
        "description": "Creates a world file based on the pixel size and the location of the upper left pixel.",
        "parameters": {
                "in_raster_dataset": {
                        "type": "string",
                        "description": "The raster dataset from which you want to create the world file."
                }
        },
        "required": [
                "in_raster_dataset"
        ]
},
    "get_cell_value": {
        "name": "get_cell_value",
        "description": "Retrieves the value of a given pixel using its x, y coordinates.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster that you want to query."
                },
                "location_point": {
                        "type": "string",
                        "description": "The X and Y coordinates of the pixel location."
                },
                "band_index": {
                        "type": "string",
                        "description": "Specify the bands that you want to query. Leave blank to query all bands in a multiband dataset.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "location_point"
        ]
},
    "get_raster_properties": {
        "name": "get_raster_properties",
        "description": "Retrieves  information from the metadata and descriptive statistics about a raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster containing the properties to retrieve."
                },
                "band_index": {
                        "type": "string",
                        "description": "Choose the band name from which to get the properties. If no band is chosen, then the first band will be used.",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "set_raster_properties": {
        "name": "set_raster_properties",
        "description": "Sets the data type, statistics, and NoData values on a raster or mosaic dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster or mosaic dataset with the properties that will be set."
                },
                "data_type": {
                        "type": "string",
                        "description": "Specifies the type of imagery in the raster.GENERIC\u2014 The raster does not have a specified data type.ELEVATION\u2014 The raster contains elevation data.THEMATIC\u2014The raster contains thematic data, which has ...",
                        "default": None
                },
                "statisticsband_index_min_max_mean_std_dev": {
                        "type": "string",
                        "description": "The bands and  values for the minimum, maximum, mean, and standard deviation.",
                        "default": None
                },
                "stats_file": {
                        "type": "string",
                        "description": "An .xml file that contains the statistics.",
                        "default": None
                },
                "nodataband_index_nodata_value": {
                        "type": "string",
                        "description": "The NoData value for each band. Each band can have a unique NoData value defined, or the same value can be specified for all bands. To define multiple NoData values for each band selection, use a spac...",
                        "default": None
                },
                "multidimensional_info": {
                        "type": "string",
                        "description": "The dimensional information for the raster dataset. Setting dimensional information will convert a  dimensionless raster  into a multidimensional raster.If the dimension is time, the dimension name mu...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "add_rule_to_relationship_class": {
        "name": "add_rule_to_relationship_class",
        "description": "Adds a rule to a relationship class. A relationship class is created with one-to-one, one-to-many, or many-to-many cardinality. A relationship class can be defined in more restrictive terms by adding a rule to a relationship class. Once a rule is added to a relationship class, that rule becomes the only valid relationship that can exist. To make other relationship combinations and cardinalities valid, additional relationship rules must be added. Learn more about relationship rules",
        "parameters": {
                "in_rel_class": {
                        "type": "string",
                        "description": "The relationship class to which a rule will be added."
                },
                "origin_subtype": {
                        "type": "string",
                        "description": "Specifies the subtype of the origin class. If the origin class has subtypes, choose the subtype to which you want to associate a relationship class rule. If the origin class has no subtypes, the relat...",
                        "default": None
                },
                "origin_minimum": {
                        "type": "string",
                        "description": "Specifies the minimum range cardinality for the origin class if the relationship class is many-to-many.",
                        "default": None
                },
                "origin_maximum": {
                        "type": "string",
                        "description": "Specifies the maximum range cardinality for the origin class if the relationship class is many-to-many or one-to-many.",
                        "default": None
                },
                "destination_subtype": {
                        "type": "string",
                        "description": "Specifies the subtype of the destination class. If the destination class has subtypes, choose the subtype to which you want to associate a relationship class rule. If the destination class has no subt...",
                        "default": None
                },
                "destination_minimum": {
                        "type": "string",
                        "description": "Specifies the minimum range cardinality for the destination class if the relationship class is many-to-many or one-to-many.",
                        "default": None
                },
                "destination_maximum": {
                        "type": "string",
                        "description": "Specifies the maximum range cardinality for the destination class if the relationship class is many-to-many or one-to-many.",
                        "default": None
                }
        },
        "required": [
                "in_rel_class"
        ]
},
    "create_relationship_class": {
        "name": "create_relationship_class",
        "description": "Creates a relationship class to store an association between fields or features in the origin table and the destination table.",
        "parameters": {
                "origin_table": {
                        "type": "string",
                        "description": "The table or feature class that is associated with the destination table."
                },
                "destination_table": {
                        "type": "string",
                        "description": "The table that is associated with the origin table."
                },
                "out_relationship_class": {
                        "type": "string",
                        "description": "The relationship class that will be created."
                },
                "relationship_type": {
                        "type": "string",
                        "description": "Specifies the type of relationship that will be created between the origin and destination tables.SIMPLE\u2014The origin and destination tables will have a simple relationship. This is the default. COMPOSI..."
                },
                "forward_label": {
                        "type": "string",
                        "description": "A name to uniquely identify the relationship when navigating from the origin table to the destination table."
                },
                "backward_label": {
                        "type": "string",
                        "description": "A name to uniquely identify the relationship when navigating from the destination table to the origin table."
                },
                "message_direction": {
                        "type": "string",
                        "description": "Specifies the direction in which messages will be passed between the origin and destination tables. For example, in a relationship between poles and transformers, when a pole is deleted, a message wil..."
                },
                "cardinality": {
                        "type": "string",
                        "description": "Specifies how many relationships will exist between rows or features in the origin table and rows or features in the destination table.ONE_TO_ONE\u2014Each row or feature in the origin table can be related..."
                },
                "attributed": {
                        "type": "string",
                        "description": "Specifies whether the relationship class will have attributes.NONE\u2014The relationship class will not have attributes. This is the default. ATTRIBUTED\u2014The relationship class will have attributes."
                },
                "origin_primary_key": {
                        "type": "string",
                        "description": "For many-to-many or attributed relationship classes, this is the field in the origin table that links to the origin_foreign_key field in the relationship class table.For one-to-one or one-to-many rela..."
                },
                "origin_foreign_key": {
                        "type": "string",
                        "description": "For many-to-many or attributed relationship classes, this is the field in the relationship class table that links to the origin_primary_key field in the origin table.For one-to-one or one-to-many rela..."
                },
                "destination_primary_key": {
                        "type": "string",
                        "description": "The  field in the destination table that links  to the destination_foreign_key field in the relationship class table. This value is required for many-to-many or attributed relationship classes, but sh...",
                        "default": None
                },
                "destination_foreign_key": {
                        "type": "string",
                        "description": "The field in the relationship class table that links to the destination_primary_key field in the destination table. This value is required for many-to-many or attributed relationship classes, but shou...",
                        "default": None
                }
        },
        "required": [
                "origin_table",
                "destination_table",
                "out_relationship_class",
                "relationship_type",
                "forward_label",
                "backward_label",
                "message_direction",
                "cardinality",
                "attributed",
                "origin_primary_key",
                "origin_foreign_key"
        ]
},
    "migrate_relationship_class": {
        "name": "migrate_relationship_class",
        "description": "Migrates an object ID-based relationship class to a global ID-based relationship class.",
        "parameters": {
                "in_relationship_class": {
                        "type": "string",
                        "description": "An object ID-based relationship class\r\nthat will be migrated to a global ID-based relationship class.  The origin and destination feature classes or tables must have an existing GlobalID field."
                }
        },
        "required": [
                "in_relationship_class"
        ]
},
    "remove_rule_from_relationship_class": {
        "name": "remove_rule_from_relationship_class",
        "description": "Removes a rule from a relationship class. Learn more about relationship rules",
        "parameters": {
                "in_rel_class": {
                        "type": "string",
                        "description": "The relationship class with the rule to remove."
                },
                "origin_subtype": {
                        "type": "string",
                        "description": "If the origin class has subtypes, the subtype that is associated with the relationship class rule to be deleted.",
                        "default": None
                },
                "destination_subtype": {
                        "type": "string",
                        "description": "If the destination class has subtypes, the subtype that is associated with the relationship class rule to be deleted.",
                        "default": None
                },
                "remove_all": {
                        "type": "string",
                        "description": "Specifies the relationship rules to be removed from the relationship class.\r\nREMOVE\u2014All relationship rules will be removed from the input relationship class.NOT_ALL\u2014Only rules from the origin and dest...",
                        "default": None
                }
        },
        "required": [
                "in_rel_class"
        ]
},
    "set_relationship_class_split_policy": {
        "name": "set_relationship_class_split_policy",
        "description": "Defines the split policy for related features. Learn more about the split policy for a relationship class",
        "parameters": {
                "in_rel_class": {
                        "type": "string",
                        "description": "The relationship class on which the split policy will be set.\r\nThe origin feature class must be a polyline or polygon feature class and the destination must be a nonspatial table."
                },
                "split_policy": {
                        "type": "string",
                        "description": "Specifies the split policy to apply to the relationship class.\r\nDEFAULT_COMPOSITE\u2014 If the feature class split model is Delete/Insert/Insert, the relationships and the part objects will be deleted. If ..."
                }
        },
        "required": [
                "in_rel_class",
                "split_policy"
        ]
},
    "table_to_relationship_class": {
        "name": "table_to_relationship_class",
        "description": "Creates an attributed relationship class from the origin, destination, and relationship tables.",
        "parameters": {
                "origin_table": {
                        "type": "string",
                        "description": "The table or feature class that will be associated to the destination table."
                },
                "destination_table": {
                        "type": "string",
                        "description": "The table or feature class that will be associated to the origin table."
                },
                "out_relationship_class": {
                        "type": "string",
                        "description": "The relationship class that will be created."
                },
                "relationship_type": {
                        "type": "string",
                        "description": "Specifies the type of association that will be created between the origin and destination tables.SIMPLE\u2014Each object will be independent of each other (a parent-to-parent relationship). This is the def..."
                },
                "forward_label": {
                        "type": "string",
                        "description": "A label describing the relationship as it is traversed from the origin table or feature class to the destination table or feature class."
                },
                "backward_label": {
                        "type": "string",
                        "description": "A label describing the relationship as it is traversed from the destination table or feature class to the origin table or feature class."
                },
                "message_direction": {
                        "type": "string",
                        "description": "Specifies the direction messages that will be propagated between the objects in the relationship. For example, in a relationship between poles and transformers, when the pole is deleted, it sends a me..."
                },
                "cardinality": {
                        "type": "string",
                        "description": "Specifies the cardinality of the relationship between the origin and destination.ONE_TO_ONE\u2014Each object of the origin table or feature class can be related to zero or one object of the destination tab..."
                },
                "relationship_table": {
                        "type": "string",
                        "description": "The table containing attributes that will be added to the relationship class."
                },
                "attribute_fields": {
                        "type": "string",
                        "description": "The names of the fields containing attribute values that will be added to the relationship class. The fields must be present in the relationship_table parameter value."
                },
                "origin_primary_key": {
                        "type": "string",
                        "description": "The field in the origin table that will be used to create the relationship."
                },
                "origin_foreign_key": {
                        "type": "string",
                        "description": "The name of the field in the relationship table that refers to the primary key field in the origin table or feature class. For table-based relationship classes, these values are used to populate the r..."
                },
                "destination_primary_key": {
                        "type": "string",
                        "description": "The field in the destination table that will be used to create the relationship."
                },
                "destination_foreign_key": {
                        "type": "string",
                        "description": "The field in the relationship table that refers to the primary key field in the destination table or feature class. For table-based relationship classes, these values are used to populate the relation..."
                }
        },
        "required": [
                "origin_table",
                "destination_table",
                "out_relationship_class",
                "relationship_type",
                "forward_label",
                "backward_label",
                "message_direction",
                "cardinality",
                "relationship_table",
                "attribute_fields",
                "origin_primary_key",
                "origin_foreign_key",
                "destination_primary_key",
                "destination_foreign_key"
        ]
},
    "export_report_to_excel": {
        "name": "export_report_to_excel",
        "description": "Exports an ArcGIS Pro report or a report file to a Microsoft Excel file  (.xlsx). Learn more about reports",
        "parameters": {
                "in_report": {
                        "type": "string",
                        "description": "The input report or .rptx file."
                },
                "out_xlsx_file": {
                        "type": "string",
                        "description": "The output Excel file."
                },
                "expression": {
                        "type": "string",
                        "description": "An SQL expression that will be used to select a subset of records. This expression will be applied in addition to any existing expressions.",
                        "default": None
                },
                "adjust_row_height": {
                        "type": "string",
                        "description": "Specifies whether the row height will adjust to fit the content of the cell.ADJUST_ROW_HEIGHT\u2014The row height will collapse or expand to fit the content of the cell. This is the default.NO_ADJUST_ROW_H...",
                        "default": None
                },
                "merge_cells": {
                        "type": "string",
                        "description": "Specifies whether the cells of the Excel file will be merged to fit the content.MERGE_CELLS\u2014The cells of the Excel file will be merged to fit the content. This is the default.NO_MERGE_CELLS\u2014The cells ...",
                        "default": None
                },
                "remove_vertical_whitespace": {
                        "type": "string",
                        "description": "Specifies whether extra white space will be removed from the output Excel file.REMOVE_WHITESPACE\u2014Extra white space will be removed from the output Excel file. This is the default.NO_REMOVE_WHITESPACE\u2014...",
                        "default": None
                },
                "display_gridlines": {
                        "type": "string",
                        "description": "Specifies whether grid lines will be automatically displayed when viewing sheets in the output Excel file.DISPLAY_GRIDLINES\u2014Grid lines will be automatically displayed when viewing sheets in the output...",
                        "default": None
                },
                "export_unsupported_formats_as_text": {
                        "type": "string",
                        "description": "Specifies whether unsupported numeric formats will be exported as text.VALUE_AS_TEXT\u2014Unsupported numeric formats will be exported as text.RAW_VALUE\u2014Unsupported numeric formats will be exported as a ge...",
                        "default": None
                },
                "sheet_export": {
                        "type": "string",
                        "description": "Specifies how each report will be exported to sheets.ALL\u2014All report sections will be exported to an individual sheet. This is the default.SUBREPORT\u2014Each subreport will be exported to  an individual  s...",
                        "default": None
                },
                "page_range_type": {
                        "type": "string",
                        "description": "Specifies the page range of the report  that will exported.ALL\u2014All pages will be exported. This is the default.LAST\u2014Only the last page only will be exported.ODD\u2014Only odd numbered pages will be exporte...",
                        "default": None
                },
                "custom_page_range": {
                        "type": "string",
                        "description": "The pages that will be exported when the page_range_type parameter is set to CUSTOM.  You can set individual pages, ranges, or a combination of both separated by commas, such as 1, 3-5, 10.",
                        "default": None
                },
                "initial_page_number": {
                        "type": "string",
                        "description": "The initial page number of the report that will be used to create a  page numbering offset to add more pages to the beginning of the report.",
                        "default": None
                },
                "final_page_number": {
                        "type": "string",
                        "description": "The page number that will be displayed on the last page of the Excel file.",
                        "default": None
                }
        },
        "required": [
                "in_report",
                "out_xlsx_file"
        ]
},
    "export_report_to_pdf": {
        "name": "export_report_to_pdf",
        "description": "Exports an ArcGIS Pro report or a report file (.rptx) to a .pdf file. Learn more about reports",
        "parameters": {
                "in_report": {
                        "type": "string",
                        "description": "The input report or .rptx file."
                },
                "out_pdf_file": {
                        "type": "string",
                        "description": "The output .pdf file."
                },
                "expression": {
                        "type": "string",
                        "description": "A SQL expression that will be used to select a subset of records. This expression is applied in addition to any existing expressions.",
                        "default": None
                },
                "resolution": {
                        "type": "string",
                        "description": "The resolution of the output .pdf file in dots per inch (dpi).",
                        "default": None
                },
                "image_quality": {
                        "type": "string",
                        "description": "Specifies the output image quality of the PDF. The image quality option controls the quality of exported rasterized data.BEST\u2014The highest available image quality will be used. This is the default.BETT...",
                        "default": None
                },
                "embed_font": {
                        "type": "string",
                        "description": "Specifies whether fonts will be embedded in the output .pdf file. Font embedding allows text and markers built from font glyphs to be displayed correctly when the .pdf file is viewed on a computer tha...",
                        "default": None
                },
                "compress_vector_graphics": {
                        "type": "string",
                        "description": "Specifies whether vector graphics will be compressed.COMPRESS_GRAPHICS\u2014Vector graphics will be compressed. Use this option unless clear text is wanted for troubleshooting. This is the default.NO_COMPR...",
                        "default": None
                },
                "image_compression": {
                        "type": "string",
                        "description": "Specifies the compression scheme that will be used to compress image or raster data in the output .pdf file.\r\nNONE\u2014Image or raster data will not be compressed.RLE\u2014Image or raster data will be compress...",
                        "default": None
                },
                "password_protect": {
                        "type": "string",
                        "description": "Specifies whether a password will be needed to view the output .pdf file.PASSWORD_PROTECT\u2014The output .pdf file will require a password  to open.NO_PASSWORD_PROTECT\u2014The output .pdf file can be opened w...",
                        "default": None
                },
                "pdf_password": {
                        "type": "string",
                        "description": "The password that will be required to open the .pdf file.",
                        "default": None
                },
                "page_range_type": {
                        "type": "string",
                        "description": "Specifies the page range of the report  that will exported.ALL\u2014All pages will be exported. This is the default.LAST\u2014Only the last page only will be exported.ODD\u2014Only odd numbered pages will be exporte...",
                        "default": None
                },
                "custom_page_range": {
                        "type": "string",
                        "description": "The pages that will be exported when the page_range_type parameter is set to CUSTOM.  You can set individual pages, ranges, or a combination of both separated by commas, such as 1, 3-5, 10.",
                        "default": None
                },
                "initial_page_number": {
                        "type": "string",
                        "description": "The initial page number that will be used to create a  page numbering offset to add more pages to the beginning of the report.",
                        "default": None
                },
                "final_page_number": {
                        "type": "string",
                        "description": "The page number that will be displayed on the last page of the output .pdf file.",
                        "default": None
                },
                "selection_symbology": {
                        "type": "string",
                        "description": "Specifies whether selection symbology will be included when exporting a report with a map frame and selected features in the source map.SELECTION_SYMBOLOGY\u2014Selection symbology will be included in the ...",
                        "default": None
                }
        },
        "required": [
                "in_report",
                "out_pdf_file"
        ]
},
    "create_fishnet": {
        "name": "create_fishnet",
        "description": "Creates a fishnet of rectangular cells.  The output can be polyline or polygon features. Learn more about how Create Fishnet works",
        "parameters": {
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the fishnet of rectangular cells."
                },
                "origin_coord": {
                        "type": "string",
                        "description": "The pivot point of the fishnet."
                },
                "y_axis_coord": {
                        "type": "string",
                        "description": "The y-axis coordinate that will be used to orient the fishnet. The fishnet will be rotated by the same angle as defined by the line connecting the origin and the y-axis coordinate."
                },
                "cell_width": {
                        "type": "string",
                        "description": "The width of each cell.To calculate the cell width using the number_rows parameter value, leave this parameter unspecified or set the value to zero; the width will be calculated when the tool is run."
                },
                "cell_height": {
                        "type": "string",
                        "description": "The height of each cell.To calculate the cell height using the number_columns parameter value,  leave this parameter unspecified or set the value to zero; the height will be calculated when the tool i..."
                },
                "number_rows": {
                        "type": "string",
                        "description": "The number of rows in the output fishnet.To calculate the number of rows using the cell_width parameter value,  leave this parameter unspecified or set the value to zero; the number of rows will be ca..."
                },
                "number_columns": {
                        "type": "string",
                        "description": "The number of columns in the output fishnet.To calculate the number of columns using the cell_height parameter value,  leave this parameter unspecified or set the value to zero; the number of columns ..."
                },
                "corner_coord": {
                        "type": "string",
                        "description": "The opposite corner of the fishnet set by the origin_coord parameter.This parameter is disabled if the origin_coord, y_axis_coord, cell_width, cell_height, number_rows, and number_columns parameters a...",
                        "default": None
                },
                "labels": {
                        "type": "string",
                        "description": "Specifies whether a point feature class will be created containing label points at the center of each fishnet cell.LABELS\u2014A point feature class will be created. This is the default.NO_LABELS\u2014A point f...",
                        "default": None
                },
                "template": {
                        "type": "string",
                        "description": "The extent of the fishnet. The extent can be provided by specifying the coordinates or using a template dataset.\r\nMAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to a...",
                        "default": None
                },
                "geometry_type": {
                        "type": "string",
                        "description": "Specifies whether the output fishnet cells will be polyline or polygon features.POLYLINE\u2014The output will be a polyline feature class. Each cell is defined by four line features.POLYGON\u2014The output will...",
                        "default": None
                }
        },
        "required": [
                "out_feature_class",
                "origin_coord",
                "y_axis_coord",
                "cell_width",
                "cell_height",
                "number_rows",
                "number_columns"
        ]
},
    "create_random_points": {
        "name": "create_random_points",
        "description": "Creates a specified number of random point features. Random points can be generated in an extent window, inside polygon features, on point features, or along line features. Learn more about how Create Random Points works",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The location or workspace in which the random points feature class will be created. This location or workspace must already exist."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the random points feature class to be created."
                },
                "constraining_feature_class": {
                        "type": "string",
                        "description": "Random points will be generated inside or along the features in this feature class. The constraining feature class can be point, multipoint, line, or polygon. Points will be randomly placed inside pol...",
                        "default": None
                },
                "constraining_extent": {
                        "type": "string",
                        "description": "Random points will be generated inside the extent. The constraining extent will only be used if no constraining feature class is specified.\r\nMAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014T...",
                        "default": None
                },
                "number_of_points_or_field": {
                        "type": "string",
                        "description": "The number of points to be randomly generated.The number of points can be specified as a long integer number or as a field from the constraining features containing numeric values for how many random ...",
                        "default": None
                },
                "minimum_allowed_distance": {
                        "type": "string",
                        "description": "The shortest distance allowed between any two randomly placed points. If a value of 1 Meter is specified, all random points will be farther than 1 meter away from the closest point.",
                        "default": None
                },
                "create_multipoint_output": {
                        "type": "string",
                        "description": "Determines if the output feature class will be a multipart or single-part feature.POINT\u2014The output will be geometry type point (each point is a separate feature). This is the default.MULTIPOINT\u2014The ou...",
                        "default": None
                },
                "multipoint_size": {
                        "type": "string",
                        "description": "If create_multipoint_output is set to MULTIPOINT, specify the number of random points to be placed in each multipoint geometry. The default is 10.",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "create_spatially_balanced_points": {
        "name": "create_spatially_balanced_points",
        "description": "Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design. This tool is typically used for designing a monitoring network by suggesting locations to take samples, and a preference for particular locations can be defined using an inclusion probability raster. Learn more about how Create Spatially Balanced Points works",
        "parameters": {
                "in_probability_raster": {
                        "type": "string",
                        "description": "Defines the inclusion probabilities for each location in the area of interest. The location values must range from 0 (low inclusion probability) to 1 (high inclusion probability)."
                },
                "number_output_points": {
                        "type": "string",
                        "description": "The number of sample locations that will be created."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the selected sample locations and their inclusion probabilities."
                }
        },
        "required": [
                "in_probability_raster",
                "number_output_points",
                "out_feature_class"
        ]
},
    "create_spatial_sampling_locations": {
        "name": "create_spatial_sampling_locations",
        "description": "Creates sample locations within a continuous study area using simple random, stratified, systematic (gridded), or cluster sampling designs. Sampling is the process of selecting individuals from a population to study them and make inferences about the entire population.  Continuous spatial sampling treats the population as a continuous area from which any location or area can be sampled.  For example, you can use this tool to create sample locations for trees within a dense forest or to collect soil moisture measurements in a crop field.  This tool is not appropriate for sampling discrete populations such as households, animals, or cities.",
        "parameters": {
                "in_study_area": {
                        "type": "string",
                        "description": "The input study area where sample locations will be created. The study area must be polygons or an integer (categorical) raster.  For rasters, cells with None values will not be included in the study ..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features representing the sample locations. For simple random and stratified sampling, the output features will be points. For cluster sampling, the output will be polygons. For systematic ..."
                },
                "sampling_method": {
                        "type": "string",
                        "description": "Specifies the sampling method that will be used to create the sample locations.RANDOM\u2014Points will be randomly created in the study area, and all locations have the same likelihood of being sampled. Al...",
                        "default": None
                },
                "strata_id_field": {
                        "type": "string",
                        "description": "For stratified sampling by strata ID field, the strata ID field defining the strata.",
                        "default": None
                },
                "strata_count_method": {
                        "type": "string",
                        "description": "For stratified sampling, specifies the method that will be used to determine the number of sample locations that will be created in each stratum. \r\nEQUAL\u2014The same number of sample locations will be cr...",
                        "default": None
                },
                "bin_shape": {
                        "type": "string",
                        "description": "For systematic and cluster sampling, specifies the shape of the polygons that will be generated in the gridded tessellation.  \r\nHEXAGON\u2014Hexagon-shaped features will be generated. The top and bottom si...",
                        "default": None
                },
                "bin_size": {
                        "type": "string",
                        "description": "For systematic and cluster sampling, the size of each polygon in the tessellation. The value can be provided as a count (the total number of tessellated polygons created in the study area) or as an ar...",
                        "default": None
                },
                "h3_resolution": {
                        "type": "string",
                        "description": "For systematic or cluster sampling with H3 hexagon bins, specifies the H3 resolution of the hexagons.With each increasing resolution value, the area of the polygons will be one seventh the size. 0\u2014Hex...",
                        "default": None
                },
                "num_samples": {
                        "type": "string",
                        "description": "The number of sample locations that will be created.  This parameter always applies to simple random and cluster sampling.  For stratified sampling, this parameter applies when the sample count will b...",
                        "default": None
                },
                "num_samples_per_strata": {
                        "type": "string",
                        "description": "For stratified sampling with an equal sample count in each stratum, the number of sample locations created within each stratum.  The total number of samples will be this value multiplied by the number...",
                        "default": None
                },
                "population_field": {
                        "type": "string",
                        "description": "The population field for stratified sampling when the sample count is equal or proportional to a population field.",
                        "default": None
                },
                "geometry_type": {
                        "type": "string",
                        "description": "For systematic sampling, specifies whether the sample locations will be tessellated polygons or centroids (points) of the tessellated polygons.POINT\u2014Centroids of the tessellated polygons will be creat...",
                        "default": None
                },
                "min_distance": {
                        "type": "string",
                        "description": "For simple random and stratified sampling, the smallest allowed distance between sample locations. For simple random sampling, all points will be at least this distance apart.  For stratified sampling...",
                        "default": None
                },
                "spatial_relationship": {
                        "type": "string",
                        "description": "Specifies which polygons from a background tessellation will be included as sampling locations. This parameter  applies to cluster sampling and to systematic sampling when the output geometry type is ...",
                        "default": None
                }
        },
        "required": [
                "in_study_area",
                "out_features"
        ]
},
    "generate_points_along_lines": {
        "name": "generate_points_along_lines",
        "description": "Creates point features along lines or polygons.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The line or polygon features that will be used to place points."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The point feature class that will be created from the input features."
                },
                "point_placement": {
                        "type": "string",
                        "description": "Specifies the method that will be used to place points.PERCENTAGE\u2014The Percentage parameter value will be used to place points along the features by percentage.DISTANCE\u2014The Distance parameter value wil..."
                },
                "distance": {
                        "type": "string",
                        "description": "The interval from the beginning of the feature \r\nat which points will be placed.This parameter is active when the Point_Placement parameter is set to DISTANCE.",
                        "default": None
                },
                "percentage": {
                        "type": "string",
                        "description": "The percentage from the beginning of the feature at which points will be placed. For example, if a percentage of 40 is used, \r\npoints will be placed at 40 percent and 80 percent of the feature's dista...",
                        "default": None
                },
                "include_end_points": {
                        "type": "string",
                        "description": "Specifies whether additional points will be included at the start point and end point of the feature.END_POINTS\u2014Additional points will be included at the start point and end point of the feature.NO_EN...",
                        "default": None
                },
                "add_chainage_fields": {
                        "type": "string",
                        "description": "Specifies whether the accumulated distance and sequence fields will be added to the output.ADD_CHAINAGE\u2014The accumulated distance (ORIG_LEN) and sequence (ORIG_SEQ) fields will be added to the output. ...",
                        "default": None
                },
                "distance_field": {
                        "type": "string",
                        "description": "A field from the input features that will be used to place output points.If the field is a numeric type, the field value will be used to place points at that interval.If the field is a string type, th...",
                        "default": None
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies the measurement method that will be used to create the points.This parameter is active when the Point_Placement parameter is set to DISTANCE.PLANAR\u2014Points will be created using a planar meth...",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_feature_class",
                "point_placement"
        ]
},
    "generate_rectangles_along_lines": {
        "name": "generate_rectangles_along_lines",
        "description": "Creates a series of rectangular polygons that follow a single linear feature or a group of linear features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polyline features defining the path of the features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class."
                },
                "length_along_line": {
                        "type": "string",
                        "description": "The length of the output polygon features along the input line features. The default value is determined by the spatial reference of the input line features. This value will be 1/100 of the input feat...",
                        "default": None
                },
                "spatial_sort_method": {
                        "type": "string",
                        "description": "Output features are created in a sequential order and require a spatial starting point. Setting the direction type to upper right will start the output features in the upper right of each input featur...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "generate_tessellation": {
        "name": "generate_tessellation",
        "description": "Generates a tessellated grid of regular polygon features to cover a given extent.  The tessellation can be of triangles, squares, diamonds, hexagons, H3 hexagons, or transverse hexagons.",
        "parameters": {
                "output_feature_class": {
                        "type": "string",
                        "description": "The path and name of the output  feature class containing the tessellated grid."
                },
                "extent": {
                        "type": "string",
                        "description": "The extent that the tessellation will cover.\r\nThis can be the currently visible area, the extent of a dataset, or manually entered values.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The ..."
                },
                "shape_type": {
                        "type": "string",
                        "description": "Specifies the shape that will be generated.HEXAGON\u2014Hexagon-shaped features will be generated. The top and bottom side of each hexagon will be parallel with the x-axis of the coordinate system (the top...",
                        "default": None
                },
                "size": {
                        "type": "string",
                        "description": "The area of each individual shape that comprises the tessellation.",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference that will be assigned to the output feature class.",
                        "default": None
                },
                "h3_resolution": {
                        "type": "string",
                        "description": "Specifies the H3 resolution of the hexagons.With each increasing resolution value, the area of the polygons will be one seventh the size. 0\u2014Hexagons will be created at the H3 resolution of 0, with an ...",
                        "default": None
                }
        },
        "required": [
                "output_feature_class",
                "extent"
        ]
},
    "generate_transects_along_lines": {
        "name": "generate_transects_along_lines",
        "description": "Creates perpendicular transect lines at a regular interval along lines.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The line features along which perpendicular transect lines will be generated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output perpendicular transect lines generated along the input features."
                },
                "interval": {
                        "type": "string",
                        "description": "The interval from the beginning of the feature \r\nat which transects will be placed."
                },
                "transect_length": {
                        "type": "string",
                        "description": "The length or width of the transect line. Each transect will be placed in such a way along the input line that half its length falls on one side of the line, and half its length falls on the other sid..."
                },
                "include_ends": {
                        "type": "string",
                        "description": "Specifies whether transects will be generated at the start and end of the input line.END_POINTS\u2014Transects will be generated at the start and end of the input line.NO_END_POINTS\u2014Transects will not be g...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "interval",
                "transect_length"
        ]
},
    "subset_features": {
        "name": "subset_features",
        "description": "Divides the records of a feature class or table into two subsets: one subset to be used as training data, and one subset to be used as test features to compare and validate the output surface.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features or table from which subsets will be created."
                },
                "out_training_feature_class": {
                        "type": "string",
                        "description": "The subset of training features that will be created."
                },
                "out_test_feature_class": {
                        "type": "string",
                        "description": "The subset of test features that will be created.",
                        "default": None
                },
                "size_of_training_dataset": {
                        "type": "string",
                        "description": "The size of the output training feature class, entered either as a percentage of the input features or as an absolute number of features.",
                        "default": None
                },
                "subset_size_units": {
                        "type": "string",
                        "description": "Specifies whether the subset size value will be used as a percentage of the input features or as an absolute number of features.PERCENTAGE_OF_INPUT\u2014 The subset size will be used as a percentage of the...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_training_feature_class"
        ]
},
    "add_subtype": {
        "name": "add_subtype",
        "description": "Adds a new subtype to the subtypes in the input table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The feature class or table containing the subtype definition to be updated."
                },
                "subtype_code": {
                        "type": "string",
                        "description": "A unique integer value for the subtype to be added."
                },
                "subtype_description": {
                        "type": "string",
                        "description": "A name (also known as description) of the subtype code."
                }
        },
        "required": [
                "in_table",
                "subtype_code",
                "subtype_description"
        ]
},
    "remove_subtype": {
        "name": "remove_subtype",
        "description": "Removes a subtype from the input table using its code.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The feature class or table containing the subtype definition."
                },
                "subtype_code": {
                        "type": "string",
                        "description": "The subtype code to remove a subtype from the input table or feature class."
                }
        },
        "required": [
                "in_table",
                "subtype_code"
        ]
},
    "set_default_subtype": {
        "name": "set_default_subtype",
        "description": "Sets the default value or code for the input table's subtype.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table or feature class whose subtype default value will be set."
                },
                "subtype_code": {
                        "type": "string",
                        "description": "The unique default value for a subtype."
                }
        },
        "required": [
                "in_table",
                "subtype_code"
        ]
},
    "set_subtype_field": {
        "name": "set_subtype_field",
        "description": "Defines the field in the input table or feature class that stores the subtype codes.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table or feature class that contains the field to set as a subtype field."
                },
                "field": {
                        "type": "string",
                        "description": "The integer field that will store the subtype codes.",
                        "default": None
                },
                "clear_value": {
                        "type": "string",
                        "description": "Specifies whether to clear the subtype field.CLEAR_SUBTYPE_FIELD\u2014The subtype field will be cleared (set to None).DO_NOT_CLEAR\u2014The subtype field will not be cleared. This is the default.",
                        "default": None
                }
        },
        "required": [
                "in_table"
        ]
},
    "analyze": {
        "name": "analyze",
        "description": "Updates database statistics of business tables, feature tables, and delta tables, along with the statistics of those tables' indexes.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The table or feature class to be analyzed."
                },
                "components": {
                        "type": "string",
                        "description": "Specifies the component type that will be analyzed.BUSINESS\u2014Business rules statistics will be updated.FEATURE\u2014Feature statistics will be updated.RASTER\u2014Statistics on raster tables will be updated.ADDS..."
                }
        },
        "required": [
                "in_dataset",
                "components"
        ]
},
    "copy_rows": {
        "name": "copy_rows",
        "description": "Copies the rows of a table  to a different table.",
        "parameters": {
                "in_rows": {
                        "type": "string",
                        "description": "The input rows to be copied to a new table."
                },
                "out_table": {
                        "type": "string",
                        "description": "The table that will be created and to which rows from the input will be copied. If the output table is in a folder, include an extension such as .csv, .txt, or .dbf to make the table the specified for..."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The default storage parameters for an enterprise geodatabase.",
                        "default": None
                }
        },
        "required": [
                "in_rows",
                "out_table"
        ]
},
    "create_table": {
        "name": "create_table",
        "description": "Creates a geodatabase table or a dBASE table.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The workspace where the output table will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the table that will be created."
                },
                "template": {
                        "type": "string",
                        "description": "One or more datasets from which the attribute schema will be used to define the output table. Fields in the template datasets will be added to the output table.",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The configuration keyword that determines the storage parameters of the table in an enterprise geodatabase.",
                        "default": None
                },
                "out_alias": {
                        "type": "string",
                        "description": "The alternate name of the \r\noutput table that will be created.",
                        "default": None
                },
                "oid_type": {
                        "type": "string",
                        "description": "Specifies whether the output Object ID field will be 32 bit or 64 bit.SAME_AS_TEMPLATE\u2014The output Object ID field type (32 bit or 64 bit) will be the same as the Object ID field of the first template ..."
                }
        },
        "required": [
                "out_path",
                "out_name",
                "oid_type"
        ]
},
    "create_unregistered_table": {
        "name": "create_unregistered_table",
        "description": "Creates an empty table in an enterprise database, enterprise geodatabase, GeoPackage, or SQLite database. The table is not registered with the geodatabase.",
        "parameters": {
                "out_path": {
                        "type": "string",
                        "description": "The enterprise database or enterprise geodatabase in which the table will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the table that will be created."
                },
                "template": {
                        "type": "string",
                        "description": "An existing dataset or list of datasets with fields and attribute schema that will be used to define the fields in the output table.",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Specifies the default storage parameters (configurations) for geodatabases in a relational database management system (RDBMS). This setting is applicable only when using enterprise geodatabase tables....",
                        "default": None
                }
        },
        "required": [
                "out_path",
                "out_name"
        ]
},
    "delete_rows": {
        "name": "delete_rows",
        "description": "Deletes all or the selected subset of rows from the input. The deletion of all rows or a subset of rows depends on the following:If the input is a feature class or table, all rows will be deleted.\r\nIf the input is a layer or table view with no selection, all rows\r\nwill be deleted.\r\nIf the input is a layer or table view with a selection, only the\r\nselected rows will be deleted.",
        "parameters": {
                "in_rows": {
                        "type": "string",
                        "description": "The feature class, layer, table, or table view whose rows will be deleted."
                }
        },
        "required": [
                "in_rows"
        ]
},
    "get_count": {
        "name": "get_count",
        "description": "Returns the total number of rows for a table.",
        "parameters": {
                "in_rows": {
                        "type": "string",
                        "description": "The input table view or raster layer. If a selection is defined on the input, the count of the selected rows will be returned."
                }
        },
        "required": [
                "in_rows"
        ]
},
    "pivot_table": {
        "name": "pivot_table",
        "description": "Creates a table from the input table by reducing redundancy  in records and flattening one-to-many relationships.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the records that will be pivoted."
                },
                "fields": {
                        "type": "string",
                        "description": "The fields that define the records that will be included in the output table."
                },
                "pivot_field": {
                        "type": "string",
                        "description": "The field whose record values will be used to generate the field names in the output table."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field whose values will populate the pivoted fields in the output table."
                },
                "out_table": {
                        "type": "string",
                        "description": "The table that will be created containing the pivoted records."
                }
        },
        "required": [
                "in_table",
                "fields",
                "pivot_field",
                "value_field",
                "out_table"
        ]
},
    "truncate_table": {
        "name": "truncate_table",
        "description": "Removes all rows from a database table or feature class using truncate procedures in the database.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input database table or feature class that will be truncated."
                }
        },
        "required": [
                "in_table"
        ]
},
    "export_tile_cache": {
        "name": "export_tile_cache",
        "description": "Exports tiles from an existing tile cache to a new tile cache or a tile package. The tiles can be either independently imported into other caches or accessed from ArcGIS Pro or mobile devices.",
        "parameters": {
                "in_cache_source": {
                        "type": "string",
                        "description": "An existing tile cache to be exported."
                },
                "in_target_cache_folder": {
                        "type": "string",
                        "description": "The output folder into which the tile cache or tile package will be exported."
                },
                "in_target_cache_name": {
                        "type": "string",
                        "description": "The name of the exported tile cache or tile package."
                },
                "export_cache_type": {
                        "type": "string",
                        "description": "Specifies whether the cache will be exported as a tile cache or a tile package. Tile packages are suitable\r\nfor ArcGIS Runtime and ArcGIS Mobile deployments.\r\nTILE_CACHE\u2014The cache will be exported as ...",
                        "default": None
                },
                "storage_format_type": {
                        "type": "string",
                        "description": "Determines the storage format of tiles.COMPACT\u2014Group tiles into large files called bundles. This storage format is more efficient in terms of storage and mobility. COMPACT_V2\u2014 Tiles are grouped in bun...",
                        "default": None
                },
                "scalesscale": {
                        "type": "string",
                        "description": "A list of scale levels at which tiles will be exported.",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "An area of interest that spatially constrains where tiles will be exported from the cache.The area of interest can be a feature class or a feature that you draw on the map.This parameter is useful if ...",
                        "default": None
                }
        },
        "required": [
                "in_cache_source",
                "in_target_cache_folder",
                "in_target_cache_name"
        ]
},
    "generate_tile_cache_tiling_scheme": {
        "name": "generate_tile_cache_tiling_scheme",
        "description": "Creates a tiling scheme file based on the information from the source dataset. The tiling scheme file will then be used in the Manage Tile Cache tool when creating cache tiles. This tool can be used to edit the properties of an existing tiling scheme, such as tile format, storage format, tile size, and so on. In addition, you can also use it to add new scale levels to an existing tiling scheme.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The source to be used to generate the tiling scheme. It can be a raster dataset,  a mosaic dataset, or a map."
                },
                "out_tiling_scheme": {
                        "type": "string",
                        "description": "The path and file name for the output tiling scheme to be created."
                },
                "tiling_scheme_generation_method": {
                        "type": "string",
                        "description": "Choose to use a new or predefined tiling scheme. You can define a new tiling scheme with this tool or browse to a predefined tiling scheme file (.xml).NEW\u2014Define a new tiling scheme using other parame..."
                },
                "number_of_scales": {
                        "type": "string",
                        "description": "The number of scale levels to be created in the tiling scheme."
                },
                "predefined_tiling_scheme": {
                        "type": "string",
                        "description": "Path to a predefined tiling scheme file (usually named conf.xml). This parameter is enabled only when the Predefined option is chosen as the tiling scheme generation method.",
                        "default": None
                },
                "scalesscale": {
                        "type": "string",
                        "description": "Scale levels to be included in the tiling scheme. By default, these are not represented as fractions. Instead, use 500 to represent a scale of 1:500, and so on. The value entered in the Number of Scal...",
                        "default": None
                },
                "scales_type": {
                        "type": "string",
                        "description": "Determines the units of the scales parameter.CELL_SIZE\u2014Indicates the values of the scales parameter are pixel sizes. This is the default.SCALE\u2014Indicates the values of the scales parameter are scale le...",
                        "default": None
                },
                "tile_origin": {
                        "type": "string",
                        "description": "The origin (upper left corner) of the tiling scheme in the coordinates of the spatial reference of the source dataset. The extent of the source dataset must be within (but does not need to coincide) t...",
                        "default": None
                },
                "dpi": {
                        "type": "string",
                        "description": "The dots per inch of the intended output device. If a DPI is chosen that does not match the resolution of the output device, typically a display monitor, the scale of the tile will appear incorrect. T...",
                        "default": None
                },
                "tile_size": {
                        "type": "string",
                        "description": "The width and height of the cache tiles in pixels. The default is 256 by 256.For the best balance between performance and manageability, avoid deviating from widths of 256 or 512.128 x 128\u2014Tile width ...",
                        "default": None
                },
                "tile_format": {
                        "type": "string",
                        "description": "The file format for the tiles in the cache.  PNG\u2014Creates PNG format with varying bit\r\ndepths. The bit depths are optimized according to the color\r\nvariation and transparency values in each tile.PNG8\u2014A...",
                        "default": None
                },
                "tile_compression_quality": {
                        "type": "string",
                        "description": "Enter a value\r\nbetween 1 and 100 for the JPEG or Mixed compression quality. The default value is 75.Compression is\r\nsupported only for Mixed and JPEG format. Choosing a higher value will result in hig...",
                        "default": None
                },
                "storage_format": {
                        "type": "string",
                        "description": "Determines the storage format of tiles. COMPACT\u2014Group tiles into large files called bundles. This storage format is more efficient in terms of storage and mobility. This is the default.EXPLODED\u2014Each t...",
                        "default": None
                },
                "lerc_error": {
                        "type": "string",
                        "description": "Set the maximum tolerance in pixel values when compressing with LERC.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_tiling_scheme",
                "tiling_scheme_generation_method",
                "number_of_scales"
        ]
},
    "import_tile_cache": {
        "name": "import_tile_cache",
        "description": "Imports tiles from an existing tile cache or a tile package. The target cache must have the same tiling scheme, spatial reference, and  storage format as the source tile cache.",
        "parameters": {
                "in_cache_target": {
                        "type": "string",
                        "description": "An existing tile cache  to which the tiles will be imported."
                },
                "in_cache_source": {
                        "type": "string",
                        "description": "An existing tile cache or a tile package from which the tiles are imported."
                },
                "scales": {
                        "type": "string",
                        "description": "A list of scale levels at which tiles will be imported.",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "An area of interest will spatially constrain where tiles are imported into the cache.This parameter is useful if you want to import tiles for irregularly shaped areas.",
                        "default": None
                },
                "overwrite": {
                        "type": "string",
                        "description": "Determines whether the images in the destination cache will be merged with the tiles from the originating cache or overwritten by them.MERGE\u2014When the tiles are imported, transparent pixels in the orig...",
                        "default": None
                }
        },
        "required": [
                "in_cache_target",
                "in_cache_source"
        ]
},
    "manage_tile_cache": {
        "name": "manage_tile_cache",
        "description": "Creates a tile cache or updates tiles in an existing tile cache. You can use this tool to create tiles, replace missing tiles, overwrite outdated tiles, and delete tiles.",
        "parameters": {
                "in_cache_location": {
                        "type": "string",
                        "description": "The folder in which the cache dataset will be created, the raster layer, or the path to an existing tile cache."
                },
                "manage_mode": {
                        "type": "string",
                        "description": "Specifies the mode that will be used to manage the cache. RECREATE_ALL_TILES\u2014Existing tiles will be replaced and new tiles will be added if the\r\nextent has changed or if layers have been added to a mu..."
                },
                "in_cache_name": {
                        "type": "string",
                        "description": "The name of the cache dataset that will be created in\r\n  the cache location.",
                        "default": None
                },
                "in_datasource": {
                        "type": "string",
                        "description": "A raster dataset, mosaic dataset, or map file.\r\nThis parameter is not required when the manage_mode parameter is set to DELETE_TILES.A map file (.mapx) cannot contain a map service or image service.",
                        "default": None
                },
                "tiling_scheme": {
                        "type": "string",
                        "description": "Specifies the tiling scheme that will be used.ARCGISONLINE_SCHEME\u2014The default ArcGIS Online tiling scheme will be used.IMPORT_SCHEME\u2014An existing tiling scheme will be imported and used.ARCGISONLINE_EL...",
                        "default": None
                },
                "import_tiling_scheme": {
                        "type": "string",
                        "description": "The path to an existing scheme file (.xml)  or to a tiling scheme imported from an existing image service or map service.",
                        "default": None
                },
                "scalesscale": {
                        "type": "string",
                        "description": "The scale levels at which tiles will be created or deleted , depending on the value of the manage_mode parameter. The pixel size is based on the spatial reference of the tiling scheme.By default, only...",
                        "default": None
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "An area of interest that will be used to constrain where tiles will be created or deleted.It can be a feature class, or it can be a feature set that you\r\ninteractively define.This parameter is useful ...",
                        "default": None
                },
                "max_cell_size": {
                        "type": "string",
                        "description": "The value that defines the visibility of the data source for which the cache will be generated. By default, the value is empty.If the value is empty, the following apply:For levels of cache that lie w...",
                        "default": None
                },
                "min_cached_scale": {
                        "type": "string",
                        "description": "The minimum scale at which tiles will be created.\r\nThis value does not need to be the smallest scale in the tiling scheme. The minimum cache scale will determine which scales are used when generating ...",
                        "default": None
                },
                "max_cached_scale": {
                        "type": "string",
                        "description": "The maximum scale at which tiles will be created. This\r\nvalue does not need to be the largest scale in the tiling scheme. The maximum cache scale will determine which scales are used when generating c...",
                        "default": None
                },
                "ready_to_serve_format": {
                        "type": "string",
                        "description": "Specifies whether the cache content will be generated using the open tile package specification and also specifies the file format of the cache schema.READY_TO_SERVE_FORMAT\u2014The cache content will be g...",
                        "default": None
                }
        },
        "required": [
                "in_cache_location",
                "manage_mode"
        ]
},
    "add_feature_class_to_topology": {
        "name": "add_feature_class_to_topology",
        "description": "Adds a feature class to a topology.",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The topology to which the feature class will be added."
                },
                "in_featureclass": {
                        "type": "string",
                        "description": "The feature class that will be added to the topology. The feature class must be in the same feature dataset as the topology."
                },
                "xy_rank": {
                        "type": "string",
                        "description": "The relative degree of positional accuracy associated with vertices of features in the feature class versus those in other feature classes in the topology.  The feature class with the highest accuracy..."
                },
                "z_rank": {
                        "type": "string",
                        "description": "Feature classes that are z-aware have elevation values embedded in their geometry for each vertex. By setting a z rank, you can influence how vertices with accurate z-values are snapped or clustered w..."
                }
        },
        "required": [
                "in_topology",
                "in_featureclass",
                "xy_rank",
                "z_rank"
        ]
},
    "add_rule_to_topology": {
        "name": "add_rule_to_topology",
        "description": "Adds a rule to a topology. The rules you choose to add depend on the spatial relationships that you wish to monitor for the feature classes that participate in the topology. For a complete list and description of the available topology rules, see geodatabase topology rules and topology error fixes for points, lines, or polygons.",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The topology to which the new rule will be added."
                },
                "rule_type": {
                        "type": "string",
                        "description": "Specifies the topology rule that will be added.Must Not Have Gaps (Area)\u2014There must be no voids within a single polygon or between adjacent polygons. All polygons must form a continuous surface. An er..."
                },
                "in_featureclass": {
                        "type": "string",
                        "description": "The input or origin feature class."
                },
                "subtype": {
                        "type": "string",
                        "description": "The subtype for the input or origin  feature class.  Provide the subtype name (not the code). If subtypes do not exist on the input feature class, or you want the rule to be applied to all subtypes in...",
                        "default": None
                },
                "in_featureclass2": {
                        "type": "string",
                        "description": "The destination feature class for the topology rule.",
                        "default": None
                },
                "subtype2": {
                        "type": "string",
                        "description": "The subtype for the destination feature class.  Provide the subtype name (not the code). If subtypes do not exist on the origin feature class, or you want the rule to be applied to all subtypes in the...",
                        "default": None
                }
        },
        "required": [
                "in_topology",
                "rule_type",
                "in_featureclass"
        ]
},
    "create_topology": {
        "name": "create_topology",
        "description": "Creates a topology. The topology will not contain any feature classes or rules. Use the Add Feature Class To Topology and the Add Rule To Topology tools to add feature classes and rules to the topology.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The feature dataset in which the  topology will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the topology to be created.  This name must be unique across the entire geodatabase."
                },
                "in_cluster_tolerance": {
                        "type": "string",
                        "description": "The cluster tolerance to be set on the topology.  The larger the value, the more likely vertices will be to cluster together.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_name"
        ]
},
    "export_topology_errors": {
        "name": "export_topology_errors",
        "description": "Exports the errors and exceptions from a geodatabase topology to the target geodatabase.  All information associated with the errors and exceptions, such as the features referenced by the error or exception, is exported. Once the errors and exceptions are exported, the feature classes can be accessed using any license level of ArcGIS.  The feature classes can be used with the Select Layer By Location tool and can be shared with other users who do not have access to the topology.",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The topology from which the errors will be exported."
                },
                "out_path": {
                        "type": "string",
                        "description": "The output workspace in which the feature classes\r\nwill be created."
                },
                "out_basename": {
                        "type": "string",
                        "description": "The name to prefix to each output feature class.  This allows you to specify unique output names when running multiple exports to the same workspace.  The default is the topology name."
                }
        },
        "required": [
                "in_topology",
                "out_path",
                "out_basename"
        ]
},
    "select_layer_by_location": {
        "name": "select_layer_by_location",
        "description": "Selects features  based on a spatial relationship to features in another dataset or the same dataset. Each feature in the Input Features parameter is evaluated using the features in the  Selecting Features parameter. If the specified Relationship parameter value is met, the input feature is selected. Learn more about Select By Location including image examples of relationships",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The features that will be evaluated using the select_features parameter values.  The selection will be applied to these features."
                },
                "overlap_type": {
                        "type": "string",
                        "description": "Specifies the spatial relationship that will be evaluated.INTERSECT\u2014The features in the input layer will be selected if they intersect a selecting feature. This is the default. INTERSECT_3D\u2014The featur...",
                        "default": None
                },
                "select_features": {
                        "type": "string",
                        "description": "The features in the Input Features parameter will be selected based on their relationship to the features from this layer or feature class.",
                        "default": None
                },
                "search_distance": {
                        "type": "string",
                        "description": "The distance that will be searched. This parameter is only valid if the overlap_type  parameter is set to INTERSECT, INTERSECT_3D, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_3D, WITHIN_A_DISTANCE_GEODESIC, ...",
                        "default": None
                },
                "selection_type": {
                        "type": "string",
                        "description": "Specifies how the selection will be applied to the input and how it will be combined with an existing selection.  This tool does not include an option to clear an existing selection; use the  Select L...",
                        "default": None
                },
                "invert_spatial_relationship": {
                        "type": "string",
                        "description": "Specifies whether the spatial relationship evaluation result or the opposite result will be used.  For example, this parameter can be used to get a list of features that do not intersect or are not wi...",
                        "default": None
                }
        },
        "required": [
                "in_layer"
        ]
},
    "remove_feature_class_from_topology": {
        "name": "remove_feature_class_from_topology",
        "description": "Removes a feature class from a topology.",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The topology from which to remove the feature class."
                },
                "in_featureclass": {
                        "type": "string",
                        "description": "The feature class to remove from the topology."
                }
        },
        "required": [
                "in_topology",
                "in_featureclass"
        ]
},
    "remove_rule_from_topology": {
        "name": "remove_rule_from_topology",
        "description": "Removes a rule from a topology.",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The topology from which to remove a rule."
                },
                "in_rule": {
                        "type": "string",
                        "description": "The topology rule to remove from the topology."
                }
        },
        "required": [
                "in_topology",
                "in_rule"
        ]
},
    "set_cluster_tolerance": {
        "name": "set_cluster_tolerance",
        "description": "Sets the cluster tolerance of a topology.",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The topology for which you want to change the cluster tolerance."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The value to be set as the cluster tolerance property of the selected topology. If you enter a value of zero, the default or minimum cluster tolerance will be applied to the topology."
                }
        },
        "required": [
                "in_topology",
                "cluster_tolerance"
        ]
},
    "validate_topology": {
        "name": "validate_topology",
        "description": "Validates a geodatabase topology. This tool performs the following operations:Cracking and clustering of feature vertices to find features that share geometry (have common coordinates)Inserting common coordinate vertices into features that share geometryRunning a set of integrity checks to identify any violations of the rules that have been defined for the topology",
        "parameters": {
                "in_topology": {
                        "type": "string",
                        "description": "The geodatabase topology that will be validated."
                },
                "visible_extent": {
                        "type": "string",
                        "description": "Specifies whether the current visible extent of the map or the full extent of the topology will be validated. Visible_Extent\u2014 The current visible extent of the map will be validated.Full_Extent\u2014The fu...",
                        "default": None
                }
        },
        "required": [
                "in_topology"
        ]
},
    "add_data_to_trajectory_dataset": {
        "name": "add_data_to_trajectory_dataset",
        "description": "Adds trajectory data to an existing  trajectory dataset.",
        "parameters": {
                "in_trajectory_dataset": {
                        "type": "string",
                        "description": "The trajectory dataset to which  the data will be added."
                },
                "trajectory_type": {
                        "type": "string",
                        "description": "Specifies the data type that will be added.Cryosat-2\u2014Cryosat-2 data will be added.ICESat-2\u2014ICESat-2 data will be added.Sentinel-3 SRAL\u2014Sentinel-3 SRAL data will be added.Sentinel-6\u2014Sentinel-6 data wil..."
                },
                "input_path": {
                        "type": "string",
                        "description": "The input files or folder. The inputs can be netCDF or HDF (.nc or .hdf files)."
                },
                "filter": {
                        "type": "string",
                        "description": "The filter for the input data. The default will be determined by the trajectory_type parameter value. Custom filter criteria can also be provided. For example,  a value of STD_ will filter files that ...",
                        "default": None
                },
                "sub_folder": {
                        "type": "string",
                        "description": "Specifies whether data in the input_path subfolders will be searched and added.SUBFOLDERS\u2014All subfolders will be searched and the data added. This is the default.NO_SUBFOLDERS\u2014Only the top-level folde...",
                        "default": None
                },
                "aux_inputs": {
                        "type": "string",
                        "description": "The properties that are determined by the trajectory_type parameter value.  Supported property names are ProductFilter, Frequency, PredefinedVariables, and Variables.  For a list of supported values a...",
                        "default": None
                }
        },
        "required": [
                "in_trajectory_dataset",
                "trajectory_type",
                "input_path"
        ]
},
    "create_trajectory_dataset": {
        "name": "create_trajectory_dataset",
        "description": "Creates an empty trajectory dataset in a geodatabase.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The geodatabase where the trajectory dataset will be stored."
                },
                "in_dataset_name": {
                        "type": "string",
                        "description": "The name of the trajectory dataset that will be created."
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The spatial reference of the trajectory dataset that will be created."
                }
        },
        "required": [
                "in_workspace",
                "in_dataset_name",
                "coordinate_system"
        ]
},
    "repair_trajectory_dataset_paths": {
        "name": "repair_trajectory_dataset_paths",
        "description": "Repairs paths to source data for a trajectory dataset.",
        "parameters": {
                "in_trajectory_dataset": {
                        "type": "string",
                        "description": "The input trajectory dataset."
                },
                "paths_list": {
                        "type": "string",
                        "description": "A  list of paths to remap."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will limit the repairs to selected items in the trajectory dataset.",
                        "default": None
                }
        },
        "required": [
                "in_trajectory_dataset",
                "paths_list"
        ]
},
    "add_field_conflict_filter": {
        "name": "add_field_conflict_filter",
        "description": "Adds a field conflict filter for a given field in a geodatabase table or feature class. Field conflict filters can be applied to versioned tables or feature classes to prevent conflicts from being identified when the same attribute is updated in the parent and child versions. Field conflict filters only apply for reconciles in which conflicts are defined by attribute.",
        "parameters": {
                "table": {
                        "type": "string",
                        "description": "Table or feature class\r\ncontaining the field or fields to which conflict filters will be applied."
                },
                "fields": {
                        "type": "string",
                        "description": "Field or list of fields that will have conflict filters applied."
                }
        },
        "required": [
                "table",
                "fields"
        ]
},
    "alter_version": {
        "name": "alter_version",
        "description": "Alters the properties of a geodatabase version.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The database connection file to the enterprise, workgroup, or desktop geodatabase where the version to be altered is located. The default is to use the workspace defined in the Current Workspace envir..."
                },
                "in_version": {
                        "type": "string",
                        "description": "The name of the version to be altered. If altering a branch version from a database connection connected as the geodatabase administrator, the version name must also include the service name, for exam..."
                },
                "name": {
                        "type": "string",
                        "description": "The new name of the version.",
                        "default": None
                },
                "description": {
                        "type": "string",
                        "description": "The new description of the version.",
                        "default": None
                },
                "access": {
                        "type": "string",
                        "description": "Specifies the access permission for the version. If no value is specified, the access permission will not be updated.PRIVATE\u2014Only the owner can view the version and modify available feature classes.PU...",
                        "default": None
                },
                "target_owner": {
                        "type": "string",
                        "description": "The name of the portal user to which the version ownership will be transferred. Ensure that the target owner user exists; the tool does not check the validity of the owner name specified. This paramet...",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "in_version"
        ]
},
    "change_version": {
        "name": "change_version",
        "description": "Modifies the workspace of a  layer or table view to connect to the specified version.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The layer or table view that will connect to the specified version.           Note:The sublayers of a topology layer, parcel layer, utility network layer, or trace network layer are not valid inputs."
                },
                "version_type": {
                        "type": "string",
                        "description": "Specifies the type of version to which the input feature layer will connect.            TRANSACTIONAL\u2014Connect to a defined state of the database (traditional version). HISTORICAL\u2014Connect to a version ..."
                },
                "version_name": {
                        "type": "string",
                        "description": "The name of the version to which the input feature layer will connect. This parameter is optional if you're using a historical version.",
                        "default": None
                },
                "date": {
                        "type": "string",
                        "description": "The date of the historical version to which the input feature layer will connect.",
                        "default": None
                },
                "include_participating": {
                        "type": "string",
                        "description": "Specifies whether the workspace of participating classes will also change.The parameter is only applicable when the input layer is a topology layer, parcel layer, utility network layer, or trace netwo...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "version_type"
        ]
},
    "create_version": {
        "name": "create_version",
        "description": "Creates a new version in a specified geodatabase or feature service.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The enterprise geodatabase that contains the parent version and will contain the new version.For branch versioning, use a feature service URL (for example, https://mysite.mydomain/server/rest/services..."
                },
                "parent_version": {
                        "type": "string",
                        "description": "The geodatabase, or version of a geodatabase, on which the new version will be based."
                },
                "version_name": {
                        "type": "string",
                        "description": "The name of the version that will be created."
                },
                "access_permission": {
                        "type": "string",
                        "description": "Specifies the permission access level for the version to protect it from being edited or viewed by users other than the owner.PRIVATE\u2014Only the owner or the geodatabase administrator can view and modif...",
                        "default": None
                },
                "version_description": {
                        "type": "string",
                        "description": "The description of the version that will be created. The description cannot exceed 64 characters.",
                        "default": None
                }
        },
        "required": [
                "in_workspace",
                "parent_version",
                "version_name"
        ]
},
    "delete_version": {
        "name": "delete_version",
        "description": "Deletes the specified version from the input enterprise geodatabase.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The database connection file to the enterprise geodatabase containing the version to be deleted.For branch versioning, use a feature service URL (that is, https://mysite.mydomain/server/rest/services/..."
                },
                "version_name": {
                        "type": "string",
                        "description": "The name of the version to be deleted.For branch versioning, if the input workspace is a database connection file, the name of the branch version to delete should be fully qualified  (for example, ser..."
                }
        },
        "required": [
                "in_workspace",
                "version_name"
        ]
},
    "prune_branch_history": {
        "name": "prune_branch_history",
        "description": "Removes retired archive records from branch-versioned datasets. Learn more about prune branch history",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The feature class, feature dataset, or table that will be pruned."
                },
                "out_log": {
                        "type": "string",
                        "description": "A log file that reports the feature classes and tables that were pruned or will be pruned. The output file will also list the replicas and  versions that prevented using the requested prune-before dat..."
                },
                "report_only": {
                        "type": "string",
                        "description": "Specifies whether the eligible archive records will be reported or pruned.REPORT_ONLY\u2014The eligible archive records  will be reported to the log file; they will not be pruned. This is the default.PRUNE...",
                        "default": None
                },
                "system_tables_only": {
                        "type": "string",
                        "description": "Specifies whether only the  eligible internal tables will be reported or pruned. \r\nSYSTEM_ONLY\u2014Only the eligible internal  tables of the extension datasets will be pruned or reported to the log file.A..."
                },
                "prune_before_date": {
                        "type": "string",
                        "description": "Archive records that are older than the specified date and time will be pruned. The date and time must be in UTC. If no date is provided, the oldest referenced moment in the database will be used.",
                        "default": None
                }
        },
        "required": [
                "in_dataset",
                "out_log",
                "system_tables_only"
        ]
},
    "reconcile_versions": {
        "name": "reconcile_versions",
        "description": "Reconciles a version or multiple versions with a target version. Learn more about how to reconcile and post versions",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The enterprise geodatabase that contains the versions to be reconciled. The default is to use the geoprocessing Current Workspace environment.For branch versioning, this will be the feature service UR..."
                },
                "reconcile_mode": {
                        "type": "string",
                        "description": "Specifies the versions that will be reconciled when the tool is run.\r\nIf the input is a branch workspace, the only valid option for this parameter is to reconcile all versions.ALL_VERSIONS\u2014Edit versio..."
                },
                "target_version": {
                        "type": "string",
                        "description": "The name of any version in the direct ancestry of the edit version, such as the parent version or the default version.\r\n It typically contains edits from other versions that you want included in the e...",
                        "default": None
                },
                "edit_versions": {
                        "type": "string",
                        "description": "The name of the edit version or versions to be reconciled with the selected target version.\r\nThis can be an individual version name or a list of version names.",
                        "default": None
                },
                "acquire_locks": {
                        "type": "string",
                        "description": "Specifies whether feature locks will be acquired.If the input is a branch workspace, locks are not acquired during the reconcile process.LOCK_ACQUIRED\u2014Locks will be acquired during the reconcile proce...",
                        "default": None
                },
                "abort_if_conflicts": {
                        "type": "string",
                        "description": "Specifies whether the reconcile process will end if conflicts are found between the target version and the edit version during the reconcile process.NO_ABORT\u2014The reconcile will not end if conflicts ar...",
                        "default": None
                },
                "conflict_definition": {
                        "type": "string",
                        "description": "Specifies whether the conditions required for a conflict to occur will be defined by object (row) or by attribute (column).BY_OBJECT\u2014Conflicts will be defined by object. Any changes to the same row or...",
                        "default": None
                },
                "conflict_resolution": {
                        "type": "string",
                        "description": "Specifies the resolution that will be used if a conflict is detected.If the input is a branch workspace, the default is to favor the edit version.FAVOR_TARGET_VERSION\u2014All conflicts will be resolved in...",
                        "default": None
                },
                "out_log": {
                        "type": "string",
                        "description": "The name and location where the log file will be written. The log file is an ASCII file containing the contents of the geoprocessing messages.",
                        "default": None
                },
                "proceed_if_conflicts_not_reviewed": {
                        "type": "string",
                        "description": "Specifies whether the reconcile will proceed if existing unreviewed conflicts are detected before the reconcile process starts. If you proceed, existing conflicts from previous sessions will be lost w...",
                        "default": None
                },
                "reconcile_checkout_versions": {
                        "type": "string",
                        "description": "Specifies whether the reconcile process will include checkout replica versions. If you are creating a checkout replica as part of a geodatabase replication workflow, an associated version is created i...",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "reconcile_mode"
        ]
},
    "register_as_versioned": {
        "name": "register_as_versioned",
        "description": "Registers an enterprise geodatabase dataset as versioned. Learn more about how to register data as branch versioned and traditional versioned.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The dataset to be registered as versioned."
                },
                "edit_to_base": {
                        "type": "string",
                        "description": "Specifies whether edits made to the default version will be moved to the base tables. This parameter is not applicable for branch versioning.NO_EDITS_TO_BASE\u2014The dataset will not be versioned with the...",
                        "default": None
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "remove_field_conflict_filter": {
        "name": "remove_field_conflict_filter",
        "description": "Removes a field conflict filter for a given field in a geodatabase table or feature class. Field conflict filters can be applied to versioned tables or feature classes to prevent conflicts from being identified when the same attribute is updated in the parent and child versions. Field conflict filters only apply for reconciles in which conflicts are defined by attribute.",
        "parameters": {
                "table": {
                        "type": "string",
                        "description": "Table or feature class\r\ncontaining the field or fields to be removed as conflict filters."
                },
                "fields": {
                        "type": "string",
                        "description": "Field or list of fields to be removed as conflict filters."
                }
        },
        "required": [
                "table",
                "fields"
        ]
},
    "unregister_as_versioned": {
        "name": "unregister_as_versioned",
        "description": "Unregisters an enterprise geodatabase dataset as versioned.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The name of the dataset to be unregistered as versioned."
                },
                "keep_edit": {
                        "type": "string",
                        "description": "Specifies whether edits made to the versioned data will be maintained.KEEP_EDIT\u2014When there are outstanding edits that could be lost, the tool will fail. Outstanding edits include edits in the delta ta...",
                        "default": None
                },
                "compress_default": {
                        "type": "string",
                        "description": "Specifies whether edits will be compressed and unused data will be removed. This option is ignored if the keep_edit parameter is set to KEEP_EDIT.This parameter is only applicable for traditional vers...",
                        "default": None
                }
        },
        "required": [
                "in_dataset"
        ]
},
    "clear_workspace_cache": {
        "name": "clear_workspace_cache",
        "description": "Clears information about a workspace that has been cached in memory.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The geodatabase, .sde connection file, or folder path representing the workspace that will be removed from the workspace cache. If no value is specified, all contents of the workspace cache will be cl...",
                        "default": None
                }
        },
        "required": []
},
    "convert_schema_report": {
        "name": "convert_schema_report",
        "description": "Converts a JSON or XLSX formatted schema report to another schema report format or to an XML workspace document that can be used to create a geodatabase.",
        "parameters": {
                "schema_report": {
                        "type": "string",
                        "description": "The JSON or XLSX schema report that will be converted."
                },
                "out_location": {
                        "type": "string",
                        "description": "The folder where the output files will be placed"
                },
                "name": {
                        "type": "string",
                        "description": "The name of the file outputs."
                },
                "formats": {
                        "type": "string",
                        "description": "Specifies the file types that will be included in the output folder.JSON\u2014The output folder will include a .json file.PDF\u2014The output folder will include a .pdf file.HTML\u2014The output folder will include ..."
                }
        },
        "required": [
                "schema_report",
                "out_location",
                "name",
                "formats"
        ]
},
    "create_cloud_storage_connection_file": {
        "name": "create_cloud_storage_connection_file",
        "description": "Creates a connection file for ArcGIS-supported cloud storage. This tool allows existing raster geoprocessing tools to write cloud raster format (CRF) datasets into the cloud storage bucket or read raster datasets (not limited to CRF) stored in the cloud storage as input. The tool also creates a cloud storage connection file that you can use to access Apache Parquet files for mapping.",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The folder path where the connection file (.acs) will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the cloud storage connection file."
                },
                "service_provider": {
                        "type": "string",
                        "description": "Specifies the cloud storage service provider that will be used.AZURE\u2014The service provider will be Microsoft Azure.AMAZON\u2014The service provider will be Amazon S3. This is currently the only provider sup..."
                },
                "bucket_name": {
                        "type": "string",
                        "description": "The name of the cloud storage container where the raster dataset or Parquet file is stored. If using this location for output for raster geoprocessing tools, this is the container where the output ras..."
                },
                "access_key_id": {
                        "type": "string",
                        "description": "The access key ID string for the specific cloud storage type.  It can also be the account name,  as is the case with Azure.",
                        "default": None
                },
                "secret_access_key": {
                        "type": "string",
                        "description": "The secret access key string to authenticate the connection to cloud storage.",
                        "default": None
                },
                "region": {
                        "type": "string",
                        "description": "The region string for the cloud storage. If provided, the value must use the format defined by the cloud storage choice. The default is the selected cloud provider's default account.",
                        "default": None
                },
                "end_point": {
                        "type": "string",
                        "description": "The service endpoint (URI) of the cloud storage, such as oss-us-west-1.aliyuncs.com. If no value is provided, the default endpoint for the selected cloud storage type will be used. The CNAME redirecte...",
                        "default": None
                },
                "folder": {
                        "type": "string",
                        "description": "The folder in the bucket_name parameter value where the raster dataset or Parquet file is stored. If using this location for output for raster geoprocessing tools, this is the folder where the output ...",
                        "default": None
                },
                "authentication": {
                        "type": "string",
                        "description": "The connection name of OAuth 2.0 authentication.",
                        "default": None
                }
        },
        "required": [
                "out_folder_path",
                "out_name",
                "service_provider",
                "bucket_name"
        ]
},
    "create_database_connection": {
        "name": "create_database_connection",
        "description": "Creates a file that ArcGIS uses to connect to a database, a cloud data warehouse, or an enterprise geodatabase.",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The folder path where the database connection file (.sde or .dbconn) will be stored."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the database connection file. The output file will have the .sde extension."
                },
                "database_platform": {
                        "type": "string",
                        "description": "Specifies the database management system platform to which the connection will be made. The following are valid options:BIGQUERY\u2014The connection will be made to Google BigQuery.DAMENG\u2014The connection wi..."
                },
                "instance": {
                        "type": "string",
                        "description": "The database server or instance to which the connection will be made.The value you specify for the database_platform parameter indicates the type of database or cloud data warehouse to which the conne...",
                        "default": None
                },
                "account_authentication": {
                        "type": "string",
                        "description": "Specifies the type of authentication that will be used.DATABASE_AUTH\u2014Database authentication will be used. An internal database username and a password will be used to connect to the database. You are...",
                        "default": None
                },
                "username": {
                        "type": "string",
                        "description": "The database username that will be used for database authentication.",
                        "default": None
                },
                "password": {
                        "type": "string",
                        "description": "The database user password that will be used for database authentication.",
                        "default": None
                },
                "save_user_pass": {
                        "type": "string",
                        "description": "Specifies whether the username and password will be saved.SAVE_USERNAME\u2014The username and password will be saved in the connection file. This is the default. If the connection file you are creating wil...",
                        "default": None
                },
                "database": {
                        "type": "string",
                        "description": "The name of the database to which the connection will be made. This parameter  applies to PostgreSQL,  Redshift, Snowflake, and SQL Server platforms.",
                        "default": None
                },
                "schema": {
                        "type": "string",
                        "description": "The user schema geodatabase to which the connection will be made. This parameter only applies to Oracle databases that contain at least one user\u2013schema geodatabase. The default value for this paramete...",
                        "default": None
                },
                "version_type": {
                        "type": "string",
                        "description": "Specifies the type of version to which the connection will be made.TRANSACTIONAL\u2014The connection will be made to a traditional transactional version.Note:This option does not apply to geodatabases in S...",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "The geodatabase transactional version or historical marker  to which the connection will be made. The default option uses the default transactional version.If you choose a branch version type, the con...",
                        "default": None
                },
                "date": {
                        "type": "string",
                        "description": "The value representing the date and time that will be used to connect to the database when working with archive-enabled data. Dates can be entered in the following formats: 6/9/2011 4:20:15 PM 6/9/201...",
                        "default": None
                },
                "auth_type": {
                        "type": "string",
                        "description": "Specifies the advanced authentication type that will be used when connecting to a cloud data warehouse, Microsoft Azure SQL Database,  Azure SQL Managed Instance, Elasticsearch, or OpenSearch.\r\nAZURE_...",
                        "default": None
                },
                "project_id": {
                        "type": "string",
                        "description": "The project ID for the Google BigQuery connection. Public data projects are not supported.",
                        "default": None
                },
                "default_dataset": {
                        "type": "string",
                        "description": "The default dataset for the Google BigQuery connection. Provide the dataset name only; the fully-qualified dataset name is not supported. The dataset name must contain 32 characters or fewer. Public d...",
                        "default": None
                },
                "refresh_token": {
                        "type": "string",
                        "description": "The refresh token value.This parameter is only applicable for Google BigQuery connections when the advanced authentication type is user authentication.",
                        "default": None
                },
                "key_file": {
                        "type": "string",
                        "description": "The key file  value.This parameter is only applicable for Google BigQuery connections when the advanced authentication type is server authentication.",
                        "default": None
                },
                "role": {
                        "type": "string",
                        "description": "The role value for a cloud data warehouse connection.This parameter is only applicable for connections to Snowflake.",
                        "default": None
                },
                "warehouse": {
                        "type": "string",
                        "description": "The warehouse value for the connection.This parameter is only applicable for connections to Snowflake.",
                        "default": None
                },
                "advanced_options": {
                        "type": "string",
                        "description": "The advanced options for the connection. This is optional connection information that is specific to the cloud data warehouse platform (Google BigQuery, Amazon Redshift, or Snowflake) to which you con...",
                        "default": None
                },
                "host_url": {
                        "type": "string",
                        "description": "The URL to connect to Elasticsearch or OpenSearch.This parameter is only applicable for connections to Elasticsearch or OpenSearch.",
                        "default": None
                }
        },
        "required": [
                "out_folder_path",
                "out_name",
                "database_platform"
        ]
},
    "create_database_connection_string": {
        "name": "create_database_connection_string",
        "description": "Creates a connection string that geoprocessing tools can use to connect to a database or an enterprise geodatabase.",
        "parameters": {
                "database_platform": {
                        "type": "string",
                        "description": "Specifies the database platform to which the connection will be made.SQL_SERVER\u2014Connect to Microsoft SQL Server or Microsoft Azure SQL Database.ORACLE\u2014Connect to Oracle.DB2\u2014Connect to IBM DB2 for Linu..."
                },
                "instance": {
                        "type": "string",
                        "description": "The database server or instance to which the connection will be made.This parameter value depends on the Database Platform parameter value chosen."
                },
                "account_authentication": {
                        "type": "string",
                        "description": "Specifies the type of authentication that will be used.DATABASE_AUTH\u2014Database authentication will be used. An internal database user name and password are used to connect to the database. You aren't r...",
                        "default": None
                },
                "username": {
                        "type": "string",
                        "description": "The database user name that will be used when using database authentication.",
                        "default": None
                },
                "password": {
                        "type": "string",
                        "description": "The database user password that will be used when using database authentication.",
                        "default": None
                },
                "database": {
                        "type": "string",
                        "description": "The name of the database to which you will connect. This parameter only applies to PostgreSQL and SQL Server platforms.",
                        "default": None
                },
                "object_name": {
                        "type": "string",
                        "description": "The name of the dataset or object in the database to which the connection string will point. This connection string can be used as a path to the specified dataset.",
                        "default": None
                },
                "data_type": {
                        "type": "string",
                        "description": "The type of dataset or object referred to in the dataset object name. If there are multiple objects with the same name in the database, you may need to specify the data type of the object for which yo...",
                        "default": None
                },
                "feature_dataset": {
                        "type": "string",
                        "description": "The name of the feature dataset containing the dataset or object for which you want to make a connection string. If the dataset is not in a feature dataset (for example, if it's at the root of the dat...",
                        "default": None
                },
                "schema": {
                        "type": "string",
                        "description": "The user schema geodatabase to which you will connect. This option only applies to Oracle databases that contain at least one user-schema geodatabase. The default value for this parameter is to use th...",
                        "default": None
                },
                "version_type": {
                        "type": "string",
                        "description": "Specifies the type of version to which you will connect. This parameter only applies when connecting to a geodatabase.TRANSACTIONAL\u2014Connect to a transactional version. If Transactional is selected, th...",
                        "default": None
                },
                "version": {
                        "type": "string",
                        "description": "The geodatabase transactional version or historical marker  to connect to. The default option uses the default transactional version.If you choose a branch version type, the connection is always to th...",
                        "default": None
                },
                "date": {
                        "type": "string",
                        "description": "The value representing the date and time that will be used to connect to the database when working with archive-enabled data. Dates can be entered in the following formats: 6/9/2011 4:20:15 PM 6/9/201...",
                        "default": None
                }
        },
        "required": [
                "database_platform",
                "instance"
        ]
},
    "create_feature_dataset": {
        "name": "create_feature_dataset",
        "description": "Creates a feature dataset in the output location: an existing enterprise,  file, or mobile geodatabase.",
        "parameters": {
                "out_dataset_path": {
                        "type": "string",
                        "description": "The enterprise, file, or mobile geodatabase where the output feature dataset will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the feature dataset to be created."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the output feature dataset. You can specify the spatial reference in the following ways: Enter the path to a .prj file, such as C:/workspace/watershed.prj. Reference a feature...",
                        "default": None
                }
        },
        "required": [
                "out_dataset_path",
                "out_name"
        ]
},
    "create_file_geodatabase": {
        "name": "create_file_geodatabase",
        "description": "Creates a file geodatabase in a folder.",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The folder where the file geodatabase will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the file geodatabase to be created."
                },
                "out_version": {
                        "type": "string",
                        "description": "Specifies the ArcGIS version for the new geodatabase.CURRENT\u2014A geodatabase compatible with the currently installed version of ArcGIS will be created. This is the default.10.0\u2014A geodatabase compatible ...",
                        "default": None
                }
        },
        "required": [
                "out_folder_path",
                "out_name"
        ]
},
    "create_folder": {
        "name": "create_folder",
        "description": "Creates a folder in the specified location.",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The disk location where the folder is created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The folder to be created."
                }
        },
        "required": [
                "out_folder_path",
                "out_name"
        ]
},
    "create_mobile_geodatabase": {
        "name": "create_mobile_geodatabase",
        "description": "Creates a mobile geodatabase. Learn more about creating and using mobile geodatabases",
        "parameters": {
                "out_folder_path": {
                        "type": "string",
                        "description": "The folder where the mobile geodatabase will be created."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the mobile geodatabase to be created."
                }
        },
        "required": [
                "out_folder_path",
                "out_name"
        ]
},
    "create_spatial_type": {
        "name": "create_spatial_type",
        "description": "Adds the ST_Geometry SQL type, subtypes, and functions to an Oracle or a PostgreSQL database. This allows you to use the ST_Geometry SQL type to store geometries in a database that does not contain a geodatabase. You can also use this tool to upgrade the existing ST_Geometry type, subtypes, and functions in an Oracle or a PostgreSQL database.",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The input_database is the database connection file (.sde) that connects to the Oracle or PostgreSQL database. You must connect as a database administrator user; in Oracle, you must connect as the sys ..."
                },
                "sde_user_password": {
                        "type": "string",
                        "description": "The password for the sde database user. If the sde user does not exist in the database, it will be created and will use the password you provide. The password policy of the underlying database will be..."
                },
                "tablespace_name": {
                        "type": "string",
                        "description": "The name of a tablespace that will be set as the default tablespace for the sde user in Oracle. If the tablespace name does not exist, it will be created in the Oracle default storage location. If a t...",
                        "default": None
                },
                "st_shape_library_path": {
                        "type": "string",
                        "description": "The location on the Oracle server where the st_shape library resides.",
                        "default": None
                }
        },
        "required": [
                "input_database",
                "sde_user_password"
        ]
},
    "create_sqlite_database": {
        "name": "create_sqlite_database",
        "description": "Creates a GeoPackage or an SQLite database that contains the ST_Geometry or SpatiaLite spatial type.",
        "parameters": {
                "out_database_name": {
                        "type": "string",
                        "description": "The location of the SQLite database or GeoPackage that will be created and the name of the file.\r\n The .sqlite  extension will be automatically assigned if the spatial_type parameter value is ST_GEOME..."
                },
                "spatial_type": {
                        "type": "string",
                        "description": "Specifies the spatial type that will be installed with the new SQLite database or the GeoPackage version that will be created.ST_GEOMETRY\u2014The Esri spatial storage type will be installed. This is the d...",
                        "default": None
                }
        },
        "required": [
                "out_database_name"
        ]
},
    "enable_editing_templates": {
        "name": "enable_editing_templates",
        "description": "Enables a file or mobile geodatabase to store editing templates.",
        "parameters": {
                "in_workspace": {
                        "type": "string",
                        "description": "The workspace containing the editing templates that will be enabled."
                }
        },
        "required": [
                "in_workspace"
        ]
},
    "export_xml_workspace_document": {
        "name": "export_xml_workspace_document",
        "description": "Creates a readable XML document of the geodatabase contents. The XML workspace document is useful for sharing geodatabase schemas or copying geodatabase schemas from one type to another.",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The input datasets that will be exported and represented in an XML workspace document. The input data can be a geodatabase, feature dataset, feature class, table, raster, or raster catalog. If there a..."
                },
                "out_file": {
                        "type": "string",
                        "description": "The XML workspace document file that will be created.\r\nThe output can be XML (with an .xml file extension) or compressed XML (with a .zip or .z file extension)."
                },
                "export_type": {
                        "type": "string",
                        "description": "Specifies whether the output XML workspace document will contain all of the data from the input (table and feature class records, including geometry) or only the schema.\r\nDATA\u2014The schema and the data ...",
                        "default": None
                },
                "storage_type": {
                        "type": "string",
                        "description": "Specifies how feature geometry will be stored when data is exported from a feature class.\r\nBINARY\u2014The geometry will be stored in a compressed base64 binary format. This binary format will produce a sm...",
                        "default": None
                },
                "export_metadata": {
                        "type": "string",
                        "description": "Specifies whether the metadata will be exported.METADATA\u2014If the input contains metadata, it will be exported. This is the default. NO_METADATA\u2014Metadata will not be exported.",
                        "default": None
                }
        },
        "required": [
                "in_data",
                "out_file"
        ]
},
    "generate_schema_report": {
        "name": "generate_schema_report",
        "description": "Generates an Excel, JSON, PDF, or HTML representation of the geodatabase schema. These formats are output to a target destination folder. Learn more about generating a schema report",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The workspace, feature dataset, feature layer, or table view that will be used to generate the schema report."
                },
                "out_location": {
                        "type": "string",
                        "description": "The folder where the report will be created."
                },
                "name": {
                        "type": "string",
                        "description": "The name of the file outputs."
                },
                "formats": {
                        "type": "string",
                        "description": "Specifies the file types that will be included in the output folder.JSON\u2014The output folder will include a .json file.PDF\u2014The output folder will include a .pdf file.HTML\u2014The output folder will include ..."
                }
        },
        "required": [
                "in_dataset",
                "out_location",
                "name",
                "formats"
        ]
},
    "import_xml_workspace_document": {
        "name": "import_xml_workspace_document",
        "description": "Imports the contents of an XML workspace document into an existing geodatabase.",
        "parameters": {
                "target_geodatabase": {
                        "type": "string",
                        "description": "An existing geodatabase where the contents of the XML workspace document will be imported."
                },
                "in_file": {
                        "type": "string",
                        "description": "The input XML workspace document file containing geodatabase contents to be imported. The file can be an .xml file or a compressed .zip or .z file containing the .xml file."
                },
                "import_type": {
                        "type": "string",
                        "description": "Specifies whether both data (feature class and table records, including geometry) and schema will be imported, or only the schema will be imported.\r\n DATA\u2014Data and schema will be imported. This is the...",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The geodatabase configuration keyword to be applied if the target_geodatabase parameter value is an enterprise or file geodatabase.",
                        "default": None
                }
        },
        "required": [
                "target_geodatabase",
                "in_file"
        ]
},
    "refresh_excel": {
        "name": "refresh_excel",
        "description": "Refreshes a Microsoft Excel file  in ArcGIS Pro.",
        "parameters": {
                "in_excel_file": {
                        "type": "string",
                        "description": "The Excel file that will be refreshed."
                }
        },
        "required": [
                "in_excel_file"
        ]
},
    "update_geodatabase_connection_properties_to_branch": {
        "name": "update_geodatabase_connection_properties_to_branch",
        "description": "Updates an enterprise geodatabase connection to work with branch versioning. Learn more about branch versioning",
        "parameters": {
                "input_database": {
                        "type": "string",
                        "description": "The input enterprise geodatabase connection to update."
                }
        },
        "required": [
                "input_database"
        ]
}
}
