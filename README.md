# M3O-Py

[![codecov](https://codecov.io/gh/mawoka-myblock/m3o-py/branch/master/graph/badge.svg?token=Y1S7YIIAY9)](https://codecov.io/gh/mawoka-myblock/m3o-py)

This is the python library for [M3O](https://github.com/m3o/m3o).

## Installation

```sh
pip install m3o-py
```

## Usage

You import API's like this:

```python
from m3o_py.api import apiService
from asyncio import run

api = apiSerivce("<m3o_api_key>")


async def main():
    await api.upload("params")


run(main())
```

If you'd use the weather API, you'd do this:

```python
from m3o_py.weather import WeatherService

weather = WeatherService("<m3o_api_key>")


async def rpint_weather():
    res = await weather.now(location="Oberhausen")
    print(f"In {res.location} are {res.temp_c}°C and it feels like {res.feels_like_c}°C. ")
```

### Run the tests

1. Set your environment variables: `export M3O_API_KEY=<your_api_key>`
2. Run the tests: `poetry run pytest tests --asyncio-mode=strict`

## Supported API's

- [x] [Cache](https://m3o.com/cache) Coverage: 75%
- [x] [Contacts](https://m3o.com/contact) Coverage: 90%
- [x] [Database](https://m3o.com/db) Coverage: 75%
- [x] [Answers](https://m3o.com/answer) Coverage: 95%
- [x] [Jokes](https://m3o.com/joke) Coverage: 92%
- [x] [Address](https://m3o.com/address) **NO TEST SINCE IT'S NOT FREE**
- [x] [IDgen](https://m3o.com/id) Coverage: 90%
- [x] [IP2Geo](https://m3o.com/ip) Coverage: 96%
- [x] [Twitter](https://m3o.com/twitter) Coverage: 92%
- [x] [Weather](https://m3o.com/weather) Coverage: 97%
- [x] [Users](https://m3o.com/user) **NO TEST SINCE I AM LAZY**
- [ ] [Apps](https://m3o.com/app)
- [ ] [Avatar](https://m3o.com/avatar)
- [ ] [Carbon](https://m3o.com/carbon)
- [ ] [Chat](https://m3o.com/chat)
- [ ] [Comments](https://m3o.com/comments)
- [ ] [Crypto](https://m3o.com/crypto)
- [ ] [Currency](https://m3o.com/currency)
- [ ] [Email](https://m3o.com/email)
- [ ] [Emoji](https://m3o.com/emoji)
- [ ] [EV Chargers](https://m3o.com/evchargers)
- [ ] [Events](https://m3o.com/event)
- [ ] [Files](https://m3o.com/file)
- [ ] [Forex](https://m3o.com/forex)
- [ ] [Functions](https://m3o.com/function)
- [ ] [Geocoding](https://m3o.com/geocoding)
- [ ] [GIFs](https://m3o.com/gifs)
- [ ] [Goole](https://m3o.com/google)
- [ ] [Hello World](https://m3o.com/helloworld)
- [ ] [Holidays](https://m3o.com/holidays)
- [ ] [Image](https://m3o.com/image)
- [ ] [Lists](https://m3o.com/lists)
- [ ] [Location](https://m3o.com/location)
- [ ] [Meme Generator](https://m3o.com/memegen)
- [ ] [Minecraft](https://m3o.com/minecraft)
- [ ] [Movies](https://m3o.com/movie)
- [ ] [Message Queue](https://m3o.com/mq)
- [ ] [News](https://m3o.com/news)
- [ ] [NFTs](https://m3o.com/nft)
- [ ] [Notes](https://m3o.com/notes)
- [ ] [OTP](https://m3o.com/otp)
- [ ] [Ping](https://m3o.com/ping)
- [ ] [Places](https://m3o.com/place)
- [ ] [Postcode](https://m3o.com/postcode)
- [ ] [Prayer](https://m3o.com/prayer)
- [ ] [QR Codes](https://m3o.com/qr)
- [ ] [Quran](https://m3o.com/quran)
- [ ] [Routes](https://m3o.com/routing)
- [ ] [RSS](https://m3o.com/rss)
- [ ] [Search](https://m3o.com/search)
- [ ] [Sentiment](https://m3o.com/sentiment)
- [ ] [SMS](https://m3o.com/sms)
- [ ] [Space](https://m3o.com/space)
- [ ] [Spam](https://m3o.com/spam)
- [ ] [Stocks](https://m3o.com/stock)
- [ ] [Stream](https://m3o.com/stream)
- [ ] [Sunnah](https://m3o.com/sunnah)
- [ ] [Thumbnail](https://m3o.com/thumbnail)
- [ ] [Time](https://m3o.com/time)
- [ ] [Translate](https://m3o.com/translate)
- [ ] [URLs](https://m3o.com/url)
- [ ] [Vehicle](https://m3o.com/vehicle)
- [ ] [YouTube](https://m3o.com/youtube)