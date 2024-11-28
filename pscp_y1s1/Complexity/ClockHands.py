""" ClockHands """
def main(hour:int, minute:int):
    """ main function """
    hour = (hour*30) + (minute/2)
    minute = minute * 6
    bet = min(abs(hour - minute),360 - abs(hour - minute))
    print('True' if bet < 6 or hour > minute else 'False')
main(int(input()), int(input()))
