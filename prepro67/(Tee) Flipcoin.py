"""Docstring"""
def main():
    """main function"""
    heigh = 0
    coin = ""
    count = 0
    while coin != "Stop":
        if coin == "H":
            count += 1
            if count > heigh:
                heigh = count
        else:
            count = 0
        coin = input()
    print(heigh)
main()
