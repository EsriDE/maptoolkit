import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

import Esri.Mapping
import Esri.Mapping.Slots

ApplicationWindow {
    visible: true
    width: 800
    height: 600

    Material.theme: Material.Dark
    Material.accent: "#C9F2FF"
    Material.background: "#0289C3"
    Material.foreground: "#FFFFFF"
    Material.primary: "#035799"

    font.pixelSize: 14

    header: ToolBar {
        RowLayout {
            anchors.fill: parent

            ToolButton {
                text: "Load"
                onClicked: {
                    geojsonHandler.loadGeoJson(filepathTextField.text, mapViewComponent.mapViewModel);
                }
            }

            TextField {
                id: filepathTextField
                Layout.margins: 8
                Layout.fillWidth: true
                placeholderText: qsTr("GeoJSON file...")
            }
        }
    }

    LoadGeoJson {
        id: geojsonHandler
    }

    MapViewComponent {
        id: mapViewComponent
        anchors.fill: parent
    }
}