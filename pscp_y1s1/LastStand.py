""" Last Stand """
import json
def main(null = json.loads(input())):
    """ function """
    num = [str(x)[-1] for x in null]
    print(*num,sep="\n")
main()
