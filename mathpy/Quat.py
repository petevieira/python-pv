#!/usr/bin/env python

from Vec4 import *
from Mat3 import *
from Mat4 import *
from math import * # for trigonometry and square root

# Labeled indices of the matrix
XX = 0; XY = 1; XZ = 2
YX = 3; YY = 4; YZ = 5
ZX = 6; ZY = 7; ZZ = 8

class Quat(Vec4):
	""" Quaternion using floats. x,y,z,w
	"""
	def __init__(self, *args):
		""" Constructs a Quaternion from 4D-tuple, 4 scalars or a Vec4

		Args:
		  *args: list of arguments.
		    4D tuple: sets Quaternion data from tuple values 
		    3 scalars: sets Quaternion data from three floats or integers
		    Vec4: sets Quaternion data from a Vec4 vector

		"""
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
		""" Initializes the Quaterion from the Vec4 vec

		Args:
		  vec (Vec4): 4D vector from which to initialize the quaternion
		              in format (x,y,z,w)

		"""
		Vec4.__init__(self, vec.x, vec.y, vec.z, vec.w)

	@staticmethod
	def from_axis_angle(axis, angle):
		""" Creates a Quaternion from an axis and an angle

		Args:
		  axis (Vec3): Axis of rotation.
		  angle (float): Angle to rotate by (radians).

		Returns:
  		Quaterions corresponding to the rotation about "axis"
  		by "angle" radians

		"""
		axis_norm = axis.norm()
		sine_angle = sin(angle/2)
		x = axis.x() * sine_angle / axis_norm
		y = axis.y() * sine_angle / axis_norm
		z = axis.z() * sine_angle / axis_norm
		u = cos(angle/2)
		return Quat(x, y, z, u)

	@staticmethod
	def from_mat3(mat):
		""" Creates a quaternion from a 3x3 matrix

		Args:
		  mat (Mat3): 3x3 matrix from which to create a quaternion

		Returns:
		  The quaternion corresponding to the 3x3 rotation matrix

		"""
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
		""" Creates a quaternion from the rotation part of a 4x4 matrix

		Args:
		  mat (Mat4): 4x4 matrix from which to create a quaternion

		Returns:
		  The quaternion corresponding to the 3x3 rotation matrix
		  inside the 4x4 matrix

		"""		
		return self.from_mat3(mat.block(0,0,3,3))

	# @staticmethod
	# def from_two_vectors(self, vec1, vec2):


	@staticmethod
	def from_euler(rpy_vec):
		""" Creates a quaternion from roll, pitch, yaw Euler angles

		Args:
		  rpy_vec (Vec3): Euler angles vector

		Returns:
		  Quaternion corresponding to the Euler angles

		"""
		Cr = cos(0.5*rpy_vec.roll())
		Cp = cos(0.5*rpy_vec.pitch())
		Cy = cos(0.5*rpy_vec.yaw())
		Sr = sin(0.5*rpy_vec.roll())
		Sp = sin(0.5*rpy_vec.pitch())
		Sy = sin(0.5*rpy_vec.yaw())

		qx = Sr*Cp*Cy - Cr*Sp*Sy
		qy = Cr*Sp*Cy + Sr*Cp*Sy
		qz = Cr*Cp*Sy - Sr*Sp*Cy
		qw = Cr*Cp*Cy + Sr*Sp*Sy

		return Quat(qx, qy, qz, qw)

	def __str__(self):
		""" Creates a string from the quaternion, to be used with print

		Returns:
		  String version of this quaternion

		"""
		return "({0}, {1}, {2}, {3})".format(self.x(), self.y(), self.z(), self.w())
