""" Sequence XXX """
def main(num = int(input()),time = int(input())):
    """ main function """
    for i in range(num):
        for _ in range(time):
            for j in range(num):
                if i in (0,num-1) or j in (0,num-1) or i == j or i+j == num-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print(" ",end="")
        print()
main()
