'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """main"""
    list_l = []
    var_n = int(input())
    for each_line in range(var_n):
        list_l.append(input())
    for each_line in range(var_n):
        print(list_l[each_line])

if __name__ == '__main__':
    main()
