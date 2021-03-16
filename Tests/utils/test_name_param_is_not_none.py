import pytest

from FileServerApp.utils import merge_filename_with_root, name_param_is_not_none


def test_param_name_is_not_none():
    # If no exceptions was raised - PASS
    name_param_is_not_none(merge_filename_with_root(""))


def test_param_name_is_none():
    # Should raise ValueError if name is none
    with pytest.raises(ValueError):
        name_param_is_not_none(merge_filename_with_root(None))
