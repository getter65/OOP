import math
import sympy as sym


class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        x = sym.Symbol('x')
        y = self.__func(x)
        derivative = y.diff(x)
        return derivative.evalf(subs={x: args[0]})


@Derivative
def sin_(x):
    return sym.sin(x)


print(sin_(math.pi/3))