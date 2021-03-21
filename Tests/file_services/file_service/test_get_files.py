import os


async def test_get_files(create_file_function, file_service):
    files = await file_service.get_files()

    assert isinstance(files, dict)
    assert len(files) == 1
    assert create_file_function.get("file_name") in files

    file_data = files[create_file_function.get("file_name")]
    for key in ("name", "create_date", "size", "content"):
        assert key in file_data


async def test_skip_files_condition_with_ext(file_service, prepare_test_environment):
    random_file = "21323"
    path = os.path.join(prepare_test_environment, random_file + ".json")

    with open(path, "wb"):
        pass

    files = await file_service.get_files()
    assert random_file not in files


async def test_skip_files_condition_with_dir(file_service, prepare_test_environment):
    random_file = "21323"
    path = os.path.join(file_service.work_dir, random_file)

    os.mkdir(path)

    files = await file_service.get_files()
    assert random_file not in files
