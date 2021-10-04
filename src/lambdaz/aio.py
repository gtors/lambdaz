import asyncio
from .util import unwrap


class AwaitableLambda:
    def __init__(self, lambda_):
        self._lambda = lambda_

    def __repr__(self):
        return f"awaitable({self._lambda!r})"

    def __call__(self, *args, **kwargs):
        fut = asyncio.Future()
        fut.set_result(unwrap(self._lambda, args, kwargs))
        return fut
