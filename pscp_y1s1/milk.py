""" Milk week 4 """
def main():
    """ main function """

    a_price = int( input() )
    b_pro = int( input() )
    c_extra = int( input() )
    d_money = int( input() )

    milk_get = d_money//a_price
    milk_cap = milk_get

    if b_pro:
        while milk_cap//b_pro:
            milk_new = (milk_cap//b_pro) * c_extra
            milk_get += milk_new
            milk_cap = milk_cap%b_pro + milk_new
    print(milk_get)
main()
