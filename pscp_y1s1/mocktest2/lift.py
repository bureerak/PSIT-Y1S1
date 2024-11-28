""" lift """
def main():
    """ main function """
    per = int(input())
    lift = float(input())
    safe = False
    alwei = 0
    for _ in range(per):
        old = int(input())
        if old >= 12:
            safe = True
        alwei += float(input())
    alwei = bool(alwei<=lift)
    okbro = bool(safe or not per)
    print("Safe" if okbro and alwei else "Not Safe")
main()
