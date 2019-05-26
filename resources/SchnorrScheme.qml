import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12
import Qt.labs.platform 1.1

import schnorr_scheme 1.0
import dsa 1.0

Page {
    id: root

    DSAKeysReader {
        id: keysReader
    }

    SchnorrSchemeClient {
        id: schnorrClient
        keys: keysReader.keys
        e: schnorrValidator.e
    }

    SchnorrSchemeValidator {
        id: schnorrValidator
        keys: keysReader.keys
        s: schnorrClient.s
        x: schnorrClient.x
    }

    PublicKeyOpenDialog {
        id: openPublicKeyDialog
        onPathChanged: keysReader.public_key_path = path
    }

    PrivateKeyOpenDialog {
        id: openPrivateKeyDialog
        onPathChanged: keysReader.private_key_path = path
    }


    header: GridLayout {
        Layout.fillWidth: true
        columns: 3

        Label {
            text: qsTr("Публичный ключ:")
        }

        TextField {
            id: publicKeyStatus
            Layout.fillWidth: true
            readOnly: true
            placeholderText: qsTr("Открытый ключ")
            text: keysReader.public_key_path
        }

        Button {
            text: qsTr("Выбрать")
            onClicked: openPublicKeyDialog.open()
        }

        Label {
            text: qsTr("Закрытый ключ")
        }

        TextField {
            id: privateKeyStatus
            Layout.fillWidth: true
            readOnly: true
            placeholderText: qsTr("Закрытый ключ")
            text: keysReader.private_key_path
        }
        Button {
            text: qsTr("Выбрать")
            onClicked: openPrivateKeyDialog.open()
        }
    }

    ScrollView {
        anchors.fill: parent

        Column {
            anchors.fill: parent
            StackLayout {
                id: schnor
                currentIndex: bar.currentIndex
                anchors.fill: parent

                SchnorrClient {
                    client: schnorrClient
                }

                SchnorrValidator {
                    validator: schnorrValidator
                }
            }
        }
    }
    footer: TabBar {
        id: bar
        Repeater {
            model: ["Клиент", "Валидатор"]
            delegate: TabButton {
                text: qsTr(modelData)
            }
        }

    }
}