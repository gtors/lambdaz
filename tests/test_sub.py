# -*- coding: utf-8 -*-

from lambdaz import _


def test_sub():
    """Ensures that add works correctly."""
    sub = (_ - 4)._
    assert sub(4) == 0


def test_rsub():
    """Ensures that add works correctly."""
    sub = (_ - 4)._
    rsub = (4 - _)._
    assert rsub(1) + sub(1) == 0
