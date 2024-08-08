""" Largest Number """
def main(a = input(),b = input(),c = input()):
    """ main function """
    x = a
    y = b
    z = c
    a = int(a) * (10**( ( (len(a)-1) * -1 ) ))
    b = int(b) * (10**( ( (len(b)-1) * -1 ) ))
    c = int(c) * (10**( ( (len(c)-1) * -1 ) ))

    if len(x)==1:
        a+=0.9
    if len(y)==1:
        b+=0.9
    if len(z)==1:
        c+=0.9

    if a < b :
        a, b = b, a
        x, y = y, x
    if b < c:
        b, c = c, b
        y, z = z, y
    if a < b:
        a, b = b, a
        x, y = y, x
    print(x + y + z)
main()
