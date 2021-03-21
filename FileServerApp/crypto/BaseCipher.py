import os

from FileServerApp.config import ENVVAR_NAME_ROOT, KEY_FOLDER, FILE_EXTENSION


class BaseCipher:
    """BaseCipher class"""

    def __init__(self):
        self.KEY_DIR = os.path.join(os.getenv(ENVVAR_NAME_ROOT), KEY_FOLDER)
        self.key = None

        if not os.path.isdir(self.KEY_DIR):
            os.mkdir(self.KEY_DIR)

    def encrypt(self, data):
        pass

    def decrypt(self, i_file, key_filename):
        nonce, tag, cipher_text = [i_file.read(x) for x in (16, 16, -1)]
        dst_path = os.path.join(self.KEY_DIR, key_filename + FILE_EXTENSION)

        with open(dst_path, "rb") as key_file:
            session_key = key_file.read()

        return nonce, tag, cipher_text, session_key

    def write_chiper_text(self, data, o_file, filename):
        pass