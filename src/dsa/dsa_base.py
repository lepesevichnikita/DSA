from .dsa_keys_container import DSAKeysContainer


class DSABase:
    PUBLIC_KEY_EXTENSION = '.dsa_pub'
    PRIVATE_KEY_EXTENSION = '.dsa'
    SIGN_EXTENSION = '.dsa_sign'

    UNEQUAL_LENGTH_OF_HASH_AND_KEY_MESSAGE = 'Binary length of hash and ' \
                                             'Q-part of public key should be ' \
                                             'equal '
    PRIVATE_KEY_IS_NONE_MESSAGE = 'Private key should be passed'

    def __init__(self, keys_container:DSAKeysContainer):
        self._keys_container = keys_container

    def _get_keys_container(self) -> DSAKeysContainer:
        return self._keys_container

    def _set_keys_container(self, keys_container: DSAKeysContainer):
        self._keys_container = keys_container

    keys_container = property(_get_keys_container, _set_keys_container)

    @property
    def has_keys_container(self) -> bool:
        return self._keys_container is not None


