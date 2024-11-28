""" sock """
def main():
    """ main function """
    temp, null, ans = input(), {}, ""
    for i in temp:
        null[i] = null.get( i, 0 ) + 1
    key_null = sorted(list(null.keys()))
    for i in key_null:
        ans += (f' {i}{i}'*(null[i]//2))
    if ans:
        print(ans.strip())
        print( len(ans.split()) )
    else:
        print('None')
        print(0)
main()
