#!/usr/bin/env python

from Vec3 import *

# Labeled indices of the matrix
XX = 0; XY = 1
YX = 2; YY = 3

class Mat2:
  """ 2x2 Matrix class.
  """
  def __init__(self, *args):
    """ Constructs a 2x2 matrix from a Mat2 or 4 scalars
    """
    self.data = ([
      0.0, 0.0,
      0.0, 0.0])
    if len(args) == 1:
      if isinstance(args[0], Mat2):
        self.__initialize_from_mat2(*args)
    elif len(args) == 4:
      self.__initialize_from_row_major_ret_mat(*args)

  def __initialize_from_row_major_ret_mat(self, 
    m00, m01,
    m10, m11):
    self.data = (
      m00, m01,
      m10, m11)

  def __initialize_from_mat2(self, mat):
    for i in range(0,3):
      self.data[i] = mat[i]

  @classmethod
  def from_rows(self, v1, v2):
    self.data[XX] = v1[0]; self.data[XY] = v1[1]
    self.data[YX] = v2[0]; self.data[YY] = v2[1]

  @classmethod
  def from_cols(self, v1, v2):
    return Mat2(
      v1[0], v2[0],
      v1[1], v2[1])

  @classmethod
  def from_angle(self, theta):
    cos_theta = cos(theta)
    sin_theta = sin(theta)
    return Mat2(
      cos_theta, -sin_theta,
      sin_theta,  cos_theta)

  def transpose(self):
    transpose_data = self.data

    transpose_indices = ([
      XX, YX,
      XY, YY])

    for i in range(0,3):
      transpose_data[i] = data[transpose_indices[i]]

    return Mat2(transpose_data)

  def row(self, i):
    return Vec2(self.data[2*i+0], self.data[2*i+1])

  def col(self, i):
    return Vec2(self.data[i+0], self.data[i+2])

  def set_row(self, i, vec):
    self.data[2*i+0] = vec[0]
    self.data[2*i+1] = vec[1]

  def set_col(self, i, vec):
    self.data[i+0] = vec[0]
    self.data[i+2] = vec[1]

  def determinant(self):
    return (self.data[XX] * self.data[YY]
      - self.data[XY] * self.data[YX])

  def det(self):
    return self.determinant()

  def inverse(self):
    inv_det = 1/self.determinant()
    m = Mat2()
    m[XX] = self.data[YY] * inv_det;  m[XY] = -self.data[XY] * inv_det
    m[XZ] = -self.data[YX] * inv_det; m[YX] = self.data[XX] * inv_det
    return m;

  def inv(self):
    return self.inverse()

  def rowcol_to_index(self, row, col):
    return row * 1 + col

  @staticmethod
  def outer(self, vec1, vec2):
    ret_mat = Mat2()
    for row in range(0,1):
      for col in range(0,1):
        ret_mat[row, col] = vec1[row] * vec2[col]
    return ret_mat

  @staticmethod
  def mul(self, mat1, mat2):
    ret_mat = Mat2()
    for row in range(0,1):
      for col in range(0,1):
        val = 0.0
        for i in range(0,1):
          val += mat1[row, i] * mat2[i, col]
        ret_mat[row, col] = val
    return ret_mat

  @staticmethod
  def identity():
    identity = ([
      1.0, 0.0,
      0.0, 1.0])
    return identity

  @staticmethod
  def zeros():
    return Mat2(
      0.0, 0.0,
      0.0, 0.0)

  @staticmethod
  def ones():
    return Mat2(
      1.0, 1.0,
      1.0, 1.0)

  def __getitem__(self, *args):
    if len(args) == 1:
      return self.data[args[0]]
    elif len(args) == 2:
      return self.data[rowcol_to_index(args[0], args[1])]
    else:
      print "Error. Invalid number of index args: {}.".format(len(args))
      print "Valid numbers are 1 and 2"

  def __setitem__(self, value, row, col):
    self.data[rowcol_to_index(row, col)] = value

  def __call__(self, row, col):
    return self.data[rowcol_to_index(row, col)]

  def __eq__(self, ret_mat):
    for i in range(0,3):
      if self.data[i] != ret_mat[i]:
        return False
    return True

  def __ne__(self, ret_mat):
    for i in range[0,3]:
      if self.data[i] == ret_mat[i]:
        return False
    return True

  def __neg__(self):
    ret_mat = self.data
    for i in range(0,3):
      ret_mat[i] = -ret_mat[i]
    return ret_mat

  def __add__(self, mat):
    ret_mat = Mat2()
    for i in range(0,3):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    ret_mat = Mat2()
    for i in range(0,3):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, mat):
    ret_mat = Mat2()
    for row in range(0,1):
      for col in range(0,1):
        val = 0.0
        for i in range(0,1):
          val += self.data[row*2+i] * mat(i, col);
        ret_mat[row, col] = val
    return ret_mat

  def __str__(self):
    return "{} {}\n{} {}\n{} {}".format(
      self.data[XX], self.data[XY],
      self.data[YX], self.data[YY])