""" Diamond """
def diamond():
    """ create diamond """
    num = int(input())
    for i in range(-(num//2),(num//2)+1):
        for j in range(num):
            if not i:
                print("*",end="")
            elif abs(i)==abs(j) or abs(i)+abs(j)==num-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
diamond()
