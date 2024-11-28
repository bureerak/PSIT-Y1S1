""" TicTacToe """
def tictoc():
    """ main function """
    bord = [ list(input()) for _ in range(3) ]
    diag_1 = set(list(bord[0][0]) + list(bord[1][1]) + list(bord[2][2]))
    diag_2 = set(list(bord[0][2]) + list(bord[1][1]) + list(bord[2][0]))
    for i in range(3):
        win_row = set(bord[i])
        win_col = set(list(bord[0][i]) + list(bord[1][i]) + list(bord[2][i]))
        len_row, len_col = len(win_row), len(win_col)
        if 1 in (len_row, len_col):
            toprint = min(win_col,win_row)
            if '-' in toprint:
                continue
            print(*min(win_col,win_row),"WIN")
            return
    if 1 in (len(diag_1),len(diag_2)):
        toprint = min(diag_1,diag_2)
        if '-' in toprint:
            print('DRAW')
            return
        print(*toprint,"WIN")
        return
    print('DRAW')
tictoc()
