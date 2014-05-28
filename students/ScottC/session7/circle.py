#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):

        self.radius = radius

    # def _get_radius(selfz):
    #     return self.value
    
    # def _set_radius(self, value):
    #     self.radius = value

    def _get_diameter(self):
        return self.radius * 2

    def _set_diameter(self, diameter):
        self.radius = diameter / 2

    diameter = property(_get_diameter, _set_diameter)

    def _get_area(self):
        return math.pi * (self.radius ** 2)

    area = property(_get_area)