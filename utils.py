import os
import random
from string import ascii_letters, digits

from config import FILENAME_LEN, FILE_EXTENSION, WORK_DIRECTORY


def get_path_from_arg(path):
    if not os.path.isdir(path):
        raise NameError("Directory is not exists")

    return path


def generate_random_file_name():
    return "".join(random.choice(ascii_letters + digits) for _ in range(FILENAME_LEN)) + FILE_EXTENSION


def name_param_is_not_none(name=None):
    if name is None:
        raise ValueError("Parameter - name is absent or has wrong value")


def check_file_existence(name=None):
    """ Check for file existence

    * Checks that name param is not None
    * Builds path to provided file
    * Check file existence

    :param name: file name
    :return: file path
    """
    name_param_is_not_none(name)
    file_path = merge_filename_with_root(name)

    if not os.path.isfile(file_path):
        raise NameError("Given file {} not exists in directory {}".format(name, file_path))

    return file_path


def merge_filename_with_root(name):
    name_param_is_not_none()
    return os.path.join(WORK_DIRECTORY, name)