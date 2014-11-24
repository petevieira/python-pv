#!/usr/bin/env python

from Vec2 import *
from Vec3 import *

# Labeled indices of the matrix
XX = 0; XY = 1; XZ = 2
YX = 3; YY = 4; YZ = 5
ZX = 6; ZY = 7; ZZ = 8

class Mat3:
  """ 3x3 Matrix class
  """

  def __init__(self, *args):
    """ Constructs a 3x3 matrix from a Mat3 or 9 scalars

    Args:
      *args: list of arguments
        None: Initializes matrix with zeros
        3x3 matrix (Mat3): 3x3 matrix of class Mat3
        9 scalars: 9 scalars of type float in row major order

    """
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
    """ Initializes the matrix data from 4 scalars in row major order

    Args:
      m00: xx index of the matrix
      m01: xy index of the matrix
      m02: xz index of the matrix
      m10: yx index of the matrix
      m11: yy index of the matrix
      m12: yz index of the matrix
      m20: zx index of the matrix
      m21: zy index of the matrix
      m22: zz index of the matrix

    """
    self.data = (
      m00, m01, m02,
      m10, m11, m12,
      m20, m21, m22)

  def __initialize_from_mat3(self, mat):
    """ Initializes the matrix data from a Mat3 matrix

    Args:
      mat (Mat3): Mat3 matrix

    """
    for i in range(0,8):
      self.data[i] = mat[i]

  @classmethod
  def from_rows(self, v1, v2, v3):
    """ Creates a 3x3 matrix from row vectors

    Args:
      v1: 1x3 row1 vector
      v2: 1x3 row2 vector
      v3: 1x3 row3 vector

    Returns:
      a Mat3 matrix

    """
    self.data[XX] = v1[0]; self.data[XY] = v1[1]; self.data[XZ] = v1[2]
    self.data[YX] = v2[0]; self.data[YY] = v2[1]; self.data[YZ] = v2[2]
    self.data[ZX] = v3[0]; self.data[ZY] = v3[1]; self.data[ZZ] = v3[2]

  @classmethod
  def from_cols(self, v1, v2, v3):
    """ Creates a 3x3 matrix from column vectors

    Args:
      v1: 3x1 column1 vector
      v2: 3x1 column2 vector
      v3: 3x1 column3 vector

    Returns:
      a Mat3 matrix

    """
    return Mat3(
      v1[0], v2[0], v3[0],
      v1[1], v2[1], v3[1],
      v1[2], v2[2], v3[2])

  def transpose(self):
    """ Returns the transpose matrix of itself

    Returns:
      the transpose of itself

    """
    transpose_data = self.data

    transpose_indices = ([
      XX, YX, ZX,
      XY, YY, ZY,
      XZ, YZ, ZZ])

    for i in range(0,8):
      transpose_data[i] = data[transpose_indices[i]]

    return Mat3(transpose_data)

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
      the desired row 1x3 of the matrix

    """
    return Vec3(self.data[3*i+0], self.data[3*i+1], self.data[3*i+2])

  def col(self, i):
    """ Returns the column i of the matrix

    Args:
      i: number of the desired column

    Returns:
      the desired column 3x1 of the matrix

    """
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
    """ Sets row i of the matrix with vector vec

    Args:
      i: row number
      vec: new vector for row i

    """
    self.data[3*i+0] = vec[0]
    self.data[3*i+1] = vec[1]
    self.data[3*i+2] = vec[2]

  def set_col(self, i, vec):
    """ Sets column i of the matrix with vector vec

    Args:
      i: colunn number
      vec: new vector for column i

    """
    self.data[i+0] = vec[0]
    self.data[i+3] = vec[1]
    self.data[i+6] = vec[2]    

  def determinant(self):
    """ Returns the determinant of the matrix

    Returns:
      the determinant of the matrix

    """
    return (
      self.data[XX] * (self.data[YY] * self.data[ZZ] - self.data[YZ] * self.data[ZY]) -
      self.data[XY] * (self.data[YZ] * self.data[ZX] - self.data[YX] * self.data[ZZ]) +
      self.data[XZ] * (self.data[YX] * self.data[ZY] - self.data[YY] * self.data[ZX]))

  def det(self):
    """ Returns the determinant of the matrix

    Returns:
      the determinant of the matrix

    """
    return self.determinant()

  def inverse(self):
    """ Returns the inverse of the matrix

    Returns:
      the inverse of the matrix

    """
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
    """ Returns the inverse of the matrix

    Returns:
      the inverse of the matrix

    """
    return self.inverse()

  def rowcol_to_index(self, row, col):
    """ Returns the index of the row vector version of the matrix
        associated with the row, col of the matrix

    Args:
      row: row number
      col: column number

    Returns:
      the index associated with the specified row and colunn

    """
    return row * 3 + col

  @staticmethod
  def cross(self, vec):
    """ Returns the skew-symmetric cross product of the given vector

    Args:
      vec: Vec3 vector to compute the cross product of

    Returns:
      the skew-symmetric cross product matrix of vec

    """
    mat = Mat3()
    mat[0,0] =    0 ; mat[0,1] = -v[2]; mat[0,2] =  v[1]
    mat[1,0] =  v[2]; mat[1,1] =    0 ; mat[1,2] = -v[0]
    mat[2,0] = -v[1]; mat[2,1] =  v[0]; mat[2,2] =    0
    return m

  @staticmethod
  def outer(self, vec1, vec2):
    """ Returns the outer product (a Mat3) of two vectors
        mat = vec1 * vec2

    Args:
      vec1: first vector in the outer product
      vec2: second vector in the outer product

    Returns:
      the matrix returned by the outer product of vec1 and vec2

    """
    ret_mat = Mat3()
    for row in range(0,2):
      for col in range(0,2):
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
    """ Returns the 3x3 identity matrix

    Returns:
      the Mat3 3x3 identity matrix

    """
    identity = ([
      1.0, 0.0, 0.0,
      0.0, 1.0, 0.0,
      0.0, 0.0, 1.0])
    return identity

  @staticmethod
  def zeros():
    """ Returns a 3x3 matrix full of zeros

    Returns:
      a Mat3 3x3 matrix of zeros

    """
    return Mat3(
      0.0, 0.0, 0.0,
      0.0, 0.0, 0.0,
      0.0, 0.0, 0.0)

  @staticmethod
  def ones():
    """ Returns a 3x3 matrix full of ones

    Returns:
      a Mat3 3x3 matrix of ones

    """
    return Mat3(
      1.0, 1.0, 1.0,
      1.0, 1.0, 1.0,
      1.0, 1.0, 1.0)

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
      return self.data[rowcol_to_index(args[0], args[1])]
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
    self.data[rowcol_to_index(row, col)] = value

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
      mat: 3x3 Mat3 matrix to test equality with

    Returns:
      True is equal, False if not

    """
    for i in range(0,8):
      if self.data[i] != ret_mat[i]:
        return False
    return True

  def __ne__(self, ret_mat):
    """ Tests inequality with another matrix by value

    Args:
      mat: 3x3 Mat3 matrix to test inequality with

    Returns:
      True is not equal, False if equal

    """
    for i in range[0,8]:
      if self.data[i] == ret_mat[i]:
        return False
    return True

  def __neg__(self):
    """ Returns the negation of all the values in the matrix

    """
    ret_mat = self.data
    for i in range(0,8):
      ret_mat[i] = -ret_mat[i]
    return ret_mat

  def __add__(self, mat):
    """ Returns the result of adding mat to the matrix

    Args:
      mat: 3x3 Mat3 matrix to add to the matrix

    Returns:
      the result of adding the two matrices

    """
    ret_mat = Mat3()
    for i in range(0,8):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    """ Returns the result of subtracting mat to the matrix

    Args:
      mat: 3x3 Mat3 matrix to subtract to the matrix

    Returns:
      the result of subtracting the two matrices

    """
    ret_mat = Mat3()
    for i in range(0,8):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, *args):
    """ Returns the result of multiplying the matrix by mat

    Args:
      mat: 3x3 Mat3 matrix to multiply the matrix by
      scalar: scalar to multiply each element by

    Returns:
      the result of multiplying the two matrices

    """
    ret_mat = Mat3()
    for row in range(0,2):
      for col in range(0,2):
        if isinstance(args[0], float):
          ret_mat[row, col] = self.data[row*3+i] * args[0]
        elif isinstance(args[0], Mat3):
          mat = args[0]
          val = 0.0
          for i in range(0,2):
            val += self.data[row*3+i] * mat(i, col);
            ret_mat[row, col] = val
    return ret_mat

  def __str__(self):
    """ Returns the string version of the matrix

    """
    return "{} {} {}\n{} {} {}\n{} {} {}".format(
      self.data[XX], self.data[XY], self.data[XZ],
      self.data[YX], self.data[YY], self.data[YZ],
      self.data[ZX], self.data[ZY], self.data[ZZ])

