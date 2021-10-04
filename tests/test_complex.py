import math

from lambdaz import a0, a1, a2


def test_complex_expression():
    """Ensures that add works correctly."""
    complex_expression = ((10 ** 5) / (a0 % 3) * 9)._
    assert math.isclose(complex_expression(5), 450000.0)  # type: ignore

    assert (a0 + a1 * a2)._(2, 2, 2) == (2 + 2 * 2)
    assert ((a0 + a1) * a2)._(2, 2, 2) == ((2 + 2) * 2)
    assert (a0 * a1 + a2)._(2, 2, 2) == (2 * 2 + 2)
