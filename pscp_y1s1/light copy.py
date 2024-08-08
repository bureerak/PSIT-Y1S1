""" Right """
def main(k = int(input()), n = int(input())):
    """main function"""
    for i in range(-(n//2),(n//2)+1):
        print(" " * (-(abs(i)) + (n//2)), end="")
        print("*"*k)
main()
