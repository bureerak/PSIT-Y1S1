""" Seeker """
def main():
    """ main function """
    text = input()+' '
    spd = ''
    res = 0
    for i in text:
        if i.isnumeric():
            spd += i
            continue
        if spd:
            res+=int(spd)
            spd=''
    print(res)
main()
