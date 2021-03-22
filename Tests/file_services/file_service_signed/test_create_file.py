from FileServerApp.config import FILENAME_LEN, DEFAULT_FILE_CONTENT


async def test_file_creation(prepare_test_environment, create_signed_file_function):
    # Tests passed if fixture "create_signed_file_module" executed without error
    assert True


async def test_filename_after_creation(prepare_test_environment, create_signed_file_function):
    # Assert
    assert len(create_signed_file_function.get("file_name")) == FILENAME_LEN


async def test_filename_content_after_creation(file_service_signed, create_signed_file_function):
    # Act
    content = await file_service_signed.read_file(create_signed_file_function.get("file_name"))

    # Assert
    assert content == DEFAULT_FILE_CONTENT
