""" Easy Histogram No Dict """
def histogram(text = input()):
    """ histogram and sort aA-zZ """
    res = {}
    for i in text:
        if i != " ":
            res[i] = res.get(i,0) + 1
    res = sorted(res.items(),key=lambda x : x[0].lower() + x[0] if x[0].isupper() else x[0])
    for i in res:
        print(*i,sep=" = ")
histogram()
