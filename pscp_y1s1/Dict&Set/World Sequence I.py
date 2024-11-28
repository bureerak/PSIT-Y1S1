""" WordSequence I """
def main():
    """ main function """
    text = input()
    for i, _ in enumerate(text):
        print(text[:i+1])
main()
