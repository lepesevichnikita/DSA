from itertools import count
from random import randint

from sympy import isprime, randprime

from .dsa_base import DSABase


class DSAKeygen(DSABase):
    DEFAULT_Q_LENGTH = 256
    DEFAULT_P_LENGTH = 3072

    def __init__(self, q_length=DEFAULT_Q_LENGTH, p_length=DEFAULT_P_LENGTH):
        super().__init__()
        self._q_length = q_length
        self._p_length = p_length

    def generate_new_keys(self) -> list:
        self.public_key.q = self._gen_Q()
        self.public_key.p = self._gen_P()
        self.public_key.g = self._gen_G()
        self.private_key = self._gen_X()
        self.public_key.y = self._gen_Y()
        return self.keys_container.keys

    @property
    def _q_range_start(self) -> int:
        start = self.binary_length_start(self._q_length)
        return start

    @property
    def _q_range_end(self) -> int:
        end = DSAKeygen.binary_length_end(self._q_length)
        return end

    @property
    def _p_range_start(self) -> int:
        start = DSAKeygen.binary_length_start(self._p_length)
        return start

    @property
    def _p_range_end(self) -> int:
        end = DSAKeygen.binary_length_end(self._p_length)
        return end

    @property
    def q_length(self) -> int:
        return self._q_length

    @q_length.setter
    def q_length(self, value: int):
        self._q_length = value

    @property
    def p_length(self):
        return self._p_length

    @p_length.setter
    def p_length(self, value):
        self._p_length = value

    def _gen_Q(self) -> int:
        q = randprime(self._q_range_start, self._q_range_end)
        return q

    def _gen_P(self) -> int:
        q = self.public_key.q
        round_to_next_divider = q - self._p_range_start % q
        p_range_start = self._p_range_start if round_to_next_divider == 0 \
            else self._p_range_start + round_to_next_divider
        p = 0
        for x in count(p_range_start, q):
            if x >= self._p_range_end:
                break
            if isprime(x + 1):
                p = x + 1
                break
        return p

    def _gen_G(self):
        p, q, *_ = self.public_key.to_list()

        def calculate_g(p_, q_, h_):
            return pow(h_, (p_ - 1) // q_, p_)

        h = randint(2, p - 2)
        g = calculate_g(p, q, h)

        while g == 1:
            h = randint(2, p - 2)
            g = calculate_g(p, q, h)
        return g

    def _gen_X(self):
        return randint(1, self.public_key.q - 1)

    def _gen_Y(self):
        p, _, g, _ = self.public_key.to_list()
        x = self.private_key
        y = pow(g, x, p)
        return y

    @staticmethod
    def binary_length_start(length: int) -> int:
        start = 2 ** (length - 1)
        return start

    @staticmethod
    def binary_length_end(length: int) -> int:
        end = (2 ** length) - 1
        return end

    def generate_new_x_y(self):
        self.private_key = self._gen_X()
        self.public_key.y = self._gen_Y()
