# hackerrank - Algorithms: Halloween Party
# Written by James Andreou, University of Waterloo

T = int(raw_input())
for t in range(0, T):
	K = int(raw_input())
	print (K / 2) * (K / 2 + K % 2)
