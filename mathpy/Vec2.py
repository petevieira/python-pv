#!/usr/bin/env python

import math

class Vec2():

	def __init__(self, *args):
		if len(args) == 2:
			self.__initialize_from_xy(*args)
		elif len(args) == 1:
			arg_type = type(*args)
			if arg_type is int or arg_type is float:
				self.__initialize_from_scalar(*args)
			elif arg_type is tuple or arg_type is list:
				self.__initialize_from_tuple(*args)
			else:
				print "error"

	def __initialize_from_xyz(self, x, y):
		self.x = x
		self.y = y

	def __initialize_from_tuple(self, xy):
		self.x = xyz[0]
		self.y = xyz[1]

	def __initialize_from_scalar(self, scalar):
		self.x = scalar
		self.y = scalar

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		else:
			print "index out of bounds"

	def __setitem__(self, index, value):
		if index == 0:
			self.x = value
		elif index == 1:
			self.y = value
		else:
			print "index out of bounds"

	def x(self):
		return self.x

	def y(self):
		return self.y

	def __len__(self):
		return 2

	def __add__(self, vec2):
		return Vec2(self.x + vec2.x,
			self.y + vec2.y)

	def __sub__(self, vec2):
		return Vec2(self.x - vec2.x,
			self.y - vec2.y)

	def __mul__(self, scalar):
		return Vec2(self.x*scalar, self.y*scalar)

	def __div__(self, scalar):
		return Vec2(self.x/scalar, self.y/scalar)

	def __radd__(self, vec2):
		return Vec2(self.x + vec2.x,
			self.y + vec2.y,)

	def __rsub__(self, vec2):
		return Vec2(self.x - vec2.x,
			self.y - vec2.y)

	def __rmul__(self, scalar):
		return Vec2(self.x*scalar, self.y*scalar)

	def __rdiv__(self, scalar):
		return Vec2(self.x/scalar, self.y/scalar)

	def __iadd__(self, vec2):
		return Vec2(self.x, self.y) + vec2

	def __isub__(self, vec2):
		return Vec2(self.x, self.y) - vec2

	def __imul__(self, scalar):
		return Vec2(self.x, self.y) * scalar

	def __idiv__(self, scalar):
		return Vec2(self.x, self.y) / scalar

	def __eq__(self, vec2):
		return self.x == vec2.x and self.y == vec2.y

	def __ne__(self, vec2):
		return self.x != vec2.x or self.y != vec2.y

	def __neg__(self):
		return Vec2(-self.x, -self.y)

	def __abs__(self):
		return Vec2(abs(self.x), abs(self.y))

	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	def norm(self):
		return math.sqrt(self.x*self.x + self.y*self.y)

	def norm2(self):
		return self.x*self.x + self.y*self.y

	def normalize(self):
		mag = self.norm()
		return Vec2(self.x/mag, self.y/mag)

	def dot(self, vec2):
		return (self.x * vec2.x +
			self.y * vec2.y)

	@staticmethod
	def lerp(vec1, vec2, u):
		if u < 0: return vec1
		if u > 1: return vec2
		return (1-u)*vec1 + u*vec2
