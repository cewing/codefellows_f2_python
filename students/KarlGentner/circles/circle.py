#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    _x = None

    def __init__(self, rad):
        self._x = rad

    @classmethod
    def from_diameter(klass, diam):
        return klass(diam/2)

    def __add__(c1, c2):
        return Circle(c1.radius + c2.radius)

    def __mul__(c, value):
        return Circle(c.radius * value)

    def __eq__(c1, c2):
        if c1.radius == c2.radius:
            return True
        else:
            return False

    def __ne__(c1, c2):
        if c1.radius != c2.radius:
            return True
        else:
            return False

    def __lt__(c1, c2):
        if c1.radius < c2.radius:
            return True
        else:
            return False

    def __le__(c1, c2):
        if c1.radius <= c2.radius:
            return True
        else:
            return False

    def __gt__(c1, c2):
        if c1.radius > c2.radius:
            return True
        else:
            return False

    def __ge__(c1, c2):
        if c1.radius >= c2.radius:
            return True
        else:
            return False

    def __repr__(self):
        return("Circle(%s)" % self._x)

    def __str__(self):
        return("Circle with radius: {0:.6f}").format(self._x)

    def rget(self):
        return self._x

    def rset(self, value):
        self._x = value

    radius = property(rget, rset)

    def dget(self):
        return self._x*2

    def dset(self, value):
        self._x = value/2

    diameter = property(dget, dset)

    def aget(self):
        return math.pi*(self._x**2)

    area = property(aget, doc="The area is read only.")
