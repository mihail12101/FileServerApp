import os

import pytest

from FileServerApp.config import ENVVAR_NAME_ROOT


@pytest.fixture(scope="session", autouse=True)
def prepare_test_environment(tmpdir_factory):
    root_dir = os.path.normpath(str(tmpdir_factory.getbasetemp()))
    os.environ[ENVVAR_NAME_ROOT] = root_dir

    return root_dir
