""" game """
def main():
    """ main fucntion """
    aside = int(input())
    bside = int(input())
    if aside%3 != bside%3:
        print("Error")
    else:
        print(aside%3)
main()
