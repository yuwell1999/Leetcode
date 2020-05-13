import sympy as sy


def cauchy_euler_equation(x, f):
    # x^2*f''(x)+4xf'(x)+2f(x)-x^2 = 0
    return pow(x, 2) * sy.diff(f(x), x, 2) + 4 * x * sy.diff(f(x), x, 1) + 2 * f(x) - pow(x, 2)


x = sy.symbols('x')
f = sy.Function('f')

# print(sy.dsolve(cauchy_euler_equation(x, f), f(x)))
sy.pprint(sy.dsolve(cauchy_euler_equation(x, f), f(x)))
