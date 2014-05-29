#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""

import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2.0

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2.0

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2.0
