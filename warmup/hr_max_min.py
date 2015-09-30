# hackerrank - Algorithms: Max Min
# Written by James Andreou, University of Waterloo
N = int(raw_input())
K = int(raw_input())
NUMS = []
for i in range(0, N) :
	NUMS.append(int(raw_input()))
MIN = max(NUMS)
NUMS.sort()
#sort for O(n), O(n^2) if you dont sort and will timeout on large input test cases
for i in range(K-1, N):
	newMIN = NUMS[i] - NUMS[i-K+1]
	if newMIN < MIN :
		MIN = newMIN
print MIN