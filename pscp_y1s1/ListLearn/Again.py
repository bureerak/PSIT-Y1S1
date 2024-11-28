""" Again&Again """
def goin(vow):
    """ niaga """
    num = 0
    for i in vow:
        for j in ('a','e','i','o','u'):
            if i == j:
                num+=1
        if num>1:
            break
    return num

def aeiou():
    """ again """
    text = input().replace(".", "")
    text = text.split()
    ans = [x for x in text if goin(x) > 1]
    ans.sort()
    if ans:
        print(*ans,sep="\n", end="")
    else:
        print("Nope",end="")
aeiou()
