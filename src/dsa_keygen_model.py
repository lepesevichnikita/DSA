from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, QThread, \
    Q_ENUMS
from src.dsa_keygen import DSAKeygen
from src.dsa_keys_container import DSAKeysContainer


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


class DSAKeygenModel(QObject, DSAKeygen):
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
        return self.keys_container.keys

    @keys.setter
    def keys(self, keys: list):
        self.keys_container.keys = keys
        self.keysValueChanged.emit()

    @pyqtProperty(list, notify=keysValueChanged)
    def public_key(self) -> list:
        return self.keys_container.public_key

    @pyqtProperty(int, notify=keysValueChanged)
    def private_key(self) -> int:
        return self.keys_container.private_key

    @pyqtProperty(str, notify=keysValueChanged)
    def p(self):
        return hex(self.keys_container.p)

    @pyqtProperty(str, notify=keysValueChanged)
    def q(self):
        return hex(self.keys_container.q)

    @pyqtProperty(str, notify=keysValueChanged)
    def g(self):
        return hex(self.keys_container.g)

    @pyqtProperty(str, notify=keysValueChanged)
    def y(self):
        return hex(self.keys_container.y)

    @pyqtProperty(str, notify=keysValueChanged)
    def x(self):
        return hex(self.keys_container.x)

    def get_q_length(self) -> int:
        return self._q_length

    def set_q_length(self, q_length: int):
        self._q_length = q_length
        self.qLengthChanged.emit()

    q_length = pyqtProperty(int, fget=get_q_length, fset=set_q_length,
                            notify=pLengthChanged)

    def get_p_length(self) -> int:
        return self._p_length

    def set_p_length(self, value: int):
        self._p_length = value
        self.pLengthChanged.emit()

    p_length = pyqtProperty(int, fget=get_p_length, fset=set_p_length,
                            notify=pLengthChanged)

    @pyqtSlot()
    def async_generate_new_keys(self):
        self._thread.keygen = self
        self._thread.method_name = 'generate_new_keys_with_signal_emit'
        self._thread.start()

    @pyqtSlot()
    def generate_new_keys_with_signal_emit(self):
        try:
            self.generate_new_keys()
            self.keysValueChanged.emit()
        except Exception as e:
            print('Error:', e)

    @pyqtSlot()
    def async_generate_new_x_y(self):
        self._thread.keygen = self
        self._thread.method_name = 'generate_new_x_y_with_signal_emit'
        self._thread.start()

    @pyqtSlot()
    def generate_new_x_y_with_signal_emit(self):
        try:
            self.generate_new_x_y()
            self.keysValueChanged.emit()
        except Exception as e:
            print('Error:', e)
