import QtQuick
import QtQuick.Controls
import Esri.Mapping
import Esri.Mapping.Slots

Item {

    function startSketching() {
        model.startSketching(MapViewModel.PolygonSketchMode);
        sketchingEnabled = true;
    }

    function stopSketching() {
        sketchingEnabled = false;
        model.stopSketching();
    }

    function createBuffer() {
        gpHandler.createBuffer(model);
    }

    property bool sketchingEnabled: false

    Geoprocessing {
        id: gpHandler
    }

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
            var polygon = JSON.parse(geometry);
            if (polygon.hasOwnProperty("rings") && Array.isArray(polygon.rings) && 0 < polygon.rings.length) {
                // Add the polygon geometry as graphic
                var geometriesJson = JSON.stringify([polygon]);
                var renderer = {
                    "label": "",
                    "description": "",
                    "type": "simple",
                    "symbol": {
                        "type": "esriSFS",
                        "style": "esriSFSSolid",
                        "color": [0, 128, 0, 78],
                        "outline": {
                            "type": "esriSLS",
                            "style": "esriSLSSolid",
                            "color": [110, 110, 110, 255],
                            "width": 1
                        }
                    }
                };
                var rendererJson = JSON.stringify(renderer);
                model.addGeometries(geometriesJson, rendererJson);

                // Delegate to the Python-based slot
                var polygonJson = JSON.stringify(polygon);
                gpHandler.sketchCompleted(polygonJson);
            } 

            // Start the next sketch
            if (sketchingEnabled) {
                model.startSketching(MapViewModel.PolygonSketchMode);
            }
        }
    }
}