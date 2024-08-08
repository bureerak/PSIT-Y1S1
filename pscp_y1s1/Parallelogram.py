""" Parallelogram """
def main():
    """ main function """
    text = input()
    lenght = len(text)
    for i in range(1,lenght+1):
        print(" "*(lenght - i),text[0:i],sep="")
    for i in range(1,lenght):
        print(text[i:],sep="")
main()
