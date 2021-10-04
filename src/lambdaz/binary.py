from .base import Lambda
from .util import unwrap_partial
from .call import CallLambda


class BinaryLambda(Lambda):
    def __init__(self, op, lhs, rhs):
        super().__init__()
        self._op = op
        self._lhs = lhs
        self._rhs = rhs

    def __repr__(self):
        return f"binary({self._op!r}, {self._lhs!r}, {self._rhs!r})"

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            un = unwrap_partial(args, kwargs)
            lhs = un(self._lhs)
            rhs = un(self._rhs)
            return self._op(lhs, rhs)
        else:
            return CallLambda(self, args, kwargs)
