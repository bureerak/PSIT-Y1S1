""" 888 """
def main():
    """ main function """
    money = int(input())
    member = int(input())
    while 8*member > money:
        member-=1
    eight = 8*member
    if money-eight==4:
        member-=1
    print( "-1" if not member else member )
main()
