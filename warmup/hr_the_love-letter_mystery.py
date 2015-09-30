# hackerrank - Algorithms: The Love Letter Mystery
# Written by James Andreou, University of Waterloo

N = int(raw_input())
for t in range(0, N):
	word = raw_input()
	pos1 = 0
	pos2 = len(word) -1;
	steps = 0
	while pos1 < pos2:
		steps += abs(ord(word[pos1]) - ord(word[pos2]))
		pos1 += 1;
		pos2 -= 1;
	print steps