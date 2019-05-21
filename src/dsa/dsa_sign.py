from random import randint

from sympy import mod_inverse

from .dsa_public_key import DSAPublicKey


class DSASign:
    def __init__(self, r: int, s: int, hash_algorithm: str):
        self._r = r
        self._s = s
        self._hash_algorithm = hash_algorithm

    @property
    def hash_algorithm(self) -> str:
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm: str):
        self._hash_algorithm = hash_algorithm

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

    s = property(_get_s, _set_s)

    def is_correct(self, public_key: DSAPublicKey, hashed_data: int) -> bool:
        result = False
        p, q, g, y = public_key.to_list()
        if self._r in range(q) and self._s in range(q):
            w = mod_inverse(self._s, q)
            u1 = (hashed_data * w) % q
            u2 = (self._r * w) % q
            v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
            result = v == self._r
        return v == self._r

    def write_into_file(self, sign_path: str):
        with open(sign_path, "wt") as file:
            file.write(self.hash_algorithm + ' ')
            file.write(" ".join([hex(value) for value in self.as_list]))


def sign_data(public_key: DSAPublicKey, private_key: int,
              hashed_data: int,
              hash_algorithm: str) -> DSASign:
    p, q, g, y = public_key.to_list()
    calc_r = lambda p_, q_, g_, k_: pow(g_, k_, p_) % q_
    calc_s = lambda q_, x_, r_, h_, k_mod_inverse_q_: (k_mod_inverse_q_ * ((h_ + x_ * r_) % q_)) % q
    k = randint(0, q-1)
    r = calc_r(p, q, g, k)
    k_mod_inverse_q = mod_inverse(k, q)
    s = calc_s(q, private_key, r, hashed_data, k_mod_inverse_q)
    return DSASign(r, s, hash_algorithm)


def read_sign_from_file(file_path: str) -> DSASign:
    with open(file_path, "rt") as file:
        data = file.read().split(' ')
        hash_algorithm, *sign_values = data
        r, s = [int(value, 16) for value in sign_values]
        result = DSASign(r, s, hash_algorithm)
    return result
