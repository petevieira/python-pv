#!/usr/bin/env python

import math # for trigonometry and square-root

class Vec2():
	""" 2D vector of floats
	"""

	def __init__(self, *args):
		""" Constructs Vec2 object from 2D-tuple, 2 scalars or 1 scalar

		Args:
		  *args: list of arguments.
		    2D tuple: sets Vec2 data from tuple values 
		    2 scalars: sets Vec2 data from two floats or integers
		    1 scalar: sets Vec2 data from a single float or integer

		"""
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

	def __initialize_from_xy(self, x, y):
		""" Initializes the Vec2 data from two floats

		Args:
		  x (float): x component of the vector
		  y (float): y component of the vector

		"""
		self.x = x
		self.y = y

	def __initialize_from_tuple(self, xy):
		""" Initializes the 2D vector from a tuple of length two.

		Args:
		  xy (tuple): Tuple containing two values, index-0 for the x
		              component and index-1 for the y component of
		              the vector.

		"""
		self.x = xy[0]
		self.y = xy[1]

	def __initialize_from_scalar(self, scalar):
		""" Initilizes the 2D vector from a single float

		Args:
		  scalar (float): Sets all the components of the vector
		                  the scalar value

		"""
		self.x = scalar
		self.y = scalar

	def __getitem__(self, index):
		""" Gets a component of the 2D vector using an
		    index value (eg. vec[0] or vec[1])

		Args:
		  index (int): Integer index number. Range 0 to 1.

		"""
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		else:
			print "index out of bounds"

	def __setitem__(self, index, value):
		""" Sets a compement specified by "index" to
		    the user specified "value"

		Args:
		  index (int): Index number. Range 0 to 1.
		  value (float): Value to set the vector component
		                 at "index" to.

		"""

		if index == 0:
			self.x = value
		elif index == 1:
			self.y = value
		else:
			print "index out of bounds"

	def x(self):
		""" Gets the x-component of the 2D vector

		Returns:
		  Float corresponding to the x-component 
		  of the 2D vector

		"""

		return self.x

	def y(self):
		""" Gets the y-component of the 2D vector

		Returns:
		  Float corresponding to the y-component 
		  of the 2D vector

		"""

		return self.y

	def __len__(self):
		""" Gets the length of the vector

		Returns:
		  Integer corresponding to the length of
		  the vector.

		"""

		return 2

	def __add__(self, vec2):
		""" Adds vec2 to this vector and returns the result

		Args:
		  vec2 (Vec2): Vector to add to this vector.

		Returns:
		  Resulting Vec2 vector from the addition

		"""

		return Vec2(self.x + vec2.x,
			self.y + vec2.y)

	def __sub__(self, vec2):
		""" Subtracts vec2 from this vector and returns the result

		Args:
		  vec2 (Vec2): Vector to subtract from this vector.

		Returns:
		  Resulting Vec2 vector from the subtraction.

		"""

		return Vec2(self.x - vec2.x,
			self.y - vec2.y)

	def __mul__(self, scalar):
		""" Multiplies this vector by a scalar

		Args:
		  scalar (float): Number to multiply this vector by

		Returns:
		  Resulting Vec2 vector from the multiplication.

		"""

		return Vec2(self.x*scalar, self.y*scalar)

	def __div__(self, scalar):
		""" Divides the Vec2 components by a scalar

		Args:
		  scalar (float): Number to divide this vector by

		Returns:
		  Resulting Vec2 vector from the division

		"""
		return Vec2(self.x/scalar, self.y/scalar)

	def __radd__(self, vec2):
		""" Adds vec2 vector to this vector

		Args:
		  vec2 (Vec2): Vector to add to this vector

		Returns:
		  Resulting vector from the addition

		"""
		return Vec2(self.x + vec2.x,
			self.y + vec2.y,)

	def __rsub__(self, vec2):
		""" Subtracts vec2 vector from this vector

		Args:
		  vec2 (Vec2): Vector to subtract from this vector

		Returns:
		  Resulting vector from the subtraction

		"""
		return Vec2(self.x - vec2.x,
			self.y - vec2.y)

	def __rmul__(self, scalar):
		""" Multiplies this vector by scalar

		Args:
		  scalar (float): Scalar to multiply this vector by

		Returns:
		  Resulting vector from the multiplication

		"""
		return Vec2(self.x*scalar, self.y*scalar)

	def __rdiv__(self, scalar):
		""" Divides this vector by scalar

		Args:
		  scalar (float): Scalar to divide this vector by

		Returns:
		  Resulting vector from the division

		"""
		return Vec2(self.x/scalar, self.y/scalar)

	def __iadd__(self, vec2):
		""" Adds vec2 vector to this vector in place

		Args:
		  vec2 (Vec2): Vector to add to this vector

		Returns:
		  Resulting vector from the addition and modifies this vector

		"""
		return Vec2(self.x, self.y) + vec2

	def __isub__(self, vec2):
		""" Subtracts vec2 vector from this vector in place

		Args:
		  vec2 (Vec2): Vector to subtract from this vector

		Returns:
		  Resulting vector from the subtraction and modifies this vector

		"""
		return Vec2(self.x, self.y) - vec2

	def __imul__(self, scalar):
		""" Multiplies this vector by scalar in place

		Args:
		  scalar (float): Scalar to multiply this vector by

		Returns:
		  Resulting vector from the multiplication and modifies this vector

		"""
		return Vec2(self.x, self.y) * scalar

	def __idiv__(self, scalar):
		""" Divides this vector by scalar in place

		Args:
		  scalar (float): Scalar to divide this vector by

		Returns:
		  Resulting vector from the division and modifies this vector

		"""
		return Vec2(self.x, self.y) / scalar

	def __eq__(self, vec2):
		""" Checks for equality with vec2

		Args:
		  vec2 (Vec2): Vector to compare this vector with

		Returns:
		  True if they are equal, False if not

		"""
		return self.x == vec2.x and self.y == vec2.y

	def __ne__(self, vec2):
		""" Checks for inequality with vec2

		Args:
		  vec2 (Vec2): Vector to compare this vector with

		Returns:
		  False if they are equal, True if not

		"""
		return self.x != vec2.x or self.y != vec2.y

	def __neg__(self):
		""" Negates the components of this vector

		Returns:
		  Negated vector

		"""
		return Vec2(-self.x, -self.y)

	def __abs__(self):
		""" Performs absolute value on components of this vector

		Returns:
		  The resulting vector with each component positive

		"""
		return Vec2(abs(self.x), abs(self.y))

	def __str__(self):
		""" Creates string from vector

		Returns:
		  String version of this vector

		"""
		return "({0}, {1})".format(self.x, self.y)

	def norm(self):
		""" Computes the L-2 norm of this vector

		Returns:
		  The L-2 norm of this vector

		"""
		return math.sqrt(self.x*self.x + self.y*self.y)

	def norm2(self):
		""" Computes the L-1 norm of this vector

		Returns:
		  The L-1 of this vector

		"""
		return self.x*self.x + self.y*self.y

	def normalize(self):
		""" Normalizes this vector so that the sum of the components is 1.0

		Returns:
		  The normalized vector

		"""
		mag = self.norm()
		return Vec2(self.x/mag, self.y/mag)

	def dot(self, vec2):
		""" Takes the dot product of Vec2 with vec2

		Args:
		  vec2 (Vec2): Vector to dot this vector with

		Returns:
		  Resulting scalar from the dot product operation

		"""
		return (self.x * vec2.x +
			self.y * vec2.y)

	@staticmethod
	def lerp(vec1, vec2, u):
		""" Linearly interpolates between vec1 and vec2 by percentage u

		Args:
		  vec1 (Vec2): Starting vector
		  vec2 (Vec2): Ending vector
		  u (float): Percentage of interpolation

		Returns:
		  Resulting vector from interpolation

		"""
		if u < 0: return vec1
		if u > 1: return vec2
		return (1-u)*vec1 + u*vec2