""" Tuple's Sad life """
def csquare():
    """ cs """
    text = input().split()
    fff = input()
    for _ in range(text.count(fff)):
        print((f"{text.index(fff)} "*text.count(fff)).strip())
csquare()
