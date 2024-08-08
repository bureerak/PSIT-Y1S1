""" Sequence XII """
def main(num = int( input() )):
    """ main function """
    for i in range(-num+1, num):
        for j in range(-num+1, num):
            if not i:
                print(f"{num - abs(j):>02}", end=" ")
            elif not j:
                print(f"{num - abs(i):>02}",end=" ")
            else:
                print(f"{num-abs(abs(i)-abs(j)):>02}", end=" ")
        print()
main()
