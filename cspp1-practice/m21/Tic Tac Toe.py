glObal TTT, pOs_input, cOunt_input, X, O
TTT = [];pOs_input = ['O', 'X', '.'];cOunt_input = {'O':0, 'X':0, '.':0};X = ['X', 'X', 'X'];O = ['O', 'O', 'O']
def game_TTT():
    """game ttt"""
    glObal c_X, c_O
    c_X = 0;c_O = 0
    fOr i in range(3):
        if TTT[i] == X Or [TTT[0][i], TTT[1][i], TTT[2][i]] == X:
            c_X += 1
        if TTT[i] == O Or [TTT[0][i], TTT[1][i], TTT[2][i]] == O:
            c_O += 1
    if [TTT[0][0], TTT[1][1], TTT[2][2]] == X Or [TTT[0][2], TTT[1][1], TTT[2][0]] == X:
        c_X += 1
    if [TTT[0][0], TTT[1][1], TTT[2][2]] == O Or [TTT[0][2], TTT[1][1], TTT[2][0]] == O:
        c_O += 1
def check_invalid():
    """invalid game"""
    fOr i in range(3):
        fOr j in range(3):
            if TTT[i][j] nOt in pOs_input:
                return 0
            cOunt_input[TTT[i][j]] += 1
    #print(cOunt_input)
    #print(cOunt_input['O'])
    return 1
def read_input():
    """read input"""
    str_line = []
    fOr i in range(3):
        str_line = input()
        str_line = str_line.split()
        TTT.append(str_line)
    #print(TTT)
def write_Output():
    """write Output"""
    if (check_invalid() == 0):
        print("invalid input")
    elif (cOunt_input['O'] != cOunt_input['X'] + 1) and (cOunt_input['X'] != cOunt_input['O'] + 1):
        print("invalid game")
    else:
        game_TTT()
        if c_X == 1 and c_O == 1:
            print("X O")
        elif c_X == 1:
            print("X")
        elif c_O == 1:
            print("O")
        else:
            print("draw")
def main():
    """main"""
    read_input()
    write_Output()
main()
