""" A """
def main():
    """ B """
    allv = float(input())
    highv = float(input())
    comp = highv
    twov = allv-highv
    if twov - highv < 0:
        x = abs(twov-highv)
        highv -= x
        twov -= highv
    else:
        twov-=highv
    print("Surprising" if abs(twov - comp) > 2 else "Not surprising")
main()
