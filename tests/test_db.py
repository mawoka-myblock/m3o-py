import os

from m3o_py.db import DbService
import pytest

m3o_key = os.getenv('M3O_KEY')
db = DbService(m3o_key)


def test_update():
    assert False


def test_truncate():
    assert False


def test_rename_table():
    assert False


def test_read():
    assert False


def test_list_tables():
    assert False


def test_drop_table():
    assert False


def test_delete():
    assert False


def test_create():
    assert False


def test_count():
    assert False
