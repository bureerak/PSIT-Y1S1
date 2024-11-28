""" Us """
def main():
    """ main function """
    road = int(input())
    ans = ""
    lenght = len(str(road))
    if lenght in (1,2) and not road%5 and road:
        if str(road)[-1] == "0":
            ans+="Horizontal Major Interstate"
        if str(road)[-1] == "5":
            ans+="Vertical Major Interstate"
    elif lenght == 3 and not int(str(road)[1:])%5 and int(str(road)[1:]):
        if not int(str(road)[0])%2:
            ans+="Even Minor Interstate"
        else:
            ans+="Odd Minor Interstate"
    else:
        return print("Others")
    return print(ans,f"I-{int(str(road)[-2:])}",sep="\n")
main()
