import pytest

from FileServerApp.utils import name_param_is_not_none


def test_param_name_is_not_none():
    # If no exceptions was raised - PASS
    name_param_is_not_none(name="Not None")


def test_param_name_is_none():
    # Should raise ValueError if name is none
    with pytest.raises(ValueError):
        name_param_is_not_none(name=None)
