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

from FileServerApp.config import FILENAME_LEN, FILE_EXTENSION, SYMBOLS, DATE_TIME_FORMAT


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
    return "".join(random.choice(SYMBOLS) for _ in range(FILENAME_LEN))


def param_is_not_none(func_to_dec):
    """Raise ValueError if given parameter 'name' is none, Decorator!

    :param func_to_dec: any called function
    :return: decorated function
    """

    def wrapper(*arg):
        # 0 is class obj, 1 is argument
        if arg[1] is None:
            raise ValueError("Parameter - name is absent or has wrong value")

        return func_to_dec(arg[0], arg[1])

    return wrapper


def check_file_existence(file_path):
    """Raise FileExistsError if given path not exists

    :param file_path: string with file_path
    """

    if not os.path.isfile(file_path):
        raise FileExistsError("Given file path {} not exists".format(file_path))


def convert_datetime(timestamp):
    """Convert date and time from timestamp

    :param timestamp: datetime object
    :return:string with date and time in DATE_TIME_FORMAT from config.py
    """
    return datetime.fromtimestamp(timestamp).strftime(DATE_TIME_FORMAT)
