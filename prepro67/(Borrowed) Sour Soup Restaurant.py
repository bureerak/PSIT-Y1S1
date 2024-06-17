"""Docstring"""
def main():
    """main function"""
    menu = ""
    price = 0
    count = 0
    while menu != "stop":
        menu = input()
        if menu == "shrimp sour soup":
            price += 80
        if menu == "mixed vegetables sour soup":
            price += 60
        if menu == "papaya sour soup":
            price += 55
        if menu in ("snapper fish sour soup","cha om shrimp sour soup"):
            price += 100
        count+=1
    if count >= 3 and price > 200:
        print(f"Original Price {price} baht")
        print(f"Discount {int(price*(15/100))} baht")
        print(f"Total {price-int((price*(15/100)))} baht")
    else:
        print(f"Original Price {price} baht")
        print("Discount 0 baht")
        print(f"Total {price} baht")
main()
