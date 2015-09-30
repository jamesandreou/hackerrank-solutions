# hackerrank - Algorithms: Maximizing XOR
# Written by James Andreou, University of Waterloo

L = int(raw_input())
R = int(raw_input())
max = 0
for a in range(L, R+1):
	for b in range(a, R+1):
		if a ^ b > max:
			max = a ^ b
print max