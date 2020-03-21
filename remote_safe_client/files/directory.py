import os
from typing import List
from remote_safe_client.files.file import File
from remote_safe_client.files.file_base import FileBase
from remote_safe_client.files.file_type import FileType


class Directory(FileBase):
    def __init__(self, directory, name):
        super().__init__(directory, name)

        self.content = self.__get_content()

    def get_path(self):
        return os.path.join(self.directory, self.name)

    def exists(self):
        return os.path.isdir(self.get_path())

    def __get_content(self) -> List:
        content = []
        directory = self.get_path()
        contents = os.listdir(directory)
        for c in contents:
            c_path = os.path.join(directory, c)
            if os.path.isfile(c_path):
                content.append(File(directory, c))
            elif os.path.isdir(c_path):
                content.append(Directory(directory, c))

        return content

    def get_dict(self) -> dict:
        return_dict = {"name": self.name, "type": FileType.DIRECTORY, "contents": []}
        for c in self.content:
            return_dict["contents"].append(c.get_dict())
        return return_dict
