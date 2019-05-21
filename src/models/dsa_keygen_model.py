from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject, QThread

from src.dsa import DSAKeygen, DSAPublicKey


class KeygenThread(QThread):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._keygen = None
        self._method_name = None

    @property
    def keygen(self) -> DSAKeygen:
        return self._keygen

    @keygen.setter
    def keygen(self, keygen: DSAKeygen):
        self._keygen = keygen

    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, method_name: str):
        self._method_name = method_name

    def run(self):
        try:
            method = getattr(self._keygen, self._method_name)
            method()
        except Exception as e:
            print(str(e))


class DSAKeygenModel(QObject):
    GENERATING_STARTED = 'GENERATING_STARTED'
    GENERATING_FINISHED = 'GENERATING_FINISHED'

    keysValueChanged = pyqtSignal()
    keysAsyncGenerate = pyqtSignal()
    pLengthChanged = pyqtSignal()
    qLengthChanged = pyqtSignal()
    stateChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._thread = KeygenThread(parent)
        self._keygen = DSAKeygen()
        self._state = DSAKeygenModel.GENERATING_FINISHED
        self._thread.started.connect(
            lambda: self.setState(DSAKeygenModel.GENERATING_STARTED))
        self._thread.finished.connect(
            lambda: self.setState(DSAKeygenModel.GENERATING_FINISHED))
        self._thread.finished.connect(self.keysValueChanged)

    @pyqtSlot()
    def setState(self, state: str):
        self._state = state
        self.stateChanged.emit()

    @pyqtProperty(str, notify=stateChanged, fset=setState)
    def state(self) -> str:
        return self._state

    @pyqtProperty(list, notify=keysValueChanged)
    def keys(self) -> list:
        return self._keygen.keys_container.keys

    @keys.setter
    def keys(self, keys: list):
        self._keygen.keys_container.keys = keys
        self.keysValueChanged.emit()

    @pyqtProperty(DSAPublicKey, notify=keysValueChanged)
    def public_key(self) -> DSAPublicKey:
        return self._keygen.public_key

    @pyqtProperty(int, notify=keysValueChanged)
    def private_key(self) -> int:
        return self._keygen.private_key


    @pyqtProperty(str, notify=keysValueChanged)
    def p(self):
        return hex(self._keygen.public_key.p)

    @pyqtProperty(str, notify=keysValueChanged)
    def q(self):
        return hex(self._keygen.public_key.q)

    @pyqtProperty(str, notify=keysValueChanged)
    def g(self):
        return hex(self._keygen.public_key.g)

    @pyqtProperty(str, notify=keysValueChanged)
    def y(self):
        return hex(self._keygen.public_key.y)

    @pyqtProperty(str, notify=keysValueChanged)
    def private_key(self):
        return hex(self._keygen.private_key)

    @pyqtProperty(int, notify=qLengthChanged)
    def q_length(self) -> int:
        return self._keygen.q_length

    @q_length.setter
    def q_length(self, q_length: int):
        self._keygen.q_length = q_length
        self.qLengthChanged.emit()

    @pyqtProperty(int, notify=pLengthChanged)
    def p_length(self) -> int:
        return self._keygen.p_length

    @p_length.setter
    def p_length(self, value: int):
        self._keygen.p_length = value
        self.pLengthChanged.emit()

    @pyqtSlot()
    def async_generate_new_keys(self):
        self._thread.keygen = self._keygen
        self._thread.method_name = 'generate_new_keys'
        self._thread.start()

    @pyqtSlot()
    def async_generate_new_x_y(self):
        self._thread.keygen = self._keygen
        self._thread.method_name = 'generate_new_x_y'
        self._thread.start()

