import hashlib
import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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
        dst_path = os.path.join(self.KEY_DIR, key_filename)

        with open(dst_path, "rb") as key_file:
            session_key = key_file.read()

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        return cipher_aes.decrypt_and_verify(cipher_text, tag)

    def write_chiper_text(self, data, o_file, filename):
        cipher_text, tag, nonce, session_key = self.encrypt(data)
        key_filename = "AES_{}".format(filename)
        dst_path = os.path.join(self.KEY_DIR, key_filename)

        with open(dst_path, "wb") as key_file:
            key_file.write(session_key)

        o_file.write(nonce + tag + cipher_text)

        return key_filename


class RSAChiper(AESCipher):
    pass


class Hasher(object):
    @staticmethod
    def hash_md5(sign_str):
        """Return hash for signature string

        :param sign_str:
        :return: hash in hex
        """
        hash_obj = hashlib.md5(sign_str)
        return hash_obj.digest()


def prepare_signature_str(ordered_signature):
    """Build signature string from OrderedDict with metadata

    :param ordered_signature: OrderedDict with metadata
    :return: string signature
    """
    return "{}_{}_{}_{}".format(ordered_signature.get('name'),
                                ordered_signature.get('create_date'),
                                ordered_signature.get('size'),
                                ordered_signature.get('content'))
