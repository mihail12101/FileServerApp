"""Main entry point to work with FileServerApp

Available arguments:
    * --src-dir "path to the directory" - The directory will used for work with files
"""
import argparse
import os

from config import ENVVAR_ROOT
from utils import get_path_from_arg

parser = argparse.ArgumentParser(description='Parse args for FileServerApp')
parser.add_argument("--src-dir", type=get_path_from_arg, help="Working directory", required=True)


def main():
    """Wrapper for main function"""
    args = parser.parse_args()
    os.environ[ENVVAR_ROOT] = os.path.normpath(args.src_dir)


if __name__ == "__main__":
    main()