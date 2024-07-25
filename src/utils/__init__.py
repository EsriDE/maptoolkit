import os
import sys


def add_module_directories():
    """
    Extends the path using the environment variable named 'maptoolkit_path'.
    Raises a ValueError if this environment variable does not exists!
    """
    # Since Python 3.8 add_dll_directory is necessary!
    if not "maptoolkit_path" in os.environ:
        raise ValueError("'maptoolkit_path' is not defined in the current environment!")
    for native_dir in os.environ["maptoolkit_path"].split(";"):
        os.add_dll_directory(native_dir)
        sys.path.append(native_dir)

def initialize_arcgis():
    """
    Initializes the ArcGIS core environment.
    Authenticates against ArcGIS Location Platform using the environment variable named 'arcgis_api_key'.
    Raises a ValueError if this environment variable does not exists!
    """
    # Validate if the arcgis_api_key environment variable exists
    if not "arcgis_api_key" in os.environ:
        raise ValueError("'arcgis_api_key' is not defined in the current environment!")
    
    # Initializes the ArcGIS Runtime core environment
    # Also authenticate against ArcGIS Location Platform using an API Key
    api_key = os.environ.get("arcgis_api_key")

    from coremapping import initialize
    initialize(api_key)