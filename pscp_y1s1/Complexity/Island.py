""" Greedy n Recursion """
def main(rnc):
    """ main function """
    terra = [ input().split() for _ in range( rnc[0] ) ]
    count = 0
    for i in range( rnc[0] ):
        while "1" in terra[i]:
            terra = islander( terra, terra[i].index('1'), i )
            count+=1
    print(count)

def islander(hill, posx, posy):
    """ island count """
    hill[posy][posx] = "0"

    if posy and hill[posy-1][posx] == '1':
        hill = islander(hill, posx, posy-1)

    if posy and posx and hill[posy-1][posx-1] == '1':
        hill = islander(hill, posx-1, posy-1)

    if posy and posx != len( hill[posy] )-1 and hill[posy-1][posx+1] == '1':
        hill = islander(hill, posx+1, posy-1)

    if posx and hill[posy][posx - 1] == '1':
        hill = islander(hill, posx-1, posy)

    if posx != len( hill[posy] )-1 and hill[posy][posx + 1] == '1':
        hill = islander(hill, posx+1, posy)

    if posy != len(hill) - 1 and hill[posy + 1][posx] == '1':
        hill = islander(hill, posx, posy+1)

    if posy != len(hill) - 1 and posx and hill[posy+1][posx-1] == '1':
        hill = islander(hill, posx-1, posy+1)

    if posy != len(hill) - 1 and posx != len( hill[posy] )-1 and hill[posy+1][posx+1] == '1':
        hill = islander(hill, posx+1, posy+1)
    return hill
main( list( map( int, input().split() ) ) )
