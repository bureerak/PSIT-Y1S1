""" sqFree """
def main():
    """ return square free """
    num = int( input() )
    counter = num
    if num <= 3:
        return num
    for i in range( 4, num+1 ):
        for j in range( 2, int(num**0.5) + 1 ):
            if not i % j**2:
                counter-=1
                break
    return counter
print( main() )
