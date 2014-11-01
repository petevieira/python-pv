#!/usr/bin/env python

from Vec4 import *
from Mat3 import *

class Quat(Vec4):
	def __init__(self, *args):
		Vec4.__init__(self, 0.0, 0.0, 0.0, 1.0)
		if len(args) == 0:
			Vec4.__init__(self, 0.0, 0.0, 0.0, 1.0)
		elif len(args) == 4:
			Vec4.__init__(self, *args)
		elif len(args) == 1:
			if (isinstance(args[0], int) or isinstance(args[0], float)
				or isinstance(args[0], tuple) or isinstance(args[0], list)):
				Vec4.__init__(self, *args)
			elif isinstance(args[0], Vec4):
				self.__initialize_from_vec4(*args)
			else:
				print "Error initializing Vec4. Invalid type {}".format(type(*args))
		else:
			print "Error initializing Vec4. Valid number of arguments "
			print "is 1 or 4. You pass {} arguments".format(len(args))

	def __initialize_from_vec4(self, vec):
		Vec4.__init__(self, vec.x, vec.y, vec.z, vec.w)

	@staticmethod
	def from_axis_angle(axis, angle):
		axis_norm = axis.norm()
		sine_angle = sin(angle/2)
		x = axis.x() * sine_angle / axis_norm
		y = axis.y() * sine_angle / axis_norm
		z = axis.z() * sine_angle / axis_norm
		u = cos(angle/2)
		return Quat(x, y, z, u)

	@staticmethod
	def from_mat3(mat):
		qx, qy, qz, qw = 0.0, 0.0, 0.0, 1.0

		trace = 1 + mat[XX] + mat[YY] + mat[ZZ]
		eps = 1e-1

		if trace > eps:
			n = math.sqrt(trace);
			qx = (mat[YZ] - mat[ZY]) / n
			qy = (mat[ZX] - mat[XZ]) / n
			qz = (mat[XY] - mat[YX]) / n
			qw = n;
		else:
			trace = 1 + mat[XX] - mat[YY] - mat[ZZ]
			if trace > eps:
				n = math.sqrt(trace)
				qx = n;
				qy = (mat[XY] + mat[YX]) / n
				qz = (mat[ZX] + mat[XZ]) / n
				qw = (mat[YZ] - mat[ZY]) / n
			else:
				trace = 1 + mat[XX] + mat[YY] - mat[ZZ]
				if trace > eps:
					n = math.sqrt(trace)
					qx = (mat[XY] + mat[YX]) / n
					qy = n;
					qz = (mat[YZ] + mat[ZY]) / n
					qw = (mat[ZX] - mat[XZ]) / n
				else:
					trace = 1 - mat[XX] - mat[YY] + mat[ZZ]
					n = math.sqrt(trace)
					qx = (mat[ZX] + mat[XZ]) / n
					qy = (mat[YZ] + mat[ZY]) / n
					qz = n;
					qw = (mat[XY] - mat[YX]) / n

		return Quat(0.5*qx, 0.5*qy, 0.5*qz, 0.5*qw)

	@staticmethod
	def from_mat4(mat):
		return self.from_mat3(mat.block(0,0,3,3))

	# @staticmethod
	# def from_two_vectors(self, vec1, vec2):


	def __str__(self):
		return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)
