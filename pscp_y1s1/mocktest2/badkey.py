""" bad keyboard """
def main():
    """ main function """
    text = input()
    ans = ""
    for i in text:
        if i == "i":
            ans+="o"
        elif i == "o":
            ans+="i"
        elif i == "I":
            ans+="O"
        elif i == "O":
            ans+="I"
        else:
            ans+=i
    print(ans)
main()
