""" Four Direction """
def arrow_create(hello = input()):
    """ arrow create by input """
    eye = {
        "U":["  *   "," ***  ","* * * ","  *   ","  *   "],
        "D":["  *   ","  *   ","* * * "," ***  ","  *   "],
        "L":["  *   "," *    ","***** "," *    ","  *   "],
        "R":["  *   ","   *  ","***** ","   *  ","  *   "]
    }
    for i in range(5):
        for j in hello:
            print(eye[j][i],end="")
        print()
arrow_create()
