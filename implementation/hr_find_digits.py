# hackerrank - Algorithms: Find Digits
# Written by James Andreou, University of Waterloo

T = int(raw_input())
for t in range(0,T):
	N = int(raw_input())
	newN = N
	count = 0
	for i in range(10, -1, -1):
		Q = newN / 10 ** i
		if Q != 0 and N % Q == 0:
			count += 1
		newN -= Q * 10**i
	print count

