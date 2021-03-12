import os
import random
from string import ascii_letters, digits

from config import FILENAME_LEN, FILE_EXTENSION, ENVVAR_ROOT


def get_path_from_arg(path):
    """Check that path given from argumets is directory"""
    if not os.path.isdir(path):
        raise NameError("Directory is not exists")

    return path


def generate_random_file_name():
    """Generate random file names usign ascii symbols and digits

    Return: string with filename + file extension
    """
    return "".join(random.choice(ascii_letters + digits) for _ in range(FILENAME_LEN)) + FILE_EXTENSION


def name_param_is_not_none(name=None):
    """Check that parameter name is not none"""
    if name is None:
        raise ValueError("Parameter - name is absent or has wrong value")


def check_file_existence(name=None):
    """ Check for file existence

    - Param "name" should contain file name with file extension!

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


def merge_filename_with_root(name=None):
    """Common operations for work with files

    - Param "name" should contain file name with file extension!

    * Check that given filename is not None
    * Getting WORK DIRECTORY from environment variables
    * Concatanate WORK DIRECTORY and filename
    """
    name_param_is_not_none(name)
    work_directory = os.path.normpath(os.getenv(ENVVAR_ROOT))
    return os.path.join(work_directory, name)
