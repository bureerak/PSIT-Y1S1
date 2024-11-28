""" Difference """
def diff(n, m):
    """ set practice """
    a, b = set(), set()
    for _ in range(n):
        a.add( int(input()) )
    for _ in range(m):
        b.add( int(input()) )
    print(*sorted(a-b))
diff( int(input()), int(input()) )
