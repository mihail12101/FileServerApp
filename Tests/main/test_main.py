import os
import subprocess

import pytest
import requests

import FileServerApp
from FileServerApp.config import ENVVAR_NAME_ROOT
from FileServerApp.main import main


@pytest.mark.skip
def test_main(tmpdir, prepare_test_environment, loop):
    path = os.path.normpath(str(tmpdir))
    subprocess.Popen(main, "", "--src-dir", f"{path}")
    assert os.getenv(ENVVAR_NAME_ROOT) == path

    # POST condition
    os.environ[ENVVAR_NAME_ROOT] = prepare_test_environment


def test_run_main_module(tmpdir, prepare_test_environment):
    path = os.path.normpath(str(tmpdir))
    main_file = FileServerApp.main.__file__
    new_proc = subprocess.Popen(["python3", f"{main_file}", "--src-dir", f"{path}"])
    session = requests.Session()
    r = session.get("http://127.0.0.1:8080/files/list")
    assert r.status_code == 400
    new_proc.kill()
