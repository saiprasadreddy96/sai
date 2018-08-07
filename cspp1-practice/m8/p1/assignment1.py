# Exercise: Assignment-1
"""
fact
"""
def factorial(var_N):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n
    '''
    if var_N in [0 1]:
        return 1
    return var_N*factorial(var_N-1)
def main():
    var_A = int(input())
    print(factorial(int(var_A)))    

if __name__ == "__main__":
    main()
