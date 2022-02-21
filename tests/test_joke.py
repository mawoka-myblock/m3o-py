import os

from m3o_py.joke import JokeService
from m3o_py import GeneralException
import pytest

m3o_key = os.getenv("M3O_KEY")
cache = JokeService(token=m3o_key)


@pytest.mark.asyncio
async def test_random():
    res = await cache.random(count=1)
    assert res.jokes[0].id is not None
