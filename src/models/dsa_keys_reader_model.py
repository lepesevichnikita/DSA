from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.dsa import DSAKeysReader, DSAPublicKey


class DSAKeysReaderModel(QObject):
    keysChanged = pyqtSignal()
    publicKeyPathChanged = pyqtSignal()
    privateKeyPathChanged = pyqtSignal()
    publicKeyChanged = pyqtSignal()
    privateKeyChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._keys_reader = DSAKeysReader()
        self.publicKeyPathChanged.connect(self.read_public_key)
        self.privateKeyPathChanged.connect(self.read_private_key)
        self.publicKeyChanged.connect(self.keysChanged)
        self.privateKeyChanged.connect(self.keysChanged)

    @pyqtProperty(DSAPublicKey, notify=publicKeyChanged)
    def public_key(self) -> DSAPublicKey:
        return self._keys_reader.keys_container.public_key

    @pyqtProperty(str, notify=publicKeyChanged)
    def q(self) -> str:
        return hex(self._keys_reader.public_key.q)

    @pyqtProperty(str, notify=publicKeyChanged)
    def g(self) -> str:
        return hex(self._keys_reader.public_key.g)

    @pyqtProperty(str, notify=publicKeyChanged)
    def p(self) -> str:
        return hex(self._keys_reader.public_key.p)

    @pyqtProperty(str, notify=publicKeyChanged)
    def y(self) -> str:
        return hex(self._keys_reader.public_key.y)

    @pyqtProperty(str, notify=privateKeyChanged)
    def private_key(self) -> str:
        return hex(self._keys_reader.private_key)

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

    @pyqtProperty(bool, notify=publicKeyChanged)
    def has_public_key(self) -> bool:
        return self._keys_reader.has_public_key

    @pyqtProperty(bool, notify=privateKeyChanged)
    def has_private_key(self) -> bool:
        return self._keys_reader.has_private_key
