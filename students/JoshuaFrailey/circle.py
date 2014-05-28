#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    u"""Create a representation of a circle with a given radius."""
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2.0

    @property
    def area(self):
        return math.pi * (self._radius**2)

    @classmethod
    def from_diameter(cls, diameter):
        u"""Create a representation of a circle with a given diameter."""
        return cls(diameter / 2.0)

    def __str__(self):
        return u"Circle with radius: {:f}".format(self.radius)

    def __repr__(self):
        return u"Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius