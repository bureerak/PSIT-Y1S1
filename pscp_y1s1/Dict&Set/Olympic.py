""" Olympic """
def champion(num:int):
    """ list score """
    board = [ input().split() for _ in range(num) ]
    board.sort( key=lambda x: x[0] )
    board.sort( key = lambda x: ( int(x[1]), int(x[2]), int(x[3]) ), reverse=True )
    total = list(map(lambda x: int(x[1]) + int(x[2]) + int(x[3]), board))
    prev, fprint = None, None
    for i in range(1,num+1):
        x = f"{board[i-1][1]} {board[i-1][2]} {board[i-1][3]}"
        if x != prev:
            fprint, prev = i, x
        print(fprint,board[i-1][0],x,total[i-1])
champion( int( input() ) )
