import os

from FileServerApp.utils import check_file_existence


def test_file_exist(prepare_test_environment, create_file_module):
    # Act
    path = check_file_existence(create_file_module)

    # Assert
    assert path == os.path.join(prepare_test_environment, create_file_module)


def test_file_none():
    # Act
    try:
        check_file_existence(None)
    except ValueError:
        # Should raise ValueError if name is none
        assert True
        return

    # Failed, should raise ValueError if none
    assert True


def test_file_not_exists():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    try:
        check_file_existence(empty_name)
    except NameError:
        # Should raise NameError if file provided, but not exists
        assert True
        return

    # Failed in case of absent of file
    assert True

