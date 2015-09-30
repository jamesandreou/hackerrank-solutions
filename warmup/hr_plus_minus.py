# hackerrank - Algorithms: Plus Minus
# Written by James Andreou, University of Waterloo
N = float(raw_input())
A = map(int, str.split(raw_input()))
print ("%.3f" % (len(filter(lambda x : x > 0, A)) / N))
print ("%.3f" % (len(filter(lambda x : x < 0, A)) / N))
print ("%.3f" % (len(filter(lambda x : x == 0, A)) / N))