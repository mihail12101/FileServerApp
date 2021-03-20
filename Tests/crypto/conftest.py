import pytest

from FileServerApp.crypto import BaseCipher


@pytest.fixture(scope="module")
def base_cipher():
    return BaseCipher()