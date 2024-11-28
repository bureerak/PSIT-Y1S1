""" Filter """
import json
def grade():
    """ filter grade and sort student number """
    temp_in = json.loads( input() )
    criteria = float( input() )
    sc_pass = [x for x in temp_in.items() if x[1] >= criteria]
    sc_pass.sort()
    if not sc_pass:
        print('Nope')
    else:
        for i in sc_pass:
            print(i[0],f"{i[1]:.2f}",sep="\t")
grade()
