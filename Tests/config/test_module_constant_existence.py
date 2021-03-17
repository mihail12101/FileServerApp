from FileServerApp import config


def test_config_has_constant_filename_len():
    assert hasattr(config, "FILENAME_LEN")


def test_config_has_constant_file_extension():
    assert hasattr(config, "FILE_EXTENSION")


def test_config_has_constant_envvar_name_root():
    assert hasattr(config, "ENVVAR_NAME_ROOT")


def test_config_has_constant_symbols():
    assert hasattr(config, "SYMBOLS")


def test_config_has_constant_default_file_content():
    assert hasattr(config, "DEFAULT_FILE_CONTENT")


def test_config_has_constant_date_time_format():
    assert hasattr(config, "DATE_TIME_FORMAT")

def test_config_has_constant_log_level():
    assert hasattr(config, "LOG_LEVEL")


def test_config_has_constant_log_format():
    assert hasattr(config, "LOG_FORMAT")