""" Netflix """
def efficient():
    """return best price by criteria."""
    num, tick, finish = max( int( input() ), int( input() ) ), 0, False
    for i in range(1,6):
        tick = i if input() == "Yes" else tick
    for i, j, k, l in ( (2, 99, 1, "Mobile"), (3, 279, 1, "Basic"),
                       (4, 349, 2, "Standard"), (5, 419, 4, "Premium") ):
        if tick <= i and j == 99:
            print( f"Mobile x { num }\nTotal = { 99 * num } THB" )
            finish = True
            break
        temp_out, pro419, pro = 419 * ( num // 4 ), num // 4, None
        if not num % 4:
            break
        if (num % 4 > 2 or k == 4) and j != 99 and tick <= i:
            temp_out += 419
            pro419 += 1
            break
        if k >= num % 4 and j != 99 and tick <= i:
            temp_out, pro = temp_out + j, l
            break
    if not finish:
        print(f"Premium x { pro419 }\n" if pro419 else "", end="")
        print(f"{ pro } x 1\n" if pro else "", end="")
        print("Total =",temp_out,"THB",end="")
efficient()
