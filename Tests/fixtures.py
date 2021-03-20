import os
from contextlib import contextmanager

from FileServerApp.config import FILE_EXTENSION


@contextmanager
def create_file(file_service):
    # Act
    file_name = file_service.create_file()

    # Assert
    file_path = os.path.join(file_service.work_dir, file_name + FILE_EXTENSION)
    assert os.path.isfile(file_path)

    yield {"file_name": file_name,
           "file_path": file_path}

    if os.path.isfile(file_path):
        os.remove(file_path)
