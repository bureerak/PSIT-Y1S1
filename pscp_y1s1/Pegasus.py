""" Saint Seiya """
def combat():
    """ Hello """
    sec = int(input())
    punch = int(input())

    result = 0
    send_out = 0
    for i in range(2,sec+1,2):
        if result>=punch:
            send_out = i-1
            break
        if not i%6:
            result+=1
        else:
            result+=165
    result += (sec - send_out)*12 if send_out else 0
    print(result)
combat()
