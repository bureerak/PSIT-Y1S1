""" ball week 4 """
def main():
    """ main function """
    meter  = float(input())
    count = 0
    while meter >= 0.01:
        count += 1
        meter *= 0.6
    print(count-1 if count else count)
main()
