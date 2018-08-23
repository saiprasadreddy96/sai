def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    matrix_4 = []
    list_1 = []
    if rows_m2 == columns_m1:
        for i in range(rows_m1):
            for j in range(columns_m2):
                temp_sum = 0
                for k in range(rows_m2):
                    temp_sum = temp_sum + ((matrix_1[i][k]) * (matrix_2[k][j]))
                list_1.append(temp_sum)
            matrix_4.append(list_1)
            list_1 = []
        return matrix_4
    else:
        print("Error: Matrix shapes invalid for mult")
        return None
def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    matrix_3 = []
    list_1 = []
    try:
        for i in range(rows_m1):
            for j in range(columns_m1):
                list_1.append((matrix_1[i][j]) + (matrix_2[i][j]))
            matrix_3.append(list_1)
            list_1 = []
        return matrix_3
    except:
        print("Error: Matrix shapes invalid for addition")
        return None
def read_matrix(r, c):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    m = [];
    try:
        for i in range(r):
            temp = input()
            list_1 = temp.split()
            list_1 = list(map(int, list_1))
            m.append(list_1)
            if len(list_1) != c:
                print("Error: Invalid input for the matrix")
                return None
        return m
    except:
        print("Error: Invalid input for the matrix")
        return None
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    """main"""
    temp = input()
    global rows_m1, columns_m1, rows_m2, columns_m2
    rows_m1 = int(temp[0:1])
    columns_m1 = int(temp[2:])
    matrix_1 = []
    matrix_1 = read_matrix(rows_m1, columns_m1)
    temp = input()
    rows_m2 = int(temp[0:1])
    columns_m2 = int(temp[2:])
    matrix_2 = []
    matrix_2 = read_matrix(rows_m2, columns_m2)
    matrix_3 = []; matrix_4 = []
    if matrix_1 != None and matrix_2 != None:
        matrix_3 = add_matrix(matrix_1, matrix_2)
        print(matrix_3)
        matrix_4 = mult_matrix(matrix_1, matrix_2)
        print(matrix_4)
if __name__ == '__main__':
    main()
