""" Run Length Decoding """
def main(code = input()):
    """ main function """
    for i in code:
        if i.isalpha():
            print(i * int(code[:code.find(i)]),end="")
            code=code[code.find(i)+1:]
main()
