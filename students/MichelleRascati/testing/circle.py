#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""

import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    def __str__(self):
        return u'Circle with radius: {:f}'.format(self._radius)

    def __repr__(self):
        return u"Circle({})".format(self._radius)

    def __add__(self, c2):
        """Return Circle with sum of input radii"""
        rad_new = self._radius + c2._radius
        return Circle(rad_new)

    def __mul__(self, m):
        """Return Circle m times as large"""
        rad_new = self._radius * m
        return Circle(rad_new)

    def __eq__(self, c2):
        return self.diameter == c2.diameter

    def __gt__(self, c2):
        return self.diameter > c2.diameter

    def __lt__(self, c2):
        return self.diameter < c2.diameter

    def __ge__(self, c2):
        return self.diameter >= c2.diameter

    def __le__(self, c2):
        return self.diameter <= c2.diameter

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        self._diameter = self._radius * 2.0
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2.0

    @property
    def area(self):
        self._area = math.pi * self._radius ** 2
        return self._area
