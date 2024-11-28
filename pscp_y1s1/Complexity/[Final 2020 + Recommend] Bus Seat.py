""" After Final Go Khonkaen """
def main(col, row, seat):
    """ main function """
    bus = [[f"{x+y*col:>02}" if x+y*col!=seat else "XX" for x in range(1,col+1)]\
        for y in range(row)]
    bus = list(zip(*bus))
    for i in range(col)[::-1]:
        print(*bus[i])
        if not i%2 and i:
            print()
main(int(input()), int(input()), int(input()))
