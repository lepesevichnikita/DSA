from sympy import mod_inverse

from src.dsa import DSAKeygen


class SchnorrSchemeKeygen(DSAKeygen):
    DEFAULT_P_LENGTH = 1024
    DEFAULT_Q_LENGTH = 160

    def __init__(self):
        super().__init__(self.DEFAULT_Q_LENGTH, self.DEFAULT_P_LENGTH)

    def _gen_Y(self) -> int:
        p, _, g, _ = self.public_key.to_list()
        x = self.private_key
        y = mod_inverse(pow(g, x, p), p)
        return y
