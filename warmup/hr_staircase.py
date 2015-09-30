# hackerrank - Algorithms: Staircase
# Written by James Andreou, University of Waterloo

N = int(raw_input())
for n in range(0, N):
	S = ""
	for c in range(0, N - n - 1):
		S += " "
	for c in range(0, n + 1):
		S += "#"
	print S