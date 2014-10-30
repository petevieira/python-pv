#!/usr/bin/env python

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
      self.__initialize_from_row_major_matrix(*args)

  def __initialize_from_row_major_matrix(self, 
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

    for i in range(0,9):
      transpose_data[i] = data[transpose_indices[i]]

    return transpose_data

  def row(self, i):
    return Vec3(self.data[3*i+0], self.data[3*i+1], self.data[3*i+2])

  def col(self, i):
    return Vec3(self.data[i+0], self.data[i+3], self.data[i+6])

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
      self.data[XY] * (self.data[YX] * self.data[ZZ] - self.data[YZ] * self.data[ZX]) +
      self.data[XZ] * (self.data[YX] * self.data[ZY] - self.data[YY] * self.data[ZX]))

  def det(self):
    return self.determinant()

  def inverse(self):
    det = self.determinant()
    m = ()
    m[XX] = (self.data[YY] * self.data[ZZ] - self.data[YZ] * self.data[ZY]) * det;
    m[XY] = (self.data[XZ] * self.data[ZY] - self.data[XY] * self.data[ZZ]) * det;
    m[XZ] = (self.data[XY] * self.data[YZ] - self.data[XZ] * self.data[YY]) * det;
    m[YX] = (self.data[YZ] * self.data[ZX] - self.data[YX] * self.data[ZZ]) * det;
    m[YY] = (self.data[XX] * self.data[ZZ] - self.data[XZ] * self.data[ZX]) * det;
    m[YZ] = (self.data[XZ] * self.data[YX] - self.data[XX] * self.data[YZ]) * det;
    m[ZX] = (self.data[YX] * self.data[ZY] - self.data[YY] * self.data[ZX]) * det;
    m[ZY] = (self.data[XY] * self.data[ZX] - self.data[XX] * self.data[ZY]) * det;
    m[ZZ] = (self.data[XX] * self.data[YY] - self.data[XY] * data[YX]) * det;
    return m;

  def inv(self):
    return self.inverse()

  def __eq__(self, m):
    for i in range(0,8):
      if self.data[i] != m[i]:
        return False
    return True

  def __ne__(self, m):
    for i in range[0,8]:
      if self.data[i] == m[i]:
        return False
    return True

  def __neg__(self):
    m = self.data
    for i in range(0,8):
      m = -m
    return m

  def __getitem__(self, index):
    return self.data[index]

  def __call__(self, row, col):
    if row == 0:
      return self.data[col]
    elif row == 1:
      return self.data[col + 3]
    elif row == 2:
      return self.data[col + 6]

  def __str__(self):
    return "{} {} {}\n{} {} {}\n{} {} {}".format(
      self.data[XX], self.data[XY], self.data[XZ],
      self.data[YX], self.data[YY], self.data[YZ],
      self.data[ZX], self.data[ZY], self.data[ZZ])

  @staticmethod
  def identity():
    identity = ([
      1.0, 0.0, 0.0,
      0.0, 1.0, 0.0,
      0.0, 0.0, 1.0])
    return identity