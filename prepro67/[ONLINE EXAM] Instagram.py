"""Docstring"""
def main():
    """main function"""
    fwer = int(input())
    foll = int(input())
    diff = abs(fwer - foll)
    if fwer == foll or diff <= 10:
        print("related")
    elif diff <= 100:
        print("almost related")
    elif diff > 100:
        print("not related")
main()
