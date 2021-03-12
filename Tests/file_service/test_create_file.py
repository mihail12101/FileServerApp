import os

import pytest

from FileServerApp import file_service
from FileServerApp.config import FILENAME_LEN, FILE_EXTENSION, DEFAULT_FILE_CONTENT


@pytest.fixture(scope="module")
def create_file(prepare_test_environment):
    # Act
    filename = file_service.create_file()

    # Assert
    file_path = os.path.join(prepare_test_environment, filename)
    assert os.path.isfile(file_path)

    return filename


def test_file_creation(prepare_test_environment, create_file):
    # Tests passed if fixture "create_file" executed without error
    assert True


def test_filename_after_creation(prepare_test_environment, create_file):
    # Assert
    assert create_file.endswith(FILE_EXTENSION)
    assert len(create_file) == FILENAME_LEN + len(FILE_EXTENSION)


def test_filename_content_after_creation(prepare_test_environment, create_file):
    # Arrange
    path = os.path.join(prepare_test_environment, create_file)

    # Act
    with open(path, "rt") as r_file:
        file_content = r_file.read()

    # Assert
    assert file_content == DEFAULT_FILE_CONTENT