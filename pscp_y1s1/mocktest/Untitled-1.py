"coke"
def main() :
    "main"
    normal_price = int(input())
    caps = int(input())
    new_price = int(input())
    want = int(input())
    if caps and want :
        promotion = want//caps
        total_dicount = new_price*promotion
        total_normal = normal_price*(want - promotion)
    else :
        print(want*normal_price)
        return

    payment = total_dicount + total_normal

    if not want % caps :
        payment += normal_price - new_price
    print(payment)
main()
