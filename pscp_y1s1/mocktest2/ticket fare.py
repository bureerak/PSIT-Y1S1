""" Ticket fare """
def main( station, money = 0 ):
    """ main function """
    a_num = int(input())
    b_num = int(input())
    c_num = int(input())
    d_num = int(input())
    e_num = int(input())
    f_num = int(input())
    g_num = int(input())
    far = abs(f_num - g_num)
    if f_num in range(1, station + 1) and g_num in range(1, station + 1):
        if far < a_num:
            money += b_num
        elif far < a_num + c_num:
            money += b_num + abs(far - a_num) * d_num
        else:
            money += b_num + (c_num*d_num)
            money += abs(far - (a_num + c_num)) * e_num
    else:
        money = "Error"
    print(money)

main( int(input()) )
