import pytest

from FileServerApp.crypto import BaseCipher, AESCipher, RSACipher


@pytest.fixture(scope="module")
def base_cipher():
    return BaseCipher()


@pytest.fixture(scope="module")
def aes_cipher():
    return AESCipher()


@pytest.fixture(scope="module")
def rsa_cipher():
    return RSACipher()
