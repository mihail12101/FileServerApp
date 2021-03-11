import argparse
import os

from utils import ENVVAR_ROOT, get_path_from_arg

parser = argparse.ArgumentParser(description='Parse args for FileServerApp')
parser.add_argument("--src-dir", type=get_path_from_arg, help="Working directory", required=True)


def main():
    args = parser.parse_args()
    os.environ[ENVVAR_ROOT] = os.path.normpath(args.src_dir)


if __name__ == "__main__":
    main()
