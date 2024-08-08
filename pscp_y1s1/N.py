""" N-word building """
def main():
    """ main function """
    num = int(input())
    for i in range(1, num+1):
        for j in range(1, num+1):
            if j in (1,num):
                print("*",end="")
            elif i == j:
                print("*",end="")
            else:
                print(" ",end="")
        print()
main()
