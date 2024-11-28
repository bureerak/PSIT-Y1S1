""" homerun """
def main():
    """ main """
    sanam = int(input())
    dist = float(input())
    homerun = 0
    for _ in range(sanam):
        num = float(input())
        if dist > num:
            homerun+=1
    print(homerun)
main()
