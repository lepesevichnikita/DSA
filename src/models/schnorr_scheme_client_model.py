from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.schnorr_scheme import SchnorrSchemeClient


class SchnorrSchemeClientModel(QObject):
    rChanged = pyqtSignal()
    xChanged = pyqtSignal()
    sChanged = pyqtSignal()
    eChanged = pyqtSignal()
    keysChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schnorr_scheme_client = SchnorrSchemeClient()
        self.rChanged.connect(self.gen_x)
        self.eChanged.connect(self.gen_s)

    @pyqtProperty(str, notify=rChanged)
    def r(self) -> str:
        return hex(self._schnorr_scheme_client.r)

    @pyqtSlot()
    def gen_r(self):
        prev_r = self._schnorr_scheme_client.r
        self._schnorr_scheme_client.gen_r()
        if prev_r != self._schnorr_scheme_client.r:
            self.rChanged.emit()

    @pyqtProperty(str, notify=xChanged)
    def x(self) -> str:
        return hex(self._schnorr_scheme_client.x)

    @pyqtSlot()
    def gen_x(self):
        prev_x = self._schnorr_scheme_client.x
        self._schnorr_scheme_client.gen_x()
        if prev_x != self._schnorr_scheme_client.x:
            self.xChanged.emit()

    @pyqtProperty(str, notify=sChanged)
    def s(self) -> str:
        return hex(self._schnorr_scheme_client.s)

    @pyqtSlot()
    def gen_s(self):
        prev_s = self._schnorr_scheme_client.s
        self._schnorr_scheme_client.gen_s()
        if prev_s != self._schnorr_scheme_client.s:
            self.sChanged.emit()

    @pyqtProperty(str, notify=eChanged)
    def e(self) -> str:
        return hex(self._schnorr_scheme_client.e)

    @e.setter
    def e(self, e: str):
        self._schnorr_scheme_client.e = int(e, 16)
        self.eChanged.emit()

    @pyqtProperty(list, notify=keysChanged)
    def keys(self) -> list:
        return self._schnorr_scheme_client.keys

    @keys.setter
    def keys(self, keys: list):
        self._schnorr_scheme_client.keys = keys
        self.keysChanged.emit()
