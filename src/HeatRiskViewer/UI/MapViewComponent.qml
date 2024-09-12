import QtQuick
import QtQuick.Controls
import Esri.Mapping

Item {

    // Create MapQuickView here, and create its Map etc. in C++ code
    MapView {
        id: view
        anchors.fill: parent
        // set focus to enable keyboard navigation
        focus: true

        DropArea {
        anchors.fill: parent

        onDropped: (drop) => {
            function loadVectorTilePackage(fileUrl) {
                var filePath = fileUrl.toString();
                filePath = filePath.replace(/^\/{2,}|^.*?:(\/){2,}/, "");
                if (filePath.endsWith(".vtpk")) {
                    console.log(`Reading vector tiles from ${filePath}`);
                    model.loadBasemapFromVectorTilePackage(filePath);
                }
            }
            drop.urls.forEach(loadVectorTilePackage);
        }
    }
    }

    // Declare the C++ instance which creates the map etc. and supply the view
    MapViewModel {
        id: model
        mapView: view
    }
}