from FileServerApp.file_services.file_service import FileService


def test_fileservice_single_obj(file_service):
    fs_obj = FileService()
    assert fs_obj is file_service
