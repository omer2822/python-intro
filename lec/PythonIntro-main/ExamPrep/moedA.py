"""
    this is exam moed A תשפ"ג
    Q1 is compute trace(A**2) as A in 10 by 10 matrix and Aij = (i+j)/(i+j+5)
    Q2 is sieve_of_Eratosthenes (find all primes up to n)
    Q3 is recursive split
    Q4 is place even on right and odd on left
    Q5 is compute and show MaclaurinSeries

"""

import numpy as np
from numpy import matrix

"""

    Q1:
        write f(A) = trace(A**2) as A in 10 by 10 matrix and Aij = (i+j)/(i+j+5)
"""

def squareAndTrace1(A):
    B = np.dot(A,A)
    return B.trace()

def squareAndTrace2(A):
    B = A@A
    return B.trace()

N = 10
C1 = np.zeros((10,10), dtype=float)
C = matrix(C1)
for i in range(N):
    for j in range(N):
        C1.itemset((i,j), ((i+j)/(i+j+5)))

#print(squareAndTrace2(C1))

"""
    Q2
"""

def sieve_of_Eratosthenes1(n):  #better one
    r = [i for i in range(2,n)]
    primes = []

    for i in range(2,n):
        p = min(r)
        primes.append(p)
        r.remove(p)
        for j in r:
            if j%p==0:
                r.remove(j)
        print(r)
        #print()
        if len(r) == 0:
            return primes

def sieve_of_Eratosthenes2(num):
    primes = []
    not_primes = []
    for i in range(2, num+1):
        if i in not_primes:
            continue

        primes.append(i)
        #print(not_primes)
        #print()
        for f in range(i**2, num+1, i):
            if f not in not_primes:
                not_primes.append(f)

    return primes
print(sieve_of_Eratosthenes1(2000))
"""
    Q3
"""

def split(data):
    if len(data) == 0:
        return []
    if data[0]%2 == 0:
        return split(data[1:]) + data[0:1]
    else:
        return data[0:1]+split(data[1:])

"""
def find_first_odd_on_right(data, N):
    mid, n = N//2, N-1
    righti = list(data[mid:]).reverse()

    for num in righti:
        if num%2 != 0:
            val, idx = num, n
            return val, idx
        n-=1

def find_first_even_on_left(data, N):
    mid, n = N//2, 0
    righti = list(data[:mid])
    for num in righti:
        if num%2 == 0:
            val, idx = num, n
            return val, idx
        n+=1
    return None
"""

y =[1,2,3,3,13, 2,1,2,1,2,2,1,1,1,2,1,2, 2, 3, 7, 2, 4, 4,4,6,3,11,1,8,5, 12]

#print(y)

x = split(y)

#print(x)


"""
    Q5
        MaclaurinSeries
"""

import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')

def MaclaurinSeries(func, n):
    g = func.subs(x,0)

    for i in range(1,n+1):
        g += (x**i)*(func.diff(x,i).subs(x,0))/sp.factorial(i)
    return g

def ShowMaclaurinSeries(func):
    xx = np.linspace(-1, 1, 200)
    ff = []
    for xj in xx:
        ff.append(func.subs(x, xj))
    plt.plot(xx,ff,label=str(func))
    orders = [1, 3, 5]
    yy = []
    for ord in orders:
        g = MaclaurinSeries(func, ord)
        for xi in xx:
            yy.append(g.subs(x,xi))
        plt.plot(xx, yy, label='order'+str(ord))
        yy = []

    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()




funct = sp.exp(x)
#print(sp.series(funct))

ShowMaclaurinSeries(funct)