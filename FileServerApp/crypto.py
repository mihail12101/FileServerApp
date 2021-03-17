import hashlib
import logging
import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from FileServerApp.config import ENVVAR_NAME_ROOT, KEY_FOLDER, LOG_LEVEL, LOG_FORMAT, FILE_EXTENSION

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(LOG_LEVEL)

# create formatter
formatter = logging.Formatter(LOG_FORMAT)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


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


class AESCipher(BaseCipher):
    def __init__(self):
        super(AESCipher, self).__init__()

    def encrypt(self, data):
        self.key = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_EAX)
        cipher_text, tag = cipher.encrypt_and_digest(data.encode("utf8"))
        return cipher_text, tag, cipher.nonce, self.key

    def decrypt(self, i_file, key_filename):
        nonce, tag, cipher_text = [i_file.read(x) for x in (16, 16, -1)]
        dst_path = os.path.join(self.KEY_DIR, key_filename + FILE_EXTENSION)

        with open(dst_path, "rb") as key_file:
            session_key = key_file.read()

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        return cipher_aes.decrypt_and_verify(cipher_text, tag)

    def write_chiper_text(self, data, o_file, filename):
        cipher_text, tag, nonce, session_key = self.encrypt(data)
        key_filename = "AES_{}".format(filename)
        dst_path = os.path.join(self.KEY_DIR, key_filename + FILE_EXTENSION)

        with open(dst_path, "wb") as key_file:
            key_file.write(session_key)

        o_file.write(nonce + tag + cipher_text)

        return key_filename


class RSAChiper(AESCipher):
    pass


class Hasher:
    @staticmethod
    def hash_md5(sign_str):
        """Return hash for signature string

        :param sign_str:
        :return: hash in hex
        """
        hash_obj = hashlib.md5(sign_str.encode())
        return hash_obj.digest()

    @staticmethod
    def save_hash(save_path, md5_hash):
        with open(save_path, "wb") as new_file:
            new_file.write(md5_hash)

        logger.info("File {} was created".format(save_path))

    @staticmethod
    def get_hash_from_file(hash_file_path):
        with open(hash_file_path, "rb") as new_file:
            return new_file.read()

    @staticmethod
    def prepare_signature_str(ordered_signature):
        """Build signature string from OrderedDict with metadata

        :param ordered_signature: OrderedDict with metadata
        :return: string signature
        """
        return "{}_{}_{}_{}".format(ordered_signature.get('name'),
                                    ordered_signature.get('create_date'),
                                    ordered_signature.get('size'),
                                    ordered_signature.get('content'))
