import logging
import os
from collections import OrderedDict

from FileServerApp.config import DEFAULT_FILE_CONTENT, LOG_LEVEL, LOG_FORMAT
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


def read_file(name):
    """Return content from the given file

    :param name: string with <file name + file extension>
    :return: string with <file content>
    """
    file_path = check_file_existence(name)
    aes = AESCipher()

    with open(file_path, "rb") as r_file:
        content = aes.decrypt(r_file, "AES_{}".format(name))

    return content.decode("utf-8")


def delete_file(name):
    """Remove file if exists

    :param name: string with <file name + file extension>
    :return: None
    """
    try:
        file_path = check_file_existence(name)
    except NameError:
        return

    os.remove(file_path)
    logger.info("File {} was removed".format(name))


def create_file():
    """Create file with random file name, encrypt data and save session_key

    :return: filename and key_filename, both with extension
    """
    file_name = generate_random_file_name()
    dst_path = merge_filename_with_root(file_name)
    aes = AESCipher()

    with open(dst_path, "wb") as new_file:
        key_filename = aes.write_chiper_text(DEFAULT_FILE_CONTENT, new_file, file_name)

    logger.info("File {} was created".format(file_name))

    return file_name, key_filename


def get_metadata(name):
    """Return stat object with metadata inside

    :param name: string with <file name + file extension>
    :return: stat obejct with metadata
    """
    file_path = check_file_existence(name)
    return OrderedDict(
        name=name,
        create_date=convert_datetime(os.path.getctime(file_path)),
        size=os.path.getsize(file_path),
        content=read_file(name)
    )
