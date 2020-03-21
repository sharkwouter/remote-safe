class ApiBase:
    def __init__(self, file_manager=None):
        self._connection = None
        self._file_manager = file_manager

    def connect(self, data):
        raise NotImplementedError("This method was not yet implemented")

    def get_file_list(self) -> dict:
        raise NotImplementedError("This method was not yet implemented")

    def get_file(self, remote_path):
        raise NotImplementedError("This method was not yet implemented")

    def send_file(self, local_path):
        raise NotImplementedError("This method was not yet implemented")
