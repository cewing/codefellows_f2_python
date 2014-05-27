#!/usr/bin/env python

import math


class Circle(object):
    ''' Creates a circle object with properties to connec diameter, 
    radius and area attributes. '''

    def __init__(self, radius):
        self.radius = radius
      
    def _get_radius(self):
        return self._radius

    def _set_radius(self, value):
        self._radius = value
        self._diameter = self._radius * 2

    radius = property(_get_radius, _set_radius)

    def _get_diameter(self):
        return self._diameter

    def _set_diameter(self, value):
        self.radius = value / 2

    diameter = property(_get_diameter, _set_diameter)

    def _get_area(self):
        return math.pi * self.radius**2

    area = property(_get_area)

    def __str__(self):
        return 'Circle with radius: %f' % (self.radius)

    def __repr__(self):
        return 'Circle(%s)' % self.radius

    def __add__(c1, c2):
        return Circle(c1.radius + c2.radius)

    def __mul__(c1, value):
        return Circle(c1.radius * value)

    def __eq__(c1, c2):
        return c1.radius == c2.radius

    def __lt__(c1, c2):
        return c1.radius < c2.radius

    def __gt__(c1, c2):
        return c1.radius > c2.radius

    def __le__(c1, c2):
        return c1.radius <= c2.radius

    def __ge__(c1, c2):
        return c1.radius >= c2.radius

    def __ne__(c1, c2):
        return c1.radius != c2.radius


""" 
__cmp__ key for special methods:  

    x<y calls x.__lt__(y),
    x<=y calls x.__le__(y),
    x==y calls x.__eq__(y), 
    x!=y and x<>y call x.__ne__(y),
    x>y calls x.__gt__(y),
    and x>=y calls x.__ge__(y).

    (from https://docs.python.org/2/reference/datamodel.html)
"""


