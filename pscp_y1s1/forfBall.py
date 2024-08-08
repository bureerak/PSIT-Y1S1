""" Forf Ball """
def main(code = input()):
    """ main function """
    x = 1
    y = 0
    z = 0
    for i in code:
        if i == "A":
            x, y = y, x
        if i == "B":
            y, z = z, y
        if i == "C":
            x,z = z,x
    if x == 1:
        print(1)
    if y == 1:
        print(2)
    if z == 1:
        print(3)
main()
