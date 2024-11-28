""" Optimize Code Practice """
def findfact( num: int, su = 0 ):
    """ Find sum of proper divisors of num """
    for i in range(1, int(num**0.5) + 1):
        if not num % i:
            su += i
            su += num//i if i > 1 else 0
    return su
def main( n:int , ans = 0):
    """ return amicable sum """
    for i in range( 1, n+1 ):
        am_pair = findfact(i)
        if i < am_pair <= n:
            check = findfact(am_pair)
            if check == i:
                ans += am_pair + i
    return ans
print( main( int(input() )) )
