import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x as var

def divided_diff(x, y):
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1,n):
        for i in range(n-j):
          coef[i, j] = (coef[i+1, j-1] - coef[i,j]) / (x[i+j] - x[i])

    return coef

def newton(coef, x):
    p=0
    for i in range(len(x) - 1):
        nj = np.prod([var - x[j] for j in range(i)])
        p += coef[i]*nj

    return p


def newton(coef, data, x):
    n = len(data) - 1
    p = coef[n]
    for k in range(1, n+1):
        p = (coef[n-k] * (x - data[n - k])) + p

    return p



n=50

x = np.arange(-1, 1, 2/n)
y = np.exp(-1/(x**2))

vand = np.vander(x, increasing=True)

coef = np.linalg.solve(vand, y)
P = np.polynomial.Polynomial(coef)

x2 = np.arange(-1, 1, .1)

coef = divided_diff(x, y)[0]

y2 = newton(coef, x, x)

plt.plot(x, y)

plt.show()