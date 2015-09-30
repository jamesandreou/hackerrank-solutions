# hackerrank - Algorithms: Cavity Map
# Written by James Andreou, University of Waterloo

N = int(raw_input())
M = []
# Load map from stdin
for i in range(0, N):
	ROW = []
	line = raw_input()
	for r in range(0, N):
		ROW.append(int(line[r]))
	M.append(ROW)
# Check if cavity
for row in range(0, N):
	output = ''
	for col in range(0, N):
		D = M[row][col]
		if row != N-1 and row != 0 and col != 0 and col != N-1 and M[row-1][col] < D and M[row+1][col] < D and M[row][col-1] < D and M[row][col+1] < D:
			output += 'X'
		else:
			output += str(D)
	print output
