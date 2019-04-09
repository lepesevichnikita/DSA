from sympy import randprime, isprime
from random import randint, choice
from itertools import islice, count
from src.dsa_keys_container import DSAKeysContainer


class DSAKeygen:
    DEFAULT_Q_LENGTH = 256
    DEFAULT_P_LENGTH = 3072

    def __init__(self, q_length=None, p_length=None):
        self._q_length = q_length if q_length else self.DEFAULT_Q_LENGTH
        self._p_length = p_length if p_length else self.DEFAULT_P_LENGTH
        self._keys_container = DSAKeysContainer()

    def generate_new_keys(self) -> list:
        self._keys_container.q = self._gen_Q()
        self._keys_container.p = self._gen_P()
        self._keys_container.g = self._gen_G()
        self._keys_container.x = self._gen_X()
        self._keys_container.y = self._gen_Y()
        return self.keys

    @property
    def keys_container(self) -> DSAKeysContainer:
        return self._keys_container

    @property
    def _q_range_start(self) -> int:
        start = self.binary_length_start(self._q_length)
        return start

    @property
    def _q_range_end(self) -> int:
        end = DSAKeygen.binary_length_end(self._q_length)
        return end

    @property
    def _p_range_start(self):
        start = DSAKeygen.binary_length_start(self._p_length)
        return start

    @property
    def _p_range_end(self):
        end = DSAKeygen.binary_length_end(self._p_length)
        return end

    def get_q_length(self) -> int:
        return self._q_length

    def set_q_length(self, value: int):
        self._q_length = value

    q_length = property(get_q_length, set_q_length)

    def get_p_length(self):
        return self._p_length

    def set_p_length(self, value):
        self._p_length = value

    p_length = property(get_p_length, set_p_length)

    def _gen_Q(self) -> int:
        q = randprime(self._q_range_start, self._q_range_end)
        return q

    def _gen_P(self) -> int:
        q = self._keys_container.q
        round = q - self._p_range_start % q
        p_range_start = self._p_range_start if round == 0 else self._p_range_start + round
        p = 0
        for x in count(p_range_start, q):
            if x >= self._p_range_end:
                break
            if isprime(x + 1):
                p = x + 1
                break
        return p

    def _gen_G(self):
        p, q, *_ = self._keys_container.public_key
        h = randint(2, p - 1)
        g = pow(h, (p - 1) // q, p)
        return g

    def _gen_X(self):
        return randint(0, self._keys_container.q)

    def _gen_Y(self):
        p, _, g, _ = self._keys_container.public_key
        x = self._keys_container.private_key
        y = pow(g, x, p)
        return y

    @staticmethod
    def binary_length_start(length: int) -> int:
        start = 2 ** (length - 1)
        return start

    @staticmethod
    def binary_length_end(length: int) -> int:
        end = 2 ** length
        return end

    def generate_new_x_y(self):
        self._keys_container.x = self._gen_X()
        self._keys_container.y = self._gen_Y()
