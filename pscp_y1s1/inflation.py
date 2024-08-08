""" Inflation Week 4 """
def main():
    """ main function """
    n_money = int(float( input() ) * 100)
    k_year = int(input())
    for _ in range(k_year):
        n_money += int(n_money*381 // 10000)
    print(f"{n_money//100}.{n_money%100:>02}")
main()
