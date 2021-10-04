import pytest
from lambdaz import a0, a1


@pytest.mark.asyncio
async def test_awaitable():
    l = (a0 + a1)._async_()
    assert (await l(2,3)) == 5
    assert repr(l) == "awaitable(binary(<built-in function add>, (a0), (a1)))"

