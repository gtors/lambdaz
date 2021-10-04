from lambdaz import a0, a1, a5

def test_args():
    l = (a0 + a1 + a5)._
    assert l(1,2,3,4,5,6) == (1 + 2 + 6)
