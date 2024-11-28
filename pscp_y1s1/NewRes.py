""" Stamp """
def main(n_time,a_getevery,b_stamp,c_everystamp,d_dis):
    """ return balance """
    total, stamp = 0, 0
    for _ in range(n_time):
        price = int(input())
        if stamp >= c_everystamp:
            can_use = stamp//c_everystamp
            highest = int(price/d_dis)+1 if price/d_dis > int(price/d_dis) else int(price/d_dis)
            stamp -= min(can_use,highest)*c_everystamp
            price = max(0,price-(d_dis*min(can_use,highest)))
        stamp+=(price//a_getevery)*b_stamp
        total+=price
    print(total,"\n",stamp,sep="")
main(int(input()),int(input()),int(input()),int(input()),int(input()))
