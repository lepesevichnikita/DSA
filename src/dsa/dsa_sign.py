from random import randint
from sympy import mod_inverse


class DSASign:
    def __init__(self, r: int, s: int):
        self._r = r
        self._s = s

    @property
    def as_list(self) -> list:
        return [self._r, self._s]

    def _get_r(self) -> int:
        return self._r

    def _set_r(self, r: int):
        self._r = r

    r = property(_get_r, _set_r)

    def _get_s(self):
        return self._s

    def _set_s(self, s: int):
        self._s = s

    def is_correct(self, public_key: list, hashed_data: int) -> bool:
        p, q, g, y = public_key
        w = pow(self._s, -1, q)
        u1 = (hashed_data * w) % p
        u2 = (self._r * w) % p
        v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
        return v == self._r


def sign_data(public_key: list, private_key: int,
              hashed_data: int) -> DSASign:
    p, q, g, y = public_key
    k = randint(0, q)
    r = pow(g, k, p) % q
    k_mod_inverse = mod_inverse(k, q)
    s = k_mod_inverse * (hashed_data + private_key * r) % q
    return DSASign(s, r)
