""" CuteCat CuteFox """
def main( num = int( input() ) ):
    """ dict cat and fox """
    res, cat, fox = {}, 0, 0
    for _ in range(num):
        temp_in = input()
        fspl,sspl = temp_in.split('"'), temp_in.split("'")
        res.update({fspl[1]:fspl[3]} if len(fspl)>len(sspl) else {sspl[1]:sspl[3]})

    for i,j in ( ('Garfield','Cat01'),('Fubuki','Fox01') ):
        if i not in res and j not in res.values():
            res.update( {i:j} )

    for i in res.values():
        if i[0:3] == 'Cat':
            cat+=1
        elif i[0:3] == 'Fox':
            fox+=1
    res = sorted(res.items(),key = lambda x: ( x[1][0] ,int(x[1][3:]) ) )
    print(f"Cat : {cat}\nFox : {fox}")
    for i in res:
        print(*i,sep=" : ")
main()
