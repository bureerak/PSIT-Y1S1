""" Donut """
def main():
    """ main function """
    price = int(input())
    piece = int(input())
    free = int(input())
    demand = int(input())

    in_box = free + piece
    have_box = demand // in_box
    need_more = demand - (have_box * in_box)

    no_pro = 0
    expiece = 0

    if need_more >= piece:
        have_box += 1
    else:
        no_pro = need_more * price
        expiece = need_more

    print( (have_box * price * piece) + no_pro, (have_box * in_box) + expiece )
main()
