from .base import Lambda
from .call import CallLambda


class ValueLambda(Lambda):
    def __init__(self, value):
        super().__init__()
        self._value = value

    def __repr__(self):
        return f"value({self._value!r})"

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            return self._value
        else:
            return CallLambda(self, args, kwargs)
