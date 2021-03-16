from collections import OrderedDict
from os import stat_result

import pytest

from FileServerApp.file_service import get_metadata


def test_metadata_type(path_to_new_file):
    # Act
    meta = get_metadata(path_to_new_file)

    # Assert
    assert isinstance(meta, OrderedDict)
    for key in ("name", "create_date", "size", "content"):
        assert key in meta


def test_metadata_none_file_provided():
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        get_metadata(None)


def test_metadata_provided_file_not_exists():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Should raise NameError if file provided, but not exists
    with pytest.raises(NameError):
        get_metadata(empty_name)
