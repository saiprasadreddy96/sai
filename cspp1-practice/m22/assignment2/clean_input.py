'''
Write a function to clean up a given string by removing the special characters and retain alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    """clean string"""
    var_l = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', ' ', '.']
    var_string1 = ""
    for each_char in string:
        if each_char not in var_l:
            var_string1 += each_char
    return var_string1
def main():
    """main"""
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
