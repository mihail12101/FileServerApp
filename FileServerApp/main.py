"""Main entry point to work with FileServerApp

Available arguments:
    * --src-dir "path to the directory" - The directory will used for work with files
"""
import argparse
import logging
import os
import sys

from aiohttp import web

from FileServerApp.Handler import Handler
from FileServerApp.config import ENVVAR_NAME_ROOT, LOG_FORMAT, DEFAULT_PORT
from FileServerApp.utils import get_path_from_arg

parser = argparse.ArgumentParser(description='Parse args for FileServerApp')
parser.add_argument("--src-dir", type=get_path_from_arg, help="Working directory", required=True)


def main(args):
    """Wrapper for main function"""
    # Logger
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)

    # Args
    args = parser.parse_args(args=args[1:])

    # Environment
    os.environ[ENVVAR_NAME_ROOT] = os.path.normpath(args.src_dir)

    # Handler
    handler = Handler()

    # Server creation
    app = web.Application()
    app.add_routes([
        web.get("/files/list", handler.get_file_list),
        web.get("/files", handler.get_file_data),
        web.post("/files", handler.create_file),
        web.delete("/files/{file_name}", handler.delete_file),
        web.post("/change_file_dir", handler.change_work_dir)
    ])

    web.run_app(app, port=DEFAULT_PORT)


if __name__ == "__main__":
    main(sys.argv)
