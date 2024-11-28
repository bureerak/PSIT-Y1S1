""" Ascending Sort """
def sort_ascen(n = int( input() )):
    """ print sort """
    num = sorted([int( input() ) for _ in range(n)])
    for i in num:
        print(i)
sort_ascen()
