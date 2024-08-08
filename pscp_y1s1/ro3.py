""" Rule of three """
def main():
    """ main function """
    num = int(input())
    x = 0
    efprice = 0
    efvalue = 0
    for _ in range(num):
        price = float(input())
        value = float(input())
        initial = value/price
        if initial > x or (initial == x and price < efprice):
            efprice = price
            efvalue = value
            x = initial
    print(f"{efprice:.2f}",f"{efvalue:.2f}")
main()
