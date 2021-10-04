from lambdaz import v, a0, a1, fn


def test_repr():
    assert repr(v("hello")._) == "value('hello')"


def test_value():
    l = v("{label}: {}").format(a1, label=a0)._
    assert l("name", "John") == "name: John"


def test_fn():
    l = v("The type of {val} is {ty}").format(ty=fn(type)(a0).__name__, val=a0)._
    assert l(1) == "The type of 1 is int"

