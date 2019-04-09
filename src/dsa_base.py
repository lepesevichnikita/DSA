import hashlib
from math import log


class DSABase:
    UNEQUAL_LENGTH_OF_HASH_AND_KEY_MESSAGE = 'Binary length of hash and ' \
                                             'Q-part of public key should be ' \
                                             'equal '
    PRIVATE_KEY_IS_NONE_MESSAGE = 'Private key should be passed'
    DEFAULT_HASH_ALGORITHM = 'sha256'

    def __init__(self, hash_algorithm: str = DEFAULT_HASH_ALGORITHM):
        self._public_key = []
        self._private_key = 0
        self._hash_algorithm = hash_algorithm
        self._hash = hashlib.new(hash_algorithm)

    @property
    def hash_digest_size(self) -> int:
        return self._hash.digest_size

    @property
    def is_selected_hash_algorithm_correct(self) -> bool:
        result = False
        if self.has_public_key:
            q_part_of_public_key, *_ = self._public_key
            binary_length_of_q_part_of_public_key = int(
                log(2, q_part_of_public_key) + 1)
            result = binary_length_of_q_part_of_public_key == self.hash_digest_size
        return result

    @property
    def public_key(self) -> list:
        return self._public_key

    @public_key.setter
    def public_key(self, public_key: list):
        if len(public_key) >= 3:
            self._public_key = public_key[:3]

    @property
    def private_key(self) -> int:
        return self._private_key

    @private_key.setter
    def private_key(self, private_key: int):
        self._private_key = private_key

    def update_data(self, data: str):
        self._hash.update(data.encode('UTF-8'))

    def reset_hash(self):
        self._hash = hashlib.new(self._hash_algorithm)

    @property
    def hashed_data(self) -> int:
        return int(self._hash.hexidigest(), 16)

    def validate_public_key_and_hash(self):
        if not self.is_selected_hash_algorithm_correct:
            raise ValueError(DSABase.UNEQUAL_LENGTH_OF_HASH_AND_KEY_MESSAGE)

    def validate_private_key(self):
        if not self.has_private_key:
            raise ValueError(DSABase.PRIVATE_KEY_IS_NONE)

    @property
    def has_public_key(self) -> bool:
        return self._public_key is not None and len(self._public_key) >= 3

    @property
    def has_private_key(self) -> bool:
        return self._private_key is not None and self._private_key > 0
