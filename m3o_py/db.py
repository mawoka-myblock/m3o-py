from typing import TypedDict, Union, Optional, Any
from aiohttp import ClientSession
from m3o_py import GeneralException, UnknownError


class DbService:
    def __init__(self, token: str):
        self.token: str = token
        self.headers: dict = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    class CountReturn(TypedDict):
        count: int

    async def count(self, table: str) -> CountReturn | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/Count", headers=self.headers,
                                    json={"table": table}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class CreateReturn(TypedDict):
        id: str

    async def create(self, table: str, record: dict) -> CreateReturn | UnknownError | GeneralException:
        """

        :param table: The table where the data should be stored
        :param record: The actual data to be stored
        :return: The id of the record
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/Create", headers=self.headers,
                                    json={"table": table, "record": record}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    async def delete(self, table: str, id: str) -> None | UnknownError | GeneralException:
        """
        :param table: The table where the data should be stored
        :param id: The id pf the element to be deleted
        :return: None
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/Delete", headers=self.headers,
                                    json={"table": table, "id": id}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    async def drop_table(self, table: str) -> None | UnknownError | GeneralException:
        """
        :param table: The table to be dropped
        :return: None
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/DropTable", headers=self.headers,
                                    json={"table": table}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    async def list_tables(self) -> list[str] | UnknownError | GeneralException:
        """
        :return: None
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/ListTables", headers=self.headers) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    class ReadInputData(TypedDict):
        id: Optional[str]
        limit: Optional[int]
        offest: Optional[str]
        order: Optional[str]
        orderBy: Optional[str]
        query: str
        table: str

    class ReadReturn(TypedDict):
        record: list[dict[str, Any]]

    async def read(self, data: ReadInputData) -> ReadInputData | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/Read", headers=self.headers,
                                    json=data) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return await resp.json()
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    async def rename_table(self, from_table: str, to: str) -> None | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/RenameTable", headers=self.headers,
                                    json={"from": from_table, "to": to}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    async def truncate(self, table: str) -> None | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/Truncate", headers=self.headers,
                                    json={"table": table}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")

    async def update(self, table: str, id: str, data: dict[str, Any]) -> None | UnknownError | GeneralException:
        """
        :param table: Table name. Defaults to 'default'
        :param id: The id of the record. Will overwrite if id is set in data
        :param data: The data to be updated
        :return:
        """
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/db/Update", headers=self.headers,
                                    json={"table": table, "data": {**data, "id": id}}) as resp:
                if resp.status == 500:
                    raise GeneralException(await resp.json())
                elif resp.status == 200:
                    return
                else:
                    raise UnknownError(f"Unknown error: {resp.status}")
