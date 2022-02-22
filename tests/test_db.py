import os

from m3o_py.db import DbService
from m3o_py import GeneralException
import pytest

m3o_key = os.getenv('M3O_KEY')
db = DbService(m3o_key)
table = "default"


@pytest.mark.asyncio
async def test_create():
    db_key = (await db.create(table=table, record={"test": "test", "id": "1"})).dict()["id"]
    assert db_key == "1"
    with pytest.raises(GeneralException):
        await db.create(table=table, record={"test": "test", "id": "1"})


@pytest.mark.asyncio
async def test_read():
    res = (await db.read(query='id == "1"', table=table)).dict()
    assert res["records"][0]["test"] == "test"


@pytest.mark.asyncio
async def test_update():
    await db.update(table=table, data={"test": "update", "id": "1"}, id="1")
    res = (await db.read(query='id == "1"', table=table)).dict()
    assert res["records"][0]["test"] == "update"


@pytest.mark.asyncio
async def test_count():
    assert (await db.count(table=table)) == 1


@pytest.mark.asyncio
async def test_delete():
    await db.delete(table=table, id="1")
    assert (await db.count(table=table)) == 0


@pytest.mark.asyncio
async def test_list_tables():
    res = (await db.list_tables()).tables
    assert [table] in res


@pytest.mark.asyncio
async def test_rename_table():
    await db.rename_table(from_table=table, to="test_table_new")
    assert (await db.list_tables()).tables == ["test_table_new"]


@pytest.mark.asyncio
async def test_drop_table():
    await db.drop_table(table="test_table_new")
    assert (await db.list_tables()).tables == []

# def test_truncate():
#    assert False
