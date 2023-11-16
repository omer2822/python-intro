import numpy as np
from numpy.linalg import pinv
"""
class FitCircle:
    def __init__(self, x, y):
        self.point = x + y*1j #complex vector
        self.N = len(x)
        self.centerA, self.centerB, self.Radius = self.fitCircle(self.point)
    def get_circle_center_and_radius(self):
        return complex(self.centerA,self.centerB), self.Radius

    def fitCircle(self, points):
        A = np.zeros((self.N,3))
        A[:, 0] = 1
        A[:,1] = 2*points.real
        A[:,2] = 2*points.imag
        b = points*points.conjugate()

        X = np.linalg.pinv(A)
        res = np.dot(X, b)
        res[0] = res[2] + res[1]**2 + res[2]**2
        return res



#N=100
N = 50
#x = np.ones(N)
#y = np.zeros(N) + 0.5

#z = x + y*1j
#
R = np.random.uniform(10, 16, size=N)
alpha = np.linspace(0, 2*np.pi, N)
x = 10+R*np.cos(alpha)
y = 1+R*np.sin(alpha)
my_circle = FitCircle(x, y)
#my_circle.fit_circle()
z, R = my_circle.get_circle_center_and_radius()
print('(a, b) = (', z.real, ',', z.imag, '), R =', R)


"""
class FitCircle:
 def __init__(self, x,y):
    self.x = x
    self.y = y
    self.a = 0.0
    self.b = 0.0
    self.R = 0.0
 def get_circle_center_and_radius(self):
    return self.a, self.b, self.R
 def fit_circle(self):
    n = len(self.x)
 # Formulation of Ax=b
    A = np.zeros((n, 3))
    bb = np.zeros((n, 1))
    A[:, 0] = self.x
    A[:, 1] = self.y
    A[:, 2] = 1
    bb[:, 0] = self.x ** 2 + self.y ** 2
    X = np.dot(pinv(A), bb)
    self.a = X[0] / 2
    self.b = X[1] / 2
    self.R = np.sqrt(X[2] + self.a ** 2 + self.b ** 2)
# code run example
N = 50
R = np.random.uniform(10, 16, size=N)
alpha = np.linspace(0, 2*np.pi, N)
x = 10+R*np.cos(alpha)
y = 1+R*np.sin(alpha)
my_circle = FitCircle(x, y)
my_circle.fit_circle()
a, b, R = my_circle.get_circle_center_and_radius()

print('(a, b) = (', a[0], ',', b[0], '), R =', R[0])
