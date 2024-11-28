""" Elo """
def elo_cal():
    """ return elo """
    ra = int(input())
    rb = int(input())
    req = input()
    ea = (1+(10**((rb-ra)/ 400))) ** -1
    print(f"{ea:.2f}" if req == "A" else f"{1-ea:.2f}")
elo_cal()
