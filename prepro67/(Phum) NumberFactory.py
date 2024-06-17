"""Docstring"""
def main():
    """main function"""
    num = input()
    num1 = int(num)
    power = 1
    before = 0
    for _ in (num):
        ans = int(num1 % 10**power) - before
        if not ans:
            before = int(num1 % 10**power)
            power += 1
            continue
        print(ans)
        before = int(num1 % 10**power)
        power += 1
main()
