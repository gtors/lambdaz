from lambdaz import a0, a1, kw


def test_repr():
    assert repr(a0(123, x=1)._) == "call((a0), args=(123,), kwargs={'x': 1})"


def test_call():
    l = a0.strip().split(",")._
    assert l("  hello,dude  ") == ["hello", "dude"]


def test_nested_call():
    l = a0()()._
    assert l(lambda: lambda: 1) == 1

    l = kw.func()._
    assert l(func=lambda: 1) == 1


    class chainable:

        def __init__(self, func):
            self._func = func
            self._next = None

        def __call__(self, *args, **kwargs):
            ret = self._func(*args, **kwargs)
            ret = self._next and self._next(ret) or ret
            return ret

        def __or__(self, other):
            if self._next:
                self._next.__or__(other)
            elif self is not other:
                self._next = other
            return self

    @chainable
    def foo(x):
        return x + x

    @chainable
    def bar(x):
        return x * x

    l = (a0 | a1)(2)._
    assert l(foo, bar) == 16


