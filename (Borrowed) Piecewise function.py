"""Docstring"""
def main():
    """main function"""
    num = float(input())
    if num <= -1:
        num = num**2+1
    elif num >= 2:
        num = 5
    else:
        num = num+4
    print(f"{num:.2f}")
main()
