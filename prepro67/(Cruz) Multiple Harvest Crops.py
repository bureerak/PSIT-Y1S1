"""docstring"""
def main():
    """main function"""
    name = input()
    growtime = int(input())
    regrowth = int(input())
    price = int(input())
    amount = int(input())
    date = int(input())

    gain = 0
    count = 1
    havest_day = ""

    if date+growtime>28:
        print(f"The Season will end before you can harvest your {name}")
        print("Your income will be 0 G")
    else:
        date += growtime
        gain += amount*price
        havest_day += f" {date}"
        while date <= 28:
            if date + regrowth > 28:
                break
            count+=1
            date+=regrowth
            gain += amount*price
            havest_day += f" {date}"
        print(f"The {name} will be harvestable for {count} days in this Season")
        print(f"Harvestable days:{havest_day}")
        print(f"Your income will be {gain:,} G")
main()
