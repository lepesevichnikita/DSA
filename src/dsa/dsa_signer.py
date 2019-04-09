from os.path import dirname, isfile

from .dsa_base import DSABase
from .dsa_sign import DSASign, sign_data
from .dsa_keys_container import DSAKeysContainer


class DSASigner(DSABase):
    def __init__(self, file_path: str = "",
                 sign: DSASign = None,
                 sign_name=""):
        super().__init__(DSAKeysContainer())
        self._file_path = file_path
        self._sign = sign
        self._sign_name = sign_name

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

    def calculate_hash_of_file(self):
        with open(self._file_path, "rb") as file:
            data = file.read()
            self.update_hash(data)

    def sign_file(self):
        self._sign = sign_data(self.keys_container.public_key,
                               self.keys_container.private_key,
                               self.hashed_data)

    def write_sign(self):
        with open(self.sign_path, "wt") as file:
            for value in self._sign.as_list:
                file.write(hex(value))

    @property
    def sign(self) -> DSASign:
        return self._sign

    @property
    def has_sign(self) -> bool:
        return self._sign is not None
