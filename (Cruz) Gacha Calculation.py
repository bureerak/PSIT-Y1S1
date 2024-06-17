"""This is program Gacha Cal"""
def main():
    """function for jade calculate"""
    jade = int(input())
    roll = jade//120
    roll = int(roll)
    left = jade%120
    print(f"You can pull {roll} times.")
    print(f"You have {left} Pyroxene left.")
main()
