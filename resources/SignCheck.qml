import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3

import dsa 1.0

Page {
    id: root
    title: qsTr("Проверить подпись")

    DSAKeysReader {
        id: keysReader
    }

    DSASignChecker {
        id: checker
        keys: keysReader.keys
        onSignStatusChanged: print(is_sign_correct)
    }

    PublicKeyOpenDialog {
        id: openPublicKeyDialog
        title: qsTr("Выберите публичный ключ")
        onPathChanged: keysReader.public_key_path = path
    }

    FileDialog {
        id: selectFileDialog
        title: qsTr("Выберите файл для подписи")
        visible: false
        selectFolder: false
        selectMultiple: false
        onAccepted: {
            var path = fileUrl.toString().replace("file://", "")
            checker.file_path = path
        }
    }

    FileDialog {
        id: selectSignDialog
        title: qsTr("Выберите подпись")
        visible: false
        selectFolder: false
        selectMultiple: false
        onAccepted: {
            var path = fileUrl.toString().replace("file://", "")
            checker.sign_path = path
        }
    }

    GridLayout {
        anchors.fill: parent
        columns: 3
        rowSpacing: 2

        Button {
            Layout.columnSpan: 3
            Layout.fillWidth: true
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
            text: qsTr("Выбранный файл")
        }

        TextField {
            Layout.fillWidth: true
            text: checker.file_path
            placeholderText: qsTr("Выбранный файл")
            readOnly: true
            selectByMouse: true
        }

        Button {
            text: qsTr("Выбрать файл")
            onClicked: selectFileDialog.open()
        }

        Label {
            text: qsTr("Хэш-сумма выбранного файла")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: checker.hash_of_file
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Выбранная подпись")
        }

        TextField {
            Layout.fillWidth: true
            text: checker.sign_path
            placeholderText: qsTr("Выбранная подпись")
            readOnly: true
            selectByMouse: true
        }

        Button {
            text: qsTr("Выбрать подпись")
            onClicked: selectSignDialog.open()
        }

        Label {
            text: qsTr("Первая часть подписи (R)")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: checker.r
            placeholderText: qsTr("Первая часть подписи (R)")
            readOnly: true
            selectByMouse: true
        }

        Label {
            text: qsTr("Вторая часть подписи (S)")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            text: checker.s
            placeholderText: qsTr("Вторая часть подписи (S)")
            readOnly: true
            selectByMouse: true
        }

        Label {
            Layout.fillWidth: true
            text: qsTr("Статус подписи: ") + qsTr(checker.is_sign_correct ? "валидна" : "невалидна")
        }
    }
}
