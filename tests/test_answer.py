import os

from m3o_py import GeneralException
from m3o_py.answer import AnswerService
import pytest

m3o_key = os.getenv('M3O_KEY')
answer = AnswerService(token=m3o_key)


@pytest.mark.asyncio
async def test_question():
    res = await answer.question(query='microsoft')
    assert "https://" in res.url

    with pytest.raises(GeneralException):
        await answer.question(query='')
