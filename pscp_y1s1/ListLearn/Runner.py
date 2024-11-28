""" Runner """
def find_winner(dist,member):
    """ return winner """
    stat, new = [input().split() for _ in range(member)], []
    stat = [[int(x[0]),int(x[1])] for x in stat]
    new += list(map(lambda a: (dist - a[1]) / a[0] , stat))
    low = min(new)
    dp = [x for x in stat if (dist - x[1]) / x[0] == low]
    dp.sort(key=lambda a: a[0],reverse=True)
    print(stat.index(dp[0])+1)
find_winner(int( input() ), int( input() ))
