#!/usr/bin/env python

from distutils.core import setup

setup(name='MathPy',
      version='1.0',
      description='Math Livrary for Kinematics',
      author='Pete Vieira',
      py_modules=['Vec2', 'Vec3', 'Vec4', 'Mat2',
                'Mat3', 'Mat4', 'Quat', 'Pose'],
      )