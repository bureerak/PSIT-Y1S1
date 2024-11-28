""" All_Primes """
def main( num:int ):
    """ main function """
    null = []
    for i in range(1,num+1):
        if i == 1:
            continue
        null.append(i)
        for j in range(2, int(i**0.5)+1 ):
            if not i%j:
                null.pop()
                break
    print(len(null))
main( int( input() ) )
