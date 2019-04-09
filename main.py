#!/usr/bin/env python3

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtCore import QUrl, qInstallMessageHandler

import sys
import resources_rc

from src import DSAKeygenModel, DSAKeysWriterModel, DSAKeysReaderModel

MAIN_QML = QUrl("qrc:///main.qml")
MODULES_IMPORT_PATH = "qrc:///modules"


def handleStatusChange(mode, message, context):
    print(message, context)


def main():
    app = QGuiApplication(sys.argv)
    qInstallMessageHandler(handleStatusChange)

    qmlRegisterType(DSAKeygenModel, "dsa", 1, 0, "DSAKeygen")
    qmlRegisterType(DSAKeysWriterModel, "dsa", 1, 0, "DSAKeysWriter")
    qmlRegisterType(DSAKeysReaderModel, "dsa", 1, 0, "DSAKeysReader")

    engine = QQmlApplicationEngine()
    engine.addImportPath(MODULES_IMPORT_PATH)
    engine.load(MAIN_QML)

    sys.exit(app.exec())


entry_points = {
    '__main__': main
}

entry_points[__name__]()
