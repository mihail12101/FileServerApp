import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from FileServerApp.config import FILE_EXTENSION
from FileServerApp.crypto.BaseCipher import BaseCipher


class AESCipher(BaseCipher):
    def __init__(self):
        super(AESCipher, self).__init__()

    def encrypt(self, data):
        self.key = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_EAX)
        cipher_text, tag = cipher.encrypt_and_digest(data.encode("utf8"))
        return cipher_text, tag, cipher.nonce, self.key

    def decrypt(self, i_file, key_filename):
        nonce, tag, cipher_text, session_key = super().decrypt(i_file, key_filename)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        return cipher_aes.decrypt_and_verify(cipher_text, tag).decode("utf8")

    def write_chiper_text(self, data, o_file, filename):
        cipher_text, tag, nonce, session_key = self.encrypt(data)
        key_filename = "AES_{}".format(filename)
        dst_path = os.path.join(self.KEY_DIR, key_filename + FILE_EXTENSION)

        with open(dst_path, "wb") as key_file:
            key_file.write(session_key)

        o_file.write(nonce + tag + cipher_text)

        return key_filename
