import os

from m3o_py.weather import WeatherService
from m3o_py import GeneralException
import pytest

m3o_key = os.getenv('M3O_KEY')
weather = WeatherService(m3o_key)


@pytest.mark.asyncio
async def test_now():
    res = await weather.now("Oberhausen")
    assert res.country == "Nordrhein-Westfalen"
    assert res.location == "Oberhausen"
    with pytest.raises(GeneralException):
        await weather.now("asdasd")


@pytest.mark.asyncio
async def test_forecast():
    res = await weather.forecast("Oberhausen", days=3)
    assert res.country == "Nordrhein-Westfalen"
    assert len(res.forecast) == 3
    with pytest.raises(GeneralException):
        await weather.forecast("asdasd", days=30)
