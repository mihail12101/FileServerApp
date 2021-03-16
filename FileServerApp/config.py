"""Config module stores all available constants are used inside the code"""
import logging
from string import ascii_letters, digits

FILENAME_LEN = 10
FILE_EXTENSION = ".txt"
DEFAULT_FILE_CONTENT = "some_text"
ENVVAR_NAME_ROOT = "FILE_SERVER_ROOT"
SYMBOLS = ascii_letters + digits

# Logger
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
