import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

import QtQml.Models 2.1

ApplicationWindow {
    title: "DSABase"
    visible: true

    minimumWidth: 1024
    minimumHeight: 720

    ObjectModel {
        id: objectModel

        Item {
            Keygen {}
        }
    }

    footer: TabBar {
        id: bar
        width: parent.width

        Repeater {
            model: ["Сгенерировать ключи", "Подписать файл", "Проверить подпись"]
            TabButton {
                text: qsTr(modelData)
            }
        }

    }

    StackLayout {
        anchors.fill: parent
        anchors.margins: 20
        currentIndex: bar.currentIndex

        Repeater {
            model: objectModel
        }
    }
}
