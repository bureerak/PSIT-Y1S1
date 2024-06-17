"""Docstring"""
def lflow1(x,name=""):
    """flower list 1"""
    if x in ("A","a"):
        x=125
        name="Azalea"
    elif x in ("C","c"):
        x=200
        name="Camellia"
    elif x in ("D","d"):
        x=50
        name="Daisy"
    elif x in ("E","e"):
        x=230
        name="Everlasting"
    elif x in ("H","h"):
        x=400
        name="Hazel"
    elif x in ("I","i"):
        x=85
        name="Ivy"
    elif x in ("K","k"):
        x=50
        name="Kosumosu"
    return x,name

def lflow2(x,name=""):
    """flower list 2"""
    if x in ("L","l"):
        x=45
        name="Lily"
    elif x in ("M","m"):
        x=110
        name="Marigold"
    elif x in ("P","p"):
        x=65
        name="Parsley"
    elif x in ("R","r"):
        x=90
        name="Rosemary"
    elif x in ("S","s"):
        x=340
        name="Sage"
    elif x in ("T","t"):
        x=235
        name="Thyme"
    elif x in ("V","v"):
        x=500
        name="Violet"
    return x,name

def main():
    """ok"""
    order = input()
    lenght = len(order)
    flower1 = "AaCcDdEeHhIiKk"
    flower2 = "LlMmPpRrSsTtVv"
    total = 0
    name = ""
    dont = ""

    for i in range(lenght):
        if order[i] in flower1:
            total += lflow1(order[i])[0]
            name += f" {lflow1(order[i])[1]}"
        elif order[i] in flower2:
            total += lflow2(order[i])[0]
            name += f" {lflow2(order[i])[1]}"
        else:
            for j in range(lenght):
                order = order.upper()
                if order[j] not in flower1 and order[j] not in flower2 and order[j] not in dont:
                    dont += f" {order[j]}"
            print("Sorry, We don't have the flower you want.")
            print(f"Flowers in your orders that we don't have:{dont}")
            break
        if i == lenght-1:
            print(f"Your orders:{name}")
            print(f"Totals: {total:,} baht")
main()
