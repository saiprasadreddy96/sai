"""
digit_product
"""
N = int(input())
P = 1
if N < 0:
    N = -N
    P = P * -1
while N >= 1:
    P = P * ( N % 10 )
    N = N // 10
print(P)
