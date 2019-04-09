from src.dsa.dsa_base import DSABase


class DSABaseSignChecker(DSABase):
    def __init__(self, hash_algorithm: str = None, sign: list = None):
        super().__init__(hash_algorithm)
        self._sign = sign

    @property
    def sign(self) -> list:
        return self._sign

    @sign.setter
    def sign(self, sign: list):
        if len(sign) >= 2:
            self._sign = sign[:2]

    def is_sign_corrupted(self) -> bool:
        self.validate_public_key_and_hash()
