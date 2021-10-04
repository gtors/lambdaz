# -*- coding: utf-8 -*-

from lambdaz import _


def test_add():
    """Ensures that add works correctly."""
    add = (_ + 2)._
    assert add(1) + 1 == 4


def test_radd():
    """Ensures that add works correctly."""
    add = (_ + 2)._
    radd = (2 + _)._
    assert add(1) == radd(1)
