""" Macdonald """
def isaddress():
    """ check is valid or not """
    random, checker = input().upper(), "ABCDEF.:-"
    error, test = False, len(random.replace(".","").replace("-","").replace(":",""))
    for i in random:
        if (i not in checker and not i.isnumeric()) or test != 12:
            error=True
            break
    if random[2::3] == "-----" and len(random) == 17 and not error:
        print("VALID 1")
    elif random[2::3] == ":::::" and len(random) == 17 and not error:
        print("VALID 2")
    elif random[4::5] == ".." and len(random) == 14 and not error:
        print("VALID 3")
    else:
        print("ERROR")
isaddress()
