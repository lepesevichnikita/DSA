import hashlib
from math import log
from os.path import dirname

from .dsa_base import DSABase
from .dsa_keys_container import DSAKeysContainer


class DSAHasher(DSABase):
    DEFAULT_HASH_ALGORITHM = 'sha256'

    def __init__(self, keys_container=DSAKeysContainer(),
                 hash_algorithm: str = DEFAULT_HASH_ALGORITHM,
                 file_path: str = ""):
        super().__init__(keys_container)
        self._hash_algorithm = hash_algorithm
        self._hash = hashlib.new(hash_algorithm)
        self._file_path = file_path

    def calculate_hash_of_file(self, block: int = 2 << 20):
        self.reset_hash()
        with open(self._file_path, "rb") as file:
            data = file.read(block)
            self.update_hash(data)

    @property
    def hash_algorithm(self) -> str:
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm: str = DEFAULT_HASH_ALGORITHM):
        self._hash_algorithm = hash_algorithm

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

    def _get_file_path(self) -> str:
        return self._file_path

    def _set_file_path(self, file_path: str):
        self._file_path = file_path

    file_path = property(_get_file_path, _set_file_path)

    @property
    def dirname(self) -> str:
        return dirname(self._file_path)

    @property
    def filename(self) -> str:
        return self._file_path.replace(self.dirname, "")

    @property
    def has_hashed_data(self) -> bool:
        return self._hash is not None and self._hash.digest_size > 0
