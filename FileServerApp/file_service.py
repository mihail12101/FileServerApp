import logging
import os

from config import DEFAULT_FILE_CONTENT, LOG_LEVEL, LOG_FORMAT
from utils import generate_random_file_name, merge_filename_with_root, check_file_existence

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

    with open(file_path, "rt") as r_file:
        file_content = r_file.read()

    return file_content


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
    """Create file with random file name

    :return: string with <file name + file extension>
    """
    file_name = generate_random_file_name()
    dst_path = merge_filename_with_root(file_name)

    with open(dst_path, "wt") as new_file:
        new_file.write(DEFAULT_FILE_CONTENT)

    logger.info("File {} was created".format(file_name))

    return file_name


def get_metadata(name):
    """Return stat object with metadata inside

    :param name: string with <file name + file extension>
    :return: stat obejct with metadata
    """
    file_path = check_file_existence(name)
    return os.stat(file_path)
