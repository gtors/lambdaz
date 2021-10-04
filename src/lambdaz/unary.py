from .base import Lambda
from .util import unwrap
from .call import CallLambda


class UnaryLambda(Lambda):
    def __init__(self, op, it):
        super().__init__()
        self._op = op
        self._it = it

    def __repr__(self):
        return f"unary({self._op!r}, {self._it!r})"

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            it = unwrap(self._it, args, kwargs)
            return self._op(it)
        else:
            return CallLambda(self, args, kwargs)
