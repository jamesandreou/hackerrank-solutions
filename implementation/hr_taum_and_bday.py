# hackerrank - Algorithms: Taum and Bday
# Written by James Andreou, University of Waterloo

T = int(raw_input())
for t in range(0, T):
    B, W = map(int, raw_input().split())
    X, Y, Z = map(int, raw_input().split())
    print min(X, Y + Z) * B + min (Y, X + Z) * W
    