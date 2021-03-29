#!/usr/bin/env python3

import unittest

from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
	def test_area(self):
		#test areas when R >= 0
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * (2.1 ** 2))

	def test_values(self):
		# make sure value errors are raised when necessary
		self.assertRaises(ValueError, circle_area, -2)

	def test_type(self):
		# Make sure type errors are raise when necessary
		self.assertRaises(TypeError, circle_area, 3+5j) #j is squ root -1
		self.assertRaises(TypeError, circle_area, True)
		self.assertRaises(TypeError, circle_area, "radius")

# to test: pypthon -m unittest debug_unittest