from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty

from src.dsa_keys_reader import DSAKeysReader
from src.dsa_keys_container import DSAKeysContainer


class DSAKeysReaderModel(QObject):
    keysChanged = pyqtSignal()
    publicKeyPathChanged = pyqtSignal()
    privateKeyPathChanged = pyqtSignal()
    publicKeyChanged = pyqtSignal()
    privateKeyChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._keys_reader = DSAKeysReader()

    @pyqtProperty(list, notify=keysChanged)
    def keys(self) -> list:
        return self._keys_reader.keys

    @keys.setter
    def keys(self, keys: list):
        try:
            self._keys_reader.keys = keys
            self.keysChanged.emit()
        except Exception as e:
            print(e)

    @pyqtProperty(str, notify=publicKeyPathChanged)
    def public_key_path(self) -> str:
        return self._keys_reader.public_key_path

    @public_key_path.setter
    def public_key_path(self, public_key_path: str):
        self._keys_reader.public_key_path = public_key_path
        self.publicKeyPathChanged.emit()

    @pyqtProperty(str, notify=privateKeyPathChanged)
    def private_key_path(self):
        return self._keys_reader.private_key_path

    @private_key_path.setter
    def private_key_path(self, private_key_path: str):
        self._keys_reader.private_key_path = private_key_path
        self.privateKeyPathChanged.emit()

    @pyqtSlot()
    def read_public_key(self):
        try:
            self._keys_reader.read_public_key()
            self.publicKeyChanged.emit()
        except Exception as e:
            print(e)

    @pyqtSlot()
    def read_private_key(self):
        try:
            self._keys_reader.read_private_key()
            self.privateKeyChanged.emit()
        except Exception as e:
            print(e)
