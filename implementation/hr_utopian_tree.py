# hackerrank - Algorithms: Utopian Tree
# Written by James Andreou, University of Waterloo

nTests = int(raw_input())
for t in range(0, nTests):
	height = 1
	t = int(raw_input())
	for n in range(0, t):
	    if n % 2 == 0:
	        height *= 2
	    else:
	        height += 1
	print height