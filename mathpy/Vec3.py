#!/usr/bin/env python

import math # for trigonometry and square-root

class Vec3():
	""" 3D vector of floats
	"""

	def __init__(self, *args):
		""" Constructs Vec3 object from 3D-tuple, 3 scalars or 1 scalar

		Args:
		  *args: list of arguments.
		    3D tuple: sets Vec3 data from tuple values 
		    3 scalars: sets Vec3 data from three floats or integers
		    1 scalar: sets Vec3 data from a single float or integer

		"""
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
		""" Initializes the Vec3 data from three floats

		Args:
		  x (float): x component of the vector
		  y (float): y component of the vector
		  z (float): z component of the vector

		"""
		self.x = x
		self.y = y
		self.z = z

	def __initialize_from_tuple(self, xyz):
		""" Initializes the 3D vector from a tuple of length three.

		Args:
		  xyz (tuple): Tuple containing three values, index-0 for the x
		              component, index-1 for the y component and 
		              index-2 for the z component of the vector.

		"""
		self.x = xyz[0]
		self.y = xyz[1]
		self.z = xyz[2]

	def __initialize_from_scalar(self, scalar):
		""" Initilizes the 3D vector from a single float

		Args:
		  scalar (float): Sets all the components of the vector
		                  the scalar value

		"""
		self.x = scalar
		self.y = scalar
		self.z = scalar

	def x(self):
		""" Gets the x-component of the 3D vector

		Returns:
		  Float corresponding to the x-component 
		  of the 3D vector

		"""
		return self.x

	def y(self):
		""" Gets the y-component of the 3D vector

		Returns:
		  Float corresponding to the y-component 
		  of the 3D vector

		"""
		return self.y

	def z(self):
		""" Gets the z-component of the 3D vector

		Returns:
		  Float corresponding to the z-component 
		  of the 3D vector

		"""
		return self.z

	def roll(self):
		""" Returns the roll Euler angle (x)
		"""
		return self.x

	def pitch(self):
		""" Returns the pitch Euler angle (y)
		"""
		return self.y

	def yaw(self):
		""" Returns the yaw Euler angle (z)
		"""
		return self.z

	def __getitem__(self, index):
		""" Gets a component of the 3D vector using an
		    index value (eg. vec[0], vec[1] or vec[2])

		Args:
		  index (int): Integer index number. Range 0 to 2.

		"""
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		elif index == 2:
			return self.z
		else:
			print "index out of bounds"

	def __setitem__(self, index, value):
		""" Sets a compement specified by "index" to
		    the user specified "value"

		Args:
		  index (int): Index number. Range 0 to 2.
		  value (float): Value to set the vector component
		                 at "index" to.

		"""
		if index == 0:
			self.x = value
		elif index == 1:
			self.y = value
		elif index == 2:
			self.z = value
		else:
			print "index out of bounds"

	def __len__(self):
		""" Length of this vector

		Returns:
		  The length of Vec3, which is 3
		"""
		return 3

	def __add__(self, vec2):
		""" Adds vec2 to this vector and returns the result

		Args:
		  vec2 (Vec3): Vector to add to this vector.

		Returns:
		  Resulting Vec3 vector from the addition

		"""
		return Vec3(self.x + vec2.x,
			self.y + vec2.y,
			self.z + vec2.z)

	def __sub__(self, vec2):
		""" Subtracts vec2 from this vector and returns the result

		Args:
		  vec2 (Vec3): Vector to subtract from this vector.

		Returns:
		  Resulting Vec3 vector from the subtraction.

		"""
		return Vec3(self.x - vec2.x,
			self.y - vec2.y,
			self.z - vec2.z)

	def __mul__(self, scalar):
		""" Multiplies this vector by a scalar

		Args:
		  scalar (float): Number to multiply this vector by

		Returns:
		  Resulting Vec3 vector from the multiplication.

		"""
		return (Vec3(self.x*scalar, self.y*scalar, self.z*scalar))

	def __div__(self, scalar):
		""" Divides the Vec3 components by a scalar

		Args:
		  scalar (float): Number to divide this vector by

		Returns:
		  Resulting Vec3 vector from the division

		"""
		return (Vec3(self.x/scalar, self.y/scalar, self.z/scalar))

	def __radd__(self, vec2):
		""" Adds vec2 vector to this vector

		Args:
		  vec2 (Vec3): Vector to add to this vector

		Returns:
		  Resulting vector from the addition

		"""
		return Vec3(self.x + vec2.x,
			self.y + vec2.y,
			self.z + vec2.z)

	def __rsub__(self, vec2):
		""" Subtracts vec2 vector from this vector

		Args:
		  vec2 (Vec3): Vector to subtract from this vector

		Returns:
		  Resulting vector from the subtraction

		"""
		return Vec3(self.x - vec2.x,
			self.y - vec2.y,
			self.z - vec2.z)

	def __rmul__(self, scalar):
		""" Multiplies this vector by scalar

		Args:
		  scalar (float): Scalar to multiply this vector by

		Returns:
		  Resulting vector from the multiplication

		"""
		return (Vec3(self.x*scalar, self.y*scalar, self.z*scalar))

	def __rdiv__(self, scalar):
		""" Divides this vector by scalar

		Args:
		  scalar (float): Scalar to divide this vector by

		Returns:
		  Resulting vector from the division

		"""
		return (Vec3(self.x/scalar, self.y/scalar, self.z/scalar))

	def __iadd__(self, vec2):
		""" Adds vec2 vector to this vector in place

		Args:
		  vec2 (Vec3): Vector to add to this vector

		Returns:
		  Resulting vector from the addition and modifies this vector

		"""
		return Vec3(self.x, self.y, self.z) + vec2

	def __isub__(self, vec2):
		""" Subtracts vec2 vector from this vector in place

		Args:
		  vec2 (Vec3): Vector to subtract from this vector

		Returns:
		  Resulting vector from the subtraction and modifies this vector

		"""
		return Vec3(self.x, self.y, self.z) - vec2

	def __imul__(self, scalar):
		""" Multiplies this vector by scalar in place

		Args:
		  scalar (float): Scalar to multiply this vector by

		Returns:
		  Resulting vector from the multiplication and modifies this vector

		"""
		return Vec3(self.x, self.y, self.z) * scalar

	def __idiv__(self, scalar):
		""" Divides this vector by scalar in place

		Args:
		  scalar (float): Scalar to divide this vector by

		Returns:
		  Resulting vector from the division and modifies this vector

		"""
		return Vec3(self.x, self.y, self.z) / scalar

	def __eq__(self, vec2):
		""" Checks for equality with vec2

		Args:
		  vec2 (Vec3): Vector to compare this vector with

		Returns:
		  True if they are equal, False if not

		"""
		return self.x == vec2.x and self.y == vec2.y and self.z == vec2.z

	def __ne__(self, vec2):
		""" Checks for inequality with vec2

		Args:
		  vec2 (Vec3): Vector to compare this vector with

		Returns:
		  False if they are equal, True if not

		"""
		return self.x != vec2.x or self.y != vec2.y or self.z != vec2.z

	def __neg__(self):
		""" Negates the components of this vector

		Returns:
		  Negated vector

		"""
		return Vec3(-self.x, -self.y, -self.z)

	def __abs__(self):
		""" Performs absolute value on components of this vector

		Returns:
		  The resulting vector with each component positive

		"""
		return Vec3(abs(self.x), abs(self.y), abs(self.z))

	def __str__(self):
		""" Creates string from vector

		Returns:
		  String version of this vector

		"""
		return "({0}, {1}, {2})".format(self.x, self.y, self.z)

	def norm(self):
		""" Computes the L-2 norm of this vector

		Returns:
		  The L-2 norm of this vector

		"""
		return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

	def norm2(self):
		""" Computes the L-1 norm of this vector

		Returns:
		  The L-1 of this vector

		"""
		return self.x*self.x + self.y*self.y + self.z*self.z

	def normalize(self):
		""" Normalizes this vector so that the sum of the components is 1.0

		Returns:
		  The normalized vector

		"""
		mag = self.norm()
		return Vec3(self.x/mag, self.y/mag, self.z/mag)

	def dot(self, vec2):
		""" Takes the dot product of this Vec3 with vec2

		Args:
		  vec2 (Vec3): Vector to dot this vector with

		Returns:
		  Resulting scalar from the dot product operation

		"""
		return (self.x * vec2.x +
			self.y * vec2.y +
			self.z * vec2.z)

	def cross(self, vec2):
		""" Computes the cross product of this vector with vec2

		Args:
		  vec2 (Vec3): Vector to cross with

		Returns:
		  Resulting vector from cross product

		"""
		x = (self.y * vec2.z) - (self.z * vec2.y)
		y = (self.z * vec2.x) - (self.x * vec2.z)
		z = (self.x * vec2.y) - (self.y * vec2.x)
		return Vec3(x, y, z)

	@staticmethod
	def lerp(vec1, vec2, u):
		""" Linearly interpolates between vec1 and vec2 by percentage u

		Args:
		  vec1 (Vec3): Starting vector
		  vec2 (Vec3): Ending vector
		  u (float): Percentage of interpolation

		Returns:
		  Resulting vector from interpolation

		"""
		if u < 0: return vec1
		if u > 1: return vec2
		return (1-u)*vec1 + u*vec2
