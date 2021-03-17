from FileServerApp.config import FILENAME_LEN, FILE_EXTENSION, DEFAULT_FILE_CONTENT
from FileServerApp.file_service import read_file


def test_file_creation(prepare_test_environment, create_file_module):
    # Tests passed if fixture "create_file_module" executed without error
    assert True


def test_filename_after_creation(prepare_test_environment, create_file_module):
    # Assert
    assert create_file_module.endswith(FILE_EXTENSION)
    assert len(create_file_module) == FILENAME_LEN + len(FILE_EXTENSION)


def test_filename_content_after_creation(prepare_test_environment, path_to_new_file, create_file_module):
    # Act
    content = read_file(create_file_module)

    # Assert
    assert content == DEFAULT_FILE_CONTENT
