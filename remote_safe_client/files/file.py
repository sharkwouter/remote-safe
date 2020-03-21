from remote_safe_client.files.file_base import FileBase
from remote_safe_client.files.file_type import FileType


class File(FileBase):
    def get_dict(self) -> dict:
        return {"name": self.name, "type": FileType.FILE}

