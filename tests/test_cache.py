import os

from m3o_py import cache
import pytest

m3o_key = os.getenv('M3O_KEY')
cache = cache.CacheService(token=m3o_key)


@pytest.mark.asyncio
async def test_set():
    assert (await cache.set("test", "100", ttl=3600)).status == "ok"


@pytest.mark.asyncio
async def test_get():
    assert (await cache.get("test")).dict() == {"key": "test", "value": "100", "ttl": "3599"} or {"key": "test",
                                                                                                  "value": "100",
                                                                                                  "ttl": "3598"}


@pytest.mark.asyncio
async def test_decrement():
    assert (await cache.decrement("test", 1)).dict() == {"key": "test", "value": "99"}


@pytest.mark.asyncio
async def test_increment():
    assert (await cache.increment("test", 1)).dict() == {"key": "test", "value": 100}


@pytest.mark.asyncio
async def test_list_key():
    assert "test" in (await cache.list_keys()).keys


@pytest.mark.asyncio
async def test_delete():
    assert (await cache.delete("test")).dict() == {"status": "ok"}
