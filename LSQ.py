import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, figure
from numpy.linalg import pinv # pseudo inverse

# Example of LSQ - fir line to COP

def fit_line(a, b, N):
    x = np.linspace(0, 10, N)

    rx = np.random.uniform(1, 2, N) # x-noise
    ry = np.random.uniform(1, 5, N) # y-noise

    x += rx
    y = a * x + b + ry

    A = np.zeros((N, 2))
    B = np.zeros((N, 1))
    # A.x = b -> x = pinv(A).b --> x = [(x1,1), (x2,1)...]^(-1).(y1...yn)
    A[:, 0] = x
    A[:, 1] = 1
    B[:, 0] = y

    # this is the answer! ( y=ax+b... X[0] is a, X[1] is b)
    X = np.dot(pinv(A), B)
    y_a = X[0] * x + X[1]

    figure()
    plot(x, y, '.r', x, y_a, 'b')
    plt.show()

def fit_parabola(a, b, c):

    x = np.linspace(-2,2,N)
    y = a*x**2 + b*x + c
    # Formulation of Ax=b
    A = np.zeros((N,3))
    b = np.zeros((N, 1))

    A[:, 0] = x**2
    A[:, 1] = x
    A[:, 2] = 1
    b[:, 0] = y

    X = np.dot(pinv(A), b)

    # this is the answer! (coefficients of parabola)
    aa = X[0]
    bb = X[1]
    cc = X[2]

    y_fit = aa*x**2+bb*x+cc

    plt.figure()
    plot(x, y, '.b', x, y_fit, 'r', linewidth=3)
    plt.grid(True)
    plt.show()


def func1(x):
    return x**2-2*x+2

def MSE(t, f, d=9, t0=0, N=100):
    x = np.linspace(t0, t, N)
    rx = np.random.uniform(1, 2, size=N)
    x = x + rx

    y = [f(xi) for xi in x]
    ry = np.random.uniform(1, 2, size=N)
    y = y + ry


    A = np.zeros((N,d))
    b = np.zeros((N,1))
    for i in range(d+1):
        A[:,i] = x**(d-i)
    b[:,0] = y

    X = np.dot(pinv(A), b)


N = 100
a = 1
b = 2
#c = 3

ra = np.random.uniform(1,2, size=N)
rb = np.random.uniform(0, 1, size=N)
rc = np.random.uniform(1,2,size=N)

x = np.linspace(0,5,N)

x = x + ra
y = a*x+b+rb


#plt.show()

fit_line(x,y,N)
#fit_parabola(x, y, rc)


