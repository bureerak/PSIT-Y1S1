""" Align """
def main():
    """ main fucntion """
    space = int(input())
    command = input()
    text = input()
    if command == "left":
        print(text," "*(space-len(text)),sep="")
    elif command == "right":
        print(" "*(space-len(text)),text,sep="")
    elif command == "center":
        x,y = divmod(space-len(text),2)
        print(" "*(x+y),text," "*x,sep="")
main()
