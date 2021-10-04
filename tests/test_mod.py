# -*- coding: utf-8 -*-

from lambdaz import _


def test_mod():
    """Ensures that add works correctly."""
    mod = (_ % 3)._
    assert mod(25) == 1


def test_rmod():
    """Ensures that add works correctly."""
    mod = (_ % 3)._
    rmod = (25 % _)._
    assert mod(25) == rmod(3)
