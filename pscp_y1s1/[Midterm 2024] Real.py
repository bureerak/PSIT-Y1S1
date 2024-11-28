""" Real or Fake """
def main():
    """ main function """

    manual = (
        ("1111110","0"),("0110000","1"),("1101101","2"),("1111001","3"),
        ("0110011","4"),("1011011","5"),("1011111","6"),("1110000","7"),
        ("1111111","8"),("1111011","9")
        )
    checker = (
        "1111110","0110000","1101101","1111001","0110011","1011011","1011111",
        "1110000","1111111","1111011"
               )
    num = ""
    eor = False

    for _ in range(3):
        comms = ""

        for _ in range(8):
            code = input()
            if code == "on":
                comms+="1"
            else:
                comms+="0"

        if comms[:-1] not in checker:
            eor = True

        for i,j in manual:
            if comms[:-1] == i:
                num+=j
        if comms[-1] == "1":
            num+="."

    if eor or num.count(".")>1:
        print("Error")
    else:
        print(f"{float(num):.2f}")
main()
