def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    m4 = []
    l1 = []
    if c1 == r2:
        for i in range(r1):
            for j in range(c2):
                sum = 0
                for k in range(r2):
                    sum = sum + (int(m1[i][k]) * int(m2[k][j]))
                l1.append(sum)
            m4.append(l1)
            l1 = []
    return m4
                                  

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    m3 = []
    l1 = []
    if r1 == r2 and c1 == c2:
        for i in range(r1):
            for j in range(c1):
                l1.append(int(m1[i][j]) + int(m2[i][j]))
            m3.append(l1)
            l1 = []
    return m3
        

def read_matrix(r, c):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    m = []
    for i in range(r):
        temp = input()
        l1 = temp.split()
        m.append(l1)
    return m

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    temp = input()
    global r1
    r1 = int(temp[0:1])
    global c1
    c1 = int(temp[2:])
    m1 = []
    m1 = read_matrix(r1, c1)
    temp = input()
    global r2
    r2 = int(temp[0:1])
    global c2
    c2 = int(temp[2:])
    m2 = []
    m2 = read_matrix(r2, c2)
    m3 = []
    m3 = add_matrix(m1, m2)
    m4 = []
    m4 = mult_matrix(m1, m2)
    print(m3)
    print(m4)

    
if __name__ == '__main__':
    main()