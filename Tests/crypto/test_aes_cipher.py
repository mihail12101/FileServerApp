import os

from FileServerApp.config import KEY_FOLDER
from FileServerApp.crypto import AESCipher


def test_aes(prepare_test_environment):
    aes = AESCipher()
    assert aes.KEY_DIR == os.path.join(prepare_test_environment, KEY_FOLDER)

