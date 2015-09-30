# hackerrank - Algorithms: Manasa and Stones
# Written by James Andreou, University of Waterloo

T = int(raw_input())
for t in range(0, T):
	N = int(raw_input())
	A = int(raw_input())
	B = int(raw_input())
	OUTPUT = []
	for n in range(0, N):
		OUTPUT.append(n*B + (N-n-1)*A)
	OUTPUT = list(set(OUTPUT))
	OUTPUT.sort()
	for o in OUTPUT:
		print (o),
	print
