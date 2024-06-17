"""Beer Again?!"""
def main():
    """main function"""
    price = int(input())

    trade_cap = int(input())
    dc_piece = trade_cap/2

    discount = int(input())
    price_dc = price*(1-(discount/100))

    free_cap = int(input())
    money = int(input())
    cap = 0
    bottle = 0

    while money >= price or cap >= trade_cap and money >= price_dc:
        if not trade_cap:
            money-=price
            cap+=1
            bottle+=1
        elif cap >= trade_cap:
            cap -= trade_cap
            if money >= dc_piece*price_dc:
                money-=dc_piece*price_dc
                cap+=dc_piece
                cap+=free_cap
                bottle+=dc_piece
            else:
                while money >= price_dc:
                    money-=price_dc
                    cap+=1
                    bottle+=1
                break
        else:
            money-=price
            cap+=1
            bottle+=1
    print(int(bottle))
    print(f"{money:.2f}")
main()
