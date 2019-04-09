from .dsa_keys_writer import DSAKeysWriter
from .dsa_keys_container import DSAKeysContainer

from PyQt5.QtCore import QObject, pyqtProperty, pyqtSlot, pyqtSignal, QThread


class DSAKeysWriterModel(QObject, DSAKeysWriter):
    keysChanged = pyqtSignal()
    keysNameChanged = pyqtSignal()
    directoryPathChanged = pyqtSignal()
    keysContainerChanged = pyqtSignal()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

    def get_keys_name(self) -> str:
        return self._keys_name

    def set_keys_name(self, keys_name: str):
        self._keys_name = keys_name
        self.keysNameChanged.emit()

    keys_name = pyqtProperty(str, fget=get_keys_name, fset=set_keys_name)

    def get_keys(self) -> list:
        return self.keys_container.keys

    def set_keys(self, keys: list):
        try:
            self.keys_container.keys = keys
        except Exception as e:
            print(e)
        finally:
            self.keysChanged.emit()

    keys = pyqtProperty(list, fget=get_keys, fset=set_keys, notify=keysChanged)

    @pyqtProperty(str, notify=directoryPathChanged)
    def directory_path(self) -> str:
        return self._get_directory_path()

    @directory_path.setter
    def directory_path(self, directory_path: str):
        self._set_directory_path(directory_path)
        self.directoryPathChanged.emit()

    @pyqtSlot()
    def write_keys(self):
        try:
            self.write_public_key()
            self.write_private_key()
        except Exception as e:
            print(str(e))
