"""Docstring 11"""
def main():
    """main function"""
    text = input().upper()
    encod = ""
    lenght = len(text)
    for i in range(lenght):
        if not i and text[i].isalpha():
            encod += text[i]
        elif text[i] not in encod and text[i].isalpha():
            if encod:
                encod+=" "+text[i]
            else:
                encod+=text[i]
    print(encod)
main()
