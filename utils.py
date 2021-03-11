import os
import random
from string import ascii_letters, digits

from config import FILENAME_LEN, FILE_EXTENSION


def get_path_from_arg(path):
    if not os.path.isdir(path):
        raise NameError("Directory is not exists")

    return path


def generate_random_file_name():
    return "".join(random.choice(ascii_letters + digits) for _ in range(FILENAME_LEN)) + FILE_EXTENSION
