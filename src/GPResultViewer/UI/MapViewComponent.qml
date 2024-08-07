import QtQuick
import QtQuick.Controls
import Esri.Mapping

Item {

    function startSketching() {
        model.startSketching(MapViewModel.PolygonSketchMode);
        sketchingEnabled = true;
    }

    function stopSketching() {
        sketchingEnabled = false;
        model.stopSketching();
    }

    property bool sketchingEnabled: false

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
        onSketchCompleted: (geometry) => {
            console.log(geometry);

            // Start the next sketch
            if (sketchingEnabled) {
                model.startSketching(MapViewModel.PolygonSketchMode);
            }
        }
    }
}