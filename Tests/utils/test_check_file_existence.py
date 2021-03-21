import pytest

from FileServerApp.utils import check_file_existence


def test_file_exist(prepare_test_environment, create_file_function):
    # Assertion, if no exeption - PASS
    check_file_existence(create_file_function.get("file_path"))


def test_file_none():
    # Act
    # Should raise TypeError if filename is None
    with pytest.raises(TypeError):
        check_file_existence(None)


def test_file_not_exists():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    # Should raise FileExistsError if file provided, but not exists
    with pytest.raises(FileExistsError):
        check_file_existence(empty_name)
