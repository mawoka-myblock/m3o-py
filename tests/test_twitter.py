import os

from m3o_py import GeneralException
from m3o_py.twitter import TwitterService
import pytest

m3o_key = os.getenv('M3O_KEY')
twitter = TwitterService(token=m3o_key)


@pytest.mark.asyncio
async def test_user():
    res = await twitter.user("Mawoka_")
    assert res.profile.username == "Mawoka_"
    assert res.profile.created_at == "Sat Apr 03 14:31:30 +0000 2021"
    with pytest.raises(GeneralException):
        await twitter.user("Mawoka_hbgvcdxfghjbfcdhnbfgcmn")


@pytest.mark.asyncio
async def test_trends():
    res = await twitter.trends()
    assert res.trends[0].name is not None


@pytest.mark.asyncio
async def test_timeline():
    res = await twitter.timeline(username="Mawoka_")
    assert res.tweets[0].username == "Mawoka_"
    with pytest.raises(GeneralException):
        await twitter.timeline(username="Mawoka_hbgvcdxfghjbfcdhn54gfdtbfgcmn")


@pytest.mark.asyncio
async def test_search():
    res = await twitter.search(query="m3o")
    assert len(res.tweets) != 0
    assert len((await twitter.search(query="mghnfxg67shtfbr sfvbg83vb7n463o")).tweets) == 0
