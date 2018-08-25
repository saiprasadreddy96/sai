'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def frequency_graph(dictionary):
   """print"""
   global temp_l
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
           elif char_1[0] == char_2[0]:
               if char_1[1] > char_2[1]:
                   temp = temp_l[i]
                   temp_l[i] = temp_l[j]
                   temp_l[j] = temp
           j += 1
def main():
    """main"""
    global dictionary
    dictionary = eval(input())
    frequency_graph(dictionary)
    for each_i in temp_l:
        str = ''
        t_t = int(dictionary[each_i])
        for each_j in range(t_t):
            str += '#'
        print(each_i, '-', str)
if __name__ == '__main__':
    main()
