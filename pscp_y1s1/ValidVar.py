""" ValidVar """
def main():
    """ main function """
    num = int(input())
    box = [input() for _ in range(num)]
    for i in box:
        if i.isidentifier() and i not in ("if","else","elif","while","for",
"True","False","continue","break","return","is","in","and","or","from","as",
"pass","not","def","None"):
            print("Valid")
        else:
            print("Invalid")
main()
