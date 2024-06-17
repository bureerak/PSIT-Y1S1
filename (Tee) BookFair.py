"""BookDiscount by WhileLoop"""
def main():
    """main function"""
    inprice = 1
    total = 0
    while inprice != -1:
        inprice = int(input())
        if inprice != -1:
            total += inprice
    if total >= 1500:
        dc(20,total)
    elif total >= 1000:
        dc(10,total)
    elif total >= 750:
        dc(5,total)
    else:
        print(f"Total price {total:.2f} baht.")

def dc(x,y):
    """Discount Function"""
    print(f"You got discount {x}%")
    print(f"Total price after discount {y*(1-(x/100)):.2f} baht.")
main()
