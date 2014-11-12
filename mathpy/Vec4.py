#!/usr/bin/env python

import math # for trigonometry and square-root

class Vec4():
	""" 4D vector of floats
	"""

	def __init__(self, *args):
		""" Constructs Vec4 object from 4D-tuple, 4 scalars or 1 scalar

		Args:
		  *args: list of arguments.
		    4D tuple: sets Vec4 data from tuple values 
		    4 scalars: sets Vec4 data from four floats or integers
		    1 scalar: sets Vec4 data from a single float or integer

		"""
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
		""" Initializes the Vec4 data from four floats

		Args:
		  x (float): x component of the vector
		  y (float): y component of the vector
		  z (float): z component of the vector
		  w (float): w component of the vector

		"""
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	def __initialize_from_tuple(self, xyzw):
		""" Initializes the 4D vector from a tuple of length four.

		Args:
		  xyz (tuple): Tuple containing three values, index-0 for the x
		              component, index-1 for the y component, 
		              index-2 for the z component and index-3 for
		              the w component of the vector.

		"""
		self.x = xyzw[0]
		self.y = xyzw[1]
		self.z = xyzw[2]
		self.w = xyzw[3]

	def __initialize_from_scalar(self, scalar):
		""" Initilizes the 4D vector from a single float

		Args:
		  scalar (float): Sets all the components of the vector
		                  the scalar value

		"""
		self.x = scalar
		self.y = scalar
		self.z = scalar
		self.w = scalar

	def x(self):
		""" Gets the x-component of the 4D vector

		Returns:
		  Float corresponding to the x-component 
		  of the 4D vector

		"""
		return self.x

	def y(self):
		""" Gets the y-component of the 4D vector

		Returns:
		  Float corresponding to the y-component 
		  of the 4D vector

		"""
		return self.y

	def z(self):
		""" Gets the z-component of the 4D vector

		Returns:
		  Float corresponding to the z-component 
		  of the 4D vector

		"""
		return self.z

	def w(self):
		""" Gets the w-component of the 4D vector

		Returns:
		  Float corresponding to the w-component 
		  of the 4D vector

		"""
		return self.w

	def __getitem__(self, index):
		""" Gets a component of the 4D vector using an
		  index value (eg. vec[0], vec[1], vec[2], or vec[3])

		Args:
		  index (int): Integer index number. Range 0 to 3.

		"""
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
		""" Sets a compement specified by "index" to
		    the user specified "value"

		Args:
		  index (int): Index number. Range 0 to 3.
		  value (float): Value to set the vector component
		                 at "index" to.

		"""
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
		""" Length of this vector

		Returns:
		  The length of Vec4, which is 4
		"""
		return 4

	def __add__(self, vec2):
		""" Adds vec2 to this vector and returns the result

		Args:
		  vec2 (Vec4): Vector to add to this vector.

		Returns:
		  Resulting Vec4 vector from the addition

		"""
		return Vec4(self.x + vec2.x, self.y + vec2.y,
			self.z + vec2.z, self.w + vec2.w)

	def __sub__(self, vec2):
		""" Subtracts vec2 from this vector and returns the result

		Args:
		  vec2 (Vec4): Vector to subtract from this vector.

		Returns:
		  Resulting Vec4 vector from the subtraction.

		"""
		return Vec4(self.x - vec2.x, self.y - vec2.y,
			self.z - vec2.z, self.w - vec2.w)

	def __mul__(self, scalar):
		""" Multiplies this vector by a scalar

		Args:
		  scalar (float): Number to multiply this vector by

		Returns:
		  Resulting Vec4 vector from the multiplication.

		"""
		return (Vec4(self.x*scalar, self.y*scalar,
			self.z*scalar, self.w*scalar))

	def __div__(self, scalar):
		""" Divides the Vec4 components by a scalar

		Args:
		  scalar (float): Number to divide this vector by

		Returns:
		  Resulting Vec4 vector from the division

		"""
		return (Vec4(self.x/scalar, self.y/scalar, 
			self.z/scalar, self.w/scalar))

	def __radd__(self, vec2):
		""" Adds vec2 vector to this vector

		Args:
		  vec2 (Vec4): Vector to add to this vector

		Returns:
		  Resulting vector from the addition

		"""
		return Vec4(self.x + vec2.x, self.y + vec2.y,
			self.z + vec2.z, self.w + vec2.w)

	def __rsub__(self, vec2):
		""" Subtracts vec2 vector from this vector

		Args:
		  vec2 (Vec4): Vector to subtract from this vector

		Returns:
		  Resulting vector from the subtraction

		"""
		return Vec4(self.x - vec2.x, self.y - vec2.y,
			self.z - vec2.z, self.w - vec2.w)

	def __rmul__(self, scalar):
		""" Multiplies this vector by scalar

		Args:
		  scalar (float): Scalar to multiply this vector by

		Returns:
		  Resulting vector from the multiplication

		"""
		return (Vec4(self.x*scalar, self.y*scalar,
			self.z*scalar, self.w*scalar))

	def __rdiv__(self, scalar):
		""" Divides this vector by scalar

		Args:
		  scalar (float): Scalar to divide this vector by

		Returns:
		  Resulting vector from the division

		"""
		return (Vec4(self.x/scalar, self.y/scalar,
			self.z/scalar, self.w/scalar))

	def __iadd__(self, vec2):
		""" Adds vec2 vector to this vector in place

		Args:
		  vec2 (Vec4): Vector to add to this vector

		Returns:
		  Resulting vector from the addition and modifies this vector

		"""
		return Vec4(self.x, self.y, self.z, self.w) + vec2

	def __isub__(self, vec2):
		""" Subtracts vec2 vector from this vector in place

		Args:
		  vec2 (Vec4): Vector to subtract from this vector

		Returns:
		  Resulting vector from the subtraction and modifies this vector

		"""
		return Vec4(self.x, self.y, self.z, self.w) - vec2

	def __imul__(self, scalar):
		""" Multiplies this vector by scalar in place

		Args:
		  scalar (float): Scalar to multiply this vector by

		Returns:
		  Resulting vector from the multiplication and modifies this vector

		"""
		return Vec4(self.x, self.y, self.z, self.w) * scalar

	def __idiv__(self, scalar):
		""" Divides this vector by scalar in place

		Args:
		  scalar (float): Scalar to divide this vector by

		Returns:
		  Resulting vector from the division and modifies this vector

		"""
		return Vec4(self.x, self.y, self.z, self.w) / scalar

	def __eq__(self, vec2):
		""" Checks for equality with vec2

		Args:
		  vec2 (Vec4): Vector to compare this vector with

		Returns:
		  True if they are equal, False if not

		"""
		return (self.x == vec2.x and self.y == vec2.y
			and self.z == vec2.z and self.w == vec2.w)

	def __ne__(self, vec2):
		""" Checks for inequality with vec2

		Args:
		  vec2 (Vec4): Vector to compare this vector with

		Returns:
		  False if they are equal, True if not

		"""
		return (self.x != vec2.x or self.y != vec2.y
			or self.z != vec2.z or self.w != vec2.w)

	def __neg__(self):
		""" Negates the components of this vector

		Returns:
		  Negated vector

		"""
		return Vec4(-self.x, -self.y, -self.z, -self.w)

	def __abs__(self):
		""" Performs absolute value on components of this vector

		Returns:
		  The resulting vector with each component positive

		"""
		return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

	def __str__(self):
		""" Creates string from vector

		Returns:
		  String version of this vector

		"""
		return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)

	def norm(self):
		""" Computes the L-2 norm of this vector

		Returns:
		  The L-2 norm of this vector

		"""
		return math.sqrt(self.x*self.x + self.y*self.y
			+ self.z*self.z + self.w*self.w)

	def norm2(self):
		""" Computes the L-1 norm of this vector

		Returns:
		  The L-1 of this vector

		"""
		return (self.x*self.x + self.y*self.y
			+ self.z*self.z + self.w*self.w)

	def normalize(self):
		""" Normalizes this vector so that the sum of the components is 1.0

		Returns:
		  The normalized vector

		"""
		mag = self.norm()
		return Vec4(self.x/mag, self.y/mag, self.z/mag, self.w/mag)

	def dot(self, vec2):
		""" Takes the dot product of this Vec4 with vec2

		Args:
		  vec2 (Vec4): Vector to dot this vector with

		Returns:
		  Resulting scalar from the dot product operation

		"""
		return (self.x*vec2.x + self.y*vec2.y +
			self.z*vec2.z + self.w*vec2.w)

	@staticmethod
	def lerp(vec1, vec2, u):
		""" Linearly interpolates between vec1 and vec2 by percentage u

		Args:
		  vec1 (Vec4): Starting vector
		  vec2 (Vec4): Ending vector
		  u (float): Percentage of interpolation

		Returns:
		  Resulting vector from interpolation

		"""
		if u < 0: return vec1
		if u > 1: return vec2
		return (1-u)*vec1 + u*vec2