""" Ink """
import math
def ink():
    """ Return sec to x,y """
    s_circle = list( map( int, input().split() ))
    for _ in range(s_circle[1]):
        xy_pos = list(map( int,input().split() ))
        xy_pos = (xy_pos[0]**2 + xy_pos[1]**2) * 3.1416
        print(math.ceil(xy_pos/s_circle[0]))
ink()
