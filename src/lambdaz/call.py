from .base import Lambda
from .util import unwrap_partial


class CallLambda(Lambda):
    def __init__(self, method, args, kwargs):
        super().__init__()
        self._method = method
        self._args = args or ()
        self._kwargs = kwargs or {}

    def __repr__(self):
        return (
            f"call({self._method!r}, "
            f"args={self._args!r}, "
            f"kwargs={self._kwargs!r})"
        )

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            un = unwrap_partial(args, kwargs)
            method = un(self._method)
            return method(
                *(un(arg) for arg in self._args),
                **{un(k): un(v) for k, v in self._kwargs.items()}
            )
        else:
            return CallLambda(self, args, kwargs)
