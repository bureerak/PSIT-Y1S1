""" PickThem """
import json
def pick_even(null):
    """ print even """
    even = [null[i[0]] for i in enumerate(null) if not null[i[0]] % 2]
    if even:
        print(*even,sep="\n")
    else:
        print("Nope")
pick_even(json.loads( input() ))
