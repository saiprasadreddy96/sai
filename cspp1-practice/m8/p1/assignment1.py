# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(N):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n
    '''
    if N == 0 or N == 1:
        return 1
    else:
        return N*factorial(N-1)
    


def main():
    A = int(input())
    print(factorial(int(A)))    

if __name__== "__main__":
    main()
