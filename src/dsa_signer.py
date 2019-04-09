from .dsa_base import DSABase
from sympy import mod_inverse
from random import randint


class DSABaseSigner(DSABase):
    def __init__(self, hash_algorithm: str = None):
        super().__init__(hash_algorithm)

    def sign_data(self) -> list:
        self.validate_public_key_and_hash()
        self.validate_private_key()
        p, q, g, y = self.public_key
        x = self.private_key
        k = randint(0, q)
        r = pow(g, k, p) % q
        k_mod_inverse = mod_inverse(k, q)
        s = k_mod_inverse * (self.hashed_data + x * r) % q
        return [r, s]
