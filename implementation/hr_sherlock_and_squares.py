# hackerrank - Algorithms: Sherlock and Squares
# Written by James Andreou, University of Waterloo

import math

T = int(raw_input())
for t in range(0, T):
	N = raw_input().split()
	# convert range bounds to their closest squares within range for O(1) solution
	a = math.ceil(math.sqrt(int(N[0])))
	b = math.floor(math.sqrt(int(N[1])))
	if a <  b:
		print 2 + int(b-a-1)
	elif a == b :
		print 1
	else :
		print 0 