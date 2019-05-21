from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from src.dsa import DSAKeysWriter


class DSAKeysWriterModel(QObject):
    keysChanged = pyqtSignal()
    keysNameChanged = pyqtSignal()
    directoryPathChanged = pyqtSignal()
    keysContainerChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._keys_writer = DSAKeysWriter()
        self.directoryPathChanged.connect(self.write_keys)

    @pyqtProperty(str, notify=keysNameChanged)
    def keys_name(self) -> str:
        return self._keys_writer.keys_name

    @keys_name.setter
    def keys_name(self, keys_name: str):
        self._keys_writer.keys_name = keys_name
        self.keysNameChanged.emit()

    @pyqtProperty(list, notify=keysChanged)
    def keys(self) -> list:
        return self._keys_writer.keys

    @keys.setter
    def keys(self, keys: list):
        try:
            self._keys_writer.keys = keys
        except Exception as e:
            print(e)
        finally:
            self.keysChanged.emit()

    @pyqtProperty(str, notify=directoryPathChanged)
    def directory_path(self) -> str:
        return self._keys_writer.directory_path

    @directory_path.setter
    def directory_path(self, directory_path: str):
        self._keys_writer.directory_path = directory_path
        self.directoryPathChanged.emit()

    @pyqtSlot()
    def write_keys(self):
        try:
            self._keys_writer.write_public_key()
            self._keys_writer.write_private_key()
        except Exception as e:
            print(str(e))
