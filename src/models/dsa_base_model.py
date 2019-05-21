from PyQt5.QtCore import pyqtProperty, QObject

from src.dsa import DSABase


class DSABaseModel(QObject):

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    @pyqtProperty(str)
    def PublicKeyExtension(self) -> str:
        return DSABase.PUBLIC_KEY_EXTENSION

    @pyqtProperty(str)
    def PrivateKeyExtension(self) -> str:
        return DSABase.PRIVATE_KEY_EXTENSION
