"""Docstring"""
def main():
    """main function"""
    count=0
    num = int(input())
    space = num*2 - 2
    for _ in range(num):
        print(" "*space,end="")
        space -= 2
        for i in range(1+(2*count)):
            if i == (2*count):
                print("*",end="")
                break
            print("* ",end="")
        print("")
        count+=1
main()
