#!/usr/bin/env python

from Vec3 import *

def test_Vec3():
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

if __name__ == "__main__":
	test_Vec3()