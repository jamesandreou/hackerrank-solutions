# hackerrank - Algorithms: Angry Professor
# Written by James Andreou, University of Waterloo

T = int(raw_input())
for t in range(0, T):
	line =  map(int, str.split(raw_input()))
	N = line[0]
	K = line[1]
	S = map(int, str.split(raw_input()))
	if len(filter(lambda x : x <= 0, S)) < K:
		print 'YES'
	else:
		print 'NO'
