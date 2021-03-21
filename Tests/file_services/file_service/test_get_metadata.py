import pytest


async def test_metadata_type(file_service, create_file_function):
    # Act
    meta = await file_service.get_metadata(create_file_function.get("file_name"))

    # Assert
    assert isinstance(meta, dict)
    for key in ("name", "create_date", "size", "content"):
        assert key in meta


async def test_metadata_none_file_provided(file_service):
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        await file_service.get_metadata(None)


async def test_metadata_provided_file_not_exists(file_service):
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Should raise FileExistsError if file provided, but not exists
    with pytest.raises(FileExistsError):
        await file_service.get_metadata(empty_name)
