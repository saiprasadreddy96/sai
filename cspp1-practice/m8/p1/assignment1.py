# Exercise: Assignment-1
"""
fact
"""
def factorial(var_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n
    '''
    if var_n in [0, 1]:
        return 1
    return var_n * factorial(var_n-1)
def main():
    """
    main
    """
    var_a = int(input())
    print(factorial(int(var_a)))
if __name__ == "__main__":
    main()
