'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def sudoku1(sudoku):
    #print(1)
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j] == '.'):
                sudoku2(sudoku, i, j)
def sudoku2(sudoku, i, j):
    #print("hi")
    a = set()
    for k in range(9):
        #print(sudoku[i][k])
        a.add(sudoku[i][k])
    #print(a)
    for l in range(9):
        #print(sudoku[l][j])
        a.add(sudoku[l][j])
    #print(a)
    m = int(i / 3) * 3
    n = int(j / 3) * 3
    #print(m)
    #print(n)
    p = m
    q = n
    while p < m+3:
        q = n
        while q < n+3:
            #print(sudoku[p][q])
            a.add(sudoku[p][q])
            q = q + 1
        p = p + 1
    #print(a)
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    str1 = ""
    for i in range(9):
        if l[i] not in a:
            str1 += l[i]
            #print(l[i])

    println(str1)




def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    temp_list1 = []
    temp_list2 = []
    temp1 = []
    temp2 = []
    for each_i in range(len(sudoku)):
        temp_list1 = sudoku[each_i]
        temp_list2 = []
        for each_j in range(9):
            temp_list2.append(sudoku[each_j][each_i])
        if  sorted(temp_list1) != [1, 2, 3, 4, 5, 6, 7, 8, 9] or sorted(temp_list2) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    for i in range(3):
        for j in range(3):
            temp_list3 = []
            for k in range(3):
                for l in range(3):
                    temp_list3.append(sudoku[k+(3*i)][l+(3*j)])
            if sorted(temp_list3) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
    return True
#def sudoku1():
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []
    # loop to read 9 lines of input from console
    #for i in range(9):
        # read a line, split it on SPACE and append row to list
    str = input()
    #for i in range(9):
    j = 0
    k = 9
    for i in range(9):
        row = list(str[j:k])
        sudoku.append(row)
        j = j + 9
        k = k + 9
    #for i in range(9):
        #print(sudoku[i])
        
    # call solution function and print result to console
    #print(sudoku)
    #print(check_sudoku(sudoku))
    sudoku1(sudoku)
if __name__ == '__main__':
    main()

