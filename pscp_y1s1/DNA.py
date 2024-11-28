""" DNA """
def same_dna(line1,line2):
    """ return longest same dna line """
    lenght_of_1, most = len(line1), ""
    check1 = bool([i for i in line1 if i not in ('A','C','G','T')])
    check2 = bool([i for i in line2 if i not in ('A','C','G','T')])
    if check1 or check2:
        return "Error"
    line1+="_"
    for i in range(lenght_of_1):
        index = i
        x = line1[index]
        while line2.find(x) != -1:
            if len(x)>len(most):
                most = x
            index+=1
            x+=line1[index]
    return most if most else "None"
print(same_dna(input(),input()))
