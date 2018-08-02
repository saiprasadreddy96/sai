S = input()
S = S + " "
I = 0
LEN1 = -1
while I < (len(S) - 2):
    J = I
    while S[J] <= S[J+1] and (J) < (len(S)-2):
        J = J + 1
    LEN2 = J - I
    if LEN2 > LEN1:
        LEN1 = LEN2
        K = int(I)
        L = int(J)
    I = J + 1
while K <= L:
    print(S[K])
    K = K + 1
