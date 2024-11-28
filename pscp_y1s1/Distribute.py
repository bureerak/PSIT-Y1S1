""" Distribute """
def main( money, child, can_count = 0 ):
    """ Distribute """
    if money < child:
        print(-1)
        return
    if money - child < 8:
        print(0)
        return
    can_count = min( money // 8, child )
    can_count -= 1 if money - can_count * 8 > 0 or money // 8 < child else 0
    print( max( 0, can_count ) )

main( int(input()), int(input()) )
