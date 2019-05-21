from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.schnorr_scheme import SchnorrSchemeValidator


class SchnorrSchemeValidatorModel(QObject):
    complexityChanged = pyqtSignal(int)
    sChanged = pyqtSignal(int)
    eChanged = pyqtSignal(int)
    isValidChanged = pyqtSignal(bool)
    xChanged = pyqtSignal(int)
    publicKeyChanged = pyqtSignal(list)

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._schnorr_scheme_validator = SchnorrSchemeValidator()
        self.xChanged.connect(self.gen_e)
        self.xChanged.connect(self.isValidChanged)
        self.sChanged.connect(self.isValidChanged)

    @pyqtProperty(int, notify=complexityChanged)
    def complexity(
            self) -> int: return self._schnorr_scheme_validator.complexity

    @complexity.setter
    def complexity(self, complexity: int):
        self._schnorr_scheme_validator.complexity = complexity
        self.complexityChanged.emit(complexity)

    @pyqtProperty(int, notify=sChanged)
    def s(self) -> int:
        return self._schnorr_scheme_validator.s

    @s.setter
    def s(self, s: int):
        self._schnorr_scheme_validator.s = s
        self.sChanged.emit(s)

    @pyqtProperty(int, notify=eChanged)
    def e(self) -> int:
        return self._schnorr_scheme_validator.e

    @pyqtSlot(int)
    def init(self, x: int):
        self.x = x
        self._schnorr_scheme_validator.gen_e()
        self.eChanged.emit(self.e)

    @pyqtProperty(int, notify=xChanged)
    def x(self) -> int:
        return self._schnorr_scheme_validator.x

    @x.setter
    def x(self, x: int):
        self._schnorr_scheme_validator.x = x
        self.xChanged.emit(x)

    @pyqtProperty(list, notify=publicKeyChanged)
    def public_key(self) -> list:
        return self._schnorr_scheme_validator.public_key

    @public_key.setter
    def public_key(self, public_key: list) -> list:
        self._schnorr_scheme_validator.public_key = public_key
        self.publicKeyChanged.emit(public_key)

    @pyqtProperty(bool, notify=isValidChanged)
    def is_valid(self) -> bool:
        return self._schnorr_scheme_validator.is_valid

    @pyqtSlot(int)
    def gen_e(self):
        self._schnorr_scheme_validator.gen_e()
        self.eChanged.emit(self._schnorr_scheme_validator.e)
