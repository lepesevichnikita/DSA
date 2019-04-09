from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty

from src.dsa.dsa_sign_checker import DSASignChecker


class DSASignCheckerModel(QObject):
    keysChanged = pyqtSignal()
    signPathChanged = pyqtSignal()
    filePathChanged = pyqtSignal()
    hashOfFileChanged = pyqtSignal()
    signChanged = pyqtSignal()
    signStatusChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._sign_checker = DSASignChecker()
        self._is_sign_correct = False
        self.filePathChanged.connect(self.calculate_hash_of_file)
        self.filePathChanged.connect(self.check_sign)
        self.signPathChanged.connect(self.read_sign)
        self.signChanged.connect(self.calculate_hash_of_file)
        self.signChanged.connect(self.check_sign)

    @pyqtProperty(bool, notify=signStatusChanged)
    def is_sign_correct(self) -> bool:
        return self._is_sign_correct

    @pyqtProperty(str, notify=signChanged)
    def r(self) -> str:
        return hex(
            self._sign_checker.sign.r) if self._sign_checker.has_sign else ""

    @pyqtProperty(str, notify=signChanged)
    def s(self) -> str:
        return hex(
            self._sign_checker.sign.s) if self._sign_checker.has_sign else ""

    @pyqtProperty(list, notify=keysChanged)
    def keys(self) -> list:
        return self._sign_checker.keys_container.keys

    @keys.setter
    def keys(self, keys: list):
        self._sign_checker.keys_container.keys = keys
        self.keysChanged.emit()

    @pyqtProperty(str, notify=signPathChanged)
    def sign_path(self) -> str:
        return self._sign_checker.sign_path

    @sign_path.setter
    def sign_path(self, sign_path: str):
        self._sign_checker.sign_path = sign_path
        self.signPathChanged.emit()

    @pyqtProperty(str, notify=filePathChanged)
    def file_path(self) -> str:
        return self._sign_checker.file_path

    @file_path.setter
    def file_path(self, file_path: str):
        self._sign_checker.file_path = file_path
        self.filePathChanged.emit()

    @pyqtSlot()
    def read_sign(self):
        self._sign_checker.read_sign()
        self.signChanged.emit()

    @pyqtSlot()
    def calculate_hash_of_file(self):
        self._sign_checker.calculate_hash_of_file()
        self.hashOfFileChanged.emit()

    @pyqtSlot()
    def check_sign(self):
        self._is_sign_correct = self._sign_checker.is_sign_correct
        self.signStatusChanged.emit()

    @pyqtProperty(str, notify=hashOfFileChanged)
    def hash_of_file(self) -> str:
        return hex(self._sign_checker.hashed_data)
