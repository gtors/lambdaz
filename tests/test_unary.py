from lambdaz import a0


def test_repr():
    assert repr(~a0._) == "unary(<built-in function invert>, (a0))"


def test_negate():
    assert (-a0._)(1) - 1 == -2


def test_pos():
    assert (+a0._)(1) == 1


def test_invert():
    assert (~a0._)(-1) == 0
