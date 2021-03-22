import pytest

from FileServerApp.config import DEFAULT_FILE_CONTENT


async def test_read_existing_file(file_service, create_file_function):
    # Act
    content = await file_service.read_file(create_file_function.get("file_name"))

    # Assert
    assert isinstance(content, str)
    assert content == DEFAULT_FILE_CONTENT


async def test_read_none_file(file_service):
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        await file_service.read_file(None)


async def test_read_non_existing_file(file_service):
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Should raise FileExistsError if file provided, but not exists
    with pytest.raises(FileExistsError):
        await file_service.read_file(empty_name)
