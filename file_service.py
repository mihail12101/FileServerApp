import logging
import os

from utils import generate_random_file_name, merge_filename_with_root, check_file_existence

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def read_file(name=None):
    """Returns content from given file

    - Param "name" should contain file name with file extension

    """
    file_path = check_file_existence(name)

    with open(file_path, "rt") as r_file:
        file_content = r_file.read()

    return file_content


def delete_file(name=None):
    """Remove file if exists

    - Param "name" should contain file name with file extension
    """
    try:
        file_path = check_file_existence(name)
    except NameError:
        return

    os.remove(file_path)
    logger.info("File {} was removed".format(name))


def create_file():
    """Create file with random file name

    Returns string with file name and extension
    """
    file_name = generate_random_file_name()
    dst_path = merge_filename_with_root(file_name)

    with open(dst_path, "wt") as new_file:
        new_file.write("some text")

    logger.info("File {} was created".format(file_name))

    return file_name


def get_metadata(name=None):
    """Returns stat object with metadata inside"""
    file_path = check_file_existence(name)
    return os.stat(file_path)
