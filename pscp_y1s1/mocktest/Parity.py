""" Parity """
def main():
    """ main function """
    code = input()
    want = input()
    bit = 0
    for i in code:
        if i == "1":
            bit+=1
    if want == "Even":
        if not bit%2:
            code+="0"
        else:
            code+="1"
    else:
        if not bit%2:
            code+="1"
        else:
            code+="0"
    print(code)
main()
