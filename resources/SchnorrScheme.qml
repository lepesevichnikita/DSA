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

    FileDialog {
        id: openPublicKeyDialog
        fileMode: FileDialog.OpenFile
        options: FileDialog.ReadOnly
        title: qsTr("Выберите открытый ключ")
        onAccepted: {
            var path = file.toString().replace("file://", "")
            print(path)
            keysReader.public_key_path = path
        }
    }

    FileDialog {
        id: openPrivateKeyDialog
        fileMode: FileDialog.OpenFile
        options: FileDialog.ReadOnly
        title: qsTr("Выберите закрытый ключ")
        onAccepted: {
            var path = file.toString().replace("file://", "")
            print(path)
            keysReader.private_key_path = path
        }
    }

    GridLayout {
        anchors.fill: parent
        columns: 2

        GridLayout {
            columns: 3
            Layout.fillHeight: true
            Layout.fillWidth: true
            Button {
                text: qsTr("Выбрать публичный ключ")
                onClicked: openPublicKeyDialog.open()
            }
            Label {
                text: qsTr("Публичный ключ:")
            }

            Label {
                id: publicKeyStatus
                text: qsTr("Не выбран")
            }

            Button {
                text: qsTr("Выбрать закрытый ключ")
                onClicked: openPrivateKeyDialog.open()
            }
            Label {
                text: qsTr("Закрытый ключ:")
            }

            Label {
                id: privateKeyStatus
                text: qsTr("Не выбран")
            }
            states: [
                State {
                    name: "publicKeySelected"
                    when: keysReader.has_public_key
                    PropertyChanges {
                        target: publicKeyStatus
                        text: qsTr("Выбран")
                    }
                },

                State {
                    name: "privateKeySelected"
                    when: keysReader.has_private_key
                    PropertyChanges {
                        target: privateKeyStatus
                        text: qsTr("Выбран")
                    }
                }
            ]
        }
        GridLayout {
            columns: 2
            Layout.fillHeight: true
            Layout.fillWidth: true
        }
    }

}