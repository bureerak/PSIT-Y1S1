""" Calculator V2 """
def main(number, tcount):
    """ main function """
    num_len = len(str(number))
    if number == 1:
        return 1
    if num_len == 1:
        return number*2
    for i in range(num_len - 1):
        tcount += (9 * 10**i) * (i + 2)
    tcount += (number - int('9' * (num_len - 1))) * ( num_len+1 )
    return tcount
print( main( int( input()) , 0) )
