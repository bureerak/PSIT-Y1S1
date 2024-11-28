""" Diginity """
def decode(num):
    """ decode num """
    lenght = len(str(num))
    while num:
        while lenght != 1:
            carry = 0
            for i in str(num):
                carry+=int(i)
            num=carry
            lenght=len(str(num))
        print(num)
        decode(int(input()))
        break
decode(int(input()))
