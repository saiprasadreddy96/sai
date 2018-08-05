"""
perfect cube
"""
G = 1
N = int(input(""))
F = 0
while G < N+1:
    if G**3 == N:
        print(str(N) + " " + "is a perfect cube")
        F = 1
        break
    G = G + 1
if F == 0:
    print(str(N) + " " + "is not a perfect cube")
