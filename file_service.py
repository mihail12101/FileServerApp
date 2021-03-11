import os

from config import WORK_DIRECTORY
from utils import generate_random_file_name


def read_file(name=None):
    root = WORK_DIRECTORY
    dst_path = os.path.join(root, name)

    if os.path.isfile(dst_path):
        with open(dst_path, "rt") as r_file:
            file_content = r_file.read()

    return file_content


def delete_file(name=None):
    root = WORK_DIRECTORY
    dst_path = os.path.join(root, name)

    if os.path.isfile(dst_path):
        os.remove(dst_path)


def create_file():
    root = WORK_DIRECTORY
    file_name = generate_random_file_name()
    dst_path = os.path.join(root, file_name)
    with open(dst_path, "wt") as new_file:
        new_file.write("some text")

    # or return dst_path?
    return file_name


def get_metadata(name=None):
    root = WORK_DIRECTORY
    dst_path = os.path.join(root, name)

