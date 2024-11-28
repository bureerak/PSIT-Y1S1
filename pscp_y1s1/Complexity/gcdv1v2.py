""" GCD_V1 """
def main(num1,num2):
    """ find GCD_Yeh-Yeh """
    most = max(num1, num2)
    least = min(num1, num2)
    gcd = least
    if not num1 or not num2:
        print(most)
        return
    while True:
        if not most%gcd and not least%gcd:
            print(gcd)
            return
        gcd -= max(most%gcd, least%gcd)
main(int(input()), int(input()))
