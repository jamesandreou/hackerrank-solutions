# hackerrank - Algorithms: Service Lane
# Written by James Andreou, University of Waterloo
line = map(int, str.split(raw_input()))
N = line[0]
T = line[1]
width = map(int, str.split(raw_input()))
for t in range(0, T):
	min_width = 3
	line = map(int, str.split(raw_input()))
	for i in range(line[0], line[1]+1):
		if width[i] < min_width:
			min_width = width[i]
	print min_width
