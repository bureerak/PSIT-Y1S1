""" Century """
def century():
    """ find century """
    num = int( input() )
    for _ in range(num):
        year = input()
        be = int(year[year.find(" ")+1:])
        if year.find("B.E.") != -1:
            be-=543
        newbe = divmod(be,100)
        ans = newbe[0]+1 if newbe[1] else newbe[0]
        print(int(ans) if be>=0 else "ERROR")
century()
