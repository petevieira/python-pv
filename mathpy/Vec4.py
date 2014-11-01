#!/usr/bin/env python

import math

class Vec4():

	def __init__(self, *args):
		self.x, self.y, self.z, self.w = 0.0, 0.0, 0.0, 0.0
		if len(args) == 0:
			self.__initialize_from_scalar(0.0, 0.0, 0.0, 0.0)
		elif len(args) == 4:
			self.__initialize_from_floats(*args)
		elif len(args) == 1:
			arg_type = type(*args)
			if arg_type is int or arg_type is float:
				self.__initialize_from_scalar(*args)
			elif arg_type is tuple or arg_type is list:
				self.__initialize_from_tuple(*args)
			else:
				print "Error initializing Vec4. Invalid type {}".format(arg_type)
		else:
			print "Error initializing Vec4. Valid number of arguments "
			print "is 1 or 4. You pass {} arguments".format(len(args))

	def __initialize_from_floats(self, x, y, z, w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	def __initialize_from_tuple(self, xyzw):
		self.x = xyzw[0]
		self.y = xyzw[1]
		self.z = xyzw[2]
		self.w = xyzw[3]

	def __initialize_from_scalar(self, scalar):
		self.x = scalar
		self.y = scalar
		self.z = scalar
		self.w = scalar

	def x(self):
		return self.x

	def y(self):
		return self.y

	def z(self):
		return self.z

	def w(self):
		return self.w

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		elif index == 2:
			return self.z
		elif index == 3:
			return self.w
		else:
			print "index out of bounds"

	def __setitem__(self, index, value):
		if index == 0:
			self.x = value
		elif index == 1:
			self.y = value
		elif index == 2:
			self.z = value
		elif index == 3:
			self.w = value
		else:
			print "index out of bounds"

	def __len__(self):
		return 4

	def __add__(self, vec2):
		return Vec4(self.x + vec2.x, self.y + vec2.y,
			self.z + vec2.z, self.w + vec2.w)

	def __sub__(self, vec2):
		return Vec4(self.x - vec2.x, self.y - vec2.y,
			self.z - vec2.z, self.w - vec2.w)

	def __mul__(self, scalar):
		return (Vec4(self.x*scalar, self.y*scalar,
			self.z*scalar, self.w*scalar))

	def __div__(self, scalar):
		return (Vec4(self.x/scalar, self.y/scalar, 
			self.z/scalar, self.w/scalar))

	def __radd__(self, vec2):
		return Vec4(self.x + vec2.x, self.y + vec2.y,
			self.z + vec2.z, self.w + vec2.w)

	def __rsub__(self, vec2):
		return Vec4(self.x - vec2.x, self.y - vec2.y,
			self.z - vec2.z, self.w - vec2.w)

	def __rmul__(self, scalar):
		return (Vec4(self.x*scalar, self.y*scalar,
			self.z*scalar, self.w*scalar))

	def __rdiv__(self, scalar):
		return (Vec4(self.x/scalar, self.y/scalar,
			self.z/scalar, self.w/scalar))

	def __iadd__(self, vec2):
		return Vec4(self.x, self.y, self.z, self.w) + vec2

	def __isub__(self, vec2):
		return Vec4(self.x, self.y, self.z, self.w) - vec2

	def __imul__(self, scalar):
		return Vec4(self.x, self.y, self.z, self.w) * scalar

	def __idiv__(self, scalar):
		return Vec4(self.x, self.y, self.z, self.w) / scalar

	def __eq__(self, vec2):
		return (self.x == vec2.x and self.y == vec2.y
			and self.z == vec2.z and self.w == vec2.w)

	def __ne__(self, vec2):
		return (self.x != vec2.x or self.y != vec2.y
			or self.z != vec2.z or self.w != vec2.w)

	def __neg__(self):
		return Vec4(-self.x, -self.y, -self.z, -self.w)

	def __abs__(self):
		return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

	def __str__(self):
		return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)

	def norm(self):
		return math.sqrt(self.x*self.x + self.y*self.y
			+ self.z*self.z + self.w*self.w)

	def norm2(self):
		return (self.x*self.x + self.y*self.y
			+ self.z*self.z + self.w*self.w)

	def normalize(self):
		mag = self.norm()
		return Vec4(self.x/mag, self.y/mag, self.z/mag, self.w/mag)

	def dot(self, vec2):
		return (self.x*vec2.x + self.y*vec2.y +
			self.z*vec2.z + self.w*vec2.w)

	@staticmethod
	def lerp(vec1, vec2, u):
		if u < 0: return vec1
		if u > 1: return vec2
		return (1-u)*vec1 + u*vec2