#!/usr/bin/env python
import sys
import math
import pylab
from matplotlib import mlab

import read_from_file
import linear_int


[price, supply, demand] = read_from_file.do(sys.argv[0], sys.argv[1])
#x = linear_int.do(1.5, price, supply)

x = []
n = len(price) - 1
curr = price[0]
while curr <= price[n]:
	x.append(curr)
	curr = round(curr + 0.2, 2)
#print x

f = [supply[0]]
k = len(x)
for i in range(1, k):
	f.append(round(linear_int.do(x[i], price, supply), 2))
#print f

g = [demand[0]]
for i in range(1, k):
	g.append(round(linear_int.do(x[i], price, demand), 2))
#print g

pylab.plot(x, f)
pylab.hold(True)
pylab.plot(x, g, 'r')
pylab.show()





