import json


async def test_get_file_list(client):
    client, handler = tuple(client)
    r = await client.get("/files/list")
    assert r.status == 200


async def test_create_file_correct(client):
    client, handler = tuple(client)

    r = await client.post("/files", json={"content": "new_content"})
    assert r.status == 200


async def test_create_file_not_correct(client):
    client, handler = tuple(client)

    r = await client.post("/files", data={"content": "new_content"})
    assert r.status == 400


async def test_change_file_dir_correct_key(client, tmpdir):
    client, handler = tuple(client)

    r = await client.post("/change_file_dir", json={"new_path": f"{tmpdir}"})
    assert r.status == 200


async def test_change_file_dir_wrong_key(client, tmpdir):
    client, handler = tuple(client)

    r = await client.post("/change_file_dir", json={"wrong_key": f"{tmpdir}"})
    assert r.status == 400


async def test_get_file_data_correct(client):
    client, handler = tuple(client)

    r = await client.post("/files", json={"content": "new_content"})
    assert r.status == 200

    r = await r.text()
    r = json.loads(r)
    create_file_name = r.get("data").get("name")

    r = await client.get(f"/files?file_name={create_file_name}")
    assert r.status == 200


async def test_get_file_data_not_correct(client):
    client, handler = tuple(client)

    r = await client.get(f"/files?file_name=not_existing_file")
    assert r.status == 400


async def test_delete_file_correct(client):
    client, handler = tuple(client)

    r = await client.post("/files", json={"content": "new_content"})
    assert r.status == 200

    r = await r.text()
    r = json.loads(r)
    create_file_name = r.get("data").get("name")

    r = await client.delete(f"/files/{create_file_name}")
    assert r.status == 200
