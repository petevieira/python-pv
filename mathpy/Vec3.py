#!/usr/bin/env python

import math

class Vec3():

	def __init__(self, *args):
		if len(args) == 3:
			self.__initialize_from_xyz(*args)
		elif len(args) == 1:
			arg_type = type(*args)
			if arg_type is int or arg_type is float:
				self.__initialize_from_scalar(*args)
			elif arg_type is tuple or arg_type is list:
				self.__initialize_from_tuple(*args)
			else:
				print "error"

	def __initialize_from_xyz(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __initialize_from_tuple(self, xyz):
		self.x = xyz[0]
		self.y = xyz[1]
		self.z = xyz[2]

	def __initialize_from_scalar(self, scalar):
		self.x = scalar
		self.y = scalar
		self.z = scalar

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		elif index == 2:
			return self.z
		else:
			print "index out of bounds"

	def __setitem__(self, index, value):
		if index == 0:
			self.x = value
		elif index == 1:
			self.y = value
		elif index == 2:
			self.z = value
		else:
			print "index out of bounds"

	def x(self):
		return self.x

	def y(self):
		return self.y

	def z(self):
		return self.z

	def roll(self):
		return self.x

	def pitch(self):
		return self.y

	def yaw(self):
		return self.z

	def __len__(self):
		return 3

	def __add__(self, vec2):
		return Vec3(self.x + vec2.x,
			self.y + vec2.y,
			self.z + vec2.z)

	def __sub__(self, vec2):
		return Vec3(self.x - vec2.x,
			self.y - vec2.y,
			self.z - vec2.z)

	def __mul__(self, scalar):
		return (Vec3(self.x*scalar, self.y*scalar, self.z*scalar))

	def __div__(self, scalar):
		return (Vec3(self.x/scalar, self.y/scalar, self.z/scalar))

	def __radd__(self, vec2):
		return Vec3(self.x + vec2.x,
			self.y + vec2.y,
			self.z + vec2.z)

	def __rsub__(self, vec2):
		return Vec3(self.x - vec2.x,
			self.y - vec2.y,
			self.z - vec2.z)

	def __rmul__(self, scalar):
		return (Vec3(self.x*scalar, self.y*scalar, self.z*scalar))

	def __rdiv__(self, scalar):
		return (Vec3(self.x/scalar, self.y/scalar, self.z/scalar))

	def __iadd__(self, vec2):
		return Vec3(self.x, self.y, self.z) + vec2

	def __isub__(self, vec2):
		return Vec3(self.x, self.y, self.z) - vec2

	def __imul__(self, scalar):
		return Vec3(self.x, self.y, self.z) * scalar

	def __idiv__(self, scalar):
		return Vec3(self.x, self.y, self.z) / scalar

	def __eq__(self, vec2):
		return self.x == vec2.x and self.y == vec2.y and self.z == vec2.z

	def __ne__(self, vec2):
		return self.x != vec2.x or self.y != vec2.y or self.z != vec2.z

	def __neg__(self):
		return Vec3(-self.x, -self.y, -self.z)

	def __abs__(self):
		return Vec3(abs(self.x), abs(self.y), abs(self.z))

	def __str__(self):
		return "({0}, {1}, {2})".format(self.x, self.y, self.z)

	def norm(self):
		return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

	def norm2(self):
		return self.x*self.x + self.y*self.y + self.z*self.z

	def normalize(self):
		mag = self.norm()
		return Vec3(self.x/mag, self.y/mag, self.z/mag)

	def dot(self, vec2):
		return (self.x * vec2.x +
			self.y * vec2.y +
			self.z * vec2.z)

	def cross(self, vec2):
		x = (self.y * vec2.z) - (self.z * vec2.y)
		y = (self.z * vec2.x) - (self.x * vec2.z)
		z = (self.x * vec2.y) - (self.y * vec2.x)
		return Vec3(x, y, z)

	@staticmethod
	def lerp(vec1, vec2, u):
		if u < 0: return vec1
		if u > 1: return vec2
		return (1-u)*vec1 + u*vec2
