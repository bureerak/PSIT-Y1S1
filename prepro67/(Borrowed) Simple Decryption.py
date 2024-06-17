"""Decryp Code"""
def decryp(a):
    """decrypt function"""
    if a in ('a', 'f', 'k', 'p', 'u','z'):
        a = 20
    if a in ('b', 'g', 'l', 'q', 'v'):
        a = 21
    if a in ('c', 'h', 'm', 'r', 'w'):
        a = 22
    if a in ('d', 'i', 'n', 's', 'x'):
        a = 23
    if a in ('e','j','o','t','y'):
        a = 24
    return a
def main():
    """main function"""
    alp1 = int(decryp(input()))
    alp2 = int(decryp(input()))
    alp3 = int(decryp(input()))
    alp4 = int(decryp(input()))
    alp5 = int(decryp(input()))
    print(alp1+alp2+alp3+alp4+alp5)
main()
