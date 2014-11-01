#!/usr/bin/env python

from Vec2 import *
from Vec3 import *

XX = 0; XY = 1; XZ = 2
YX = 3; YY = 4; YZ = 5
ZX = 6; ZY = 7; ZZ = 8

class Mat3:

  def __init__(self, *args):
    self.data = ([
      0.0, 0.0, 0.0,
      0.0, 0.0, 0.0,
      0.0, 0.0, 0.0])
    if len(args) == 1:
      if isinstance(args[0], Mat3):
        self.__initialize_from_mat3(*args)
    elif len(args) == 9:
      self.__initialize_from_row_major_ret_mat(*args)

  def __initialize_from_row_major_ret_mat(self, 
    m00, m01, m02,
    m10, m11, m12,
    m20, m21, m22):
    self.data = (
      m00, m01, m02,
      m10, m11, m12,
      m20, m21, m22)

  def __initialize_from_mat3(self, mat):
    for i in range(0,8):
      self.data[i] = mat[i]

  @classmethod
  def from_rows(self, v1, v2, v3):
    self.data[XX] = v1[0]; self.data[XY] = v1[1]; self.data[XZ] = v1[2]
    self.data[YX] = v2[0]; self.data[YY] = v2[1]; self.data[YZ] = v2[2]
    self.data[ZX] = v3[0]; self.data[ZY] = v3[1]; self.data[ZZ] = v3[2]

  @classmethod
  def from_cols(self, v1, v2, v3):
    return Mat3(
      v1[0], v2[0], v3[0],
      v1[1], v2[1], v3[1],
      v1[2], v2[2], v3[2])

  def transpose(self):
    transpose_data = self.data

    transpose_indices = ([
      XX, YX, ZX,
      XY, YY, ZY,
      XZ, YZ, ZZ])

    for i in range(0,8):
      transpose_data[i] = data[transpose_indices[i]]

    return transpose_data

  def row(self, i):
    return Vec3(self.data[3*i+0], self.data[3*i+1], self.data[3*i+2])

  def col(self, i):
    return Vec3(self.data[i+0], self.data[i+3], self.data[i+6])

  def block(self, row, col, rows, cols):
    x = self.data[rowcol_to_index(row,col)]
    # row vectors
    if rows == 1:
      if cols == 1:
        return self.data[rowcol_to_index(row,col)]
      elif cols == 2:
        assert(col <= 2)
        return Vec2(x, self.data[rowcol_to_index(row,col+1)])
      elif cols == 3:
        assert(col <= 1)
        return Vec3(
          x,
          self.data[rowcol_to_index(row,col+1)],
          self.data[rowcol_to_index(row,col+2)])
      else:
        assert 0
    # column vectors
    elif cols == 1:
      if rows == 1:
        return self.data[rowcol_to_index(row,col)]
      elif rows == 2:
        assert(row <= 2)
        return Vec2(
          x,
          self.data[rowcol_to_index(row+1,col)])
      elif rows == 3:
        assert(row <= 1)
        return Vec3(
          x,
          self.data[rowcol_to_index(row+1,col)],
          self.data[rowcol_to_index(row+2,col)])
      else:
        assert 0
    # square matrices
    elif rows == 2:
      assert cols == 2, "Error! Requested non-square matrix block of size {} by {}".format(rows, cols)
      return Mat2(
        x,
        self.data[rowcol_to_index(row,col+1)],
        self.data[rowcol_to_index(row+1,col)],
        self.data[rowcol_to_index(row+1,col+1)])
    else:
      assert 0

  def set_row(self, i, vec):
    self.data[3*i+0] = vec[0]
    self.data[3*i+1] = vec[1]
    self.data[3*i+2] = vec[2]

  def set_col(self, i, vec):
    self.data[i+0] = vec[0]
    self.data[i+3] = vec[1]
    self.data[i+6] = vec[2]    

  def determinant(self):
    return (
      self.data[XX] * (self.data[YY] * self.data[ZZ] - self.data[YZ] * self.data[ZY]) -
      self.data[XY] * (self.data[YZ] * self.data[ZX] - self.data[YX] * self.data[ZZ]) +
      self.data[XZ] * (self.data[YX] * self.data[ZY] - self.data[YY] * self.data[ZX]))

  def det(self):
    return self.determinant()

  def inverse(self):
    inv_det = 1/self.determinant()
    m = Mat3()
    m[XX] = (self.data[YY] * self.data[ZZ] - self.data[YZ] * self.data[ZY]) * inv_det;
    m[XY] = (self.data[XZ] * self.data[ZY] - self.data[XY] * self.data[ZZ]) * inv_det;
    m[XZ] = (self.data[XY] * self.data[YZ] - self.data[XZ] * self.data[YY]) * inv_det;
    m[YX] = (self.data[YZ] * self.data[ZX] - self.data[YX] * self.data[ZZ]) * inv_det;
    m[YY] = (self.data[XX] * self.data[ZZ] - self.data[XZ] * self.data[ZX]) * inv_det;
    m[YZ] = (self.data[XZ] * self.data[YX] - self.data[XX] * self.data[YZ]) * inv_det;
    m[ZX] = (self.data[YX] * self.data[ZY] - self.data[YY] * self.data[ZX]) * inv_det;
    m[ZY] = (self.data[XY] * self.data[ZX] - self.data[XX] * self.data[ZY]) * inv_det;
    m[ZZ] = (self.data[XX] * self.data[YY] - self.data[XY] * self.data[YX]) * inv_det;
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
    ret_mat = Mat3()
    for row in range(0,2):
      for col in range(0,2):
        ret_mat[row, col] = vec1[row] * vec2[col]
    return ret_mat

  @staticmethod
  def mul(self, mat1, mat2):
    ret_mat = Mat3()
    for row in range(0,2):
      for col in range(0,2):
        val = 0.0
        for i in range(0,2):
          val += mat1[row, i] * mat2[i, col]
        ret_mat[row, col] = val
    return ret_mat

  @staticmethod
  def identity():
    identity = ([
      1.0, 0.0, 0.0,
      0.0, 1.0, 0.0,
      0.0, 0.0, 1.0])
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
    for i in range(0,8):
      if self.data[i] != ret_mat[i]:
        return False
    return True

  def __ne__(self, ret_mat):
    for i in range[0,8]:
      if self.data[i] == ret_mat[i]:
        return False
    return True

  def __neg__(self):
    ret_mat = self.data
    for i in range(0,8):
      ret_mat[i] = -ret_mat[i]
    return ret_mat

  def __add__(self, mat):
    ret_mat = Mat3()
    for i in range(0,8):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    ret_mat = Mat3()
    for i in range(0,8):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, mat):
    ret_mat = Mat3()
    for row in range(0,2):
      for col in range(0,2):
        val = 0.0
        for i in range(0,2):
          val += self.data[row*3+i] * mat(i, col);
        ret_mat[row, col] = val
    return ret_mat

  def __str__(self):
    return "{} {} {}\n{} {} {}\n{} {} {}".format(
      self.data[XX], self.data[XY], self.data[XZ],
      self.data[YX], self.data[YY], self.data[YZ],
      self.data[ZX], self.data[ZY], self.data[ZZ])

