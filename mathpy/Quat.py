#!/usr/bin/env python

class Vec3():

	def __init__(self, x=0, y=0, z=0, u=0):
		self.x, self.y, self.z, self.u = x, y, z, u

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		elif index == 2:
			return self.z
		elif index = 3:
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
		return Vec3(self.x + vec2.x,
			self.y + vec2.y,
			self.z + vec2.z)

	def __sub__(self, vec2):
		return Vec3(self.x - vec2.x,
			self.y - vec2.y,
			self.z - vec2.z)

	def __mul__(self, scalar):
		return (Vec3(self.x*scalar, self.y*scalar, self.z*scalar))

	def __eq__(self, vec2):
		return (self.x == vec2.x or self.y == vec2.y 
			or self.z == vec2.z or self.u == vec2.u)

	def __str__(self):
		return "({0}, {1}, {2})".format(self.x, self.y, self.z, self.u)

	def dot(self, vec2):
		return (self.x * vec2.x +
			self.y * vec2.y +
			self.z * vec2.z)

	def cross(self, vec2):
		x = (self.y * vec2.z) - (self.z * vec2.y)
		y = (self.z * vec2.x) - (self.x * vec2.z)
		z = (self.x * vec2.y) - (self.y * vec2.x)
		return Vec3(x, y, z)