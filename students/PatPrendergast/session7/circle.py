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
        return self.radius * 2

    def area(self, radius):
        return math.pi * self.radius**2
        
        
