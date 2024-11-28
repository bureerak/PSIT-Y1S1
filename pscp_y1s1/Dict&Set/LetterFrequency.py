""" LetterFrequency """
def main():
    """ main function """
    text = input().replace(' ','')
    null = {}
    for i in text:
        null[i] = null.get(i,0) + 1
    print((sorted(null.items(),key=lambda x:x[1],reverse=True))[0][0])
main()
