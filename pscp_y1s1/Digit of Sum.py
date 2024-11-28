""" Sum of Digit """
def find_sod(n):
    """ sum of digit finder """
    return n if int(n)<=9 else find_sod(sum([int(i) for i in str(n)]))
def main(n):
    """Input until 0"""
    while int(n):
        print(find_sod(n))
        n = input()
main(input())
