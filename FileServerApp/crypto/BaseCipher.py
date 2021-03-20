import os

from FileServerApp.config import ENVVAR_NAME_ROOT, KEY_FOLDER


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
        pass

    def write_chiper_text(self, data, o_file, filename):
        pass