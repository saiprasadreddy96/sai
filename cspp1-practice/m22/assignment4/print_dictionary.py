'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
def print_dictionary(dictionary):
    """print"""
    temp_l = []
    temp_l.extend(dictionary.keys())
    #print(temp_l)
    for i in range(len(temp_l)-1):
        j = i + 1
        while j < len(temp_l):
            char_1 = temp_l[i]
            char_2 = temp_l[j]
            if char_1[0] > char_2[0]:
                temp = temp_l[i]
                temp_l[i] = temp_l[j]
                temp_l[j] = temp
            j += 1
    #print(temp_l)
    for each_i in temp_l:
        print(each_i,'-', dictionary[each_i])
def main():
    """main"""
    dictionary = eval(input())
    print_dictionary(dictionary)
if __name__ == '__main__':
    main()
