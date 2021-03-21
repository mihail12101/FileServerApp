from FileServerApp.config import FILENAME_LEN
from FileServerApp.utils import generate_random_file_name


def test_random_file_name():
    # Act
    name = generate_random_file_name()

    # Assert
    assert len(name) == FILENAME_LEN
