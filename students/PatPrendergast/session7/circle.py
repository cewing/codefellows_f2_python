#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    ''' Creates a circle object with diameter, radius and area attributes'''

    def __init__(self, radius):
        self.radius = radius

    def diameter(self, radius):
        diameter = radius * 2
        return diameter

    def area(self, radius):
        area = math.pi * radius**2
        return area

