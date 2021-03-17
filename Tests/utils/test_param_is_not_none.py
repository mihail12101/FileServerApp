import pytest

from FileServerApp.utils import param_is_not_none


def test_param_is_not_none(file_service):
    # If no exceptions was raised - PASS
    param_is_not_none(file_service.delete_file(""))


def test_param_name_is_none(file_service):
    # Should raise ValueError if name is none
    with pytest.raises(ValueError):
        param_is_not_none(file_service.delete_file(None))
