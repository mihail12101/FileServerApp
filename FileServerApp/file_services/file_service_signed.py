import logging
import os

from FileServerApp.config import ENVVAR_NAME_ROOT, FILE_EXTENSION, DEFAULT_FILE_CONTENT
from FileServerApp.config import KEY_FOLDER, MD5_PREFIX
from FileServerApp.crypto import Hasher
from FileServerApp.file_services import FileService
from FileServerApp.utils import param_is_not_none, check_file_existence, convert_datetime

logger = logging.getLogger(__name__)


class FileServiceSigned(FileService, Hasher):
    """Singleton class for work with signed files

    Has following methods:
        - create_file()
        - read_file(file_path)
        - delete_file(file_path)
        - get_metadata(file_path)
    """
    __instance = None
    __work_dir = None
    __key_folder = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(FileServiceSigned, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

        if not self.__work_dir:
            self.__work_dir = os.getenv(ENVVAR_NAME_ROOT)

        if not self.__key_folder:
            self.__key_folder = os.path.join(os.getenv(ENVVAR_NAME_ROOT), KEY_FOLDER)

            if not os.path.isdir(self.__key_folder):
                os.mkdir(self.__key_folder)

    @property
    def work_dir(self):
        return self.__work_dir

    @property
    def key_folder(self):
        return self.__key_folder

    @param_is_not_none
    async def read_file(self, file_name):
        """Return content from the given file

        :param file_name: string with <file_name>
        :return: string with <file content>
        """
        content = await super().read_file(file_name)

        # Signing process
        hash_file = MD5_PREFIX + file_name + FILE_EXTENSION
        hash_file_path = os.path.join(self.__key_folder, hash_file)

        # Getting hash
        md5_hash_metadata = await self.get_hash_from_metadata(file_name)
        hash_from_file = self.get_hash_from_file(hash_file_path)

        if hash_from_file != md5_hash_metadata:
            raise PermissionError("Signatures are not match")

        return content

    @param_is_not_none
    async def delete_file(self, file_name):
        """Remove file if exists

        :param file_name: string with <file_name>
        :return: None
        """
        await super().delete_file(file_name)

        # Deletion hash file
        hash_file = MD5_PREFIX + file_name + FILE_EXTENSION
        hash_file_path = os.path.join(self.__key_folder, hash_file)

        if os.path.isfile(hash_file_path):
            os.remove(hash_file_path)
            logger.info("File {} was removed".format(hash_file_path))

    async def create_file(self, content=DEFAULT_FILE_CONTENT):
        """Create file with random file name, encrypt data and save session_key

        :return: string with filename without extension
        """
        file_name = await super().create_file()

        # Signing process
        hash_file = MD5_PREFIX + file_name + FILE_EXTENSION
        file_path = os.path.join(self.__key_folder, hash_file)

        # Getting hash
        md5_hash = await self.get_hash_from_metadata(file_name)

        # Save hash
        self.save_hash(file_path, md5_hash)

        return file_name

    @param_is_not_none
    async def __get_metadata(self, file_name):
        """Return stat object with metadata inside

        :param file_name: string with <file_name>
        :return: dict obejct with metadata
        """
        file_path = os.path.join(self.__work_dir, file_name + FILE_EXTENSION)
        check_file_existence(file_path)

        return {"name": file_name,
                "create_date": convert_datetime(os.path.getctime(file_path)),
                "size": os.path.getsize(file_path),
                "content": await super().read_file(file_name)}

    @param_is_not_none
    async def get_hash_from_metadata(self, file_name):
        meta = await self.__get_metadata(file_name)
        signature = self.prepare_signature_str(meta)
        return self.hash_md5(signature)
