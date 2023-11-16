import numpy as np
import sympy as sp
from sympy import *
import pandas as pd

x = sp.Symbol('x')



def whprint():

    df1 = pd.DataFrame([['Hello', 'Hey', 'Shalom'], [10, 20]])

    df2 = pd.DataFrame(data={'Items': [1, 2, 3], 'Name': ['Yossi', 'moshe', 'tomer']})

    print(df1)
    print()
    print(df2)
    print()

    e = sp.exp(x ** 2)
    print(e.integrate())
    print()
    print(sp.integrate(e))


def set_funcations_and_print():
    f1 = sp.exp(x) + 3 * x ** 3
    g = sp.sin(x)
    h = exp(x) * (x - 1) ** 2
    dh = simplify(h.diff(x, 1))

    poli = x ** 3 + 2 * x ** 2 - 5 * x + 1

    a, b = -6, 6
    f = sp.exp(x) + 3 * x ** 3
    print('f = ', f)
    print('f\' = ', f.diff(x, 1))
    print('f\'\' = ', f.diff(x, 2))

    print('g = ', g)
    print('g\' = ', g.diff(x, 1))
    print('g\'\' = ', g.diff(x, 2))

    print()
    print('integral of f\' = ', integrate(f.diff(x, 1)))

    print('h = ', h)
    print('h\' = ', h.diff(x, 1))
    print('h\'(2) = ', simplify(h.diff(x, 1)).subs(x, 2))
    print('h\'(2) = ', dh.subs(x, 2))

def Taylor(f,x0, n=3):
    g=0
    for i in range(n):
        g += (f.diff(x,i).subs(x,x0))/sp.factorial(i)*((x-x0)**i)

    return g

def TaylorSeries(func, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (func.diff(x, i).subs(x, x0)) / sp.factorial(i) * (x - x0) ** i
        i += 1
    return p


def graph():
    f1 = sp.exp(x) + 3 * x ** 3
    g = sp.sin(x)
    h = exp(x) * (x - 1) ** 2
    dh = simplify(h.diff(x, 1))

    poli = x ** 3 + 2 * x ** 2 - 5 * x + 1

    a, b = -6, 6
    xx = np.linspace(a, b, 1000)

    y_g = [g.subs(x, x0) for x0 in xx]
    y_f = [f1.subs(x, x0) for x0 in xx]
    y_h = [h.subs(x, x0) for x0 in xx]
    y_dh = [dh.subs(x, x0) for x0 in xx]

    import matplotlib.pyplot as plt

    plt.plot(xx, y_g, 'r')
    plt.show()

func = sp.log(1+x)

print(Taylor(func, 0, 6))
print(TaylorSeries(func,0,5))