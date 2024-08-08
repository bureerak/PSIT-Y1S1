""" A """
def main():
    """ B """
    year = int(input())
    if year % 4:
        print("No")
    elif year % 100:
        print("Yes")
    elif year % 400:
        print("No")
    else:
        print("Yes")
main()
