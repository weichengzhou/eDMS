
import os
from typing import List

from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

from .exception import FileExtensionNotAllowed, FileSizeTooBig

@deconstructible
class FileExtensionValidator:

    _allowed_extensions: List[str] = []

    def __init__(self, allowed_extensions: List[str]):
        """
        :param allowed_extensions:
            允許的檔案副檔名, 大小寫皆會被轉成小寫比對
            e.g. [.csv, .pdf, .doc]
        """
        for allowed_extension in allowed_extensions:
            self._allowed_extensions.append(allowed_extension.lower())
    

    def __call__(self, value):
        file_extension: str = os.path.splitext(value.name)[1]
        is_allowed: bool = file_extension.lower() in self._allowed_extensions
        if not is_allowed:
            raise FileExtensionNotAllowed('不支援檔案格式，請選擇 %s 等檔案格式'
                % self._allowed_extensions)


@deconstructible
class FileSizeValidator:

    _max_size: int

    def __init__(self, max_size: int):
        self._max_size = max_size
    

    def __call__(self, value):
        if value.size > self._max_size:
            raise FileSizeTooBig('檔案大小超過 %s' % self._max_size)