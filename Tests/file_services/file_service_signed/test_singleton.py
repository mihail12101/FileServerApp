import os

from FileServerApp.file_services.file_service_signed import FileServiceSigned


def test_fileservice_single_obj(file_service_signed):
    fs_obj = FileServiceSigned()
    assert fs_obj is file_service_signed


def test_file_service_signed_creation_keys_directory(change_root_dir):
    # Needed to reset default fields in FileServiceSinged class
    FileServiceSigned._FileServiceSigned__instance = None
    FileServiceSigned._FileService__instance = None

    # Act
    new_fs_signed = FileServiceSigned()

    assert os.path.isdir(new_fs_signed.key_folder)
