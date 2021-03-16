from FileServerApp.utils import name_param_is_not_none


def test_param_name_is_not_none():
    try:
        name_param_is_not_none(name="Not None")
    except ValueError:
        # Should not raise ValueError if name is not none
        assert False

    # Passed if name is not none
    assert True


def test_param_name_is_none():
    try:
        name_param_is_not_none(name=None)
    except ValueError:
        # Should raise ValueError if name is none
        assert True
        return

    # Failed, should raise ValueError if none
    assert True
