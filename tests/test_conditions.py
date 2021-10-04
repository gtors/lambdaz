from lambdaz import a0, a1, a2, val


def test_repr():
    assert repr(a0._and_(a1)._or_(a2)._) == "((a0) and (a1) or (a2))"


def test_and_or():
    l = val(True)._and_(False)._
    assert l() is False

    l = ((a0 + a1) == a2)._and_(True)._
    assert l(1, 2, 3) is True

    l = a0._and_(a1)._or_(a2)._
    assert l(1, 2, 3) == 2
    assert l(0, 2, 3) == 3
    assert l(1, 0, 3) == 3

    l = a0._or_(a1)._or_(a2)._
    assert l(1, 2, 3) == 1
    assert l(0, 2, 3) == 2
    assert l(0, 0, 3) == 3

    l = a0._or_(a1)._and_(a2)._
    assert l(1, 2, 3) == 1
    assert l(0, 2, 3) == 3
    assert l(0, 0, 3) == 0

    l = a0._and_((a1)._or_(a2))._
    assert l(1, 2, 3) == 2
    assert l(0, 2, 3) == 0
    assert l(1, 0, 3) == 3

    l = (a0._or_(a1))()._
    assert l(None, val(123)._) == 123


def test_equal():
    assert (a0 == 1)._(1)


def test_not_equal():
    assert (a0 != 1)._(2)


def test_less_than():
    assert (a0 < 2)._(1)
    assert (a0 <= 2)._(2)


def test_greater_than():
    assert (a0 > 2)._(3)
    assert (a0 >= 2)._(2)
