""" MissingNumber """
def missme():
    """ miss """
    num = int(input())
    null = set(x for x in range(1,num+1))
    noll = set()
    while True:
        temp_in = int(input())
        if not temp_in:
            break
        noll.add(temp_in)
    print(*sorted(null - noll),sep="\n")
missme()
