# This Python file uses the following encoding: utf-8
import sys
import os
import json
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtNetwork import QSslSocket
from PySide6.QtCore import QCoreApplication

from utils import add_module_directories, initialize_arcgis


if __name__ == "__main__":
    # Extend the path containing native libraries
    add_module_directories()

    # Initializes the ArcGIS Core environment
    initialize_arcgis()

    application = QGuiApplication(sys.argv)
    name = "Map Viewer example"
    QCoreApplication.setApplicationName(name)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("supportsSsl", QSslSocket.supportsSsl())
    engine.addImportPath(os.path.join(Path(__file__).parent, "MapViewer"))
    engine.loadFromModule("UI", "Main")
    engine.quit.connect(QCoreApplication.quit)

    items = engine.rootObjects()
    if not items:
        sys.exit(-1)

    ex = application.exec()
    del engine
    sys.exit(ex)
