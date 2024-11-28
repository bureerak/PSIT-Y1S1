""" IT Business """
def atm(bank, inhand):
    """ atm like """
    error = 0
    while error < 3:
        press = input().replace(" ","")
        if press == "end":
            break
        if press[0]=="D" and float(press[1:]) <= inhand:
            bank, inhand, error = bank+float(press[1:]), inhand-float(press[1:]), 0
        elif press[0]=="W" and float(press[1:]) <= bank:
            bank, inhand, error = bank-float(press[1:]), inhand+float(press[1:]), 0
        else:
            error+=1
    print(f"{bank:.2f}",f"{inhand:.2f}",sep="\n")
atm(float(input()), float(input()))
