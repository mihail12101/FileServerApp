from FileServerApp import config


def test_config_has_constant_filename_len():
    assert hasattr(config, "FILENAME_LEN")


def test_config_has_constant_file_extension():
    assert hasattr(config, "FILE_EXTENSION")


def test_config_has_constant_envvar_name_root():
    assert hasattr(config, "ENVVAR_NAME_ROOT")


def test_config_has_constant_symbols():
    assert hasattr(config, "SYMBOLS")
