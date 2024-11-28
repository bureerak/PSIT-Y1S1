""" is_prime """
def is_prime(num:int) -> str:
    """ Is Prime or Not """
    for i in range(2,num):
        if not num%i:
            return print("No")
    return print("Yes" if num not in (0,1) else "No")
is_prime(int(input()))
