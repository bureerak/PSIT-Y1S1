""" Grader """
def scorer(sc):
    """ grade by score """
    if 95 <= sc <= 100:
        sc = 4
    elif 90 <= sc < 95:
        sc = 3.5
    elif 85 <= sc < 90:
        sc = 3
    elif 80 <= sc < 85:
        sc = 2.5
    elif 75 <= sc < 80:
        sc = 2
    elif 70 <= sc < 75:
        sc = 1.5
    elif 65 <= sc < 70:
        sc = 1
    elif 60 <= sc < 65:
        sc = 0.5
    elif 0 <= sc < 60:
        sc = 0
    return sc
def main(clss = int( input() ), al = 0):
    """ main function """
    for _ in range(clss):
        al += scorer(float(input())) * 4
    print(f"{float(str(al/(4*clss))[:4]):.2f}")
main()
