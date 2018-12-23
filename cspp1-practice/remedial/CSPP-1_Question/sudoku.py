'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.
    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_sudoku(s):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if len(s) < 81 or len(s) > 81:
        return "Invalid input"
    n = 9
    count = 0
    intlist = ['1','2','3','4','5','6','7','8','9']
    a = [s[i:i+n] for i in range(0, len(s), n)]
    for i in range(len(a)):
    	# for j in a[i]:
    	if '.' not in a[i]:
    		count += 1
    if count == 9:
    	return "Given sudoku is solved"
    for i in range(len(a)):
    	temp_list = intlist[:]
    	for j in a[i]:
    		if j == '.':
    			j == 'p'
    		else:
    			temp_list.remove(j)
    	# a = set(i)
    	# if len(a) != 9:
    	# 	return "Invalid Sudoku:Duplicate values"
    	for k in temp_list:
    		print(k)

    return ""
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    s = str(input())
    print(check_sudoku(s))

if __name__ == '__main__':
    main()


