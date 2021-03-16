import os

from FileServerApp.config import ENVVAR_NAME_ROOT
from FileServerApp.main import main


def test_main(tmpdir, prepare_test_environment):
    path = os.path.normpath(str(tmpdir))
    main(["--src-dir", path])
    assert os.getenv(ENVVAR_NAME_ROOT) == path

    # POST condition
    os.environ[ENVVAR_NAME_ROOT] = prepare_test_environment
