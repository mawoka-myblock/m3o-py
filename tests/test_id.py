import os

from m3o_py.id import IDgenService
from m3o_py import GeneralException
import pytest

m3o_key = os.getenv("M3O_KEY")
idgen = IDgenService(token=m3o_key)


@pytest.mark.asyncio
async def test_generate():
    assert (await idgen.generate(type="uuid")).type == "uuid"
    with pytest.raises(GeneralException):
        await idgen.generate(type="invalid")


@pytest.mark.asyncio
async def test_types():
    assert (await idgen.types()).types == ["uuid", "shortid", "snowflake", "bigflake"]
