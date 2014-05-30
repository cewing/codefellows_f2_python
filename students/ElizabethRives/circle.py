#!/usr/bin/env python


import math


class Circle(object):

	def __init__(self, radius):
		self._radius = radius

	def _get_radius(self):
		return self._radius
		
	def _get_diameter(self):
		self._diameter = self._radius * 2
		return self._diameter

	def _set_radius(self, value):
		self._radius = value
		self._diameter = value * 2

	def _set_diameter(self, value):
		self._diameter = value
		self._radius = value/2

	def _get_area(self):
		self._area = math.pi * (self._radius ** 2)
		return self._area

	radius = property(_get_radius, _set_radius)
	diameter = property(_get_diameter, _set_diameter)
	area = property(_get_area)

	def __str__(self):
		return 'Circle with radius: %.6f' % self.radius

	def __repr__(self):
		return 'Circle(%s)' % self.radius

	def __add__(self, other):
		return Circle(self.radius + other.radius) 

	def __mul__(self, other):
		return Circle(self.radius * other)

	def __eq__(self, other):
		return self.area == other.area

	def __gt__(self, other):
		return self.area > other.area

	def __lt__(self, other):
		return self.area < other.area

	def __ge__(self, other):
		return self.area >= other.area

	def __le__(self, other):
		return self.area <= other.area












		


	


    	

