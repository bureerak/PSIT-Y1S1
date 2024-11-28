""" Lotto """
def reward_chck():
    """ check prize """
    big_prize = input()
    parall1 = f"{((int(big_prize)+1)%1000000):>06}"
    parall2 = f"{((int(big_prize)-1)%1000000):>06}"
    last2digit = input()
    first3_1,first3_2 = input(),input()
    last3_1,last3_2 = input(),input()
    mylotto = input()
    reward = 0
    if mylotto == big_prize:
        reward+=6000000
    if mylotto in (parall1,parall2):
        reward+=100000
    if mylotto[4:] == last2digit:
        reward+=2000
    if mylotto[:3] == first3_1:
        reward+=4000
    if mylotto[:3] == first3_2:
        reward+=4000
    if mylotto[3:] in last3_1:
        reward+=4000
    if mylotto[3:] == last3_2:
        reward+=4000
    print(reward)
reward_chck()
