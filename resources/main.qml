import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12

import QtQml.Models 2.1

ApplicationWindow {
    property int margins: 20
    title: stackView.currentItem.title
    visible: true

    minimumWidth: 1024
    minimumHeight: 720

    ObjectModel {
        id: objectModel

    }

    header: RowLayout {
        id: headerBar
        width: parent.width
        Button {
            Layout.margins: margins
            Layout.alignment: Qt.AlignLeft | Qt.AlignVCenter
            text: qsTr("Назад")
            onClicked: stackView.pop()
        }
        states: [
            State {
                name: 'on home page'
                when: stackView.depth == 1
                PropertyChanges {
                    target: headerBar
                    visible: false
                }
            }
        ]
    }

    StackView {
        id: stackView
        anchors.fill: parent
        anchors.margins: margins
        initialItem: mainPage

        MainPage {
            id: mainPage
            buttons: ObjectModel {
                Button {
                    text: qsTr("Сгенерировать ключ")
                    onClicked: stackView.push(keygenPage)
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: true
                }
                Button {
                    text: qsTr("Подписать файл")
                    onClicked: stackView.push(fileSignPage)
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: true
                }
                Button {
                    text: qsTr("Проверить подпись")
                    onClicked: stackView.push(signCheckingPage)
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: true
                }

                Button {
                    text: qsTr("Схема Шнора")
                    onClicked: stackView.push(schnorrScheme)
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: true
                }
            }
        }

        Component {
            id: keygenPage
            Keygen {
                anchors.margins: margins
            }
        }

        Component {
            id: fileSignPage
            FileSign {
                anchors.margins: margins
            }
        }

        Component {
            id: signCheckingPage
            SignCheck {
                anchors.margins: margins
            }
        }

        Component {
            id: schnorrScheme
            SchnorrScheme {
                anchors.margins: margins
            }

        }
    }

}
