""" Tax """
def tax_function(money, l_con, percen,tax):
    """ tax calculate """
    if money > l_con:
        tax += (money - l_con) * (percen/100)
        money = l_con
    return tax ,money
def main( money = int(input()) ):
    """ main fuction """
    tax = 0
    tax,money = tax_function(money, 4000000, 35, tax)
    tax,money = tax_function(money, 2000000, 30, tax)
    tax,money = tax_function(money, 1000000, 25, tax)
    tax,money = tax_function(money, 750000, 20, tax)
    tax,money = tax_function(money, 500000, 15, tax)
    tax,money = tax_function(money, 300000, 10, tax)
    tax,money = tax_function(money, 150000, 5, tax)
    print(int(tax))
main()
