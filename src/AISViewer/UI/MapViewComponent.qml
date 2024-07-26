import QtQuick
import QtQuick.Controls
import Esri.Mapping

Item {

    function loadGeoJsonFeatures(geoJsonFeatures) {
        model.addGeoJsonFeatures(geoJsonFeatures);
    }

    // The map view model
    property MapViewModel mapViewModel: model

    // Create MapQuickView here, and create its Map etc. in C++ code
    MapView {
        id: view
        anchors.fill: parent
        // set focus to enable keyboard navigation
        focus: true
    }

    // Declare the C++ instance which creates the map etc. and supply the view
    MapViewModel {
        id: model
        mapView: view
        basemapStyle: "OsmStandard"
    }
}