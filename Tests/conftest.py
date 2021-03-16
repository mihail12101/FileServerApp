import os

import pytest

from FileServerApp.config import ENVVAR_NAME_ROOT
from Tests.fixtures import create_file

"""Test environment"""


@pytest.fixture(scope="session", autouse=True)
def prepare_test_environment(tmpdir_factory):
    root_dir = os.path.normpath(str(tmpdir_factory.getbasetemp()))
    os.environ[ENVVAR_NAME_ROOT] = root_dir

    return root_dir


"""File creation fixtures"""


@pytest.fixture(scope="module")
def create_file_module(prepare_test_environment):
    with create_file(**locals()) as new_file:
        yield new_file


@pytest.fixture(scope="function")
def create_file_function(prepare_test_environment):
    with create_file(**locals()) as new_file:
        yield new_file


@pytest.fixture(scope="module")
def path_to_new_file(prepare_test_environment, create_file_module):
    return os.path.join(prepare_test_environment, create_file_module)


@pytest.fixture(scope="function")
def path_to_new_file_function(prepare_test_environment, create_file_function):
    return os.path.join(prepare_test_environment, create_file_function)
