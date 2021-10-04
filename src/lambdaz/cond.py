from .base import Lambda
from .util import unwrap_partial
from .call import CallLambda


AND = object()
OR = object()


class CondLambda(Lambda):
    def __init__(self, cond, lhs, rhs):
        super().__init__()
        self._z_conditions = [lhs, cond, rhs]

    def _or_(self, rhs):
        self._z_conditions.append(OR)
        self._z_conditions.append(rhs)
        return self

    def _and_(self, rhs):
        self._z_conditions.append(AND)
        self._z_conditions.append(rhs)
        return self

    def __repr__(self):
        expr = " ".join([
            (it is OR and "or") or
            (it is AND and "and") or
            repr(it)
            for it in self._z_conditions
        ])
        return f"({expr})"

    def __call__(self, *args, **kwargs):
        if self._z_terminated:
            un = unwrap_partial(args, kwargs)
            last_it = None
            skip_next = False
            for it in self._z_conditions:
                if skip_next:
                    skip_next = False
                    continue
                if it is AND and not bool(last_it):
                    skip_next = True
                    continue
                if it is OR and bool(last_it):
                    return last_it
                last_it = un(it)
            else:
                return last_it
        else:
            return CallLambda(self, args, kwargs)


class AndLambda(CondLambda):
    def __init__(self, lhs, rhs):
        super().__init__(AND, lhs, rhs)


class OrLambda(CondLambda):
    def __init__(self, lhs, rhs):
        super().__init__(OR, lhs, rhs)

