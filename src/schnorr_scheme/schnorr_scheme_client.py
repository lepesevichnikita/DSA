from src.dsa.dsa_keys_container import DSAKeysContainer

from random import randint


class SchnorrSchemeClient:

    def __init__(self):
        self._keys_container = DSAKeysContainer()
        self._keys_container.keys = keys
        self._x = 0
        self._s = 0
        self._r = 0
        self._e = 0

    @property
    def keys(self) -> list:
        return self._keys_container.keys

    @keys.setter
    def keys(self, keys: list):
        self._keys_container.keys = keys

    @property
    def x(self) -> int:
        return self._x

    def gen_x(self):
        p, q, g, _ = self._keys_container.public_key
        if self._r == 0:
            self.gen_r()
        self._x = pow(g, self._r, p)

    @property
    def r(self) -> int:
        return self._r

    def gen_r(self):
        self._r = randint(0, self._keys_container.q - 1)

    @property
    def s(self) -> list:
        return self._s

    def gen_s(self):
        p, q, g, _ = self._keys_container.public_key
        w = self._keys_container.private_key
        self._s = (self._r + w * self._e) % p

    @property
    def e(self) -> list:
        return self._e

    @x.setter
    def e(self, e: list):
        self._e = e
