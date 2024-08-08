""" Virus """
def main(virus = input(),sc = 0):
    """ main function """
    for i in virus:
        if i == "o":
            sc+=1
    print(sc)
main()
