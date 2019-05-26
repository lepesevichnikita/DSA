from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.schnorr_scheme import SchnorrSchemeValidator


class SchnorrSchemeValidatorModel(QObject):
    complexityChanged = pyqtSignal()
    sChanged = pyqtSignal()
    eChanged = pyqtSignal()
    isValidChanged = pyqtSignal()
    xChanged = pyqtSignal()
    publicKeyChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schnorr_scheme_validator = SchnorrSchemeValidator()
        self.xChanged.connect(self.gen_e)
        self.xChanged.connect(self.isValidChanged)
        self.sChanged.connect(self.isValidChanged)

    @pyqtProperty(int, notify=complexityChanged)
    def complexity(self) -> int:
        return self._schnorr_scheme_validator.complexity

    @complexity.setter
    def complexity(self, complexity: int):
        self._schnorr_scheme_validator.complexity = complexity
        self.complexityChanged.emit()

    @pyqtProperty(str, notify=sChanged)
    def s(self) -> str:
        return hex(self._schnorr_scheme_validator.s)

    @s.setter
    def s(self, s: str):
        self._schnorr_scheme_validator.s = int(s, 16)
        self.sChanged.emit()

    @pyqtProperty(str, notify=eChanged)
    def e(self) -> str:
        return hex(self._schnorr_scheme_validator.e)

    @pyqtSlot()
    def init(self, x: str):
        self.x = int(x, 16)
        self.gen_e()

    @pyqtSlot()
    def gen_e(self):
        prev_e = self._schnorr_scheme_validator.e
        self._schnorr_scheme_validator.gen_e()
        if prev_e != self._schnorr_scheme_validator.e:
            self.eChanged.emit()

    @pyqtProperty(str, notify=xChanged)
    def x(self) -> str:
        return hex(self._schnorr_scheme_validator.x)

    @x.setter
    def x(self, x: str):
        self._schnorr_scheme_validator.x = int(x, 16)
        self.xChanged.emit()

    @pyqtProperty(list, notify=publicKeyChanged)
    def keys(self) -> list:
        return self._schnorr_scheme_validator.keys

    @keys.setter
    def keys(self, keys: list):
        self._schnorr_scheme_validator.keys = keys
        self.publicKeyChanged.emit()

    @pyqtProperty(bool, notify=isValidChanged)
    def is_valid(self) -> bool:
        return self._schnorr_scheme_validator.is_valid

    @pyqtSlot()
    def gen_e(self):
        self._schnorr_scheme_validator.gen_e()
        self.eChanged.emit()
