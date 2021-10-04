from lambdaz import a0


def test_shift():
    assert (a0 >> 1)._(8) == 4
    assert (8 >> a0)._(1) == 4
    assert (1 << a0)._(1) == 2
    assert (a0 << 1)._(2) == 4


def test_and():
    assert (a0 & 1)._(2) == 0
    assert (3 & a0)._(1) == 1


def test_or():
    assert (a0 | 1)._(3) == 3
    assert (1 | a0)._(3) == 3


def test_xor():
    assert (a0 ^ 2)._(3) == 1
    assert (3 ^ a0)._(2) == 1
