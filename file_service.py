import os

from utils import generate_random_file_name, name_param_is_not_none, merge_filename_with_root, check_file_existence


def read_file(name=None):
    file_path = check_file_existence(name)

    with open(file_path, "rt") as r_file:
        file_content = r_file.read()

    return file_content


def delete_file(name=None):
    try:
        file_path = check_file_existence(name)
    except NameError:
        return

    os.remove(file_path)


def create_file():
    file_name = generate_random_file_name()
    dst_path = merge_filename_with_root(file_name)

    with open(dst_path, "wt") as new_file:
        new_file.write("some text")

    return file_name


def get_metadata(name=None):
    name_param_is_not_none(name)
    # dst_path = merge_filename_with_root(name)
