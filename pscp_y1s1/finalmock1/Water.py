""" Water """
def waterfee():
    """ n : month , a : nm rate , b : limit , c : af rate , d : free rate """
    month = int( input() )
    a_nmrate = float( input() )
    b_limit = float( input() )
    c_aflim = float( input() )
    d_free = float( input() )
    per_month = [float(input()) for _ in range(month)]
    null = [0]*month
    for i in range(month):
        null[i] += min(per_month[i], b_limit) * a_nmrate
        null[i] += (per_month[i] - b_limit)*c_aflim if per_month[i] - b_limit > 0 else 0
        if null[i] <= d_free:
            null[i] = 0
    print(f'{sum(null):.2f}')
waterfee()
