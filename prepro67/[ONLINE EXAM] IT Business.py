"""Docstring"""
def main():
    """main function"""
    bank = float(input())
    money = float(input())
    status = ""
    count = 0
    while status != "end":
        if count == 3:
            status = "end"
            break
        status = input()
        if status[0] == "D":
            current = float(status[2:])
            if money >= current:
                money-=current
                bank+=current
                count=0
            else:
                count+=1
                continue
        elif status[0] == "W":
            current = float(status[2:])
            if bank >= current:
                bank-=current
                money+=current
                count=0
            else:
                count+=1
                continue
    print(f"{bank:.2f}")
    print(f"{money:.2f}")
main()
