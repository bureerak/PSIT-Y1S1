"""Duck x Bunny"""
def main():
    """main function docstring"""
    number = int(input())
    legs = int(input())
    bunny = (legs-(2*number)) / 2
    duck = (legs-(4*bunny)) / 2
    checker = (legs-(2*number)) % 2
    if bunny < 0 or duck < 0:
        print("ERROR")
    elif checker:
        print("ERROR")
    elif bunny + duck == number:
        bunny = int(bunny)
        duck = int(duck)
        print(bunny)
        print(duck)
    else:
        print("ERROR")
main()
