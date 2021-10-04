import operator


from .consts import TERMINATION_SIGN


class Lambda:
    def __init__(self, **kwargs):
        from .unary import UnaryLambda
        from .binary import BinaryLambda
        from .aio import AwaitableLambda
        from .cond import AndLambda, OrLambda

        self._z_terminated = False
        self._z_binary = kwargs.get("binary", BinaryLambda)
        self._z_unary = kwargs.get("unary", UnaryLambda)
        self._z_awaitable = kwargs.get("awaitable", AwaitableLambda)
        self._z_or = kwargs.get("or", OrLambda)
        self._z_and = kwargs.get("and", AndLambda)

    def __add__(self, other):
        return self._z_binary(operator.add, self, other)

    def __radd__(self, other):
        return self._z_binary(operator.add, other, self)

    def __sub__(self, other):
        return self._z_binary(operator.sub, self, other)

    def __rsub__(self, other):
        return self._z_binary(operator.sub, other, self)

    def __mod__(self, other):
        return self._z_binary(operator.mod, self, other)

    def __rmod__(self, other):
        return self._z_binary(operator.mod, other, self)

    def __pow__(self, other):
        return self._z_binary(operator.pow, self, other)

    def __rpow__(self, other):
        return self._z_binary(operator.pow, other, self)

    def __lshift__(self, other):
        return self._z_binary(operator.lshift, self, other)

    def __rlshift__(self, other):
        return self._z_binary(operator.lshift, other, self)

    def __rshift__(self, other):
        return self._z_binary(operator.rshift, self, other)

    def __rrshift__(self, other):
        return self._z_binary(operator.rshift, other, self)

    def __xor__(self, other):
        return self._z_binary(operator.xor, self, other)

    def __rxor__(self, other):
        return self._z_binary(operator.xor, other, self)

    def __and__(self, other):
        return self._z_binary(operator.and_, self, other)

    def __rand__(self, other):
        return self._z_binary(operator.and_, other, self)

    def __or__(self, other):
        return self._z_binary(operator.or_, self, other)

    def __ror__(self, other):
        return self._z_binary(operator.or_, other, self)

    def __mul__(self, other):
        return self._z_binary(operator.mul, self, other)

    def __rmul__(self, other):
        return self._z_binary(operator.mul, other, self)

    def __truediv__(self, other):
        return self._z_binary(operator.truediv, self, other)

    def __rtruediv__(self, other):
        return self._z_binary(operator.truediv, other, self)

    def __floordiv__(self, other):
        return self._z_binary(operator.floordiv, self, other)

    def __rfloordiv__(self, other):
        return self._z_binary(operator.floordiv, other, self)

    def __getitem__(self, key):
        return self._z_unary(operator.itemgetter(key), self)

    def __neg__(self):
        return self._z_unary(operator.neg, self)

    def __pos__(self):
        return self._z_unary(operator.pos, self)

    def __invert__(self):
        return self._z_unary(operator.invert, self)

    def __getattr__(self, name):
        if name == TERMINATION_SIGN:
            return self._terminated_()
        else:
            return self._z_unary(operator.attrgetter(name), self)

    def __eq__(self, other):
        return self._z_binary(operator.eq, self, other)

    def __ne__(self, other):
        return self._z_binary(operator.ne, self, other)

    def __lt__(self, other):
        return self._z_binary(operator.lt, self, other)

    def __gt__(self, other):
        return self._z_binary(operator.gt, self, other)

    def __le__(self, other):
        return self._z_binary(operator.le, self, other)

    def __ge__(self, other):
        return self._z_binary(operator.ge, self, other)

    def _contains_(self, other):
        return self._z_binary(operator.contains, self, other)._terminated_()

    def _and_(self, other):
        return self._z_and(self, other)

    def _or_(self, other):
        return self._z_or(self, other)

    def _not_contains_(self, other):
        return self._contains_(other)._not_()

    def _in_(self, other):
        return self._z_binary(operator.contains, other, self)._terminated_()

    def _not_in_(self, other):
        return self._in_(other)._not_()

    def _not_(self):
        return self._z_unary(operator.not_, self)._terminated_()

    def _len_(self):
        return self._z_unary(len, self)

    def _terminated_(self):
        self._z_terminated = True
        return self

    def _async_(self):
        return self._z_awaitable(self)
