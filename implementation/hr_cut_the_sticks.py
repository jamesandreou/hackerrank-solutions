# hackerrank - Algorithms: Cut the sticks
# Written by James Andreou, University of Waterloo

N = int(raw_input())
S = map(int, str.split(raw_input()))
while len(S) > 0:
	S.sort()
	min = S[0]
	print len(S)
	S = map(lambda x : x - min, S)
	S = filter(lambda x : x > 0, S)
