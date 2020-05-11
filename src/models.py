import os


class CombineSource(object):
    def __init__(self, path, size=0):
        self._path = path
        self._size = size

    def read(self):
        empty_byte = 0xff
        content_buffer = bytearray()
        temp_content = []

        for _ in range(self._size):
            content_buffer.append(empty_byte)

        content = content_buffer
        if not os.path.exists(self._path):
            return content

        with open(self._path, "rb") as file:
            temp_content.extend(file.read())

        size_diff = self._size - len(temp_content)

        if size_diff > 0:
            start_len =  len(temp_content)
            temp_content.extend(content_buffer[start_len:])
        
        content = temp_content
            
        return content
