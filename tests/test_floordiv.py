# -*- coding: utf-8 -*-

from lambdaz import _


def test_floordiv():
    """Ensures that add works correctly."""
    floordiv = (_ // 2)._
    assert floordiv(5) == 2


def test_rfloordiv():
    """Ensures that add works correctly."""
    floordiv = (_ // 2)._
    rfloordiv = (5 // _)._
    assert floordiv(5) == rfloordiv(2)
