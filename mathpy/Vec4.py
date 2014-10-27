#!/usr/bin/env python

import math

class Vec4():

	def __init__(self, *args):
		if len(args) == 0:
			initialize_from_scalar(0, 0, 0, 0)
		elif len(args) == 4:
			self.initialize_from_floats(*args)
		elif len(args) == 1:
			arg_type = type(*args)
			if arg_type is int or arg_type is float:
				self.initialize_from_scalar(*args)
			elif arg_type is tuple or arg_type is list:
				self.initialize_from_tuple(*args)
			else:
				print "Error initializing Vec4. Invalid type {}".format(arg_type)
		else:
			print "Error initializing Vec4. Valid number of arguments "
			print "is 1 or 4. You pass {} arguments".format(len(args))

	def initialize_from_floats(self, x, y, z, u):
		self.x = x
		self.y = y
		self.z = z
		self.u = u

	def initialize_from_tuple(self, xyzu):
		self.x = xyzu[0]
		self.y = xyzu[1]
		self.z = xyzu[2]
		self.u = xyzu[3]

	def initialize_from_scalar(self, scalar):
		self.x = scalar
		self.y = scalar
		self.z = scalar
		self.u = scalar

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		elif index == 2:
			return self.z
		elif index == 3:
			return self.u
		else:
			print "index out of bounds"

	def x(self):
		return self.x

	def y(self):
		return self.y

	def z(self):
		return self.z

	def u(self):
		return self.u

	def __add__(self, vec2):
		return Vec4(self.x + vec2.x, self.y + vec2.y,
			self.z + vec2.z, self.u + vec2.u)

	def __sub__(self, vec2):
		return Vec4(self.x - vec2.x, self.y - vec2.y,
			self.z - vec2.z, self.u - vec2.u)

	def __mul__(self, scalar):
		return (Vec4(self.x*scalar, self.y*scalar,
			self.z*scalar, self.u*scalar))

	def __div__(self, scalar):
		return (Vec4(self.x/scalar, self.y/scalar, 
			self.z/scalar, self.u/scalar))

	def __radd__(self, vec2):
		return Vec4(self.x + vec2.x, self.y + vec2.y,
			self.z + vec2.z, self.u + vec2.u)

	def __rsub__(self, vec2):
		return Vec4(self.x - vec2.x, self.y - vec2.y,
			self.z - vec2.z, self.u - vec2.u)

	def __rmul__(self, scalar):
		return (Vec4(self.x*scalar, self.y*scalar,
			self.z*scalar, self.u*scalar))

	def __rdiv__(self, scalar):
		return (Vec4(self.x/scalar, self.y/scalar,
			self.z/scalar, self.u/scalar))

	def __iadd__(self, vec2):
		return Vec4(self.x, self.y, self.z, self.u) + vec2

	def __isub__(self, vec2):
		return Vec4(self.x, self.y, self.z, self.u) - vec2

	def __imul__(self, scalar):
		return Vec4(self.x, self.y, self.z, self.u) * scalar

	def __idiv__(self, scalar):
		return Vec4(self.x, self.y, self.z, self.u) / scalar

	def __eq__(self, vec2):
		return (self.x == vec2.x and self.y == vec2.y
			and self.z == vec2.z and self.u == vec2.u)

	def __ne__(self, vec2):
		return (self.x != vec2.x or self.y != vec2.y
			or self.z != vec2.z or self.u != vec2.u)

	def __neg__(self):
		return Vec4(-self.x, -self.y, -self.z, -self.u)

	def __abs__(self):
		return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.u))

	def __str__(self):
		return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.u)

	def norm(self):
		return math.sqrt(self.x*self.x + self.y*self.y
			+ self.z*self.z + self.u*self.u)

	def norm2(self):
		return (self.x*self.x + self.y*self.y
			+ self.z*self.z + self.u*self.u)

	def normalize(self):
		mag = self.norm()
		return Vec4(self.x/mag, self.y/mag, self.z/mag, self.u/mag)

	def dot(self, vec2):
		return (self.x*vec2.x + self.y*vec2.y +
			self.z*vec2.z + self.u*vec2.u)

def lerp(vec1, vec2, u):
	if u < 0: return vec1
	if u > 1: return vec2
	return (1-u)*vec1 + u*vec2
