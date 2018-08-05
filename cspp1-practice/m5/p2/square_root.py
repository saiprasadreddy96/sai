"""
square root approximation
"""
N = int(input())
EPSILON = 0.1
A = 0
A = int(A)
while (N - (A*A) > EPSILON) and A < N:
    if N - (A*A) > EPSILON:
        A = A + EPSILON
print(A)
