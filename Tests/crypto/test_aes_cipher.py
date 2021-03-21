import os

from FileServerApp.config import KEY_FOLDER, DEFAULT_FILE_CONTENT, FILE_EXTENSION


def test_aes(prepare_test_environment, aes_cipher):
    assert aes_cipher.KEY_DIR == os.path.join(prepare_test_environment, KEY_FOLDER)


def test_aes_encrypt(aes_cipher):
    data = DEFAULT_FILE_CONTENT
    params = aes_cipher.encrypt(data)

    assert isinstance(params, tuple)
    assert len(params) == 4


async def test_aes_write_chiper_text_and_decrypt(create_file_function, aes_cipher, loop):
    data = DEFAULT_FILE_CONTENT
    with open(create_file_function.get("file_path"), "wb") as r_file:
        key_filename = aes_cipher.write_chiper_text(data, r_file, create_file_function.get("file_name"))

    key_path = os.path.join(aes_cipher.KEY_DIR, key_filename + FILE_EXTENSION)

    assert os.path.isfile(key_path)

    with open(create_file_function.get("file_path"), "rb") as r_file:
        content = aes_cipher.decrypt(r_file, key_filename)

    assert content == data
