""" GCD_N """
import math
def main(num):
    """ main function """
    info = [int(input()) for _ in range(num)]
    print(math.gcd(*info))
main( int(input()) )
