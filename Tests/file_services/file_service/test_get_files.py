async def test_get_files(create_file_function, file_service):
    files = await file_service.get_files()

    assert isinstance(files, dict)
    assert len(files) == 1
    assert create_file_function.get("file_name") in files

    file_data = files[create_file_function.get("file_name")]
    for key in ("name", "create_date", "size", "content"):
        assert key in file_data
