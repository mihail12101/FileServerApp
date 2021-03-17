from FileServerApp.config import FILENAME_LEN, DEFAULT_FILE_CONTENT


def test_file_creation(prepare_test_environment, create_signed_file_module):
    # Tests passed if fixture "create_signed_file_module" executed without error
    assert True


def test_filename_after_creation(prepare_test_environment, create_signed_file_module):
    # Assert
    assert len(create_signed_file_module.get("file_name")) == FILENAME_LEN


def test_filename_content_after_creation(file_service_signed, create_signed_file_module):
    # Act
    content = file_service_signed.read_file(create_signed_file_module.get("file_name"))

    # Assert
    assert content == DEFAULT_FILE_CONTENT
