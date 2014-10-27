#!/usr/bin/env python

class Quat(Vec4):
	def __init__(self, *args):
		if len(args) == 0:
			self.q = Vec4(0, 0, 0, 1)
		elif len(args) == 4:
			self.q = Vec4(*args)
		elif len(args) == 1:
			arg_type = type(*args)
			if arg_type is int or arg_type is float:
				self.initialize_from_scalar(*args)
			elif arg_type is tuple or arg_type is list:
				self.initialize_from_tuple(*args)
			elif arg_type is Vec4:
				self.q = *args
			else:
				print "Error initializing Vec4. Invalid type {}".format(arg_type)
		else:
			print "Error initializing Vec4. Valid number of arguments "
			print "is 1 or 4. You pass {} arguments".format(len(args))

def fromAxisAngle(axis, angle):
	axis_norm = axis.norm()
	sine_angle = sin(angle/2)
	x = axis.x() * sine_angle / axis_norm
	y = axis.y() * sine_angle / axis_norm
	z = axis.z() * sine_angle / axis_norm
	u = cos(angle/2)
	return Quat(x, y, z, u)