import QtQuick 2.9
import QtQuick.Controls 2.7
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3

import dsa 1.0

ColumnLayout {
    id: root
    anchors.fill: parent

    DSAKeygen {
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

    state: keygen.state
    onStateChanged: print(state)

    states: [
        State {
            name: 'GENERATING_STARTED'
            PropertyChanges {
                target: key_lengths
                enabled: false
            }
        },
        State {
            name: 'GENERATING_FINISHED'
            PropertyChanges {
                target: key_lengths
                enabled: true
            }
        }
    ]

    ColumnLayout {
        id: key_lengths

        Button {
            Layout.fillWidth: true
            text: qsTr("Сгенерировать новые ключи")
            onClicked: keygen.async_generate_new_keys()
        }

        RowLayout {
            Label {
                Layout.fillWidth: true
                text: qsTr("Длина P")
            }

            TextField {
                text: keygen.p_length
                placeholderText: qsTr("Введите размер P в битах")
                onEditingFinished: keygen.p_length = Math.abs(parseInt(text)) || 8
            }
        }

        RowLayout {
            Label {
                Layout.fillWidth: true
                text: qsTr("Длина Q")
            }

            TextField {
                text: keygen.q_length
                placeholderText: qsTr("Введите размер Q в битах")
                onEditingFinished: keygen.q_length = Math.abs(parseInt(text)) || 8
            }
        }
    }

    FileDialog {
        id: openPublicKeyDialog
        title: qsTr("Выберите публичный ключ")
        visible: false
        selectFolder: false
        selectMultiple: false
        onAccepted: {
            var path = fileUrl.toString().replace("file://", "")
            keysReader.public_key_path = path
            keysReader.read_public_key()
        }
    }

    Button {
        Layout.fillWidth: true
        text: qsTr("Открыть публичный ключ")
        onClicked: openPublicKeyDialog.open()
    }
    RowLayout {
        Label {
            text: qsTr("P")
        }

        TextField {
            Layout.fillWidth: true
            text: keygen.p
            readOnly: true
            selectByMouse: true
        }
    }

    RowLayout {
        Label {
            text: qsTr("Q")
        }

        TextField {
            Layout.fillWidth: true
            text: keygen.q
            readOnly: true
            selectByMouse: true
        }
    }

    RowLayout {
        Label {
            text: qsTr("G")
        }

        TextField {
            Layout.fillWidth: true
            text: keygen.g
            readOnly: true
            selectByMouse: true
        }
    }

    RowLayout {
        Label {
            text: qsTr("Y")
        }

        TextField {
            Layout.fillWidth: true
            text: keygen.y
            readOnly: true
            selectByMouse: true
        }
    }

    Button {
        Layout.fillWidth: true
        text: qsTr("Сгенерировать новую пару X/Y")
        onClicked: keygen.async_generate_new_x_y()
    }

    FileDialog {
        id: openPrivateKeyDialog
        title: qsTr("Выберите закрытый ключ")
        visible: false
        selectFolder: false
        selectMultiple: false
        onAccepted: {
            var path = fileUrl.toString().replace("file://", "")
            keysReader.private_key_path = path
            keysReader.read_private_key()
        }
    }

    Button {
        Layout.fillWidth: true
        text: qsTr("Открыть закрытый ключ")
        onClicked: openPrivateKeyDialog.open()
    }

    RowLayout {
        Label {
            text: qsTr("X")
        }

        TextField {
            Layout.fillWidth: true
            text: keygen.x
            readOnly: true
            selectByMouse: true
        }
    }

    RowLayout {
        FileDialog {
            id: saveDialog
            title: qsTr("Выберите каталог для сохранения ключей")
            visible: false
            selectFolder: true
            selectMultiple: false
            onAccepted: {
                print(folder)
                keysWriter.directory_path = folder.
                                            toString().
                                            replace("file://", "")
                keysWriter.write_keys()
            }
        }
        TextField {
            Layout.fillWidth: true
            placeholderText: qsTr("Введите название для ключей")
            onEditingFinished: {
                keysWriter.keys_name = text
            }
        }
        Button {
            Layout.fillWidth: true
            text: qsTr("Сохранить ключи")
            onClicked: saveDialog.open()
        }
    }
}