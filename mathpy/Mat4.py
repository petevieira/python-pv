#!/usr/bin/env python

from Vec2 import *
from Vec3 import *
from Vec4 import *
from Mat3 import *

# Labeled indices of the matrix
XX = 0;  XY = 1;  XZ = 2;  XW = 3
YX = 4;  YY = 5;  YZ = 6;  YW = 7
ZX = 8;  ZY = 9;  ZZ = 10; ZW = 11
WX = 12; WY = 13; WZ = 14; WW = 15

class Mat4:
  """ 4x4 Matrix class.
  """

  def __init__(self, *args):
    """ Constructs a 4x4 matrix from a Mat4 or 16 scalars

    Args:
      *args: list of arguments
        None: Initializes matrix with zeros
        4x4 matrix (Mat4): 4x4 matrix of class Mat4
        16 scalars: 16 scalars of type float in row major order

    """
    self.data = ([
      0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0,])
    if len(args) == 1:
      if isinstance(args[0], Mat4):
        self.__initialize_from_mat4(*args)
      elif isinstance(args[0], tuple) or isinstance(args[0], list):
        self.__initialize_from_tuple(*args)
      else:
        print "Error constructing matrix. Unhandled arg of length 1"
    elif len(args) == 16:
      if isinstance(args[0], float) or isinstance(args[0], int):
        self.__initialize_from_row_major_ret_mat(*args)
      else:
        print "Error constructing matrix. Unhandled arg of length 16"
    else:
      print "Error constructing matrix. Unhandled number of args"

  def __initialize_from_row_major_ret_mat(self, 
    m00, m01, m02, m03,
    m10, m11, m12, m13,
    m20, m21, m22, m23,
    m30, m31, m32, m33):
    """ Initializes the matrix data from 4 scalars in row major order

    Args:
      m00: xx index of the matrix
      m01: xy index of the matrix
      m02: xz index of the matrix
      m03: xw index of the matrix
      m10: yx index of the matrix
      m11: yy index of the matrix
      m12: yz index of the matrix
      m13: yw index of the matrix
      m20: zx index of the matrix
      m21: zy index of the matrix
      m22: zz index of the matrix
      m23: zw index of the matrix
      m30: wx index of the matrix
      m31: wy index of the matrix
      m32: wz index of the matrix
      m33: ww index of the matrix

    """
    self.data = (
      m00, m01, m02, m03,
      m10, m11, m12, m13,
      m20, m21, m22, m23,
      m30, m31, m32, m33)

  def __initialize_from_tuple(self, mat):
    self.data = mat

  def __initialize_from_mat4(self, mat):
    """ Initializes the matrix data from a Mat4 matrix

    Args:
      mat (Mat4): Mat4 matrix

    """
    for i in range(0,15):
      self.data[i] = mat[i]

  @classmethod
  def from_rows(self, v1, v2, v3, v4):
    """ Creates a 4x4 matrix from row vectors

    Args:
      v1: 1x4 row1 vector
      v2: 1x4 row2 vector
      v3: 1x4 row3 vector
      v4: 1x4 row4 vector

    Returns:
      a Mat4 matrix

    """
    return Mat4(
      v1[0], v1[1], v1[2], v1[3],
      v2[0], v2[1], v2[2], v2[3],
      v3[0], v3[1], v3[2], v3[3],
      v4[0], v4[1], v4[2], v4[3])

  @classmethod
  def from_cols(self, v1, v2, v3, v4):
    """ Creates 4x4 matrix from column vectors

    Args:
      v1: 4x1 column1 vector
      v2: 4x1 column2 vector
      v3: 4x1 column3 vector
      v4: 4x1 column4 vector

    Returns:
      a Mat4 matrix

    """
    return Mat4(
      v1[0], v2[0], v3[0], v4[0],
      v1[1], v2[1], v3[1], v4[1],
      v1[2], v2[2], v3[2], v4[2],
      v1[3], v2[3], v3[3], v4[3])

  def transpose(self):
    """ Returns the transpose matrix of itself

    Returns:
      the transpose of itself

    """
    transpose_data = self.data

    transpose_indices = ([
      XX, YX, ZX, WX,
      XY, YY, ZY, WY,
      XZ, YZ, ZZ, WZ,
      XW, YW, ZW, WW])

    for i in range(0,15):
      transpose_data[i] = self.data[transpose_indices[i]]

    return Mat4(transpose_data)

  def num_rows(self):
    """ Returns the number of rows in the matrix

    """
    return 3

  def num_cols(self):
    """ Returns the number of columns in the matrix

    """
    return 3

  def size(self):
    """ Returns the size of the matrix

    """
    return ([3, 3])

  def row(self, i):
    """ Returns the row i of the matrix

    Args:
      i: number of the desired row

    Returns:
      the desired row 1x4 of the matrix

    """
    return Vec4(self.data[4*i+0], self.data[4*i+1], self.data[4*i+2], self.data[4*i+3])

  def col(self, i):
    """ Returns the column i of the matrix

    Args:
      i: number of the desired column

    Returns:
      the desired column 4x1 of the matrix

    """
    return Vec4(self.data[i+0], self.data[i+4], self.data[i+8], self.data[i+12])

  def rowcol_to_index(self, row, col):
    """ Returns the index of the row vector version of the matrix
        associated with the row, col of the matrix

    Args:
      row: row number
      col: column number

    Returns:
      the index associated with the specified row and colunn

    """
    return row * 4 + col

  def block(self, row, col, rows, cols):
    x = self.data[self.rowcol_to_index(row,col)]
    # row vectors
    if rows == 1:
      if cols == 1:
        return self.data[self.rowcol_to_index(row,col)]
      elif cols == 2:
        assert(col <= 2)
        return Vec2(x, self.data[self.rowcol_to_index(row,col+1)])
      elif cols == 3:
        assert(col <= 1)
        return Vec3(
          x,
          self.data[self.rowcol_to_index(row,col+1)],
          self.data[self.rowcol_to_index(row,col+2)])
      elif cols == 4:
        return self.row(row)
      else:
        assert 0
    # column vectors
    elif cols == 1:
      if rows == 1:
        return self.data[self.rowcol_to_index(row,col)]
      elif rows == 2:
        assert(row <= 2)
        return Vec2(
          x,
          self.data[self.rowcol_to_index(row+1,col)])
      elif rows == 3:
        assert(row <= 1)
        return Vec3(
          x,
          self.data[self.rowcol_to_index(row+1,col)],
          self.data[self.rowcol_to_index(row+2,col)])
      elif rows == 4:
        return self.col(col)
      else:
        assert 0
    # square matrices
    elif rows == 2:
      assert cols == 2, "Error! Requested non-square matrix block of size {} by {}".format(rows, cols)
      return Mat2(
        x,
        self.data[self.rowcol_to_index(row,col+1)],
        self.data[self.rowcol_to_index(row+1,col)],
        self.data[self.rowcol_to_index(row+1,col+1)])
    elif rows == 3:
      assert cols == 3, "Error! Requested non-square matrix block of size {} by {}".format(rows, cols)
      return Mat3(
        x,
        self.data[self.rowcol_to_index(row,col+1)],
        self.data[self.rowcol_to_index(row,col+2)],
        self.data[self.rowcol_to_index(row+1,col)],
        self.data[self.rowcol_to_index(row+1,col+1)],
        self.data[self.rowcol_to_index(row+1,col+2)],
        self.data[self.rowcol_to_index(row+2,col)],
        self.data[self.rowcol_to_index(row+2,col+1)],
        self.data[self.rowcol_to_index(row+2,col+2)])
    else:
      assert 0

  def set_row(self, i, vec):
    """ Sets row i of the matrix with vector vec

    Args:
      i: row number
      vec: new vector for row i

    """
    self.data[4*i+0] = vec[0]
    self.data[4*i+1] = vec[1]
    self.data[4*i+2] = vec[2]
    self.data[4*i+3] = vec[3]

  def set_col(self, i, vec):
    """ Sets column i of the matrix with vector vec

    Args:
      i: colunn number
      vec: new vector for column i

    """
    self.data[i+0] = vec[0]
    self.data[i+4] = vec[1]
    self.data[i+8] = vec[2]
    self.data[i+12] = vec[3]

  def determinant(self):
    """ Returns the determinant of the matrix

    Returns:
      the determinant of the matrix

    """
    return (
      self.data[XX] * (self.data[YY] * self.data[ZZ] * self.data[WW] +
        self.data[YZ] * self.data[ZW] * self.data[WY] +
        self.data[YW] * self.data[ZY] * self.data[WX]) +

      self.data[XY] * (self.data[YX] * self.data[ZW] * self.data[WZ] +
        self.data[YZ] * self.data[ZX] * self.data[WW] +
        self.data[YW] * self.data[ZZ] * self.data[WX]) +

      self.data[XZ] * (self.data[YX] * self.data[ZY] * self.data[WW] +
        self.data[YY] * self.data[ZW] * self.data[WX] +
        self.data[YW] * self.data[ZX] * self.data[WY]) +

      self.data[XW] * (self.data[YX] * self.data[ZZ] * self.data[WY] +
        self.data[YY] * self.data[ZX] * self.data[WZ] +
        self.data[YZ] * self.data[ZY] * self.data[WX]) -

      self.data[XX] * (self.data[YY] * self.data[ZW] * self.data[WZ] -
        self.data[YZ] * self.data[ZY] * self.data[WW] -
        self.data[YW] * self.data[ZZ] * self.data[WY]) -

      self.data[XY] * (self.data[YX] * self.data[ZZ] * self.data[WW] -
        self.data[YZ] * self.data[ZW] * self.data[WX] -
        self.data[YW] * self.data[ZX] * self.data[WZ]) -

      self.data[XZ] * (self.data[YX] * self.data[ZW] * self.data[WY] -
        self.data[YY] * self.data[ZX] * self.data[WW] -
        self.data[YW] * self.data[ZY] * self.data[WX]) -

      self.data[XW] * (self.data[YX] * self.data[ZY] * self.data[WZ] -
        self.data[YY] * self.data[ZZ] * self.data[WX] -
        self.data[YZ] * self.data[ZX] * self.data[WY]))

  def det(self):
    """ Returns the determinant of the matrix

    Returns:
      the determinant of the matrix

    """
    return self.determinant()

  # def inverse(self):
  #   det = self.determinant()
  #   if det != 0:
  #     inv_det = 1.0/det
  #   else:
  #     return None

  #   m = Mat4()
  #   m[XX] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[XY] = (self.data[XY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[XZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[XW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[XZ] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[XW] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det

  #   m[YX] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[YY] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[YZ] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[YW] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det

  #   m[ZX] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[ZY] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[ZZ] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[ZW] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det

  #   m[WX] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[WY] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[WZ] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det
  #   m[WW] = (self.data[YY] * (self.data[ZZ] * self.data[WW] - self.data[ZW] * self.data[WZ]);
  #     + self.data[YZ] * (self.data[ZW] * self.data[WY] - self.data[ZY] * self.data[WW])
  #     + self.data[YW] * (self.data[ZY] * self.data[WZ] - self.data[ZZ] * self.data[WY])
  #     )* inv_det

  #   return m;

  # def inv(self):
    # return self.inverse()


  # @staticmethod
  # def cross(self, vec):
  #   mat = Mat4()
  #   mat[0,0] =    0 ; mat[0,1] = -v[2]; mat[0,2] =  v[1]
  #   mat[1,0] =  v[2]; mat[1,1] =    0 ; mat[1,2] = -v[0]
  #   mat[2,0] = -v[1]; mat[2,1] =  v[0]; mat[2,2] =    0
  #   return m

  @staticmethod
  def outer(self, vec1, vec2):
    """ Returns the outer product (a Mat4) of two vectors
        mat = vec1 * vec2

    Args:
      vec1: first vector in the outer product
      vec2: second vector in the outer product

    Returns:
      the matrix returned by the outer product of vec1 and vec2

    """
    ret_mat = Mat4()
    for row in range(0,3):
      for col in range(0,3):
        ret_mat[row, col] = vec1[row] * vec2[col]
    return ret_mat

  @staticmethod
  def mul(self, mat1, mat2):
    """ Returns the product of two matrices

    Args:
      mat1: first matrix
      mat2: second matrix

    Returns:
      the matrix product of mat1 and mat2

    """
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
    """ Returns the 4x4 identity matrix

    Returns:
      the Mat4 4x4 identity matrix

    """
    identity = ([
      1.0, 0.0, 0.0, 0.0,
      0.0, 1.0, 0.0, 0.0,
      0.0, 0.0, 1.0, 0.0,
      0.0, 0.0, 0.0, 1.0])
    return Mat4(identity)

  @staticmethod
  def zeros():
    """ Returns a 4x4 matrix full of zeros

    Returns:
      a Mat4 4x4 matrix of zeros

    """
    return Mat4(
      0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0,
      0.0, 0.0, 0.0, 0.0)

  @staticmethod
  def ones():
    """ Returns a 4x4 matrix full of ones

    Returns:
      a Mat4 4x4 matrix of ones

    """
    return Mat4(
      1.0, 1.0, 1.0, 1.0,
      1.0, 1.0, 1.0, 1.0,
      1.0, 1.0, 1.0, 1.0,
      1.0, 1.0, 1.0, 1.0)

  def __getitem__(self, *args):
    """ Returns the value in the matrix associated with either a
        single index into the row vector version of the matrix or
        the row, col index of the matrix

    Args:
      *args: list of arguments
        index: single scalar specifying the index in the
               row vector version of the matrix
        row, col: two scalars representing the row and col of the index

    Returns:
      value in the matrix associated with the index given

    """
    if len(args) == 1:
      return self.data[args[0]]
    elif len(args) == 2:
      return self.data[self.rowcol_to_index(args[0], args[1])]
    else:
      print "Error. Invalid number of index args: {}.".format(len(args))
      print "Valid numbers are 1 and 2"

  def __setitem__(self, value, row, col):
    """ Sets the value at row, col to value

    Args:
      value: scalar to set the value to
      row: row index of the value to set
      col: column index of the value to set

    """
    self.data[self.rowcol_to_index(row, col)] = value

  def __call__(self, *args):
    """ Returns the value in the matrix at row, col

    Args:
      row: row index of the desired value
      col: col index of the desired value

    Returns:
      the value in the matrix at row, col

    """
    if len(args) == 1:
      return self.data[args[0]]
    elif len(args) == 2:
      return self.data[rowcol_to_index(args[0], args[1])]
    else:
      print "Error. Invalid number of index args: {}.".format(len(args))
      print "Valid numbers are 1 and 2"

  def __eq__(self, ret_mat):
    """ Tests equality with another matrix by value

    Args:
      mat: 4x4 Mat4 matrix to test equality with

    Returns:
      True is equal, False if not

    """
    for i in range(0,15):
      if self.data[i] != ret_mat[i]:
        return False
    return True

  def __ne__(self, ret_mat):
    """ Tests inequality with another matrix by value

    Args:
      mat: 4x4 Mat4 matrix to test inequality with

    Returns:
      True is not equal, False if equal

    """
    for i in range[0,15]:
      if self.data[i] == ret_mat[i]:
        return False
    return True

  def __neg__(self):
    """ Returns the negation of all the values in the matrix

    """
    ret_mat = self.data
    for i in range(0,15):
      ret_mat[i] = -ret_mat[i]
    return ret_mat

  def __add__(self, mat):
    """ Returns the result of adding mat to the matrix

    Args:
      mat: 4x4 Mat4 matrix to add to the matrix

    Returns:
      the result of adding the two matrices

    """
    ret_mat = Mat4()
    for i in range(0,15):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    """ Returns the result of subtracting mat to the matrix

    Args:
      mat: 4x4 Mat4 matrix to subtract to the matrix

    Returns:
      the result of subtracting the two matrices

    """
    ret_mat = Mat4()
    for i in range(0,15):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, *args):
    """ Returns the result of multiplying the matrix by mat

    Args:
      mat: 4x4 Mat4 matrix to multiply the matrix by
      scalar: scalar to multiply each element by

    Returns:
      the result of multiplying the two matrices

    """
    ret_mat = Mat4()
    for row in range(0,3):
      for col in range(0,3):
        if isinstance(args[0], float):
          ret_mat[row, col] = self.data[row*4+i] * args[0]
        elif isinstance(args[0], Mat4):
          mat = args[0]
          val = 0.0
          for i in range(0,3):
            val += self.data[row*4+i] * mat(i, col);
            ret_mat[row, col] = val
    return ret_mat

  def __str__(self):
    """ Returns the string version of the matrix

    """
    return "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}".format(
      self.data[XX], self.data[XY], self.data[XZ], self.data[XW],
      self.data[YX], self.data[YY], self.data[YZ], self.data[YW],
      self.data[ZX], self.data[ZY], self.data[ZZ], self.data[ZW],
      self.data[WX], self.data[WY], self.data[WZ], self.data[WW])

