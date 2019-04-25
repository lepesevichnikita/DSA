#!/usr/bin/env python3

import sys

from PyQt5.QtCore import QUrl, qInstallMessageHandler
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType

# noinspection PyUnresolvedReferences
import resources_rc
from src.models import DSAKeygenModel, DSAKeysWriterModel, DSAKeysReaderModel, \
    DSASignerModel, DSASignCheckerModel

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
    qmlRegisterType(DSASignerModel, "dsa", 1, 0, "DSASigner")
    qmlRegisterType(DSASignCheckerModel, "dsa", 1, 0, "DSASignChecker")

    engine = QQmlApplicationEngine()
    engine.load(MAIN_QML)

    sys.exit(app.exec())


entry_points = {
    '__main__': main
}

entry_points[__name__]()
