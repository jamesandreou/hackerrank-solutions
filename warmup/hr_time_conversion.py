# hackerrank - Algorithms: Time Conversion
# Written by James Andreou, University of Waterloo

S = raw_input()
TYPE = S[len(S)-2]
if S[:2] == "12":
	if TYPE == "A":
		print "00" + S[2:-2]
	else:
		print S[:-2]
elif TYPE == "P":
	HOUR = int(S[:2]) + 12
	print str(HOUR) + S[2:-2]
else:
	print S[:-2]