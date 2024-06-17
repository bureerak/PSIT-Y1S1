"""slice"""
def main():
    """function"""
    text = input()
    text_a = text[::2]
    text_b = text[1::2]
    text = text_b+text_a
    print(text)
main()
