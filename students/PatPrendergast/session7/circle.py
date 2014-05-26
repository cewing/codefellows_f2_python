#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    ''' Creates a circle object with diameter, radius and area attributes'''

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

    def __str__(Circle):
        return 'Circle'

    def __repr__(self):
        """
        String representation, uses list (superclass) representation
        """
        return 'Circle(%s)' % super(vector, self).__repr__()

    def __add__(c1, c2):
        return Circle(c1.radius + c2.radius)
        
        
