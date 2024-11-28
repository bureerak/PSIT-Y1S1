""" MissingNumber No Set """
def mnns():
    """ M """
    num = int(input())
    null = {f'{x}':x for x in range(1,num+1)}
    while True:
        temp_in = input()
        if temp_in == '0':
            break
        null.pop(temp_in)
    print(*(null.keys()),sep="\n")
mnns()
