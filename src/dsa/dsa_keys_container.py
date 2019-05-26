from .dsa_public_key import DSAPublicKey


class DSAKeysContainer:
    PRIVATE_KEY_IS_NONE_MESSAGE = 'Private key should be passed'
    HAS_ZERO_VALUES = 'Public key is too short'
    PUBLIC_KEY_IS_NONE_MESSAGE = 'Public key should be passed'

    def __init__(self):
        self._public_key = DSAPublicKey()
        self._x = 0

    @property
    def keys(self) -> list:
        return [self._public_key, self._x]

    @keys.setter
    def keys(self, keys: list):
        public_key, private_key = keys
        if self._validate_public_key(public_key):
            self.public_key = public_key
        if self._validate_private_key(private_key):
            self.private_key = private_key

    @property
    def public_key(self) -> DSAPublicKey:
        return self._public_key

    @public_key.setter
    def public_key(self, public_key: DSAPublicKey):
        self._validate_public_key(public_key)
        self._public_key = public_key

    @property
    def private_key(self) -> int:
        return self._x

    @private_key.setter
    def private_key(self, private_key: int):
        self._validate_private_key(private_key)
        self._x = private_key

    @staticmethod
    def _validate_public_key(public_key: DSAPublicKey = None,
                             raise_error: bool = False) -> bool:
        result = True
        if public_key is None:
            result = False
            if raise_error:
                raise ValueError(DSAKeysContainer.PUBLIC_KEY_IS_NONE_MESSAGE)
        if public_key.has_zero_values:
            result = False
            if raise_error:
                raise ValueError(
                    DSAKeysContainer.HAS_ZERO_VALUES)
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
        DSAKeysContainer._validate_public_key(self.public_key)

    @property
    def has_public_key(self) -> bool:
        return self.public_key is not None and self.public_key.is_full

    @property
    def has_private_key(self) -> bool:
        return self.private_key is not None and self.private_key >= 3

    @property
    def has_keys(self) -> bool:
        return self.has_public_key & self.has_private_key
