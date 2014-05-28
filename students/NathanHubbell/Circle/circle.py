#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self,radius):
        self._radius = radius
        self._diameter = radius*2
        self._area=math.pi*radius**2
    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return self._diameter
    @property
    def area(self):
        return self._area
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius*2
        self._area = math.pi*radius**2
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter/2
        self._area=math.pi*(diameter/2)**2


    def __str__(self):
        return "Circle with radius: %s00000"%repr(float(self.radius))
    def __repr__(self):
        return "Circle(%s)"%str(self.radius)
    def __add__(self,other):
        return Circle(self.radius+other.radius)
    def __mul__(self,other):
        return Circle(self.radius*other)

    def __gt__(self,other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.radius < other.radius:
            return True
        else:
            return False


    def __eq__(self,other):
        if self.radius == other.radius:
            return True
        else:
            return False


    def __le__(self,other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __ge__(self,other):
        if self.radius >= other.radius:
            return True
        else:
            return False
