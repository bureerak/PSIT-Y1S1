"""Docstring"""
def main():
    """main function"""
    water = int(input())
    box = int(input())

    count = 0
    num = 1
    diff = 0

    for _ in range((box*3)):
        if count == 3:
            diff += num
            count = 0
            num = 1
        num *= int(input())
        count += 1
    diff+=num
    if water <= diff:
        print("Happy")
    else:
        print("Unhappy")
main()
