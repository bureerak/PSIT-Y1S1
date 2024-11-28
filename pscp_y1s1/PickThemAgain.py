""" PickThemAgain """
def main():
    """ main function """
    null = [int(x) for x in input().split()]
    num = [x for x in null if not x % 3 or not x % 5]
    num.reverse()
    if num:
        print(*num,sep="\n")
    else:
        print("Nope")
main()
