""" Fibonacci Recursive """
dp = {0: 0, 1: 1, 2: 1}
def rec_fib( num ):
    """ fibonacci recursive """
    if num in dp:
        return dp[num]
    dp[num] = rec_fib(num - 1) + rec_fib(num - 2)
    return dp[num]
def looper(num ,lim = 0):
    """ for loop by recursive """
    if lim < num:
        rec_fib(lim + 900)
        looper(num, lim+900)
    return rec_fib(num)
print( looper( int(input()) ) )
