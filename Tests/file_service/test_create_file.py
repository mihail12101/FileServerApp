import os

from FileServerApp.config import FILENAME_LEN, FILE_EXTENSION, DEFAULT_FILE_CONTENT


def test_file_creation(prepare_test_environment, create_file):
    # Tests passed if fixture "create_file" executed without error
    assert True


def test_filename_after_creation(prepare_test_environment, create_file):
    # Assert
    assert create_file.endswith(FILE_EXTENSION)
    assert len(create_file) == FILENAME_LEN + len(FILE_EXTENSION)


def test_filename_content_after_creation(path_to_new_file):
    # Act
    with open(path_to_new_file, "rt") as r_file:
        file_content = r_file.read()

    # Assert
    assert file_content == DEFAULT_FILE_CONTENT
