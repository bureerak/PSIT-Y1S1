""" Classify """
def classy():
    """ classify """
    null, fprint, num, cheker = [], [], [], "--"
    while True:
        inp = input()
        if inp == "END":
            break
        null+=[[inp[:2],int(inp[2:4])]]
    null.sort(key=lambda a : int(a[1]))
    null.sort(key=lambda a : int(a[0]))
    for i in null:
        if i not in fprint:
            fprint.append(i)
            num.append(null.count(i))
    for i in fprint:
        if i[0] != cheker:
            cheker=i[0]
            continue
        i[0]="--"
    for i,j in zip(fprint,num):
        print(*i,j)

classy()
