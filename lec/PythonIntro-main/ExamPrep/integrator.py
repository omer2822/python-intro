import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, figure
from numpy.linalg import pinv # pseudo inverse

class Integrator:
    def __init__(self, a, b, N):
        self.a, self.b, self.N = a, b, N
        self.points, self.weights = self.construct_method()

    def integrate(self, f):
        s=0
        for i in range(self.N):
            s += self.weights[i] * f(self.points[i])
        return s

class MidPoint(Integrator):
    def construct_method(self):
        h = (self.b - self.a) / float(self.N)
        X = np.linspace(self.a + (h*0.5), self.b - (h*0.5), self.N)
        W = np.ones(len(X)) * h
        return X, W

class Trapezoidal(Integrator):
    def construct_method(self):
        h = (self.b - self.a) / float(self.N-1)
        X = np.linspace(self.a, self.b, self.N)
        W = np.zeros(len(X)) + h
        W[0], W[-1] = h/2, h/2
        return X, W

class Trapezoidal_IsGood(Integrator):
    def construct_method(self):
        X, W = [], []
        h = (self.b - self.a) / float(self.N-1)
        for i in range(self.N):
            X.append(self.a + (i * h))
            W.append(h)
        X[0], X[1], W[0], W[-1] = self.a, self.a + h, h / 2, h / 2
        return X, W



def f(x):
    return x*x

N=101
trapez = Trapezoidal_IsGood(0, 2, N)
print(trapez.integrate(f))

midPoint = MidPoint(0, 2, N)
print(midPoint.integrate(f))