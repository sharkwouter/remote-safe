import os


class FileBase:
    def __init__(self, directory, name):
        self.directory = directory
        self.name = name
        if not self.exists():
            raise FileNotFoundError("{} doesn't exist".format(self.get_path()))

    def get_path(self):
        return os.path.join(self.directory, self.name)

    def exists(self):
        return os.path.isfile(self.get_path())

    def get_dict(self) -> dict:
        raise NotImplementedError()
