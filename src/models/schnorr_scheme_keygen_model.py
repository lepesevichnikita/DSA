from PyQt5.QtCore import QObject

from src.schnorr_scheme import SchnorrSchemeKeygen
from .dsa_keygen_model import DSAKeygenModel


class SchnorrSchemeKeygenModel(DSAKeygenModel):

    def __init__(self, parent: QObject):
        super().__init__(parent)
        self._keygen = SchnorrSchemeKeygen()
        print('kek')
