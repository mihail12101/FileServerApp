from FileServerApp.config import DEFAULT_FILE_CONTENT
from FileServerApp.file_service import read_file


def test_read_existing_file(create_file_function):
    # Act
    content = read_file(create_file_function)

    # Assert
    assert isinstance(content, str)
    assert content == DEFAULT_FILE_CONTENT


def test_read_none_file():
    # Act
    try:
        read_file(None)
    except ValueError:
        # Should raise ValueError if name was not provided
        assert True
        return

    # Failed in case of not provided filename
    assert False


def test_read_non_existing_file():
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    try:
        read_file(empty_name)
    except NameError:
        # Should raise NameError if file provided, but not exists
        assert True
        return

    # Failed in case of absent of file
    assert False
