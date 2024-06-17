"""Stardew Marriage Condition"""
def main():
    """main function"""
    name = input()
    gold = int(input())
    weather = input()
    affection = int(input())
    house_tier = int(input())
    if weather != "rain":
        print("*Old Mariner is missing*")
    elif affection < 10:
        print(f"\"I've got this old amulet to sell... \
but somethin' tells me yer not ready for it, {name}.\"")
    elif house_tier < 2:
        print(f"\"I can see that sparkle in yer eye, {name}. \
Ye must be head over heels in love. But I'm afraid a bigger \
house is essential for a happy marriage.\"")
    elif gold < 5000:
        print("*Not enough money*")
    else:
        print("*You can buy the Mermaid's Pendant*")
main()
