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
from datetime import datetime

from FileServerApp.config import FILENAME_LEN, FILE_EXTENSION, ENVVAR_NAME_ROOT, SYMBOLS, DATE_TIME_FORMAT


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
    return "".join(random.choice(SYMBOLS) for _ in range(FILENAME_LEN)) + FILE_EXTENSION


def name_param_is_not_none(func_to_dec):
    """Raise ValueError if given parameter 'name' is none

    Decorator!

    :param func_to_dec: any called function, string with <file name + file extension>
    :return: decorated function
    """

    def wrapper(arg):
        if arg is None:
            raise ValueError("Parameter - name is absent or has wrong value")

        return func_to_dec(arg)

    return wrapper


@name_param_is_not_none
def merge_filename_with_root(name):
    """Common operations for work with files

        * Check that given file name is not None
        * Getting WORK DIRECTORY from environment variables
        * Concatanate WORK DIRECTORY and filename

    :param name: string with <file name + file extension>
    :return: string with <path to given file>
    """
    work_directory = os.path.normpath(os.getenv(ENVVAR_NAME_ROOT))
    return os.path.join(work_directory, name)


@name_param_is_not_none
def check_file_existence(name):
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


def convert_datetime(timestamp):
    """Convert date and time from timestamp

    :param timestamp: datetime object
    :return:string with date and time in DATE_TIME_FORMAT from config.py
    """
    return datetime.fromtimestamp(timestamp).strftime(DATE_TIME_FORMAT)