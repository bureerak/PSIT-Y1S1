""" RectangleArea """
def findlapping():
    """ x y width height """
    fst, sec = [int(x) for x in input().split()], [int(x) for x in input().split()]
    width = min(fst[0]+fst[2], sec[0]+sec[2]) - max(fst[0],sec[0])
    height = min(fst[1]+fst[3], sec[1]+sec[3]) - max(fst[1],sec[1])
    print(width*height if width*height > 0 else 'no overlapping')
findlapping()
