"""Config module stores all available constants are used inside the code"""
import logging
from string import ascii_letters, digits


# Environmnet
ENVVAR_NAME_ROOT = "FILE_SERVER_ROOT"

# File Settings
FILE_EXTENSION = ".txt"
FILENAME_LEN = 10
DEFAULT_FILE_CONTENT = "some_text"

# DateTime
DATE_TIME_FORMAT = "%Y.%m.%d %H:%M:%S"

# Crypto
KEY_FOLDER = "Keys"
MD5_PREFIX = "MD5_"
SECRET_CODE = "UBS91LvFzTo8MbIVlI1u"
RSA_PROTECTION = "scryptAndAES128-CBC"
CERT_EXTENSION = ".pem"

# Logger
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Web Server
DEFAULT_PORT = 8080

# Other
SYMBOLS = ascii_letters + digits
