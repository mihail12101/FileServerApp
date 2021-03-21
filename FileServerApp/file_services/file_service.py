import logging
import os

from FileServerApp.config import DEFAULT_FILE_CONTENT
from FileServerApp.config import ENVVAR_NAME_ROOT, FILE_EXTENSION
from FileServerApp.utils import check_file_existence
from FileServerApp.utils import convert_datetime, param_is_not_none
from FileServerApp.utils import generate_random_file_name

logger = logging.getLogger(__name__)


class FileService:
    """Singleton class for insecure work with files

    Has following insecure methods:
        - create_file()
        - read_file(file_path)
        - delete_file(file_path)
        - get_metadata(file_path)
    """
    __instance = None
    __work_dir = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(FileService, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__work_dir:
            return

        self.__work_dir = os.getenv(ENVVAR_NAME_ROOT)

    @property
    def work_dir(self):
        return self.__work_dir

    @param_is_not_none
    async def read_file(self, file_name):
        """Return content from the given file

        :param file_name: string with <file_name>
        :return: string with <file content>
        """
        file_path = os.path.join(self.__work_dir, file_name + FILE_EXTENSION)
        check_file_existence(file_path)

        with open(file_path, "r", encoding="utf8") as r_file:
            content = r_file.read()

        return content

    @param_is_not_none
    async def delete_file(self, file_name):
        """Remove file if exists

        :param file_name: string with <file_name>
        :return: None
        """
        file_path = os.path.join(self.__work_dir, file_name + FILE_EXTENSION)

        if os.path.isfile(file_path):
            os.remove(file_path)
            logger.info("File {} was removed".format(file_path))

    async def create_file(self, content=DEFAULT_FILE_CONTENT):
        """Create file with random file name, encrypt data and save session_key

        :return: string with filename without extension
        """
        file_name = generate_random_file_name()
        file_path = os.path.join(self.__work_dir, file_name + FILE_EXTENSION)

        with open(file_path, "w", encoding="utf8") as new_file:
            new_file.write(content)

        logger.info("File {} was created".format(file_name))

        return file_name

    @param_is_not_none
    async def get_metadata(self, file_name):
        """Return stat object with metadata inside

        :param file_name: string with <file_name>
        :return: dict obejct with metadata
        """
        file_path = os.path.join(self.__work_dir, file_name + FILE_EXTENSION)
        check_file_existence(file_path)

        return {"name": file_name,
                "create_date": convert_datetime(os.path.getctime(file_path)),
                "size": os.path.getsize(file_path),
                "content": await self.read_file(file_name)}

    async def get_files(self):
        files_data = {}

        for file in os.listdir(self.work_dir):
            file_path = os.path.join(self.work_dir, file)

            if not os.path.isfile(file_path) or FILE_EXTENSION not in file:
                continue

            file_name_without_ext = os.path.splitext(file)[0]
            files_data[file_name_without_ext] = await self.get_metadata(file_name_without_ext)

        return files_data

    async def change_work_dir(self, new_directory):
        path = os.path.normpath(new_directory)

        self.__work_dir = path
        os.environ[ENVVAR_NAME_ROOT] = self.__work_dir
