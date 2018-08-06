"""
odd or even
"""



def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    if x % 2 == 1:
        a = "true"
        return a
    else:
        a = "false"
        return a
    

def main():
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
