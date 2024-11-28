""" So """
def main():
    """ main function """
    password,code = input(), input()
    turns = 0
    for i in zip(password,code):
        diff = abs(ord(i[0])-ord(i[1]))
        turns += min(diff,26-diff)
    print(turns)
main()
