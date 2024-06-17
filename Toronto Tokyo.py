"""I wonder if u know"""
def main():
    """Tokyo Toronto"""
    name = input()
    hour = int(input())
    minute = int(input())
    if name == "Toronto":
        hour = hour * 60
        minute = hour + minute
        minute += 780
        if minute > 1440:
            minute -= 1440
            hhh = minute // 60
            mmm = minute % 60
        elif minute < 1440:
            hhh = minute // 60
            mmm = minute % 60
        else:
            hhh = 0
            mmm = 0
        hhh = int(hhh)
        mmm = int(mmm)
        print(f"Now in Tokyo, it's {hhh:>02}:{mmm:>02}")
    elif name == "Tokyo":
        hour = hour * 60
        minute = hour + minute
        minute -= 780
        if minute < 0:
            minute = minute*-1
            minute = 1440-minute
        if minute > 1440:
            minute -= 1440
            hhh = minute // 60
            mmm = minute % 60
        elif minute < 1440:
            hhh = minute // 60
            mmm = minute % 60
        else:
            hhh = 0
            mmm = 0
        hhh = int(hhh)
        mmm = int(mmm)
        print(f"Now in Toronto, it's {hhh:>02}:{mmm:>02}")
    else:
        print("Error, Not Toronto or Tokyo.")
main()
