""" Harshad """
def is_harshad():
    """ Harshad Check input*10 """
    num = [abs(int(input())) for _ in range(10)]
    for i in num:
        if not int(i):
            print("No")
        elif not int(i)%int(digit_of_sum(i)):
            print("Yes")
        else:
            print("No")
def digit_of_sum(n):
    """ find digit of sum """
    carry = 0
    for i in str(n):
        carry += int(i)
    return carry
is_harshad()
