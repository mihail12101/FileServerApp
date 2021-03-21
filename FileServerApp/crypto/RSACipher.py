import os

from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA

from FileServerApp.config import SECRET_CODE, RSA_PROTECTION, CERT_EXTENSION, FILE_EXTENSION
from FileServerApp.crypto import AESCipher


class RSACipher(AESCipher):
    """ RSA Cipher class """

    def __init__(self):
        super().__init__()

        self.private_key = None
        self.private_key_path = None

        self.public_key = None
        self.public_key_path = None

        self.generate_public_and_private_keys()

    def encrypt(self, data):
        cipher_text, tag, nonce, session_key = super().encrypt(data)
        cipher_rsa = PKCS1_OAEP.new(self.public_key)
        encrypted_session_key = cipher_rsa.encrypt(session_key)

        return cipher_text, tag, nonce, encrypted_session_key

    def decrypt(self, i_file, key_filename):
        cipher_rsa = PKCS1_OAEP.new(self.private_key)

        nonce, tag, cipher_text, session_key = super(AESCipher, self).decrypt(i_file, key_filename)

        session_key = cipher_rsa.decrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        return cipher_aes.decrypt_and_verify(cipher_text, tag).decode("utf8")

    def write_chiper_text(self, data, o_file, filename):
        cipher_text, tag, nonce, session_key = self.encrypt(data)
        key_filename = f"AES_{filename}"
        session_key_path = os.path.join(self.KEY_DIR, key_filename + FILE_EXTENSION)

        if not os.path.isfile(session_key_path):
            with open(session_key_path, "wb") as s_key_file:
                s_key_file.write(session_key)

        o_file.write(nonce + tag + cipher_text)

        return key_filename

    def generate_public_and_private_keys(self):
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=SECRET_CODE, pkcs=8, protection=RSA_PROTECTION)

        self.private_key_path = os.path.join(self.KEY_DIR, "private_rsa_key" + CERT_EXTENSION)
        self.public_key_path = os.path.join(self.KEY_DIR, "public_rsa_key" + CERT_EXTENSION)

        self.private_key = RSA.importKey(encrypted_key, passphrase=SECRET_CODE)
        if not os.path.isfile(self.private_key_path):
            with open(self.private_key_path, "wb") as pr_key_file:
                pr_key_file.write(encrypted_key)

        pub_key = key.public_key().exportKey()
        self.public_key = RSA.importKey(pub_key)
        if not os.path.isfile(self.public_key_path):
            with open(self.public_key_path, "wb") as pub_key_file:
                pub_key_file.write(pub_key)
