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
  """ Homogeneous transform class """

  def __init__(self, *args):
    """ Constructs a homogeneous transform from a 4x4 matrix,
        or 16 scalars

    """
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

  def __initialize_from_mat3(self, mat):
    for i in range(0,15):
      self.data[i] = mat[i]

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