#!/usr/bin/env python
import sys

def do(sa0, sa1):
	try:
		infilename = sa1
	except:
		print "Usage: ", sa0, " infile outfile"
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

	return price, supply, demand
