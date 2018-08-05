"""
SQUARE ROOT BISECTOIN
"""
A = int(input())
EPSILON = 0.01
LOW = 0.0
HIGH = A
ANS = (HIGH + LOW)/2.0
while abs(ANS**2 - A) >= EPSILON:
    if ANS**2 < A:
        LOW = ANS
    else:
        HIGH = ANS
    ANS = (HIGH + LOW)/2.0
print(ANS)
