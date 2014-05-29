#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""

import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2.0
        self._area = math.pi * radius ** 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2.0
        self._area = math.pi * (value / 2.0) ** 2

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
        self._radius = math.sqrt(value / math.pi)
