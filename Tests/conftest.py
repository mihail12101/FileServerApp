import os

import pytest

from FileServerApp.config import ENVVAR_NAME_ROOT
from FileServerApp.file_services.file_service import FileService
from FileServerApp.file_services.file_service_signed import FileServiceSigned
from Tests.fixtures import create_file, create_aes_file

"""Test environment"""


@pytest.fixture(scope="session", autouse=True)
def prepare_test_environment(tmpdir_factory):
    root_dir = os.path.normpath(str(tmpdir_factory.getbasetemp()))
    os.environ[ENVVAR_NAME_ROOT] = root_dir

    return root_dir


"""AES creation fixtures"""


@pytest.fixture(scope="module")
def create_file_aes_module(prepare_test_environment):
    with create_aes_file(**locals()) as new_file:
        yield new_file


"""FileService creation fixtures"""


@pytest.fixture(scope="session")
def file_service(prepare_test_environment):
    return FileService()


@pytest.fixture(scope="module")
def create_file_module(file_service):
    with create_file(file_service) as new_file:
        yield new_file


@pytest.fixture(scope="function")
def create_file_function(file_service):
    with create_file(file_service) as new_file:
        yield new_file


"""FileServiceSigned creation fixtures"""


@pytest.fixture(scope="session")
def file_service_signed(prepare_test_environment):
    return FileServiceSigned()


@pytest.fixture(scope="module")
def create_signed_file_module(file_service_signed):
    with create_file(file_service_signed) as new_file:
        yield new_file


@pytest.fixture(scope="function")
def create_signed_file_function(file_service_signed):
    with create_file(file_service_signed) as new_file:
        yield new_file
