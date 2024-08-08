# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "Esri.Mapping.Slots"
QML_IMPORT_MAJOR_VERSION = 1

from PySide6.QtCore import QObject, Property, Signal, Slot
from PySide6.QtQml import QmlElement

from arcgis.features import FeatureSet
from arcgis.geometry import Geometry
import json

from coremapping import MapViewModel


@QmlElement
class Geoprocessing(QObject):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._geometries = []

    @Slot(QObject)
    def createBuffer(self, map_viewmodel: MapViewModel):
        try:
            if (None is map_viewmodel):
                raise ValueError("The map view model must be initialized!")

            print(self._geometries)
            map_viewmodel.clearOperationalLayers()
        except Exception as ex:
            print(ex)

    @Slot(str)
    def sketchCompleted(self, geometry: str):
        try:
            geometry_dict = json.loads(geometry)
            sketch_geometry = Geometry(geometry_dict)
            self._geometries.append(sketch_geometry)
        except Exception as ex:
            print(ex)