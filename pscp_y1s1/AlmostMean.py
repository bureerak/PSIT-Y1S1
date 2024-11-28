""" AlmostMean """
def means(num = int(input())):
    """ return mean """
    null = [input().split("\t") for _ in range(num)]
    cal = [float(x[1]) for x in null]
    mean = sum(cal) / num
    comp, new = float('-inf'), ""
    for i in null:
        if float(comp)<float(i[1])<=mean:
            comp, new = i[1], i[0]
    print(new,comp,sep="\t")
means()
