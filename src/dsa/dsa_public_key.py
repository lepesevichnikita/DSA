class DSAPublicKey:
    def __init__(self, p: int = 0, q: int = 0, g: int = 0, y: int = 0):
        self._p = p
        self._q = q
        self._g = g
        self._y = y

    @property
    def p(self) -> int:
        return self._p

    @p.setter
    def p(self, p: int):
        self._p = p

    @property
    def q(self) -> int:
        return self._q

    @q.setter
    def q(self, q: int):
        self._q = q

    @property
    def g(self) -> int:
        return self._g

    @g.setter
    def g(self, g: int):
        self._g = g

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y

    def to_list(self) -> list:
        return [self._p, self._q, self._g, self._y]

    @property
    def is_empty(self) -> bool:
        return all(map(lambda num: num == 0, self.to_list()))

    @property
    def is_full(self) -> bool:
        return all(map(lambda num: num != 0, self.to_list()))

    @property
    def has_non_zero_values(self) -> bool:
        return not self.is_empty

    @property
    def has_zero_values(self) -> bool:
        return not self.is_full

    @property
    def has_q(self) -> bool:
        result = self._q > 0
        return result

    @property
    def has_p(self) -> bool:
        result = self._p > 0
        return result

    @property
    def has_g(self) -> bool:
        result = self._g > 0
        return result

    @property
    def has_y(self) -> bool:
        result = self._y > 0
        return result
