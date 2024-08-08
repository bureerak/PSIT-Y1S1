""" SequenceXI """
def main(x = int( input() )):
    """ main function """
    for i in range(1, x+1):
        space = ""
        for j in range(1, (x*2)):
            if j < i:
                space += f"{j:>02d} "
            elif j >= ((x*2)-i):
                space += f"{(x*2)-j:>02} "
            else:
                space += f"{i:>02d} "
        print(space.strip(),end="")
        print()
    for i in range(x-1, 0, -1):
        space = ""
        for j in range(1, (x*2)):
            if j < i:
                space += f"{j:>02d} "
            elif j >= ((x*2)-i):
                space += f"{(x*2)-j:>02} "
            else:
                space += f"{i:>02d} "
        print(space.strip(),end="")
        print()
main()
