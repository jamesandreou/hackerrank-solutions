# hackerrank - Algorithms: Chocolate Feast
# Written by James Andreou, University of Waterloo

T = int(raw_input())
for t in range(0, T):
	line = map(int, str.split(raw_input()))
	N, C, M, total, wrappers = line[0], line[1], line[2], 0, 0
	#spend all money
	total += N / C
	wrappers = total
	while wrappers >= M:
		total += wrappers / M
		wrappers = wrappers % M + wrappers / M
	print total

