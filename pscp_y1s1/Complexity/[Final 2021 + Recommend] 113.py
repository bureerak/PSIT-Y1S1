""" 112 is real """
def main():
    """ main function """
    num = input()
    while '113' in num:
        num = num.replace('113','')
    print(num)
main()
