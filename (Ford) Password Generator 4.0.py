"""Docstring"""
def main():
    """mainfucntion"""
    text = input()
    text = text.lower()
    text = text[::-1]
    text = text.capitalize()
    count = len(text)

    ans = ""
    ans+=text+"2024"

    for _ in range(count-1):
        ans+="_"+text+"2024"

    for i in range(count):
        if text[i].isnumeric():
            print("Only use alphabetical password.")
            break
        if i == count-1:
            print(ans)
main()
