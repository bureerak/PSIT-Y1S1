"""Nijika"""
def main():
    """main function"""
    num = int(input())
    num = num % 2
    num = bool(num)
    print("Odd"*num or "Even")
main()
