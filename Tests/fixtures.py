import os
from contextlib import contextmanager

from FileServerApp import file_service


@contextmanager
def create_file(prepare_test_environment):
    # Act
    filename = file_service.create_file()

    # Assert
    file_path = os.path.join(prepare_test_environment, filename)
    assert os.path.isfile(file_path)

    yield filename
    if os.path.isfile(file_path):
        os.remove(file_path)
