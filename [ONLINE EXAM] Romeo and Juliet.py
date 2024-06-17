"""Docstring"""
def main():
    """main function"""
    hour = int(input())
    minute = int(input())
    if minute >= 15:
        minute-=15
        print(f"{hour:>02}:{minute:02}")
    else:
        minute = minute-15+60
        if not hour:
            hour = 24
        hour -= 1
        print(f"{hour:>02}:{minute:02}")
main()
