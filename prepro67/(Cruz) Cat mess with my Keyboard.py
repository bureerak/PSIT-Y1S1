"""Docstring"""
def main():
    """main function"""
    text = input()
    real = ""
    for i in text:
        if i.isnumeric():
            real+=""
        else:
            real+=i
    print(real)
main()
