# hackerrank - Algorithms: Is Fibo
# Written by James Andreou, University of Waterloo
import math

def perfect_square(n):
    r = math.sqrt(n)
    return int(r + 0.5) ** 2 == n
        

T = int(raw_input())
for t in range(0, T):
	N = int(raw_input())**2 * 5
	if perfect_square(N+4) or perfect_square(N-4):
		print 'IsFibo'
	else:
		print 'IsNotFibo'