'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
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
        temp1 = sorted(temp_list1)
        temp2 = sorted(temp_list2)
        if  temp1 != [1, 2, 3, 4, 5, 6, 7, 8, 9] or temp2 != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    """temp_list3 = [0] * 9
    for each_i in range(9):
        temp_list3[each_i] = [0] * 9
    temp_list4 = [0] * 9
    k = 0
    for each_i in range(len(sudoku)):
        for each_j in range(9):
            if each_i in [1, 2, 0] and each_j in [1, 2, 0]:
                temp_list3[0][temp_list4[0]] = sudoku[each_i][each_j]
                temp_list4[k] += 1
            elif each_i in [1, 2, 0] and each_j in [4, 5, 3]:
                temp_list3[1][temp_list4[1]] = sudoku[each_i][each_j]
                temp_list4[1] += 1
            elif each_i in [1, 2, 0] and each_j in [7, 8, 6]:
                temp_list3[2][temp_list4[2]] = sudoku[each_i][each_j]
                temp_list4[2] += 1
            elif each_i in [4, 5, 3] and each_j in [1, 2, 0]:
                temp_list3[3][temp_list4[3]] = sudoku[each_i][each_j]
                temp_list4[3] += 1
            elif each_i in [4, 5, 3] and each_j in [4, 5, 3]:
                temp_list3[4][temp_list4[4]] = sudoku[each_i][each_j]
                temp_list4[4] += 1
            elif each_i in [4, 5, 3] and each_j in [7, 8, 6]:
                temp_list3[5][temp_list4[5]] = sudoku[each_i][each_j]
                temp_list4[5] += 1
            elif each_i in [7, 8, 6] and each_j in [1, 2, 0]:
                temp_list3[6][temp_list4[6]] = sudoku[each_i][each_j]
                temp_list4[6] += 1
            elif each_i in [7, 8, 6] and each_j in [4, 5, 3]:
                temp_list3[7][temp_list4[7]] = sudoku[each_i][each_j]
                temp_list4[7] += 1
            elif each_i in [7, 8, 6] and each_j in [7, 8, 6]:
                temp_list3[8][temp_list4[8]] = sudoku[each_i][each_j]
                temp_list4[8] += 1
    for each_i in range(len(temp_list3)):
        temp_list1 = temp_list3[each_i]
        if sorted(temp_list1) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False"""
    """for i in range(3):
        for j in range(3):
            for k in range("""
    return True
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []
    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        row = list(map(int, row))
        sudoku.append(row)
    # call solution function and print result to console
    #print(sudoku)
    print(check_sudoku(sudoku))
if __name__ == '__main__':
    main()
