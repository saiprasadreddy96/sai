"""
fizz_buzz
"""
N = int(input())
I = 1
while I <= N:
    if I % 3 == 0 and I % 5 == 0:
        print("FizzBuzz")
    elif I % 3 == 0:
        print("Fizz")
    elif I % 5 == 0:
        print("Buzz")
    else:
        print(I)
    I = I + 1

    
