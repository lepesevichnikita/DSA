from random import randint

from src.dsa.dsa_keys_container import DSAKeysContainer


class SchnorrSchemeValidator:

    def __init__(self, public_key:list, complexity: int = 1):
        self._complexity = complexity
        self._r = 0
        self._x = 0
        self._s = 0
        self._e = 0
        self._keys_container = DSAKeysContainer()
        self._keys_container.public_key = public_key

    @property
    def public_key(self) -> list:
        return self._keys_container.public_key

    @public_key.setter
    def public_key(self, public_key: list):
        self._keys_container.public_key = public_key

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
        self._e = randint(0, (2**self._complexity)-1)

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
        p, _, g, y = self.public_key
        return self._x == (pow(g, self._s, p) * pow(y, self._e, p))
