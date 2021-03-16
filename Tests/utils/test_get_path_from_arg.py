import pytest

from FileServerApp.utils import get_path_from_arg


def test_get_path_from_arg_with_existing_path(prepare_test_environment):
    # Act
    path = get_path_from_arg(prepare_test_environment)

    # Assert
    assert path == prepare_test_environment


def test_get_path_from_arg_with_non_existing_path(prepare_test_environment):
    # Act
    # Should raise NameError if file provided, but not exists
    with pytest.raises(NameError):
        get_path_from_arg("")
