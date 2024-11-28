""" Flatten """
import json
def main(temp:list):
    """ main function """
    ins = []
    for i in temp:
        if isinstance(i, int):
            ins.append(i)
        else:
            ins.extend(main(i))
    return ins
print(sorted(main( json.loads(input()) ),reverse=True))
