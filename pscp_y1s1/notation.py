""" [Midterm 2024] Scientific Notation """
def scnot(inc:str):
    """ scnotation """
    is_float = inc.find('x') == -1
    if is_float and not float(inc):
        return 0
    if not is_float:
        num = inc[:inc.find('x')-1]
        str_num = str(num)
        power = int(inc[inc.find('^')+1:])
        bef = str_num[:str_num.find('.')]
        aft = str_num[str_num.find('.')+1:]
        if power >= 0:
            aft += '0'*(power - len(aft))
            bef += aft[:power]
            aft = aft.replace(aft[:power],'',1)
            num = bef + '.' + aft if aft else bef
            return num
        bef = ('0'*(abs(power) - len(bef)) + bef) if not float(num).is_integer() else \
                ('0'*(abs(power) - len(bef) - 1) + bef)
        aft = bef[:abs(power)] + aft
        return f"0.{aft.rstrip('0')}"
    dot_pos = inc.find('.') if inc.find('.') != -1 else len(inc)
    for i in inc:
        if i not in ('0','.'):
            fst_d = inc.find(i)
            break
    b_num = len(inc[min(fst_d,dot_pos):max(fst_d,dot_pos)])
    b_num = b_num - 1 if dot_pos > fst_d else -b_num
    a_num = inc[fst_d]+'.'+inc[fst_d+1:].replace('.','')
    a_num = a_num if '0' in inc[dot_pos+1:] else a_num.rstrip('0')
    a_num = a_num[:-1] if a_num.endswith('.') else a_num
    return f"{a_num} x 10^{b_num}"

def minus(temp_in:str):
    """ minus or not function """
    if temp_in[0] != '-':
        print( scnot(temp_in) )
    else:
        print('-', scnot(temp_in[1:]), sep="")

minus(input())
