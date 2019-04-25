from .dsa_base import DSABase
from .dsa_keys_container import DSAKeysContainer


class DSAKeysWriter(DSABase):

    def __init__(self,
                 directory_path: str = None,
                 keys_name: str = None,
                 keys_container: DSAKeysContainer = DSAKeysContainer()):
        super().__init__(keys_container)
        self.directory_path = directory_path
        self._keys_name = keys_name

    def _get_keys_name(self) -> str:
        return self._keys_name

    def _set_keys_name(self, keys_name: str):
        self._keys_name = keys_name

    keys_name = property(_get_keys_name, _set_keys_name)

    def _get_directory_path(self) -> str:
        return self._directory_path

    def _set_directory_path(self, directory_path: str):
        self._directory_path = self._end_directory_path_with_slash(
            directory_path)

    directory_path = property(_get_directory_path, _set_directory_path)

    @staticmethod
    def _end_directory_path_with_slash(directory_path: str) -> str:
        result = directory_path
        if directory_path is not None and not directory_path.endswith('/'):
            result += '/'
        return result

    @property
    def public_key_path(self) -> str:
        return self._directory_path + self.keys_name + DSAKeysWriter.PUBLIC_KEY_EXTENSION

    @property
    def private_key_path(self) -> str:
        return self._directory_path + self.keys_name + DSAKeysWriter.PRIVATE_KEY_EXTENSION

    @property
    def public_key(self) -> list:
        return self.keys_container.public_key

    @public_key.setter
    def public_key(self, public_key: list):
        self.keys_container.public_key = public_key

    @property
    def private_key(self) -> int:
        return self.keys_container.private_key

    @private_key.setter
    def private_key(self, private_key):
        self.keys_container.private_key = private_key

    def is_correct_keys_destination(self) -> bool:
        return self.has_directory_path & self.has_keys_name \
               & self.has_keys_container

    def write_public_key(self):
        if self.is_correct_keys_destination() \
                & self.keys_container.has_public_key:
            self._write_all_values_from_public_key()
        return self

    def write_private_key(self):
        if self.is_correct_keys_destination() \
                & self.keys_container.has_private_key:
            with open(self.private_key_path, "wt") as file:
                file.write(hex(self.private_key))
        return self

    @property
    def has_directory_path(self) -> bool:
        return self._directory_path is not None

    @property
    def has_keys_name(self) -> bool:
        return self._keys_name is not None

    def _write_all_values_from_public_key(self):
        with open(self.public_key_path, "wt") as file:
            file.write(" ".join([hex(value) for value in self.public_key]))
