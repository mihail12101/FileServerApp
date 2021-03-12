from os import stat_result

from FileServerApp.file_service import get_metadata


def test_metadata_type(path_to_new_file):
    # Act
    meta = get_metadata(path_to_new_file)

    # Assert
    assert isinstance(meta, stat_result)


def test_metadata_none_file_provided():
    # Act
    try:
        get_metadata(None)
    except ValueError:
        # Should raise ValueError if name was not provided
        assert True
        return

    # Failed in case of not provided filename
    assert False


def test_metadata_provided_file_not_exists():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    try:
        get_metadata(empty_name)
    except NameError:
        # Should raise NameError if file provided, but not exists
        assert True
        return

    # Failed in case of absent of file
    assert False