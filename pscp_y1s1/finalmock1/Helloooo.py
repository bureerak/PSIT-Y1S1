""" Helloooo """
def main():
    """ main function """
    text = input()
    sara = ''
    for i in text[-1::-1]:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            sara = -(text[::-1].find(i) + 1)
            alp = text[sara]
            break
    if not sara:
        return print(text)
    ans = text[:sara] + alp*4
    ans =  ans + text[sara+1:] if sara+1 else ans
    return print(ans)
main()
