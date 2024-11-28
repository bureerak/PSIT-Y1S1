""" Duplicate I """
def redun(m, n):
    """ redundance data """
    m_group, n_group = set(), set()
    for _ in range(m):
        m_group.add( int(input()) )
    for _ in range(n):
        n_group.add( int(input()) )
    red = m_group & n_group
    if red:
        print(*sorted(red,reverse=True),sep="\n",end="")
    else:
        print("Nope",end="")
redun(int( input() ), int( input() ))
