""" circular prime """
def primer(n):
    """ return prime """
    n = int(n)
    if n == 1:
        return False
    for i in range( 2, int(n**0.5)+1 ):
        if not n%i:
            return False
    return True

def circle():
    """ main function """
    num = int( input() )
    null = set()
    for i in range(1,num+1):
        if i in null:
            continue
        if not primer(i):
            continue
        temp, chck = set(), i
        temp.add(i)
        lenght = len( str(i) )
        for _ in range( lenght-1 ):
            chck = str(chck)[1:] + str(chck)[0]
            if not primer(chck):
                temp = []
                break
            temp.add(int(chck) if int(chck) <= num else 0)
        null = null | set(temp)
    print(sum(null))
circle()
