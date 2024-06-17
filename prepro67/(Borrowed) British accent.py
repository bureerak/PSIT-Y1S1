"""Docstring"""
def main():
    """main function"""
    text = input()
    left = text[0]
    right = text[-1]
    text = text[1:-1].replace("t","")
    text = left+text+right
    print(text)
main()
