global ttt, pos_input, count_input, x, o
ttt = [];pos_input = ['o', 'x', '.'];count_input = {'o':0, 'x':0, '.':0};x = ['x', 'x', 'x'];o = ['o', 'o', 'o']
def game_ttt():
    global c_x, c_o
    c_x = 0;c_o = 0
    for i in range(3):
        if ttt[i] == x or [ttt[0][i], ttt[1][i], ttt[2][i]] == x:
            c_x += 1
        if ttt[i] == o or [ttt[0][i], ttt[1][i], ttt[2][i]] == o:
            c_o += 1
    if [ttt[0][0], ttt[1][1], ttt[2][2]] == x or [ttt[0][2], ttt[1][1], ttt[2][0]] == x:
        c_x += 1
    if [ttt[0][0], ttt[1][1], ttt[2][2]] == o or [ttt[0][2], ttt[1][1], ttt[2][0]] == o:
        c_o += 1
def check_invalid():
    for i in range(3):
        for j in range(3):
            if ttt[i][j] not in pos_input:
                return 0
            count_input[ttt[i][j]] += 1
    return 1
def read_input():
    str_line = []
    for i in range(3):
        str_line = input()
        str_line = str_line.split()
        ttt.append(str_line)
def write_output():
    if (check_invalid() == 0):
        print("invalid input")
    elif count_input['o'] != count_input['x']:
        print("invalid game")
    else:
        game_ttt()
        if c_x == 1 and c_o ==1:
            print("x o")
        elif c_x == 1:
            print("x")
        elif c_0 == 1:
            print("o")
        else:
            print("draw")
        
def main():
    read_input()
    write_output()
main()
