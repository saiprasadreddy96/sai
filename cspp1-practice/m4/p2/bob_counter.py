"""
bob counter
"""
S = input()
S1 = "bob"
C = 0
I = 0
while I < (len(S) - len(S1) + 1):
    J = I
    if S[J : J + 3] == S1:
        C = C + 1
    I = I + 1
print(C)

