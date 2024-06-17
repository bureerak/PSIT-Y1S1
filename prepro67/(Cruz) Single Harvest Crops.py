"""Grow time Calculate"""
def main():
    """main function"""
    name = input()
    time = int(input())
    price = int(input())
    amount = int(input())
    date = int(input())
    if time+date <= 28:
        print(f"The {name} will be harvestable on day \
{time+date} of the Season")
        print(f"Your income will be {amount*price:,} G")
    else:
        print(f"The Season will end before you \
can harvest your {name}")
        print("Your income will be 0 G")
main()
