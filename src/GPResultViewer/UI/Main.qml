import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

import Esri.Mapping

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

            ButtonGroup {
                buttons: [navigateButton, sketchButton]
            }

            RadioButton {
                id: navigateButton
                checked: true
                text: qsTr("Navigate")
                onToggled: {
                    mapViewComponent.stopSketching();
                }
            }

            RadioButton {
                id: sketchButton
                text: qsTr("Sketch")
                onToggled: {
                    mapViewComponent.startSketching();
                }
            }
        }
    }

    MapViewComponent {
        id: mapViewComponent
        anchors.fill: parent
    }
}