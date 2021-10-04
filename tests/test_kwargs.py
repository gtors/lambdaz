from lambdaz import kw


def test_kwargs():
    l = (kw.first_name + ' ' + kw.last_name)._
    assert l(first_name="foo", last_name="bar") == "foo bar"
    assert repr(l) == (
        "binary(<built-in function add>, "
        "binary(<built-in function add>, "
        "(kw.first_name), ' '), (kw.last_name))"
    )
