# hackerrank - Algorithms: Lonely Integer
# Written by James Andreou, University of Waterloo

N = int(raw_input())
A = map(int, str.split(raw_input()))
A.sort()
for i in range(0, N, 2):
	if i == N-1 or A[i] != A[i+1]:
		print A[i]
		break