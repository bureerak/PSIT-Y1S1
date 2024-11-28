""" ISBN """
def main(num):
    """ main function """
    temp = num.replace('-','')
    chck = num.split('-')[-1]
    multi = list(map(lambda a,b: a*int(b), range(10,1,-1), list(temp[:-1])))
    lebel = -sum(multi) % 11
    lebel = 'X' if lebel == 10 else lebel
    if str(lebel) == chck:
        print('Yes')
        return
    print('No',lebel)
main( input() )
