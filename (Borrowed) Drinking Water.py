"""Water"""
def main():
    """main function"""
    price = int(input())
    promo = int(input())
    price_pro = int(input())
    bottle = int(input())
    money = 0
    count = 0
    cap = 0

    while count < bottle:
        count+=1
        if not promo:
            money += price
        elif cap == promo:
            cap = 0
            money+=price_pro
        else:
            money += price
        cap+=1
    print(money)
main()
