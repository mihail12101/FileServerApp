import os

import pytest
from aiohttp import web

from FileServerApp.Handler import Handler
from FileServerApp.config import ENVVAR_NAME_ROOT, FILE_EXTENSION
from FileServerApp.file_services import FileService
from FileServerApp.file_services import FileServiceSigned

"""Test environment"""


@pytest.fixture(scope="session", autouse=True)
def prepare_test_environment(tmpdir_factory):
    root_dir = os.path.normpath(str(tmpdir_factory.getbasetemp()))
    os.environ[ENVVAR_NAME_ROOT] = root_dir

    return root_dir


@pytest.fixture
def change_root_dir(prepare_test_environment, tmpdir):
    new_root = str(tmpdir)
    os.environ[ENVVAR_NAME_ROOT] = new_root

    yield new_root

    os.environ[ENVVAR_NAME_ROOT] = prepare_test_environment


""" Web Server """

@pytest.fixture
def client(loop, aiohttp_client):
    handler = Handler()
    app = web.Application()
    app.add_routes([
        web.get("/files/list", handler.get_file_list),
        web.get("/files", handler.get_file_data),
        web.post("/files", handler.create_file),
        web.delete("/files/{file_name}", handler.delete_file),
        web.post("/change_file_dir", handler.change_work_dir)
    ])

    return loop.run_until_complete(aiohttp_client(app)), handler

"""FileService creation fixtures"""


@pytest.fixture(scope="session")
def file_service(prepare_test_environment):
    return FileService()


@pytest.fixture(scope="function")
async def create_file_function(file_service, loop):
    # Act
    file_name = await file_service.create_file()

    # Assert
    file_path = os.path.join(file_service.work_dir, file_name + FILE_EXTENSION)
    assert os.path.isfile(file_path)

    yield {"file_name": file_name,
           "file_path": file_path}

    if os.path.isfile(file_path):
        os.remove(file_path)


"""FileServiceSigned creation fixtures"""


@pytest.fixture(scope="session")
def file_service_signed(prepare_test_environment):
    fs_signed = FileServiceSigned()
    assert os.path.isdir(fs_signed.key_folder)
    return fs_signed


@pytest.fixture(scope="function")
async def create_signed_file_function(file_service_signed, loop):
    # Act
    file_name = await file_service_signed.create_file()

    # Assert
    file_path = os.path.join(file_service_signed.work_dir, file_name + FILE_EXTENSION)
    assert os.path.isfile(file_path)

    yield {"file_name": file_name,
           "file_path": file_path}

    if os.path.isfile(file_path):
        os.remove(file_path)
