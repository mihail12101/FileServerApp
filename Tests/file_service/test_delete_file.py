import os

from FileServerApp.file_service import delete_file


def test_delete_existing_file(create_file_function, path_to_new_file_function):
    # Act
    delete_file(create_file_function)

    # Assert
    assert not os.path.isfile(path_to_new_file_function)


def test_delete_none_file():
    # Act
    try:
        delete_file(None)
    except ValueError:
        # Should raise ValueError if name was not provided
        assert True
        return

        # Failed in case of not provided filename
    assert False


def test_delete_not_existing_file():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    try:
        delete_file(empty_name)
    except (NameError, ValueError):
        # Should not raise any exceptions if file not exists
        assert False

    # No exceptions was raised if file not exists
    assert True
