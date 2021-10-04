import math

from lambdaz import _


def test_truediv():
    """Ensures that add works correctly."""
    math_expression = (_ / 6)._
    assert math.isclose(math_expression(39), 6.5)  # type: ignore


def test_rtruediv():
    """Ensures that add works correctly."""
    assert (42 / _)._(8) == (_ / 8)._(42)
