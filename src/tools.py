import os
from .models import CombineSource


class Tools(object):
    def __init__(self):
        self._read_contents = bytearray()

    def add_combine_source(self, source):
        if isinstance(source, CombineSource):
            content = source.read()
            self._read_contents.extend(content)

    def export(self, file_path):
        folder_path = os.path.dirname(file_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # write data from self._read_contents to file_path
        with open(file_path, "wb") as file:
            file.write(self._read_contents)
        
