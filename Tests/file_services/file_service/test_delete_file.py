import os

import pytest


async def test_delete_existing_file(file_service, create_file_function):
    # Act
    await file_service.delete_file(create_file_function.get('file_name'))

    # Assert
    assert not os.path.isfile(create_file_function.get("file_path"))


async def test_delete_none_file(file_service):
    # Act
    # Should raise ValueError if name was not provided
    with pytest.raises(ValueError):
        await file_service.delete_file(None)


async def test_delete_non_existing_file(file_service):
    # Arrange
    # Not None name, but not exists
    empty_name = ""

    # Act
    # Assert - if no exceptions - PASS
    await file_service.delete_file(empty_name)
