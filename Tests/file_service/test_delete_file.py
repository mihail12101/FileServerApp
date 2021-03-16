import os

import pytest

from FileServerApp.file_service import delete_file


def test_delete_existing_file(create_file_function, path_to_new_file_function):
    # Act
    delete_file(create_file_function)

    # Assert
    assert not os.path.isfile(path_to_new_file_function)


def test_delete_none_file():
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        delete_file(None)


def test_delete_non_existing_file():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    # Assert - if no exceptions - PASS
    delete_file(empty_name)
