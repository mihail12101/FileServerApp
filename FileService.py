import os

from utils import ENVVAR_ROOT, generate_random_file_name


def get_working_directory():
    return os.path.normpath(os.getenv(ENVVAR_ROOT))


def read_file(name=None):
    root = get_working_directory()
    dst_path = os.path.join(root, name)

    if os.path.isfile(dst_path):
        with open(dst_path, "rt", encoding="utf-8") as r_file:
            file_content = r_file.read()

    return file_content


def delete_file(name=None):
    root = get_working_directory()
    dst_path = os.path.join(root, name)

    if os.path.isfile(dst_path):
        os.remove(dst_path)
        print(f"\n File: {name} was removed")


def create_file():
    root = get_working_directory()
    file_name = generate_random_file_name()
    dst_path = os.path.join(root, file_name)
    with open(dst_path, "wt", encoding="utf-8") as new_file:
        new_file.write("some text")

    # or return dst_path?
    return file_name


def get_metadata(name=None):
    root = get_working_directory()
    dst_path = os.path.join(root, name)

