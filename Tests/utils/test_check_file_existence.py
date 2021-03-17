import os

import pytest

from FileServerApp.utils import check_file_existence


def test_file_exist(prepare_test_environment, create_file_module):
    # Act
    check_file_existence(create_file_module)

    # Assert
    assert path == os.path.join(prepare_test_environment, create_file_module)


def test_file_none():
    # Act
    # Should raise ValueError if filename is None
    with pytest.raises(ValueError):
        check_file_existence(None)


def test_file_not_exists():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    # Should raise NameError if file provided, but not exists
    with pytest.raises(NameError):
        check_file_existence(empty_name)
