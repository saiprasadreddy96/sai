# Exercise: Assignment-2
def sumofdigits(num_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if num_n <= 0:
        return 0
    num_sum = num_n % 10
    return num_sum + sumofdigits(num_n//10)
def main():
    """
    main
    """
    num_a = input()
    print(sumofdigits(int(num_a)))  
if __name__ == "__main__":
    main()

