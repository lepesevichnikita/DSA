from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.schnorr_scheme import SchnorrSchemeClient


class SchnorrSchemeClientModel(QObject):
    rChanged = pyqtSignal(int)
    xChanged = pyqtSignal(int)
    sChanged = pyqtSignal(int)
    eChanged = pyqtSignal(int)
    keysChanged = pyqtSignal(list)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schnorr_scheme_client = SchnorrSchemeClient()
        self.rChanged.connect(self.gen_x)
        self.eChanged.connect(self.gen_s)

    @pyqtProperty(int, notify=rChanged)
    def r(self) -> int:
        return self._schnorr_scheme_client.r

    @pyqtSlot(int)
    def gen_r(self):
        self._schnorr_scheme_client.gen_r()

    @pyqtProperty(int, notify=xChanged)
    def x(self) -> int:
        return self._schnorr_scheme_client.x

    @pyqtSlot(int)
    def gen_x(self):
        self._schnorr_scheme_client.gen_x()
        self.xChanged.emit(self.x)

    @pyqtProperty(int, notify=sChanged)
    def s(self) -> int:
        return self._schnorr_scheme_client.s

    @pyqtSlot(int)
    def gen_s(self):
        self._schnorr_scheme_client.gen_s()
        self.sChanged.emit(self.s)

    @pyqtProperty(int, notify=eChanged)
    def e(self) -> int:
        return self._schnorr_scheme_client.e

    @e.setter
    def e(self, e: int):
        self._schnorr_scheme_client.e = e
        self.eChanged.emit(e)

    @pyqtProperty(list, notify=keysChanged)
    def keys(self) -> list:
        return self._schnorr_scheme_client.keys

    @keys.setter
    def keys(self, keys: list):
        self._schnorr_scheme_client.keys = keys
        self.keysChanged.emit(keys)
