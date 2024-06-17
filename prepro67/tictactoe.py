"""docstring"""
import json
brd = input()
brd = json.loads(brd)
row1 = brd[0].copy()
row2 = brd[1].copy()
row3 = brd[2].copy()

def horizon(row):
    """horizon row"""
    if row[0] == " ":
        return None
    fst = row[0]
    for i in row[1:]:
        if i != fst:
            return None
    return fst

def vertical(ro1,ro2,ro3):
    """Vertical Row"""
    for i in range(3):
        if ro1[i] == ro2[i] and ro1[i] == ro3[i] and ro1[i] in ("X","O"):
            seq = ""
            if not i:
                seq = "first"
            elif i == 1:
                seq = "second"
            elif i == 2:
                seq = "third"
            return ro1[i],seq
    return 0,0

def diag(ro1,ro2,ro3):
    """diagonal row"""
    if ro1[0]==ro2[1] and row1[0]==ro3[2] and ro1[0]!=" ":
        return ro1[0],"first diagonal row"
    if ro1[2]==ro2[1] and ro1[2]==ro3[0] and ro1[2]!=" ":
        return ro1[2],"second diagonal row"
    return 0,0

if horizon(row1):
    print(f"{horizon(row1)} player won, haha Ez!!")
    print("first horizon row")
elif horizon(row2):
    print(f"{horizon(row2)} player won, haha Ez!!")
    print("second horizon row")
elif horizon(row3):
    print(f"{horizon(row3)} player won, haha Ez!!")
    print("third horizon row")

elif vertical(row1,row2,row3) != (0,0):
    print(f"{vertical(row1,row2,row3)[0]} player won, haha Ez!!")
    print(f"{vertical(row1,row2,row3)[1]} vertical row")
elif diag(row1,row2,row3) != (0,0):
    print(f"{diag(row1,row2,row3)[0]} player won, haha Ez!!")
    print(f"{diag(row1,row2,row3)[1]}")
else:
    print("Haha Draw, 15FF")
