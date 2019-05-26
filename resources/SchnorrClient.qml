import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12
import Qt.labs.platform 1.1

import schnorr_scheme 1.0
import dsa 1.0

Page {
    id: root
    property SchnorrSchemeClient client

    header: Label {
        text: qsTr("Клиент")
        font.pointSize: Qt.application.font.pointSize * 2
    }

    GridLayout {
        anchors.fill: parent
        columns: 4

        Label {
            text: qsTr("R")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            readOnly: true
            text: client.r
        }

        Button {
            text: qsTr("Сгенерировать")
            onClicked: client.gen_r()
        }

        Label {
            text: qsTr("X")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            readOnly: true
            text: client.x
        }
    }
}
