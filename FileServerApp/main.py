"""Main entry point to work with FileServerApp

Available arguments:
    * --src-dir "path to the directory" - The directory will used for work with files
"""
import argparse
import logging
import os
import sys

from FileServerApp.config import ENVVAR_NAME_ROOT, LOG_FORMAT
from FileServerApp.utils import get_path_from_arg

parser = argparse.ArgumentParser(description='Parse args for FileServerApp')
parser.add_argument("--src-dir", type=get_path_from_arg, help="Working directory", required=True)


def main(args):
    """Wrapper for main function"""
    # Logger
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

    args = parser.parse_args(args=args[1:])
    os.environ[ENVVAR_NAME_ROOT] = os.path.normpath(args.src_dir)


if __name__ == "__main__":
    main(sys.argv)
