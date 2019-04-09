import QtQuick 2.7
import QtQuick.Controls 2.5

import QtQml.Models 2.1

ApplicationWindow {
    title: "DSABase"
    visible: true

    minimumWidth: 1024
    minimumHeight: 720

    ObjectModel {
        id: objectModel

        Keygen {}
        FileSign {}
        Item{}
    }

    footer: TabBar {
        id: tabBar
        width: parent.width
        currentIndex: swipeView.currentIndex

        Repeater {
            model: ["Сгенерировать ключи", "Подписать файл", "Проверить подпись"]
            TabButton {
                text: qsTr(modelData)
            }
        }

    }

    SwipeView {
        id: swipeView
        anchors.fill: parent
        anchors.margins: 20
        currentIndex: tabBar.currentIndex

        Repeater {
            model: objectModel
        }
    }
}
