""" Factors """
def factor():
    """ how to fact  """
    num = int( input() )
    for _ in range(num):
        save = []
        nunsi = {}
        ans = ''
        sep = ' x '
        temp_out = findfact( int(input()), save)
        for i in temp_out:
            nunsi[i] = nunsi.get(i,0) + 1
        nunkey = nunsi.keys()
        for i in nunkey:
            ans+= f" {i}"
            ans+= '**'+f'{nunsi[i]}' if nunsi[i] > 1 else ''
        ans = ans.strip().split()
        print(sep.join(ans))

def findfact(fac, save):
    """ calculate """
    for i in range(2, fac+1):
        if not fac%i:
            save.append(i)
            if fac//i == i:
                save.append(i)
                return save
            fac = fac//i
            return findfact(fac, save)
    return save

factor()
