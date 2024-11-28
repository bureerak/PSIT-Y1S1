"""PongYa problem via iJudge during pair programming"""
def pongya():
    """
    Basic pongya game.

    Arguments:
    - num (int): Num to count

    Returns:
    - output (int/str): Word or num to say

    Raises:
       None.
    """
    num = int(input())
    if not num % 3 or str(num).endswith('3'):
        print('PONG')
    else:
        print(num)
pongya()
