import pytest

from FileServerApp.crypto import BaseCipher, AESCipher


@pytest.fixture(scope="module")
def base_cipher():
    return BaseCipher()


@pytest.fixture(scope="module")
def aes_cipher():
    return AESCipher()