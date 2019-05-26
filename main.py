#!/usr/bin/env python3

import sys

from PyQt5.QtCore import qInstallMessageHandler, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

# noinspection PyUnresolvedReferences
import resources_rc
from src.models import DSABaseModel, DSAKeygenModel, DSAKeysReaderModel, \
    DSAKeysWriterModel, DSASignCheckerModel, DSASignerModel, \
    SchnorrSchemeClientModel, SchnorrSchemeKeygenModel, \
    SchnorrSchemeValidatorModel

MAIN_QML = QUrl("qrc:///main.qml")
MODULES_IMPORT_PATH = "qrc:///modules"


def handleStatusChange(mode, message, context):
    print(mode)
    print(message, context)


def main():
    app = QApplication(sys.argv)
    qInstallMessageHandler(handleStatusChange)

    qmlRegisterType(DSAKeygenModel, "dsa", 1, 0, "DSAKeygen")
    qmlRegisterType(DSAKeysWriterModel, "dsa", 1, 0, "DSAKeysWriter")
    qmlRegisterType(DSAKeysReaderModel, "dsa", 1, 0, "DSAKeysReader")
    qmlRegisterType(DSASignerModel, "dsa", 1, 0, "DSASigner")
    qmlRegisterType(DSASignCheckerModel, "dsa", 1, 0, "DSASignChecker")
    qmlRegisterType(SchnorrSchemeClientModel, "schnorr_scheme", 1, 0,
                    "SchnorrSchemeClient")
    qmlRegisterType(SchnorrSchemeValidatorModel, "schnorr_scheme", 1, 0,
                    "SchnorrSchemeValidator")
    qmlRegisterType(DSABaseModel, "dsa", 1, 0, "DSABaseModel")
    qmlRegisterType(SchnorrSchemeKeygenModel, "schnorr_scheme", 1, 0,
                    "SchnorrSchemeKeygen")

    engine = QQmlApplicationEngine()
    engine.load(MAIN_QML)

    sys.exit(app.exec())


entry_points = {
    '__main__': main
}

entry_points[__name__]()
