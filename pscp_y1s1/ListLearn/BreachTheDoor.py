""" BreachTheDoor """
def main():
    """ main function """
    text = input().split()
    fprint = ""
    for i in text:
        mini = ""
        for j in i:
            if j.isalpha():
                mini += j
        if len(mini)>6:
            fprint+=mini+" "
    print(fprint.strip())
main()
