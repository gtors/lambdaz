from lambdaz import _


def test_pow():
    """Ensures that add works correctly."""
    pow_ = (_ ** 2)._
    assert pow_(3) == 9


def test_rpow():
    """Ensures that add works correctly."""
    pow_ = (_ ** 2)._
    rpow = (3 ** _)._
    assert pow_(3) == rpow(2)
