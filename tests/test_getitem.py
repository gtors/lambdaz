# -*- coding: utf-8 -*-

from lambdaz import _


def test_getitem():
    """Ensures that getitem works correctly."""
    assert _['a']._({'a': 1}) + 2 == 3
    assert _[0]({0: 'a'}) + 'b' == 'ab'  # noqa: WPS336


def test_slice():
    assert _[::-1][:4]._("olleh") == "hell"
