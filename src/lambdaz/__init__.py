import operator

from .args import KwargLambdaCreator, ArgLambda
from .value import ValueLambda


__version__ = "0.1.0"


kw = KwargLambdaCreator()
fn = v = val = ValueLambda
_ = it = a0 = ArgLambda(0)
a1 = ArgLambda(1)
a2 = ArgLambda(2)
a3 = ArgLambda(3)
a4 = ArgLambda(4)
a5 = ArgLambda(5)
a6 = ArgLambda(6)
