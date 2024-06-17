"""Docstring"""
def main():
    """main function"""
    text = input()
    check = text.find("Woof")
    if check == -1:
        print("Meow Meow Meow")
    else:
        print("Spy!!")
main()
