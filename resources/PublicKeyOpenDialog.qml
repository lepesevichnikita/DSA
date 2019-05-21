import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import Qt.labs.platform 1.1

import dsa 1.0

FileDialog {
    id: root
    property string path

    DSABaseModel {
        id: dsa
    }

    title: qsTr("Выберите публичный ключ")
    visible: false
    options: FileDialog.OpenFile
    nameFilters: [
        [qsTr("Публичный ключ DSA"), "(*", dsa.PublicKeyExtension, ")"].join("")
    ]
    onAccepted: {
        path = file.toString().replace("file://", "")
    }
}
