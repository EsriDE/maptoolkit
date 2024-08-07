import os
from pathlib import Path
import sys

from utils import add_module_directories, initialize_arcgis, create_quick_app

#import arcpy


if __name__ == "__main__":
    # Extend the path containing native libraries
    add_module_directories()

    # Initializes the ArcGIS Core environment
    initialize_arcgis()

    # Create a quick app and engine
    app_folder = os.path.join(Path(__file__).parent, "GPResultViewer")
    application, engine = create_quick_app("Geoprocessing Sample", app_folder)

    ex = application.exec()
    del engine
    sys.exit(ex)