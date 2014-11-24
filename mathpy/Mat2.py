#!/usr/bin/env python

from Vec2 import *

# Labeled indices of the matrix
XX = 0; XY = 1
YX = 2; YY = 3

class Mat2:
  """ 2x2 Matrix class.
  """

  def __init__(self, *args):
    """ Constructs a 2x2 matrix from a Mat2 or 4 scalars

    Args:
      *args: list of arguments
        None: Initializes matrix with zeros
        2x2 matrix (Mat2): 2x2 matrix of class Mat2
        4 scalars: 4 scalars of type float in row major order

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
    """ Initializes the matrix data from 4 scalars in row major order

    Args:
      m00: xx index of the matrix
      m01: xy index of the matrix
      m10: yx index of the matrix
      m11: yy index of the matrix

    """
    self.data = (
      m00, m01,
      m10, m11)

  def __initialize_from_mat2(self, mat):
    """ Initializes the matrix data from a Mat2 matrix

    Args:
      mat (Mat2): Mat2 matrix

    """
    for i in range(0,3):
      self.data[i] = mat[i]

  @classmethod
  def from_rows(self, v1, v2):
    """ Creates a 2x2 matrix from row vectors

    Args:
      v1: 1x2 row1 vector
      v2: 1x2 row2 vector

    Returns:
      a Mat2 matrix

    """
    return Mat2(
      v1[0], v1[1]
      v2[0], v2[1])

  @classmethod
  def from_cols(self, v1, v2):
    """ Creates a 2x2 matrix from column vectors

    Args:
      v1: 2x1 column1 vector
      v2: 2x1 column2 vector

    Returns:
      a Mat2 matrix

    """
    return Mat2(
      v1[0], v2[0],
      v1[1], v2[1])

  @classmethod
  def from_angle(self, theta):
    """ Creates a 2x2 matrix from a rotation angle

    Args:
      theta: Angle to rotate by

    Returns:
      A Mat2 matrix representing a rotation about
      the z-axis of angle theta

    """
    cos_theta = cos(theta)
    sin_theta = sin(theta)
    return Mat2(
      cos_theta, -sin_theta,
      sin_theta,  cos_theta)

  def transpose(self):
    """ Returns the transpose matrix of itself

    Returns:
      the transpose of itself

    """
    transpose_data = self.data

    transpose_indices = ([
      XX, YX,
      XY, YY])

    for i in range(0,3):
      transpose_data[i] = data[transpose_indices[i]]

    return Mat2(transpose_data)

  def num_rows(self):
    """ Returns the number of rows in the matrix

    """
    return 2

  def num_cols(self):
    """ Returns the number of columns in the matrix

    """
    return 2

  def size(self):
    """ Returns the size of the matrix

    """
    return ([2, 2])

  def row(self, i):
    """ Returns the row i of the matrix

    Args:
      i: number of the desired row

    Returns:
      the desired row 1x2 of the matrix

    """
    return Vec2(self.data[2*i+0], self.data[2*i+1])

  def col(self, i):
    """ Returns the column i of the matrix

    Args:
      i: number of the desired column

    Returns:
      the desired column 2x1 of the matrix

    """
    return Vec2(self.data[i+0], self.data[i+2])

  def set_row(self, i, vec):
    """ Sets row i of the matrix with vector vec

    Args:
      i: row number
      vec: new vector for row i

    """
    self.data[2*i+0] = vec[0]
    self.data[2*i+1] = vec[1]

  def set_col(self, i, vec):
    """ Sets column i of the matrix with vector vec

    Args:
      i: colunn number
      vec: new vector for column i

    """
    self.data[i+0] = vec[0]
    self.data[i+2] = vec[1]

  def determinant(self):
    """ Returns the determinant of the matrix

    Returns:
      the determinant of the matrix

    """
    return (self.data[XX] * self.data[YY]
      - self.data[XY] * self.data[YX])

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
    m = Mat2()
    m[XX] = self.data[YY] * inv_det;  m[XY] = -self.data[XY] * inv_det
    m[XZ] = -self.data[YX] * inv_det; m[YX] = self.data[XX] * inv_det
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
    return row * 2 + col

  @staticmethod
  def outer(self, vec1, vec2):
    """ Returns the outer product (a Mat2) of two vectors
        mat = vec1 * vec2

    Args:
      vec1: first vector in the outer product
      vec2: second vector in the outer product

    Returns:
      the matrix returned by the outer product of vec1 and vec2

    """
    ret_mat = Mat2()
    for row in range(0,1):
      for col in range(0,1):
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
    """ Returns the 2x2 identity matrix

    Returns:
      the Mat2 2x2 identity matrix

    """
    identity = ([
      1.0, 0.0,
      0.0, 1.0])
    return identity

  @staticmethod
  def zeros():
    """ Returns a 2x2 matrix full of zeros

    Returns:
      a Mat2 2x2 matrix of zeros

    """
    return Mat2(
      0.0, 0.0,
      0.0, 0.0)

  @staticmethod
  def ones():
    """ Returns a 2x2 matrix full of ones

    Returns:
      a Mat2 2x2 matrix of ones

    """
    return Mat2(
      1.0, 1.0,
      1.0, 1.0)

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

  def __call__(self, row, col):
    """ Returns the value in the matrix at row, col

    Args:
      row: row index of the desired value
      col: col index of the desired value

    Returns:
      the value in the matrix at row, col

    """
    return self.data[rowcol_to_index(row, col)]

  def __eq__(self, mat):
    """ Tests equality with another matrix by value

    Args:
      mat: 2x2 Mat2 matrix to test equality with

    Returns:
      True is equal, False if not

    """
    for i in range(0,3):
      if self.data[i] != mat[i]:
        return False
    return True

  def __ne__(self, mat):
    """ Tests inequality with another matrix by value

    Args:
      mat: 2x2 Mat2 matrix to test inequality with

    Returns:
      True is not equal, False if equal

    """
    for i in range[0,3]:
      if self.data[i] == ret_mat[i]:
        return False
    return True

  def __neg__(self):
    """ Returns the negation of all the values in the matrix

    """
    ret_mat = self.data
    for i in range(0,3):
      ret_mat[i] = -ret_mat[i]
    return ret_mat

  def __add__(self, mat):
    """ Returns the result of adding mat to the matrix

    Args:
      mat: 2x2 Mat2 matrix to add to the matrix

    Returns:
      the result of adding the two matrices

    """
    ret_mat = Mat2()
    for i in range(0,3):
      ret_mat[i] = self.data[i] + mat[i]
    return ret_mat

  def __sub__(self, mat):
    """ Returns the result of subtracting mat to the matrix

    Args:
      mat: 2x2 Mat2 matrix to subtract to the matrix

    Returns:
      the result of subtracting the two matrices

    """
    ret_mat = Mat2()
    for i in range(0,3):
      ret_mat[i] = self.data[i] - mat[i]
    return ret_mat

  def __mul__(self, mat):
    """ Returns the result of multiplying the matrix by mat

    Args:
      mat: 2x2 Mat2 matrix to multiply the matrix by

    Returns:
      the result of multiplying the two matrices

    """
    ret_mat = Mat2()
    for row in range(0,1):
      for col in range(0,1):
        val = 0.0
        for i in range(0,1):
          val += self.data[row*2+i] * mat(i, col);
        ret_mat[row, col] = val
    return ret_mat

  def __str__(self):
    """ Returns the string version of the matrix

    """
    return "{} {}\n{} {}\n{} {}".format(
      self.data[XX], self.data[XY],
      self.data[YX], self.data[YY])