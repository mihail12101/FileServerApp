import os

from utils import generate_random_file_name, merge_filename_with_root, check_file_existence


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


def create_file():
    """Create file with random file name

    Returns string with file name and extension
    """
    file_name = generate_random_file_name()
    dst_path = merge_filename_with_root(file_name)

    with open(dst_path, "wt") as new_file:
        new_file.write("some text")

    return file_name


def get_metadata(name=None):
    """Returns stat object with metadata inside"""
    file_path = check_file_existence(name)
    return os.stat(file_path)
