import os

from m3o_py import GeneralException
from m3o_py.user import UserService
import requests
import pytest

m3o_key = os.getenv('M3O_KEY')
users = UserService(token=m3o_key)
email = ""


@pytest.mark.asyncio
async def test_create():
    assert False


@pytest.mark.asyncio
async def test_send_verification_email():
    assert False


@pytest.mark.asyncio
async def test_delete():
    assert False


@pytest.mark.asyncio
async def test_list():
    assert False


@pytest.mark.asyncio
async def test_login():
    assert False


@pytest.mark.asyncio
async def test_logout():
    assert False


@pytest.mark.asyncio
async def test_read():
    assert False


@pytest.mark.asyncio
async def test_read_session():
    assert False


@pytest.mark.asyncio
async def test_reset_password():
    assert False


@pytest.mark.asyncio
async def test_send_magic_link():
    assert False


@pytest.mark.asyncio
async def test_send_password_reset_email():
    assert False


@pytest.mark.asyncio
async def test_update():
    assert False


@pytest.mark.asyncio
async def test_update_password():
    assert False


@pytest.mark.asyncio
async def test_verify_email():
    assert False


@pytest.mark.asyncio
async def test_verify_token():
    assert False
