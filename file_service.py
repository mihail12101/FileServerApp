import os

from config import WORK_DIRECTORY
from utils import generate_random_file_name, name_param_is_not_none, merge_filename_with_root


def read_file(name=None):
    name_param_is_not_none(name)

    dst_path = merge_filename_with_root(name)

    if os.path.isfile(dst_path):
        with open(dst_path, "rt") as r_file:
            file_content = r_file.read()

    return file_content


def delete_file(name=None):
    name_param_is_not_none(name)

    dst_path = merge_filename_with_root(name)

    if os.path.isfile(dst_path):
        os.remove(dst_path)


def create_file():
    file_name = generate_random_file_name()
    dst_path = merge_filename_with_root(file_name)

    with open(dst_path, "wt") as new_file:
        new_file.write("some text")

    return file_name


def get_metadata(name=None):
    name_param_is_not_none(name)
    dst_path = merge_filename_with_root(name)

