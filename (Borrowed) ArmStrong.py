"""Armstrong > Four Arm"""
def main():
    """main function"""
    num = input()
    posi = len(num)
    checker = 0
    for i in num:
        cal = int(i)**posi
        checker += cal
    if int(num) == checker:
        print(num,"is a ArmStrong number")
    else:
        print(num,"is not a ArmStrong number")
main()
