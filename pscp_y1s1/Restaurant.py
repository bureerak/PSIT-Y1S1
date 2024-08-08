""" Restaurant """
def main():
    """ main function """
    a_price = float( input() )
    b_pro = float( input() )
    c_discount = float( input() )
    d_recommend = float( input() )
    after_order = a_price + d_recommend

    if after_order >= b_pro:
        after_order *= 1 - ( c_discount/100 )
    if a_price >= b_pro:
        a_price *= 1 - ( c_discount/100 )

    if after_order - a_price <= 0:
        print("Yes",end="")
    else:
        print("No",end="")

    if after_order - a_price:
        print(f" {abs(after_order - a_price):.3f}")
main()
