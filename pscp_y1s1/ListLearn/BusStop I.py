""" Buss """
def fakebuss(p, n):
    """ buss goๆ """
    a_list, buss = [input().split() for _ in range(n)], []
    a_list.sort(key=lambda a : int(a[0]))
    count = 0
    for stop in a_list:
        for _ in range(buss.count(stop[0])):
            count+=1
            buss.remove(stop[0])
        lenght = len(stop)
        for i in range( 1,lenght ):
            if int(stop[i]) > int(stop[0]):
                if len(buss) >= p:
                    break
                buss.append(stop[i])
    print(count)
fakebuss(int( input() ), int( input() ))
