from lambdaz import a0, v


def test_contains():
    l = v((1,2,3))._contains_(a0)._
    assert l(1)


def test_not_contains():
    l = v((1,2,3))._not_contains_(a0)._
    assert l(0)


def test_in():
    l = a0._in_((1,2,3))._
    assert l(1)


def test_not_in():
    l = a0._not_in_((1,2,3))._
    assert l(0)

