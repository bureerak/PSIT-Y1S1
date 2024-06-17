"""Docstring"""
def main():
    """main function"""
    gem = int(input())
    b_tier = 0
    y_tier = 0
    r_tier = 0
    while gem >= 1200 and r_tier < 10:
        row_1 = input()
        row_2 = input()
        b_tier += row_1.count("B")+row_2.count("B")
        y_tier += row_1.count("Y")+row_2.count("Y")
        r_tier += row_1.count("R")+row_2.count("R")
        gem-=1200

    print("---Result---")
    print(f"1 star : {b_tier}")
    print(f"2 stars: {y_tier}")
    print(f"3 stars: {r_tier}")
    if r_tier >= 10:
        print("Congratulations!")
    print(f"You have {gem} pyroxene.")
main()
