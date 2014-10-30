#!/usr/bin/env python

from Vec4 import *
from Mat3 import *

class Quat(Vec4):
	def __init__(self, *args):
		Vec4.__init__(self, 0, 0, 0, 1)
		if len(args) == 0:
			Vec4.__init__(self, 0, 0, 0, 1)
		elif len(args) == 4:
			Vec4.__init__(self, *args)
		elif len(args) == 1:
			if isinstance(args[0], int) or isinstance(args[0], float):
				Vec4.initialize_from_scalar(self, *args)
			elif isinstance(args[0], tuple) or isinstance(args[0], list):
				Vec4.initialize_from_tuple(self, *args)
			elif isinstance(args[0], Vec4):
				self.__initialize_from_vec4(*args)
			elif isinstance(args[0], Mat3):
				self.__initialize_from_mat3(*args)
			else:
				print "Error initializing Vec4. Invalid type {}".format(arg_type)
		else:
			print "Error initializing Vec4. Valid number of arguments "
			print "is 1 or 4. You pass {} arguments".format(len(args))

	def __initialize_from_vec4(self, vec):
		print "initializing from vec4"
		Vec4.__init__(self, vec.x, vec.y, vec.z, vec.w)

	def __initialize_from_mat3(self, mat):
		m00 = mat[0]; m01 = mat[1]; m02 = mat[2]
		m10 = mat[3]; m11 = mat[4]; m12 = mat[5]
		m20 = mat[6]; m21 = mat[7]; m22 = mat[8]

	def __str__(self):
		return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)

	def from_axis_angle(axis, angle):
		axis_norm = axis.norm()
		sine_angle = sin(angle/2)
		x = axis.x() * sine_angle / axis_norm
		y = axis.y() * sine_angle / axis_norm
		z = axis.z() * sine_angle / axis_norm
		u = cos(angle/2)
		return Quat(x, y, z, u)