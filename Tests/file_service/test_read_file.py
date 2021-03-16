import pytest

from FileServerApp.config import DEFAULT_FILE_CONTENT
from FileServerApp.file_service import read_file


def test_read_existing_file(create_file_function):
    # Act
    content = read_file(create_file_function)

    # Assert
    assert isinstance(content, str)
    assert content == DEFAULT_FILE_CONTENT


def test_read_none_file():
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        read_file(None)


def test_read_non_existing_file():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Should raise NameError if file provided, but not exists
    with pytest.raises(NameError):
        read_file(empty_name)
