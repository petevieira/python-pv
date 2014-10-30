#!/usr/bin/env python

import sys
from Vec3 import *
from Mat3 import *
from Quat import *

def test_Vec3():
	print "Testing Vec3...\n"

	v1 = Vec3(0.1, 5, -3.0)
	v2 = Vec3(1, 1, 3)
	v3 = (v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
	v3 = Vec3(v3)
	v4 = Vec3(10)
	v1 += v2
	v2 -= v3
	v3 *= 2
	v4 /= 2

	print "v1: {}".format(v1)
	print "v2: {}".format(v2)
	print "v3: {}".format(v3)
	print "v4: {}".format(v4)
	print "v1 + v2: {}".format(v1 + v2)
	print "v1 - v2: {}".format(v1 - v2)
	print "v1 * 3: {}".format(v1 * 3)
	print "v1 / 2: {}".format(v1 / 3)
	print "-v1: {}".format(-v1)
	print "abs(v1): {}".format(abs(v1))
	print "v1 . v2: {}".format(v1.dot(v2))
	print "v1 X v2: {}".format(v1.cross(v2))
	print "v1[i]: ({}, {}, {})".format(v1[0], v1[1], v1[2])
	print "v1 == v2: {}".format(v1 == v2)
	print "v1 is v2: {}".format(v1 is v2)
	print "v1 != v2: {}".format(v1 != v2)
	print "v1 is not v2: {}".format(v1 is not v2)
	print "v1.norm(): {}".format(v1.norm())
	print "v1.norm2(): {}".format(v1.norm2())
	print "v1.normalized(): {}".format(v1.normalize())
	print "lerp(v1,v2): {}".format(Vec3.lerp(v1, v2, .5))

def test_Mat3():
	print "Testing Mat3...\n"
	m1 = Mat3(
		1,0,0,
		0,1,0,
		0,0,1)
	v1 = Vec3(0, 1, 1.3)
	m2 = Mat3.from_cols(v1, v1, v1)
	m3 = Mat3(m2)
	print "m1:\n{}".format(m1)
	print "m2:\n{}".format(m2)

def test_Quat():
	print "Testing Quat...\n"
	q1 = Quat()
	q2 = Quat(.5, .5, .5, .5)
	v3 = (q1.x + q2.x, q1.y + q2.y, q1.z + q2.z, q1.w + q2.w)
	q3 = Quat(v3)
	q4 = Quat(10)
	v1 = Vec4(1, 2, 4, 5)
	q5 = Quat(v1)
	m1 = Mat3(1,0,0, 0,1,0, 0,0,1)
	q6 = Quat(m1)
	print "q1: {}".format(q1)
	print "q2: {}".format(q2)
	print "q3: {}".format(q3)
	print "q4: {}".format(q4)
	print "q5: {}".format(q5)
	print "q1+q2: {}".format(q1+q2)

	q1 += q2
	q2 -= q3
	q3 *= 2
	q4 /= 2
	print "q1 += q2: {}".format(q1)
	print "q2 -= q3: {}".format(q2)
	print "q3 *= 2: {}".format(q3)
	print "q4 /= 2: {}".format(q4)

if __name__ == "__main__":

	test_quat = None
	test_vec3 = None
	test_mat3 = None

	for arg in sys.argv:
		print "Arg: {}".format(arg)
		if arg == "--Quat":
			test_quat = True
		elif arg == "--Vec3":
			test_vec3 = True
		elif arg == "--Mat3":
			test_mat3 = True

	print "Starting Tests...\n\n"

	if test_vec3 :
		test_Vec3()
	if test_quat:
		test_Quat()
	if test_mat3:
		test_Mat3()
