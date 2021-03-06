import pytest


async def test_metadata_type(file_service_signed, create_signed_file_function):
    # Act
    meta = await file_service_signed.get_metadata(create_signed_file_function.get("file_name"))

    # Assert
    assert isinstance(meta, dict)
    for key in ("name", "create_date", "size", "content"):
        assert key in meta


async def test_metadata_none_file_provided(file_service_signed):
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        await file_service_signed.get_metadata(None)


async def test_metadata_provided_file_not_exists(file_service_signed):
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Should raise FileExistsError if file provided, but not exists
    with pytest.raises(FileExistsError):
        await file_service_signed.get_metadata(empty_name)
