# This Python file uses the following encoding: utf-8
import sys
import os
import json
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtNetwork import QSslSocket
from PySide6.QtCore import QCoreApplication


# Since Python 3.8 add_dll_directory is necessary!
if not "maptoolkit_path" in os.environ:
    raise ValueError("'maptoolkit_path' is not defined in the current environment!")
for native_dir in os.environ["maptoolkit_path"].split(";"):
    os.add_dll_directory(native_dir)
    sys.path.append(native_dir)

from coremapping import initialize, MapViewModel


if __name__ == "__main__":

     # Validate if the arcgis_api_key environment variable exists
    if not "arcgis_api_key" in os.environ:
        raise ValueError("'arcgis_api_key' is not defined in the current environment!")
    
    # Initializes the ArcGIS Runtime core environment
    # Also authenticate against ArcGIS Location Platform using an API Key
    api_key = os.environ.get("arcgis_api_key")
    initialize(api_key)

    application = QGuiApplication(sys.argv)
    name = "Map Viewer example"
    QCoreApplication.setApplicationName(name)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("supportsSsl", QSslSocket.supportsSsl())
    engine.addImportPath(Path(__file__).parent)
    engine.loadFromModule("UI", "Main")
    engine.quit.connect(QCoreApplication.quit)

    items = engine.rootObjects()
    if not items:
        sys.exit(-1)


    ex = application.exec()
    del engine
    sys.exit(ex)
