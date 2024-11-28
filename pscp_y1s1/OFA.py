""" One For All """
def holder():
    """ print OFA holder tree """
    num = int(input())
    per = [input() for _ in range(num)]
    for i in range(1,num+1):
        if i==num:
            print(f"{per[i-1]}_{i}",end="")
        elif i%2:
            print(f"{per[i-1]}{'*'*i}",end="")
        else:
            print(f"{per[i-1]}{'-'*i}",end="")
holder()
