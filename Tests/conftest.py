import os

import pytest

from FileServerApp import file_service
from FileServerApp.config import ENVVAR_NAME_ROOT


@pytest.fixture(scope="session", autouse=True)
def prepare_test_environment(tmpdir_factory):
    root_dir = os.path.normpath(str(tmpdir_factory.getbasetemp()))
    os.environ[ENVVAR_NAME_ROOT] = root_dir

    return root_dir


@pytest.fixture(scope="module")
def create_file(prepare_test_environment):
    # Act
    filename = file_service.create_file()

    # Assert
    file_path = os.path.join(prepare_test_environment, filename)
    assert os.path.isfile(file_path)

    return filename

@pytest.fixture(scope="module")
def path_to_new_file(prepare_test_environment, create_file):
    return os.path.join(prepare_test_environment, create_file)