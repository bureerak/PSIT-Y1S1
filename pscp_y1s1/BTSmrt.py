""" BTS/MRT """
def is_free():
    """ Check whether it free or not """
    day = input()
    old = float(input())
    height = float(input())
    if old < 14 and height < 90 or (old>=60 and day == "Senior Day"):
        print("FREE")
    elif old < 14 and height <= 140 and day == "Children Day":
        print("FREE")
    else:
        print("PAY")
is_free()
