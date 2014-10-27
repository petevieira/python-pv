#!/usr/bin/env python

from Vec3 import *

class Mat3:
  self.data = ([
    0.0, 0.0, 0.0,
    0.0, 0.0, 0.0,
    0.0, 0.0, 0.0])

  XX = 0
  XY = 1
  XZ = 2
  YX = 3
  YY = 4
  YZ = 5
  ZX = 6
  ZY = 7
  ZZ = 8

  def __init__(self):
    if len(args) == 9:
      initialize_from_row_major_matrix(*args)

  
  def initialize_from_row_major_matrix(self,
    m00, m01, m02,
    m10, m11, m12,
    m20, m21, m22):

  def transpose(self):
    transpose_data = self.data

    transpose_indices = ([
      XX, YX, ZX,
      XY, YY, ZY,
      XZ, YZ, ZZ])

    for i in range(0,9):
      transpose_data[i] = data[transpose_indices[i]]

    return transpose_data

  def __eq__(m):
    self.data = m

  def __getitem__(self, index):
    return self.data[index]

  @staticmethod
  def identity():
    identity = ([
      1.0, 0.0, 0.0,
      0.0, 1.0, 0.0,
      0.0, 0.0, 1.0]
    return Mat3(identity)