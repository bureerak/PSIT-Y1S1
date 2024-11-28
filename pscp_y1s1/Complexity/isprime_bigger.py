""" is_prime """
def is_prime(num:int):
    """ Is Prime or Not """
    for i in range(2, int(num ** 0.5) + 1):
        if not num%i:
            return print("NO")
    return print("YES" if num not in (0,1) else "NO")
is_prime(int(input()))
