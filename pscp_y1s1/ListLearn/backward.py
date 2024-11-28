""" BackWard """
def main():
    """ main function """
    null = []
    while True:
        x = input()
        if x == "NULL":
            break
        null.append(x)
    print(*reversed(null),sep="\n",end="")
main()
