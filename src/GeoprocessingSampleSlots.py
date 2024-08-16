# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "Esri.Mapping.Slots"
QML_IMPORT_MAJOR_VERSION = 1

from PySide6.QtCore import QObject, Property, Signal, Slot
from PySide6.QtQml import QmlElement

from arcgis.features import FeatureSet
from arcgis.geometry import Geometry
from arcpyutils import construct_geodesic_buffer
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
            
            if len(self._geometries) < 1:
                print("No sketch geometries available!")
                return

            features = [{
                "geometry": geometry,
                "attributes": {}
                } for geometry in self._geometries
            ]
            featureset = FeatureSet(features)
            buffer_featureset = construct_geodesic_buffer(featureset, distance_km=20)
            map_viewmodel.clearGraphicOverlays()
            self._geometries = []

            renderer = {
                "label": "",
                "description": "",
                "type": "simple",
                "symbol": {
                    "type": "esriSFS",
                    "style": "esriSFSSolid",
                    "color": [0, 128, 0, 178],
                    "outline": {
                        "type": "esriSLS",
                        "style": "esriSLSSolid",
                        "color": [110, 110, 110, 255],
                        "width": 1
                    }
                }
            }
            buffer_geometries = []
            for feature in buffer_featureset.features:
                buffer_geometries.append(feature.geometry)

            buffer_geometries_json = json.dumps(buffer_geometries)
            renderer_json = json.dumps(renderer)
            map_viewmodel.addGeometries(buffer_geometries_json, renderer_json)
        except Exception as ex:
            print(ex)

    @Slot(str)
    def sketchCompleted(self, geometry: str):
        try:
            geometry_dict = json.loads(geometry)
            sketch_geometry = Geometry(geometry_dict)
            self._geometries.append(sketch_geometry)
            #print(sketch_geometry)
        except Exception as ex:
            print(ex)