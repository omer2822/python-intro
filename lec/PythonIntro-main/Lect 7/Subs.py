import numpy as np


def GaussElimination(A,b):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0:
                lmbd = A[i, k] / A[k, k]
                #print(lmbd)
                A[i, :] = A[i, :] - lmbd * A[k, :]
                b[i] = b[i] - lmbd * b[k]
    return A, b


def GaussSubs(A,b):
    n = len(A)
    for k in range(n-1, -1, -1):
        print(b[k])
        b[k] = (b[k] - A[k, k+1 : n] * b[k+1 : n]) / A[k, k]

    return b


#A = np.matrix([[4.0, -2.0, 1.0], [-2.0, 4.0, -2.0], [1.0, -2.0, 4.0]])
#b = np.matrix([11.0, -16.0, 17.0])


A = np.matrix([[ 1, -3,  2],[-3,  3, -1],[-4,  1,  1]])
b = np.matrix([2,0,3])

#print(np.linalg.det(A))
#aa, bb = GaussElimination(A, b.T)
#print(aa,bb)
#xx = GaussSubs(aa,b)

#print(xx)
from numpy.linalg import inv
#xSol = inv(A)*b.T
#print(xSol)

#print(GaussElimination(A, b.T))


A = np.array([[7.0, -2.0, 1.0], [14.0, -7.0, -3.0], [-7.0, 11.0, 18.0]])
b = [12.0, 17.0, 5.0]
x = np.linalg.solve(A,b)
print(x)