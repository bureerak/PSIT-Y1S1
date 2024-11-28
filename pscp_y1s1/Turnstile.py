""" turnstile """
def turnpass():
    """ count turnstile pass """
    state = False
    count = 0
    com = input()
    while com != "END":
        if com == "C":
            state = True
        if com == "P" and state:
            count+=1
            state=False
        com = input()
    print(count)
turnpass()
