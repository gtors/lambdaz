from .base import Lambda
from .call import CallLambda


class ArgLambda(Lambda):
    def __init__(self, index):
        super().__init__()
        self._index = index

    def __repr__(self):
        return f"(a{self._index})"

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            return args[self._index]
        else:
            return CallLambda(self, args, kwargs)

    def _terminated_(self):
        clone = ArgLambda(self._index)
        Lambda._terminated_(clone)
        return clone


class KwargLambda(Lambda):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def __repr__(self):
        return f"(kw.{self._name})"

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            return kwargs[self._name]
        else:
            return CallLambda(self, args, kwargs)

    def _terminated_(self):
        clone = KwargLambda(self._name)
        Lambda._terminated_(clone)
        return clone


class KwargLambdaCreator:
    def __getattr__(self, name):
        return KwargLambda(name)

