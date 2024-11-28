""" Kaprekar """
def two_xort(num):
    """ Xort and Return High to Low/Low to High """
    x1,x2,x3,x4 = int(num[0]),int(num[1]),int(num[2]),int(num[3])
    for _ in range(3):
        if x1 < x2:
            x1,x2 = x2,x1
        if x2 < x3:
            x2,x3 = x3,x2
        if x3 < x4:
            x3,x4 = x4,x3
    num_htl = str(x1)+str(x2)+str(x3)+str(x4)
    num_lth = str(num_htl)[::-1]
    return int(num_htl)-int(num_lth)
def kaprekar_count():
    """ count until == 6174 """
    num = input()
    count=0
    while num != "6174":
        count+=1
        result = str(two_xort(num))
        if len(result)<4:
            result+="0"*(4-len(result))
        num = result
    print(count)
kaprekar_count()
