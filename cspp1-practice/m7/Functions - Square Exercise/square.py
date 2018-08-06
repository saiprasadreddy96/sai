"""
square
"""


def square(x):
    '''
    x: int or float.
    '''
    return x*x
    


def main():
	data = input()
	data = float(data)
	temp = str(data).split('.')
	if(temp[1] == '0'):
		print(square(int(float(str(data)))))
	else:
		print(square(data))

if __name__== "__main__":
	main()

