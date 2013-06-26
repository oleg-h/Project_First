#!/usr/bin/env python
import sys

try:
	infilename = sys.argv[1]
except:
	print "Usage: ", sys.argv[0], " infile outfile"
 	sys.exit(1)
 
ifile = open(infilename, 'r')

price = []
supply = []
demand = []

for line in ifile :
	ln = line.split(":")
	price += [float(ln[0].strip())]
	supply += [float(ln[1].strip())]
	demand += [float(ln[2].strip())]
ifile.close()

#return price, supply, demand
print price, supply, demand
