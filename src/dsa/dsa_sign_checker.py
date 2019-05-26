from .dsa_hasher import DSAHasher
from .dsa_sign import DSASign, read_sign_from_file


class DSASignChecker(DSAHasher):
    def __init__(self, sign: DSASign = None, sign_path: str = None):
        super().__init__()
        self._sign = sign
        self._sign_path = sign_path

    @property
    def sign(self) -> DSASign:
        return self._sign

    @sign.setter
    def sign(self, sign: DSASign):
        self._sign = sign
        self.hash_algorithm = self._sign.hash_algorithm

    @property
    def sign_path(self) -> str:
        return self._sign_path

    @sign_path.setter
    def sign_path(self, sign_path: str):
        self._sign_path = sign_path

    def read_sign(self):
        self._sign = read_sign_from_file(self._sign_path)

    @property
    def has_sign(self):
        return self._sign is not None

    @property
    def is_available_for_checking(self) -> bool:
        return self.has_sign & self.has_keys_container & self.has_hashed_data

    @property
    def is_sign_correct(self) -> bool:
        result = False
        if self.is_available_for_checking:
            result = self._sign.is_correct(self.public_key,
                                           self.hashed_data)
        return result
