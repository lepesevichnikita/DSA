import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import Qt.labs.platform 1.1

import dsa 1.0
import schnorr_scheme 1.0

Page {
    id: root
    title: qsTr("Сгенировать ключи")

    SchnorrSchemeKeygen {
        id: keygen
    }

    DSAKeysWriter {
        id: keysWriter
        keys: keygen.keys
    }

    DSAKeysReader {
        id: keysReader
        keys: keygen.keys
        onPublicKeyChanged: {
            keygen.keys = keys
        }
        onPrivateKeyChanged: {
            keygen.keys = keys
        }
    }

    FolderDialog {
        id: saveDialog
        title: qsTr("Выберите каталог для сохранения ключей")
        visible: false
        options: FolderDialog.ShowDirsOnly
        onAccepted: {
            keysWriter.directory_path = currentFolder.
                                        toString().
                                        replace("file://", "")
        }
    }

    PublicKeyOpenDialog {
        id: openPublicKeyDialog
        onPathChanged: keysReader.public_key_path = path
    }

    PrivateKeyOpenDialog {
        id: openPrivateKeyDialog
        onPathChanged: keysReader.private_key_path = path
    }

    GridLayout {
        id: keygenPageData
        anchors.fill: parent
        columns: 4

        state: keygen.state
        states: [
            State {
                name: 'GENERATING_STARTED'
                PropertyChanges {
                    target: keygenPageData
                    enabled: false
                }
            },
            State {
                name: 'GENERATING_FINISHED'
                PropertyChanges {
                    target: keygenPageData
                    enabled: true
                }
            }
        ]

        Button {
            Layout.fillWidth: true
            Layout.columnSpan: 4
            text: qsTr("Сгенерировать новые ключи")
            onClicked: keygen.async_generate_new_keys()
        }

        Label {
            text: qsTr("Длина P")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.p_length
            placeholderText: qsTr("Введите размер P в битах")
            onEditingFinished: keygen.p_length = Math.abs(parseInt(text)) || 8
        }

        Label {
            text: qsTr("Длина Q")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.q_length
            placeholderText: qsTr("Введите размер Q в битах")
            onEditingFinished: keygen.q_length = Math.abs(parseInt(text)) || 8
        }

        Button {
            Layout.fillWidth: true
            Layout.columnSpan: 4
            text: qsTr("Открыть публичный ключ")
            onClicked: openPublicKeyDialog.open()
        }

        Label {
            text: qsTr("P")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.p
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Q")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.q
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("G")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.g
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Y")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.y
            readOnly: true
            selectByMouse: true
        }

        Button {
            Layout.fillWidth: true
            Layout.columnSpan: 4
            text: qsTr("Сгенерировать новую пару X/Y")
            onClicked: keygen.async_generate_new_x_y()
        }

        Button {
            Layout.fillWidth: true
            Layout.columnSpan: 4
            text: qsTr("Открыть закрытый ключ")
            onClicked: openPrivateKeyDialog.open()
        }

        Label {
            text: qsTr("X")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: keygen.private_key
            readOnly: true
            selectByMouse: true
        }

        TextField {
            Layout.fillWidth: true
            placeholderText: qsTr("Введите название для ключей")
            Layout.columnSpan: 3
            onEditingFinished: {
                keysWriter.keys_name = text
            }
        }

        Button {
            text: qsTr("Сохранить ключи")
            onClicked: saveDialog.open()
        }
    }
}