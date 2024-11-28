""" lay """
def testo():
    """ pringle """
    x1 = input()
    x2 = input()
    x3 = input()
    finger = int(input())
    reach = 0
    reach = x2.count(")",0,finger)
    x2 = x2.replace(")"," ",reach)
    print(reach)
    print("None." if not x2.count(")") else "There are still some left.")
    print(x1,x2,x3,sep="\n")
testo()
