from .dsa_base import DSABase
from .dsa_public_key import DSAPublicKey


class DSAKeysReader(DSABase):
    def __init__(self, public_key_path: str = "",
                 private_key_path: str = ""):
        super().__init__()
        self._public_key_path = public_key_path
        self._private_key_path = private_key_path

    @property
    def public_key_path(self) -> str:
        return self._public_key_path

    @public_key_path.setter
    def public_key_path(self, public_key_path: str):
        self._public_key_path = public_key_path

    @property
    def private_key_path(self) -> str:
        return self._private_key_path

    @private_key_path.setter
    def private_key_path(self, private_key_path: str):
        self._private_key_path = private_key_path

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
