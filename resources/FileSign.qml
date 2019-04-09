import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3

import dsa 1.0

ColumnLayout {

    DSAKeysReader {
        id: keysReader
    }

    DSASigner {
        id: signer
        keys: keysReader.keys
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

    TextField {
        Layout.fillWidth: true
        text: keysReader.p
        placeholderText: qsTr("P")
        readOnly: true
        selectByMouse: true
    }

    TextField {
        Layout.fillWidth: true
        text: keysReader.q
        placeholderText: qsTr("Q")
        readOnly: true
        selectByMouse: true
    }

    TextField {
        Layout.fillWidth: true
        text: keysReader.g
        placeholderText: qsTr("G")
        readOnly: true
        selectByMouse: true
    }

    TextField {
        Layout.fillWidth: true
        text: keysReader.y
        placeholderText: qsTr("Y")
        readOnly: true
        selectByMouse: true
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

    RowLayout {
        TextField {
            Layout.fillWidth: true
            text: keysReader.private_key
            placeholderText: qsTr("Выбранный файл")
            readOnly: true
            selectByMouse: true
        }
        Button {
            text: qsTr("Открыть закрытый ключ")
            onClicked: openPrivateKeyDialog.open()
        }
    }

    RowLayout {
        FileDialog {
            id: selectFileDialog
            title: qsTr("Выберите файл для подписи")
            visible: false
            selectFolder: false
            selectMultiple: false
            onAccepted: {
                var path = fileUrl.toString().replace("file://", "")
                signer.file_path = path
            }
        }

        TextField {
            Layout.fillWidth: true
            text: signer.file_path
            placeholderText: qsTr("Выбранный файл")
            readOnly: true
            selectByMouse: true
        }

        Button {
            text: qsTr("Выбрать файл")
            onClicked: selectFileDialog.open()
        }
    }



    RowLayout {
        Label {
            text: qsTr("Хэш-сумма выбранного файла")
        }

        TextField {
            Layout.fillWidth: true
            text: signer.hash_of_file
            readOnly: true
            selectByMouse: true
        }
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("Подпись")
    }


    Button {
        Layout.fillWidth: true
        text: qsTr("Вычислить подпись")
        onClicked: signer.sign_file()
    }

    TextField {
        Layout.fillWidth: true
        text: signer.r
        placeholderText: qsTr("Первая часть подписи (R)")
        readOnly: true
        selectByMouse: true
    }

    TextField {
        Layout.fillWidth: true
        text: signer.s
        placeholderText: qsTr("Вторая часть подписи (S)")
        readOnly: true
        selectByMouse: true
    }

    RowLayout {
        TextField {
            Layout.fillWidth: true
            text: signer.sign_name
            placeholderText: qsTr("Название подписи")
            selectByMouse: true
            onEditingFinished: {
                signer.sign_name = text
            }
        }

        Button {
            Layout.fillWidth: true
            text: qsTr("Сохранить подпись")
            onClicked: signer.write_sign()
        }
    }
}
