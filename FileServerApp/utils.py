"""Module 'utils' contains helper functions

List of available functions:
 * get_path_from_arg
 * generate_random_file_name
 * name_param_is_not_none
 * check_file_existence
 * merge_filename_with_root
"""
import os
import random
from string import ascii_letters, digits

from FileServerApp.config import FILENAME_LEN, FILE_EXTENSION, ENVVAR_NAME_ROOT


def get_path_from_arg(path):
    """Check that path given from argumets is a directory

    :param path: string with <path to a directory>
    :return: <path> if the given directory is exists
    """
    """"""
    if not os.path.isdir(path):
        raise NameError("Given directory is not exists")

    return path


def generate_random_file_name():
    """Generate random file names usign ascii symbols and digits

    :return: string with <file name + file extension>
    """
    return "".join(random.choice(ascii_letters + digits) for _ in range(FILENAME_LEN)) + FILE_EXTENSION


def name_param_is_not_none(name=None):
    """Raise ValueError if given parameter 'name' is none

    :param name: string with <file name + file extension>
    :return: None
    """
    """"""
    if name is None:
        raise ValueError("Parameter - name is absent or has wrong value")


def check_file_existence(name=None):
    """Check for file existence

        * Checks that name param is not None
        * Builds path to provided file
        * Check file existence

    :param name: string with <file name + file extension>
    :return: string with <path to given file>
    """
    file_path = merge_filename_with_root(name)

    if not os.path.isfile(file_path):
        raise NameError("Given file {} not exists in directory {}".format(name, file_path))

    return file_path


def merge_filename_with_root(name=None):
    """Common operations for work with files

        * Check that given file name is not None
        * Getting WORK DIRECTORY from environment variables
        * Concatanate WORK DIRECTORY and filename

    :param name: string with <file name + file extension>
    :return: string with <path to given file>
    """
    name_param_is_not_none(name)
    work_directory = os.path.normpath(os.getenv(ENVVAR_NAME_ROOT))
    return os.path.join(work_directory, name)
