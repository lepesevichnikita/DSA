from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.dsa import DSASigner


class DSASignerModel(QObject):
    keysChanged = pyqtSignal()
    filePathChanged = pyqtSignal()
    signNameChanged = pyqtSignal()
    signChanged = pyqtSignal()
    hashOfFileChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._signer = DSASigner()
        self._file_path = ""
        self._sign_name = ""
        self.filePathChanged.connect(self.calculate_hash_of_file)
        self.filePathChanged.connect(self.hashOfFileChanged)
        self.filePathChanged.connect(self.sign_file)

    @pyqtProperty(list, notify=keysChanged)
    def keys(self) -> list:
        return self._signer.keys_container.keys

    @pyqtProperty(str, notify=signChanged)
    def r(self) -> str:
        return hex(self._signer.sign.r) if self._signer.has_sign else ""

    @pyqtProperty(str, notify=signChanged)
    def s(self) -> str:
        return hex(self._signer.sign.s) if self._signer.has_sign else ""

    @keys.setter
    def keys(self, keys: list):
        self._signer.keys = keys
        self.keysChanged.emit()

    @pyqtProperty(str, notify=filePathChanged)
    def file_path(self) -> str:
        return self._signer.file_path

    @file_path.setter
    def file_path(self, file_path: str):
        self._signer.file_path = file_path
        self.filePathChanged.emit()

    @pyqtProperty(str, notify=signNameChanged)
    def sign_name(self) -> str:
        return self._signer.sign_name

    @sign_name.setter
    def sign_name(self, sign_name: str):
        self._signer.sign_name = sign_name
        self.signNameChanged.emit()

    @pyqtSlot()
    def calculate_hash_of_file(self):
        self._signer.calculate_hash_of_file()

    @pyqtSlot()
    def sign_file(self):
        self._signer.sign_file()
        self.signChanged.emit()

    @pyqtSlot()
    def write_sign(self):
        self._signer.write_sign()

    @pyqtProperty(str, notify=hashOfFileChanged)
    def hash_of_file(self) -> str:
        return hex(self._signer.hashed_data)
