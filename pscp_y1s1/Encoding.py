""" Encoding """
def main():
    """ main function """
    code = input()
    curr = ""
    count = ""
    for i in code:
        if i != curr:
            print(str(count)+curr,end="")
            curr = i
            count = 1
        else:
            count+=1
    print(str(count)+curr,end="")
main()
