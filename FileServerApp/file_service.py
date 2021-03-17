import logging
import os

from FileServerApp.config import DEFAULT_FILE_CONTENT, LOG_LEVEL, LOG_FORMAT, ENVVAR_NAME_ROOT, FILE_EXTENSION
from FileServerApp.crypto import AESCipher
from FileServerApp.utils import generate_random_file_name, check_file_existence, convert_datetime

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


def read_file(file_name):
    """Return content from the given file

    :param file_name: string with <file name>
    :return: string with <file content>
    """
    file_path = os.path.join(os.getenv(ENVVAR_NAME_ROOT), file_name + FILE_EXTENSION)
    check_file_existence(file_path)
    aes = AESCipher()

    with open(file_path, "rb") as r_file:
        content = aes.decrypt(r_file, "AES_{}".format(file_name))

    return content.decode("utf-8")


def delete_file(file_name):
    """Remove file if exists

    :param file_name: string with <file name + file extension>
    :return: None
    """
    file_path = os.path.join(os.getenv(ENVVAR_NAME_ROOT), file_name + FILE_EXTENSION)
    if os.path.isfile(file_path):
        os.remove(file_path)
        logger.info("File {} was removed".format(file_name))


def create_file():
    """Create file with random file name, encrypt data and save session_key

    :return: filename and key_filename, both with extension
    """
    file_name = generate_random_file_name()
    file_path = os.path.join(os.getenv(ENVVAR_NAME_ROOT), file_name + FILE_EXTENSION)
    aes = AESCipher()

    with open(file_path, "wb") as new_file:
        key_filename = aes.write_chiper_text(DEFAULT_FILE_CONTENT, new_file, file_name)

    logger.info("File {} was created".format(file_name))

    return file_name, key_filename


def get_metadata(file_name):
    """Return stat object with metadata inside

    :param file_name: string with <file name + file extension>
    :return: stat obejct with metadata
    """
    file_path = os.path.join(os.getenv(ENVVAR_NAME_ROOT), file_name + FILE_EXTENSION)
    check_file_existence(file_path)

    return {"name": file_name,
            "create_date": convert_datetime(os.path.getctime(file_path)),
            "size": os.path.getsize(file_path),
            "content": read_file(file_name)}
