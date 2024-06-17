"""Docstring"""
def main():
    """sdaf"""
    text = input()
    first = text[0].upper()
    last = text[1:]
    text = first+last
    if text[-1] == "." or text[-1] == "?":
        print(text)
    else:
        print(text + ".")
main()
