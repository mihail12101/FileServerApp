from FileServerApp.crypto import prepare_signature_str
from FileServerApp.file_service import get_metadata


class BaseChiper:
    """BaseChiper class"""

    def __init__(self):
        pass

    def encrypt(self, data):
        pass

    def decrypt(self, date):
        pass

    def write_chiper_text(self, data):
        pass



def test_signature_type(create_file_module):
    meta = get_metadata(create_file_module)
    signature = prepare_signature_str(meta)
    assert isinstance(signature, str)
    assert signature == "{}_{}_{}_{}".format(meta.get('name'),
                                             meta.get('create_date'),
                                             meta.get('size'),
                                             meta.get('content'))
