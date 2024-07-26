# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "Esri.Mapping.Slots"
QML_IMPORT_MAJOR_VERSION = 1

from PySide6.QtCore import QObject, Property, Signal, Slot
from PySide6.QtQml import QmlElement

from arcgisutils import read_csv_files_as_sdf
from coremapping import MapViewModel


@QmlElement
class LoadGeoJson(QObject):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    @Slot(str, QObject, result=str)
    def loadGeoJson(self, filepath: str, map_viewmodel: MapViewModel):
        try:
            if (None is map_viewmodel):
                raise ValueError("The map view model must be initialized!")

            ais_sdf = read_csv_files_as_sdf(filepath, x_column="LON", y_column="LAT", sr=4326, nrows=500)
            ais_fset = ais_sdf.spatial.to_featureset()
            map_viewmodel.addGeoJsonFeatures(ais_fset.to_geojson)
        except Exception as ex:
            print(ex)
        
