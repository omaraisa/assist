import sys
import json
import os
import traceback

# The 'spatial_functions.py' is now in the same directory as this script.
# No need to modify sys.path.

try:
    from spatial_functions import SpatialFunctions
except ImportError:
    # Backup: search for spatial_functions.py and load it dynamically
    import pathlib
    import importlib.util
    
    script_dir = pathlib.Path(__file__).parent
    
   

if __name__ == "__main__":
    main()
