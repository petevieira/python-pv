#!/usr/bin/env python

from Vec3 import *
from Mat3 import *
from Mat4 import *

# Labeled indices of the Pose matrix
XX = 0;  XY = 1;  XZ = 2;  XW = 3
YX = 4;  YY = 5;  YZ = 6;  YW = 7
ZX = 8;  ZY = 9;  ZZ = 10; ZW = 11
WX = 12; WY = 13; WZ = 14; WW = 15

class Pose(Mat4):

  def __init__(self, *args):
    self.data = ([
      1.0, 0.0, 0.0, 0.0,
      0.0, 1.0, 0.0, 0.0,
      0.0, 0.0, 1.0, 0.0,
      0.0, 0.0, 0.0, 1.0,])
    if len(args) == 1:
      if isinstance(args[0], Mat4):
        self.__initialize_from_mat4(*args)
    elif len(args) == 16:
      self.__initialize_from_row_major_ret_mat(*args)

  def __initialize_from_row_major_ret_mat(self, 
    m00, m01, m02, m03,
    m10, m11, m12, m13,
    m20, m21, m22, m23,
    m30, m31, m32, m33):
    self.data = (
      m00, m01, m02, m03,
      m10, m11, m12, m13,
      m20, m21, m22, m23,
      m30, m31, m32, m33)

  def __initialize_from_mat3(self, mat):
    for i in range(0,15):
      self.data[i] = mat[i]

  @classmethod
  def from_rows(self, v1, v2, v3, v4):
    return Mat4(
      v1[0], v1[1], v1[2], v1[3],
      v2[0], v2[1], v2[2], v2[3],
      v3[0], v3[1], v3[2], v3[3],
      v4[0], v4[1], v4[2], v4[3])

  @classmethod
  def from_cols(self, v1, v2, v3, v4):
    return Mat4(
      v1[0], v2[0], v3[0], v4[0],
      v1[1], v2[1], v3[1], v4[1],
      v1[2], v2[2], v3[2], v4[2],
      v1[3], v2[3], v3[3], v4[3])

  def rotation(self):
    """ Gets the rotation part of the transformation matrix

    Returns:
      The 3x3 rotation matrix for this pose

    """
    return self.block(0,0,3,3)

  def translation(self):
    """ Gets the translation part of the transformation matrix

    Returns:
      The 3x1 translation vector for this pose

    """
    return Vec3(
      self.data[XW], self.data[YW], self.data[ZW])

  @staticmethod
  def outer(self, vec1, vec2):
    ret_mat = Mat4()
    for row in range(0,3):
      for col in range(0,3):
        ret_mat[row, col] = vec1[row] * vec2[col]
    return ret_mat

  @staticmethod
  def mul(self, mat1, mat2):
    ret_mat = Mat4()
    for row in range(0,3):
      for col in range(0,3):
        val = 0.0
        for i in range(0,3):
          val += mat1[row, i] * mat2[i, col]
        ret_mat[row, col] = val
    return ret_mat

  @staticmethod
  def identity():
    identity = ([
      1.0, 0.0, 0.0, 0.0,
      0.0, 1.0, 0.0, 0.0,
      0.0, 0.0, 1.0, 0.0,
      0.0, 0.0, 0.0, 1.0])
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
    for i in range(0,15):
      if self.data[i] != ret_mat[i]:
        return False
    return True

  def __ne__(self, ret_mat):
    for i in range[0,15]:
      if self.data[i] == ret_mat[i]:
        return False
    return True

  def __neg__(self):
    ret_mat = self.data
    for i in range(0,15):
      ret_mat[i] = -ret_mat[i]
    return ret_mat

  def __add__(self, mat):
    ret_mat = Mat4()
    for i in range(0,15):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    ret_mat = Mat4()
    for i in range(0,15):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, mat):
    ret_mat = Mat4()
    for row in range(0,3):
      for col in range(0,3):
        val = 0.0
        for i in range(0,3):
          val += self.data[row*4+i] * mat(i, col);
        ret_mat[row, col] = val
    return ret_mat

