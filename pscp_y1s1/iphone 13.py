""" Iphone """
def main():
    """ main function """
    serial = input()
    storage = input().replace(" ","")
    if serial.find("iPhone 13") == -1:
        return print("Not Available")
    serial = serial.replace("iPhone 13","").strip().replace(" ","")
    check = 0
    if serial == "mini":
        check = (("128GB",25900),("256GB",29900),("512GB",37900))
    elif not serial:
        check = (("128GB",29900),("256GB",33900),("512GB",41900))
    elif serial == "Pro":
        check = (("128GB",38900),("256GB",42900),("512GB",50900),("1TB",58900))
    elif serial == "ProMax":
        check = (("128GB",42900),("256GB",46900),("512GB",54900),("1TB",62900))
    for i, j in check:
        if i == storage:
            value = j
            return print(value)
    return print("Not Available")
main()
