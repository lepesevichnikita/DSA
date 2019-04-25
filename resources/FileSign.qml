import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3

import dsa 1.0

Page {
    id: root
    title: qsTr("Подписать файл")

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

    GridLayout {
        anchors.fill: parent
        columns: 3
        rowSpacing: 2

        Button {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: qsTr("Открыть публичный ключ")
            onClicked: openPublicKeyDialog.open()
        }

        Label {
            text: qsTr("P")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: keysReader.p
            placeholderText: qsTr("P")
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Q")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: keysReader.q
            placeholderText: qsTr("Q")
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("G")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: keysReader.g
            placeholderText: qsTr("G")
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Y")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: keysReader.y
            placeholderText: qsTr("Y")
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Закрытый ключ")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: keysReader.private_key
            placeholderText: qsTr("Закрытый ключ")
            readOnly: true
            selectByMouse: true
        }

        Button {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            text: qsTr("Открыть закрытый ключ")
            onClicked: openPrivateKeyDialog.open()
        }

        Label {
            text: qsTr("Файл для подписи")
        }

        TextField {
            Layout.fillWidth: true
            text: signer.file_path
            placeholderText: qsTr("Выберите файл")
            readOnly: true
            selectByMouse: true
        }

        Button {
            Layout.fillWidth: true
            text: qsTr("Выбрать файл")
            onClicked: selectFileDialog.open()
        }

        Label {
            text: qsTr("Хэш-сумма выбранного файла")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: signer.hash_of_file
            readOnly: true
            selectByMouse: true
        }

        Label {
            Layout.columnSpan: 3
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            text: qsTr("Подпись")
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

        Button {
            Layout.fillWidth: true
            text: qsTr("Вычислить подпись")
            onClicked: signer.sign_file()
        }


        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
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
