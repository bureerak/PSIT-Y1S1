"""Salon Promotion"""
def main():
    """main function"""
    times = int(input())
    if times<10:
        print("Not free")
    elif times%10 == 0:
        print("Free")
    else:
        print("Not free")
main()
