import os
from string import ascii_letters, digits

FILENAME_LEN = 10
FILE_EXTENSION = ".txt"
ENVVAR_ROOT = "FILE_SERVER_ROOT"
SYMBOLS = ascii_letters + digits
WORK_DIRECTORY = os.path.normpath(os.getenv(ENVVAR_ROOT))