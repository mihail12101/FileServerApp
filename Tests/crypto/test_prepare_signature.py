from FileServerApp.crypto import prepare_signature_str
from FileServerApp.file_service import get_metadata


def test_signature_type(create_file_module):
    meta = get_metadata(create_file_module)
    signature = prepare_signature_str(meta)
    assert isinstance(signature, str)
    assert signature == "{}_{}_{}_{}".format(meta.get('name'),
                                             meta.get('create_date'),
                                             meta.get('size'),
                                             meta.get('content'))
