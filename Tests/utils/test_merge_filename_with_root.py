import os

from FileServerApp.utils import merge_filename_with_root


def test_file_exists(prepare_test_environment, create_file_module):
    path = merge_filename_with_root(create_file_module)

    assert path == os.path.join(prepare_test_environment, create_file_module)


def test_file_none():
    # Act
    try:
        merge_filename_with_root(None)
    except ValueError:
        # Should raise ValueError if name was not provided
        assert True
        return

    # Failed in case of not provided filename
    assert False


def test_file_not_exists(prepare_test_environment):
    # Arrange
    # Not None name, but not exists
    empty_name = "test_test"

    # Act
    path = merge_filename_with_root(empty_name)

    # Assert
    assert path == os.path.join(prepare_test_environment, empty_name)


