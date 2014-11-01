#!/usr/bin/env python

from Vec3 import *

XX = 0; XY = 1
YX = 2; YY = 3

class Mat2:

  def __init__(self, *args):
    self.data = ([
      0.0, 0.0
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
    return Mat3(
      v1[0], v2[0],
      v1[1], v2[1])

  def transpose(self):
    transpose_data = self.data

    transpose_indices = ([
      XX, YX,
      XY, YY])

    for i in range(0,9):
      transpose_data[i] = data[transpose_indices[i]]

    return transpose_data

  def row(self, i):
    return Vec2(self.data[2*i+0], self.data[2*i+1])

  def col(self, i):
    return Vec2(self.data[i+0], self.data[i+2])

  def set_row(self, i, vec):
    self.data[3*i+0] = vec[0]
    self.data[3*i+1] = vec[1]

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
    return row * 3 + col

  @staticmethod
  def cross(self, vec):
    mat = Mat3()
    mat[0,0] =    0 ; mat[0,1] = -v[2]; mat[0,2] =  v[1]
    mat[1,0] =  v[2]; mat[1,1] =    0 ; mat[1,2] = -v[0]
    mat[2,0] = -v[1]; mat[2,1] =  v[0]; mat[2,2] =    0
    return m

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
    ret_mat = Mat3()
    for i in range(0,3):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    ret_mat = Mat3()
    for i in range(0,3):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, mat):
    ret_mat = Mat2()
    for row in range(0,1):
      for col in range(0,1):
        val = 0.0
        for i in range(0,2):
          val += self.data[row*2+i] * mat(i, col);
        ret_mat[row, col] = val
    return ret_mat

  def __str__(self):
    return "{} {} {}\n{} {} {}\n{} {} {}".format(
      self.data[XX], self.data[XY]
      self.data[YX], self.data[YY])