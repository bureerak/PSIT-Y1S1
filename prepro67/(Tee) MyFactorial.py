"""Factorial Create by ME :)"""
def main():
    """main function"""
    num = int(input())
    minu = num
    ans = 1
    if num < 0:
        print("Error")
    else:
        for _ in range(num):
            ans *= minu
            minu -= 1
            if not minu:
                break
        print(ans)
main()
