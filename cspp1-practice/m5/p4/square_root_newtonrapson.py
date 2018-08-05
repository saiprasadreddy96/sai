"""
Newton Raphson Method
"""
EPSILON = 0.01
A = int(input())
GUESS = A/2.0
while abs(GUESS*GUESS - A) >= EPSILON:
    GUESS = GUESS - (((GUESS**2) - A)/(2*GUESS))
print(GUESS)
