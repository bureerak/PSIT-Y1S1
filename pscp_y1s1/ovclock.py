""" second-converter """
def main(k_sec, s_min, m_hour ,h_day):
    """ main function """
    k_sec %= s_min*m_hour*h_day
    hh, k_sec = divmod(k_sec, s_min*m_hour)
    mm, k_sec = divmod(k_sec, s_min)
    print(hh,mm,k_sec,sep=":")
main(int(input()),int(input()),int(input()),int(input()))
