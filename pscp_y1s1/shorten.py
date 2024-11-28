""" Shorten """
def minimize():
    """ return minimize number """
    num = int(input())
    carry,first=num,num
    ans=""
    if num != -1:
        while num != -1:
            if num!=carry and num-carry==1:
                carry=num
            elif num!=carry and num-carry>1:
                if first==carry:
                    ans+=f"{first}, "
                else:
                    ans+=f"{first}-{carry}, "
                carry,first = num,num
            num=int(input())
        print(ans,end="")
        print(f"{first}" if first==carry else f"{first}-{carry}")
minimize()
