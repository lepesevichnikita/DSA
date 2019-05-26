from .dsa_base import DSABase


class DSAKeysWriter(DSABase):

    def __init__(self,
                 directory_path: str = None,
                 keys_name: str = None):
        super().__init__()
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
        return "%s %s %s" % (
            self._directory_path, self.keys_name, DSABase.PUBLIC_KEY_EXTENSION)

    @property
    def private_key_path(self) -> str:
        return "%s %s %s" % (
            self._directory_path, self.keys_name, DSABase.PRIVATE_KEY_EXTENSION)

    def is_correct_keys_destination(self) -> bool:
        return self.has_directory_path & self.has_keys_name \
               & self.has_keys_container

    def write_public_key(self):
        if self.is_correct_keys_destination() \
                & self.has_public_key:
            self._write_all_values_from_public_key()
        return self

    def write_private_key(self):
        if self.is_correct_keys_destination() and self.has_private_key:
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
            public_key_as_array_of_int = self.public_key.to_list()
            public_key_as_array_of_hex = [hex(value) for value in
                                          public_key_as_array_of_int]
            public_key_as_string = " ".join(public_key_as_array_of_hex)
            file.write(public_key_as_string)
