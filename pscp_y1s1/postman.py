"""Post Office"""
def main():
    """ main function """
    n_envelop = int(input())
    m_pack = int(input())
    res = (n_envelop*13) + (m_pack*15)
    for _ in range(n_envelop):
        number = float(input())
        if 0 <= number <= 10:
            res+=16
        elif 10 < number <= 20:
            res+=18
        elif 20 < number <= 100:
            res+=23
        elif 100 < number <= 250:
            res+=28
        elif 250 < number <= 500:
            res+=33
        elif 500 < number <= 1000:
            res+=48
        elif 1000 < number <= 2000:
            res+=68

    for _ in range(m_pack):
        mumber = float(input())
        if 0 <= mumber <= 500:
            res+=45
        elif 500 < mumber <= 1000:
            res+=55
        elif 1000 < mumber <= 2000:
            res+=70
    print(res)
main()
