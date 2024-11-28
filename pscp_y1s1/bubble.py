""" Bubble """
def bubble():
    """ return step """
    path = input()[1:]
    goal = len(path)
    path += "_________"
    curr,step,impos = 0,0,False
    while goal > curr:
        des = ("o","O","|")
        if path[curr] in ("o","|"):
            step+=1
            curr+=1
        elif path[curr] == "O":
            step+=1
            able=path[curr+1:curr+4]
            if able == "   ":
                impos = True
                break
            if "O" in able and (path[curr+4] in (" ","|") or path[curr+1:curr+5] == "|"):
                des = "O"
            for i in range(3)[::-1]:
                if able[i] in des:
                    curr += i+1
                    break
        elif path[curr]==" ":
            impos=True
            break
    print(f"IMPOSSIBLE\n{goal-max(curr,step)}" if impos else f"POSSIBLE\n{step}")
bubble()
