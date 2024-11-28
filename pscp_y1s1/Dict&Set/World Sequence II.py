""" World Sequence II """
def main(text1, text2):
    """ main function """
    high = max(len(text1), len(text2))
    for x in range(high+1):
        print(text2[:x] + text1[x:])
main(input(), input())
