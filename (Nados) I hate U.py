"""Docstring"""
def main():
    """main function"""
    text = input()
    num = len(text)
    ans = ""
    for i in range(num):
        if text[i] == "U" or text[i] == "u":
            ans += f"{i}"
        else:
            ans += text[i]
    print(ans)
main()
