"""Final 2019 + Recommend] Pro"""
def main():
    """ main function """
    x = int( input() )
    y = int( input() )
    a = int( input() )
    z = int( input() )
    pro_get = z//x
    free_head = x-y
    low = free_head * pro_get
    z -= low
    print( z * a )
main()
