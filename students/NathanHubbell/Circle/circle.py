#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self,radius):
        self._radius = radius
        self._diameter = radius*2
    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return self._diameter
    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius*2
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter/2





#class E(object):
#    def __init__(self, x=5):
#        self._x = x
#    @property
#    def x(self):
#        return self._x
#    @x.setter
#    def x(self, value):
#        self._x = value