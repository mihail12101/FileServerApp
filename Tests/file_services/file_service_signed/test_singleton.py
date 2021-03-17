import os

from FileServerApp.file_services.file_service_signed import FileServiceSigned


def test_fileservice_single_obj(file_service_signed):
    fs_obj = FileServiceSigned()
    assert fs_obj is file_service_signed

def test_file_service_signed_creation_keys_directory(file_service_signed):
    file_service_signed.__work_dir = None

    fss_obj = FileServiceSigned()
    assert os.path.isdir(fss_obj.key_folder)