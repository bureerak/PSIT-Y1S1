""" coke """
def main():
    """ main function """
    a_price = int(input())
    b_cap = int(input())
    c_newp = int(input())
    d_want = int(input())
    total = 0
    fst_set = b_cap + 1
    fst_price = (b_cap*a_price) + c_newp
    if not b_cap:
        return print(a_price*d_want)
    if fst_set <= d_want:
        d_want-=fst_set
        total+=fst_price
        fst_set-=1
        fst_price-=a_price
    needset = d_want//fst_set
    d_want-=needset*fst_set
    total+=needset*fst_price
    return print(total+(d_want*a_price))
main()
