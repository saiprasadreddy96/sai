a=input("Enter the value of a")
b=input("Enter the value of b")

try:
    x=int(a)
    y=int(b)
    if x < y:
        print("smaller")
    elif x == y:
        print("equal")
    else:
        print("bigger")

except:
    print("string involved")
    
    
    
    
    
