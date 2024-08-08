""" A """
def main(w1 = float(input()), w2 = float(input()), w3 = float(input())):
    """ B """
    if w1 < w2:
        w1, w2 = w2, w1
    if w2 < w3:
        w2, w3 = w3, w2
    if w1 < w2:
        w1, w2 = w2, w1
    a = abs(w1**2-(w2**2+w3**2))
    print("Yes" if w1**2==w2**2+w3**2 or 0 <= a < 0.01 else "No")
main()
