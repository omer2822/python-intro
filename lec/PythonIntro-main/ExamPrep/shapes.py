import numpy as np
import math

def dist(p,q):
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2)**0.5


class Shape(object):
    def __init__(self, points):
        self.points = points
    def describe(self):
        print('I am a shape')

    def perimiter(self):
        s=0
        for i in range(len(self.points)):
            s += dist(self.points[i-1], self.points[i])
        return s

class Quadrilateral(Shape):
    def __init__(self, points):
        if self.is_Quadrilateral(points):
            print("T")
        else:
            self.points=points

    def describe(self):
        print('I am a Quadrilateral')
    def is_Quadrilateral(self, points):
        if len(points)!=4:
            return False
        # to do : check that no 3 point are on the same line


def line_equation(x1,x2,y1,y2):
    m = (y2-y1)/(x2-x1)
    b1 = y1-m*x1
    return m, b1

p1 = (0,0)
p2 = (1,0)
p3 = (0,1)
s = Shape([(0,0),(1,0),(0,1),(1,1)])
