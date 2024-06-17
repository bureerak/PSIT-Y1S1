"""Stair program"""
def main():
    """main function"""
    stair = int(input())
    count = stair
    for i in range(stair):
        if not i:
            print("*"*count)
            count-=1
        else:
            print(" "*(i-1),"*"*count)
            count-=1
main()
