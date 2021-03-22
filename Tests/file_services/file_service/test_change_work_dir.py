import os

from FileServerApp.config import ENVVAR_NAME_ROOT


async def test_new_work_dir(tmpdir, file_service, prepare_test_environment):
    # Arrange
    new_path = str(tmpdir)

    # Act
    await file_service.change_work_dir(new_path)

    # Assert
    assert os.getenv(ENVVAR_NAME_ROOT) == new_path

    # Post
    os.environ[ENVVAR_NAME_ROOT] = prepare_test_environment