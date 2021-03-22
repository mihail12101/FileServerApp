import os

from FileServerApp.config import KEY_FOLDER, DEFAULT_FILE_CONTENT, FILE_EXTENSION


def test_rsa(prepare_test_environment, rsa_cipher):
    assert rsa_cipher.KEY_DIR == os.path.join(prepare_test_environment, KEY_FOLDER)


def test_rsa_encrypt(rsa_cipher):
    data = DEFAULT_FILE_CONTENT
    params = rsa_cipher.encrypt(data)

    assert isinstance(params, tuple)
    assert len(params) == 4


async def test_rsa_write_chiper_text_and_decrypt(create_file_function, rsa_cipher, loop):
    data = DEFAULT_FILE_CONTENT
    with open(create_file_function.get("file_path"), "wb") as r_file:
        key_filename = rsa_cipher.write_chiper_text(data, r_file, create_file_function.get("file_name"))

    key_path = os.path.join(rsa_cipher.KEY_DIR, key_filename + FILE_EXTENSION)

    assert os.path.isfile(key_path)

    with open(create_file_function.get("file_path"), "rb") as r_file:
        content = rsa_cipher.decrypt(r_file, key_filename)

    assert content == data
