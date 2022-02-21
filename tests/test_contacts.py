import os

from m3o_py import contacts
import pytest

m3o_key = os.getenv("M3O_KEY")
cache = contacts.ContactsService(token=m3o_key)
contact_id = ""
test_contact = {'addresses': [{'label': 'company address', 'location': '123 street address'}], 'birthday': '1995-01-01',
                'emails': [{'address': 'home@example.com', 'label': 'home'},
                           {'address': 'work@example.com', 'label': 'work'}],
                'links': [{'label': 'blog', 'url': 'https://blog.joe.me'}], 'name': 'joe',
                'note': 'this person is very important',
                'phones': [{'label': 'home', 'number': '010-12345678'}, {'label': 'work', 'number': '010-87654321'}],
                'social_medias': [{'label': 'twitter', 'username': 'joe-twitter'},
                                  {'label': 'facebook', 'username': 'joe-facebook'}]}


@pytest.mark.asyncio
async def test_create():
    response = await cache.create(test_contact)
    response["contact"].pop('created_at')
    response["contact"].pop('updated_at')
    global contact_id
    contact_id = response["contact"]['id']
    response["contact"].pop("id")
    assert response["contact"] == test_contact


@pytest.mark.asyncio
async def test_list():
    response = await cache.list()
    response["contacts"][0].pop('created_at')
    response["contacts"][0].pop('updated_at')
    response["contacts"][0].pop("id")
    assert response["contacts"][0] == test_contact


@pytest.mark.asyncio
async def test_read():
    response = (await cache.read(contact_id))["contact"]
    print(response)
    response.pop('created_at')
    response.pop('updated_at')
    response.pop("id")
    assert response == test_contact


@pytest.mark.asyncio
async def test_update():
    test_contact["name"] = "joe-updated"
    test_contact["id"] = contact_id
    response = await cache.update(test_contact)
    response["contact"].pop('created_at')
    response["contact"].pop('updated_at')
    assert response["contact"] == test_contact


@pytest.mark.asyncio
async def test_delete():
    assert await cache.delete(contact_id) == {}
