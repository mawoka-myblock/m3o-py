import os

from m3o_py import GeneralException
from m3o_py.ip import IP2GeoService
import pytest

m3o_key = os.getenv('M3O_KEY')
ip = IP2GeoService(token=m3o_key)


@pytest.mark.asyncio
async def test_lookup():
    assert (await ip.lookup("93.148.214.31")).ip == "93.148.214.31"
    with pytest.raises(GeneralException):
        await ip.lookup("asdsasda")
