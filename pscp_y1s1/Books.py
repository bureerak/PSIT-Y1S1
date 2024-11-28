""" Books """
import math
def day_read():
    """ return day to read """
    book,page = int(input()),int(input())
    x = int(input())
    y = int(input())
    total,day = 0,0
    while book:
        z = math.ceil((page*x)/y)
        total+=z
        if z>=page:
            break
        if total>=page:
            total=0
            book-=1
        day+=1
        x+=1
        y+=1
    print(day+book)
day_read()
