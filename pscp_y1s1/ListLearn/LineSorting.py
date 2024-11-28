""" Line Sorting """
def key_ex(num = int( input() )):
    """ function main """
    null = [input() for x in range(num)]
    null.sort(key=len)
    print(*null,sep="\n")
key_ex()
