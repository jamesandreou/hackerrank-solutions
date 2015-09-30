# hackerrank - Algorithms: Caesar Cipher
# Written by James Andreou, University of Waterloo
N = int(raw_input())
S = raw_input()
K = int(raw_input()) % 26
NEW = ""
for c in S:
	if ord(c) >= ord('A') and ord(c) <= ord('Z'):
		if ord(c) + K > ord('Z'):
			NEW += chr(ord('A') + (K - (ord('Z') - ord(c))) - 1)
		else:
			NEW += chr(ord(c) + K)
	elif ord(c) >= ord('a') and ord(c) <= ord('z'):
		if ord(c) + K > ord('z'):
			NEW += chr(ord('a') + (K - (ord('z') - ord(c))) - 1)
		else:
			NEW += chr(ord(c) + K)
	else:
		NEW += c
print NEW
