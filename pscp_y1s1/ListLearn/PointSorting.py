""" lambda test """
def pointsort(num = int( input() )):
    """ returned point in order """
    for _ in range(num):
        xnum = int( input() )
        xarr = [input().split() for _ in range(xnum)]
        xarr = [[int(x[0]),int(x[1])] for x in xarr]
        xarr.sort(key=lambda x: x[1],reverse=True)
        xarr.sort(key=lambda x: x[0] + x[1])
        for i in xarr:
            print(*i)
pointsort()
