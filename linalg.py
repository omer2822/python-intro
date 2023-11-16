import numpy as np

def GaussElimination(A,b):
    n = len(A)
    U = A.copy()
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0:
                lmbd = U[i, k] / U[k, k]
                U[i, :]  = U[i, :] - lmbd * U[k, :]
                b[i] = b[i] - lmbd * b[k]
    return U,b

def LU(A,b):
    n = len(A)
    U = A.copy()
    L = np.eye(n)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0:
                lmbd = U[i, k] / U[k, k]
                U[i, :]  = U[i, :] - lmbd * U[k, :]
                L[i,k] = lmbd
                b[i] = b[i] - lmbd * b[k]

    return L,U,b

def GaussSubs(A,b):
    n = len(A)
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - A[k, k + 1:n] * b[k + 1:n]) / A[k, k]
    return b

from numpy.linalg import det

def kramer(A,b):
    da = det(A)
    if da == 0:
        return None
    x = np.zeros((A.shape[0],1))
    for k in range(A.shape[0]):
        Ak = np.matrix(A)
        Ak[:,k] = b
        x[k] = det(Ak)/da
    return x

A = np.matrix([[4, -2, 1], [-2, 4, -2], [1.0, -2.0, 4.0]])
b = np.matrix([11.0, -16.0, 17.0])

print(kramer(A,b.T).T)
aa, bb = GaussElimination(A, b.T)

xx = GaussSubs(aa,bb)
print("xxx:", xx.T)
print("bb:", bb.T)
#print("aa:", aa) # A מדורגת
#print("A:", A)
#print(np.linalg.cond(aa))
#print(np.linalg.cond(A))


from scipy.linalg import ldl  # L+D+U decomposition




