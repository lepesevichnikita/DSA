from .dsa_base import DSABase
from .dsa_public_key import DSAPublicKey


class DSAKeysReader(DSABase):
    def __init__(self, public_key_path: str = None,
                 private_key_path: str = None):
        super().__init__()
        if public_key_path is not None:
            self._public_key_path = public_key_path
        if private_key_path is not None:
            self._private_key_path = private_key_path

    def _get_keys(self) -> list:
        return self.keys_container.keys

    def _set_keys(self, keys: list):
        self.keys_container.keys = keys

    keys = property(_get_keys, _set_keys)

    def _get_public_key_path(self) -> str:
        return self._public_key_path

    def _set_public_key_path(self, public_key_path: str):
        self._public_key_path = public_key_path

    public_key_path = property(_get_public_key_path, _set_public_key_path)

    def _get_private_key_path(self):
        return self._private_key_path

    def _set_private_key_path(self, private_key_path: str):
        self._private_key_path = private_key_path

    private_key_path = property(_get_private_key_path, _set_private_key_path)

    def read_public_key(self):
        with open(self._public_key_path, 'r') as file:
            public_key_as_array_of_hex = file.read().split(" ")
            public_key_as_array_of_int = [int(value, 16) for value in
                                          public_key_as_array_of_hex]
            self.keys_container.public_key = DSAPublicKey(
                *public_key_as_array_of_int)
        return self

    def read_private_key(self):
        with open(self._private_key_path, 'r') as file:
            number = file.read()
            self.keys_container.private_key = int(number, 16)
        return self
