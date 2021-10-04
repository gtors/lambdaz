# -*- coding: utf-8 -*-

from lambdaz import _


def test_mul():
    """Ensures that add works correctly."""
    mul = (_ * 10)._
    assert mul(10) == 100


def test_rmul():
    """Ensures that add works correctly."""
    mul = (_ * 2)._
    rmul = (2 * _)._
    assert mul(4) == rmul(4)
