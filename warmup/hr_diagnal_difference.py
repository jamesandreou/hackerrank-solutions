# hackerrank - Algorithms: Diagnal Difference
# Written by James Andreou, University of Waterloo
N = int(raw_input())
M = []
for a in range(0, N):
	M.append(map(int, str.split(raw_input())))
print abs(sum (M[i][i] for i in range(0,len(M))) - sum (M[i][len(M)-i-1] for i in range(0, len(M))))

