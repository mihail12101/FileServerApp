import pytest

from FileServerApp.config import DEFAULT_FILE_CONTENT


async def test_read_existing_file(file_service_signed, create_signed_file_function):
    # Act
    content = await file_service_signed.read_file(create_signed_file_function.get("file_name"))

    # Assert
    assert isinstance(content, str)
    assert content == DEFAULT_FILE_CONTENT


async def test_read_existing_file_with_wrong_singature(file_service_signed, create_signed_file_function):
    with open(create_signed_file_function.get('file_path'), "a") as cr_file:
        cr_file.write("some_add_text")

    with pytest.raises(PermissionError):
        await file_service_signed.read_file(create_signed_file_function.get("file_name"))


async def test_read_none_file(file_service_signed):
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        await file_service_signed.read_file(None)


async def test_read_non_existing_file(file_service_signed):
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Should raise FileExistsError if file provided, but not exists
    with pytest.raises(FileExistsError):
        await file_service_signed.read_file(empty_name)
