""" Coke V2 """
def lowprice():
    """ return cheapest price """
    a_price = int( input() )
    b_cap = int( input() )
    c_special = int( input() )
    d_need = int( input() )
    used = 0
    if not b_cap:
        return a_price * d_need
    promotion = d_need // b_cap
    promotion -= 1 if not d_need%b_cap and d_need//b_cap else 0
    d_need -= promotion
    used += (d_need * a_price) + (promotion * c_special)
    return used
print( lowprice() )
