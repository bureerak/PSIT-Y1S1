"""Program for John"""
def main():
    """main function"""
    name = input()
    direct = input()
    if direct == "Left":
        print("-"*(len(name)+2))
        print("#",name,"|",sep="")
        print("-"*(len(name)+2))
    elif direct == "Right":
        print("-"*(len(name)+2))
        print("|",name,"#",sep="")
        print("-"*(len(name)+2))
    elif direct == "Both":
        print("-"*(len(name)+2))
        print("#",name,"#",sep="")
        print("-"*(len(name)+2))
    elif direct == "None":
        print("-"*(len(name)+2))
        print("|",name,"|",sep="")
        print("-"*(len(name)+2))
main()
