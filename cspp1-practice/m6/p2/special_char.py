'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    S = input()
S1 = ""
I = 0
while I < len(S):
    if S[I] == '!' or S[I] == '@' or S[I] == '#' or S[I] == '$' or S[I] == '%' or S[I] == '^' or S[I] == '&' or S[I] == '*':
        S1 = S1 + ' '
    else:
        S1 = S1 + S[I]
    I = I + 1
print(S1)


if __name__ == "__main__":
    main()
