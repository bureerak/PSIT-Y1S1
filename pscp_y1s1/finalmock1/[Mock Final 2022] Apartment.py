""" apartment """
def apart(a, b, c, d, e):
    """ main function """
    crit1 = round((b - c * d) / (2 * d))
    crit1 = crit1 if crit1 in range(0, (a - c) + 1) else 0
    lst = [0, crit1, a - c]
    ans = [[(b - d * x) * (c + x), x + c] for x in lst]
    temp = ans

    crit1,crit2 = (c * e - b) // (2 * e), ((c * e - b) // (2 * e)) +1
    crit1 = crit1 if crit1 in range(0, c + 1) else 0
    crit2 = crit2 if crit2 in range(0, c + 1) else 0
    lst = [0, crit1,crit2, c]
    ans = [[(b + e * x) * (c - x), c - x] for x in lst]
    temp += ans

    temp.sort(key=lambda x: ( -x[0], x[1] ))
    print(int(temp[0][0]), int(temp[0][1]), sep='\n')

apart(int(input()), int(input()), int(input()), int(input()), int(input()))
