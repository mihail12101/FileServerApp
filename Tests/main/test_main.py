import os
import subprocess

import FileServerApp
from FileServerApp.config import ENVVAR_NAME_ROOT
from FileServerApp.main import main


def test_main(tmpdir, prepare_test_environment):
    path = os.path.normpath(str(tmpdir))
    main(["", "--src-dir", path])
    assert os.getenv(ENVVAR_NAME_ROOT) == path

    # POST condition
    os.environ[ENVVAR_NAME_ROOT] = prepare_test_environment


def test_run_main_module(tmpdir, prepare_test_environment):
    path = os.path.normpath(str(tmpdir))
    main_file = FileServerApp.main.__file__
    subprocess.run(["python3", f"{main_file}", "--src-dir", f"{path}"])
