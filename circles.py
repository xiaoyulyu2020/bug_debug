#!/usr/bin/env python3

from math import pi

def circle_are(r):
	if type(r) not in [int, float]:
		raise TypeError("The R must be a non-negative real number!")
	if r < 0:
		raise ValueError("The R can not be negative")

	return pi * (r ** 2)
