from .dsa_base import DSABase
from .dsa_hasher import DSAHasher
from .dsa_keys_container import DSAKeysContainer
from .dsa_sign import DSASign, sign_data


class DSASigner(DSAHasher):
    def __init__(self, sign: DSASign = None,
                 sign_name="",
                 keys_container=DSAKeysContainer()):
        super().__init__(keys_container)
        self._sign = sign
        self._sign_name = sign_name

    @property
    def sign_filename(self) -> str:
        result = self._sign_name if len(self._sign_name) > 0 else self.filename
        result += DSABase.SIGN_EXTESNION
        return result

    @property
    def sign_path(self):
        return self.dirname + '/' + self.sign_filename

    def _get_sign_name(self) -> str:
        return self._sign_name

    def _set_sign_name(self, sign_name: str):
        self._sign_name = sign_name

    sign_name = property(_get_sign_name, _set_sign_name)

    def sign_file(self):
        if self.is_available_for_signing:
            self._sign = sign_data(self.keys_container.public_key,
                                   self.keys_container.private_key,
                                   self.hashed_data,
                                   self.hash_algorithm)

    def write_sign(self):
        self._sign.write_into_file(self.sign_path)

    @property
    def sign(self) -> DSASign:
        return self._sign

    @property
    def has_sign(self) -> bool:
        return self._sign is not None

    @property
    def has_hash_algorithm(self) -> bool:
        return self.hash_algorithm is not None and len(self.hash_algorithm) > 0

    @property
    def is_available_for_signing(self) -> bool:
        return self.has_keys_container & self.has_hashed_data & self.has_hash_algorithm
