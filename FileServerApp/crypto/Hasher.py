import hashlib
import logging

logger = logging.getLogger(__name__)


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
