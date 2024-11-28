""" [Midterm 2024] Scientific Notation """
def main( x = input(), notation = True):
    """ main function """
    if x.find('x') == -1:
        notation = False
    if not notation:
        if not float(x):
            return print(0)
        dot_pos = x.find('.') if x.find('.') != -1 else len(x)
        for i in x:
            if i.isnumeric() and i != '0':
                nodot = x.replace('.','')
                deci_pos = nodot.find(i) + 1
                break
        x += '.'
        check =  '0' in x[x.find('.'):]
        x = x.replace(".","")
        notion = ( x[deci_pos - 1] + "." + x[deci_pos:] )
        notion = notion.rstrip('0.') if not check else notion.rstrip('.')
        b = f'x 10^{dot_pos - deci_pos}' if dot_pos - deci_pos else ""
        print( notion, b )
    else:
        notion = float(x[:x.find(' ')]) * (10** int(x[x.find('^')+1:]))
        print(int(notion) if int(notion) == notion else notion)
main()
