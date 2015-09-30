# hackerrank - Algorithms: Sherlock and The Beast
# Written by James Andreou, University of Waterloo

# Binary string approach mapping digit 0 -> 3 and 1 -> 5

# Pad numbers with 0s
def pad(num, n):
	z = '0' * (n - len(num))
	return z + num
# Convert from 0,1 binary strings to 3,5
def convertToThreeFive(x):
	if x == '0':
		return '3'
	else:
		return '5'

T = int(raw_input())

for t in range(0, T):
	N = int(raw_input())
	L = '-1'
	i = 2**N
	while i >= 0:
		num = bin(i)[2:]
		if len(num) < N:
			num = pad(num, N)
		if num.count('0') % 5 == 0 and num.count('1') % 3 == 0:
			L = map(convertToThreeFive, num)
			L = ''.join(L)
			break
		i -= 1
	print L

