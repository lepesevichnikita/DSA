from random import randint

from src.dsa import DSABase


class SchnorrSchemeClient(DSABase):

    def __init__(self):
        super().__init__()
        self._x = 0
        self._s = 0
        self._r = 0
        self._e = 0

    @property
    def x(self) -> int:
        return self._x

    def gen_x(self):
        pk = self.public_key
        if pk.has_p and pk.has_q and pk.has_g:
            p, q, g, _ = self.public_key.to_list()
            if self._r == 0:
                self.gen_r()
            self._x = pow(g, self._r, p)

    @property
    def r(self) -> int:
        return self._r

    def gen_r(self):
        if self.public_key.has_q:
            self._r = randint(0, self.public_key.q - 1)

    @property
    def s(self) -> int:
        return self._s

    def gen_s(self):
        pk = self.public_key
        if pk.has_p and pk.has_q and pk.has_g:
            p, q, g, _ = self.public_key.to_list()
            w = self._keys_container.private_key
            self._s = (self._r + w * self._e) % q

    @property
    def e(self) -> int:
        return self._e

    @e.setter
    def e(self, e: int):
        self._e = e
