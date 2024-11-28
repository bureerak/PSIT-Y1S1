""" Bfully Pair """
def pair(text):
    """ is fully pair or not """
    tofind, ans = "",""
    for i in text:
        tofind += i if i not in tofind else ""
    for i in tofind:
        if text.count(i)%2:
            ans+=i
    print(ans if ans else "fully paired")
pair(input())
