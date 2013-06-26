#!/usr/bin/env python
import sys
import math

def do(x,y,fy):
	if 	len(y) == len(fy):
		n = len(y)

		for i in range (1, n):
			if y[i-1] < x and y[i] > x:
				a = (fy[i] - fy[i-1])/(y[i] - y[i-1])
				b = fy[i-1] - a*y[i-1]
				return a*x + b
			if y[i] == x:
				return fy[i]
		return -1
