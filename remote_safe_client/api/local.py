import os
from remote_safe_client.api.api_base import ApiBase
from remote_safe_client.files.directory import Directory


class Local(ApiBase):

    def connect(self, data):

        self._connection = data["path"]
        if not os.path.isdir(self._connection):
            os.makedirs(self._connection)

    def get_file_list(self) -> dict:
        dir_name = os.path.dirname(self._connection)
        base_name = os.path.basename(self._connection)
        return Directory(dir_name, base_name).get_dict()

    def get_file(self, remote_path):
        pass

    def send_file(self, local_path):
        pass