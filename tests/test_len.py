from lambdaz import a0


def test_len():
    l = (a0._len_() > 3)._
    assert next(filter(l, [(), (1,2), (1,2,3,4)])) == (1,2,3,4)
