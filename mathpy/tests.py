  #!/usr/bin/env python

import sys
from Vec2 import *
from Vec3 import *
from Quat import *
from Mat2 import *
from Mat3 import *


def test_vec2():
  print "Testing Vec2..."
  v1 = Vec2()
  print "  v1: {}".format(v1)
  assert(v1.x() == 0 and v1.y() == 0)
  assert(v1[0] == 0 and v1[1] == 0)
  assert(v1(0) == 0 and v1(1) == 0)
  v2 = Vec2(1, 2)
  assert(v2.x() == 1 and v2.y() == 2)
  v3 = Vec2(4.5)
  assert(v3.x() == 4.5 and v3.y() == 4.5)
  v3[0] = 5
  v3[1] = 6.2
  assert(v3.x() == 5 and v3.y() == 6.2)
  v3[0] = 1
  v3[1] = 2.3
  assert(v3.x() == 1 and v3.y() == 2.3)
  assert(len(v3) == 2)
  assert(v1 + v2 == Vec2(1, 2))
  assert(v1 - v2 == Vec2(-1, -2))
  assert(v2 * 2 == Vec2(2, 4))
  assert(v2 / 2.0 == Vec2(0.5, 1.0))

def test_vec3():
  print "Testing Vec3..."
  v1 = Vec3()
  print "  v1: {}".format(v1)
  assert(v1.x() == 0 and v1.y() == 0 and v1.z() == 0)
  assert(v1[0] == 0 and v1[1] == 0 and v1[2] == 0)
  assert(v1(0) == 0 and v1(1) == 0 and v1(2) == 0)
  v2 = Vec3(1, 2, 3)
  assert(v2.x() == 1 and v2.y() == 2 and v2.z() == 3)
  v3 = Vec3(4.5)
  assert(v3.x() == 4.5 and v3.y() == 4.5 and v3.z() == 4.5)
  v3[0] = 5
  v3[1] = 6.2
  v3[2] = -1
  assert(v3.x() == 5 and v3.y() == 6.2 and v3.z() == -1)
  assert(len(v3) == 3)
  assert(v1 + v2 == Vec3(1, 2, 3))
  assert(v1 - v2 == Vec3(-1, -2, -3))
  assert(v3 * 2 == Vec3(10, 12.4, -2))
  assert(v3 / 2.0 == Vec3(2.5, 3.1, -.5))

def test_vec4():
  print "Testing Vec4..."
  v1 = Vec4()
  print "  v1: {}".format(v1)
  assert(v1.x() == 0 and v1.y() == 0 and v1.z() == 0 and v1.w() == 0)
  assert(v1[0] == 0 and v1[1] == 0 and v1[2] == 0 and v1[3] == 0)
  assert(v1(0) == 0 and v1(1) == 0 and v1(2) == 0 and v1(3) == 0)
  v2 = Vec4(1, 2, 3, 4)
  assert(v2.x() == 1 and v2.y() == 2 and v2.z() == 3 and v2.w() == 4)
  v3 = Vec4(4.5)
  assert(v3.x() == 4.5 and v3.y() == 4.5 and v3.z() == 4.5 and v3.w() == 4.5)
  v3[0] = 5
  v3[1] = 6.2
  v3[2] = -1
  v3[3] = .2
  assert(v3.x() == 5 and v3.y() == 6.2 and v3.z() == -1 and v3.w() == .2)
  assert(len(v3) == 4)
  assert(v1 + v2 == Vec4(1, 2, 3, 4))
  assert(v1 - v2 == Vec4(-1, -2, -3, -4))
  assert(v3 * 2 == Vec4(10, 12.4, -2, .4))
  assert(v3 / 2.0 == Vec4(2.5, 3.1, -.5, .1))

def test_mat2():
  print "Testing Mat2..."
  m0 = Mat2()
  assert(m0.xx() == 0 and m0.xy() == 0 and m0.yx() == 0 and m0.yy() == 0)
  print "  m0:\n{}".format(m0)
  m1 = Mat2(1,0, 0,1)
  assert(m1.xx() == 1 and m1.xy() == 0 and m1.yx() == 0 and m1.yy() == 1)
  m3 = Mat2(m0)
  m4 = Mat2.identity()
  assert(m4.xx() == 1 and m4.xy() == 0 and m4.yx() == 0 and m4.yy() == 1)
  m4 = Mat2.zeros()
  assert(m4.xx() == 0 and m4.xy() == 0 and m4.yx() == 0 and m4.yy() == 0)
  m4 = Mat2.ones()
  assert(m4(0,0) == 1 and m4(0,1) == 1 and m4(1,0) == 1 and m4(1,1)== 1)


def test_mat3():
  print "Testing Mat3..."
  m1 = Mat3(1,0,0, 0,1,0, 0,0,1)
  v1 = Vec3(0, 1, 1.3)
  m2 = Mat3.from_cols(v1, v1, v1)
  m3 = Mat3(m2)

def test_quat():
  print "Testing Quat..."
  q1 = Quat()
  print "  q1: {}".format(q1)
  q2 = Quat(.5, .5, .5, .5)
  v3 = (q1.x() + q2.x(), q1.y() + q2.y(), q1.z() + q2.z(), q1.w() + q2.w())
  q3 = Quat(v3)
  q4 = Quat(10)
  v1 = Vec4(1, 2, 4, 5)
  q5 = Quat(v1)
  m1 = Quat.from_mat3(Mat3(0,-1,0, 1,0,0, 0,0,1))
  q6 = Quat(m1)

  q1 += q2
  q2 -= q3
  q3 *= 2
  q4 /= 2

if __name__ == "__main__":


  run_vec2_test = None  
  run_vec3_test = None
  run_vec4_test = None

  run_quat_test = None

  run_mat2_test = None
  run_mat3_test = None

  for arg in sys.argv:
    print "Arg: {}".format(arg)
    if arg == "vec2":
      run_vec2_test = True
    elif arg == "vec3":
      run_vec3_test = True
    elif arg == "vec4":
      run_vec4_test = True
    elif arg == "quat":
      run_quat_test = True
    elif arg == "mat2":
      run_mat2_test = True
    elif arg == "mat3":
      run_mat3_test = True

  print "Starting Tests...\n"

  if run_vec2_test:
    test_vec2()
  if run_vec3_test:
    test_vec3()
  if run_vec4_test:
    test_vec4()

  if run_quat_test:
    test_quat()

  if run_mat2_test:
    test_mat2()
  if run_mat3_test:
    test_mat3()
