from typing import TypedDict, Union
from aiohttp import ClientSession
from m3o_py import GeneralException, UnknownError


class CacheService:
    def __init__(self, token: str):
        self.token: str = token
        self.headers: dict = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    class DecrementReturn(TypedDict):
        key: str
        value: str

    async def decrement(self, key: str, value: int) -> DecrementReturn | UnknownError | GeneralException:
        async with ClientSession(headers=self.headers) as session:
            async with session.post("https://api.m3o.com/v1/cache/Decrement",
                                    json={"key": key, "value": value}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class DeleteReturn(TypedDict):
        status: str

    async def delete(self, key: str) -> DeleteReturn | UnknownError | GeneralException:
        async with ClientSession(headers=self.headers) as session:
            async with session.post("https://api.m3o.com/v1/cache/Delete",
                                    json={"key": key}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class GetReturn(TypedDict):
        key: str
        ttl: int
        value: str

    async def get(self, key: str) -> GetReturn | None | UnknownError | GeneralException:
        async with ClientSession(headers=self.headers) as session:
            async with session.post("https://api.m3o.com/v1/cache/Get",
                                    json={"key": key}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class IncrementReturn(TypedDict):
        key: str
        value: int

    async def increment(self, key: str, value: int) -> IncrementReturn | UnknownError | GeneralException:
        async with ClientSession(headers=self.headers) as session:
            async with session.post("https://api.m3o.com/v1/cache/Increment",
                                    json={"key": key, "value": value}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class ListKeysReturn(TypedDict):
        keys: list[str]

    async def list_keys(self) -> ListKeysReturn | UnknownError | GeneralException:
        async with ClientSession(headers=self.headers) as session:
            async with session.post("https://api.m3o.com/v1/cache/ListKeys") as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class SetReturn(TypedDict):
        status: str

    async def set(self, key: str, value: str, ttl: int) -> SetReturn | UnknownError | GeneralException:
        async with ClientSession(headers=self.headers) as session:
            async with session.post("https://api.m3o.com/v1/cache/Set",
                                    json={"key": key, "value": value, "ttl": ttl}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")
