from typing import TypedDict, Optional
from aiohttp import ClientSession
from m3o_py import GeneralException, UnknownError


class CreateAddressesInput(TypedDict):
    label: str
    location: str


class CreateEmailInput(TypedDict):
    address: str
    label: str


class CreatePhoneInput(TypedDict):
    number: str
    label: str


class CreateLinkInput(TypedDict):
    label: str
    url: str


class CreateSocialMediaInput(TypedDict):
    label: str
    username: str


class CreateContactOutput(TypedDict):
    id: str
    name: str
    phones: Optional[CreatePhoneInput]
    emails: Optional[CreateEmailInput]
    links: Optional[CreateLinkInput]
    birthday: str
    addresses: Optional[CreateAddressesInput]
    social_medias: Optional[CreateSocialMediaInput]
    note: str
    created_at: str
    updated_at: str


class CreateContactInput(TypedDict):
    addresses: Optional[list[CreateAddressesInput]]
    birthday: Optional[str]
    emails: Optional[list[CreateEmailInput]]
    links: Optional[list[CreateLinkInput]]
    name: str
    note: Optional[str]
    phones: Optional[list[CreatePhoneInput]]
    social_medias: Optional[list[CreateSocialMediaInput]]


class UpdateContactInput(TypedDict):
    id: str
    addresses: Optional[list[CreateAddressesInput]]
    birthday: Optional[str]
    emails: Optional[list[CreateEmailInput]]
    links: Optional[list[CreateLinkInput]]
    name: Optional[str]
    note: Optional[str]
    phones: Optional[list[CreatePhoneInput]]
    social_medias: Optional[list[CreateSocialMediaInput]]


class ListContactsOutput(TypedDict):
    contacts: list[CreateContactOutput]


class ContactsService:
    def __init__(self, token: str):
        self.token: str = token
        self.headers: dict = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    class CreateContactOutputWrapper(TypedDict):
        contact: CreateContactOutput

    async def create(self, contact: CreateContactInput) -> CreateContactOutputWrapper | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/contact/Create",
                                    json=contact, headers=self.headers) as response:
                if response.status == 500:
                    raise GeneralException(await response.json())
                elif response.status == 200:
                    return await response.json()
                else:
                    raise UnknownError(f"Unknown error: {response.status}")

    async def delete(self, contact_id: str) -> None | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post(f"https://api.m3o.com/v1/contact/Delete",
                                    headers=self.headers, json={"id": contact_id}) as response:
                if response.status == 500:
                    raise GeneralException(await response.json())
                elif response.status == 200:
                    return await response.json()
                else:
                    raise UnknownError(f"Unknown error: {response.status}")

    async def list(self, limit: Optional[int] = None,
                   offset: Optional[int] = None) -> ListContactsOutput | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/contact/List", headers=self.headers,
                                    json={"limit": limit, "offset": offset}) as response:
                if response.status == 500:
                    raise GeneralException(await response.json())
                elif response.status == 200:
                    return await response.json()
                else:
                    raise UnknownError(f"Unknown error: {response.status}")

    async def read(self, contact_id: str) -> CreateContactOutputWrapper | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/contact/Read", headers=self.headers,
                                    json={"id": contact_id}) as response:
                if response.status == 500:
                    raise GeneralException(await response.json())
                elif response.status == 200:
                    return await response.json()
                else:
                    raise UnknownError(f"Unknown error: {response.status}")

    async def update(self, contact: UpdateContactInput) -> CreateContactOutputWrapper | UnknownError | GeneralException:
        async with ClientSession() as session:
            async with session.post("https://api.m3o.com/v1/contact/Update", headers=self.headers,
                                    json=contact) as response:
                if response.status == 500:
                    raise GeneralException(await response.json())
                elif response.status == 200:
                    return await response.json()
                else:
                    raise UnknownError(f"Unknown error: {response.status}")
