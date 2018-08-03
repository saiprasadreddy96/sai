"""
vowels
"""

S = input()
C = 0
I = 0
while I < len(S):
    if S[I] == 'a' or S[I] == 'e' or S[I] == 'i' or S[I] == 'o' or S[I] == 'u':
        C = C + 1
    I = I + 1
print(C)
