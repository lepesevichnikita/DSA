from .dsa_keys_container import DSAKeysContainer
from .dsa_public_key import DSAPublicKey


class DSABase:
    PUBLIC_KEY_EXTENSION = '.dsa_pub'
    PRIVATE_KEY_EXTENSION = '.dsa'
    SIGN_EXTENSION = '.dsa_sign'

    UNEQUAL_LENGTH_OF_HASH_AND_KEY_MESSAGE = 'Binary length of hash and ' \
                                             'Q-part of public key should be ' \
                                             'equal '
    PRIVATE_KEY_IS_NONE_MESSAGE = 'Private key should be passed'

    def __init__(self):
        self._keys_container = DSAKeysContainer()

    @property
    def keys_container(self) -> DSAKeysContainer:
        return self._keys_container

    @keys_container.setter
    def keys_container(self, keys_container: DSAKeysContainer):
        self._keys_container = keys_container

    @property
    def has_keys_container(self) -> bool:
        return self._keys_container is not None

    @property
    def has_private_key(self) -> bool:
        result = False
        if self.has_keys_container:
            result = self._keys_container.has_private_key
        return result

    @property
    def has_public_key(self) -> bool:
        result = False
        if self.has_keys_container:
            result = self._keys_container.has_public_key
        return result

    @property
    def public_key(self) -> DSAPublicKey:
        result = DSAPublicKey()
        if self.has_keys_container:
            result = self._keys_container.public_key
        return result

    @public_key.setter
    def public_key(self, public_key: DSAPublicKey):
        if self.has_keys_container:
            self._keys_container.public_key = public_key

    @property
    def private_key(self) -> int:
        result = 0
        if self.has_keys_container and self.has_private_key:
            result = self._keys_container.private_key
        return result

    @private_key.setter
    def private_key(self, private_key: int):
        if self.has_keys_container:
            self._keys_container.private_key = private_key

    @property
    def keys(self) -> list:
        result = []
        if self.has_keys_container and self.has_keys:
            result = self.keys_container.keys
        return result

    @keys.setter
    def keys(self, keys: list):
        if self.has_keys_container:
            self.keys_container.keys = keys

    @property
    def has_keys(self) -> bool:
        result = False
        if self.has_keys_container:
            result = self._keys_container.has_keys
        return result
