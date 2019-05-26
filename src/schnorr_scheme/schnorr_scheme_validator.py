from random import randint

from src.dsa import DSABase


class SchnorrSchemeValidator(DSABase):

    def __init__(self):
        super().__init__()
        self._complexity = 3
        self._r = 0
        self._x = 0
        self._s = 0
        self._e = 0

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def complexity(self) -> int:
        return self._complexity

    @complexity.setter
    def complexity(self, complexity: int):
        self._complexity = complexity

    @property
    def r(self) -> int:
        return self._r

    @r.setter
    def r(self, r: int):
        self._r = r

    def gen_e(self):
        self._e = randint(0, (2 ** self._complexity) - 1)

    @property
    def s(self) -> int:
        return self._s

    @s.setter
    def s(self, s: int):
        self._s = s

    @property
    def e(self) -> int:
        return self._e

    @property
    def is_valid(self) -> bool:
        result = False
        pk = self.public_key
        if pk.has_p and pk.has_g and pk.has_y:
            p, _, g, y = pk.to_list()
            test_x = pow(g, self._s, p) * pow(y, self._e, p) % p
            result = self._x == test_x
        return result
