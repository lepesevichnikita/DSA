import hashlib
from math import log
from src.dsa.dsa_keys_container import DSAKeysContainer


class DSABase:
    PUBLIC_KEY_EXTENSION = '.dsa_pub'
    PRIVATE_KEY_EXTENSION = '.dsa'
    SIGN_EXTESNION = '.dsa_sign'

    UNEQUAL_LENGTH_OF_HASH_AND_KEY_MESSAGE = 'Binary length of hash and ' \
                                             'Q-part of public key should be ' \
                                             'equal '
    PRIVATE_KEY_IS_NONE_MESSAGE = 'Private key should be passed'
    DEFAULT_HASH_ALGORITHM = 'sha256'

    def __init__(self, keys_container, hash_algorithm: str = DEFAULT_HASH_ALGORITHM):
        self._keys_container = keys_container
        self._hash_algorithm = hash_algorithm
        self._hash = hashlib.new(hash_algorithm)

    def _get_keys_container(self) -> DSAKeysContainer:
        return self._keys_container

    def _set_keys_container(self, keys_container: DSAKeysContainer):
        self._keys_container = keys_container

    keys_container = property(_get_keys_container, _set_keys_container)

    @property
    def hash_digest_size(self) -> int:
        return self._hash.digest_size

    @property
    def is_selected_hash_algorithm_correct(self) -> bool:
        result = False
        if self._keys_container.has_public_key:
            q = self._keys_container.q
            binary_length_of_q = int(log(2, q) + 1)
            result = binary_length_of_q == self.hash_digest_size
        return result

    def update_hash(self, data: bytearray):
        self._hash.update(data)

    def reset_hash(self):
        self._hash = hashlib.new(self._hash_algorithm)

    @property
    def hashed_data(self) -> int:
        return int(self._hash.hexdigest(), 16)

    def validate_public_key_and_hash(self):
        if not self.is_selected_hash_algorithm_correct:
            raise ValueError(DSABase.UNEQUAL_LENGTH_OF_HASH_AND_KEY_MESSAGE)

    def validate_private_key(self):
        self._keys_container.validate_private_key()

    @property
    def has_keys_container(self) -> bool:
        return self._keys_container is not None

