import QtQuick 2.7
import QtQuick.Controls 2.5

import QtQml.Models 2.1

ApplicationWindow {
    property int margins: 20
    title: swipeView.currentItem.title
    visible: true

    minimumWidth: 1024
    minimumHeight: 720

    ObjectModel {
        id: objectModel

        Keygen {}

        FileSign {}

        SignCheck {}
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
        anchors.margins: margins
        currentIndex: tabBar.currentIndex

        Repeater {
            model: objectModel
        }
    }
}
