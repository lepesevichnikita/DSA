class DSAKeysContainer:
    PRIVATE_KEY_IS_NONE_MESSAGE = 'Private key should be passed'
    PUBLIC_KEY_IS_TOO_SHORT_MESSAGE = 'Public key is too short'
    PUBLIC_KEY_IS_NONE_MESSAGE = 'Public key should be passed'

    def __init__(self):
        self._q = 0
        self._p = 0
        self._g = 0
        self._x = 0
        self._y = 0

    @property
    def keys(self) -> list:
        return [self.public_key, self._x]

    @keys.setter
    def keys(self, keys: list):
        public_key, private_key = keys
        if self._validate_public_key(public_key):
            self.public_key = public_key
        if self._validate_private_key(private_key):
            self.private_key = private_key

    @property
    def public_key(self) -> list:
        return [self._p, self._q, self._g, self._y]

    @public_key.setter
    def public_key(self, public_key: list):
        self._validate_public_key(public_key)
        self._p, self._q, self._g, self._y = public_key

    @property
    def private_key(self) -> int:
        return self._x

    @private_key.setter
    def private_key(self, private_key: int) -> int:
        self._validate_private_key(private_key)
        self._x = private_key

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

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @staticmethod
    def _validate_public_key(public_key: list = None,
                             raise_error: bool = False) -> bool:
        result = True
        if public_key is None:
            result = False
            if raise_error:
                raise ValueError(DSAKeysContainer.PUBLIC_KEY_IS_NONE_MESSAGE)
        if len(public_key) < 3:
            result = False
            if raise_error:
                raise ValueError(
                    DSAKeysContainer.PUBLIC_KEY_IS_TOO_SHORT_MESSAGE)
        return result

    @staticmethod
    def _validate_private_key(private_key: int = None,
                              raise_error: bool = False) -> bool:
        result = True
        if private_key is None or private_key == 0:
            result = False
            if raise_error:
                raise ValueError(DSAKeysContainer.PRIVATE_KEY_IS_NONE_MESSAGE)
        return result

    def validate_private_key(self):
        DSAKeysContainer._validate_private_key(self._x)

    def validate_public_key(self):
        DSAKeysContainer._validate_public_key(self._public_key)

    @property
    def has_public_key(self) -> bool:
        return self.public_key is not None and len(self.public_key) >= 3

    @property
    def has_private_key(self) -> bool:
        return self.private_key is not None and self.private_key >= 3

    @property
    def has_keys(self) -> bool:
        return self.has_public_key & self.has_private_key
