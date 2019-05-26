import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12
import Qt.labs.platform 1.1

import schnorr_scheme 1.0
import dsa 1.0

Page {
    id: root
    property SchnorrSchemeValidator validator
    property alias schnorrValidator: root.validator

    Component.onCompleted: print(schnorrValidator)

    header: Label {
        text: qsTr("Валидатор")
        font.pointSize: Qt.application.font.pointSize * 2
    }


    GridLayout {
        anchors.fill: parent
        columns: 4

        Label {
            text: qsTr("Сложность")
        }

        Slider {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            from: 1.0
            to: 160.0
            value: schnorrValidator.complexity
            onMoved: schnorrValidator.complexity = value
        }

        Label {
            text: schnorrValidator.complexity
        }

        Label {
            text: qsTr("X")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            readOnly: true
            text: schnorrValidator.x
        }


        Label {
            text: qsTr("E")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 2
            readOnly: true
            text: schnorrValidator.e
        }

        Button {
            text: qsTr("Сгенерировать")
            onClicked: schnorrValidator.gen_e()
        }

        Label {
            text: qsTr("S")
        }

        TextField {
            Layout.fillWidth: true
            Layout.columnSpan: 3
            readOnly: true
            text: schnorrValidator.s
        }

        Label {
            text: qsTr("Статус валидации")
        }

        Label {
            text: schnorrValidator.is_valid ? qsTr("Успешно пройдена") : qsTr("Не пройдена")
        }


    }

}
