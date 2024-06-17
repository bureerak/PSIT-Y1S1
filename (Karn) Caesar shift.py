"""Ceasar Im sry"""
def main():
    """main function"""
    a_1 = ord(input())
    a_2 = ord(input())
    a_3 = ord(input())
    a_4 = ord(input())
    direction = input()
    if direction == "RIGHT":
        a_1 += abs(a_1%10-a_1//10 ) * 2
        a_2 += abs(a_2%10-a_2//10 ) * 2
        a_3 += abs(a_3%10-a_3//10 ) * 2
        a_4 += abs(a_4%10-a_4//10 ) * 2
        a_1 = cal_r(a_1)
        a_2 = cal_r(a_2)
        a_3 = cal_r(a_3)
        a_4 = cal_r(a_4)
        print(chr(a_4),chr(a_3),chr(a_2),chr(a_1),sep="-")
    elif direction == "LEFT":
        a_1 -= abs(a_1%10-a_1//10 ) * 2
        a_2 -= abs(a_2%10-a_2//10 ) * 2
        a_3 -= abs(a_3%10-a_3//10 ) * 2
        a_4 -= abs(a_4%10-a_4//10 ) * 2
        a_1 = cal_l(a_1)
        a_2 = cal_l(a_2)
        a_3 = cal_l(a_3)
        a_4 = cal_l(a_4)
        print(chr(a_4),chr(a_3),chr(a_2),chr(a_1),sep="-")
def cal_l(x):
    """LEFT cal function"""
    if x < 65:
        x = x+26
    return x
def cal_r(x):
    """RIGHT cal function"""
    if x > 90:
        x = x-26
    return x
main()
