import QtQuick 2.12
import QtQuick.Controls 2.7
import QtQuick.Layouts 1.12

Page {
    id: root
    property var buttons
    title: qsTr("Главная страница")

    ColumnLayout {
        anchors.fill: parent

        Repeater {
            model: buttons
        }
    }
}